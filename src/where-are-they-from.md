---
title: Where are they from?
toc: false
head: |
  <link rel="icon" href="favicon.png" type="image/png" sizes="32x32">
  <script src="https://cdn.jsdelivr.net/npm/iframe-resizer@5.5.9/js/iframeResizer.contentWindow.min.js">
  </script>
  <script>if (window.self !== window.top) { document.documentElement.classList.add("embedded"); }</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
  <style>.embedded { --serif: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; } html.embedded body { font-size: 17px; line-height: 1.6; color: var(--dmo-fg); } .embedded main { margin-top: 0 !important; margin-bottom: 0 !important; } html.embedded main > p { letter-spacing: -0.01em; } .embedded main > p { margin: 28px 0; } .embedded main > h2 { margin-top: 56px; } .embedded main > h3 { margin-top: 44px; } .embedded .standalone-only + p { margin-top: 0; } .embedded #observablehq-footer { display: none; } p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display { max-width: 920px; } .embedded #observablehq-center { margin: 0 !important; } .embedded main > h1, .embedded .standalone-only { display: none; } .dmo-tiles { display: grid; grid-template-columns: 1fr; gap: 1.25rem; } .dmo-tile { padding: 0 0.25rem; } .dmo-tile + .dmo-tile { border-top: 1px solid #33322f; padding-top: 1.25rem; } @media (min-width: 760px) { .dmo-tiles { grid-template-columns: repeat(3, 1fr); gap: 0; } .dmo-tile { padding: 0 1.5rem; } .dmo-tile + .dmo-tile { border-top: 0; padding-top: 0; border-left: 1px solid #33322f; } } html.embedded { --dmo-fg: #15171a; --dmo-bg-solid: #ffffff; --theme-foreground: var(--dmo-fg); --theme-background: var(--dmo-bg-solid); --theme-foreground-muted: color-mix(in srgb, var(--dmo-fg) 68%, var(--dmo-bg-solid)); --theme-foreground-faint: color-mix(in srgb, var(--dmo-fg) 38%, var(--dmo-bg-solid)); --theme-foreground-fainter: color-mix(in srgb, var(--dmo-fg) 18%, var(--dmo-bg-solid)); --theme-foreground-faintest: color-mix(in srgb, var(--dmo-fg) 8%, var(--dmo-bg-solid)); } @media (prefers-color-scheme: dark) { html.embedded { --dmo-fg: #dcdcd6; --dmo-bg-solid: #15171a; } } html.embedded, html.embedded body { background: var(--dmo-bg-solid); }  .phone-note { display: none; font-size: 14px; line-height: 1.5; color: var(--theme-foreground-muted); margin: 0 0 1.25rem; padding: 0.6rem 0.9rem; border-left: 3px solid #9c57f3; } .embedded main > p.phone-note { margin: 0 0 24px; } @media (max-width: 640px) { .phone-note { display: block; } } </style>
  <script>
  (function () {
    var d = document.documentElement, embedded = window.self !== window.top;
    // match the blog page this chart sits in (its light or dark colors) once it tells us what they are
    function ok(v) { return typeof v === "string" && /^rgba?\([0-9., %\/]+\)$/.test(v); }
    window.addEventListener("message", function (e) {
      var t = e.data && e.data.dmoTheme;
      if (!t || e.source !== window.parent) return;
      if (ok(t.fg)) d.style.setProperty("--dmo-fg", t.fg);
      if (ok(t.bg)) d.style.setProperty("--dmo-bg-solid", t.bg);
    });
    if (embedded) { try { window.parent.postMessage({dmoHello: 1}, "*"); } catch (e) {} }
    // links to other sites open in a new tab; links to the blog itself replace the whole page
    function fixLinks() {
      document.querySelectorAll("a[href]").forEach(function (a) {
        try {
          var u = new URL(a.href, location.href);
          if (u.protocol.indexOf("http") !== 0) return;
          if (/(^|\.)digmeoutliers\.com$/.test(u.hostname)) { a.target = "_top"; }
          else if (u.hostname !== location.hostname) { a.target = "_blank"; a.rel = "noopener noreferrer"; }
        } catch (e) {}
      });
    }
    // inside the blog post: no extra space under the last block, so the text that follows sits one normal paragraph gap below
    var trimmed;
    function trimTail() {
      if (window.self === window.top) return;
      var kids = document.querySelectorAll("main > *");
      for (var i = kids.length - 1; i >= 0; i--) {
        if (kids[i].offsetHeight > 0) {
          if (trimmed && trimmed !== kids[i]) trimmed.style.marginBottom = "";
          kids[i].style.marginBottom = "0"; trimmed = kids[i];
          break;
        }
      }
    }
    var timer;
    function later() { clearTimeout(timer); timer = setTimeout(function () { fixLinks(); trimTail(); }, 100); }
    document.addEventListener("DOMContentLoaded", function () {
      fixLinks(); trimTail();
      new MutationObserver(later).observe(document.body, {childList: true, subtree: true});
    });
  })();
  </script>
  <script>
  // ?chart=<id>: show only that chart, scaled up (used by the Expand pop-up)
  (function () {
    var only = new URLSearchParams(location.search).get("chart");
    if (!only || !/^[a-z0-9-]+$/.test(only)) return;
    var d = document.documentElement;
    d.setAttribute("data-only", only);
    var keepSwitch = only === "map";
    var st = document.createElement("style");
    st.textContent = 'html[data-only] { --dmo-fg: #dcdcd6 !important; --dmo-bg-solid: #1a1a19 !important; }'
      + ' html[data-only], html[data-only] body { background: #1a1a19 !important; }'
      + ' html[data-only] main > *:not([data-chart="' + only + '"])' + (keepSwitch ? ':not(:has(.dmo-ctl))' : '') + ' { display: none !important; }'
      + ' html[data-only] main { max-width: none !important; margin: 0 !important; padding: 14px 18px !important; }'
      + ' html[data-only] #observablehq-center, html[data-only] #observablehq-main { margin: 0 !important; padding: 0 !important; }'
      + ' html[data-only] .card { max-width: none !important; margin: 0 !important; padding: 1rem !important; border: 0 !important; }'
      + ' html[data-only] main svg { width: 100% !important; height: auto !important; }'
      + ' html[data-only] .dmo-expand, html[data-only] #observablehq-footer, html[data-only] .phone-note { display: none !important; }'
      + ' html[data-only] .dmo-seg { margin: 0 0 0.5rem !important; }';
    document.head.appendChild(st);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { try { window.parent.postMessage({dmoCollapse: 1}, "*"); } catch (err) {} } });
  })();
  </script>
---

# Where are they from?

<div class="standalone-only" style="font-size:13px;color:var(--theme-foreground-muted);margin:0 0 1rem;"><strong>Draft</strong>: unlisted page, not part of the published blog yet.</div>

```js
import {makeTooltip, enableTap, pin, unpin} from "./components/tooltip.js";
import {addExpandButtons} from "./components/expand.js";
import * as topojson from "npm:topojson-client";
```

```js
const rows = FileAttachment("data/geography_2001_2025.csv").csv({typed: true});
const places = FileAttachment("data/places_geocoded.csv").csv({typed: true});
const popRows = FileAttachment("data/places_population.csv").csv({typed: true});
const boroughRows = FileAttachment("data/borough_points.csv").csv({typed: true});
const boroughShapes = FileAttachment("data/borough_shapes.json").json();
const worldTopo = fetch(import.meta.resolve("npm:world-atlas@2/countries-110m.json")).then((r) => r.json());
```

```js
// ---- Palette: the same brand hues as the other posts ----
const PURPLE = "#9c57f3", GOLD = "#d6b45b", TEAL = "#58cec8", BLUE = "#3d73d9", GREY = "#6b6a66";
const CARD = "background:#1a1a19;border-radius:12px;max-width:100%;height:auto;font-family:var(--sans-serif);";
const tip = makeTooltip({minWidth: 150, maxWidth: 280});
const showTip = (event, html) => tip.show(event, html);
const hideTip = (event) => tip.hide(event);
const years = d3.sort(new Set(rows.map((d) => d.list_year)));
const urlModes = (new URLSearchParams(location.search).get("mode") ?? "").split(",");

// a small switch for use with view()
function segmented(options, initial, def) {
  const el = document.createElement("div");
  el.className = "dmo-seg dmo-ctl";
  el.style.cssText = "display:inline-flex;border:1px solid #8a8985;border-radius:999px;overflow:hidden;background:#d9d8d3;margin:0.25rem 0.75rem 0.75rem 0;vertical-align:middle;font-family:var(--sans-serif);";
  const buttons = options.map(([label, value]) => {
    const b = document.createElement("button");
    b.type = "button"; b.textContent = label;
    b.style.cssText = "border:0;background:#d9d8d3;color:#5f5e5a;font-size:13px;padding:6px 16px;cursor:pointer;font-family:var(--sans-serif);white-space:nowrap;";
    b.onclick = () => { el.value = value; paint(); el.dispatchEvent(new Event("input", {bubbles: true})); };
    el.append(b);
    return [b, value];
  });
  function paint() { buttons.forEach(([b, v]) => { b.style.background = el.value === v ? "#15171a" : "#d9d8d3"; b.style.color = el.value === v ? "#ffffff" : "#5f5e5a"; b.style.fontWeight = el.value === v ? 600 : 400; }); }
  el.value = initial; paint();
  el.setValue = (v) => { el.value = v; paint(); el.dispatchEvent(new Event("input", {bubbles: true})); };
  el.reset = () => { if (def !== undefined && el.value !== def) el.setValue(def); };
  return el;
}

function statTiles(defs) {
  const wrap = document.createElement("div");
  wrap.className = "dmo-tiles";
  const card = document.createElement("div");
  card.className = "card";
  card.style.cssText = "background:#1a1a19;padding:1.75rem 1.5rem;max-width:920px;margin:0 auto;";
  card.append(wrap);
  defs.forEach((t) => {
    const tile = document.createElement("div");
    tile.className = "dmo-tile";
    const label = document.createElement("div");
    label.style.cssText = "color:#898781;font-size:12px;text-transform:uppercase;letter-spacing:0.04em;margin-bottom:0.5rem;";
    label.textContent = t.label;
    const value = document.createElement("div");
    value.style.cssText = "color:#f0efec;font-size:32px;font-weight:600;font-family:var(--sans-serif);line-height:1.1;";
    value.textContent = t.value;
    const caption = document.createElement("div");
    caption.style.cssText = "color:#c9c8c3;font-size:13px;margin-top:0.6rem;line-height:1.4;";
    caption.textContent = t.caption;
    tile.append(label, value, caption);
    wrap.append(tile);
  });
  return card;
}
```

```js
// ---- data prep: entries that have a place, and where each place is on the map ----
const placeInfo = new Map(places.map((p) => [p.place, p]));
const located = rows.filter((d) => d.group && placeInfo.has(d.place));
const unlocated = rows.length - located.length;
const era = (lo, hi) => located.filter((d) => d.list_year >= lo && d.list_year <= hi);
const shareOf = (lo, hi, test) => 100 * era(lo, hi).filter(test).length / era(lo, hi).length;
const nArtists = (r) => new Set(r.map((d) => d.artist_id)).size;
const countries = new Set(located.map((d) => d.country));

// London and New York City can be split into boroughs (the "Boroughs" view): a borough has its own point, every other place uses its city's point
const boroughPt = new Map(boroughRows.map((d) => [d.city + "|" + d.borough, d]));
const hasBorough = (d) => boroughPt.has(d.city + "|" + d.borough);
const boroughCities = new Set(boroughRows.map((d) => d.city));
const CALLOUT_CITIES = new Set(["London"]);   // too many boroughs to name inside their outlines: names go in columns beside the city, with lines to the bubbles
const ptKey = (d, level) => level === "boroughs" && hasBorough(d) ? d.city + "|" + d.borough : d.place;
const ptCoord = (key) => boroughPt.get(key) ?? placeInfo.get(key);

function placePoints(entries, level) {
  return [...d3.rollup(entries, (v) => nArtists(v), (d) => ptKey(d, level))].map(([k, n]) => ({lon: ptCoord(k).lon, lat: ptCoord(k).lat, w: n}));
}

// one bubble per place, per region, or per country (or, in the borough view, per borough or place)
function bubbles(level) {
  const keyOf = level === "cities" ? (d) => d.place : level === "boroughs" ? (d) => ptKey(d, level) : level === "regions" ? (d) => d.country + "|" + (d.region ?? "") : (d) => d.country;
  return [...d3.group(located, keyOf)].map(([key, v]) => {
    const byPlace = d3.rollup(v, (vv) => nArtists(vv), (d) => ptKey(d, level));
    let lat = 0, lon = 0, w = 0;
    for (const [pl, n] of byPlace) { const p = ptCoord(pl); lat += p.lat * n; lon += p.lon * n; w += n; }
    const first = v[0];
    const cityName = `${first.city}, ${first.region || first.country}`;
    const name = level === "cities" ? cityName : level === "boroughs" ? (hasBorough(first) ? `${first.borough}, ${first.city}` : boroughCities.has(first.city) ? `${first.city} (borough not recorded)` : cityName) : level === "regions" ? (first.region ? `${first.region}, ${first.country}` : first.country) : first.country;
    const byArtist = d3.rollups(v, (vv) => vv.length, (d) => d.artist_name).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
    return {key, name, lat: lat / w, lon: lon / w, artists: nArtists(v), albums: v.length, top: byArtist.slice(0, 3), points: placePoints(v, level), placeSet: new Set(v.map((d) => ptKey(d, level))),
      splits: level === "cities" && v.some(hasBorough) ? v[0].city : null,
      hidden: level === "boroughs" && !hasBorough(first) && boroughCities.has(first.city),   // artists in London or New York City with no borough on file are left off the borough view (a note under the map says how many)
      callout: level === "boroughs" && hasBorough(first) && CALLOUT_CITIES.has(first.city) ? first.borough : null, calloutCity: first.city};
  }).filter((d) => !d.hidden).sort((a, b) => b.artists - a.artists);
}
const cityRank = bubbles("cities");
const hometown = cityRank[0];
const cityName = (d) => d.name.split(",")[0];
const topByAlbums = d3.greatest(cityRank, (d) => d.albums);
```

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">"From" here means the place an artist is most associated with. For most artists that is where they or the band got started, as <a href="https://musicbrainz.org/" target="_top" style="color:inherit; text-decoration:underline;">MusicBrainz</a> records it. Where that was clearly off, such as a London band filed as American, or where an artist's best-known home is a different city from the one where they were born, I researched it and chose the city most tied to their music. Johnny Cash, for instance, was born in Kingsland, Arkansas, and is tied to both Memphis and Nashville; I put him in Memphis. For London and New York City I also looked up the borough. Supergroups and collaborations are a judgment call: I used editorial judgment and put each one in the city that best matches the group's musical identity, usually the home of its most prominent member or the scene it belongs to. boygenius, for example, is filed in Los Angeles, even though its members come from Los Angeles, Memphis, and Richmond; each member is filed in their own city. It is not where an artist lives now, records, or is signed. Each place is shown at its map coordinates. The state and country bubbles sit at the average position of the cities inside them, weighted by artists, so the U.S. bubble lands in the middle of the country, not on any single place.</div>
</div>

<p class="phone-note">On a phone? Tap a bubble or bar to see its details. These charts have more room on a laptop or tablet.</p>

## Every artist, on the map

Each bubble is a place. Bigger means more artists from there, and color shows how many albums each of those artists has had on a list: purple for one, up to gold for several. Start with countries, then double-click a bubble to zoom in a level, to states and regions and then to cities. In London and New York City, one more double-click goes down to the boroughs. You can also use the buttons, drag to pan, and scroll to zoom. Hover or click a bubble for details, or search for an artist or a place to see who is there.

```js
// ---- search: artists and places ----
const searchItems = (() => {
  const items = [];
  const seenArtist = new Map();
  for (const d of located) if (!seenArtist.has(d.artist_id)) seenArtist.set(d.artist_id, d);
  for (const d of seenArtist.values()) items.push({kind: "artist", label: d.artist_name, sub: `${d.city}, ${d.region || d.country}`, artistId: d.artist_id});
  const cities = new Map(), regions = new Map(), ctries = new Set();
  for (const d of located) {
    cities.set(d.place, `${d.city}, ${d.region || d.country}`);
    if (d.region) regions.set(d.country + "|" + d.region, `${d.region}, ${d.country}`);
    ctries.add(d.country);
  }
  for (const c of ctries) items.push({kind: "country", label: c, key: c});
  for (const [k, l] of regions) items.push({kind: "region", label: l, key: k});
  for (const [k, l] of cities) items.push({kind: "city", label: l, key: k});
  return items;
})();
const KIND_LABEL = {artist: "Artist", city: "City", region: "State or region", country: "Country"};
const KIND_ORDER = {country: 0, region: 1, city: 2, artist: 3};

function selectionEntries(sel) {
  if (!sel) return [];
  if (sel.kind === "artist") return located.filter((d) => d.artist_id === sel.artistId);
  if (sel.kind === "city") return located.filter((d) => d.place === sel.key);
  if (sel.kind === "region") return located.filter((d) => d.country + "|" + (d.region ?? "") === sel.key);
  return located.filter((d) => d.country === sel.key);
}

function placeSearch() {
  const container = document.createElement("div");
  container.className = "dmo-ctl";
  container.style.cssText = "position:relative;max-width:420px;margin:0.25rem 0 0.75rem;";
  const row = document.createElement("div");
  row.style.cssText = "display:flex;align-items:center;gap:8px;";
  const input = document.createElement("input");
  input.type = "text";
  input.placeholder = "Search for an artist or a place…";
  input.autocomplete = "off";
  input.style.cssText = "flex:1;box-sizing:border-box;padding:8px 10px;font-size:14px;border:1px solid var(--theme-foreground-faint);border-radius:6px;background:var(--theme-background);color:var(--theme-foreground);";
  const clearBtn = document.createElement("button");
  clearBtn.type = "button";
  clearBtn.textContent = "Clear";
  clearBtn.style.cssText = "font-size:13px;padding:7px 10px;border-radius:6px;border:1px solid var(--theme-foreground-faint);background:transparent;color:var(--theme-foreground);cursor:pointer;display:none;";
  row.append(input, clearBtn);
  const suggestions = document.createElement("div");
  suggestions.style.cssText = "position:absolute;top:100%;left:0;right:0;background:#1a1a19;border:1px solid #383835;border-radius:8px;margin-top:4px;max-height:280px;overflow-y:auto;z-index:20;display:none;";
  container.append(row, suggestions);
  let current = null;
  Object.defineProperty(container, "value", {get() { return current; }});
  function render(query) {
    suggestions.innerHTML = "";
    const q = query.trim().toLowerCase();
    if (!q) { suggestions.style.display = "none"; return; }
    const starts = (s) => s.toLowerCase().split(/[\s,]+/).some((w) => w.startsWith(q)) || s.toLowerCase().startsWith(q);
    const matches = searchItems.filter((a) => a.label.toLowerCase().includes(q))
      .sort((a, b) => (starts(b.label) - starts(a.label)) || (KIND_ORDER[a.kind] - KIND_ORDER[b.kind]) || a.label.localeCompare(b.label)).slice(0, 10);
    if (!matches.length) { suggestions.style.display = "none"; return; }
    for (const a of matches) {
      const item = document.createElement("div");
      item.style.cssText = "padding:8px 10px;cursor:pointer;color:#f0efec;font-size:14px;display:flex;justify-content:space-between;gap:10px;";
      item.innerHTML = `<span>${a.label}</span><span style="color:#898781;font-size:12px;white-space:nowrap;">${a.kind === "artist" ? a.sub : KIND_LABEL[a.kind]}</span>`;
      item.addEventListener("pointerenter", () => (item.style.background = "#2a2a27"));
      item.addEventListener("pointerleave", () => (item.style.background = "transparent"));
      item.addEventListener("mousedown", (event) => { event.preventDefault(); select(a); });
      suggestions.append(item);
    }
    suggestions.style.display = "block";
  }
  function select(a) {
    current = a;
    input.value = a.label;
    suggestions.style.display = "none";
    clearBtn.style.display = "inline-block";
    // show the map at the level that matches what was searched for
    const seg = document.querySelector(".dmo-seg");
    const want = a.kind === "country" ? "countries" : a.kind === "region" ? "regions" : "cities";
    if (seg && seg.value !== want && !(seg.value === "boroughs" && want === "cities")) seg.setValue(want);
    container.dispatchEvent(new Event("input"));
  }
  function clear() {
    if (!current && !input.value) return;
    current = null; input.value = "";
    suggestions.style.display = "none";
    clearBtn.style.display = "none";
    container.dispatchEvent(new Event("input"));
  }
  container.reset = clear;
  input.addEventListener("input", () => { if (current) { current = null; clearBtn.style.display = "none"; container.dispatchEvent(new Event("input")); } render(input.value); });
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") { const first = suggestions.firstChild; if (first) first.dispatchEvent(new MouseEvent("mousedown", {bubbles: true, cancelable: true})); }
    if (event.key === "Escape") suggestions.style.display = "none";
  });
  input.addEventListener("blur", () => setTimeout(() => (suggestions.style.display = "none"), 150));
  clearBtn.addEventListener("click", clear);
  return container;
}

const mapSelection = view(placeSearch());
```

```js
const mapLevel = view(segmented([["Countries", "countries"], ["Regions", "regions"], ["Cities", "cities"], ["Boroughs", "boroughs"]], ["cities", "regions", "countries", "boroughs"].includes(urlModes[0]) ? urlModes[0] : "countries", "countries"));
const mapColor = view(segmented([["Albums per artist", "per"], ["Total albums", "total"]], ["per", "total"].includes(urlModes[1]) ? urlModes[1] : "per", "per"));

// a second Reset, up here with the other switches: it presses the Reset button under the map (back to countries, no zoom, search cleared)
const resetTop = document.createElement("button");
resetTop.type = "button"; resetTop.textContent = "Reset"; resetTop.className = "dmo-ctl";
resetTop.style.cssText = "border:1px solid #8a8985;border-radius:999px;background:#d9d8d3;color:#5f5e5a;font-size:13px;padding:6px 16px;margin:0.25rem 0.75rem 0.75rem 0;vertical-align:middle;cursor:pointer;font-family:var(--sans-serif);white-space:nowrap;";
resetTop.onclick = () => [...document.querySelectorAll('[data-chart="map"] button')].find((b) => b.textContent === "Reset")?.click();
display(resetTop);
```

```js
// where the bulk of a set of places sits: a box around the middle of the artists (trims far-flung outliers)
function boundsOf(pts, trim = 0.03, pad = 0.12) {
  const wq = (vals, p) => {
    const s = vals.slice().sort((a, b) => a[0] - b[0]);
    const tot = d3.sum(s, (x) => x[1]);
    let acc = 0;
    for (const [v, w] of s) { acc += w; if (acc >= p * tot) return v; }
    return s[s.length - 1][0];
  };
  const lons = pts.map((p) => [p.lon, p.w]), lats = pts.map((p) => [p.lat, p.w]);
  const t = pts.length > 8 ? trim : 0;
  const [x0, y0, x1, y1] = [wq(lons, t), wq(lats, t), wq(lons, 1 - t), wq(lats, 1 - t)];
  const dx = Math.max(x1 - x0, 1.5) * pad, dy = Math.max(y1 - y0, 1) * pad;
  return [[x0 - dx, y0 - dy], [x1 + dx, y1 + dy]];
}
```

```js
function worldMap(level, colorMode, sel) {
  unpin();
  const W = 880, H = 500;
  const world = worldTopo;
  const land = topojson.feature(world, world.objects.countries);
  const feats = land.features.filter((f) => f.id !== "010");
  const projection = d3.geoNaturalEarth1().fitExtent([[10, 10], [W - 10, H - 10]], {type: "FeatureCollection", features: feats});
  const path = d3.geoPath(projection);
  const data = bubbles(level);
  const selEntries = selectionEntries(sel);
  const selPlaces = new Set(selEntries.map((d) => ptKey(d, level)));
  const isSel = (d) => !sel || [...d.placeSet].some((p) => selPlaces.has(p));
  const rmax = {cities: 24, regions: 34, countries: 48, boroughs: 16}[level];
  const maxA = d3.max(data, (d) => d.artists);
  const r0 = (d) => Math.max(2.4, rmax * Math.sqrt(d.artists / maxA));
  const colorVal = colorMode === "per" ? (d) => d.albums / d.artists : (d) => d.albums;
  const cmax = colorMode === "per" ? 3.5 : d3.quantile(data.map((d) => d.albums).sort(d3.ascending), 0.97);
  const ramp = d3.interpolateRgbBasis(["#3b2a86", "#9c57f3", "#f2cf6a"]);
  const color = d3.scaleSequential(ramp).domain([1, cmax]).clamp(true);

  const wrap = document.createElement("div");
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, H]).attr("width", W).attr("height", H).attr("style", CARD).style("touch-action", "pan-y");
  const g = svg.append("g");
  const landPaths = g.append("g").selectAll("path").data(feats).join("path").attr("d", path).attr("fill", "#2a2a2d").attr("stroke", "#76767d").attr("stroke-width", 0.6).attr("vector-effect", "non-scaling-stroke");

  // borough view: outline each London and New York City borough, and name it once you are zoomed in
  let shapeLabels = null, shapePaths = null;
  if (level === "boroughs") {
    shapePaths = g.append("g").selectAll("path").data(boroughShapes.features).join("path").attr("d", path)
      .attr("fill", "#3a3a40").attr("fill-opacity", 0.9).attr("stroke", "#a9a9b1");   // outline width is set in the zoom handler (cheaper than non-scaling-stroke)
    shapeLabels = g.append("g").attr("pointer-events", "none").selectAll("text").data(boroughShapes.features.filter((f) => !CALLOUT_CITIES.has(f.properties.city))).join("text")
      .attr("x", (f) => path.centroid(f)[0]).attr("text-anchor", "middle").attr("fill", "#b9b8b2")
      .attr("stroke", "#1a1a19").attr("paint-order", "stroke").attr("stroke-linejoin", "round").style("display", "none").text((f) => f.properties.borough);
  }

  // country names: appear as you zoom in, biggest countries first
  const labelData = feats.map((f) => {
    const polys = f.geometry.type === "Polygon" ? [f.geometry.coordinates] : f.geometry.coordinates;
    let best = polys[0], ba = 0;
    for (const p of polys) { const a = d3.geoArea({type: "Polygon", coordinates: p}); if (a > ba) { ba = a; best = p; } }
    const poly = {type: "Polygon", coordinates: best};
    const c = path.centroid(poly);
    const short = {"United States of America": "United States", "Dem. Rep. Congo": "DR Congo", "Central African Rep.": "C.A.R.", "Bosnia and Herz.": "Bosnia", "Dominican Rep.": "Dominican Rep."};
    return {name: short[f.properties.name] ?? f.properties.name, x: c[0], y: c[1], area: path.area(poly)};
  }).filter((d) => isFinite(d.x) && d.name);
  const labels = g.append("g").attr("pointer-events", "none").selectAll("text").data(labelData).join("text")
    .attr("x", (d) => d.x).attr("y", (d) => d.y).attr("text-anchor", "middle").attr("fill", "#8d8d94")
    .attr("stroke", "#1a1a19").attr("paint-order", "stroke").attr("stroke-linejoin", "round").style("display", "none").text((d) => d.name);

  const dots = g.append("g").selectAll("circle").data(data.slice().sort((a, b) => b.artists - a.artists)).join("circle")
    .attr("cx", (d) => projection([d.lon, d.lat])[0]).attr("cy", (d) => projection([d.lon, d.lat])[1])
    .attr("fill", (d) => color(colorVal(d))).attr("fill-opacity", (d) => isSel(d) ? 0.82 : 0.12)
    .attr("stroke", (d) => sel && isSel(d) ? "#ffffff" : "#f0efec").attr("stroke-opacity", (d) => !sel ? 0.55 : isSel(d) ? 1 : 0.15)
    .attr("stroke-width", (d) => sel && isSel(d) ? 1.8 : 0.8).attr("vector-effect", "non-scaling-stroke")
    .style("cursor", "pointer");
  // side labels with leader lines (London): the names stand in two columns beside the city, each joined by a line to its borough's bubble
  const calloutData = data.filter((d) => d.callout);
  const calloutBox = new Map();   // city -> [[lon, lat], [lon, lat]] corners of its outline
  for (const city of CALLOUT_CITIES) {
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const f of boroughShapes.features) if (f.properties.city === city) for (const poly of f.geometry.coordinates) for (const [x, y] of poly[0]) { x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
    calloutBox.set(city, [[x0, y0], [x1, y1]]);
  }
  const co = svg.append("g").attr("pointer-events", "none").style("display", "none");
  const coLines = co.selectAll("line").data(calloutData).join("line").attr("stroke", "#9a9aa2").attr("stroke-opacity", 0.8).attr("stroke-width", 0.8);
  const coText = co.selectAll("text").data(calloutData).join("text").attr("fill", "#d9d8d3").attr("font-size", 11).attr("dominant-baseline", "middle")
    .attr("stroke", "#1a1a19").attr("stroke-width", 3).attr("paint-order", "stroke").attr("stroke-linejoin", "round").text((d) => d.callout);
  function layoutCallouts(t) {
    const show = calloutData.length > 0 && t.k >= 40;
    co.style("display", show ? null : "none");
    if (!show) return;
    for (const city of CALLOUT_CITIES) {
      const items = calloutData.filter((d) => d.calloutCity === city).map((d) => { const p = projection([d.lon, d.lat]); return {d, x: t.applyX(p[0]), y: t.applyY(p[1])}; });
      if (!items.length) continue;
      const [[x0, y0], [x1, y1]] = calloutBox.get(city);
      const a = projection([x0, y1]), b = projection([x1, y0]);   // top-left and bottom-right corners of the outline, on screen
      const left = t.applyX(a[0]), right = t.applyX(b[0]), top = t.applyY(a[1]), bottom = t.applyY(b[1]), mid = (left + right) / 2;
      for (const side of [-1, 1]) {
        const col = items.filter((i) => (side < 0 ? i.x < mid : i.x >= mid)).sort((p, q) => p.y - q.y);
        const step = Math.max(15, col.length > 1 ? (bottom - top) / (col.length - 1) : 0);
        const first = (top + bottom) / 2 - step * (col.length - 1) / 2;
        col.forEach((i, n) => Object.assign(i.d, {_lx: side < 0 ? left - 18 : right + 18, _ly: first + n * step, _ax: i.x, _ay: i.y, _side: side}));
      }
    }
    coText.attr("x", (d) => d._lx).attr("y", (d) => d._ly).attr("text-anchor", (d) => (d._side < 0 ? "end" : "start"));
    coLines.attr("x1", (d) => d._lx + (d._side < 0 ? 4 : -4)).attr("y1", (d) => d._ly).attr("x2", (d) => d._ax).attr("y2", (d) => d._ay);
  }
  const nextLevelOf = (d) => ({countries: "regions", regions: "cities"}[level]) ?? (d.splits ? "boroughs" : undefined);   // London and New York City go one level deeper, to boroughs
  const html = (d) => `<b>${d.name}</b><br>${d.artists.toLocaleString()} artist${d.artists === 1 ? "" : "s"} &middot; ${d.albums.toLocaleString()} album${d.albums === 1 ? "" : "s"} on lists<br><span style="color:#898781">${(d.albums / d.artists).toFixed(1)} albums per artist</span><br><span style="color:#898781">${d.top.map(([n, c]) => n + (c > 1 ? ` (${c})` : "")).join(", ")}</span>${nextLevelOf(d) ? `<br><span style="color:#e4e3de;font-size:12px;font-weight:600">Double-click to zoom in${d.splits ? " to the boroughs" : ""}</span>` : ""}`;
  dots.on("pointerenter pointermove", (event, d) => tip.show(event, html(d), 14)).on("pointerleave", hideTip)
    .on("click", (event, d) => { event.stopPropagation(); pin(event, html(d)); })
    .on("dblclick", (event, d) => {
      event.stopPropagation(); event.preventDefault(); unpin(); hideTip();
      if (level === "boroughs") return;   // boroughs are the deepest layer, so a double-click does nothing more
      const nextLevel = nextLevelOf(d);
      // going into a city's boroughs: fit the whole city's outline
      const cityShape = nextLevel === "boroughs" ? (() => {
        let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
        for (const f of boroughShapes.features) if (f.properties.city === d.splits) for (const poly of f.geometry.coordinates) for (const [x, y] of poly[0]) { x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
        return [[x0, y0], [x1, y1]];
      })() : null;
      const bpts = cityShape ? [{lon: cityShape[0][0], lat: cityShape[0][1], w: 1}, {lon: cityShape[1][0], lat: cityShape[1][1], w: 1}] : d.points;
      window.__dmoFocus = {box: boundsOf(bpts), maxK: nextLevel === "regions" ? 5 : nextLevel === "boroughs" || level === "boroughs" ? 400 : 9,
        fill: nextLevel === "boroughs" && CALLOUT_CITIES.has(d.splits) ? 0.6 : 0.85};   // a city with side labels is shown smaller, to leave room for them
      if (nextLevel) document.querySelector(".dmo-seg").setValue(nextLevel); else focusNow();
    });
  svg.on("click", () => unpin());

  let k = 1;
  const zoom = d3.zoom().scaleExtent([1, 400]).translateExtent([[0, 0], [W, H]]).extent([[0, 0], [W, H]]).on("zoom", (event) => {
    k = event.transform.k;
    g.attr("transform", event.transform);
    dots.attr("r", (d) => r0(d) * Math.pow(Math.min(k, 14), 0.3) / k);   // on screen the bubble grows only slowly as you zoom in, and stops growing past 14x so boroughs stay apart
    labels.style("display", (d) => k >= 1.7 && d.area * k * k > 2600 ? null : "none").attr("font-size", 11 / k).attr("stroke-width", 3 / k);
    if (shapePaths) {
      shapePaths.attr("stroke-width", 1 / k);
      const deep = k >= 40;   // zoomed in on a city: the coarse world coastline no longer lines up, so let the borough outlines stand alone
      landPaths.attr("fill-opacity", deep ? 0 : 1).attr("stroke-opacity", deep ? 0 : 1);
    }
    if (shapeLabels) shapeLabels.style("display", k >= 40 ? null : "none").attr("y", (f) => path.centroid(f)[1] + 16 / k).attr("font-size", 10 / k).attr("stroke-width", 3 / k);
    layoutCallouts(event.transform);
    window.__dmoMapT = event.transform;
  });
  svg.call(zoom).on("dblclick.zoom", null);
  svg.call(zoom.transform, window.__dmoMapT ?? d3.zoomIdentity);

  // zoom to a box of [lon, lat] corners
  function flyTo(box, maxK = 14, fill = 0.85) {   // 14 for normal zooming; the borough view goes much deeper
    const [[x0, y0], [x1, y1]] = [projection(box[0]), projection(box[1])];
    const kk = Math.max(1, Math.min(maxK, fill / Math.max(Math.abs(x1 - x0) / W, Math.abs(y1 - y0) / H, 0.001)));
    const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    svg.transition().duration(650).call(zoom.transform, d3.zoomIdentity.translate(W / 2 - kk * cx, H / 2 - kk * cy).scale(kk));
  }
  function focusNow() { const f = window.__dmoFocus; window.__dmoFocus = null; if (f) flyTo(f.box, f.maxK, f.fill); }
  if (window.__dmoFocus) focusNow();
  else if (sel && window.__dmoSelFlown !== sel.label) {
    window.__dmoSelFlown = sel.label;
    const pts = placePoints(selEntries, level);
    const single = pts.length === 1;
    const [[a, b], [c, e]] = boundsOf(pts);
    flyTo(single ? [[a - 1.2, b - 0.8], [c + 1.2, e + 0.8]] : [[a, b], [c, e]], single ? 6 : 8);
  } else if (!sel) window.__dmoSelFlown = undefined;

  const bar = document.createElement("div");
  bar.style.cssText = "display:flex;gap:8px;flex-wrap:wrap;margin:0.9rem 0 0.25rem;justify-content:center;";
  const mkBtn = (label, fn) => {
    const b = document.createElement("button");
    b.type = "button"; b.textContent = label;
    b.style.cssText = "font-size:13px;color:#c9c8c3;background:#232321;border:1px solid #383835;border-radius:999px;padding:5px 14px;cursor:pointer;font-family:var(--sans-serif);";
    b.onclick = fn; return b;
  };
  function resetAll() {
    svg.interrupt();
    window.__dmoFocus = null; window.__dmoSelFlown = undefined;
    svg.call(zoom.transform, d3.zoomIdentity);   // also stores the reset view for the redraws below
    document.querySelectorAll(".dmo-ctl").forEach((el) => { if (el.reset) el.reset(); });
  }
  bar.append(
    mkBtn("Reset", resetAll),
    mkBtn("North America", () => flyTo([[-170, 12], [-52, 72]])),
    mkBtn("Europe", () => flyTo([[-26, 34], [42, 71]])),
    mkBtn("Australia and New Zealand", () => flyTo([[110, -48], [180, -9]])),
    mkBtn("+", () => svg.transition().duration(250).call(zoom.scaleBy, 1.7)),
    mkBtn("−", () => svg.transition().duration(250).call(zoom.scaleBy, 1 / 1.7))
  );

  // a standing hint on the map itself (not zoomed)
  const hint = {countries: "Double-click a bubble to zoom in", regions: "Double-click a bubble to zoom in",
    cities: "Double-click a bubble to zoom in. London and New York City open into boroughs."}[level];   // no hint in the borough view: there is nothing deeper to zoom to
  if (hint) {
    const hintG = svg.append("g").attr("transform", "translate(14,12)").attr("pointer-events", "none");
    hintG.append("rect").attr("width", hint.length * 7.4 + 24).attr("height", 30).attr("rx", 9).attr("fill", "#1a1a19").attr("fill-opacity", 0.88);
    hintG.append("text").attr("x", 12).attr("y", 20).attr("fill", "#e4e3de").attr("font-size", 14).text(hint);
  }

  // legend (not zoomed): size, then color
  const lg = svg.append("g").attr("transform", `translate(16,${H - 16})`).attr("pointer-events", "none");
  const ex = [Math.max(1, Math.round(maxA / 20)), Math.round(maxA / 3), maxA].filter((v, i, a) => a.indexOf(v) === i);
  let lx = 0;
  ex.forEach((v) => {
    const r = Math.max(2.4, rmax * Math.sqrt(v / maxA));
    lg.append("circle").attr("cx", lx + r).attr("cy", -r).attr("r", r).attr("fill", "none").attr("stroke", "#c9c8c3").attr("stroke-opacity", 0.7);
    lg.append("text").attr("x", lx + r).attr("y", 11).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(v);
    lx += 2 * r + 10;
  });
  lg.insert("rect", ":first-child").attr("x", -10).attr("y", -2 * rmax - 24).attr("width", lx + 6).attr("height", 2 * rmax + 44).attr("rx", 8).attr("fill", "#1a1a19").attr("fill-opacity", 0.8);
  lg.append("text").attr("x", 0).attr("y", -2 * rmax - 8).attr("fill", "#898781").attr("font-size", 10).text("Artists");
  const gid = "grad" + Math.random().toString(36).slice(2, 7);
  const grad = svg.append("defs").append("linearGradient").attr("id", gid);
  d3.range(0, 1.01, 0.25).forEach((t) => grad.append("stop").attr("offset", t).attr("stop-color", ramp(t)));
  const cg = svg.append("g").attr("transform", `translate(${W - 176},${H - 28})`).attr("pointer-events", "none");
  cg.append("rect").attr("x", -12).attr("y", -24).attr("width", 174).attr("height", 52).attr("rx", 8).attr("fill", "#1a1a19").attr("fill-opacity", 0.8);
  cg.append("rect").attr("width", 150).attr("height", 8).attr("rx", 4).attr("fill", `url(#${gid})`);
  cg.append("text").attr("x", 0).attr("y", 20).attr("fill", "#898781").attr("font-size", 10).text("1");
  cg.append("text").attr("x", 150).attr("y", 20).attr("text-anchor", "end").attr("fill", "#898781").attr("font-size", 10).text(colorMode === "per" ? "3.5+" : `${Math.round(cmax)}+`);
  cg.append("text").attr("x", 75).attr("y", -6).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(colorMode === "per" ? "Albums per artist" : "Total albums on lists");

  wrap.append(svg.node(), bar);
  if (level === "boroughs") {   // artists with no borough on file are not on this view, so say how many
    const missing = [...boroughCities].map((c) => [c, nArtists(located.filter((d) => d.city === c && !hasBorough(d)))]).filter(([, n]) => n > 0);
    if (missing.length) {
      const note = document.createElement("p");
      note.style.cssText = "font-size:12px;color:#898781;margin:0.5rem 0 0;text-align:center;";
      note.textContent = `Not shown: ${listOf(missing.map(([c, n]) => `${n} ${c} artist${n === 1 ? "" : "s"} with no borough on file`))}.`;
      wrap.append(note);
    }
  }
  return wrap;
}
```

<div class="card" data-chart="map" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
worldMap(mapLevel, mapColor, mapSelection)
```

</div>

```js
function selectionList(sel) {
  const box = document.createElement("div");
  box.style.cssText = "max-width:900px;margin:1rem auto 0;font-size:14px;color:var(--theme-foreground);";
  const muted = "color:var(--theme-foreground-muted);";
  if (!sel) { box.innerHTML = `<p style="${muted}margin:0;">Search for an artist or a place above to see who is there. Please allow a moment for zoom-in views to render.</p>`; return box; }
  const entries = selectionEntries(sel);
  if (sel.kind === "artist") {
    const rowsSorted = entries.slice().sort((a, b) => a.list_year - b.list_year);
    box.innerHTML = `<div style="font-weight:600;font-size:15px;margin-bottom:0.5rem;">${sel.label}: ${entries.length} album${entries.length === 1 ? "" : "s"} on the lists <span style="font-weight:400;${muted}">&middot; from ${sel.sub}</span></div>`;
    const t = document.createElement("table");
    t.style.cssText = "width:100%;max-width:520px;border-collapse:collapse;font-size:14px;";
    t.innerHTML = `<thead><tr>${["Year", "Rank", "Album"].map((h) => `<th style="text-align:left;padding:6px 12px 6px 0;border-bottom:1px solid var(--theme-foreground-faint);${muted}font-weight:600;">${h}</th>`).join("")}</tr></thead><tbody>${rowsSorted.map((d) => `<tr><td style="padding:6px 12px 6px 0;border-bottom:1px solid var(--theme-foreground-faintest);">${d.list_year}</td><td style="padding:6px 12px;border-bottom:1px solid var(--theme-foreground-faintest);">#${d.rank}</td><td style="padding:6px 12px;border-bottom:1px solid var(--theme-foreground-faintest);">${d.release_group_name}</td></tr>`).join("")}</tbody>`;
    box.append(t);
    return box;
  }
  const byArtist = d3.rollups(entries, (v) => v.length, (d) => d.artist_name).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
  box.innerHTML = `<div style="font-weight:600;font-size:15px;margin-bottom:0.5rem;">${sel.label}: ${byArtist.length.toLocaleString()} artist${byArtist.length === 1 ? "" : "s"}, ${entries.length.toLocaleString()} album${entries.length === 1 ? "" : "s"} on the lists</div>`;
  const list = document.createElement("div");
  list.style.cssText = "column-width:210px;column-gap:24px;line-height:1.5;";
  const LIMIT = 150;
  const draw = (all) => {
    list.innerHTML = byArtist.slice(0, all ? byArtist.length : LIMIT).map(([n, c]) => `<div style="break-inside:avoid;">${n}${c > 1 ? ` <span style="${muted}">(${c})</span>` : ""}</div>`).join("");
  };
  draw(byArtist.length <= LIMIT);
  box.append(list);
  if (byArtist.length > LIMIT) {
    const more = document.createElement("button");
    more.type = "button"; more.textContent = `Show all ${byArtist.length.toLocaleString()} artists`;
    more.style.cssText = "margin-top:0.75rem;font-size:13px;padding:6px 14px;border-radius:999px;border:1px solid var(--theme-foreground-faint);background:transparent;color:var(--theme-foreground);cursor:pointer;";
    more.onclick = () => { draw(true); more.remove(); };
    box.append(more);
  }
  const note = document.createElement("p");
  note.style.cssText = `font-size:12px;${muted}margin:0.75rem 0 0;`;
  note.textContent = "A number in parentheses is how many albums that artist has had on the lists.";
  box.append(note);
  return box;
}
```

```js
selectionList(mapSelection)
```

```js
statTiles([
  {label: "Countries represented", value: `${countries.size}`,
   caption: `Home countries of the ${nArtists(located).toLocaleString()} artists on the lists.`},
  {label: "Albums from the U.S.", value: `${shareOf(2001, 2010, (d) => d.group === "United States").toFixed(0)}% → ${shareOf(2016, 2025, (d) => d.group === "United States").toFixed(0)}%`,
   caption: "Share of list entries, 2001–2010 compared with 2016–2025."},
  {label: "Biggest hometown", value: cityName(hometown),
   caption: `Most artists of any city: ${hometown.artists}, with ${hometown.albums} albums on the lists.`}
])
```

The map is mostly two clusters of big bubbles, with a long tail of small ones. ${cityName(hometown)} is the biggest hometown by artists, ahead of ${cityName(cityRank[1])} and ${cityName(cityRank[2])}${topByAlbums.key !== hometown.key ? ` (${cityName(topByAlbums)} has more albums on the lists, ${topByAlbums.albums} to ${hometown.albums}, because its artists made the list more often)` : ""}, and the lists are overwhelmingly American, with Britain a distant second. But the U.S. share has slipped, from ${shareOf(2001, 2010, (d) => d.group === "United States").toFixed(0)}% of entries in the first decade to ${shareOf(2016, 2025, (d) => d.group === "United States").toFixed(0)}% in the last ten years.

## Interesting observations

The map shows all 25 years at once. The sections below take that picture apart: how the mix of places has changed over time, what's inside the biggest cities, which places stay, take the top spot, or arrive new, how the Northwest and Bay Area scenes have fared, and how big the hometowns are.

### Home turf, over the years

Start with the whole world, then click into a group to see what is underneath it. Each band is a place's share of every year's list, so the bands stack up to the share for the place you are in. Click a band, or its name below the chart, to go deeper: a country, then its biggest regions, then the biggest cities. The three largest places at each step are shown, and everything else is grouped as "Other."

```js
function tree() {
  const keyAt = (d, depth) => {
    if (depth === 0) return d.group;
    if (depth === 1) return d.group === "Europe" || d.group === "Rest of world" ? d.country : (d.region || d.country);
    return d.city || d.country;
  };
  return {keyAt};
}
const T = tree();
const totalByYear = d3.rollup(located, (v) => v.length, (d) => d.list_year);

function trendDrill() {
  const wrap = document.createElement("div");
  const W = 880, H = 400, m = {l: 46, r: 16, t: 14, b: 30};
  const ROOT = ["United States", "United Kingdom", "Canada", "Europe", "Rest of world"];
  const rootColors = {"United States": PURPLE, "United Kingdom": GOLD, "Canada": TEAL, "Europe": BLUE, "Rest of world": GREY};
  const palette = [PURPLE, GOLD, TEAL, BLUE];
  let path = [];

  const crumbs = document.createElement("div");
  crumbs.style.cssText = "display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin:0 0 0.6rem;font-size:13px;color:#c9c8c3;font-family:var(--sans-serif);";
  const host = document.createElement("div");
  const chips = document.createElement("div");
  chips.style.cssText = "display:flex;gap:10px;flex-wrap:wrap;margin:0.8rem 0 0.25rem;justify-content:center;";
  wrap.append(crumbs, host, chips);

  function childrenOf(p) {
    const depth = p.length;
    const pool = located.filter((d) => p.every((k, i) => T.keyAt(d, i) === k));
    const by = d3.rollups(pool, (v) => v, (d) => T.keyAt(d, depth)).sort((a, b) => b[1].length - a[1].length);
    let list = by.map(([key, v]) => ({key, v}));
    if (depth === 0) list = ROOT.map((key) => ({key, v: pool.filter((d) => d.group === key)}));
    else if (list.length > 4) {
      const top = list.slice(0, 3), rest = list.slice(3);
      list = [...top, {key: `Other (${rest.length} places)`, v: rest.flatMap((x) => x.v), other: true}];
    }
    return {pool, list, deeper: depth < 2};
  }
  function seriesFor(v) {
    const byYear = d3.rollup(v, (vv) => vv.length, (d) => d.list_year);
    return years.map((yr) => {
      const lo = yr - 1, hi = yr + 1;
      const num = d3.sum(d3.range(lo, hi + 1), (y) => byYear.get(y) ?? 0), den = d3.sum(d3.range(lo, hi + 1), (y) => totalByYear.get(y) ?? 0);
      return {yr, share: 100 * num / den, n: byYear.get(yr) ?? 0, total: totalByYear.get(yr)};
    });
  }

  function render() {
    const {pool, list, deeper} = childrenOf(path);
    crumbs.innerHTML = "";
    const crumb = (label, upTo) => {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = label;
      const last = upTo === path.length;
      b.style.cssText = `font-size:13px;color:${last ? "#1a1a19" : "#c9c8c3"};background:${last ? "#f0efec" : "#232321"};border:1px solid #383835;border-radius:999px;padding:4px 12px;cursor:${last ? "default" : "pointer"};font-family:var(--sans-serif);`;
      b.onclick = () => { if (!last) { path = path.slice(0, upTo); render(); } };
      return b;
    };
    crumbs.append(crumb("All places", 0));
    path.forEach((p, i) => { const sep = document.createElement("span"); sep.textContent = "›"; sep.style.color = "#898781"; crumbs.append(sep, crumb(p, i + 1)); });

    const colorOf = (item, i) => item.other ? GREY : (path.length === 0 ? rootColors[item.key] : palette[i % palette.length]);
    const names = list.map((it) => it.key);
    const sers = list.map((it) => seriesFor(it.v));
    const stackData = years.map((yr, yi) => Object.fromEntries([["yr", yr], ...list.map((it, i) => [it.key, sers[i][yi].share])]));
    const stack = d3.stack().keys(names)(stackData);
    const top = d3.max(stack[stack.length - 1], (d) => d[1]);
    const x = d3.scaleLinear([years[0], years[years.length - 1]], [m.l, W - m.r]);
    const y = d3.scaleLinear([0, Math.min(100, Math.ceil(top / 5) * 5 + (top > 95 ? 0 : 0))], [H - m.b, m.t]);
    const svg = d3.create("svg").attr("viewBox", [0, 0, W, H]).attr("width", W).attr("height", H).attr("style", CARD);
    y.ticks(5).forEach((v) => {
      svg.append("line").attr("x1", m.l).attr("x2", W - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : "#2a2a27");
      svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(v + "%");
    });
    [2001, 2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", x(yr)).attr("y", H - m.b + 18).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr));
    const area = d3.area().x((d, i) => x(years[i])).y0((d) => y(d[0])).y1((d) => y(d[1])).curve(d3.curveMonotoneX);
    const canDrill = (it) => deeper && !it.other && childrenOf([...path, it.key]).list.length > 0;
    stack.forEach((s, i) => {
      const it = list[i];
      svg.append("path").attr("d", area(s)).attr("fill", colorOf(it, i)).attr("fill-opacity", 0.9).attr("stroke", "#1a1a19").attr("stroke-width", 1)
        .style("cursor", canDrill(it) ? "pointer" : "default")
        .on("click", () => { if (canDrill(it)) { path = [...path, it.key]; render(); } });
    });
    // hover readout
    const cursor = svg.append("line").attr("y1", m.t).attr("y2", H - m.b).attr("stroke", "#f0efec").attr("stroke-opacity", 0.6).style("display", "none").attr("pointer-events", "none");
    svg.append("rect").attr("x", m.l).attr("y", m.t).attr("width", W - m.l - m.r).attr("height", H - m.t - m.b).attr("fill", "none").attr("pointer-events", "all")
      .on("pointermove pointerenter", (event) => {
        const yr = Math.max(years[0], Math.min(years[years.length - 1], Math.round(x.invert(d3.pointer(event, svg.node())[0]))));
        const yi = years.indexOf(yr);
        cursor.attr("x1", x(yr)).attr("x2", x(yr)).style("display", null);
        const lines = list.map((it, i) => `<span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:${colorOf(it, i)};margin-right:6px"></span>${it.key}: ${sers[i][yi].n} of ${sers[i][yi].total} (${(100 * sers[i][yi].n / sers[i][yi].total).toFixed(0)}%)`);
        tip.show(event, `<b>${yr} list</b><br>${lines.join("<br>")}`);
      })
      .on("pointerleave", (event) => { cursor.style("display", "none"); hideTip(event); });
    host.innerHTML = "";
    host.append(svg.node());
    // chips: click to drill
    chips.innerHTML = "";
    list.forEach((it, i) => {
      const b = document.createElement("button");
      b.type = "button";
      const n = it.v.length;
      b.innerHTML = `<span style="width:12px;height:12px;border-radius:3px;background:${colorOf(it, i)};display:inline-block"></span>${it.key} <span style="color:#898781">${n.toLocaleString()}</span>${canDrill(it) ? ' <span style="color:#898781">›</span>' : ""}`;
      b.style.cssText = `display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3;background:#232321;border:1px solid #383835;border-radius:999px;padding:5px 12px;cursor:${canDrill(it) ? "pointer" : "default"};font-family:var(--sans-serif);`;
      b.onclick = () => { if (canDrill(it)) { path = [...path, it.key]; render(); } };
      chips.append(b);
    });
  }
  render();
  return wrap;
}
```

<div class="card" data-chart="trend" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
trendDrill()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">The bands use a three-year average to smooth the bumps. Hover to see the actual numbers for any single year. The number next to each name is the total albums from that place across all 25 lists.</p>

```js
const cityShare = (lo, hi, city) => shareOf(lo, hi, (d) => d.city === city);
statTiles([
  {label: "London's share of the list", value: `${cityShare(2001, 2010, "London").toFixed(0)}% → ${cityShare(2016, 2025, "London").toFixed(0)}%`,
   caption: "2001–2010 compared with 2016–2025. London doubled its share."},
  {label: "Seattle's share of the list", value: `${cityShare(2001, 2010, "Seattle").toFixed(0)}% → ${cityShare(2016, 2025, "Seattle").toFixed(0)}%`,
   caption: "The same two periods. KEXP's hometown barely moved."},
  {label: "Beyond the U.S., U.K., and Canada", value: `${shareOf(2001, 2010, (d) => d.group === "Europe" || d.group === "Rest of world").toFixed(0)}% → ${shareOf(2016, 2025, (d) => d.group === "Europe" || d.group === "Rest of world").toFixed(0)}%`,
   caption: "Share of entries from everywhere else, the same two periods."}
])
```

Two stories stand out. The first is that KEXP's hometown held steady: Seattle supplied about a tenth of the entries, ${shareOf(2001, 2010, (d) => d.city === "Seattle").toFixed(0)}% in 2001–2010 and ${shareOf(2016, 2025, (d) => d.city === "Seattle").toFixed(0)}% in 2016–2025. The second is that the growth is happening elsewhere, in London and in the long tail of countries outside the U.S., U.K., and Canada. The U.S. share fell from ${shareOf(2001, 2010, (d) => d.group === "United States").toFixed(0)}% to ${shareOf(2016, 2025, (d) => d.group === "United States").toFixed(0)}%, and the U.K. and the countries beyond the U.S., U.K., and Canada picked up the difference.

### Inside the biggest cities

Two cities have a borough on file for most of their artists: New York City and London. Each bar below is the number of artists from that part of town. Where no borough is recorded, the artist is counted under "Not specified."

```js
function boroughBars() {
  const cities = [["New York City", "New York City's boroughs"], ["London", "London's boroughs"]];
  const W = 880, rowH = 24, m = {l: 210, r: 120, t: 26, b: 8}, headH = 30, maxRows = 8;
  const panels = cities.map(([city, title]) => {
    const pool = located.filter((d) => d.city === city);
    const by = d3.rollups(pool, (v) => ({n: nArtists(v), top: d3.rollups(v, (vv) => vv.length, (d) => d.artist_name).sort((a, b) => b[1] - a[1]).slice(0, 3).map((x) => x[0])}), (d) => d.borough || "Not specified");
    const named = by.filter(([k]) => k !== "Not specified").sort((a, b) => b[1].n - a[1].n);
    const none = by.find(([k]) => k === "Not specified");
    const rowsList = [...named.slice(0, maxRows - 1), ...(named.length > maxRows - 1 ? [["Other named places", {n: d3.sum(named.slice(maxRows - 1), (x) => x[1].n), top: []}]] : []), ...(none ? [none] : [])];
    return {city, title, rowsList, total: nArtists(pool)};
  });
  const height = m.t + m.b + d3.sum(panels, (p) => headH + p.rowsList.length * rowH + 14);
  const xmax = d3.max(panels, (p) => d3.max(p.rowsList, (r) => r[1].n));
  const x = d3.scaleLinear([0, xmax], [0, W - m.l - m.r]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, height]).attr("width", W).attr("height", height).attr("style", CARD);
  let top = m.t - 8;
  const tapPts = [];
  panels.forEach((p) => {
    svg.append("text").attr("x", 20).attr("y", top + 16).attr("fill", "#f0efec").attr("font-size", 14).attr("font-weight", 600).text(p.title);
    svg.append("text").attr("x", 20 + 8 + p.title.length * 8.2).attr("y", top + 16).attr("fill", "#898781").attr("font-size", 12).text(`${p.total} artists`);
    const g = svg.append("g").attr("transform", `translate(${m.l},${top + headH})`);
    p.rowsList.forEach(([name, v], i) => {
      const cy = i * rowH + rowH / 2;
      const isNone = name === "Not specified", isOther = name === "Other named places";
      g.append("text").attr("x", -12).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", isNone || isOther ? "#898781" : "#c9c8c3").attr("font-size", 12).text(name);
      const html = `<b>${name}</b><br>${v.n} artist${v.n === 1 ? "" : "s"}${v.top.length ? `<br><span style="color:#898781">${v.top.join(", ")}</span>` : ""}`;
      g.append("rect").attr("x", 0).attr("y", cy - 8).attr("width", Math.max(2, x(v.n))).attr("height", 16).attr("rx", 3).attr("fill", isNone ? GREY : isOther ? "#8a7bb0" : PURPLE)
        .on("pointerenter pointermove", (event) => showTip(event, html)).on("pointerleave", hideTip);
      tapPts.push({x: m.l + x(v.n) / 2, y: top + headH + cy, html});
      g.append("text").attr("x", x(v.n) + 8).attr("y", cy).attr("dominant-baseline", "middle").attr("fill", "#f0efec").attr("font-size", 12).attr("pointer-events", "none").text(v.n);
    });
    top += headH + p.rowsList.length * rowH + 14;
  });
  enableTap(svg, tip, tapPts, 24);
  return svg.node();
}
```

<div class="card" data-chart="boroughs" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
boroughBars()
```

</div>

```js
const nyc = located.filter((d) => d.city === "New York City"), ldn = located.filter((d) => d.city === "London");
const boroughArtists = (pool, name) => nArtists(pool.filter((d) => d.borough === name));
const londonBoroughs = d3.rollups(ldn.filter((d) => d.borough), (v) => nArtists(v), (d) => d.borough).sort((a, b) => b[1] - a[1]);
const la = located.filter((d) => d.city === "Los Angeles"), laTotal = nArtists(la), laNamed = nArtists(la.filter((d) => d.borough));
```

```js
statTiles([
  {label: "Brooklyn", value: `${boroughArtists(nyc, "Brooklyn")}`,
   caption: `Artists from Brooklyn, out of ${nArtists(nyc)} from New York City. Manhattan has ${boroughArtists(nyc, "Manhattan")}.`},
  {label: "London, borough on file", value: `${nArtists(ldn.filter((d) => d.borough))} of ${nArtists(ldn)}`,
   caption: "London artists with a borough on file, from MusicBrainz or my own research. The rest are counted just as London."},
  {label: "Cities with one artist", value: `${bubbles("cities").filter((d) => d.artists === 1).length}`,
   caption: `Of ${bubbles("cities").length} places, the number that have exactly one artist on the lists.`}
])
```

Brooklyn alone has nearly three times as many artists as Manhattan. London's artists are spread over more boroughs, led by ${londonBoroughs[0][0]} with ${londonBoroughs[0][1]} and ${londonBoroughs[1][0]} with ${londonBoroughs[1][1]}. Los Angeles has far less detail: neighborhoods like Silver Lake and Hollywood are named for only ${laNamed} of its ${laTotal} artists, so they didn't get a chart.

### Risers, fallers, and new arrivals

Zooming out from any one city, three more numbers sum up how the map has shifted between the first decade of lists and the last ten years.

```js
const cKey = (d) => `${d.city}, ${d.region || d.country}`;
const nFirst = era(2001, 2010).length, nLast = era(2016, 2025).length;
const cityStats = [...d3.group(located, cKey)].map(([k, v]) => {
  const a = v.filter((d) => d.list_year <= 2010).length, c = v.filter((d) => d.list_year >= 2016).length;
  const sa = 100 * a / nFirst, sc = 100 * c / nLast;
  return {k, name: k.split(",")[0], all: v.length, sa, sc, chg: sc - sa, ratio: sa > 0 ? sc / sa : Infinity};
});
const grower = d3.greatest(cityStats, (x) => x.chg), faller = d3.least(cityStats, (x) => x.chg);
const nextFallers = cityStats.slice().sort((a, b) => a.chg - b.chg).slice(1, 3);
const relGrower = d3.greatest(cityStats.filter((x) => x.all >= 15), (x) => x.ratio);
const firstYearOf = d3.rollup(located, (v) => d3.min(v, (d) => d.list_year), (d) => d.country);
const newcomers = [...firstYearOf].filter(([c, y]) => y >= 2020).sort((a, b) => a[1] - b[1] || a[0].localeCompare(b[0]));
const perList = d3.rollup(located, (v) => new Set(v.map((d) => d.country)).size, (d) => d.list_year);
const perListRange = (lo, hi) => d3.extent(d3.range(lo, hi + 1), (y) => perList.get(y));
```

```js
statTiles([
  {label: "Fastest-growing city", value: grower.name,
   caption: `From ${grower.sa.toFixed(0)}% of the list in 2001–2010 to ${grower.sc.toFixed(0)}% in 2016–2025, a gain of ${grower.chg.toFixed(0)} points.`},
  {label: "Fastest-declining city", value: faller.name,
   caption: `From ${faller.sa.toFixed(0)}% to ${faller.sc.toFixed(0)}%, a drop of ${Math.abs(faller.chg).toFixed(0)} points. ${nextFallers.map((x) => x.name).join(" and ")} slipped the most after it.`},
  {label: "New countries since 2020", value: `${newcomers.length}`,
   caption: `First-time home countries: ${newcomers.map(([c]) => c).join(", ")}.`}
])
```

Growth and decline here are measured as a city's share of the whole list, so they show who gained room and who lost it. ${grower.name} gained the most, ${grower.chg.toFixed(0)} points, and ${faller.name} lost the most, ${Math.abs(faller.chg).toFixed(0)} points. In relative terms, ${relGrower.name} grew fastest: its share went from ${relGrower.sa.toFixed(1)}% to ${relGrower.sc.toFixed(1)}%, more than ${Math.floor(relGrower.ratio)} times as large. The cities that faded are mostly ones that were once regulars. The newcomers are a different kind of change: the number of home countries on a single list was ${perListRange(2001, 2010)[0]} to ${perListRange(2001, 2010)[1]} in the 2000s and has been ${perListRange(2022, 2025)[0]} to ${perListRange(2022, 2025)[1]} in the last four years. Most of the newcomers each have one or two albums, but together they are why the map has more small dots at the edges than it used to. (Puerto Rico counts as its own country here because that is how MusicBrainz files it.)

```js
const unlocatedNames = [...new Set(rows.filter((d) => !(d.group && placeInfo.has(d.place))).map((d) => d.artist_name))];
// KEXP's own regional shows define "local": Audioasis takes music from WA, OR, ID, AK and BC; Vinelands covers the Bay Area and, more widely, Northern California
const NW_STATES = new Set(["Washington", "Oregon", "Idaho", "Alaska"]);
const isNW = (d) => (d.country === "United States" && NW_STATES.has(d.region)) || (d.country === "Canada" && d.region === "British Columbia");
const BAY = new Set(["San Francisco", "Oakland", "Berkeley", "San Jose", "Alameda", "Richmond", "El Sobrante", "Santa Rosa", "Palo Alto", "Woodside", "Walnut Creek", "Vallejo",
  "Sacramento", "Santa Cruz", "Chico", "Modesto", "Stockton"]);
const isBay = (d) => d.region === "California" && BAY.has(d.city);
const bayRecent = era(2024, 2025).filter(isBay);
const newcomerAlbums = located.filter((d) => newcomers.some(([c]) => c === d.country));
```

Something outside the data may be part of this story. KEXP has region-focused shows, including Wo' Pop, El Sonido, and, since September 2023, The Continent and Eastern Echoes. I checked the play data for the artists behind the new countries (the ${newcomerAlbums.length} albums include Songhoy Blues, Mdou Moctar, Altın Gün, Liraz, and Bad Bunny), and those shows account for only a small slice of their airplay. Most of it came on KEXP's general shows. A few artists did lean on the regional programming, Liraz most of all, but The Continent and Eastern Echoes began after several of the newcomers had already arrived. So the programming may have helped some artists find an audience, but it does not explain the new countries on its own.

### Staying power, top spots, and new arrivals

Three more ways to look at places across all ${years.length} lists: which ones are always there, which ones have produced the #1 album, and how often a brand-new hometown shows up.

```js
// ---- staying power: which places are on every list, who takes the top spot, and when each place first appears ----
const placeName = new Map(located.map((d) => [d.place, `${d.city}, ${d.region || d.country}`]));
const placeCity = (pl) => placeName.get(pl).split(",")[0];
const entriesAt = d3.group(located, (d) => d.place, (d) => d.list_year);
const listsOn = [...entriesAt].map(([pl, m]) => ({place: pl, name: placeName.get(pl), city: placeCity(pl), by: new Map([...m].map(([y, v]) => [y, v.length])), lists: m.size, albums: d3.sum([...m.values()], (v) => v.length)}))
  .sort((a, b) => b.lists - a.lists || b.albums - a.albums);
const onEvery = listsOn.filter((d) => d.lists === years.length);
const firstYear = new Map(listsOn.map((d) => [d.place, d3.min(d.by.keys())]));
const newByYear = d3.group([...firstYear], ([, y]) => y);
const newSince = (yr) => [...firstYear].filter(([, y]) => y >= yr).length;
const namesAt = (pl, yr) => [...new Set((entriesAt.get(pl)?.get(yr) ?? []).map((d) => d.artist_name))].slice(0, 4).join(", ");
const ones = located.filter((d) => d.rank === 1);
const entryShare = d3.rollup(located, (v) => v.length / located.length, (d) => d.place);
const onesBy = [...d3.group(ones, (d) => d.place)].map(([pl, v]) => {
  const byArtist = d3.rollups(v, (vv) => vv.length, (d) => d.artist_name).sort((a, b) => b[1] - a[1]);
  return {place: pl, name: placeName.get(pl), city: placeCity(pl), n: v.length, expected: years.length * entryShare.get(pl), artists: byArtist.length, topArtist: byArtist[0][0], list: v.slice().sort((a, b) => a.list_year - b.list_year)};
});
const onesRows = (() => {
  const have = new Set(onesBy.map((d) => d.place));
  const extra = [...entryShare].sort((a, b) => b[1] - a[1]).slice(0, 6).map(([pl]) => pl).filter((pl) => !have.has(pl))
    .map((pl) => ({place: pl, name: placeName.get(pl), city: placeCity(pl), n: 0, expected: years.length * entryShare.get(pl), artists: 0, topArtist: "", list: []}));
  return [...onesBy, ...extra].sort((a, b) => b.n - a.n || b.expected - a.expected);
})();
const seattleOnes = onesRows.find((d) => d.city === "Seattle"), nycOnes = onesRows.find((d) => d.city === "New York City");
const lastYear = years[years.length - 1];
```

```js
statTiles([
  {label: `On all ${years.length} lists`, value: `${onEvery.length}`,
   caption: `${listOf(onEvery.map((d) => d.city))}. At the other end, ${listsOn.filter((d) => d.lists === 1).length} of the ${listsOn.length} places appear on just one list.`},
  {label: "Seattle's #1 albums", value: `${seattleOnes.n} of ${years.length}`,
   caption: `Seattle has ${(100 * entryShare.get(seattleOnes.place)).toFixed(0)}% of all entries but ${(100 * seattleOnes.n / years.length).toFixed(0)}% of the #1 albums.`},
  {label: "New hometowns since 2016", value: `${newSince(2016)}`,
   caption: `Places that had never been on a list before, out of ${listsOn.length} in all.`}
])
```

Each row in the first chart is a place and each square is one list. The brighter the square, the more albums from that place on that list.

```js
function staysChart() {
  const rowsL = listsOn.slice(0, 15);
  const W = 880, rowH = 25, m = {l: 215, r: 80, t: 28, b: 10};
  const cw = (W - m.l - m.r) / years.length, H = m.t + rowsL.length * rowH + m.b;
  const color = d3.scaleSequential(d3.interpolateRgbBasis(["#3b2a86", "#9c57f3", "#f2cf6a"])).domain([1, 8]).clamp(true);
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, H]).attr("width", W).attr("height", H).attr("style", CARD);
  [2001, 2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", m.l + (years.indexOf(yr) + 0.5) * cw).attr("y", 18).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr));
  const tapPts = [];
  const htmlFor = (d, yr, n) => `<b>${d.name}</b><br>${yr} list: ${n ? `${n} album${n === 1 ? "" : "s"}` : "no albums"}${n ? `<br><span style="color:#898781">${namesAt(d.place, yr)}</span>` : ""}`;
  rowsL.forEach((d, i) => {
    const y = m.t + i * rowH;
    svg.append("text").attr("x", m.l - 10).attr("y", y + rowH / 2 - 2).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 12).text(d.name);
    svg.append("text").attr("x", W - m.r + 10).attr("y", y + rowH / 2 - 2).attr("dominant-baseline", "middle").attr("fill", d.lists === years.length ? "#f0efec" : "#898781").attr("font-size", 12).text(`${d.lists} of ${years.length}`);
    years.forEach((yr, j) => {
      const n = d.by.get(yr) ?? 0, html = htmlFor(d, yr, n);
      svg.append("rect").attr("x", m.l + j * cw + 1).attr("y", y).attr("width", cw - 2).attr("height", rowH - 5).attr("rx", 3)
        .attr("fill", n ? color(n) : "#232321").attr("stroke", n ? "none" : "#2f2f2c")
        .on("pointerenter pointermove", (event) => showTip(event, html)).on("pointerleave", hideTip);
      tapPts.push({x: m.l + (j + 0.5) * cw, y: y + (rowH - 5) / 2, html});
    });
  });
  enableTap(svg, tip, tapPts, 14);
  return svg.node();
}
```

<div class="card" data-chart="stays" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
staysChart()
```

</div>

Albums from ${onEvery.length} places appear on every list: ${listOf(onEvery.map((d) => d.city))}. The next group misses a few years: ${listOf(listsOn.filter((d) => d.lists < years.length).slice(0, 4).map((d) => `${d.city} (${d.lists} of ${years.length})`))}.

The top spot is harder to win. In the second chart, each bar is the number of #1 albums from a place, and the gold marker is how many it would have if the #1 albums followed each place's share of all list entries.

```js
function numberOnesBars() {
  const W = 880, rowH = 26, m = {l: 215, r: 110, t: 26, b: 8};
  const height = m.t + m.b + onesRows.length * rowH;
  const x = d3.scaleLinear([0, Math.ceil(d3.max(onesRows, (d) => Math.max(d.n, d.expected)))], [0, W - m.l - m.r]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, height]).attr("width", W).attr("height", height).attr("style", CARD);
  svg.append("text").attr("x", 20).attr("y", 18).attr("fill", "#898781").attr("font-size", 12).text("#1 albums, 2001 to " + lastYear);
  svg.append("circle").attr("cx", W - 200).attr("cy", 14).attr("r", 5).attr("fill", GOLD);
  svg.append("text").attr("x", W - 190).attr("y", 18).attr("fill", "#898781").attr("font-size", 12).text("expected from its share of entries");
  const tapPts = [];
  onesRows.forEach((d, i) => {
    const cy = m.t + i * rowH + rowH / 2;
    const html = `<b>${d.name}</b><br>${d.n} #1 album${d.n === 1 ? "" : "s"}, about ${d.expected.toFixed(1)} expected${d.list.length ? `<br><span style="color:#898781">${d.list.map((e) => `${e.list_year}: ${e.artist_name}`).join("<br>")}</span>` : ""}`;
    svg.append("text").attr("x", m.l - 12).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", d.n ? "#c9c8c3" : "#898781").attr("font-size", 12).text(d.name);
    if (d.n) svg.append("rect").attr("x", m.l).attr("y", cy - 8).attr("width", x(d.n)).attr("height", 16).attr("rx", 3).attr("fill", PURPLE)
      .on("pointerenter pointermove", (event) => showTip(event, html)).on("pointerleave", hideTip);
    svg.append("circle").attr("cx", m.l + x(d.expected)).attr("cy", cy).attr("r", 5).attr("fill", GOLD).attr("stroke", "#1a1a19").attr("stroke-width", 1.5)
      .on("pointerenter pointermove", (event) => showTip(event, html)).on("pointerleave", hideTip);
    svg.append("text").attr("x", W - m.r + 12).attr("y", cy).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 12).attr("pointer-events", "none")
      .text(d.n ? `${d.n} · ${d.artists} artist${d.artists === 1 ? "" : "s"}` : "none");
    tapPts.push({x: m.l + x(Math.max(d.n, d.expected)) / 2, y: cy, html});
  });
  enableTap(svg, tip, tapPts, 24);
  return svg.node();
}
```

<div class="card" data-chart="top-spot" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
numberOnesBars()
```

</div>

```js
const oneBand = onesBy.filter((d) => d.n >= 2 && d.artists === 1).sort((a, b) => b.n - a.n);
```

The ${years.length} #1 albums came from ${new Set(ones.map((d) => d.artist_id)).size} different artists in ${onesBy.length} places. Seattle has ${seattleOnes.n}, against about ${seattleOnes.expected.toFixed(1)} if #1s followed share of entries; New York City has ${nycOnes.n} against ${nycOnes.expected.toFixed(1)}. Several places rest on a single band: ${listOf(oneBand.map((d) => `${d.city} (${d.topArtist})`))}. With only ${years.length} #1 albums, one more or less changes a place's count, so read this loosely.

Last, how often does a place show up for the first time? In the third chart, each bar is the number of places that appeared on a list for the first time that year. The first list is left out, since every place on it was new.

```js
function newPlacesBars() {
  const yrs = years.slice(1);
  const W = 880, H = 300, m = {l: 46, r: 16, t: 16, b: 30};
  const counts = yrs.map((yr) => (newByYear.get(yr) ?? []).length);
  const x = d3.scaleBand(yrs, [m.l, W - m.r]).padding(0.25);
  const y = d3.scaleLinear([0, d3.max(counts)], [H - m.b, m.t]).nice();
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, H]).attr("width", W).attr("height", H).attr("style", CARD);
  y.ticks(5).forEach((v) => {
    svg.append("line").attr("x1", m.l).attr("x2", W - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : "#2a2a27");
    svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(v);
  });
  [2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", x(yr) + x.bandwidth() / 2).attr("y", H - m.b + 18).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr));
  const tapPts = [];
  yrs.forEach((yr, i) => {
    const places = (newByYear.get(yr) ?? []).map(([pl]) => placeCity(pl));
    const html = `<b>${yr} list</b><br>${counts[i]} new place${counts[i] === 1 ? "" : "s"}${places.length ? `<br><span style="color:#898781">${places.slice(0, 8).join(", ")}${places.length > 8 ? `, and ${places.length - 8} more` : ""}</span>` : ""}`;
    svg.append("rect").attr("x", x(yr)).attr("y", y(counts[i])).attr("width", x.bandwidth()).attr("height", y(0) - y(counts[i])).attr("rx", 2).attr("fill", PURPLE)
      .on("pointerenter pointermove", (event) => showTip(event, html)).on("pointerleave", hideTip);
    tapPts.push({x: x(yr) + x.bandwidth() / 2, y: (y(counts[i]) + y(0)) / 2, html});
  });
  enableTap(svg, tip, tapPts, 18);
  return svg.node();
}
```

<div class="card" data-chart="new-places" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
newPlacesBars()
```

</div>

The pace slowed as the map filled in, but it never stopped: ${newSince(2016)} of the ${listsOn.length} places appeared for the first time in the last ten years, about ${(newSince(2016) / 10).toFixed(1)} a year. The ${lastYear} list added ${listOf((newByYear.get(lastYear) ?? []).map(([pl]) => placeCity(pl)))}.

### Two local scenes

KEXP has two shows built around local music, and each defines its region. Audioasis, from Seattle, takes submissions from Washington, Oregon, Idaho, Alaska, and British Columbia. Vinelands, from the Bay Area, covers San Francisco, Oakland, Berkeley, and the cities around them, and KEXP also names Northern California more widely. In the chart, the Bay Area means those core cities plus Northern California out to Sacramento, Modesto, and Stockton. Here is each region's share of every year's list. The two panels have different scales, because the Northwest is several times bigger than the Bay Area.

```js
function localTrend() {
  const W = 880, H = 500, m = {l: 46, r: 16, t: 12, b: 30}, gap = 40;
  const ph = (H - m.t - m.b - gap) / 2;
  const panels = [
    {name: "Northwest", sub: "Washington, Oregon, Idaho, Alaska, British Columbia", test: isNW, color: PURPLE, ymax: 35, step: 10},
    {name: "Bay Area and Northern California", sub: "KEXP's Vinelands region, out to Sacramento", test: isBay, color: GOLD, ymax: 10, step: 2}
  ];
  const rowsFor = (test) => {
    const by = d3.rollup(located.filter(test), (v) => v.length, (d) => d.list_year);
    return years.map((yr) => {
      const span = [yr - 1, yr, yr + 1];
      const n = by.get(yr) ?? 0, total = totalByYear.get(yr);
      return {yr, n, total, pct: 100 * n / total, avg: 100 * d3.sum(span, (y) => by.get(y) ?? 0) / d3.sum(span, (y) => totalByYear.get(y) ?? 0)};
    });
  };
  const data = panels.map((p) => rowsFor(p.test));
  const x = d3.scaleLinear([2000.5, 2025.5], [m.l, W - m.r]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, H]).attr("width", W).attr("height", H).attr("style", CARD);
  const top = (i) => m.t + i * (ph + gap);
  const ys = panels.map((p, i) => d3.scaleLinear([0, p.ymax], [top(i) + ph, top(i)]));
  // KEXP's San Francisco broadcasts began in March 2024, so the 2024 and 2025 lists are the first that follow
  const bandX0 = x(2023.5), bandX1 = x(2025.5);
  panels.forEach((p, i) => {
    const y = ys[i];
    svg.append("rect").attr("x", bandX0).attr("width", bandX1 - bandX0).attr("y", top(i)).attr("height", ph).attr("fill", TEAL).attr("fill-opacity", 0.14);
    d3.range(0, p.ymax + 0.1, p.step).forEach((v) => {
      svg.append("line").attr("x1", m.l).attr("x2", W - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : "#2a2a27");
      svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(v + "%");
    });
    svg.append("text").attr("x", m.l + 8).attr("y", top(i) + 14).attr("fill", p.color).attr("font-size", 13).attr("font-weight", 600).text(p.name);
    svg.append("text").attr("x", m.l + 8).attr("y", top(i) + 30).attr("fill", "#898781").attr("font-size", 11).text(p.sub);
    svg.append("path").attr("d", d3.line().x((d) => x(d.yr)).y((d) => y(d.avg)).curve(d3.curveMonotoneX)(data[i])).attr("fill", "none").attr("stroke", p.color).attr("stroke-width", 2.5);
    svg.append("g").selectAll("circle").data(data[i]).join("circle").attr("cx", (d) => x(d.yr)).attr("cy", (d) => y(d.pct)).attr("r", 2.6).attr("fill", p.color).attr("fill-opacity", 0.5);
  });
  [2001, 2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", x(yr)).attr("y", H - m.b + 18).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr));
  // label for the band, in the Bay Area panel
  const lab = svg.append("text").attr("x", bandX0 - 8).attr("y", top(1) + 14).attr("text-anchor", "end").attr("fill", TEAL).attr("font-size", 11);
  lab.append("tspan").attr("x", bandX0 - 8).text("KEXP on the air in San Francisco");
  lab.append("tspan").attr("x", bandX0 - 8).attr("dy", 14).text("from March 2024 (KEXC 92.7 FM)");
  // hover readout across both panels
  const cursor = svg.append("line").attr("y1", m.t).attr("y2", H - m.b).attr("stroke", "#f0efec").attr("stroke-opacity", 0.6).style("display", "none").attr("pointer-events", "none");
  svg.append("rect").attr("x", m.l).attr("y", m.t).attr("width", W - m.l - m.r).attr("height", H - m.t - m.b).attr("fill", "none").attr("pointer-events", "all")
    .on("pointermove pointerenter", (event) => {
      const yr = Math.max(years[0], Math.min(years[years.length - 1], Math.round(x.invert(d3.pointer(event, svg.node())[0]))));
      const yi = years.indexOf(yr);
      cursor.attr("x1", x(yr)).attr("x2", x(yr)).style("display", null);
      const line = (p, i) => `<span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:${p.color};margin-right:6px"></span>${p.name}: ${data[i][yi].n} of ${data[i][yi].total} (${data[i][yi].pct.toFixed(0)}%)`;
      tip.show(event, `<b>${yr} list</b><br>${panels.map(line).join("<br>")}`);
    })
    .on("pointerleave", (event) => { cursor.style("display", "none"); hideTip(event); });
  return svg.node();
}
```

<div class="card" data-chart="local" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
localTrend()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Dots are each year's actual share; the line is a three-year average. The teal band marks the 2024 and 2025 lists, the first two after KEXP began broadcasting in San Francisco. A year's share is the share of that year's list, and the lists were 90 to 91 albums long until 2024, when they grew to 100.</p>

```js
const nwShare = (lo, hi) => shareOf(lo, hi, isNW), bayShare = (lo, hi) => shareOf(lo, hi, isBay);
const nwYears = years.map((yr) => ({yr, pct: shareOf(yr, yr, isNW)}));
const nwLow = d3.least(nwYears, (d) => d.pct), nwHigh = d3.greatest(nwYears, (d) => d.pct);
```

```js
statTiles([
  {label: "Northwest share of the list", value: `${nwShare(2001, 2010).toFixed(0)}% → ${nwShare(2016, 2025).toFixed(0)}%`,
   caption: "2001–2010 compared with 2016–2025."},
  {label: "Bay Area share of the list", value: `${bayShare(2001, 2010).toFixed(0)}% → ${bayShare(2016, 2025).toFixed(0)}%`,
   caption: "The same two periods, for the Bay Area and Northern California."},
  {label: "Bay Area albums since KEXC", value: `${bayRecent.length}`,
   caption: `On the 2024 and 2025 lists combined, from ${nArtists(bayRecent)} artists. Too few to call a trend.`}
])
```

The Northwest has supplied roughly ${nwShare(2001, 2025).toFixed(0)}% of all list entries, but the year-to-year swings are large, from ${nwLow.pct.toFixed(0)}% in ${nwLow.yr} to ${nwHigh.pct.toFixed(0)}% in ${nwHigh.yr}, and it has run lower since the mid-2010s. The Bay Area is much smaller. Most years it has one to four albums on a list. KEXP began simulcasting on KEXC 92.7 FM in San Francisco in March 2024, so the 2024 and 2025 lists are the first to come after it. Those two lists hold ${bayRecent.length} Bay Area albums from ${nArtists(bayRecent)} artists, which is too few to read anything into yet. One artist more or less moves the line, so this is one to check again after the 2026 list.

### Big cities and small towns

How big are the places these artists come from? Size here is the population of the city itself today, from GeoNames, so a small town beside a big city counts as a small town. The first chart groups every hometown by size and follows each group's share of the lists over time.

```js
// ---- city sizes: population of the city proper, from GeoNames (Wikipedia where GeoNames had no match) ----
const popOf = new Map(popRows.filter((d) => d.population > 0).map((d) => [d.place, d.population]));
const sized = located.filter((d) => popOf.has(d.place));
const unsizedPlaces = [...new Set(located.filter((d) => !popOf.has(d.place)).map((d) => d.city))];
const unsizedEntries = located.length - sized.length;
const SIZE_BUCKETS = [
  {key: "Under 100,000", test: (p) => p < 1e5, color: PURPLE},
  {key: "100,000 to 1 million", test: (p) => p >= 1e5 && p < 1e6, color: GOLD},
  {key: "1 to 3 million", test: (p) => p >= 1e6 && p < 3e6, color: TEAL},
  {key: "3 million or more", test: (p) => p >= 3e6, color: BLUE}
];
const inBucket = (b) => (d) => b.test(popOf.get(d.place));
const sizeShare = (lo, hi, b) => { const s = sized.filter((d) => d.list_year >= lo && d.list_year <= hi); return 100 * s.filter(inBucket(b)).length / s.length; };
const sizedTotalByYear = d3.rollup(sized, (v) => v.length, (d) => d.list_year);
// GeoNames gives metro-area figures for Australian cities, so also show the biggest-city share without them
const bigShareNoAus = (lo, hi) => { const s = sized.filter((d) => d.list_year >= lo && d.list_year <= hi && !(d.country === "Australia" && popOf.get(d.place) >= 1e6)); return 100 * s.filter(inBucket(SIZE_BUCKETS[3])).length / s.length; };
const fmtN = d3.format(",");
const listOf = (a) => new Intl.ListFormat("en").format(a);
const placeStats = [...d3.group(sized, (d) => d.place)].map(([pl, v]) => {
  const pop = popOf.get(pl), n = nArtists(v);
  return {place: pl, name: `${v[0].city}, ${v[0].region || v[0].country}`, city: v[0].city, pop, artists: n, per: 1e5 * n / pop,
    top: d3.rollups(v, (vv) => vv.length, (d) => d.artist_name).sort((a, b) => b[1] - a[1]).slice(0, 3).map((x) => x[0])};
});
```

```js
function sizeTrend() {
  const wrap = document.createElement("div");
  const W = 880, H = 380, m = {l: 46, r: 16, t: 14, b: 30};
  const ser = SIZE_BUCKETS.map((b) => {
    const by = d3.rollup(sized.filter(inBucket(b)), (v) => v.length, (d) => d.list_year);
    return years.map((yr) => {
      const span = [yr - 1, yr, yr + 1];
      return {yr, n: by.get(yr) ?? 0, total: sizedTotalByYear.get(yr), share: 100 * d3.sum(span, (y) => by.get(y) ?? 0) / d3.sum(span, (y) => sizedTotalByYear.get(y) ?? 0)};
    });
  });
  const keys = SIZE_BUCKETS.map((b) => b.key);
  const stack = d3.stack().keys(keys)(years.map((yr, yi) => Object.fromEntries([["yr", yr], ...keys.map((k, i) => [k, ser[i][yi].share])])));
  const x = d3.scaleLinear([years[0], years[years.length - 1]], [m.l, W - m.r]);
  const y = d3.scaleLinear([0, 100], [H - m.b, m.t]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, H]).attr("width", W).attr("height", H).attr("style", CARD);
  y.ticks(5).forEach((v) => {
    svg.append("line").attr("x1", m.l).attr("x2", W - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : "#2a2a27");
    svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(v + "%");
  });
  [2001, 2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", x(yr)).attr("y", H - m.b + 18).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr));
  const area = d3.area().x((d, i) => x(years[i])).y0((d) => y(d[0])).y1((d) => y(d[1])).curve(d3.curveMonotoneX);
  stack.forEach((s, i) => svg.append("path").attr("d", area(s)).attr("fill", SIZE_BUCKETS[i].color).attr("fill-opacity", 0.9).attr("stroke", "#1a1a19").attr("stroke-width", 1));
  const cursor = svg.append("line").attr("y1", m.t).attr("y2", H - m.b).attr("stroke", "#f0efec").attr("stroke-opacity", 0.6).style("display", "none").attr("pointer-events", "none");
  svg.append("rect").attr("x", m.l).attr("y", m.t).attr("width", W - m.l - m.r).attr("height", H - m.t - m.b).attr("fill", "none").attr("pointer-events", "all")
    .on("pointermove pointerenter", (event) => {
      const yr = Math.max(years[0], Math.min(years[years.length - 1], Math.round(x.invert(d3.pointer(event, svg.node())[0]))));
      const yi = years.indexOf(yr);
      cursor.attr("x1", x(yr)).attr("x2", x(yr)).style("display", null);
      const lines = SIZE_BUCKETS.map((b, i) => `<span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:${b.color};margin-right:6px"></span>${b.key}: ${ser[i][yi].n} of ${ser[i][yi].total} (${(100 * ser[i][yi].n / ser[i][yi].total).toFixed(0)}%)`);
      tip.show(event, `<b>${yr} list</b><br>${lines.join("<br>")}`);
    })
    .on("pointerleave", (event) => { cursor.style("display", "none"); hideTip(event); });
  const chips = document.createElement("div");
  chips.style.cssText = "display:flex;gap:10px;flex-wrap:wrap;margin:0.8rem 0 0.25rem;justify-content:center;";
  SIZE_BUCKETS.forEach((b) => {
    const chip = document.createElement("div");
    chip.innerHTML = `<span style="width:12px;height:12px;border-radius:3px;background:${b.color};display:inline-block"></span>${b.key} <span style="color:#898781">${fmtN(sized.filter(inBucket(b)).length)}</span>`;
    chip.style.cssText = "display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3;background:#232321;border:1px solid #383835;border-radius:999px;padding:5px 12px;font-family:var(--sans-serif);";
    chips.append(chip);
  });
  wrap.append(svg.node(), chips);
  return wrap;
}
```

<div class="card" data-chart="size" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
sizeTrend()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Each band is a size group's share of every year's list, using a three-year average. Hover for the actual counts for any single year. The number next to each group is its total albums across all 25 lists.</p>

```js
const bigPlaces = placeStats.filter((d) => d.pop >= 3e6).sort((a, b) => b.artists - a.artists);
```

Small towns held steady at about ${smallMid.toFixed(0)}%: places under 100,000 supplied between ${smallLow.toFixed(0)}% and ${smallHigh.toFixed(0)}% of entries in every five-year stretch. The change is in the middle and at the top. Cities of 100,000 to 1 million, a group that includes Seattle and Portland, went from ${sizeShare(2001, 2010, SIZE_BUCKETS[1]).toFixed(0)}% to ${sizeShare(2016, 2025, SIZE_BUCKETS[1]).toFixed(0)}%, while cities of 3 million or more, led by ${listOf(bigPlaces.slice(0, 3).map((d) => d.city))}, went from ${sizeShare(2001, 2010, SIZE_BUCKETS[3]).toFixed(0)}% to ${sizeShare(2016, 2025, SIZE_BUCKETS[3]).toFixed(0)}%.

Size is one thing, but the "small town artist makes it big" idea is really about how much music a place produces for its size. The second chart counts artists per 100,000 residents, for places with at least three artists on the lists, with the three biggest cities below for comparison.

```js
function perResidentBars() {
  const top = placeStats.filter((d) => d.artists >= 3).sort((a, b) => b.per - a.per).slice(0, 10);
  const refs = ["New York City, New York, United States", "London, England, United Kingdom", "Los Angeles, California, United States"]
    .map((k) => placeStats.find((d) => d.place === k)).filter((d) => d && !top.includes(d));
  const W = 880, rowH = 26, m = {l: 230, r: 250, t: 30, b: 8}, gapH = 34;
  const height = m.t + m.b + (top.length + refs.length) * rowH + gapH;
  const x = d3.scaleLinear([0, d3.max(top, (d) => d.per)], [0, W - m.l - m.r]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, height]).attr("width", W).attr("height", height).attr("style", CARD);
  svg.append("text").attr("x", 20).attr("y", 20).attr("fill", "#898781").attr("font-size", 12).text("Artists per 100,000 residents");
  const tapPts = [];
  const draw = (list, y0, isRef) => list.forEach((d, i) => {
    const cy = y0 + i * rowH + rowH / 2;
    const html = `<b>${d.name}</b><br>${d.artists} artist${d.artists === 1 ? "" : "s"}, ${fmtN(d.pop)} residents<br>${d.per.toFixed(1)} per 100,000<br><span style="color:#898781">${d.top.join(", ")}</span>`;
    svg.append("text").attr("x", m.l - 12).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", isRef ? "#898781" : "#c9c8c3").attr("font-size", 12).text(d.name);
    svg.append("rect").attr("x", m.l).attr("y", cy - 8).attr("width", Math.max(2, x(d.per))).attr("height", 16).attr("rx", 3).attr("fill", isRef ? GREY : PURPLE)
      .on("pointerenter pointermove", (event) => showTip(event, html)).on("pointerleave", hideTip);
    tapPts.push({x: m.l + x(d.per) / 2, y: cy, html});
    svg.append("text").attr("x", m.l + x(d.per) + 8).attr("y", cy).attr("dominant-baseline", "middle").attr("fill", "#f0efec").attr("font-size", 12).attr("pointer-events", "none").text(d.per.toFixed(1));
    svg.append("text").attr("x", m.l + x(d.per) + 44).attr("y", cy).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).attr("pointer-events", "none").text(`${d.artists} artists · ${fmtN(d.pop)} residents`);
  });
  draw(top, m.t, false);
  const y1 = m.t + top.length * rowH;
  if (refs.length) svg.append("text").attr("x", 20).attr("y", y1 + 22).attr("fill", "#898781").attr("font-size", 12).text("For comparison");
  draw(refs, y1 + gapH, true);
  enableTap(svg, tip, tapPts, 24);
  return svg.node();
}
```

<div class="card" data-chart="per-resident" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
perResidentBars()
```

</div>

```js
const seattleStat = placeStats.find((d) => d.city === "Seattle"), nycStat = placeStats.find((d) => d.city === "New York City");
const smallestPlace = d3.least(placeStats, (d) => d.pop);
const smallestArtist = sized.find((d) => d.place === smallestPlace.place).artist_name;
const smallA = sizeShare(2001, 2010, SIZE_BUCKETS[0]), smallB = sizeShare(2016, 2025, SIZE_BUCKETS[0]);
const smallFives = [[2001, 2005], [2006, 2010], [2011, 2015], [2016, 2020], [2021, 2025]].map(([lo, hi]) => sizeShare(lo, hi, SIZE_BUCKETS[0]));
const smallLow = d3.min(smallFives), smallHigh = d3.max(smallFives), smallMid = (smallA + smallB) / 2;
const smallSteady = Math.abs(smallA - smallB) < 2 && smallHigh - smallLow < 5;
const smallArtists = new Set(sized.filter((d) => popOf.get(d.place) < 1e5).map((d) => d.artist_id)).size;
const perRank = placeStats.filter((d) => d.artists >= 3).sort((a, b) => b.per - a.per);
```

```js
statTiles([
  {label: "From towns under 100,000", value: smallSteady ? `about ${smallMid.toFixed(0)}%` : `${smallA.toFixed(0)}% → ${smallB.toFixed(0)}%`,
   caption: smallSteady ? `Holds steady: between ${smallLow.toFixed(0)}% and ${smallHigh.toFixed(0)}% of list entries in every five-year stretch. That is ${smallArtists} of ${nArtists(sized).toLocaleString()} artists.`
     : `Share of list entries from places under 100,000, 2001–2010 compared with 2016–2025. That is ${smallArtists} of ${nArtists(sized).toLocaleString()} artists.`},
  {label: "Smallest hometown", value: smallestPlace.city,
   caption: `Population ${fmtN(smallestPlace.pop)}. Home of ${smallestArtist}.`},
  {label: "Seattle, per resident", value: `${(seattleStat.per / nycStat.per).toFixed(0)}×`,
   caption: `Seattle has ${seattleStat.per.toFixed(1)} artists per 100,000 residents, New York City ${nycStat.per.toFixed(1)}.`}
])
```

Per resident, Seattle is the outlier: ${seattleStat.artists} artists from a city of ${fmtN(seattleStat.pop)}, or ${seattleStat.per.toFixed(1)} per 100,000, about ${(seattleStat.per / perRank[1].per).toFixed(1)} times the rate of the next place. Behind it come much smaller cities such as ${listOf(perRank.slice(1, 4).map((d) => d.city))}. The very smallest hometowns, like ${smallestPlace.city}, are one-artist stories, which is why the chart only includes places with at least three artists.

<p style="font-size:13px;color:var(--theme-foreground-muted);">City populations: <a href="https://www.geonames.org/" target="_top" style="color:inherit;text-decoration:underline;">GeoNames</a> (CC BY 4.0), with Wikipedia for a few places GeoNames did not list. They are today's population of the city itself, not the metro area and not the population when the artist grew up, and they are not perfectly comparable from one country to another. The biggest difference is Australia: GeoNames gives metro-area figures for its cities (Melbourne ${(placeStats.find((d) => d.city === "Melbourne").pop / 1e6).toFixed(1)} million, Sydney ${(placeStats.find((d) => d.city === "Sydney").pop / 1e6).toFixed(1)} million) but the city itself for London, New York City, and most other places, so Melbourne and Sydney land in the 3 million or more group. Leaving Australia's big cities out, that group's share goes from ${bigShareNoAus(2001, 2010).toFixed(0)}% to ${bigShareNoAus(2016, 2025).toFixed(0)}%, so the rise is real but a little smaller. ${unsizedEntries} entries, from ${listOf(unsizedPlaces)}, have no size on file and are left out of the charts in this section.</p>

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Here's what these charts can't tell us. An artist is counted in one place, so a band that has lived in several cities shows up in the one I judged it most associated with, not in all of them. ${unlocated} of ${rows.length} entries (${(100 * unlocated / rows.length).toFixed(1)}%) have no place (${unlocatedNames.join(", ")}) and are left out of every chart on this page. City coordinates come from a lookup against OpenStreetMap, so a few small places may sit slightly off. Borough detail exists only where MusicBrainz or my own research recorded it, so those bars undercount the real distribution inside a city. The borough outlines on the map are simplified from the Office for National Statistics boundaries for London (Open Government Licence; contains National Statistics data &copy; Crown copyright and database right) and the city's own borough boundaries for New York City.</div>
</div>

```js
addExpandButtons(() => [...document.querySelectorAll(".dmo-seg")].map((e) => e.value).join(","));
```
