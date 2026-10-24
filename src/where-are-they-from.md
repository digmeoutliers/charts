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
  <style>.embedded { --serif: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; } html.embedded body { font-size: 17px; line-height: 1.6; color: var(--dmo-fg); } .embedded main { margin-top: 0 !important; } .embedded main > p { margin: 28px 0; } .embedded main > h2 { margin-top: 56px; } .embedded main > h3 { margin-top: 44px; } .embedded .standalone-only + p { margin-top: 0; } .embedded #observablehq-footer { display: none; } p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display { max-width: 920px; } .embedded #observablehq-center { margin: 0 !important; } .embedded main > h1, .embedded .standalone-only { display: none; } .dmo-tiles { display: grid; grid-template-columns: 1fr; gap: 1.25rem; } .dmo-tile { padding: 0 0.25rem; } .dmo-tile + .dmo-tile { border-top: 1px solid #33322f; padding-top: 1.25rem; } @media (min-width: 760px) { .dmo-tiles { grid-template-columns: repeat(3, 1fr); gap: 0; } .dmo-tile { padding: 0 1.5rem; } .dmo-tile + .dmo-tile { border-top: 0; padding-top: 0; border-left: 1px solid #33322f; } } html.embedded { --dmo-fg: #15171a; --dmo-bg-solid: #ffffff; --theme-foreground: var(--dmo-fg); --theme-background: var(--dmo-bg-solid); --theme-foreground-muted: color-mix(in srgb, var(--dmo-fg) 68%, var(--dmo-bg-solid)); --theme-foreground-faint: color-mix(in srgb, var(--dmo-fg) 38%, var(--dmo-bg-solid)); --theme-foreground-fainter: color-mix(in srgb, var(--dmo-fg) 18%, var(--dmo-bg-solid)); --theme-foreground-faintest: color-mix(in srgb, var(--dmo-fg) 8%, var(--dmo-bg-solid)); } @media (prefers-color-scheme: dark) { html.embedded { --dmo-fg: #dcdcd6; --dmo-bg-solid: #15171a; } } html.embedded, html.embedded body { background: var(--dmo-bg-solid); }  .phone-note { display: none; font-size: 14px; line-height: 1.5; color: var(--theme-foreground-muted); margin: 0 0 1.25rem; padding: 0.6rem 0.9rem; border-left: 3px solid #9c57f3; } .embedded main > p.phone-note { margin: 0 0 24px; } @media (max-width: 640px) { .phone-note { display: block; } } </style>
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
    var timer;
    function later() { clearTimeout(timer); timer = setTimeout(fixLinks, 100); }
    document.addEventListener("DOMContentLoaded", function () {
      fixLinks();
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
  el.style.cssText = "display:inline-flex;border:1px solid #8a8985;border-radius:999px;overflow:hidden;background:#d9d8d3;margin:0.25rem 0.75rem 0.75rem 0;font-family:var(--sans-serif);";
  const buttons = options.map(([label, value]) => {
    const b = document.createElement("button");
    b.type = "button"; b.textContent = label;
    b.style.cssText = "border:0;background:#d9d8d3;color:#5f5e5a;font-size:13px;padding:6px 16px;cursor:pointer;font-family:var(--sans-serif);";
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

function placePoints(entries) {
  return [...d3.rollup(entries, (v) => nArtists(v), (d) => d.place)].map(([pl, n]) => ({lon: placeInfo.get(pl).lon, lat: placeInfo.get(pl).lat, w: n}));
}

// one bubble per place, per region, or per country
function bubbles(level) {
  const keyOf = level === "cities" ? (d) => d.place : level === "regions" ? (d) => d.country + "|" + (d.region ?? "") : (d) => d.country;
  return [...d3.group(located, keyOf)].map(([key, v]) => {
    const byPlace = d3.rollup(v, (vv) => nArtists(vv), (d) => d.place);
    let lat = 0, lon = 0, w = 0;
    for (const [pl, n] of byPlace) { const p = placeInfo.get(pl); lat += p.lat * n; lon += p.lon * n; w += n; }
    const first = v[0];
    const name = level === "cities" ? `${first.city}, ${first.region || first.country}` : level === "regions" ? (first.region ? `${first.region}, ${first.country}` : first.country) : first.country;
    const byArtist = d3.rollups(v, (vv) => vv.length, (d) => d.artist_name).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
    return {key, name, lat: lat / w, lon: lon / w, artists: nArtists(v), albums: v.length, top: byArtist.slice(0, 3), points: placePoints(v), placeSet: new Set(v.map((d) => d.place))};
  }).sort((a, b) => b.artists - a.artists);
}
const hometown = bubbles("cities")[0];
```

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">"From" here means an artist's home base, usually where the artist or band got started, as <a href="https://musicbrainz.org/" target="_top" style="color:inherit; text-decoration:underline;">MusicBrainz</a> records it. Where that was clearly off, such as a London band filed as American, I researched it and corrected it. It is not where an artist lives now, records, or is signed. Each place is shown at its map coordinates. The state and country bubbles sit at the average position of the cities inside them, weighted by artists, so the U.S. bubble lands in the middle of the country, not on any single place.</div>
</div>

<p class="phone-note">On a phone? Tap a bubble or bar to see its details. These charts have more room on a laptop or tablet.</p>

## Every artist, on the map

Each bubble is a place. Bigger means more artists from there, and color shows how many albums each of those artists has had on a list: purple for one, up to gold for several. Start with countries, then double-click a bubble to zoom in a level, to states and regions and then to cities. You can also use the buttons, drag to pan, and scroll to zoom. Hover or click a bubble for details, or search for an artist or a place to see who is there.

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
    if (seg && seg.value !== want) seg.setValue(want);
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
const mapLevel = view(segmented([["Countries", "countries"], ["States and regions", "regions"], ["Cities", "cities"]], ["cities", "regions", "countries"].includes(urlModes[0]) ? urlModes[0] : "countries", "countries"));
const mapColor = view(segmented([["Albums per artist", "per"], ["Total albums", "total"]], ["per", "total"].includes(urlModes[1]) ? urlModes[1] : "per", "per"));
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
  const selPlaces = new Set(selEntries.map((d) => d.place));
  const isSel = (d) => !sel || [...d.placeSet].some((p) => selPlaces.has(p));
  const rmax = {cities: 24, regions: 34, countries: 48}[level];
  const maxA = d3.max(data, (d) => d.artists);
  const r0 = (d) => Math.max(2.4, rmax * Math.sqrt(d.artists / maxA));
  const colorVal = colorMode === "per" ? (d) => d.albums / d.artists : (d) => d.albums;
  const cmax = colorMode === "per" ? 3.5 : d3.quantile(data.map((d) => d.albums).sort(d3.ascending), 0.97);
  const ramp = d3.interpolateRgbBasis(["#3b2a86", "#9c57f3", "#f2cf6a"]);
  const color = d3.scaleSequential(ramp).domain([1, cmax]).clamp(true);

  const wrap = document.createElement("div");
  const svg = d3.create("svg").attr("viewBox", [0, 0, W, H]).attr("width", W).attr("height", H).attr("style", CARD).style("touch-action", "pan-y");
  const g = svg.append("g");
  g.append("g").selectAll("path").data(feats).join("path").attr("d", path).attr("fill", "#2a2a2d").attr("stroke", "#76767d").attr("stroke-width", 0.6).attr("vector-effect", "non-scaling-stroke");

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
  const nextLevel = {countries: "regions", regions: "cities"}[level];
  const html = (d) => `<b>${d.name}</b><br>${d.artists.toLocaleString()} artist${d.artists === 1 ? "" : "s"} &middot; ${d.albums.toLocaleString()} album${d.albums === 1 ? "" : "s"} on lists<br><span style="color:#898781">${(d.albums / d.artists).toFixed(1)} albums per artist</span><br><span style="color:#898781">${d.top.map(([n, c]) => n + (c > 1 ? ` (${c})` : "")).join(", ")}</span>${nextLevel ? '<br><span style="color:#898781;font-size:11px">Double-click to zoom in</span>' : ""}`;
  dots.on("pointerenter pointermove", (event, d) => tip.show(event, html(d), 14)).on("pointerleave", hideTip)
    .on("click", (event, d) => { event.stopPropagation(); pin(event, html(d)); })
    .on("dblclick", (event, d) => {
      event.stopPropagation(); event.preventDefault(); unpin(); hideTip();
      window.__dmoFocus = {box: boundsOf(d.points), maxK: nextLevel === "regions" ? 5 : 9};
      if (nextLevel) document.querySelector(".dmo-seg").setValue(nextLevel); else focusNow();
    });
  svg.on("click", () => unpin());

  let k = 1;
  const zoom = d3.zoom().scaleExtent([1, 14]).translateExtent([[0, 0], [W, H]]).extent([[0, 0], [W, H]]).on("zoom", (event) => {
    k = event.transform.k;
    g.attr("transform", event.transform);
    dots.attr("r", (d) => r0(d) * Math.pow(k, -0.7));   // on screen the bubble grows only slowly as you zoom in
    labels.style("display", (d) => k >= 1.7 && d.area * k * k > 2600 ? null : "none").attr("font-size", 11 / k).attr("stroke-width", 3 / k);
    window.__dmoMapT = event.transform;
  });
  svg.call(zoom).on("dblclick.zoom", null);
  svg.call(zoom.transform, window.__dmoMapT ?? d3.zoomIdentity);

  // zoom to a box of [lon, lat] corners
  function flyTo(box, maxK = 14) {
    const [[x0, y0], [x1, y1]] = [projection(box[0]), projection(box[1])];
    const kk = Math.max(1, Math.min(maxK, 0.85 / Math.max(Math.abs(x1 - x0) / W, Math.abs(y1 - y0) / H, 0.001)));
    const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    svg.transition().duration(650).call(zoom.transform, d3.zoomIdentity.translate(W / 2 - kk * cx, H / 2 - kk * cy).scale(kk));
  }
  function focusNow() { const f = window.__dmoFocus; window.__dmoFocus = null; if (f) flyTo(f.box, f.maxK); }
  if (window.__dmoFocus) focusNow();
  else if (sel && window.__dmoSelFlown !== sel.label) {
    window.__dmoSelFlown = sel.label;
    const pts = placePoints(selEntries);
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
  if (!sel) { box.innerHTML = `<p style="${muted}margin:0;">Search for an artist or a place above to see who is there.</p>`; return box; }
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
  {label: "Biggest hometown", value: hometown.name.split(",")[0],
   caption: `${hometown.artists} artists and ${hometown.albums} albums on the lists.`}
])
```

The map is mostly two clusters of big bubbles, with a long tail of small ones. ${hometown.name.split(",")[0]} is the biggest hometown, ahead of New York City and London, and the lists are overwhelmingly American, with Britain a distant second. But the U.S. share has slipped, from ${shareOf(2001, 2010, (d) => d.group === "United States").toFixed(0)}% of entries in the first decade to ${shareOf(2016, 2025, (d) => d.group === "United States").toFixed(0)}% in the last ten years.

## Interesting observations

The map shows all 25 years at once. The charts below split that picture in two ways: how the mix of places has changed over time, and what's inside the biggest cities.

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
  {label: `${hometown.name.split(",")[0]}'s share of the list`, value: `${cityShare(2001, 2010, hometown.name.split(",")[0]).toFixed(0)}% → ${cityShare(2016, 2025, hometown.name.split(",")[0]).toFixed(0)}%`,
   caption: "The same two periods. KEXP's hometown barely moved."},
  {label: "Beyond the U.S., U.K., and Canada", value: `${shareOf(2001, 2010, (d) => d.group === "Europe" || d.group === "Rest of world").toFixed(0)}% → ${shareOf(2016, 2025, (d) => d.group === "Europe" || d.group === "Rest of world").toFixed(0)}%`,
   caption: "Share of entries from everywhere else, the same two periods."}
])
```

Two stories stand out. The first is that KEXP's hometown held steady: ${hometown.name.split(",")[0]} supplied about a tenth of every list, year after year. The second is that the growth is happening elsewhere, in London and in the long tail of countries outside the U.S., U.K., and Canada. The U.S. share fell from ${shareOf(2001, 2010, (d) => d.group === "United States").toFixed(0)}% to ${shareOf(2016, 2025, (d) => d.group === "United States").toFixed(0)}%, and the U.K. and the countries beyond the U.S., U.K., and Canada picked up the difference.

### Inside the biggest cities

Two cities have more detail on file than the rest: a borough. Each bar below is the number of artists from that part of town. Where MusicBrainz doesn't name one, the artist is counted under "Not specified."

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
statTiles([
  {label: "Brooklyn", value: `${boroughArtists(nyc, "Brooklyn")}`,
   caption: `Artists from Brooklyn, out of ${nArtists(nyc)} from New York City. Manhattan has ${boroughArtists(nyc, "Manhattan")}.`},
  {label: "London, borough on file", value: `${nArtists(ldn.filter((d) => d.borough))} of ${nArtists(ldn)}`,
   caption: "London artists whose borough MusicBrainz records. The rest are counted just as London."},
  {label: "Cities with one artist", value: `${bubbles("cities").filter((d) => d.artists === 1).length}`,
   caption: `Of ${bubbles("cities").length} places, the number that have exactly one artist on the lists.`}
])
```

Brooklyn alone has nearly three times as many artists as Manhattan. London's artists are spread over more boroughs, but the details are thin: for most of them MusicBrainz only says London. Los Angeles is the same story in a smaller way: neighborhoods like Silver Lake and Hollywood are named for only a handful of its 59 artists, so they didn't get a chart.

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

Growth and decline here are measured as a city's share of the whole list, so they show who gained room and who lost it. ${grower.name} gained the most and ${faller.name} lost the most, by almost the same amount. In relative terms, ${relGrower.name} grew fastest: its share went from ${relGrower.sa.toFixed(1)}% to ${relGrower.sc.toFixed(1)}%, more than ${Math.floor(relGrower.ratio)} times as large. The cities that faded are mostly ones that were once regulars. The newcomers are a different kind of change: the number of home countries on a single list was ${perListRange(2001, 2010)[0]} to ${perListRange(2001, 2010)[1]} in the 2000s and has been ${perListRange(2022, 2025)[0]} to ${perListRange(2022, 2025)[1]} in the last four years. Most of the newcomers each have one or two albums, but together they are why the map has more small dots at the edges than it used to. (Puerto Rico counts as its own country here because that is how MusicBrainz files it.)

```js
const BAY = new Set(["San Francisco", "Oakland", "Berkeley", "San Jose", "Palo Alto", "Walnut Creek", "Vallejo"]);
const isBay = (d) => d.region === "California" && BAY.has(d.city);
const bayPerYear = (lo, hi) => era(lo, hi).filter(isBay).length / (hi - lo + 1);
const bayRecent = era(2024, 2025).filter(isBay);
const newcomerAlbums = located.filter((d) => newcomers.some(([c]) => c === d.country));
```

Two things outside the data may be part of this story. KEXP began simulcasting on KEXC 92.7 FM in San Francisco in March 2024, so the 2024 and 2025 lists are the first to come after it. Those two lists held ${bayPerYear(2024, 2025).toFixed(1)} Bay Area albums a year (${bayRecent.length} albums from ${nArtists(bayRecent)} artists), up from ${bayPerYear(2021, 2023).toFixed(1)} a year in 2021&ndash;2023 and about level with the ${bayPerYear(2001, 2010).toFixed(1)} a year of 2001&ndash;2010. That is two lists and a handful of albums, so it is too early to call a trend, but it is worth watching on the 2026 list. (Here the Bay Area means San Francisco, Oakland, Berkeley, San Jose, Palo Alto, Walnut Creek, and Vallejo.) KEXP also has region-focused shows, including Wo' Pop, El Sonido, and, since September 2023, The Continent and Eastern Echoes. I checked the play data for the artists behind the new countries (the ${newcomerAlbums.length} albums include Songhoy Blues, Mdou Moctar, Altın Gün, Liraz, and Bad Bunny), and those shows account for only a small slice of their airplay. Most of it came on KEXP's general shows. A few artists did lean on the regional programming, Liraz most of all, but The Continent and Eastern Echoes began after several of the newcomers had already arrived. So the programming may have helped some artists find an audience, but it does not explain the new countries on its own.

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Here's what these charts can't tell us. An artist is counted in one place, so a band that formed in one city and moved to another shows up where it started. ${unlocated} of ${rows.length} entries (${(100 * unlocated / rows.length).toFixed(1)}%) have no usable place (either no location on file, or only a country with no city) and are left out of every chart on this page. City coordinates come from a lookup against OpenStreetMap, so a few small places may sit slightly off. Borough detail exists only where MusicBrainz or my own research recorded it, so those bars undercount the real distribution inside a city.</div>
</div>

```js
addExpandButtons(() => [...document.querySelectorAll(".dmo-seg")].map((e) => e.value).join(","));
```
