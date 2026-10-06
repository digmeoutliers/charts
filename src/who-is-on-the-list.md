---
title: Who's on the list? (prototype)
toc: false
head: '<link rel="icon" href="favicon.png" type="image/png" sizes="32x32"><script src="https://cdn.jsdelivr.net/npm/iframe-resizer@5.5.9/js/iframeResizer.contentWindow.min.js"></script><script>if (window.self !== window.top) { document.documentElement.classList.add("embedded"); }</script><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"><style>.embedded { --serif: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; } .embedded body { font-size: 17px; line-height: 1.6; color: #15171a; } .embedded main { margin-top: 0 !important; } .embedded main > p { margin: 28px 0; } .embedded main > h2 { margin-top: 56px; } .embedded main > h3 { margin-top: 44px; } .embedded .standalone-only + p { margin-top: 0; } .embedded #observablehq-footer { display: none; } p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display { max-width: 920px; } .embedded #observablehq-center { margin: 0 !important; } .embedded main > h1, .embedded .standalone-only { display: none; } .dmo-tiles { display: grid; grid-template-columns: 1fr; gap: 1.25rem; } .dmo-tile { padding: 0 0.25rem; } .dmo-tile + .dmo-tile { border-top: 1px solid #33322f; padding-top: 1.25rem; } @media (min-width: 760px) { .dmo-tiles { grid-template-columns: repeat(3, 1fr); gap: 0; } .dmo-tile { padding: 0 1.5rem; } .dmo-tile + .dmo-tile { border-top: 0; padding-top: 0; border-left: 1px solid #33322f; } }</style>'
---

# Who's on the list? (prototype)

<p class="standalone-only"><strong>Prototype</strong> &mdash; unlisted draft charts for the next post. Not linked from anywhere.</p>

```js
const rows = FileAttachment("data/who_is_on_the_list_2001_2025.csv").csv({typed: true});
```

```js
// Colors come from the existing palette. Meaning here is by category, with its own legend on every chart
// (the album-count tiers in the wheel post use these same hues for a different purpose).
const catColor = {
  "Groups": "#2d6fbe",
  "Solo women": "#58cec8",
  "Solo men": "#d6b45b",
  "Other / not recorded": "#6b6a64"
};
const catOrder = ["Groups", "Solo women", "Solo men", "Other / not recorded"];
function category(d) {
  if (d.artist_type === "Group") return "Groups";
  if (d.artist_type === "Person") {
    if (d.artist_gender === "Female") return "Solo women";
    if (d.artist_gender === "Male") return "Solo men";
  }
  return "Other / not recorded";
}
const years = d3.sort(new Set(rows.map((d) => d.list_year)));
const periods = [[2001, 2005], [2006, 2010], [2011, 2015], [2016, 2020], [2021, 2025]];
```

```js
const viewMode = view(Inputs.radio(["Entries (albums on the lists)", "Distinct artists"], {value: "Entries (albums on the lists)"}));
```

```js
// counts per bucket, either by list entry or by distinct artist within the bucket
function bucketCounts(items, mode, filter) {
  const counts = {};
  const pool = filter ? items.filter(filter) : items;
  if (mode === "Distinct artists") {
    const seen = new Set();
    for (const d of pool) {
      if (seen.has(d.artist_id)) continue;
      seen.add(d.artist_id);
      const c = category(d);
      counts[c] = (counts[c] || 0) + 1;
    }
  } else {
    for (const d of pool) {
      const c = category(d);
      counts[c] = (counts[c] || 0) + 1;
    }
  }
  return counts;
}

function shareChart({buckets, cats, width = 880, height = 380, rotate = true}) {
  const marginL = 44, marginR = 12, marginT = 16, marginB = rotate ? 44 : 36;
  const plotW = width - marginL - marginR, plotH = height - marginT - marginB;
  const x = d3.scaleBand().domain(buckets.map((b) => b.label)).range([0, plotW]).padding(0.2);
  const y = d3.scaleLinear().domain([0, 100]).range([plotH, 0]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height)
    .attr("style", "background:#1a1a19;border-radius:12px;max-width:100%;height:auto;font-family:var(--sans-serif);");
  const g = svg.append("g").attr("transform", `translate(${marginL},${marginT})`);
  [0, 25, 50, 75, 100].forEach((t) => {
    g.append("line").attr("x1", 0).attr("x2", plotW).attr("y1", y(t)).attr("y2", y(t)).attr("stroke", "#33322f");
    g.append("text").attr("x", -8).attr("y", y(t)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 10).text(t + "%");
  });
  const tip = d3.select(document.createElement("div"))
    .attr("style", "position:fixed;pointer-events:none;background:#1a1a19;color:#f0efec;border:1px solid #383835;border-radius:8px;padding:8px 10px;font-size:12px;opacity:0;transition:opacity 0.1s;z-index:10;min-width:170px;");
  document.body.appendChild(tip.node());
  buckets.forEach((b) => {
    const total = d3.sum(cats, (c) => b.counts[c] || 0);
    let cum = 0;
    const bar = g.append("g").attr("transform", `translate(${x(b.label)},0)`);
    cats.forEach((c, i) => {
      const n = b.counts[c] || 0;
      if (!n) return;
      const pct = 100 * n / total, y0 = cum, y1 = cum + pct;
      cum = y1;
      const hgt = Math.max(0, y(y0) - y(y1) - (i < cats.length - 1 ? 1.5 : 0));
      bar.append("rect").attr("x", 0).attr("y", y(y1)).attr("width", x.bandwidth()).attr("height", hgt).attr("fill", catColor[c]).attr("rx", 1.5);
    });
    bar.append("rect").attr("x", 0).attr("y", 0).attr("width", x.bandwidth()).attr("height", plotH).attr("fill", "transparent")
      .on("pointerenter pointermove", (event) => {
        const lines = cats.map((c) => {
          const n = b.counts[c] || 0;
          return `<div style="display:flex;justify-content:space-between;gap:12px"><span><span style="display:inline-block;width:9px;height:9px;border-radius:2px;background:${catColor[c]};margin-right:6px"></span>${c}</span><b>${(100 * n / total).toFixed(0)}% <span style="font-weight:400;color:#898781">(${n})</span></b></div>`;
        });
        tip.style("opacity", 1).html(`<b>${b.label}</b> &middot; ${total}<br>${lines.join("")}`)
          .style("left", event.clientX + 14 + "px").style("top", event.clientY + 14 + "px");
      })
      .on("pointerleave", () => tip.style("opacity", 0));
    const cx = x(b.label) + x.bandwidth() / 2;
    const lab = g.append("text").attr("x", cx).attr("y", plotH + (rotate ? 10 : 20)).attr("fill", "#898781").attr("font-size", rotate ? 9 : 12)
      .attr("text-anchor", rotate ? "end" : "middle").text(b.label);
    if (rotate) lab.attr("transform", `rotate(-55,${cx},${plotH + 10})`);
  });
  return svg.node();
}

function legend(cats) {
  const d = document.createElement("div");
  d.style.cssText = "display:flex;gap:20px;flex-wrap:wrap;margin:0.75rem 0 0.25rem;justify-content:center;";
  d.innerHTML = cats.map((c) => `<span style="display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3"><span style="width:12px;height:12px;border-radius:3px;background:${catColor[c]};display:inline-block"></span>${c}</span>`).join("");
  return d;
}
```

## 1. Bands or solo artists?

```js
const yearBuckets = years.map((yr) => ({label: String(yr), counts: bucketCounts(rows, viewMode, (d) => d.list_year === yr)}));
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.5rem;max-width:900px;margin:0 auto;">

```js
shareChart({buckets: yearBuckets, cats: catOrder})
```

```js
legend(catOrder)
```

</div>

```js
// Headline numbers for the draft text (computed from the data, not typed in)
const grp = (lo, hi) => {
  const r = rows.filter((d) => d.list_year >= lo && d.list_year <= hi);
  return {n: r.filter((d) => d.artist_type === "Group").length, of: r.length};
};
const g0110 = grp(2001, 2010), g1625 = grp(2016, 2025);
```

```js
(() => {
  const p = document.createElement("p");
  p.innerHTML = `<em>Draft line:</em> groups were ${Math.round(100 * g0110.n / g0110.of)}% of list entries in 2001&ndash;2010 and ${Math.round(100 * g1625.n / g1625.of)}% in 2016&ndash;2025.`;
  return p;
})()
```

### The #1 albums

```js
function numberOneStrip() {
  const ones = rows.filter((d) => d.rank === 1);
  const width = 880, height = 230, marginL = 30, marginR = 20;
  const x = d3.scalePoint(ones.map((d) => d.list_year), [marginL, width - marginR]).padding(0.5);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height)
    .attr("style", "background:#1a1a19;border-radius:12px;max-width:100%;height:auto;font-family:var(--sans-serif);");
  const tip = d3.select(document.createElement("div"))
    .attr("style", "position:fixed;pointer-events:none;background:#1a1a19;color:#f0efec;border:1px solid #383835;border-radius:8px;padding:8px 10px;font-size:12px;opacity:0;transition:opacity 0.1s;z-index:10;");
  document.body.appendChild(tip.node());
  ones.forEach((d) => {
    const cx = x(d.list_year), c = category(d);
    svg.append("circle").attr("cx", cx).attr("cy", 40).attr("r", 9).attr("fill", catColor[c])
      .on("pointerenter pointermove", (event) => {
        tip.style("opacity", 1).html(`<b>${d.list_year}</b> &middot; ${d.artist_name}<br><i>${d.release_group_name}</i><br><span style="color:#898781">${c}</span>`)
          .style("left", event.clientX + 14 + "px").style("top", event.clientY + 14 + "px");
      })
      .on("pointerleave", () => tip.style("opacity", 0));
    svg.append("text").attr("x", cx).attr("y", 62).attr("fill", "#c9c8c3").attr("font-size", 10).attr("text-anchor", "end")
      .attr("transform", `rotate(-55,${cx},62)`).text(`${d.list_year}  ${d.artist_name}`);
  });
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.5rem;max-width:900px;margin:0 auto;">

```js
numberOneStrip()
```

```js
legend(catOrder.slice(0, 3))
```

</div>

## 2. Who are the solo artists?

```js
const soloRows = rows.filter((d) => d.artist_type === "Person" && (d.artist_gender === "Female" || d.artist_gender === "Male"));
const periodBuckets = periods.map(([lo, hi]) => ({
  label: `${lo}–${hi}`,
  counts: bucketCounts(soloRows, viewMode, (d) => d.list_year >= lo && d.list_year <= hi)
}));
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.5rem;max-width:900px;margin:0 auto;">

```js
shareChart({buckets: periodBuckets, cats: ["Solo women", "Solo men"], height: 340, rotate: false})
```

```js
legend(["Solo women", "Solo men"])
```

</div>

```js
(() => {
  const nb = rows.filter((d) => d.artist_gender === "Non-binary");
  const p = document.createElement("p");
  p.style.cssText = "font-size:13px;color:var(--theme-foreground-muted);";
  p.innerHTML = `Share of <em>solo artists with a recorded gender</em>. Hover a bar for the counts. ${new Set(nb.map((d) => d.artist_id)).size} non-binary solo artists (${nb.length} entries) are too few to chart as their own group and are left out of these percentages. Groups have no gender recorded.`;
  return p;
})()
```

## 3. Who comes back?

```js
// Artists first listed 2001-2015 (so everyone has had 10+ years to return), split by type/gender
const firstYear = d3.rollup(rows, (v) => d3.min(v, (d) => d.list_year), (d) => d.artist_id);
const yearsListed = d3.rollup(rows, (v) => new Set(v.map((d) => d.list_year)).size, (d) => d.artist_id);
const catOfArtist = new Map(rows.map((d) => [d.artist_id, category(d)]));
const cohort = [...firstYear].filter(([id, fy]) => fy <= 2015).map(([id]) => id);
const retention = ["Groups", "Solo women", "Solo men"].map((c) => {
  const ids = cohort.filter((id) => catOfArtist.get(id) === c);
  const back = ids.filter((id) => yearsListed.get(id) >= 2).length;
  return {c, n: ids.length, back, pct: ids.length ? 100 * back / ids.length : 0};
});

function retentionChart() {
  const width = 640, height = 190, labelW = 110, rowH = 56, padTop = 14;
  const plotW = width - labelW - 190;
  const x = d3.scaleLinear().domain([0, 100]).range([0, plotW]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height)
    .attr("style", "background:#1a1a19;border-radius:12px;max-width:100%;height:auto;font-family:var(--sans-serif);");
  const g = svg.append("g").attr("transform", `translate(${labelW},${padTop})`);
  retention.forEach((r, i) => {
    const yy = i * rowH;
    g.append("text").attr("x", -12).attr("y", yy + 15).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 13).text(r.c);
    g.append("rect").attr("x", 0).attr("y", yy).attr("width", plotW).attr("height", 30).attr("rx", 4).attr("fill", catColor[r.c]).attr("opacity", 0.28);
    g.append("rect").attr("x", 0).attr("y", yy).attr("width", x(r.pct)).attr("height", 30).attr("rx", 4).attr("fill", catColor[r.c]);
    g.append("text").attr("x", plotW + 12).attr("y", yy + 15).attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 13)
      .text(`${r.pct.toFixed(0)}% came back  (${r.back} of ${r.n})`);
  });
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem;max-width:820px;margin:0 auto;">

```js
retentionChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Artists first listed 2001&ndash;2015, so everyone has had at least ten years to return. Solid = appeared on more than one year's list; faded = one and done.</p>

## What this can't tell us (draft box)

- Gender is recorded for individual artists only. It covers solo artists, about a third of everyone on the lists.
- MusicBrainz classifies some solo-led projects as groups, and group lineups change over time, so groups get no gender here.
- Non-binary solo artists are too few to chart separately.
