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

Each dot is one album on one year's list, in rank order: #1 is the top left, and the list reads across and down like a page. Gold is a solo woman, teal is a solo man, and purple is a band. Click a color in the key to light up one kind of artist, pick years from the box, or search for an artist to see where all of their albums sit. Hover any dot to see who it is.

```js
function yearMultiSelect(allYears) {
  const container = document.createElement("div");
  container.style.cssText = "position:relative;max-width:320px;margin:0 0 0.75rem;";
  const toggle = document.createElement("button");
  toggle.type = "button";
  toggle.style.cssText = "width:100%;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:8px;font-size:14px;padding:8px 10px;border-radius:6px;border:1px solid var(--theme-foreground-faint);background:var(--theme-background);color:var(--theme-foreground);cursor:pointer;";
  const toggleLabel = document.createElement("span");
  const caret = document.createElement("span");
  caret.textContent = "▾";
  caret.style.cssText = "color:var(--theme-foreground-faint);";
  toggle.append(toggleLabel, caret);
  const panel = document.createElement("div");
  panel.style.cssText = "position:absolute;top:100%;left:0;right:0;background:var(--theme-background);border:1px solid var(--theme-foreground-faint);border-radius:8px;margin-top:4px;padding:10px;max-height:280px;overflow-y:auto;z-index:20;display:none;box-shadow:0 4px 16px rgba(0,0,0,0.15);";
  const controls = document.createElement("div");
  controls.style.cssText = "display:flex;gap:8px;margin-bottom:0.5rem;";
  const selectAllBtn = document.createElement("button");
  selectAllBtn.type = "button";
  selectAllBtn.textContent = "Select all";
  selectAllBtn.style.cssText = "font-size:12px;padding:4px 10px;border-radius:6px;border:1px solid var(--theme-foreground-faint);background:transparent;color:var(--theme-foreground);cursor:pointer;";
  const clearAllBtn = document.createElement("button");
  clearAllBtn.type = "button";
  clearAllBtn.textContent = "Clear all";
  clearAllBtn.style.cssText = selectAllBtn.style.cssText;
  controls.append(selectAllBtn, clearAllBtn);
  const grid = document.createElement("div");
  grid.style.cssText = "display:flex;flex-wrap:wrap;gap:6px 16px;font-size:13px;";
  const boxes = allYears.map((yr) => {
    const label = document.createElement("label");
    label.style.cssText = "display:flex;align-items:center;gap:4px;cursor:pointer;";
    const input = document.createElement("input");
    input.type = "checkbox";
    input.checked = true;
    input.value = yr;
    label.append(input, document.createTextNode(String(yr)));
    grid.append(label);
    return input;
  });
  panel.append(controls, grid);
  container.append(toggle, panel);
  Object.defineProperty(container, "value", { get() { return boxes.filter((b) => b.checked).map((b) => +b.value); } });
  function updateLabel() {
    const n = boxes.filter((b) => b.checked).length;
    toggleLabel.textContent = n === allYears.length ? `All ${n} years` : n === 0 ? "No years selected" : `${n} of ${allYears.length} years`;
  }
  function notify() { updateLabel(); container.dispatchEvent(new Event("input")); }
  function setAll(checked) { for (const b of boxes) b.checked = checked; notify(); }
  selectAllBtn.addEventListener("click", setAll.bind(null, true));
  clearAllBtn.addEventListener("click", setAll.bind(null, false));
  for (const b of boxes) b.addEventListener("change", notify);
  function open() { panel.style.display = "block"; caret.textContent = "▴"; }
  function close() { panel.style.display = "none"; caret.textContent = "▾"; }
  toggle.addEventListener("click", () => (panel.style.display === "block" ? close() : open()));
  document.addEventListener("pointerdown", (event) => { if (!container.contains(event.target)) close(); });
  document.addEventListener("keydown", (event) => { if (event.key === "Escape") close(); });
  updateLabel();
  return container;
}

const selectedYears = view(yearMultiSelect(years));
```

```js
const artistList = (() => {
  const seen = new Map();
  for (const d of rows) if (!seen.has(d.artist_id)) seen.set(d.artist_id, d.artist_name);
  return Array.from(seen, ([id, name]) => ({id, name})).sort((a, b) => a.name.localeCompare(b.name));
})();

function artistSearch(list) {
  const container = document.createElement("div");
  container.style.cssText = "position:relative;max-width:320px;margin:0.25rem 0 0.75rem;";
  const row = document.createElement("div");
  row.style.cssText = "display:flex;align-items:center;gap:8px;";
  const input = document.createElement("input");
  input.type = "text";
  input.placeholder = "Search for an artist…";
  input.autocomplete = "off";
  input.style.cssText = "flex:1;box-sizing:border-box;padding:8px 10px;font-size:14px;border:1px solid var(--theme-foreground-faint);border-radius:6px;background:var(--theme-background);color:var(--theme-foreground);";
  const clearBtn = document.createElement("button");
  clearBtn.type = "button";
  clearBtn.textContent = "Clear";
  clearBtn.style.cssText = "font-size:13px;padding:7px 10px;border-radius:6px;border:1px solid var(--theme-foreground-faint);background:transparent;color:var(--theme-foreground);cursor:pointer;display:none;";
  row.append(input, clearBtn);
  const suggestions = document.createElement("div");
  suggestions.style.cssText = "position:absolute;top:100%;left:0;right:0;background:#1a1a19;border:1px solid #383835;border-radius:8px;margin-top:4px;max-height:240px;overflow-y:auto;z-index:20;display:none;";
  container.append(row, suggestions);
  Object.defineProperty(container, "value", { get() { return container._selectedId ?? null; } });
  function renderSuggestions(query) {
    suggestions.innerHTML = "";
    const q = query.trim().toLowerCase();
    if (!q) { suggestions.style.display = "none"; return; }
    const matches = list.filter((a) => a.name.toLowerCase().includes(q)).slice(0, 8);
    if (!matches.length) { suggestions.style.display = "none"; return; }
    for (const a of matches) {
      const item = document.createElement("div");
      item.textContent = a.name;
      item.style.cssText = "padding:8px 10px;cursor:pointer;color:#f0efec;font-size:14px;";
      item.addEventListener("pointerenter", () => (item.style.background = "#2a2a27"));
      item.addEventListener("pointerleave", () => (item.style.background = "transparent"));
      item.addEventListener("mousedown", (event) => { event.preventDefault(); select(a); });
      suggestions.append(item);
    }
    suggestions.style.display = "block";
  }
  function select(a) {
    container._selectedId = a.id;
    input.value = a.name;
    suggestions.style.display = "none";
    clearBtn.style.display = "inline-block";
    container.dispatchEvent(new Event("input"));
  }
  function clear() {
    container._selectedId = null;
    input.value = "";
    suggestions.style.display = "none";
    clearBtn.style.display = "none";
    input.focus();
    container.dispatchEvent(new Event("input"));
  }
  input.addEventListener("input", () => { container._selectedId = null; clearBtn.style.display = "none"; renderSuggestions(input.value); });
  clearBtn.addEventListener("click", clear);
  return container;
}

const selectedArtist = view(artistSearch(artistList));
const gridState = {cat: null};   // the color-key filter survives redraws when the boxes above change
```

```js
function waffleChart(yearsSel, artistSel) {
  const cols = 10, pitch = 12, r = 4.6, perRow = 5, gapX = 34, gapY = 36, labelH = 16;
  const panelW = cols * pitch;
  const maxRows = Math.ceil(d3.max(years, (y) => byYear.get(y).length) / cols);
  const panelH = maxRows * pitch;
  const width = 880, height = 14 + 5 * (panelH + gapY + labelH);
  const x0 = (width - (perRow * panelW + (perRow - 1) * gapX)) / 2;

  const wrap = document.createElement("div");
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const yearOn = new Set(yearsSel);

  years.forEach((yr, yi) => {
    const px = x0 + (yi % perRow) * (panelW + gapX), py = 14 + Math.floor(yi / perRow) * (panelH + gapY + labelH);
    svg.append("text").attr("x", px).attr("y", py + 6).attr("fill", "#c9c8c3").attr("font-size", 12).attr("font-weight", 600).attr("opacity", yearOn.has(yr) ? 1 : 0.35).text(yr);
    const list = byYear.get(yr).slice().sort((a, b) => a.rank - b.rank);
    list.forEach((d, i) => {
      const cx = px + (i % cols) * pitch + pitch / 2, cy = py + labelH + Math.floor(i / cols) * pitch + pitch / 2;
      const c = category(d);
      svg.append("circle").attr("cx", cx).attr("cy", cy).attr("r", r).attr("fill", catColor[c]).attr("data-cat", c).attr("data-year", yr).attr("data-artist", d.artist_id)
        .style("transition", "opacity 0.15s")
        .on("pointerenter pointermove", (event) => showTip(event, `<b>${yr} &middot; #${d.rank}</b><br>${d.artist_name}<br><i>${d.release_group_name}</i><br><span style="color:#898781">${swatch(c)}${c}</span>`))
        .on("pointerleave", hideTip);
    });
  });

  const key = document.createElement("div");
  key.style.cssText = "display:flex;gap:10px;flex-wrap:wrap;margin:0.9rem 0 0.25rem;justify-content:center;";
  const buttons = new Map();
  function apply() {
    const sel = gridState.cat;
    svg.selectAll("circle")
      .style("opacity", function () {
        const okCat = !sel || this.getAttribute("data-cat") === sel;
        const okYear = yearOn.has(+this.getAttribute("data-year"));
        const okArtist = !artistSel || this.getAttribute("data-artist") === artistSel;
        return okCat && okYear && okArtist ? 1 : 0.1;
      })
      .attr("stroke", function () { return artistSel && this.getAttribute("data-artist") === artistSel ? "#f0efec" : "none"; })
      .attr("stroke-width", 1.6);
    buttons.forEach((b, c) => { b.style.outline = sel === c ? "2px solid #f0efec" : "none"; b.style.opacity = !sel || sel === c ? 1 : 0.55; });
  }
  catOrder.forEach((c) => {
    const n = rows.filter((d) => category(d) === c).length;
    const b = document.createElement("button");
    b.type = "button";
    b.style.cssText = "display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3;background:#232321;border:1px solid #383835;border-radius:999px;padding:5px 12px;cursor:pointer;font-family:var(--sans-serif);";
    b.innerHTML = `<span style="width:12px;height:12px;border-radius:3px;background:${catColor[c]};display:inline-block"></span>${c} <span style="color:#898781">${n.toLocaleString()}</span>`;
    b.onclick = () => { gridState.cat = gridState.cat === c ? null : c; apply(); };
    buttons.set(c, b);
    key.append(b);
  });
  apply();
  wrap.append(svg.node(), key);
  if (artistSel) {
    const mine = rows.filter((d) => d.artist_id === artistSel).sort((a, b) => a.list_year - b.list_year);
    const t = document.createElement("div");
    t.style.cssText = "margin:0.9rem 0 0.25rem;font-size:13px;color:#c9c8c3;line-height:1.7;";
    t.innerHTML = `<b style="color:#f0efec">${mine[0].artist_name}</b> &middot; ${category(mine[0])} &middot; ${mine.length} album${mine.length === 1 ? "" : "s"} on the lists<br>` +
      mine.map((d) => `${d.list_year} &middot; #${d.rank} &middot; <i>${d.release_group_name}</i>`).join("<br>");
    wrap.append(t);
  }
  return wrap;
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;">

```js
waffleChart(selectedYears, selectedArtist)
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

The same story, as a share of each year's list. Every album counts once.

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
shareArea("Entries")
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
soloCounts("Entries")
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

## Counting albums or counting artists?

So far every chart has counted albums, so an artist with three albums on the lists counts three times. Counting each artist once instead barely changes the picture:

```js
function albumsVsArtists() {
  const cats = ["Groups", "Solo men", "Solo women", "Other / not recorded"];
  const albumCounts = bucketCounts(rows, "Entries");
  const artistCounts = bucketCounts(rows, "Distinct artists");
  const nAlbums = d3.sum(cats, (c) => albumCounts[c] || 0), nArtists = d3.sum(cats, (c) => artistCounts[c] || 0);
  const width = 880, m = {l: 150, r: 200, t: 18, b: 12}, rowH = 66, height = m.t + cats.length * rowH + m.b;
  const pw = width - m.l - m.r;
  const x = d3.scaleLinear().domain([0, 70]).range([0, pw]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const g = svg.append("g").attr("transform", `translate(${m.l},${m.t})`);
  cats.forEach((c, i) => {
    const y0 = i * rowH;
    const a = 100 * (albumCounts[c] || 0) / nAlbums, b = 100 * (artistCounts[c] || 0) / nArtists;
    g.append("text").attr("x", -14).attr("y", y0 + 24).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 13).text(c);
    [[a, albumCounts[c] || 0, "of albums", 1, 0], [b, artistCounts[c] || 0, "of artists", 0.45, 24]].forEach(([v, n, lab, op, dy]) => {
      g.append("rect").attr("x", 0).attr("y", y0 + 6 + dy).attr("width", Math.max(2, x(v))).attr("height", 18).attr("rx", 3).attr("fill", catColor[c]).attr("opacity", op)
        .on("pointerenter pointermove", (event) => showTip(event, `<b>${c}</b><br>${v.toFixed(0)}% ${lab} (${n.toLocaleString()})`))
        .on("pointerleave", hideTip);
      g.append("text").attr("x", x(v) + 10).attr("y", y0 + 15 + dy).attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 12).text(`${v.toFixed(0)}% ${lab}  (${n.toLocaleString()})`);
    });
  });
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.75rem;max-width:900px;margin:0 auto;">

```js
albumsVsArtists()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Solid bars count albums on the lists. Faded bars count each artist once.</p>

## Do they come back?

Back to the question from the first post: who sticks around? Counting artists here makes sense, because the question is about people, not albums.

```js
// how long it takes returning artists to come back (artists first listed by 2015, so 10+ years are observable)
const _first = d3.rollup(rows, (v) => d3.min(v, (d) => d.list_year), (d) => d.artist_id);
const _all = d3.rollup(rows, (v) => d3.sort(new Set(v.map((d) => d.list_year))), (d) => d.artist_id);
const _gaps = [..._first].filter(([id, fy]) => fy <= 2015).map(([id]) => _all.get(id)).filter((ys) => ys.length >= 2).map((ys) => ys[1] - ys[0]);
const within = (k) => Math.round(100 * _gaps.filter((g) => g <= k).length / _gaps.length);
```

```js
(() => {
  const p = document.createElement("p");
  p.innerHTML = `Why only artists first listed by 2015? An artist who debuts on a list in 2024 hasn't had time to come back, so for them "one and done" mostly means "not yet." And when artists do come back, they do it quickly: of those who returned, ${within(3)}% were back within three years and ${within(10)}% within ten. Giving every artist at least ten years to return catches nearly all of the comebacks, and keeps the comparison fair between artists who debuted in 2003 and ones who debuted in 2013.`;
  return p;
})()
```

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

About half of every kind of artist came back. The solo women look a little higher, and they stay a bit higher when I move the cutoff earlier or later, but with only 57 of them in this group, their range overlaps with everyone else's. I'd call it a tie, and a good one to revisit as more years come in.

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Whether an artist counts as a band or a solo act, and the gender recorded for solo artists, comes from <a href="https://musicbrainz.org/" target="_top" style="color:inherit; text-decoration:underline;">MusicBrainz</a>, a free music database that volunteers around the world add to and correct. That crowd-sourcing is why it's so thorough, and also why it's occasionally wrong. In my own saved copy I found a year typo on one album that MusicBrainz's editors had already fixed by the time I looked, and another date that I had to correct myself. When I catch an error that matters, I note it on the <a href="https://digmeoutliers.com/data-notes/" target="_top" style="color:inherit; text-decoration:underline;">Data Notes</a> page.</div>
</div>

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">What this can't tell us</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Gender is only recorded for individual artists, so every gender figure here covers solo artists, about a third of everyone on the lists. I don't assign one to bands: lineups change from album to album, and MusicBrainz counts some solo-led projects as bands. Five non-binary solo artists are too few to chart on their own, so they're left out of the gender percentages.</div>
</div>
