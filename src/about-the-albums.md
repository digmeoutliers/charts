---
title: About the albums
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
    // inside the blog post: no extra space above the first block or under the last one, so the text around the embed sits one normal paragraph gap away
    var trimmed, trimmedTop;
    function trimTail() {
      if (window.self === window.top) return;
      var kids = document.querySelectorAll("main > *"), i;
      for (i = kids.length - 1; i >= 0; i--) {
        if (kids[i].offsetHeight > 0) {
          if (trimmed && trimmed !== kids[i]) trimmed.style.marginBottom = "";
          kids[i].style.marginBottom = "0"; trimmed = kids[i];
          break;
        }
      }
      for (i = 0; i < kids.length; i++) {
        if (kids[i].offsetHeight > 0) {
          if (trimmedTop && trimmedTop !== kids[i]) trimmedTop.style.marginTop = "";
          kids[i].style.marginTop = "0"; trimmedTop = kids[i];
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
    var keepSwitch = false;
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

# About the albums

<div class="standalone-only" style="font-size:13px;color:var(--theme-foreground-muted);margin:0 0 1rem;"><strong>Draft</strong>: unlisted page, not part of the published blog yet.</div>

```js
import {makeTooltip} from "./components/tooltip.js";
import {addExpandButtons} from "./components/expand.js";
```

```js
const rows = FileAttachment("data/albums_2001_2025.csv").csv({typed: true});
const monthRows = FileAttachment("data/albums_release_months.csv").csv({typed: true});
```

```js
// ---- Palette: purple leads every hero chart; teal and gold mark smaller categories; white marks medians. ----
const PURPLE = "#9c57f3", TEAL = "#58cec8", GOLD = "#d6b45b", BLUE = "#6fa8ff", GREY = "#6b6a66";
const FG = "#f0efec", MID = "#c9c8c3", MUTED = "#898781", GRID = "#2c2c2a", SURFACE = "#1a1a19";
const SVG_STYLE = "max-width:100%;height:auto;display:block;font-family:var(--sans-serif);";
const years = d3.range(2001, 2026);
const tip = makeTooltip({minWidth: 150, maxWidth: 280});

const withRun = rows.filter((d) => d.runtime_min != null);
const studio = withRun.filter((d) => d.type === "Studio album");
const studioAndEP = withRun.filter((d) => d.type === "Studio album" || d.type === "Studio EP");
const studioIn = (lo, hi) => studio.filter((d) => d.list_year >= lo && d.list_year <= hi);
const medianOf = (r) => d3.median(r, (d) => d.runtime_min);
const meanOf = (r) => d3.mean(r, (d) => d.runtime_min);
const meanTracks = (r) => d3.mean(r, (d) => d.n_tracks);
const pct = (r, test) => 100 * r.filter(test).length / r.length;
const shareUnder = (r, mins) => pct(r, (d) => d.runtime_min < mins);
const shareOver = (r, mins) => pct(r, (d) => d.runtime_min >= mins);
const rowsIn = (lo, hi) => rows.filter((d) => d.list_year >= lo && d.list_year <= hi);
const eras = [[2001, 2005], [2006, 2010], [2011, 2015], [2016, 2020], [2021, 2025]];

// small pill buttons used inside the dark chart cards
function toggleBar(options, current, onPick) {
  const bar = document.createElement("div");
  bar.style.cssText = "display:flex;gap:8px;flex-wrap:wrap;margin:0 0 0.9rem;";
  const buttons = options.map(([value, label]) => {
    const b = document.createElement("button");
    b.type = "button"; b.textContent = label;
    b.onclick = () => { current = value; paint(); onPick(value); };
    bar.append(b);
    return [b, value];
  });
  function paint() {
    buttons.forEach(([b, v]) => {
      const on = v === current;
      b.style.cssText = `font-size:13px;font-family:var(--sans-serif);border-radius:999px;padding:5px 12px;cursor:pointer;border:1px solid ${on ? FG : "#383835"};background:${on ? FG : "#232321"};color:${on ? SURFACE : MID};font-weight:${on ? 600 : 400};`;
    });
  }
  paint();
  return bar;
}

// a row of color swatches with labels
function legend(items) {
  const el = document.createElement("div");
  el.style.cssText = "display:flex;gap:6px 16px;flex-wrap:wrap;margin:0 0 0.6rem;font-size:13px;color:#c9c8c3;font-family:var(--sans-serif);";
  items.forEach(([label, color]) => {
    const s = document.createElement("span");
    s.style.cssText = "display:inline-flex;align-items:center;gap:6px;";
    s.innerHTML = `<span style="width:11px;height:11px;border-radius:2px;background:${color};display:inline-block"></span>${label}`;
    el.append(s);
  });
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
const nAll = rows.length;
const nStudio = rows.filter((d) => d.type === "Studio album").length;
const nEP = rows.filter((d) => d.type === "Studio EP").length;
const early = studioIn(2001, 2005), late = studioIn(2021, 2025);
const first10 = studioIn(2001, 2010), last10 = studioIn(2016, 2025);
// split the drop in average length between "fewer tracks" and "shorter tracks"
const n1 = meanTracks(first10), n2 = meanTracks(last10), M1 = meanOf(first10), M2 = meanOf(last10);
const fromFewerTracks = (n1 - n2) * (M1 / n1);
const fromShorterTracks = (M1 - M2) - fromFewerTracks;
const perTrack = (r) => d3.sum(r, (d) => d.runtime_min) / d3.sum(r, (d) => d.n_tracks);
const epRuns = withRun.filter((d) => d.type === "Studio EP");
const epShift = d3.max(years, (yr) => Math.abs(medianOf(studioAndEP.filter((d) => d.list_year === yr)) - medianOf(studioIn(yr, yr))));
const titleShare = (lo, hi, key) => pct(rowsIn(lo, hi), (d) => d[key] === 1);
const datedRows = rows.filter((d) => d.release_month != null);
```

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Album length here is the runtime of the album's main release in MusicBrainz, the sum of its track lengths. If the main release is a deluxe edition, the runtime is the deluxe edition's, so a few individual albums run long. The medians barely move because of them, which is why the charts lean on medians and shares. ${nAll - withRun.length} albums with a missing track time, or under five minutes in total, are left out of the length charts. Studio album means MusicBrainz's type Album with no secondary type like live, compilation or soundtrack, and studio EP is the same for EPs. As everywhere in this series, the lists are KEXP listeners' favorites, so this is a picture of what one indie-leaning audience loves, not of the whole record business.</div>
</div>

<p class="phone-note">On a phone? Tap a row, bar or cell to see its details. These charts have more room on a laptop or tablet.</p>

## Albums are getting shorter, and the long ones are going

Each line below is one list year, 2001 at the top and 2025 at the bottom. A line's height at any point shows how many of that year's studio albums run that long, and the white dots mark the typical album, the median. "Studio albums" here means full-length albums only: EPs, live albums and compilations are left out. Hover a line to see the year's numbers. To compare years, pick up to three with the buttons or by clicking their lines, and they are drawn on top of each other underneath.

```js
function ridgeline() {
  const width = 880, m = {l: 64, r: 24, t: 50, b: 34};
  const lo = 10, hi = 90, bin = 2, nb = (hi - lo) / bin, rowH = 22, peak = 64;
  const W = width - m.l - m.r;
  const x = (v) => m.l + (v - lo) / (hi - lo) * W;
  const base = (i) => m.t + peak + i * rowH;
  const height = base(years.length - 1) + m.b;
  const dens = (yr) => {
    const vals = studioIn(yr, yr).map((d) => d.runtime_min), c = new Array(nb).fill(0);
    vals.forEach((v) => { if (v >= lo && v < hi) c[Math.floor((v - lo) / bin)]++; });
    const out = [];
    for (let i = 0; i < nb; i++) {
      let s = 0, w = 0;
      for (let j = -5; j <= 5; j++) { const k = i + j; if (k < 0 || k >= nb) continue; const g = Math.exp(-0.5 * (j / 1.6) ** 2); s += c[k] * g; w += g; }
      out.push(s / w / vals.length);
    }
    return out;
  };
  const D = years.map(dens), top = d3.max(D, (a) => d3.max(a));
  const SEL = [GOLD, BLUE, FG];            // colors for up to three picked years
  const picked = new Map();                // year -> color, oldest first
  function toggle(yr) {
    if (picked.has(yr)) { picked.delete(yr); return; }
    let color = SEL.find((c) => ![...picked.values()].includes(c));
    if (!color) { const oldest = picked.keys().next().value; color = picked.get(oldest); picked.delete(oldest); }
    picked.set(yr, color);
  }
  const wrap = document.createElement("div");
  const bar = document.createElement("div");
  bar.style.cssText = "display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 0.9rem;font-family:var(--sans-serif);";
  const holder = document.createElement("div"), compare = document.createElement("div");
  const chipCss = "font-size:12px;font-family:var(--sans-serif);border-radius:999px;padding:3px 9px;cursor:pointer;";
  const chipFor = new Map();
  const hint = document.createElement("span");
  hint.style.cssText = "font-size:13px;color:#c9c8c3;margin-right:4px;";
  hint.textContent = "Compare years:";
  bar.append(hint);
  years.forEach((yr) => {
    const b = document.createElement("button");
    b.type = "button"; b.textContent = yr;
    b.onclick = () => { toggle(yr); update(); };
    chipFor.set(yr, b); bar.append(b);
  });
  const preset = document.createElement("button");
  preset.type = "button"; preset.textContent = "2001 vs 2025";
  preset.onclick = () => { picked.clear(); toggle(2001); toggle(2025); update(); };
  const clear = document.createElement("button");
  clear.type = "button"; clear.textContent = "Clear";
  clear.onclick = () => { picked.clear(); update(); };
  [preset, clear].forEach((b) => { b.style.cssText = chipCss + "border:1px solid #8a8985;background:transparent;color:#f0efec;"; bar.append(b); });
  function paintChips() {
    years.forEach((yr) => {
      const c = picked.get(yr), b = chipFor.get(yr);
      b.style.cssText = chipCss + (c ? `border:1px solid ${c};background:${c};color:${SURFACE};font-weight:600;` : "border:1px solid #383835;background:#232321;color:#c9c8c3;");
    });
    clear.style.visibility = picked.size ? "visible" : "hidden";
  }

  function drawMain() {
    const any = picked.size > 0;
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", "Distribution of studio album length for each list year, 2001 at the top to 2025 at the bottom. The hump slides from about 48 minutes to about 42 and the tail of long albums thins out.");
    [20, 40, 60, 80].forEach((v) => {
      svg.append("line").attr("x1", x(v)).attr("x2", x(v)).attr("y1", m.t - 8).attr("y2", height - m.b + 6).attr("stroke", GRID);
      svg.append("text").attr("x", x(v)).attr("y", height - 8).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${v} min`);
    });
    years.forEach((yr, i) => {
      const c = picked.get(yr), ends = !any && (yr === 2001 || yr === 2025);
      const pts = D[i].map((v, k) => [x(lo + (k + 0.5) * bin), base(i) - v / top * peak]);
      const line = pts.map((p) => p.map((n) => n.toFixed(1)).join(",")).join(" L");
      svg.append("path").attr("d", `M${x(lo)},${base(i)} L${line} L${x(hi)},${base(i)} Z`).attr("fill", SURFACE);
      svg.append("polyline").attr("points", pts.map((p) => p.map((n) => n.toFixed(1)).join(",")).join(" ")).attr("fill", "none")
        .attr("stroke", c || (ends ? FG : PURPLE)).attr("stroke-opacity", any && !c ? 0.3 : 1).attr("stroke-width", c ? 2.6 : ends ? 2 : 1.2).attr("stroke-linejoin", "round");
      if (c || (!any && yr % 4 === 1)) svg.append("text").attr("x", m.l - 10).attr("y", base(i) + 4).attr("text-anchor", "end").attr("fill", c || (ends ? FG : MUTED)).attr("font-size", 12).attr("font-weight", c ? 600 : 400).text(yr);
    });
    const meds = years.map((yr, i) => [x(medianOf(studioIn(yr, yr))), base(i)]);
    if (!any) {
      svg.append("polyline").attr("points", meds.map((p) => p.join(",")).join(" ")).attr("fill", "none").attr("stroke", FG).attr("stroke-opacity", 0.7).attr("stroke-dasharray", "2 3").attr("pointer-events", "none");
      meds.forEach((p) => svg.append("circle").attr("cx", p[0]).attr("cy", p[1]).attr("r", 2.8).attr("fill", FG).attr("pointer-events", "none"));
    } else {
      years.forEach((yr, i) => { const c = picked.get(yr); if (c) svg.append("circle").attr("cx", meds[i][0]).attr("cy", meds[i][1]).attr("r", 4).attr("fill", c).attr("stroke", SURFACE).attr("stroke-width", 1.5).attr("pointer-events", "none"); });
    }
    // reference lines sit on top of the curves so they can be read all the way down
    [[44, "one LP, about 44 min", TEAL], [74, "CD, 74 min", "#a9a79f"]].forEach(([v, label, c]) => {
      svg.append("line").attr("x1", x(v)).attr("x2", x(v)).attr("y1", m.t - 8).attr("y2", height - m.b + 6).attr("stroke", c).attr("stroke-opacity", 0.85).attr("stroke-dasharray", "3 4").attr("pointer-events", "none");
      svg.append("text").attr("x", x(v)).attr("y", m.t - 16).attr("text-anchor", "middle").attr("fill", c).attr("font-size", 12).text(label);
    });
    // hover and click bands, on top of everything
    years.forEach((yr, i) => {
      const r = studioIn(yr, yr);
      const html = `<b>${yr} list</b><br>${r.length} studio albums with track times<br>Median <b>${medianOf(r).toFixed(1)} min</b><br><span style="color:#898781">${shareUnder(r, 46).toFixed(0)}% under 46 min &middot; ${shareOver(r, 60).toFixed(0)}% over 60 min</span><br><span style="color:#898781">Click to ${picked.has(yr) ? "remove from" : "add to"} the comparison</span>`;
      svg.append("rect").attr("x", m.l).attr("y", base(i) - rowH + 4).attr("width", W).attr("height", rowH).attr("fill", "transparent").style("cursor", "pointer")
        .on("pointerenter pointermove", (event) => tip.show(event, html)).on("pointerleave", (event) => tip.hide(event))
        .on("click", () => { tip.hideNow(); toggle(yr); update(); });
    });
    holder.innerHTML = ""; holder.append(svg.node());
  }

  // the picked years drawn on top of each other, same minutes axis
  function drawCompare() {
    compare.innerHTML = "";
    if (!picked.size) return;
    const h = 230, cm = {l: 64, r: 24, t: 14, b: 32};
    const cx = (v) => cm.l + (v - lo) / (hi - lo) * (width - cm.l - cm.r);
    const cy = (v) => h - cm.b - v / top * (h - cm.b - cm.t);
    const entries = [...picked].sort((a, b) => a[0] - b[0]);
    const key = document.createElement("div");
    key.style.cssText = "display:flex;flex-direction:column;gap:3px;margin:1rem 0 0.4rem;font-size:13px;color:#c9c8c3;font-family:var(--sans-serif);";
    entries.forEach(([yr, c]) => {
      const r = studioIn(yr, yr), line = document.createElement("div");
      line.innerHTML = `<span style="display:inline-block;width:11px;height:11px;border-radius:2px;background:${c};margin-right:8px"></span><b style="color:${FG}">${yr}</b>: median <b style="color:${FG}">${medianOf(r).toFixed(1)} min</b>, ${shareUnder(r, 46).toFixed(0)}% under 46 min, ${shareOver(r, 60).toFixed(0)}% over 60 min (${r.length} albums)`;
      key.append(line);
    });
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", "The chosen list years drawn on top of each other: how many studio albums run each length");
    [20, 40, 60, 80].forEach((v) => {
      svg.append("line").attr("x1", cx(v)).attr("x2", cx(v)).attr("y1", cm.t).attr("y2", h - cm.b).attr("stroke", GRID);
      svg.append("text").attr("x", cx(v)).attr("y", h - 10).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${v} min`);
    });
    svg.append("line").attr("x1", cm.l).attr("x2", width - cm.r).attr("y1", h - cm.b).attr("y2", h - cm.b).attr("stroke", "#4a4a46");
    entries.forEach(([yr, c]) => {
      const dd = D[years.indexOf(yr)];
      const pts = dd.map((v, k) => [cx(lo + (k + 0.5) * bin), cy(v)]);
      const path = pts.map((p) => p.map((n) => n.toFixed(1)).join(",")).join(" L");
      svg.append("path").attr("d", `M${cx(lo)},${cy(0)} L${path} L${cx(hi)},${cy(0)} Z`).attr("fill", c).attr("fill-opacity", 0.07);
      svg.append("polyline").attr("points", pts.map((p) => p.map((n) => n.toFixed(1)).join(",")).join(" ")).attr("fill", "none").attr("stroke", c).attr("stroke-width", 2.4).attr("stroke-linejoin", "round");
      const md = medianOf(studioIn(yr, yr));
      svg.append("line").attr("x1", cx(md)).attr("x2", cx(md)).attr("y1", cy(0)).attr("y2", cy(0) - 14).attr("stroke", c).attr("stroke-width", 3);
    });
    [44, 74].forEach((v) => svg.append("line").attr("x1", cx(v)).attr("x2", cx(v)).attr("y1", cm.t).attr("y2", h - cm.b).attr("stroke", v === 44 ? TEAL : "#a9a79f").attr("stroke-opacity", 0.85).attr("stroke-dasharray", "3 4"));
    compare.append(key, svg.node());
    const note = document.createElement("div");
    note.style.cssText = "font-size:12px;color:#898781;margin-top:4px;font-family:var(--sans-serif);";
    note.textContent = "Short bars on the baseline mark each year's median.";
    compare.append(note);
  }
  function update() { paintChips(); drawMain(); drawCompare(); }
  wrap.append(bar, holder, compare);
  update();
  return wrap;
}
```

<div class="card" data-chart="hero" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
ridgeline()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Studio albums only. The two white curves are 2001 and 2025, and the white dots and dotted line follow each year's median. The two dashed lines are for scale: teal is about what fits on one vinyl LP, and grey is the length of a standard CD. They are reference points, not explanations.</p>

In 2001 the typical studio album on the list ran ${medianOf(studioIn(2001, 2001)).toFixed(0)} minutes. In 2025 it ran ${medianOf(studioIn(2025, 2025)).toFixed(0)}. The bump in the 35 to 45 minute range was there from the start, so what has changed is everything to its right: albums that run 50, 60 or more minutes have been thinning out for a quarter century.

## What's on the lists

```js
statTiles([
  {label: "Albums on the lists", value: nAll.toLocaleString(), caption: "Every album on every Annual list, 2001 through 2025."},
  {label: "Typical studio album", value: `${medianOf(late).toFixed(0)} min`, caption: `Median length on the 2021–2025 lists, down from ${medianOf(early).toFixed(0)} minutes on the 2001–2005 lists.`},
  {label: "Fits on one LP", value: `${shareUnder(late, 46).toFixed(0)}%`, caption: `Share of 2021–2025 studio albums running under 46 minutes, up from ${shareUnder(early, 46).toFixed(0)}% in 2001–2005.`}
])
```

Studio albums are ${(100 * nStudio / nAll).toFixed(0)}% of the lists, which is why the hero chart is about them. Here is the rest of what shows up under "album", using the release types MusicBrainz keeps. EPs are counted separately, not as studio albums.

```js
function typeBar() {
  const order = [["Studio album", PURPLE], ["Studio EP", GOLD], ["Compilation", "#8f8e89"], ["Live", "#6f6e6a"], ["Soundtrack", "#56554f"], ["Mixtape", "#444340"], ["Remix album", "#3a3936"], ["Single, other or unknown", "#30302e"]];
  const counts = d3.rollup(rows, (v) => v.length, (d) => d.type);
  const width = 880, h = 34;
  const wrap = document.createElement("div");
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
    .attr("role", "img").attr("aria-label", `Albums by type: ${(100 * nStudio / nAll).toFixed(0)}% studio albums`);
  let xpos = 0;
  order.forEach(([name, color]) => {
    const n = counts.get(name) || 0, w = Math.max(n / nAll * width, 3);
    svg.append("rect").attr("x", xpos).attr("y", 0).attr("width", Math.max(w - 1, 2)).attr("height", h).attr("fill", color)
      .on("pointerenter pointermove", (event) => tip.show(event, `<b>${name}</b><br>${n.toLocaleString()} albums (${(100 * n / nAll).toFixed(1)}%)`)).on("pointerleave", (event) => tip.hide(event));
    xpos += w;
  });
  const key = document.createElement("div");
  key.style.cssText = "display:flex;gap:6px 18px;flex-wrap:wrap;margin-top:0.9rem;font-size:13px;color:#c9c8c3;font-family:var(--sans-serif);";
  order.forEach(([name, color]) => {
    const n = counts.get(name) || 0;
    const s = document.createElement("span");
    s.style.cssText = "display:inline-flex;align-items:center;gap:6px;";
    s.innerHTML = `<span style="width:11px;height:11px;border-radius:2px;background:${color};display:inline-block"></span>${name} <span style="color:#898781">${n.toLocaleString()}</span>`;
    key.append(s);
  });
  wrap.append(svg.node(), key);
  return wrap;
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem;max-width:900px;margin:0 auto;position:relative;">

```js
typeBar()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Type is MusicBrainz's primary and secondary release type. The studio EPs are ${nEP} of ${nAll.toLocaleString()} albums, and they show no trend across the 25 years.</p>

## When the albums come out

```js
function monthBars() {
  const width = 880, m = {l: 48, r: 16, t: 28, b: 34}, h = 260;
  const names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  const x = d3.scaleBand(d3.range(1, 13), [m.l, width - m.r]).padding(0.28);
  const topV = Math.ceil(d3.max(monthRows, (d) => Math.max(d.listed_albums, d.expected_from_ballots)) / 100) * 100;
  const y = d3.scaleLinear([0, topV], [h - m.b, m.t]);
  const wrap = document.createElement("div");
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
    .attr("role", "img").attr("aria-label", "Listed albums by release month, with the number the ballots predict. Most come out in spring and fall, and very few in November and December.");
  svg.append("rect").attr("x", x(11) - x.step() * 0.14).attr("y", m.t - 10).attr("width", x.step() * 2).attr("height", h - m.b - m.t + 10).attr("fill", "#232321");
  d3.range(0, topV + 1, 100).forEach((v) => {
    svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", GRID);
    svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MUTED).attr("font-size", 12).text(v);
  });
  monthRows.forEach((d) => {
    const html = `<b>${names[d.month - 1]}</b><br>${d.listed_albums} albums on the lists<br><span style="color:#898781">${d.expected_from_ballots} expected from the ballots</span>`;
    svg.append("rect").attr("x", x(d.month)).attr("y", y(d.listed_albums)).attr("width", x.bandwidth()).attr("height", y(0) - y(d.listed_albums)).attr("rx", 3).attr("fill", PURPLE)
      .on("pointerenter pointermove", (event) => tip.show(event, html)).on("pointerleave", (event) => tip.hide(event));
    svg.append("text").attr("x", x(d.month) + x.bandwidth() / 2).attr("y", h - m.b + 20).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(names[d.month - 1]);
  });
  const cx = (d) => x(d.month) + x.bandwidth() / 2;
  svg.append("polyline").attr("points", monthRows.map((d) => `${cx(d)},${y(d.expected_from_ballots)}`).join(" ")).attr("fill", "none").attr("stroke", FG).attr("stroke-width", 1.5).attr("stroke-dasharray", "3 3").attr("pointer-events", "none");
  monthRows.forEach((d) => svg.append("path").attr("d", `M${cx(d)},${y(d.expected_from_ballots) - 6} l6,6 l-6,6 l-6,-6 z`).attr("fill", FG).attr("stroke", SURFACE).attr("stroke-width", 1.5).attr("pointer-events", "none"));
  monthRows.forEach((d) => svg.append("text").attr("x", cx(d)).attr("y", Math.min(y(d.listed_albums), y(d.expected_from_ballots) - 6) - 8).attr("text-anchor", "middle").attr("fill", FG).attr("font-size", 12).attr("font-weight", 500).attr("pointer-events", "none").text(d.listed_albums));
  wrap.append(legend([["Albums on the lists", PURPLE], ["Expected, if the lists mirrored the ballots' candidates", FG]]), svg.node());
  return wrap;
}
```

<div class="card" data-chart="months" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
monthBars()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">${datedRows.length.toLocaleString()} of ${nAll.toLocaleString()} albums have a full release date in MusicBrainz. The diamonds show how many would come out in each month if the lists matched the share of ballot candidates released that month, using the seven KEXP ballots I could recover (2014, 2016, 2018, 2020, 2021, 2022 and 2023) and scaling to the same total.</p>

Albums come out all year, but not evenly: ${d3.sum(monthRows.filter((d) => d.month === 9 || d.month === 10), (d) => d.listed_albums).toLocaleString()} of the ${datedRows.length.toLocaleString()} came out in September or October, and only ${monthRows[6].listed_albums} in July. The summer dip and the fall peak show up in the ballot candidates too, so they reflect when records come out and not just what voters pick. Voting happens in the fall, which is why November and December are nearly empty: those albums mostly wait for next year's list.

## How the lengths changed

The ridgeline showed the shape. The heat map below counts instead: each column is a list year, each row is a stretch of five minutes, and a brighter cell means a bigger share of that year's studio albums sit there.

```js
function lengthHeat() {
  const width = 880, m = {l: 74, r: 64, t: 28, b: 34}, rowH = 27;
  const bins = d3.range(20, 85, 5), nb = bins.length;
  const cellW = (width - m.l - m.r) / years.length;
  const height = m.t + nb * rowH + m.b;
  const binOf = (v) => Math.max(0, Math.min(nb - 1, Math.floor((v - 20) / 5)));
  const grid = years.map((yr) => {
    const r = studioIn(yr, yr), c = new Array(nb).fill(0);
    r.forEach((d) => c[binOf(d.runtime_min)]++);
    return {yr, n: r.length, c};
  });
  const peak = d3.max(grid, (g) => d3.max(g.c.map((v) => v / g.n)));
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", SVG_STYLE)
    .attr("role", "img").attr("aria-label", "Heat map of the share of studio albums at each length, by list year. A bright band sits at 35 to 45 minutes throughout, and the 50 to 60 minute rows fade.");
  const label = (k) => k === 0 ? "under 25" : k === nb - 1 ? "80+" : `${bins[k]}–${bins[k] + 5}`;
  grid.forEach((g, i) => bins.forEach((b, k) => {
    const share = g.c[k] / g.n, row = nb - 1 - k;
    const range = k === 0 ? "under 25 min" : k === nb - 1 ? "80 min or more" : `${b} to ${b + 5} min`;
    svg.append("rect").attr("x", m.l + i * cellW).attr("y", m.t + row * rowH).attr("width", cellW - 2).attr("height", rowH - 2).attr("rx", 2)
      .attr("fill", PURPLE).attr("fill-opacity", 0.06 + 0.94 * Math.sqrt(share / peak))
      .on("pointerenter pointermove", (event) => tip.show(event, `<b>${g.yr} &middot; ${range}</b><br>${g.c[k]} of ${g.n} studio albums (${(100 * share).toFixed(0)}%)`)).on("pointerleave", (event) => tip.hide(event));
  }));
  bins.forEach((b, k) => svg.append("text").attr("x", m.l - 10).attr("y", m.t + (nb - 1 - k) * rowH + rowH / 2).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MUTED).attr("font-size", 12).text(label(k)));
  [2001, 2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", m.l + (yr - 2001) * cellW + cellW / 2 - 1).attr("y", height - 12).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(yr));
  svg.append("text").attr("x", m.l - 10).attr("y", m.t - 12).attr("text-anchor", "end").attr("fill", MUTED).attr("font-size", 12).text("minutes");
  const y44 = m.t + (nb - 1) * rowH + rowH - (44 - 20) / 5 * rowH - 1;
  svg.append("line").attr("x1", m.l).attr("x2", m.l + years.length * cellW).attr("y1", y44).attr("y2", y44).attr("stroke", TEAL).attr("stroke-dasharray", "3 4").attr("pointer-events", "none");
  svg.append("text").attr("x", m.l + years.length * cellW + 6).attr("y", y44).attr("dominant-baseline", "middle").attr("fill", TEAL).attr("font-size", 12).text("44 min");
  return svg.node();
}
```

<div class="card" data-chart="heat" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
lengthHeat()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Studio albums only. Brightness is the share of that year's albums in the row (square-root scaled so the thin rows stay visible), and the teal dashed line is about one vinyl LP.</p>

There is a bright ridge between 35 and 45 minutes in nearly every column, and it gets brighter. The 50 to 60 minute rows start strong and fade. In 2001 through 2005, ${shareOver(early, 46).toFixed(0)}% of studio albums ran 46 minutes or more. In 2021 through 2025, ${shareOver(late, 46).toFixed(0)}% did.

The next chart puts a number on it. It shows the median length by year, and a toggle switches to the share of albums in four length bands, five years at a time.

```js
const medianUI = {mode: new URLSearchParams(location.search).get("mode") || "studio"};
function medianChart() {
  const width = 880, m = {l: 62, r: 24, t: 30, b: 34}, h = 300;
  const wrap = document.createElement("div");
  const holder = document.createElement("div");
  function draw(mode) {
    medianUI.mode = mode;
    holder.innerHTML = "";
    if (mode === "bands") { holder.append(bandsView()); return; }
    const pool = mode === "studio" ? studio : studioAndEP;
    const series = years.map((yr) => ({yr, v: medianOf(pool.filter((d) => d.list_year === yr)), n: pool.filter((d) => d.list_year === yr).length}));
    const x = d3.scaleLinear([2001, 2025], [m.l, width - m.r]);
    const y = d3.scaleLinear([36, 54], [h - m.b, m.t]);
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", `Median length of ${mode === "studio" ? "studio albums" : "albums and EPs"} by list year, falling from about ${series[0].v.toFixed(0)} to about ${series[24].v.toFixed(0)} minutes.`);
    [36, 42, 48, 54].forEach((v) => {
      svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", GRID);
      svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MUTED).attr("font-size", 12).text(v);
    });
    svg.append("text").attr("x", m.l - 8).attr("y", m.t - 14).attr("text-anchor", "end").attr("fill", MUTED).attr("font-size", 12).text("minutes");
    svg.append("path").attr("d", d3.line().x((d) => x(d.yr)).y((d) => y(d.v)).curve(d3.curveMonotoneX)(series)).attr("fill", "none").attr("stroke", PURPLE).attr("stroke-width", 2.6).attr("stroke-linejoin", "round");
    [series[0], series[24]].forEach((d, i) => {
      svg.append("circle").attr("cx", x(d.yr)).attr("cy", y(d.v)).attr("r", 5).attr("fill", PURPLE).attr("stroke", SURFACE).attr("stroke-width", 2);
      svg.append("text").attr("x", x(d.yr) + (i ? -4 : 9)).attr("y", y(d.v) + (i ? 24 : -10)).attr("text-anchor", i ? "end" : "start").attr("fill", FG).attr("font-size", 13).attr("font-weight", 500).text(`${d.v.toFixed(0)} min`);
    });
    [2001, 2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", x(yr)).attr("y", h - 10).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(yr));
    series.forEach((d) => svg.append("circle").attr("cx", x(d.yr)).attr("cy", y(d.v)).attr("r", 9).attr("fill", "transparent")
      .on("pointerenter pointermove", (event) => tip.show(event, `<b>${d.yr} list</b><br>Median <b>${d.v.toFixed(1)} min</b><br><span style="color:#898781">${d.n} ${mode === "studio" ? "studio albums" : "albums and EPs"}</span>`)).on("pointerleave", (event) => tip.hide(event)));
    holder.append(svg.node());
  }
  function bandsView() {
    const bands = [["Under 30 min", (v) => v < 30, "#5f5e5a"], ["30 to 46 min", (v) => v >= 30 && v < 46, PURPLE], ["46 to 60 min", (v) => v >= 46 && v < 60, TEAL], ["Over 60 min", (v) => v >= 60, GOLD]];
    const bh = 280, bw = 96;
    const x = d3.scaleBand(eras.map((e) => e.join("–")), [m.l, width - m.r]).paddingInner(0.3).paddingOuter(0.15);
    const y = d3.scaleLinear([0, 100], [bh - m.b, m.t]);
    const out = document.createElement("div");
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, bh]).attr("width", width).attr("height", bh).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", "Share of studio albums in four length bands, by five-year group of lists. The 30 to 46 minute band grows and the longer bands shrink.");
    [0, 25, 50, 75, 100].forEach((v) => {
      svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", GRID);
      svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${v}%`);
    });
    eras.forEach(([lo, hi]) => {
      const r = studioIn(lo, hi);
      let acc = 0;
      bands.forEach(([name, test, color]) => {
        const share = pct(r, (d) => test(d.runtime_min)), x0 = x(`${lo}–${hi}`);
        svg.append("rect").attr("x", x0).attr("width", x.bandwidth()).attr("y", y(acc + share)).attr("height", Math.max(y(acc) - y(acc + share) - 1.5, 0.5)).attr("fill", color)
          .on("pointerenter pointermove", (event) => tip.show(event, `<b>${lo}–${hi} lists &middot; ${name}</b><br>${share.toFixed(0)}% of ${r.length} studio albums`)).on("pointerleave", (event) => tip.hide(event));
        if (share >= 7) svg.append("text").attr("x", x0 + x.bandwidth() / 2).attr("y", y(acc + share / 2)).attr("dominant-baseline", "middle").attr("text-anchor", "middle").attr("fill", color === PURPLE || color === "#5f5e5a" ? "#fff" : SURFACE).attr("font-size", 12).attr("font-weight", 500).attr("pointer-events", "none").text(`${share.toFixed(0)}%`);
        acc += share;
      });
      svg.append("text").attr("x", x(`${lo}–${hi}`) + x.bandwidth() / 2).attr("y", bh - 10).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${lo}–${String(hi).slice(2)}`);
    });
    out.append(legend(bands.map(([n, , c]) => [n, c])), svg.node());
    return out;
  }
  wrap.append(toggleBar([["studio", "Studio albums"], ["all", "Albums and EPs"], ["bands", "Length bands"]], medianUI.mode, draw), holder);
  draw(medianUI.mode);
  return wrap;
}
```

<div class="card" data-chart="median" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
medianChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Length comes from the main release's track times, as described in the note at the top. Adding the ${epRuns.length} EPs moves a year's median by at most ${epShift.toFixed(1)} minutes, so the shortening is not an EP effect.</p>

The typical studio album lost about ${(medianOf(early) - medianOf(late)).toFixed(0)} minutes between the first five lists and the last five. The bands show where it went: albums over 60 minutes slipped from ${shareOver(early, 60).toFixed(0)}% to ${shareOver(late, 60).toFixed(0)}%, albums of 46 to 60 minutes roughly halved, from ${pct(early, (d) => d.runtime_min >= 46 && d.runtime_min < 60).toFixed(0)}% to ${pct(late, (d) => d.runtime_min >= 46 && d.runtime_min < 60).toFixed(0)}%, and the 30 to 46 minute album became the standard.

### Fewer songs, or shorter songs?

An album can get shorter because it has fewer tracks or because the tracks are shorter. It is mostly fewer tracks. Studio albums on the 2001 through 2010 lists averaged ${n1.toFixed(1)} tracks, and on the 2016 through 2025 lists ${n2.toFixed(1)}. Songs did not get longer to make up for it: the average track barely changed, from ${perTrack(first10).toFixed(2)} minutes in the first group to ${perTrack(last10).toFixed(2)} in the second. Of the ${(M1 - M2).toFixed(1)} minute drop in the average album, about ${Math.abs(fromFewerTracks).toFixed(1)} minutes comes from having fewer tracks and about ${Math.abs(fromShorterTracks).toFixed(1)} from shorter ones.

```js
statTiles([
  {label: "Tracks per album", value: `${n1.toFixed(1)} → ${n2.toFixed(1)}`, caption: "Average tracks on a studio album, 2001–2010 lists compared with 2016–2025."},
  {label: "Average track", value: `${perTrack(first10).toFixed(2)} → ${perTrack(last10).toFixed(2)}`, caption: "Minutes per track over the same two periods. Songs are not getting longer."},
  {label: "Drop from fewer tracks", value: `${(100 * Math.abs(fromFewerTracks) / (M1 - M2)).toFixed(0)}%`, caption: `Share of the ${(M1 - M2).toFixed(1)} minute drop in the average album that comes from having fewer tracks.`}
])
```

The chart below shows every album, one bar per album, cut into its tracks. Slide through the years, or press Play. The dashed lines are the same two reference points as before, teal for one LP and grey for a CD.

```js
function trackChart() {
  const byYear = d3.group(withRun, (d) => d.list_year);
  const kindOf = (d) => d.type === "Studio album" ? 0 : d.type === "Studio EP" ? 1 : 2;
  const colors = [PURPLE, GOLD, GREY];
  const width = 880, X0 = 10, W = 860, maxMin = 90, px = W / maxMin, rowH = 8.4, TOP = 30;
  const maxRows = d3.max(years, (yr) => byYear.get(yr).length);
  const height = TOP + maxRows * rowH + 10;   // tallest year, so the card does not jump while playing
  let year = 2001, order = "rank", timer = null;
  const wrap = document.createElement("div");
  const yearLabel = document.createElement("span");
  yearLabel.style.cssText = `font-size:26px;font-weight:600;min-width:64px;color:${FG};font-family:var(--sans-serif);`;
  const play = document.createElement("button");
  const slider = document.createElement("input");
  const pillCss = "font-size:13px;font-family:var(--sans-serif);border-radius:999px;padding:5px 14px;cursor:pointer;border:1px solid #383835;background:#232321;color:#c9c8c3;";
  play.type = "button"; play.textContent = "Play"; play.style.cssText = pillCss;
  slider.type = "range"; slider.min = 2001; slider.max = 2025; slider.step = 1; slider.value = year; slider.setAttribute("aria-label", "List year");
  slider.style.cssText = `flex:1;min-width:160px;accent-color:${PURPLE};`;
  const top1 = document.createElement("div");
  top1.style.cssText = "display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:0 0 0.7rem;";
  top1.append(yearLabel, play, slider);
  const orderBar = toggleBar([["rank", "By list rank"], ["len", "Longest first"]], order, (v) => { order = v; draw(); });
  const stats = document.createElement("div");
  stats.style.cssText = "font-size:13px;line-height:1.5;color:#c9c8c3;margin:0 0 0.5rem;font-family:var(--sans-serif);";
  const chart = document.createElement("div");
  function draw() {
    const list = byYear.get(year).map((d) => ({d, kind: kindOf(d), t: String(d.track_seconds).split("|").map(Number), tot: d.runtime_min}));
    if (order === "len") list.sort((a, b) => b.tot - a.tot);
    const alb = list.filter((r) => r.kind === 0);
    yearLabel.textContent = year; slider.value = year;
    stats.innerHTML = `<b style="color:${FG}">${year}</b>: ${list.length} albums with track times. Studio albums: median <b style="color:${FG}">${d3.median(alb, (r) => r.tot).toFixed(1)} min</b>, average <b style="color:${FG}">${d3.mean(alb, (r) => r.t.length).toFixed(1)} tracks</b>, average track <b style="color:${FG}">${(d3.sum(alb, (r) => r.tot) / d3.sum(alb, (r) => r.t.length)).toFixed(1)} min</b>.`;
    const rowsBottom = TOP + list.length * rowH + 4;
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", `Every album on the ${year} list as a bar, cut into its tracks`);
    svg.append("text").attr("x", X0).attr("y", TOP - 14).attr("fill", MUTED).attr("font-size", 12).text("0 min");
    list.forEach((r, i) => {
      const y = TOP + i * rowH;
      const html = `<b>${r.d.artist_name}</b><br><i>${r.d.release_group_name}</i><br>${year} list &middot; #${r.d.rank}<br><span style="color:#898781">${r.t.length} tracks &middot; ${r.tot.toFixed(0)} min &middot; ${r.d.type}</span>`;
      const g = svg.append("g");
      let xp = X0;
      r.t.forEach((sec) => {
        const w = sec / 60 * px;
        if (xp - X0 >= W) return;
        g.append("rect").attr("x", xp).attr("y", y).attr("width", Math.max(Math.min(w, X0 + W - xp) - 1, 0.6)).attr("height", rowH - 1.8).attr("fill", colors[r.kind]);
        xp += w;
      });
      g.append("rect").attr("x", X0).attr("y", y).attr("width", W).attr("height", rowH - 1.8).attr("fill", "transparent")
        .on("pointerenter pointermove", (event) => tip.show(event, html)).on("pointerleave", (event) => tip.hide(event));
    });
    [[44, "one LP, about 44 min", TEAL], [74, "CD, 74 min", "#a9a79f"]].forEach(([v, label, c]) => {
      svg.append("line").attr("x1", X0 + v * px).attr("x2", X0 + v * px).attr("y1", TOP - 10).attr("y2", rowsBottom).attr("stroke", c).attr("stroke-opacity", 0.85).attr("stroke-dasharray", "3 4").attr("pointer-events", "none");
      svg.append("text").attr("x", X0 + v * px - 6).attr("y", TOP - 14).attr("text-anchor", "end").attr("fill", c).attr("font-size", 12).text(label);
    });
    chart.innerHTML = ""; chart.append(svg.node());
  }
  function stop() { if (timer) { clearInterval(timer); timer = null; } play.textContent = "Play"; }
  slider.oninput = () => { stop(); year = +slider.value; draw(); };
  play.onclick = () => {
    if (timer) { stop(); return; }
    if (year >= 2025) year = 2000;
    play.textContent = "Pause";
    timer = setInterval(() => { year++; draw(); if (year >= 2025) stop(); }, 1000);
  };
  wrap.append(top1, orderBar, legend([["Studio album", PURPLE], ["Studio EP", GOLD], ["Other (live, compilation, soundtrack)", GREY]]), stats, chart);
  draw();
  invalidation.then(stop);
  return wrap;
}
```

<div class="card" data-chart="tracks" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
trackChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">One bar per album, with a gap between tracks. Bars longer than 90 minutes run off the right edge. ${nAll - withRun.length} albums with missing track times are left out.</p>

## Some theories about why

This data can show that albums are getting shorter, but it can't say why. These are the explanations I have seen people give, and what the lists say about each one. None of this is proven, and a lot of it comes from musicians, engineers and fans talking, not from studies.

<!-- JOHN: this is the spot for quotes and links from engineers and the forum threads; none have been added yet. -->

**The CD gave way to the LP.** A CD can hold 74 to 80 minutes, so for years there was room to keep adding songs, and some albums did. A vinyl LP holds about 20 to 22 minutes a side before the sound starts to suffer, and a record longer than that needs two discs, which costs more to make and sell. As vinyl returned, a 40-minute album became the sensible size again. The lists fit that story: the share of studio albums under 46 minutes, about what fits on one LP, went from ${shareUnder(early, 46).toFixed(0)}% to ${shareUnder(late, 46).toFixed(0)}%. Two things argue for caution. Even on the 2001 through 2005 lists, only ${shareOver(early, 60).toFixed(0)}% of albums ran over 60 minutes, so these lists never leaned hard on the CD's full length. And the shortening began in the mid-2000s, well before vinyl's comeback was big. There is no format information in this data, so I can't tell which records were pressed on vinyl.

**Streaming changed the incentives.** In the streaming era an artist can release songs one at a time, apart from any album, and each one earns its own streams and, on a site like Bandcamp, its own purchases. If that is the plan, there is less reason to pack an album. I checked this against MusicBrainz's list of singles by the artists KEXP plays. Singles per album rose from about 1.5 in 2001 to about 3.8 since 2018, and the share of listed albums with at least one standalone single, meaning one that is not on the album, rose from 15% on the 2001 through 2005 lists to 45% on the 2021 through 2025 lists. The timing is the catch. Most of that rise came after 2017, while most of the drop in tracks per album had happened by about 2015, so singles don't explain the early part of the shortening. MusicBrainz's coverage of recent digital releases may also be better than its coverage of older ones, so some of the rise may be better record-keeping.

**More EPs.** If artists were splitting their songs across more releases, EPs should be on the rise. They aren't. EPs are ${(100 * nEP / nAll).toFixed(0)}% of the lists with no trend, and across all the releases MusicBrainz has for these artists, the EP share of albums plus EPs has not climbed either.

## Titles and EPs

A few smaller changes that came out of the same data.

```js
statTiles([
  {label: "Typical studio EP", value: `${medianOf(epRuns).toFixed(0)} min`, caption: `Median length of the ${epRuns.length} studio EPs on the lists. In every five-year group it sits between ${d3.min(eras, ([lo, hi]) => medianOf(epRuns.filter((d) => d.list_year >= lo && d.list_year <= hi))).toFixed(0)} and ${d3.max(eras, ([lo, hi]) => medianOf(epRuns.filter((d) => d.list_year >= lo && d.list_year <= hi))).toFixed(0)} minutes.`},
  {label: "Self-titled albums", value: `${titleShare(2001, 2010, "self_titled").toFixed(0)}% → ${titleShare(2016, 2025, "self_titled").toFixed(0)}%`, caption: "Share of albums whose title is the artist's name, 2001–2010 compared with 2016–2025."},
  {label: "One-word titles", value: `${titleShare(2001, 2010, "one_word").toFixed(0)}% → ${titleShare(2016, 2025, "one_word").toFixed(0)}%`, caption: "Share of albums with a one-word title, the same two periods."}
])
```

Self-titled albums have faded, and one-word titles have gone the other way. "Self-titled" here means the title matches the artist's name once a leading "The" is ignored, and a hyphenated word counts as one word.

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Here's what these charts can't tell us. Track times come from one release of each album, and I can't tell from this data whether a record was ever pressed on vinyl. The explanations above are theories: the lists show that albums got shorter and roughly when, not why. The singles and EP numbers cover all the releases MusicBrainz has for these artists, not only the albums on the lists, and MusicBrainz's record-keeping for recent digital releases may be more complete than for older ones.</div>
</div>

```js
addExpandButtons(() => medianUI.mode);
```
