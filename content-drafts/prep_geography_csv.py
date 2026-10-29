# Builds src/data/geography_2001_2025.csv (one row per annual-list entry, with the artist's place), src/data/places_geocoded.csv (lat/lon per place)
# and src/data/places_population.csv (city size per place: GeoNames first, Wikipedia as a secondary source).
# Rebuilt 2026-10-27 after the location scrub (previous version: prep_geography_csv_asof_20261027.py).
import pandas as pd, json, numpy as np, re, time, unicodedata, requests, os
S = 'D:/_Audio_KEXP/output/step17/'
B = 'D:/_KEXP_Blog/src/data/'
HERE = 'D:/_KEXP_Blog/content-drafts/'
UA = {'User-Agent': 'KEXP-listener-list-research/0.1 (personal blog data project; https://digmeoutliers.com)'}
fx = lambda s: unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode().lower().strip()

w = pd.read_csv(B + 'who_is_on_the_list_2001_2025.csv')
a = pd.read_excel(S + 'dim_artist.xlsx'); loc = pd.read_excel(S + 'dim_locations.xlsx')
m = w.merge(a[['artist_id', 'location_id']], on='artist_id', how='left').merge(loc, on='location_id', how='left')
EUROPE = set('AL AD AT BY BE BA BG HR CY CZ DK EE FI FR DE GR HU IS IE IT XK LV LI LT LU MT MD MC ME NL MK NO PL PT RO RU SM RS SK SI ES SE CH UA VA'.split())
def group(cc):
    if not isinstance(cc, str): return ''
    if cc == 'US': return 'United States'
    if cc == 'GB': return 'United Kingdom'
    if cc == 'CA': return 'Canada'
    return 'Europe' if cc in EUROPE else 'Rest of world'
m['group'] = m.country_code.map(group)
def clean_borough(s):
    if not isinstance(s, str): return ''
    return s.replace('London Borough of ', '').replace('Royal Borough of ', '').strip()
out = pd.DataFrame({
    'list_year': m.list_year, 'rank': m['rank'], 'artist_id': m.artist_id, 'artist_name': m.artist_name,
    'release_group_name': m.release_group_name, 'artist_type': m.artist_type, 'artist_gender': m.artist_gender,
    'group': m.group, 'country_code': m.country_code, 'country': m.country_name,
    'region': m.state_name.where(m.state_name.notna(), ''), 'city': m.normalized_city.where(m.normalized_city.notna(), ''),
    'borough': m.location_disambiguation.map(clean_borough), 'place': m.geocode_city.where(m.geocode_city.notna(), '')})
out.to_csv(B + 'geography_2001_2025.csv', index=False, encoding='utf-8')

# ---- GeoNames index (cities with 1,000+ people)
cols = ['id', 'name', 'ascii', 'alt', 'lat', 'lon', 'fclass', 'fcode', 'cc', 'cc2', 'a1', 'a2', 'a3', 'a4', 'pop', 'elev', 'dem', 'tz', 'mod']
g = pd.read_csv('D:/_Audio_KEXP/input/geonames/cities1000.txt', sep='\t', header=None, names=cols, dtype={'a1': str}, keep_default_na=False, quoting=3)
g['pop'] = g['pop'].astype(int)
prim, alt = {}, {}
for r in g.itertuples():
    for n in {fx(r.name), fx(r.ascii)}: prim.setdefault((r.cc, n), []).append(r)
    for n in {fx(x) for x in r.alt.split(',') if x}: alt.setdefault((r.cc, n), []).append(r)
US_ABBR = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
CA_A1 = {'Alberta': '01', 'British Columbia': '02', 'Manitoba': '03', 'New Brunswick': '04', 'Newfoundland and Labrador': '05', 'Nova Scotia': '07', 'Ontario': '08', 'Prince Edward Island': '09', 'Quebec': '10', 'Saskatchewan': '11', 'Yukon': '12', 'Northwest Territories': '13', 'Nunavut': '14'}
AU_A1 = {'Australian Capital Territory': '01', 'New South Wales': '02', 'Northern Territory': '03', 'Queensland': '04', 'South Australia': '05', 'Tasmania': '06', 'Victoria': '07', 'Western Australia': '08'}
GB_A1 = {'England': 'ENG', 'Scotland': 'SCT', 'Wales': 'WLS', 'Northern Ireland': 'NIR'}
def a1_code(cc, state):
    if not isinstance(state, str) or not state: return None
    return {'US': US_ABBR, 'CA': CA_A1, 'AU': AU_A1, 'GB': GB_A1}.get(cc, {}).get(state)
def geonames_match(cc, state, city):
    code = a1_code(cc, state)
    for via, idx in (('geonames', prim), ('geonames (alternate name)', alt)):
        c = idx.get((cc, fx(city)), [])
        if not c: continue
        c1 = [x for x in c if code and x.a1 == code]
        if code and not c1: continue            # name exists in the country but in another state: do not guess
        pick = max(c1 or c, key=lambda x: x.pop)
        return pick, via, len(c1 or c)
    return None, '', 0

# ---- places (one per city; boroughs share their city's place)
P = out[out.place != ''][['place', 'country_code', 'region', 'city']].drop_duplicates('place').reset_index(drop=True)
rows = []
for r in P.itertuples():
    pick, via, n = geonames_match(r.country_code, r.region, r.city)
    rows.append(dict(place=r.place, country_code=r.country_code, region=r.region, city=r.city,
                     geonames_id=pick.id if pick else '', geonames_name=pick.name if pick else '', gn_lat=pick.lat if pick else np.nan, gn_lon=pick.lon if pick else np.nan,
                     population=pick.pop if pick and pick.pop > 0 else np.nan, pop_source=via if pick and pick.pop > 0 else '', pop_note=(f'{n} same-name places in that state/country; largest used' if pick and n > 1 else '')))
PP = pd.DataFrame(rows)
# places where the automatic match picked a different place of the same name (checked by hand)
MANUAL = {'Ashill, England, United Kingdom': dict(geonames_id='', geonames_name='', gn_lat=50.89, gn_lon=-3.30, population=np.nan, pop_source='',
          pop_note='Ashill, Devon (hamlet in Uffculme parish, Joss Stone\'s teenage home); GeoNames lists only Ashill, Norfolk; no population found')}
for pl, fix in MANUAL.items():
    for k, v in fix.items(): PP.loc[PP.place == pl, k] = v

# ---- Wikipedia as the secondary source for city size
def wiki_pop(city, region, country):
    def num(txt):
        for f in ('population_total', 'population_est', 'population_city', 'population', 'population_ref'):
            mm = re.search(r'\|\s*' + f + r'\s*=\s*([^\n]*)', txt)
            if mm:
                v = re.sub(r'<ref.*?(</ref>|/>)', '', mm.group(1), flags=re.S)
                v = re.sub(r'\{\{[^{}]*\}\}', '', v)                 # template calls hold codes (e.g. GSS=E08000009), not populations
                n = re.search(r'(\d{1,3}(?:,\d{3})+|\d{4,})', v)
                if n and not re.fullmatch(r'(18|19|20)\d\d', n.group(1)): return int(n.group(1).replace(',', ''))   # a bare year is not a population
        return None
    HINT = {'Pajala Municipality': 'Pajala'}      # page titles that differ from the place name
    tries = [HINT.get(city), f'{city}, {region}' if region else None, f'{city}, {country}', city]
    for t in [x for x in tries if x]:
        txt = None
        for attempt in range(4):                      # Wikipedia sometimes answers a burst of requests with a non-JSON throttle page
            try:
                resp = requests.get('https://en.wikipedia.org/w/api.php', params={'action': 'query', 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'titles': t, 'redirects': 1, 'format': 'json', 'formatversion': 2}, headers=UA, timeout=40)
                pg = resp.json()['query']['pages'][0]
                txt = pg['revisions'][0]['slots']['main']['content']
                break
            except Exception: time.sleep(3 * (attempt + 1))
        time.sleep(1.0)
        if txt is None: continue
        if re.search(r'\{\{\s*(disambiguation|disambig|dab)', txt, re.I): continue
        n = num(txt)
        if n: return n, pg['title']
    return None, ''
need = PP[PP.population.isna()].index
prev = pd.read_csv(B + 'places_population.csv').set_index('place') if os.path.exists(B + 'places_population.csv') else pd.DataFrame()   # reuse earlier Wikipedia answers (and earlier misses) instead of asking again
for i in need:
    r = PP.loc[i]
    if r.place in MANUAL: continue
    if r.place in prev.index and (prev.loc[r.place, 'pop_source'] == 'wikipedia' or prev.loc[r.place, 'pop_note'] == 'no population found'):
        PP.loc[i, ['population', 'pop_source', 'pop_note']] = [prev.loc[r.place, 'population'], prev.loc[r.place, 'pop_source'] if pd.notna(prev.loc[r.place, 'pop_source']) else '', prev.loc[r.place, 'pop_note']]
        continue
    country = loc[loc.country_code == r.country_code].country_name.dropna().iloc[0] if (loc.country_code == r.country_code).any() else ''
    n, title = wiki_pop(r.city, r.region, country)
    if n: PP.loc[i, ['population', 'pop_source', 'pop_note']] = [n, 'wikipedia', f'secondary source, page "{title}"; may be a district or county rather than the city']
    else: PP.loc[i, 'pop_note'] = 'no population found'

# ---- coordinates: keep the earlier lookup, GeoNames coordinates for new places, Nominatim only as a last resort
cache = json.load(open(HERE + 'geocode_cache.json', encoding='utf-8'))
def nominatim(q):
    try:
        r = requests.get('https://nominatim.openstreetmap.org/search', params={'q': q, 'format': 'json', 'limit': 1}, headers=UA, timeout=40).json()
        time.sleep(1.1)
        if r: return {'lat': float(r[0]['lat']), 'lon': float(r[0]['lon']), 'name': r[0]['display_name'], 'type': r[0].get('type', '')}
    except Exception: pass
    return None
coords, srcs = [], []
for r in PP.itertuples():
    if r.place in MANUAL: coords.append((r.gn_lat, r.gn_lon)); srcs.append('manual'); continue
    v = cache.get(r.place)
    if v and 'lat' in v and r.geonames_id != '' and abs(v['lat'] - r.gn_lat) + abs(v['lon'] - r.gn_lon) > 0.6:   # earlier lookup found a different place of the same name
        coords.append((r.gn_lat, r.gn_lon)); srcs.append('geonames'); continue
    if v and 'lat' in v: coords.append((v['lat'], v['lon'])); srcs.append(v.get('type', 'lookup')); continue
    if r.geonames_id != '' and not np.isnan(r.gn_lat): coords.append((r.gn_lat, r.gn_lon)); srcs.append('geonames'); continue
    v = nominatim(r.place)
    if v: cache[r.place] = v; coords.append((v['lat'], v['lon'])); srcs.append(v['type'] or 'lookup')
    else: coords.append((np.nan, np.nan)); srcs.append('NOT FOUND')
json.dump(cache, open(HERE + 'geocode_cache.json', 'w', encoding='utf-8'), ensure_ascii=False)
PP['lat'] = [round(c[0], 4) for c in coords]; PP['lon'] = [round(c[1], 4) for c in coords]; PP['coord_source'] = srcs
PP[PP.lat.notna()][['place', 'lat', 'lon']].assign(osm_type=[s for s, k in zip(PP.coord_source, PP.lat.notna()) if k]).to_csv(B + 'places_geocoded.csv', index=False, encoding='utf-8')
PP[['place', 'country_code', 'region', 'city', 'population', 'pop_source', 'pop_note', 'geonames_id', 'geonames_name']].to_csv(B + 'places_population.csv', index=False, encoding='utf-8')
# ---- borough points (London and New York City) for the map's borough view; looked up once, then kept in the cache
OFFICIAL_Q = {'Kensington and Chelsea': 'Royal Borough of Kensington and Chelsea', 'Greenwich': 'Royal Borough of Greenwich'}
BOX = {'London': (51.25, 51.75, -0.55, 0.35), 'New York City': (40.45, 40.95, -74.30, -73.65)}      # a result outside the city is rejected
bp = out[out.city.isin(list(BOX)) & (out.borough != '')][['city', 'borough']].drop_duplicates().sort_values(['city', 'borough'])
brows = []
for r in bp.itertuples():
    key = f'borough|{r.city}|{r.borough}'
    v = cache.get(key)
    if not v:
        q = (OFFICIAL_Q.get(r.borough, f'London Borough of {r.borough}') + ', London, England') if r.city == 'London' else f'{r.borough}, New York City, New York, USA'
        v = nominatim(q)
        if v: cache[key] = v
    s = BOX[r.city]
    if v and s[0] <= v['lat'] <= s[1] and s[2] <= v['lon'] <= s[3]: brows.append(dict(city=r.city, borough=r.borough, lat=round(v['lat'], 4), lon=round(v['lon'], 4)))
    else: print('borough not placed:', r.city, r.borough, v)
json.dump(cache, open(HERE + 'geocode_cache.json', 'w', encoding='utf-8'), ensure_ascii=False)
pd.DataFrame(brows).to_csv(B + 'borough_points.csv', index=False, encoding='utf-8')
print('boroughs placed:', len(brows), 'of', len(bp))
print(len(out), (out.group != '').sum(), 'places:', len(PP), '| located:', int(PP.lat.notna().sum()), '| with population:', int(PP.population.notna().sum()))
print('population source:', PP.pop_source.replace('', 'none').value_counts().to_dict())
print('coordinate source:', PP.coord_source.value_counts().to_dict())
print(out.group.value_counts().to_string())
