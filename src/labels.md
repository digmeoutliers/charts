---
title: Who puts out the albums
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

# Who puts out the albums?

<div class="standalone-only" style="font-size:13px;color:var(--theme-foreground-muted);margin:0 0 1rem;"><strong>Draft</strong>: unlisted page, not part of the published blog yet.</div>

```js
import {makeTooltip} from "./components/tooltip.js";
import {addExpandButtons} from "./components/expand.js";
```

```js
const rows = FileAttachment("data/labels_2001_2025.csv").csv({typed: true});
```

```js
// ---- Palette: purple leads every hero chart; teal and gold mark smaller categories. ----
const PURPLE = "#9c57f3", TEAL = "#58cec8", GOLD = "#d6b45b", BLUE = "#6fa8ff", GREY = "#6b6a66", SILVER = "#b8b6ae";
const FG = "#f0efec", MID = "#c9c8c3", MUTED = "#898781", GRID = "#2c2c2a", SURFACE = "#1a1a19";
const SVG_STYLE = "max-width:100%;height:auto;display:block;font-family:var(--sans-serif);";
const years = d3.range(2001, 2026);
const tip = makeTooltip({minWidth: 150, maxWidth: 280});
const CLASS_COLOR = {"Independent": PURPLE, "Major": TEAL, "Self-released": GOLD, "No label on file": GOLD};

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
const inYears = (lo, hi) => rows.filter((d) => d.list_year >= lo && d.list_year <= hi);
const early = inYears(2001, 2010), late = inYears(2016, 2025), latest5 = inYears(2021, 2025);
const pctOf = (r, test) => 100 * r.filter(test).length / r.length;
const shareClass = (r, cls) => pctOf(r, (d) => d.owner_class === cls);
const shareFamily = (r, fam) => pctOf(r, (d) => d.family === fam);
const short = (l) => l === "Warner Records" ? l : l.replace(/ (Records|Recordings)$/, "");   // names as shown: Sub Pop, not Sub Pop Records
const words = ["No", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"];
const named = rows.filter((d) => d.owner_class === "Independent" || d.owner_class === "Major");   // albums on a named label
const labelCounts = d3.rollups(named, (v) => ({n: v.length, lists: new Set(v.map((d) => d.list_year)).size, cls: v[0].owner_class, fam: v[0].family}), (d) => d.label)
  .map(([label, o]) => ({label, ...o})).sort((a, b) => d3.descending(a.n, b.n) || d3.ascending(a.label, b.label));
const topTen = d3.sum(labelCounts.slice(0, 10), (d) => d.n), topTwentyFive = d3.sum(labelCounts.slice(0, 25), (d) => d.n);
const onEveryList = labelCounts.filter((d) => d.lists === 25);
const oneYearOnly = labelCounts.filter((d) => d.lists === 1).length;
const listLength = d3.rollup(rows, (v) => d3.max(v, (d) => d.rank), (d) => d.list_year);
const rankShare = (d) => d.rank / listLength.get(d.list_year);
const top10Rows = rows.filter((d) => d.rank <= 10);
const numberOnes = rows.filter((d) => d.rank === 1);
const changedHands = rows.filter((d) => d.changed_hands === 1).length;
const countIn = (r, label) => r.filter((d) => d.label === label).length;
const moverRows = labelCounts.filter((d) => d.label !== "[no label]").map((d) => ({...d, a: countIn(early, d.label), b: countIn(late, d.label)}))
  .map((d) => ({...d, change: d.b - d.a}));
const risers = moverRows.slice().sort((x, y) => d3.descending(x.change, y.change)).slice(0, 8);
const fallers = moverRows.slice().sort((x, y) => d3.ascending(x.change, y.change)).slice(0, 8);
const selfEarly = early.filter((d) => d.owner_class === "Self-released").length, selfLate = late.filter((d) => d.owner_class === "Self-released").length;
// label country, for the albums where it is on file (worldwide labels left out)
const withCountry = rows.filter((d) => d.label_country && d.label_country !== "XW");
const countryEarly = withCountry.filter((d) => d.list_year <= 2010), countryLate = withCountry.filter((d) => d.list_year >= 2016);
const ukArtists = withCountry.filter((d) => d.artist_country === "GB");
const ukOnUs = ukArtists.filter((d) => d.label_country === "US");
const sameCountry = withCountry.filter((d) => d.artist_country);
```

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">A label here is the first-listed label on the release of each album that KEXP played, as MusicBrainz records it. Where an album lists more than one label, I count the first. "Major" means a label owned today by Universal, Sony or Warner at 50% or more, which is how the UK trade body AIM draws the line. Everything else is independent, including labels that are only distributed by a major, and "self-released" means MusicBrainz shows no label. Ownership changes over time, so I use who owns the label today: ${changedHands} entries sit on labels that have changed hands, and a label that was independent when its album came out may count as major here (or the other way around). The classification is my own hand-made list. About 80% of entries sit on labels I checked one by one; the rest are small labels with one or two entries each, labelled independent by default. Details are in Data Notes. As everywhere in this series, the lists are KEXP listeners' favorites, so this is a picture of what one indie-leaning audience loves, not of the whole record business.</div>
</div>

<p class="phone-note">On a phone? Tap a row, bar or cell to see its details. These charts have more room on a laptop or tablet.</p>

## The biggest labels on the lists, ranked by albums

Each line follows one label's rank by number of albums, in five-year groups of lists. A line starts the first time a label reaches the top spots and ends when it drops out of them. Hover or tap a line to follow one label, and switch between the top 5, 10 and 15.

```js
const bumpUI = {top: ["5", "10", "15"].includes(new URLSearchParams(location.search).get("mode")) ? new URLSearchParams(location.search).get("mode") : "10"};
const BANDS = [[2001, 2005], [2006, 2010], [2011, 2015], [2016, 2020], [2021, 2025]];
// each label's albums and rank in each five-year group (ties broken by the label's total over all 25 lists, then by name)
const bumpCounts = BANDS.map(([lo, hi]) => d3.rollup(named.filter((d) => d.label !== "[no label]" && d.list_year >= lo && d.list_year <= hi), (v) => v.length, (d) => d.label));
const labelTotal = new Map(labelCounts.map((d) => [d.label, d.n]));
const labelInfo = new Map(labelCounts.map((d) => [d.label, d]));
const bumpRanks = bumpCounts.map((m) => new Map([...m].sort((a, b) => d3.descending(a[1], b[1]) || d3.descending(labelTotal.get(a[0]), labelTotal.get(b[0])) || d3.ascending(a[0], b[0])).map(([l], i) => [l, i + 1])));
function bumpChart() {
  const width = 880, m = {l: 140, r: 140, t: 30, b: 14};
  const wrap = document.createElement("div");
  const holder = document.createElement("div");
  const clip = (s) => s.length > 17 ? s.slice(0, 16) + "…" : s;
  function draw(topValue) {
    bumpUI.top = topValue;
    holder.innerHTML = "";
    const N = +topValue, rowH = Math.min(64, 440 / (N - 1)), h = m.t + (N - 1) * rowH + m.b + 10;
    const x = d3.scalePoint(BANDS.map((b) => b.join("–")), [m.l, width - m.r]);
    const y = (r) => m.t + (r - 1) * rowH;
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", `How the ${N} biggest labels rank by number of albums on the lists, in five-year groups from 2001 to 2025. Sub Pop stays first throughout; Columbia and the Secretly Group labels climb; Capitol and Astralwerks fall away.`);
    BANDS.forEach((b) => svg.append("text").attr("x", x(b.join("–"))).attr("y", 14).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(b.join("–")));
    d3.range(1, N + 1).forEach((r) => {
      svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(r)).attr("y2", y(r)).attr("stroke", GRID).attr("stroke-dasharray", "1 4");
      svg.append("text").attr("x", 4).attr("y", y(r)).attr("dominant-baseline", "middle").attr("fill", "#5f5e5a").attr("font-size", 11).text(r);
    });
    const shown = [...labelInfo.values()].filter((d) => d3.min(bumpRanks, (r) => r.get(d.label) || 99) <= N);
    const groups = new Map();
    let pinned = null;
    function focus(label) { groups.forEach((g, l) => g.attr("opacity", !label || l === label ? 1 : 0.13)); }
    shown.forEach((d) => {
      const color = d.cls === "Major" ? TEAL : PURPLE;
      const pts = BANDS.map((b, i) => ({i, key: b.join("–"), r: bumpRanks[i].get(d.label), n: bumpCounts[i].get(d.label) || 0})).map((q) => ({...q, ok: q.r && q.r <= N}));
      const g = svg.append("g").attr("opacity", 1).style("transition", "opacity .15s");
      groups.set(d.label, g);
      const line = d3.line().defined((q) => q.ok).x((q) => x(q.key)).y((q) => y(q.r)).curve(d3.curveMonotoneX);
      g.append("path").attr("d", line(pts)).attr("fill", "none").attr("stroke", color).attr("stroke-width", 3).attr("stroke-opacity", 0.92);
      pts.filter((q) => q.ok).forEach((q) => g.append("circle").attr("cx", x(q.key)).attr("cy", y(q.r)).attr("r", 5.5).attr("fill", color).attr("stroke", SURFACE).attr("stroke-width", 2));
      // name each unbroken run at its start and at its end
      let run = [];
      const runs = [];
      pts.forEach((q) => { if (q.ok) run.push(q); else if (run.length) { runs.push(run); run = []; } });
      if (run.length) runs.push(run);
      runs.forEach((rn) => {
        const first = rn[0], last = rn[rn.length - 1];
        const put = (q, left) => g.append("text").attr("x", x(q.key) + (left ? -12 : 12)).attr("y", y(q.r)).attr("text-anchor", left ? "end" : "start").attr("dominant-baseline", "middle")
          .attr("fill", color).attr("stroke", SURFACE).attr("stroke-width", 3.5).attr("paint-order", "stroke").attr("font-size", 13).attr("font-weight", 600).attr("pointer-events", "none").text(clip(short(d.label)));
        if (last === first && first.i === BANDS.length - 1) { put(first, false); return; }   // a lone dot in the last column is named on its right
        put(first, true);
        if (last !== first) put(last, false);
      });
      const rowsHtml = pts.map((q) => `${q.key}: ${q.n ? `<b>#${q.r}</b> · ${q.n} album${q.n === 1 ? "" : "s"}` : "none"}`).join("<br>");
      const html = `<b>${short(d.label)}</b><br><span style="color:#898781">${d.cls === "Major" ? "Major-owned" : "Independent"}${d.fam && d.fam !== d.label ? " · " + d.fam : ""}</span><br>${rowsHtml}`;
      g.append("path").attr("d", line(pts)).attr("fill", "none").attr("stroke", "transparent").attr("stroke-width", 18).attr("pointer-events", "stroke").style("cursor", "pointer")
        .on("pointerenter pointermove", (event) => { focus(d.label); tip.show(event, html); })
        .on("pointerleave", (event) => { focus(pinned); tip.hide(event); })
        .on("click", (event) => { pinned = pinned === d.label ? null : d.label; focus(pinned); event.stopPropagation(); });
    });
    svg.on("click", () => { pinned = null; focus(null); });
    holder.append(legend([["Independent", PURPLE], ["Major-owned", TEAL]]), svg.node());
  }
  wrap.append(toggleBar([["5", "Top 5"], ["10", "Top 10"], ["15", "Top 15"]], bumpUI.top, draw), holder);
  draw(bumpUI.top);
  return wrap;
}
```

<div class="card" data-chart="rank" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
bumpChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Rank by number of albums in each five-year group of lists. Ties are broken by the label's total across all 25 lists. Albums with no label, or self-released, are not ranked. A line ends where a label drops out of the top spots shown.</p>


## Interesting observations

The chart above follows individual labels. The sections below take the picture apart: how the majors faded, who the biggest labels are overall, who rose and fell, and where the labels are based.

In 2001, ${shareClass(inYears(2001, 2001), "Major").toFixed(0)}% of the albums on the list came from a major-owned label. In 2025 it was ${shareClass(inYears(2025, 2025), "Major").toFixed(0)}%. Independents rose from ${shareClass(inYears(2001, 2001), "Independent").toFixed(0)}% to ${shareClass(inYears(2025, 2025), "Independent").toFixed(0)}% over the same stretch. Most of the decline is one company's labels: Universal's went from ${shareFamily(early, "Universal Music Group").toFixed(1)}% of entries on the 2001 to 2010 lists to ${shareFamily(late, "Universal Music Group").toFixed(1)}% on the 2016 to 2025 lists, while Warner's (${shareFamily(early, "Warner Music Group").toFixed(1)}% to ${shareFamily(late, "Warner Music Group").toFixed(1)}%) and Sony's (${shareFamily(early, "Sony Music Entertainment").toFixed(1)}% to ${shareFamily(late, "Sony Music Entertainment").toFixed(1)}%) barely moved.

### Majors and independents, year by year

Each bar is one list year, split by who owns the label the album came out on. Switch to see the major slice split by owner, and hover a bar for the counts.

```js
const heroUI = {mode: new URLSearchParams(location.search).get("mode") === "owners" ? "owners" : "class"};
function ownerGroup(d) {
  if (d.owner_class === "Independent") return "Independent";
  if (d.owner_class === "Major") return {"Universal Music Group": "Universal", "Sony Music Entertainment": "Sony", "Warner Music Group": "Warner"}[d.family] || "Major";
  return "Self-released or no label";
}
const GROUP_COLOR = {"Independent": PURPLE, "Universal": TEAL, "Sony": BLUE, "Warner": SILVER, "Major": TEAL, "Self-released or no label": GOLD};
function heroChart() {
  const width = 880, h = 340, m = {l: 48, r: 16, t: 24, b: 34};
  const wrap = document.createElement("div");
  const holder = document.createElement("div");
  function draw(mode) {
    heroUI.mode = mode;
    holder.innerHTML = "";
    const order = mode === "owners" ? ["Independent", "Universal", "Sony", "Warner", "Self-released or no label"] : ["Independent", "Major", "Self-released or no label"];
    const group = (d) => mode === "owners" ? ownerGroup(d) : (d.owner_class === "Major" ? "Major" : ownerGroup(d));
    const x = d3.scaleBand(years, [m.l, width - m.r]).paddingInner(0.18);
    const y = d3.scaleLinear([0, 100], [h - m.b, m.t]);
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", "Share of each list year's albums by label owner, 2001 to 2025. Independent labels grow and major labels shrink.");
    [0, 25, 50, 75, 100].forEach((v) => {
      svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : GRID);
      svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${v}%`);
    });
    years.forEach((yr) => {
      const r = rows.filter((d) => d.list_year === yr);
      const counts = d3.rollup(r, (v) => v.length, group);
      let acc = 0;
      const lines = [];
      order.forEach((g) => {
        const n = counts.get(g) || 0, share = 100 * n / r.length;
        if (n) svg.append("rect").attr("x", x(yr)).attr("width", x.bandwidth()).attr("y", y(acc + share)).attr("height", Math.max(y(acc) - y(acc + share) - 1, 0.5)).attr("fill", GROUP_COLOR[g]);
        lines.push(`<span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:${GROUP_COLOR[g]};margin-right:6px"></span>${g}: <b>${share.toFixed(0)}%</b> (${n})`);
        acc += share;
      });
      const html = `<b>${yr} list</b><br>${lines.join("<br>")}`;
      svg.append("rect").attr("x", x(yr) - 2).attr("width", x.bandwidth() + 4).attr("y", m.t).attr("height", h - m.t - m.b).attr("fill", "transparent")
        .on("pointerenter pointermove", (event) => tip.show(event, html)).on("pointerleave", (event) => tip.hide(event));
    });
    [2001, 2005, 2010, 2015, 2020, 2025].forEach((yr) => svg.append("text").attr("x", x(yr) + x.bandwidth() / 2).attr("y", h - 10).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(yr));
    holder.append(legend(order.map((g) => [g, GROUP_COLOR[g]])), svg.node());
  }
  wrap.append(toggleBar([["class", "Independent and major"], ["owners", "Majors by owner"]], heroUI.mode, draw), holder);
  draw(heroUI.mode);
  return wrap;
}
```

<div class="card" data-chart="shares" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
heroChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Owner is who owns the label today, not when the album came out. "Self-released or no label" is ${rows.filter((d) => d.owner_class === "Self-released").length} albums MusicBrainz shows with no label plus ${rows.filter((d) => d.owner_class === "No label on file").length} with no label on file.</p>

### Majors faded, but they still land near the top

```js
statTiles([
  {label: "Major-owned labels", value: `${shareClass(early, "Major").toFixed(0)}% → ${shareClass(late, "Major").toFixed(0)}%`, caption: "Share of albums on a major-owned label, 2001–2010 lists compared with 2016–2025."},
  {label: "Top ten spots", value: `${pctOf(top10Rows, (d) => d.owner_class === "Major").toFixed(0)}%`, caption: `Share of top ten places that went to a major-owned label, against ${shareClass(rows, "Major").toFixed(0)}% of all entries.`},
  {label: "Number ones", value: `${numberOnes.filter((d) => d.owner_class === "Major").length} of ${numberOnes.length}`, caption: `Albums that finished #1 on a major-owned label, against ${numberOnes.filter((d) => d.owner_class === "Independent").length} on independents.`}
])
```

A major album that makes the list does well. Measured as a share of the list, the average major album finishes about ${(100 * (d3.mean(rows.filter((d) => d.owner_class === "Independent"), rankShare) - d3.mean(rows.filter((d) => d.owner_class === "Major"), rankShare))).toFixed(0)} percentage points higher than the average independent one (${d3.mean(rows.filter((d) => d.owner_class === "Major"), rankShare).toFixed(2)} of the way down the list against ${d3.mean(rows.filter((d) => d.owner_class === "Independent"), rankShare).toFixed(2)}).

### Who puts them out

Sub Pop is KEXP's hometown label, and since July 1, 2025 it has run a pop-up record store in the [gathering space at KEXP's headquarters](https://www.subpop.com/sub_pop_in_the_kexp_gathering_space).

```js
const leagueUI = {period: "all"};
function leagueChart() {
  const width = 880, m = {l: 150, r: 150, t: 8, b: 6}, rowH = 22, N = 25;
  const wrap = document.createElement("div");
  const holder = document.createElement("div");
  const periods = {all: [2001, 2025, "all 25 lists"], early: [2001, 2010, "the 2001 to 2010 lists"], late: [2016, 2025, "the 2016 to 2025 lists"]};
  function draw(period) {
    leagueUI.period = period;
    holder.innerHTML = "";
    const [lo, hi, nameOfPeriod] = periods[period];
    const r = named.filter((d) => d.list_year >= lo && d.list_year <= hi);
    const top = d3.rollups(r, (v) => ({n: v.length, lists: new Set(v.map((d) => d.list_year)).size, cls: v[0].owner_class, fam: v[0].family, owner: v[0].owner_today}), (d) => d.label)
      .map(([label, o]) => ({label, ...o})).sort((a, b) => d3.descending(a.n, b.n) || d3.ascending(a.label, b.label)).slice(0, N);
    const h = m.t + N * rowH + m.b;
    const x = d3.scaleLinear([0, d3.max(top, (d) => d.n)], [m.l, width - m.r]);
    const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
      .attr("role", "img").attr("aria-label", `The ${N} biggest labels by number of albums on ${nameOfPeriod}`);
    const nLists = hi - lo + 1;
    top.forEach((d, i) => {
      const y0 = m.t + i * rowH;
      const html = `<b>${short(d.label)}</b><br>${d.n} albums on ${nameOfPeriod}<br>On ${d.lists} of ${nLists} lists<br><span style="color:#898781">${d.cls === "Major" ? "Major-owned" : "Independent"}${d.fam && d.fam !== d.label ? " · " + d.fam : ""}</span>`;
      svg.append("text").attr("x", m.l - 8).attr("y", y0 + rowH / 2).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MID).attr("font-size", 13).text(short(d.label).length > 22 ? short(d.label).slice(0, 21) + "…" : short(d.label));
      svg.append("rect").attr("x", m.l).attr("y", y0 + 3).attr("width", Math.max(x(d.n) - m.l, 1)).attr("height", rowH - 7).attr("rx", 2).attr("fill", CLASS_COLOR[d.cls]);
      svg.append("text").attr("x", x(d.n) + 6).attr("y", y0 + rowH / 2).attr("dominant-baseline", "middle").attr("fill", FG).attr("font-size", 12).attr("font-weight", 500).text(d.n);
      svg.append("text").attr("x", width - m.r + 46).attr("y", y0 + rowH / 2).attr("dominant-baseline", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${d.lists} of ${nLists} lists`);
      svg.append("rect").attr("x", 0).attr("y", y0).attr("width", width).attr("height", rowH).attr("fill", "transparent")
        .on("pointerenter pointermove", (event) => tip.show(event, html)).on("pointerleave", (event) => tip.hide(event));
    });
    holder.append(legend([["Independent", PURPLE], ["Major-owned", TEAL]]), svg.node());
  }
  wrap.append(toggleBar([["all", "All 25 lists"], ["early", "2001–2010"], ["late", "2016–2025"]], leagueUI.period, draw), holder);
  draw(leagueUI.period);
  return wrap;
}
```

<div class="card" data-chart="labels" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
leagueChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">The ${labelCounts.length} named labels behind ${named.length.toLocaleString()} albums. Albums with no label, or self-released, are left out of the bars.</p>

```js
statTiles([
  {label: "Labels", value: `${labelCounts.length}`, caption: `Named labels behind the ${named.length.toLocaleString()} albums with a label on file. ${oneYearOnly} of them appear in only one list year.`},
  {label: "Top ten", value: `${(100 * topTen / nAll).toFixed(0)}%`, caption: `Share of all entries held by the ten biggest labels (the top 25 hold ${(100 * topTwentyFive / nAll).toFixed(0)}%).`},
  {label: "On every list", value: `${onEveryList.length}`, caption: `${onEveryList.map((d) => `${short(d.label)} (${d.n} entries)`).join(" and ")}.`}
])
```

The league table: ${labelCounts.slice(0, 10).map((d) => `${short(d.label)} ${d.n}`).join(", ")}. ${words[labelCounts.slice(0, 12).filter((d) => d.cls === "Major").length]} majors make the top twelve: ${labelCounts.slice(0, 12).filter((d) => d.cls === "Major").map((d) => short(d.label)).join(", ")}.

### The families behind the names

Labels have owners, and a few families sit behind many of the names on the lists. The Beggars Group (Matador, 4AD, XL, Rough Trade, Young and Beggars Banquet) held about ${shareFamily(early, "Beggars Group").toFixed(0)}% of entries on the early lists and about ${shareFamily(late, "Beggars Group").toFixed(0)}% on the recent ones, about one album in ten. The Secretly Group (Jagjaguwar, Dead Oceans and Secretly Canadian) went from ${shareFamily(early, "Secretly Group").toFixed(1)}% to ${shareFamily(late, "Secretly Group").toFixed(1)}%.

```js
function familyChart() {
  const width = 880, m = {l: 190, r: 70, t: 4, b: 6}, rowH = 40;
  const fams = d3.rollups(named, (v) => v.length, (d) => d.family).sort((a, b) => d3.descending(a[1], b[1])).slice(0, 8).map(([f]) => f);
  const h = m.t + fams.length * rowH + m.b;
  const peak = d3.max(fams, (f) => Math.max(shareFamily(early, f), shareFamily(late, f)));
  const x = d3.scaleLinear([0, peak], [m.l, width - m.r]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
    .attr("role", "img").attr("aria-label", "Share of albums from each of the eight biggest label families, 2001 to 2010 lists compared with 2016 to 2025");
  fams.forEach((f, i) => {
    const y0 = m.t + i * rowH, e = shareFamily(early, f), l = shareFamily(late, f);
    const members = d3.rollups(named.filter((d) => d.family === f), (v) => v.length, (d) => d.label).sort((a, b) => d3.descending(a[1], b[1])).slice(0, 6).map(([n]) => n).join(", ");
    const html = `<b>${f}</b><br>2001–2010: <b>${e.toFixed(1)}%</b> of entries<br>2016–2025: <b>${l.toFixed(1)}%</b><br><span style="color:#898781">${members}</span>`;
    svg.append("text").attr("x", m.l - 10).attr("y", y0 + rowH / 2).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MID).attr("font-size", 13).text(f.replace(" Music Entertainment", "").replace(" Music Group", "'s labels").replace("Universal", "Universal").replace("Merge Records", "Merge"));
    [[e, GREY, 7], [l, PURPLE, 21]].forEach(([v, c, off]) => {
      svg.append("rect").attr("x", m.l).attr("y", y0 + off - 4).attr("width", Math.max(x(v) - m.l, 1)).attr("height", 11).attr("rx", 2).attr("fill", c);
      svg.append("text").attr("x", x(v) + 6).attr("y", y0 + off + 1.5).attr("dominant-baseline", "middle").attr("fill", FG).attr("font-size", 12).text(`${v.toFixed(1)}%`);
    });
    svg.append("rect").attr("x", 0).attr("y", y0).attr("width", width).attr("height", rowH).attr("fill", "transparent")
      .on("pointerenter pointermove", (event) => tip.show(event, html)).on("pointerleave", (event) => tip.hide(event));
  });
  const wrap = document.createElement("div");
  wrap.append(legend([["2001–2010 lists", GREY], ["2016–2025 lists", PURPLE]]), svg.node());
  return wrap;
}
```

<div class="card" data-chart="families" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
familyChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Share of all entries on the 2001 to 2010 and 2016 to 2025 lists. Families are my own grouping of labels under a common owner, as of today (see the note at the top).</p>

```js
statTiles([
  {label: "Universal's labels", value: `${shareFamily(early, "Universal Music Group").toFixed(0)}% → ${shareFamily(late, "Universal Music Group").toFixed(0)}%`, caption: "Share of entries, 2001–2010 compared with 2016–2025."},
  {label: "Beggars Group", value: `${shareFamily(early, "Beggars Group").toFixed(0)}% → ${shareFamily(late, "Beggars Group").toFixed(0)}%`, caption: "Matador, 4AD, XL, Rough Trade and others, about one album in ten throughout."},
  {label: "Secretly Group", value: `${shareFamily(early, "Secretly Group").toFixed(0)}% → ${shareFamily(late, "Secretly Group").toFixed(0)}%`, caption: "Jagjaguwar, Dead Oceans and Secretly Canadian."}
])
```

### Risers and fallers

```js
function moversChart() {
  const width = 880, m = {l: 170, r: 90, t: 6, b: 6}, rowH = 24, mid = m.l + (width - m.l - m.r) / 2;
  const list = [...risers.slice(0, 8), ...fallers.slice(0, 8).reverse()];
  const h = m.t + list.length * rowH + m.b + 28;
  const span = d3.max(list, (d) => Math.abs(d.change));
  const half = (width - m.l - m.r) / 2;
  const x = d3.scaleLinear([-span, span], [mid - half, mid + half]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
    .attr("role", "img").attr("aria-label", "Labels that gained and lost the most albums between the 2001 to 2010 lists and the 2016 to 2025 lists");
  svg.append("text").attr("x", mid + 8).attr("y", 14).attr("fill", PURPLE).attr("font-size", 12).attr("font-weight", 600).text("Gained albums");
  svg.append("text").attr("x", mid - 8).attr("y", 14).attr("text-anchor", "end").attr("fill", GOLD).attr("font-size", 12).attr("font-weight", 600).text("Lost albums");
  svg.append("line").attr("x1", mid).attr("x2", mid).attr("y1", 22).attr("y2", h - m.b).attr("stroke", "#4a4a46");
  list.forEach((d, i) => {
    const y0 = 28 + m.t + i * rowH, gain = d.change > 0;
    const html = `<b>${short(d.label)}</b><br>${d.a} albums on the 2001–2010 lists<br>${d.b} on the 2016–2025 lists<br><span style="color:#898781">${d.cls === "Major" ? "Major-owned" : "Independent"}</span>`;
    svg.append("text").attr("x", gain ? m.l - 10 : width - m.r + 10).attr("y", y0 + rowH / 2).attr("text-anchor", gain ? "end" : "start").attr("dominant-baseline", "middle").attr("fill", MID).attr("font-size", 13).text(short(d.label).length > 20 ? short(d.label).slice(0, 19) + "…" : short(d.label));
    svg.append("rect").attr("x", Math.min(mid, x(d.change))).attr("y", y0 + 4).attr("width", Math.abs(x(d.change) - mid)).attr("height", rowH - 9).attr("rx", 2).attr("fill", d.cls === "Major" ? TEAL : (gain ? PURPLE : GREY));
    svg.append("text").attr("x", gain ? x(d.change) + 6 : x(d.change) - 6).attr("y", y0 + rowH / 2).attr("text-anchor", gain ? "start" : "end").attr("dominant-baseline", "middle").attr("fill", FG).attr("font-size", 12).attr("font-weight", 500).text(`${d.a} → ${d.b}`);
    svg.append("rect").attr("x", 0).attr("y", y0).attr("width", width).attr("height", rowH).attr("fill", "transparent")
      .on("pointerenter pointermove", (event) => tip.show(event, html)).on("pointerleave", (event) => tip.hide(event));
  });
  const wrap = document.createElement("div");
  wrap.append(legend([["Independent, gained", PURPLE], ["Independent, lost", GREY], ["Major-owned", TEAL]]), svg.node());
  return wrap;
}
```

<div class="card" data-chart="movers" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
moversChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Albums on each label on the 2001 to 2010 lists and on the 2016 to 2025 lists, for the eight labels that gained the most and the eight that lost the most.</p>

The biggest risers were ${risers.slice(0, 6).map((d) => `${short(d.label)} (${d.a} to ${d.b})`).join(", ")}. The biggest fallers were ${fallers.slice(0, 6).map((d) => `${short(d.label)} (${d.a} to ${d.b})`).join(", ")}. Self-released albums went from ${selfEarly} to ${selfLate} entries (${(100 * selfEarly / early.length).toFixed(1)}% to ${(100 * selfLate / late.length).toFixed(1)}%).

### Where the labels are based

This echoes the geography post. MusicBrainz records a country for most labels, about ${(100 * withCountry.length / nAll).toFixed(0)}% of entries once worldwide labels are set aside. Among those, ${pctOf(countryEarly, (d) => d.label_country === "US").toFixed(0)}% of albums were on a US-based label on the early lists and ${pctOf(countryLate, (d) => d.label_country === "US").toFixed(0)}% on the recent ones, while the UK's share went from ${pctOf(countryEarly, (d) => d.label_country === "GB").toFixed(0)}% to ${pctOf(countryLate, (d) => d.label_country === "GB").toFixed(0)}%.

```js
function whereChart() {
  const width = 880, h = 300, m = {l: 48, r: 16, t: 14, b: 34};
  const groups = [["US", "United States", PURPLE], ["GB", "United Kingdom", TEAL], ["other", "Elsewhere", GOLD]];
  const bands = [[2001, 2005], [2006, 2010], [2011, 2015], [2016, 2020], [2021, 2025]];
  const x = d3.scaleBand(bands.map((b) => b.join("–")), [m.l, width - m.r]).paddingInner(0.3).paddingOuter(0.15);
  const y = d3.scaleLinear([0, 100], [h - m.b, m.t]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, h]).attr("width", width).attr("height", h).attr("style", SVG_STYLE)
    .attr("role", "img").attr("aria-label", "Share of albums on labels based in the United States, the United Kingdom and elsewhere, by five-year group of lists");
  [0, 25, 50, 75, 100].forEach((v) => {
    svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", y(v)).attr("y2", y(v)).attr("stroke", v === 0 ? "#4a4a46" : GRID);
    svg.append("text").attr("x", m.l - 8).attr("y", y(v)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${v}%`);
  });
  bands.forEach(([lo, hi]) => {
    const r = withCountry.filter((d) => d.list_year >= lo && d.list_year <= hi), key = `${lo}–${hi}`;
    let acc = 0;
    groups.forEach(([code, name, color]) => {
      const n = r.filter((d) => code === "other" ? d.label_country !== "US" && d.label_country !== "GB" : d.label_country === code).length, share = 100 * n / r.length;
      svg.append("rect").attr("x", x(key)).attr("width", x.bandwidth()).attr("y", y(acc + share)).attr("height", Math.max(y(acc) - y(acc + share) - 1.5, 0.5)).attr("fill", color)
        .on("pointerenter pointermove", (event) => tip.show(event, `<b>${lo}–${hi} lists · ${name}</b><br>${share.toFixed(0)}% of ${r.length} albums with a label country`)).on("pointerleave", (event) => tip.hide(event));
      if (share >= 7) svg.append("text").attr("x", x(key) + x.bandwidth() / 2).attr("y", y(acc + share / 2)).attr("dominant-baseline", "middle").attr("text-anchor", "middle").attr("fill", color === PURPLE ? "#fff" : SURFACE).attr("font-size", 12).attr("font-weight", 500).attr("pointer-events", "none").text(`${share.toFixed(0)}%`);
      acc += share;
    });
    svg.append("text").attr("x", x(key) + x.bandwidth() / 2).attr("y", h - 10).attr("text-anchor", "middle").attr("fill", MUTED).attr("font-size", 12).text(`${lo}–${String(hi).slice(2)}`);
  });
  const wrap = document.createElement("div");
  wrap.append(legend(groups.map(([, name, color]) => [name, color])), svg.node());
  return wrap;
}
```

<div class="card" data-chart="where" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;position:relative;">

```js
whereChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">${withCountry.length.toLocaleString()} of ${nAll.toLocaleString()} albums have a country on file for the label (worldwide labels left out).</p>

```js
statTiles([
  {label: "US-based labels", value: `${pctOf(countryEarly, (d) => d.label_country === "US").toFixed(0)}% → ${pctOf(countryLate, (d) => d.label_country === "US").toFixed(0)}%`, caption: "Albums on a label based in the US, 2001–2010 lists compared with 2016–2025."},
  {label: "UK artists on US labels", value: `${(100 * ukOnUs.length / ukArtists.length).toFixed(0)}%`, caption: `${ukOnUs.length} of the ${ukArtists.length} albums by UK artists with a label country on file.`},
  {label: "Same country", value: `${pctOf(sameCountry, (d) => d.label_country === d.artist_country).toFixed(0)}%`, caption: "Albums on a label based in the artist's own country."}
])
```

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Here's what these charts can't tell us. A label is a legal and a marketing name, and the lines are blurry: some independents are distributed by majors, some labels run by artists sit inside majors, and ownership changes. Today's ownership is applied to every year. Label country is where MusicBrainz says the label is based, and it is missing for about three entries in ten. The classification is mine, and where I could not check a label individually it defaults to independent.</div>
</div>

```js
addExpandButtons((id) => id === "rank" ? bumpUI.top : heroUI.mode);
```
