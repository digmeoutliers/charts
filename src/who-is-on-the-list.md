---
title: Who's on the list? (draft)
toc: false
head: '<link rel="icon" href="favicon.png" type="image/png" sizes="32x32"><script src="https://cdn.jsdelivr.net/npm/iframe-resizer@5.5.9/js/iframeResizer.contentWindow.min.js"></script><script>if (window.self !== window.top) { document.documentElement.classList.add("embedded"); }</script><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"><style>.embedded { --serif: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; } .embedded body { font-size: 17px; line-height: 1.6; color: #15171a; } .embedded main { margin-top: 0 !important; } .embedded main > p { margin: 28px 0; } .embedded main > h2 { margin-top: 56px; } .embedded main > h3 { margin-top: 44px; } .embedded .standalone-only + p { margin-top: 0; } .embedded #observablehq-footer { display: none; } p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display { max-width: 920px; } .embedded #observablehq-center { margin: 0 !important; } .embedded main > h1, .embedded .standalone-only { display: none; } .dmo-tiles { display: grid; grid-template-columns: 1fr; gap: 1.25rem; } .dmo-tile { padding: 0 0.25rem; } .dmo-tile + .dmo-tile { border-top: 1px solid #33322f; padding-top: 1.25rem; } @media (min-width: 760px) { .dmo-tiles { grid-template-columns: repeat(3, 1fr); gap: 0; } .dmo-tile { padding: 0 1.5rem; } .dmo-tile + .dmo-tile { border-top: 0; padding-top: 0; border-left: 1px solid #33322f; } }</style>'
---

# Who's on the list?

<p class="standalone-only"><strong>Draft</strong> &mdash; unlisted page for the next post. Not linked from anywhere.</p>

```js
const rows = FileAttachment("data/who_is_on_the_list_2001_2025.csv").csv({typed: true});
```

```js
// ---- Palette: the same four brand hues as the wheel post, used by category here (each chart has its own key). ----
// To change a color or the stacking order, edit ONLY these two lines.
const catColor = {"Solo women": "#d6b45b", "Solo men": "#58cec8", "Groups": "#9c57f3", "Other / not recorded": "#6b6a64"};
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
const byYear = d3.group(rows, (d) => d.list_year);
const CARD = "background:#1a1a19;border-radius:12px;max-width:100%;height:auto;font-family:var(--sans-serif);";

// one shared tooltip
const tipEl = (() => {
  const t = document.createElement("div");
  t.style.cssText = "position:fixed;pointer-events:none;background:#1a1a19;color:#f0efec;border:1px solid #383835;border-radius:8px;padding:8px 10px;font-size:12px;font-family:var(--sans-serif);opacity:0;transition:opacity 0.1s;z-index:10;min-width:150px;max-width:260px;";
  document.body.appendChild(t);
  return t;
})();
function showTip(event, html) {
  tipEl.innerHTML = html;
  tipEl.style.opacity = 1;
  tipEl.style.left = Math.min(event.clientX + 14, window.innerWidth - 270) + "px";
  tipEl.style.top = event.clientY + 14 + "px";
}
function hideTip() { tipEl.style.opacity = 0; }
const swatch = (c) => `<span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:${catColor[c]};margin-right:6px"></span>`;

function legendEl(cats) {
  const d = document.createElement("div");
  d.style.cssText = "display:flex;gap:20px;flex-wrap:wrap;margin:0.75rem 0 0.25rem;justify-content:center;";
  d.innerHTML = cats.map((c) => `<span style="display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3"><span style="width:12px;height:12px;border-radius:3px;background:${catColor[c]};display:inline-block"></span>${c}</span>`).join("");
  return d;
}

// counts per bucket, either by list entry or by distinct artist within the bucket
function bucketCounts(items, mode, filter) {
  const counts = {};
  const pool = filter ? items.filter(filter) : items;
  const seen = new Set();
  for (const d of pool) {
    if (mode === "Distinct artists") {
      if (seen.has(d.artist_id)) continue;
      seen.add(d.artist_id);
    }
    const c = category(d);
    counts[c] = (counts[c] || 0) + 1;
  }
  return counts;
}

function statTiles(defs) {
  const wrap = document.createElement("div");
  wrap.className = "dmo-tiles";
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
  return wrap;
}
```

```js
// numbers used in the tiles and text, computed from the data
const pct = (n, d) => (100 * n / d);
const era = (lo, hi) => rows.filter((d) => d.list_year >= lo && d.list_year <= hi);
const e0110 = era(2001, 2010), e1625 = era(2016, 2025), e2125 = era(2021, 2025);
const share = (r, c) => pct(r.filter((d) => category(d) === c).length, r.length);
const perYear = (r, c, nYears) => r.filter((d) => category(d) === c).length / nYears;
const ones = rows.filter((d) => d.rank === 1);
const top10 = (r) => r.filter((d) => d.rank <= 10);
```

## Every album, by who made it

Each dot is one album on one year's list, in rank order: #1 is the top left, and the list reads across and down like a page. Gold is a solo woman, teal is a solo man, and purple is a band. Click a color in the key to light up one kind of artist, or hover a dot to see who it is.

```js
function waffleChart() {
  const cols = 10, pitch = 12, r = 4.6, perRow = 5, gapX = 34, gapY = 36, labelH = 16;
  const panelW = cols * pitch;
  const maxRows = Math.ceil(d3.max(years, (y) => byYear.get(y).length) / cols);
  const panelH = maxRows * pitch;
  const width = 880, height = 14 + 5 * (panelH + gapY + labelH);
  const x0 = (width - (perRow * panelW + (perRow - 1) * gapX)) / 2;

  const wrap = document.createElement("div");
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  let selected = null;

  years.forEach((yr, yi) => {
    const px = x0 + (yi % perRow) * (panelW + gapX), py = 14 + Math.floor(yi / perRow) * (panelH + gapY + labelH);
    svg.append("text").attr("x", px).attr("y", py + 6).attr("fill", "#c9c8c3").attr("font-size", 12).attr("font-weight", 600).text(yr);
    const list = byYear.get(yr).slice().sort((a, b) => a.rank - b.rank);
    list.forEach((d, i) => {
      const cx = px + (i % cols) * pitch + pitch / 2, cy = py + labelH + Math.floor(i / cols) * pitch + pitch / 2;
      const c = category(d);
      svg.append("circle").attr("cx", cx).attr("cy", cy).attr("r", r).attr("fill", catColor[c]).attr("data-cat", c)
        .style("transition", "opacity 0.15s")
        .on("pointerenter pointermove", (event) => showTip(event, `<b>${yr} &middot; #${d.rank}</b><br>${d.artist_name}<br><i>${d.release_group_name}</i><br><span style="color:#898781">${swatch(c)}${c}</span>`))
        .on("pointerleave", hideTip);
    });
  });

  const key = document.createElement("div");
  key.style.cssText = "display:flex;gap:10px;flex-wrap:wrap;margin:0.9rem 0 0.25rem;justify-content:center;";
  const buttons = new Map();
  function apply() {
    svg.selectAll("circle").style("opacity", function () { return !selected || this.getAttribute("data-cat") === selected ? 1 : 0.1; });
    buttons.forEach((b, c) => { b.style.outline = selected === c ? "2px solid #f0efec" : "none"; b.style.opacity = !selected || selected === c ? 1 : 0.55; });
  }
  catOrder.forEach((c) => {
    const n = rows.filter((d) => category(d) === c).length;
    const b = document.createElement("button");
    b.type = "button";
    b.style.cssText = "display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3;background:#232321;border:1px solid #383835;border-radius:999px;padding:5px 12px;cursor:pointer;font-family:var(--sans-serif);";
    b.innerHTML = `<span style="width:12px;height:12px;border-radius:3px;background:${catColor[c]};display:inline-block"></span>${c} <span style="color:#898781">${n.toLocaleString()}</span>`;
    b.onclick = () => { selected = selected === c ? null : c; apply(); };
    buttons.set(c, b);
    key.append(b);
  });
  wrap.append(svg.node(), key);
  return wrap;
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;">

```js
waffleChart()
```

</div>

```js
statTiles([
  {label: "#1 albums made by a band", value: `${ones.filter((d) => category(d) === "Groups").length} of ${ones.length}`,
   caption: `Only ${ones.filter((d) => d.artist_type === "Person").length} came from a solo artist, and ${ones.filter((d) => d.artist_type === "Person" && d.list_year > 2014).length} of those ${ones.filter((d) => d.artist_type === "Person").length} came after 2014.`},
  {label: "Share of list entries from bands", value: `${share(e0110, "Groups").toFixed(0)}% → ${share(e1625, "Groups").toFixed(0)}%`,
   caption: "2001–2010 compared with 2016–2025."},
  {label: "Share from solo women", value: `${share(e0110, "Solo women").toFixed(0)}% → ${share(e1625, "Solo women").toFixed(0)}%`,
   caption: `Same two periods. Solo men went from ${share(e0110, "Solo men").toFixed(0)}% to ${share(e1625, "Solo men").toFixed(0)}%.`}
])
```

The first thing you notice is the purple. The second is the gold: a few scattered dots in the early years, then whole rows of it by the 2020s.

## The share, year by year

Counting every album gives one picture, and counting each artist once per year gives a slightly different one. Switch between them.

```js
const viewMode = view(Inputs.radio(["Entries (albums on the lists)", "Distinct artists"], {value: "Entries (albums on the lists)"}));
```

```js
function shareArea(mode) {
  const width = 880, height = 400, m = {l: 44, r: 16, t: 16, b: 32};
  const pw = width - m.l - m.r, ph = height - m.t - m.b;
  const raw = years.map((yr) => bucketCounts(rows, mode, (d) => d.list_year === yr));
  const tot = raw.map((c) => d3.sum(catOrder, (k) => c[k] || 0));
  const shares = raw.map((c, i) => Object.fromEntries(catOrder.map((k) => [k, (c[k] || 0) / tot[i]])));
  // 3-year centered average to smooth the curves (the tooltip shows the actual year)
  const sm = shares.map((_, i) => {
    const sl = shares.slice(Math.max(0, i - 1), Math.min(shares.length, i + 2));
    const o = Object.fromEntries(catOrder.map((k) => [k, d3.mean(sl, (s) => s[k])]));
    const s = d3.sum(Object.values(o));
    return Object.fromEntries(Object.entries(o).map(([k, v]) => [k, v / s]));
  });
  const x = d3.scaleLinear().domain([years[0], years[years.length - 1]]).range([0, pw]);
  const y = d3.scaleLinear().domain([0, 1]).range([ph, 0]);
  const series = d3.stack().keys(catOrder)(sm);
  const area = d3.area().x((d, i) => x(years[i])).y0((d) => y(d[0])).y1((d) => y(d[1])).curve(d3.curveMonotoneX);

  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const g = svg.append("g").attr("transform", `translate(${m.l},${m.t})`);
  [0, 0.25, 0.5, 0.75, 1].forEach((t) => {
    g.append("line").attr("x1", 0).attr("x2", pw).attr("y1", y(t)).attr("y2", y(t)).attr("stroke", "#33322f");
    g.append("text").attr("x", -8).attr("y", y(t)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 10).text(Math.round(t * 100) + "%");
  });
  series.forEach((s) => g.append("path").attr("d", area(s)).attr("fill", catColor[s.key]).attr("opacity", 0.92));
  years.filter((yr) => (yr - 2001) % 4 === 0).forEach((yr) => g.append("text").attr("x", x(yr)).attr("y", ph + 20).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr));

  const cursor = g.append("line").attr("y1", 0).attr("y2", ph).attr("stroke", "#f0efec").attr("stroke-width", 1).attr("opacity", 0);
  g.append("rect").attr("width", pw).attr("height", ph).attr("fill", "transparent")
    .on("pointermove pointerenter", (event) => {
      const [mx] = d3.pointer(event);
      const i = Math.max(0, Math.min(years.length - 1, Math.round(((mx / pw) * (years[years.length - 1] - years[0])))));
      cursor.attr("x1", x(years[i])).attr("x2", x(years[i])).attr("opacity", 0.8);
      const lines = [...catOrder].reverse().map((k) => `<div style="display:flex;justify-content:space-between;gap:12px"><span>${swatch(k)}${k}</span><b>${(100 * (shares[i][k])).toFixed(0)}% <span style="font-weight:400;color:#898781">(${raw[i][k] || 0})</span></b></div>`);
      showTip(event, `<b>${years[i]}</b> &middot; ${tot[i]}<br>${lines.join("")}`);
    })
    .on("pointerleave", () => { cursor.attr("opacity", 0); hideTip(); });
  const wrap = document.createElement("div");
  wrap.append(svg.node(), legendEl([...catOrder].reverse()));
  return wrap;
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.75rem;max-width:900px;margin:0 auto;">

```js
shareArea(viewMode)
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">The curves use a three-year average to smooth the bumps. Hover to see the actual numbers for any single year.</p>

Bands start near three-quarters of every list and settle at roughly three in five. The teal barely moves. Nearly all of the change is gold.

## Who gets to #1?

The top spot tells the same story, only more starkly.

```js
function numberOneLanes() {
  const lanes = ["Groups", "Solo women", "Solo men"];
  const width = 880, height = 270, m = {l: 96, r: 24, t: 20, b: 30};
  const x = d3.scalePoint(years, [m.l, width - m.r]).padding(0.5);
  const laneY = Object.fromEntries(lanes.map((l, i) => [l, m.t + 28 + i * 66]));
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  lanes.forEach((l) => {
    svg.append("line").attr("x1", m.l).attr("x2", width - m.r).attr("y1", laneY[l]).attr("y2", laneY[l]).attr("stroke", "#33322f").attr("stroke-dasharray", "2 4");
    svg.append("text").attr("x", m.l - 14).attr("y", laneY[l]).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", catColor[l]).attr("font-size", 12).attr("font-weight", 600).text(l);
  });
  years.forEach((yr, i) => { if (i % 2 === 0) svg.append("text").attr("x", x(yr)).attr("y", height - 10).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(yr); });
  ones.forEach((d) => {
    const c = category(d), cx = x(d.list_year), cy = laneY[c];
    svg.append("circle").attr("cx", cx).attr("cy", cy).attr("r", 10).attr("fill", catColor[c])
      .on("pointerenter pointermove", (event) => showTip(event, `<b>${d.list_year}</b> &middot; ${d.artist_name}<br><i>${d.release_group_name}</i>`))
      .on("pointerleave", hideTip);
    if (c !== "Groups") svg.append("text").attr("x", cx).attr("y", cy + 24).attr("text-anchor", "middle").attr("fill", "#c9c8c3").attr("font-size", 10).text(d.artist_name);
  });
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;">

```js
numberOneLanes()
```

</div>

Bands took the top spot every year from 2001 to 2004. Sufjan Stevens broke the run in 2005, and then bands won it nine years straight. Since 2015, solo artists have hit #1 four times: Courtney Barnett twice, David Bowie, and Lizzo.

## Solo artists: counts, not just shares

A rising share can mean one group is growing or another is shrinking, so here are the actual numbers: how many albums by solo women and by solo men made each year's list.

```js
function soloCounts(mode) {
  const width = 880, height = 380, m = {l: 44, r: 120, t: 16, b: 32};
  const pw = width - m.l - m.r, ph = height - m.t - m.b;
  const cats = ["Solo women", "Solo men"];
  const data = years.map((yr) => ({yr, c: bucketCounts(rows, mode, (d) => d.list_year === yr)}));
  const ymax = d3.max(data, (d) => d3.max(cats, (k) => d.c[k] || 0));
  const x = d3.scaleLinear().domain([years[0], years[years.length - 1]]).range([0, pw]);
  const y = d3.scaleLinear().domain([0, Math.ceil((ymax + 2) / 5) * 5]).range([ph, 0]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const g = svg.append("g").attr("transform", `translate(${m.l},${m.t})`);
  y.ticks(5).forEach((t) => {
    g.append("line").attr("x1", 0).attr("x2", pw).attr("y1", y(t)).attr("y2", y(t)).attr("stroke", "#33322f");
    g.append("text").attr("x", -8).attr("y", y(t)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 10).text(t);
  });
  years.filter((yr) => (yr - 2001) % 4 === 0).forEach((yr) => g.append("text").attr("x", x(yr)).attr("y", ph + 20).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr));
  // era averages (dashed)
  const avg = (k, lo, hi) => d3.mean(data.filter((d) => d.yr >= lo && d.yr <= hi), (d) => d.c[k] || 0);
  cats.forEach((k) => {
    [[2001, 2010], [2021, 2025]].forEach(([lo, hi]) => {
      const a = avg(k, lo, hi);
      g.append("line").attr("x1", x(lo)).attr("x2", x(hi)).attr("y1", y(a)).attr("y2", y(a)).attr("stroke", catColor[k]).attr("stroke-width", 1.5).attr("stroke-dasharray", "5 4").attr("opacity", 0.9);
    });
    g.append("path").attr("d", d3.line().x((d) => x(d.yr)).y((d) => y(d.c[k] || 0)).curve(d3.curveMonotoneX)(data)).attr("fill", "none").attr("stroke", catColor[k]).attr("stroke-width", 2.5);
    data.forEach((d) => g.append("circle").attr("cx", x(d.yr)).attr("cy", y(d.c[k] || 0)).attr("r", 3.4).attr("fill", catColor[k]));
    const endY = y(data[data.length - 1].c[k] || 0);
    g.append("text").attr("x", pw + 10).attr("y", endY).attr("dominant-baseline", "middle").attr("fill", catColor[k]).attr("font-size", 12).attr("font-weight", 600).text(k);
    g.append("text").attr("x", pw + 10).attr("y", endY + 14).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 10)
      .text(`${avg(k, 2001, 2010).toFixed(1)} → ${avg(k, 2021, 2025).toFixed(1)} a year`);
  });
  const cursor = g.append("line").attr("y1", 0).attr("y2", ph).attr("stroke", "#f0efec").attr("opacity", 0);
  g.append("rect").attr("width", pw).attr("height", ph).attr("fill", "transparent")
    .on("pointermove pointerenter", (event) => {
      const [mx] = d3.pointer(event);
      const i = Math.max(0, Math.min(years.length - 1, Math.round((mx / pw) * (years[years.length - 1] - years[0]))));
      cursor.attr("x1", x(years[i])).attr("x2", x(years[i])).attr("opacity", 0.7);
      showTip(event, `<b>${years[i]}</b><br>${cats.map((k) => `<div style="display:flex;justify-content:space-between;gap:12px"><span>${swatch(k)}${k}</span><b>${data[i].c[k] || 0}</b></div>`).join("")}`);
    })
    .on("pointerleave", () => { cursor.attr("opacity", 0); hideTip(); });
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.75rem;max-width:900px;margin:0 auto;">

```js
soloCounts(viewMode)
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Dashed lines are the average for 2001&ndash;2010 and for 2021&ndash;2025. Only artists with a recorded gender are counted.</p>

```js
statTiles([
  {label: "Solo women on each year's list", value: `${perYear(e0110, "Solo women", 10).toFixed(1)} → ${perYear(e2125, "Solo women", 5).toFixed(1)}`,
   caption: "Average albums per year, 2001–2010 compared with 2021–2025."},
  {label: "Solo men on each year's list", value: `${perYear(e0110, "Solo men", 10).toFixed(1)} → ${perYear(e2125, "Solo men", 5).toFixed(1)}`,
   caption: "Essentially unchanged. The rise is all on one side."},
  {label: "Top-10 spots held by solo women", value: `${share(top10(e0110), "Solo women").toFixed(0)}% → ${share(top10(e1625), "Solo women").toFixed(0)}%`,
   caption: "2001–2010 compared with 2016–2025."}
])
```

Solo women went from five or six albums a year to more than twenty. Solo men didn't change. The lists didn't get any bigger, so the new room came from bands, not from solo men.

## Do they come back?

Back to the question from the first post: who sticks around? To keep the comparison fair, this looks only at artists first listed by 2015, so everyone has had at least ten years to return.

```js
function wilson(k, n, z = 1.96) {
  const p = k / n, d = 1 + z * z / n, c = p + z * z / (2 * n), a = z * Math.sqrt(p * (1 - p) / n + z * z / (4 * n * n));
  return [100 * (c - a) / d, 100 * (c + a) / d];
}
const firstYear = d3.rollup(rows, (v) => d3.min(v, (d) => d.list_year), (d) => d.artist_id);
const yearsListed = d3.rollup(rows, (v) => new Set(v.map((d) => d.list_year)).size, (d) => d.artist_id);
const catOfArtist = new Map(rows.map((d) => [d.artist_id, category(d)]));
const cohort = [...firstYear].filter(([id, fy]) => fy <= 2015).map(([id]) => id);
const retention = ["Groups", "Solo women", "Solo men"].map((c) => {
  const ids = cohort.filter((id) => catOfArtist.get(id) === c);
  const back = ids.filter((id) => yearsListed.get(id) >= 2).length;
  const [lo, hi] = wilson(back, ids.length);
  return {c, n: ids.length, back, p: 100 * back / ids.length, lo, hi};
});

function retentionChart() {
  const width = 880, height = 250, m = {l: 120, r: 190, t: 20, b: 40};
  const pw = width - m.l - m.r;
  const x = d3.scaleLinear().domain([30, 80]).range([0, pw]);
  const rowH = 58;
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const g = svg.append("g").attr("transform", `translate(${m.l},${m.t})`);
  [30, 40, 50, 60, 70, 80].forEach((t) => {
    g.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", 0).attr("y2", retention.length * rowH - 10).attr("stroke", "#33322f");
    g.append("text").attr("x", x(t)).attr("y", retention.length * rowH + 6).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(t + "%");
  });
  retention.forEach((r, i) => {
    const cy = i * rowH + 20;
    g.append("text").attr("x", -14).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 13).text(r.c);
    g.append("line").attr("x1", x(r.lo)).attr("x2", x(r.hi)).attr("y1", cy).attr("y2", cy).attr("stroke", catColor[r.c]).attr("stroke-width", 6).attr("stroke-linecap", "round").attr("opacity", 0.45);
    g.append("circle").attr("cx", x(r.p)).attr("cy", cy).attr("r", 9).attr("fill", catColor[r.c])
      .on("pointerenter pointermove", (event) => showTip(event, `<b>${r.c}</b><br>${r.back} of ${r.n} came back<br><span style="color:#898781">plausible range ${r.lo.toFixed(0)}–${r.hi.toFixed(0)}%</span>`))
      .on("pointerleave", hideTip);
    g.append("text").attr("x", pw + 16).attr("y", cy - 7).attr("dominant-baseline", "middle").attr("fill", "#f0efec").attr("font-size", 14).attr("font-weight", 600).text(`${r.p.toFixed(0)}% came back`);
    g.append("text").attr("x", pw + 16).attr("y", cy + 10).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(`range ${r.lo.toFixed(0)}–${r.hi.toFixed(0)}% · ${r.n} artists`);
  });
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.75rem;max-width:900px;margin:0 auto;">

```js
retentionChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Dots are the share who appeared on more than one year's list. The line is the range the true figure could plausibly fall in, given how many artists there are. Where the lines overlap, the data can't tell the groups apart.</p>

About half of every kind of artist came back. The solo women look a little higher, but with only 57 of them in this group, their range overlaps with everyone else's. I'd call it a tie.

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">What this can't tell us</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Gender is only recorded for individual artists, so every gender figure here covers solo artists, about a third of everyone on the lists. I don't assign one to bands: lineups change from album to album, and MusicBrainz counts some solo-led projects as bands. Five non-binary solo artists are too few to chart on their own, so they're left out of the gender percentages.</div>
</div>
