---
title: How long have they been at it?
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
    var keepSwitch = only === "heat" || only === "first";
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

# How long have they been at it?

<div class="standalone-only" style="font-size:13px;color:var(--theme-foreground-muted);margin:0 0 1rem;"><strong>Draft</strong>: unlisted page, not part of the published blog yet.</div>

```js
import {makeTooltip, enableTap} from "./components/tooltip.js";
import {addLens} from "./components/lens.js";
import {addExpandButtons} from "./components/expand.js";
```

```js
const rows = FileAttachment("data/age_and_career_2001_2025.csv").csv({typed: true});
```

```js
// ---- Palette: same as the "Who's on the list?" post (gold = solo women, teal = solo men, purple = bands). ----
const catColor = {"Solo women": "#d6b45b", "Solo men": "#58cec8", "Groups": "#9c57f3", "Other / not recorded": "#dcdad2"};
const catOrder = ["Solo women", "Solo men", "Groups", "Other / not recorded"];

function category(d) {
  if (d.artist_type === "Group") return "Groups";
  if (d.artist_type === "Person") {
    if (d.artist_gender === "Female") return "Solo women";
    if (d.artist_gender === "Male") return "Solo men";
  }
  return "Other / not recorded";
}
const years = d3.sort(new Set(rows.map((d) => d.list_year)));
const CARD = "background:#1a1a19;border-radius:12px;max-width:100%;height:auto;font-family:var(--sans-serif);";
const tip = makeTooltip({minWidth: 150, maxWidth: 260});
const showTip = (event, html) => tip.show(event, html);
const hideTip = (event) => tip.hide(event);
const swatch = (c) => `<span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:${catColor[c]};margin-right:6px"></span>`;
const ordinal = (n) => { const s = ["th", "st", "nd", "rd"], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); };

function keyButtons(cats, counts, state, apply) {
  const key = document.createElement("div");
  key.style.cssText = "display:flex;gap:10px;flex-wrap:wrap;margin:0.9rem 0 0.25rem;justify-content:center;";
  const buttons = new Map();
  cats.forEach((c) => {
    const b = document.createElement("button");
    b.type = "button";
    b.style.cssText = "display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3;background:#232321;border:1px solid #383835;border-radius:999px;padding:5px 12px;cursor:pointer;font-family:var(--sans-serif);";
    b.innerHTML = `<span style="width:12px;height:12px;border-radius:3px;background:${catColor[c]};display:inline-block"></span>${c} <span style="color:#898781">${counts[c].toLocaleString()}</span>`;
    b.onclick = () => { state.cat = state.cat === c ? null : c; apply(); refresh(); };
    buttons.set(c, b);
    key.append(b);
  });
  function refresh() {
    buttons.forEach((b, c) => { b.style.outline = state.cat === c ? "2px solid #f0efec" : "none"; b.style.opacity = !state.cat || state.cat === c ? 1 : 0.55; });
  }
  refresh();
  return key;
}

// a small two-button switch for use with view()
function segmented(options, initial) {
  const el = document.createElement("div");
  el.className = "dmo-seg dmo-ctl";
  el.style.cssText = "display:inline-flex;border:1px solid #8a8985;border-radius:999px;overflow:hidden;background:#d9d8d3;margin:0.25rem 0 1rem;font-family:var(--sans-serif);";
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
// ---- numbers used in the tiles and text, computed from the data ----
const era = (lo, hi) => rows.filter((d) => d.list_year >= lo && d.list_year <= hi);
const withCareer = rows.filter((d) => d.career_years != null);
const careerIn = (lo, hi) => withCareer.filter((d) => d.list_year >= lo && d.list_year <= hi);
const medYears = (lo, hi) => d3.median(careerIn(lo, hi), (d) => d.career_years);
const longest = d3.greatest(withCareer, (d) => d.career_years);
const longestBand = d3.greatest(withCareer.filter((d) => d.artist_type === "Group"), (d) => d.career_years);

const shareWhere = (r, test) => 100 * r.filter(test).length / r.length;

const soloAges = rows.filter((d) => d.age_at_release != null);
const agesIn = (lo, hi, c) => soloAges.filter((d) => d.list_year >= lo && d.list_year <= hi && (!c || category(d) === c));
const youngestAge = d3.min(soloAges, (d) => d.age_at_release), oldestAge = d3.max(soloAges, (d) => d.age_at_release);
const youngest = soloAges.filter((d) => d.age_at_release === youngestAge);
const oldest = soloAges.filter((d) => d.age_at_release === oldestAge);
const names = (r) => [...new Set(r.map((d) => d.artist_name))].join(" and ");
const over40 = (lo, hi, c) => shareWhere(agesIn(lo, hi, c), (d) => d.age_at_release >= 40);
const under25 = (lo, hi, c) => shareWhere(agesIn(lo, hi, c), (d) => d.age_at_release < 25);
```

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">MusicBrainz keeps one "begin" date for every artist, but it means different things. For a person it is a birth date, and for a band it is the year the band formed. Those aren't comparable, so for "years in" I built my own start year for every artist. For a band, it is the formed date MusicBrainz lists (or, when there isn't one, the year of its first release). For a solo artist, it is the year of their first release under their own name, not their birth year. This is a convention I chose, not a fact about anyone's career. A solo artist who came out of a well-known band starts the clock at their first solo release: Bob Mould's start is 1989, not Hüsker Dü in 1979, and Johnny Marr's is 2013, not The Smiths' 1982. I count the person and the band separately, the way MusicBrainz does. Birth dates are used only in the age chart, and only for solo artists. MusicBrainz has a birth date for ${(100 * rows.filter((d) => d.age_at_release != null).length / rows.filter((d) => d.artist_type === "Person" && !d.posthumous).length).toFixed(0)}% of the solo albums here, so the age charts cover those. The ${rows.filter((d) => d.posthumous).length} albums released after an artist's death are left out of the career and age charts.</div>
</div>

<p class="phone-note">On a phone? Tap a dot or bar to see its details. These charts have more room on a laptop or tablet.</p>

## Every album, by how long they'd been at it

Each dot is one album on one year's list, placed by how many years the artist had been at it when the album came out. Gold is a solo woman, teal is a solo man, and purple is a band, the same as in the last post. The white line is the typical artist, the median for that year's list. Click a color in the key to look at one kind of artist, and hover any dot to see who it is.

```js
const heroState = {cat: null};
const medianCache = (() => {
  const out = {};
  for (const key of ["all", ...catOrder]) {
    out[key] = years.map((yr) => ({yr, v: d3.median(withCareer.filter((d) => d.list_year === yr && (key === "all" || category(d) === key)), (d) => d.career_years)}));
  }
  return out;
})();

function careerSwarm() {
  const width = 880, height = 630, m = {l: 46, r: 16, t: 28, b: 34};
  const colW = (width - m.l - m.r) / years.length;
  const y = d3.scaleLinear([0, 60], [height - m.b, m.t]);
  const xc = (yr) => m.l + (years.indexOf(yr) + 0.5) * colW;
  const r = 2.7;
  const wrap = document.createElement("div");
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  [0, 10, 20, 30, 40, 50, 60].forEach((v) => {
    svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : "#2a2a27");
    svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(v);
  });
  svg.append("text").attr("x", 14).attr("y", 14).attr("fill", "#898781").attr("font-size", 11).text("Years in");
  years.forEach((yr) => svg.append("text").attr("x", xc(yr)).attr("y", height - m.b + 18).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(yr));

  const tapPts = [];
  years.forEach((yr) => {
    const nodes = withCareer.filter((d) => d.list_year === yr).map((d) => ({d, x: xc(yr), y: y(d.career_years), tx: xc(yr), ty: y(d.career_years)}));
    const sim = d3.forceSimulation(nodes)
      .force("x", d3.forceX((n) => n.tx).strength(0.06))
      .force("y", d3.forceY((n) => n.ty).strength(0.9))
      .force("collide", d3.forceCollide(r + 0.45))
      .stop();
    for (let i = 0; i < 140; i++) {
      sim.tick();
      nodes.forEach((n) => { n.x = Math.max(xc(yr) - colW / 2 + r, Math.min(xc(yr) + colW / 2 - r, n.x)); n.y = Math.min(y(0), n.y); });
    }
    nodes.forEach(({d, x, y: py}) => {
      const c = category(d);
      const html = `<b>${d.artist_name}</b><br><i>${d.release_group_name}</i><br>${d.list_year} list &middot; #${d.rank}<br><span style="color:#898781">${swatch(c)}${c}</span><br>${d.career_years} year${d.career_years === 1 ? "" : "s"} in <span style="color:#898781">(started ${d.career_start})</span>`;
      tapPts.push({x, y: py, html});
      svg.append("circle").attr("cx", x).attr("cy", py).attr("r", r).attr("fill", catColor[c]).attr("data-cat", c)
        .style("transition", "opacity 0.15s")
        .on("pointerenter pointermove", (event) => tip.show(event, html, 92))
        .on("pointerleave", hideTip);
    });
  });

  const line = d3.line().defined((p) => p.v != null).x((p) => xc(p.yr)).y((p) => y(p.v)).curve(d3.curveMonotoneX);
  const med = svg.append("path").attr("fill", "none").attr("stroke", "#f0efec").attr("stroke-width", 2.4).attr("stroke-linejoin", "round").attr("opacity", 0.95).attr("pointer-events", "none");
  const lens = addLens(svg, {radius: 76, zoom: 3});
  enableTap(svg, tip, tapPts, 9, lens);

  function apply() {
    const sel = heroState.cat;
    svg.selectAll("circle[data-cat]").style("opacity", function () { return !sel || this.getAttribute("data-cat") === sel ? 1 : 0.1; });
    med.attr("d", line(medianCache[sel ?? "all"]));
  }
  const counts = Object.fromEntries(catOrder.map((c) => [c, withCareer.filter((d) => category(d) === c).length]));
  apply();
  wrap.append(svg.node(), keyButtons(catOrder, counts, heroState, apply));
  return wrap;
}
```

<div class="card" data-chart="hero" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
careerSwarm()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Years in is the year an album came out minus the artist's start year, as described in the note at the top. The white line is the median for each year's list. Albums released after an artist's death are left out.</p>


## Interesting observations

The dots above show every album on every list. The charts below break career stage into pieces and look at what else it's tied to: which record it is in an artist's catalog, how old the solo artists are, and who has stayed on the lists the longest.

The bottom of every column is crowded: in any year, plenty of artists are in their first few years. What changed is the middle of the chart. In the first decade, the typical artist on a list was ${medYears(2001, 2010).toFixed(0)} years in. In the last ten years it was ${medYears(2016, 2025).toFixed(0)}. The lists haven't stopped finding new names, but more of the room now goes to artists who have been around a while.

```js
statTiles([
  {label: "Typical years in", value: `${medYears(2001, 2010).toFixed(0)} → ${medYears(2016, 2025).toFixed(0)}`,
   caption: "Median years since the artist's start, 2001–2010 compared with 2016–2025."},
  {label: "Longest-running artist", value: `${longest.career_years} years`,
   caption: `${longest.artist_name}, ${longest.release_group_name} (${longest.list_year} list).`},
  {label: "Longest-running band", value: `${longestBand.career_years} years`,
   caption: `${longestBand.artist_name}, ${longestBand.release_group_name} (${longestBand.list_year} list).`}
])
```


### Debut or deep catalog?

Years are one way to measure career stage. Another is to count releases: is this an artist's first record, or their fifth? Each cell below is the share of a year's numbered ${noun}s that were that artist's 1st, 2nd, 3rd, and so on. ${countMode === "albums" ? "Only studio albums get a number, so EPs, live albums, and compilations are left out" : "Studio albums and studio EPs get a number, but I have chosen to leave live albums, compilations, and similar non-studio releases out for this particular analysis"} (${rows.length - numbered.length} of ${rows.length} entries). EPs are a real part of many careers, especially in indie music, so by default they count. A word on "album": everywhere else in this series, "album" is the way KEXP uses it, for anything on the lists, which means LPs, EPs, and in two cases singles. MusicBrainz, where the release types come from, keeps "Album" for full-length LPs and files EPs and singles under their own types. So "studio albums only" below uses MusicBrainz's narrower meaning. Switch to it if you'd rather not count EPs. Hover a cell to see which artists it holds.

```js
const countMode = view(segmented([["Studio albums and EPs", "both"], ["Studio albums only", "albums"]], new URLSearchParams(location.search).get("mode") === "albums" ? "albums" : "both"));
```

```js
const noun = countMode === "albums" ? "album" : "release";
const numOf = (d) => countMode === "albums" ? d.studio_album_number : d.studio_release_number;
const numbered = rows.filter((d) => numOf(d) != null);
const numberedIn = (lo, hi) => numbered.filter((d) => d.list_year >= lo && d.list_year <= hi);
// each artist's first appearance on any list (earliest year, then best rank)
const firsts = [...d3.group(rows.filter((d) => d.artist_type !== "Other"), (d) => d.artist_id).values()]
  .map((v) => v.slice().sort((a, b) => a.list_year - b.list_year || a.rank - b.rank)[0]);
const firstsNumbered = firsts.filter((d) => numOf(d) != null);
const lateBloomers = firstsNumbered.filter((d) => d.artist_name !== "Thurston Moore").sort((a, b) => numOf(b) - numOf(a)).slice(0, 3);
```

```js
const buckets = [
  {label: `1st ${noun}`, test: (n) => n === 1},
  {label: `2nd ${noun}`, test: (n) => n === 2},
  {label: `3rd ${noun}`, test: (n) => n === 3},
  {label: "4th or 5th", test: (n) => n >= 4 && n <= 5},
  {label: "6th to 9th", test: (n) => n >= 6 && n <= 9},
  {label: "10th or later", test: (n) => n >= 10}
];
function albumNumberHeat() {
  const width = 880, m = {l: 96, r: 16, t: 30, b: 14}, cellH = 42;
  const cellW = (width - m.l - m.r) / years.length;
  const height = m.t + buckets.length * cellH + m.b;
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const color = d3.scaleSequential(d3.interpolateRgb("#25232b", "#9c57f3")).domain([0, 0.45]);
  const tapPts = [];
  years.forEach((yr, xi) => svg.append("text").attr("x", m.l + (xi + 0.5) * cellW).attr("y", m.t - 10).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(yr));
  buckets.forEach((b, bi) => {
    svg.append("text").attr("x", m.l - 10).attr("y", m.t + (bi + 0.5) * cellH).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 12).text(b.label);
    years.forEach((yr, xi) => {
      const pool = numbered.filter((d) => d.list_year === yr);
      const hit = pool.filter((d) => b.test(numOf(d)));
      const share = hit.length / pool.length;
      const cx = m.l + (xi + 0.5) * cellW, cy = m.t + (bi + 0.5) * cellH;
      const who = hit.slice().sort((a, c) => a.rank - c.rank).map((d) => d.artist_name);
      const html = `<b>${yr} &middot; ${b.label}</b><br>${hit.length} of ${pool.length} ${noun}s (${(100 * share).toFixed(0)}%)` + (who.length ? `<br><span style="color:#898781">${who.slice(0, 6).join(", ")}${who.length > 6 ? `, and ${who.length - 6} more` : ""}</span>` : "");
      tapPts.push({x: cx, y: cy, html});
      svg.append("rect").attr("x", m.l + xi * cellW + 1).attr("y", m.t + bi * cellH + 1).attr("width", cellW - 2).attr("height", cellH - 2).attr("rx", 3)
        .attr("fill", color(share))
        .on("pointerenter pointermove", (event) => tip.show(event, html))
        .on("pointerleave", hideTip);
      svg.append("text").attr("x", cx).attr("y", cy).attr("text-anchor", "middle").attr("dominant-baseline", "middle").attr("pointer-events", "none")
        .attr("fill", share > 0.12 ? "#f0efec" : "#898781").attr("font-size", 11).text((100 * share).toFixed(0));
    });
  });
  enableTap(svg, tip, tapPts, Math.max(cellW, cellH) / 2);
  return svg.node();
}
```

<div class="card" data-chart="heat" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
albumNumberHeat()
```

</div>

Numbers in the cells are percentages of that year's numbered ${noun}s. A brighter cell means a bigger share.

```js
statTiles([
  {label: `${noun === "album" ? "Albums" : "Releases"} that were a debut`, value: `${shareWhere(numberedIn(2001, 2010), (d) => numOf(d) === 1).toFixed(0)}% → ${shareWhere(numberedIn(2016, 2025), (d) => numOf(d) === 1).toFixed(0)}%`,
   caption: `Share of numbered ${noun}s that were the artist's first, 2001–2010 compared with 2016–2025.`},
  {label: `Fourth ${noun} or later`, value: `${shareWhere(numberedIn(2001, 2010), (d) => numOf(d) >= 4).toFixed(0)}% → ${shareWhere(numberedIn(2016, 2025), (d) => numOf(d) >= 4).toFixed(0)}%`,
   caption: "The same two periods. The top of the chart is thinning and the bottom is filling in."},
  {label: `First list, first ${noun}`, value: `${shareWhere(firstsNumbered, (d) => numOf(d) === 1).toFixed(0)}%`,
   caption: `Share of artists whose first appearance on any list was their debut ${noun} (${firstsNumbered.length.toLocaleString()} artists).`}
])
```

Debuts fell from ${shareWhere(numberedIn(2001, 2010), (d) => numOf(d) === 1).toFixed(0)}% of the numbered ${noun}s in 2001&ndash;2010 to ${shareWhere(numberedIn(2016, 2025), (d) => numOf(d) === 1).toFixed(0)}% in 2016&ndash;2025, while records from the fourth onward grew from ${shareWhere(numberedIn(2001, 2010), (d) => numOf(d) >= 4).toFixed(0)}% to ${shareWhere(numberedIn(2016, 2025), (d) => numOf(d) >= 4).toFixed(0)}%. Some of that is the same artists coming back, as the earlier posts showed. But the next chart asks a different question: for each artist, how far into their catalog were they the first time they made a list?

### When do artists first make a list?

Each bar counts artists by which ${noun} first put them on a list.

```js
function firstListBars() {
  const width = 880, height = 400, m = {l: 54, r: 16, t: 46, b: 54};
  const labels = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th or later"];
  const bucketOf = (n) => Math.min(n, 9) - 1;
  const total = firstsNumbered.length;
  const counts = labels.map((_, i) => Object.fromEntries(catOrder.map((c) => [c, firstsNumbered.filter((d) => bucketOf(numOf(d)) === i && category(d) === c).length])));
  const x = d3.scaleBand(labels, [m.l, width - m.r]).padding(0.25);
  const y = d3.scaleLinear([0, d3.max(counts, (c) => d3.sum(Object.values(c)))], [height - m.b, m.t]).nice();
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  y.ticks(5).forEach((v) => {
    svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : "#2a2a27");
    svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(v);
  });
  // key: the same colors as the charts above
  const keyW = catOrder.map((c) => 16 + c.length * 6.8 + 22);
  let kx = (width - d3.sum(keyW) + 22) / 2;
  catOrder.forEach((c, i) => {
    svg.append("rect").attr("x", kx).attr("y", 12).attr("width", 11).attr("height", 11).attr("rx", 2.5).attr("fill", catColor[c]);
    svg.append("text").attr("x", kx + 16).attr("y", 18).attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 12).text(c);
    kx += keyW[i];
  });
  const tapPts = [];
  labels.forEach((lab, i) => {
    let base = 0;
    const n = d3.sum(Object.values(counts[i]));
    catOrder.forEach((c) => {
      const v = counts[i][c];
      if (!v) return;
      const html = `<b>Artist's ${lab} ${noun}</b><br>${swatch(c)}${c}: ${v} artist${v === 1 ? "" : "s"}<br><span style="color:#898781">${n} in all (${(100 * n / total).toFixed(0)}% of artists)</span>`;
      tapPts.push({x: x(lab) + x.bandwidth() / 2, y: y(base + v / 2), html});
      svg.append("rect").attr("x", x(lab)).attr("width", x.bandwidth()).attr("y", y(base + v)).attr("height", y(base) - y(base + v)).attr("fill", catColor[c])
        .on("pointerenter pointermove", (event) => tip.show(event, html))
        .on("pointerleave", hideTip);
      base += v;
    });
    svg.append("text").attr("x", x(lab) + x.bandwidth() / 2).attr("y", y(n) - 7).attr("text-anchor", "middle").attr("fill", "#f0efec").attr("font-size", 12).attr("font-weight", 600).text(`${(100 * n / total).toFixed(0)}%`);
    svg.append("text").attr("x", x(lab) + x.bandwidth() / 2).attr("y", height - m.b + 20).attr("text-anchor", "middle").attr("fill", "#c9c8c3").attr("font-size", 12).text(lab);
  });
  svg.append("text").attr("x", (m.l + width - m.r) / 2).attr("y", height - 10).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(`Studio ${noun} that first put the artist on a list`);
  enableTap(svg, tip, tapPts, 40);
  return svg.node();
}
```

<div class="card" data-chart="first" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
firstListBars()
```

</div>

Most artists don't wait. About ${shareWhere(firstsNumbered, (d) => numOf(d) === 1).toFixed(0)}% first made a list with their debut and ${shareWhere(firstsNumbered, (d) => numOf(d) <= 2).toFixed(0)}% by their second ${noun}. But a long tail waits much longer. ${lateBloomers.map((d) => `${d.artist_name} (${noun} ${numOf(d)}, ${d.list_year})`).join(", ")}, three legendary artists whose vast catalogs mostly predate the KEXP Annual lists, all arrived late.

### How old are the solo artists?

Ages only make sense for people, so this chart looks at solo artists only: how old they were when the album came out, split by gender and by period. Each dot is one album, and the white line marks the median.

```js
function ageSwarm() {
  const lanes = [
    {c: "Solo women", lo: 2001, hi: 2010, label: "2001–2010"}, {c: "Solo women", lo: 2016, hi: 2025, label: "2016–2025"},
    {c: "Solo men", lo: 2001, hi: 2010, label: "2001–2010"}, {c: "Solo men", lo: 2016, hi: 2025, label: "2016–2025"}
  ];
  const width = 880, laneH = 112, m = {l: 150, r: 20, t: 12, b: 40};
  const height = m.t + m.b + lanes.length * laneH;
  const x = d3.scaleLinear([14, 90], [m.l, width - m.r]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  d3.range(20, 90, 10).forEach((v) => {
    svg.append("line").attr("x1", x(v)).attr("x2", x(v)).attr("y1", m.t).attr("y2", height - m.b).attr("stroke", "#2a2a27");
    svg.append("text").attr("x", x(v)).attr("y", height - m.b + 18).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(v);
  });
  svg.append("text").attr("x", (m.l + width - m.r) / 2).attr("y", height - 8).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text("Age when the album came out");
  const tapPts = [];
  const r = 3;
  lanes.forEach((lane, li) => {
    const cy = m.t + (li + 0.5) * laneH;
    if (li === 2) svg.append("line").attr("x1", 14).attr("x2", width - 14).attr("y1", m.t + li * laneH).attr("y2", m.t + li * laneH).attr("stroke", "#383835");
    svg.append("text").attr("x", 16).attr("y", cy - 6).attr("fill", catColor[lane.c]).attr("font-size", 13).attr("font-weight", 600).text(lane.c);
    svg.append("text").attr("x", 16).attr("y", cy + 12).attr("fill", "#898781").attr("font-size", 12).text(lane.label);
    const items = agesIn(lane.lo, lane.hi, lane.c);
    const nodes = items.map((d) => ({d, x: x(d.age_at_release), y: cy, tx: x(d.age_at_release)}));
    const sim = d3.forceSimulation(nodes).force("x", d3.forceX((n) => n.tx).strength(1)).force("y", d3.forceY(cy).strength(0.12)).force("collide", d3.forceCollide(r + 0.4)).stop();
    for (let i = 0; i < 160; i++) {
      sim.tick();
      nodes.forEach((n) => { n.y = Math.max(cy - laneH / 2 + 8, Math.min(cy + laneH / 2 - 8, n.y)); });
    }
    nodes.forEach(({d, x: px, y: py}) => {
      const html = `<b>${d.artist_name}</b><br><i>${d.release_group_name}</i><br>${d.list_year} list &middot; #${d.rank}<br>Age ${d.age_at_release} when it came out`;
      tapPts.push({x: px, y: py, html});
      svg.append("circle").attr("cx", px).attr("cy", py).attr("r", r).attr("fill", catColor[lane.c])
        .on("pointerenter pointermove", (event) => showTip(event, html))
        .on("pointerleave", hideTip);
    });
    const md = d3.median(items, (d) => d.age_at_release);
    svg.append("line").attr("x1", x(md)).attr("x2", x(md)).attr("y1", cy - laneH / 2 + 6).attr("y2", cy + laneH / 2 - 6).attr("stroke", "#f0efec").attr("stroke-width", 2).attr("pointer-events", "none");
    svg.append("text").attr("x", x(md) + 6).attr("y", cy - laneH / 2 + 14).attr("fill", "#f0efec").attr("font-size", 11).attr("pointer-events", "none").text(`median ${md}`);
  });
  enableTap(svg, tip, tapPts, 12);
  return svg.node();
}
```

<div class="card" data-chart="age" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
ageSwarm()
```

</div>

```js
statTiles([
  {label: "Solo men aged 40 or older", value: `${over40(2001, 2010, "Solo men").toFixed(0)}% → ${over40(2016, 2025, "Solo men").toFixed(0)}%`,
   caption: `2001–2010 compared with 2016–2025. For solo women: ${over40(2001, 2010, "Solo women").toFixed(0)}% to ${over40(2016, 2025, "Solo women").toFixed(0)}%.`},
  {label: "Youngest solo artist", value: `${youngestAge}`,
   caption: `${names(youngest)} (${youngest.map((d) => d.list_year).join(" and ")}).`},
  {label: "Oldest solo artist", value: `${oldestAge}`,
   caption: `${names(oldest)} (${oldest.map((d) => d.list_year).join(" and ")}).`}
])
```

The typical solo artist is in their early to mid thirties, and that hasn't moved much for women (median ${d3.median(agesIn(2001, 2010, "Solo women"), (d) => d.age_at_release)} in 2001&ndash;2010, ${d3.median(agesIn(2016, 2025, "Solo women"), (d) => d.age_at_release)} in 2016&ndash;2025). For men it has crept up, from ${d3.median(agesIn(2001, 2010, "Solo men"), (d) => d.age_at_release)} to ${d3.median(agesIn(2016, 2025, "Solo men"), (d) => d.age_at_release)}, and the share aged 40 or older has roughly doubled for both. Solo women are still the younger group: ${under25(2016, 2025, "Solo women").toFixed(0)}% of their albums in 2016&ndash;2025 came from artists under 25, against ${under25(2016, 2025, "Solo men").toFixed(0)}% for solo men.

### The long-haulers

Some artists turn up on the lists again and again. This chart follows the ${lifeList().length} artists with seven or more albums on the lists. Each line runs from the artist's start to their last listed album, and each dot is an album, placed by the year it came out.

```js
function lifeList() {
  const by = d3.group(rows.filter((d) => d.artist_type !== "Other"), (d) => d.artist_id);
  return [...by].filter(([id, v]) => v.length >= 7 && v[0].career_start != null)
    .map(([id, v]) => ({name: v[0].artist_name, start: v[0].career_start, items: v.slice().sort((a, b) => a.release_year - b.release_year), c: category(v[0])}))
    .sort((a, b) => a.start - b.start || a.name.localeCompare(b.name));
}
function lifelines() {
  const list = lifeList();
  const rowH = 18, m = {l: 240, r: 74, t: 34, b: 10};
  const width = 880, height = m.t + m.b + list.length * rowH;
  const lo = Math.floor(d3.min(list, (a) => a.start) / 10) * 10, hi = 2028;
  const x = d3.scaleLinear([lo, hi], [m.l, width - m.r]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  d3.range(lo, hi, 10).forEach((v) => {
    svg.append("line").attr("x1", x(v)).attr("x2", x(v)).attr("y1", m.t - 6).attr("y2", height - m.b).attr("stroke", "#2a2a27");
    svg.append("text").attr("x", x(v)).attr("y", m.t - 14).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(v);
  });
  const tapPts = [];
  list.forEach((a, i) => {
    const cy = m.t + i * rowH + rowH / 2;
    svg.append("text").attr("x", m.l - 14).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 12).text(a.name);
    const last = a.items[a.items.length - 1].release_year;
    svg.append("line").attr("x1", x(a.start)).attr("x2", x(last)).attr("y1", cy).attr("y2", cy).attr("stroke", catColor[a.c]).attr("stroke-width", 2).attr("opacity", 0.3);
    const startHtml = `<b>${a.name}</b><br>Start: ${a.start}`;
    tapPts.push({x: x(a.start), y: cy, html: startHtml});
    svg.append("circle").attr("cx", x(a.start)).attr("cy", cy).attr("r", 7.5).attr("fill", "none").attr("stroke", catColor[a.c]).attr("stroke-width", 1.5)
      .on("pointerenter pointermove", (event) => showTip(event, startHtml)).on("pointerleave", hideTip);
    a.items.forEach((d) => {
      const html = `<b>${a.name}</b><br><i>${d.release_group_name}</i><br>Released ${d.release_year} &middot; #${d.rank} on the ${d.list_year} list<br>${d.career_years == null ? "" : d.career_years + " years in"}`;
      tapPts.push({x: x(d.release_year), y: cy, html});
      svg.append("circle").attr("cx", x(d.release_year)).attr("cy", cy).attr("r", 5).attr("fill", catColor[a.c])
        .on("pointerenter pointermove", (event) => showTip(event, html)).on("pointerleave", hideTip);
    });
    svg.append("text").attr("x", width - m.r + 12).attr("y", cy).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(`${a.items.length} albums`);
  });
  enableTap(svg, tip, tapPts, 14);
  return svg.node();
}
```

<div class="card" data-chart="lives" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
lifelines()
```

</div>

The open circle marks each artist's start. When an artist's first album came out in their start year, the circle sits around that dot, as it does for Iron & Wine and SAULT. The typical artist here got going around ${d3.median(lifeList(), (a) => a.start)} and has kept landing albums for about ${d3.median(lifeList(), (a) => a.items[a.items.length - 1].release_year - a.start)} years, which is part of why the middle of the first chart is so full.

### A revolving door with a regular cast

These long-haulers can look like they contradict the first post, which ended on the idea that the lists are less a fixed canon of favorites and more a constantly refreshing roster. Both are true. It depends on whether you count artists or spots on the list.

```js
const onList = rows.filter((d) => d.artist_type !== "Other");
const appearances = d3.rollup(onList, (v) => v.length, (d) => d.artist_id);
const firstSeen = d3.rollup(onList, (v) => d3.min(v, (d) => d.list_year), (d) => d.artist_id);
const shareOfSpots = (k) => 100 * d3.sum([...appearances.values()].filter((n) => n >= k)) / onList.length;
const shareOfArtists = (k) => 100 * [...appearances.values()].filter((n) => n >= k).length / appearances.size;
const isFirst = (d) => d.list_year === firstSeen.get(d.artist_id);
const firstTimers = (lo, hi) => onList.filter((d) => d.list_year >= lo && d.list_year <= hi);
```

```js
statTiles([
  {label: "Artists who made one list", value: `${(100 * [...appearances.values()].filter((n) => n === 1).length / appearances.size).toFixed(0)}%`,
   caption: "Share of all artists who have appeared on exactly one list. Most artists come once and don't return."},
  {label: "Spots held by regulars", value: `${shareOfSpots(5).toFixed(0)}%`,
   caption: `The ${shareOfArtists(5).toFixed(0)}% of artists with five or more albums on the lists hold this share of all the spots.`},
  {label: "Spots that go to first-timers", value: `${shareWhere(firstTimers(2011, 2015), isFirst).toFixed(0)}% → ${shareWhere(firstTimers(2021, 2025), isFirst).toFixed(0)}%`,
   caption: "Share of each period's entries from an artist's first appearance on any list, 2011–2015 compared with 2021–2025."}
])
```

Most artists do pass through once: ${(100 * [...appearances.values()].filter((n) => n === 1).length / appearances.size).toFixed(0)}% of everyone who has made a list made exactly one. But a small group of repeat artists holds far more than its share of the spots. The ${shareOfArtists(5).toFixed(0)}% of artists with five or more albums hold ${shareOfSpots(5).toFixed(0)}% of all the entries, and the ${lifeList().length} artists in the chart above are only ${shareOfArtists(7).toFixed(0)}% of artists but hold ${shareOfSpots(7).toFixed(0)}% of the spots. The door is still turning: about ${(firstTimers(2021, 2025).filter(isFirst).length / 5).toFixed(0)} artists a year make a list for the first time, or roughly one spot in three. It is turning a little more slowly than it used to, though, and that matches what the first chart showed. So the best way to put the two ideas together is a revolving door with a regular cast.

```js
addExpandButtons(() => document.querySelector(".dmo-seg")?.value);
```
