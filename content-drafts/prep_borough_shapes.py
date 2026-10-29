# Shrinks the London and New York City borough outlines (downloaded to D:/_Audio_KEXP/input/boundaries/) into one small file for the map.
# Uses only the standard library. Sources: London = radoi90/housequest-data (from ONS boundaries, Open Government Licence);
# New York City = dwillis/nyc-maps (NYC borough boundaries).
import json, math, sys

SRC = 'D:/_Audio_KEXP/input/boundaries/'
OUT = 'D:/_KEXP_Blog/src/data/borough_shapes.json'
DIGITS = 4          # about 10 m

def simplify(ring, tol):
    """Douglas-Peucker on a closed ring (lon/lat degrees), iterative."""
    pts = ring[:-1] if ring[0] == ring[-1] else ring
    n = len(pts)
    if n <= 4: return ring
    # anchor on the first point and the point farthest from it so a closed ring simplifies sensibly
    far = max(range(n), key=lambda i: (pts[i][0] - pts[0][0]) ** 2 + (pts[i][1] - pts[0][1]) ** 2)
    keep = [False] * n; keep[0] = keep[far] = True
    stack = [(0, far), (far, n)]
    def dist(p, a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        if dx == 0 and dy == 0: return math.hypot(p[0] - a[0], p[1] - a[1])
        t = max(0, min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)))
        return math.hypot(p[0] - (a[0] + t * dx), p[1] - (a[1] + t * dy))
    while stack:
        i, j = stack.pop()
        a, b = pts[i], pts[j % n]
        best, idx = 0, None
        for k in range(i + 1, j):
            d = dist(pts[k % n], a, b)
            if d > best: best, idx = d, k
        if idx is not None and best > tol:
            keep[idx % n] = True; stack += [(i, idx), (idx, j)]
    out = [pts[i] for i in range(n) if keep[i]]
    out.append(out[0])
    return out

def polys(geom):
    return [geom['coordinates']] if geom['type'] == 'Polygon' else geom['coordinates']

def area2(r):   # signed area (shoelace); negative = clockwise on a lon/lat plane
    return sum(r[i][0] * r[i + 1][1] - r[i + 1][0] * r[i][1] for i in range(len(r) - 1))

def shrink(geom, tol):
    res = []
    for poly in polys(geom):
        rings = []
        for ri, ring in enumerate(poly):
            r = simplify(ring, tol)
            r = [[round(x, DIGITS), round(y, DIGITS)] for x, y in r]
            # d3 wants exterior rings clockwise and holes counter-clockwise (the opposite of GeoJSON's own rule), or it fills the whole globe
            if (ri == 0 and area2(r) > 0) or (ri > 0 and area2(r) < 0): r.reverse()
            if len(r) >= 4: rings.append(r)
        if rings: res.append(rings)
    return {'type': 'MultiPolygon', 'coordinates': res}

feats = []
lon = json.load(open(SRC + 'london/london_boroughs.geojson', encoding='utf-8'))
for f in lon['features']:
    feats.append({'type': 'Feature', 'properties': {'city': 'London', 'borough': f['properties']['name']}, 'geometry': shrink(f['geometry'], 0.0004)})
nyc = json.load(open(SRC + 'nyc/boroughs.geojson', encoding='utf-8'))
for f in nyc['features']:
    name = f['properties']['BoroName']
    feats.append({'type': 'Feature', 'properties': {'city': 'New York City', 'borough': 'The Bronx' if name == 'Bronx' else name}, 'geometry': shrink(f['geometry'], 0.0006)})
json.dump({'type': 'FeatureCollection', 'features': feats}, open(OUT, 'w', encoding='utf-8'), separators=(',', ':'))
import os
print(len(feats), 'shapes;', os.path.getsize(OUT) // 1024, 'KB;', 'London names:', sorted(f['properties']['borough'] for f in feats if f['properties']['city'] == 'London'))
print('NYC names:', [f['properties']['borough'] for f in feats if f['properties']['city'] != 'London'])
