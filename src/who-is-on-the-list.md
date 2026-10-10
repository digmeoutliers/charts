---
title: Who's on the list? (draft)
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
---

# Who's on the list?

<p class="standalone-only"><strong>Draft</strong> &mdash; unlisted page for the next post. Not linked from anywhere.</p>

```js
import {makeTooltip, enableTap} from "./components/tooltip.js";
import {addLens} from "./components/lens.js";
```

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

// one shared tooltip (stays on screen near the edges, works with taps)
const tip = makeTooltip({minWidth: 150, maxWidth: 260});
const showTip = (event, html) => tip.show(event, html);
const hideTip = (event) => tip.hide(event);
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
// numbers used in the tiles and text, computed from the data
const pct = (n, d) => (100 * n / d);
const era = (lo, hi) => rows.filter((d) => d.list_year >= lo && d.list_year <= hi);
const e0110 = era(2001, 2010), e1625 = era(2016, 2025), e2125 = era(2021, 2025);
const share = (r, c) => pct(r.filter((d) => category(d) === c).length, r.length);
const perYear = (r, c, nYears) => r.filter((d) => category(d) === c).length / nYears;
const ones = rows.filter((d) => d.rank === 1);
const top10 = (r) => r.filter((d) => d.rank <= 10);
```

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">Note from John</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Whether an artist counts as a band or a solo act, and the gender recorded for solo artists, comes straight from <a href="https://musicbrainz.org/" target="_top" style="color:inherit; text-decoration:underline;">MusicBrainz</a>, a free music database that volunteers around the world add to and correct. That crowd-sourcing is why it's so thorough, and also why it's never complete or perfectly accurate. In my own saved copy I found a year typo that MusicBrainz's editors had already fixed by the time I looked, and another date that I had to correct myself. If an artist is misgendered or mislabeled here, that comes directly from the source; I haven't changed those fields, and the fix belongs there. When I catch an error that matters to a chart, I note it on the <a href="https://digmeoutliers.com/data-notes/" target="_top" style="color:inherit; text-decoration:underline;">Data Notes</a> page. And if you spot something wrong or missing, I'd encourage you to <a href="https://musicbrainz.org/register" target="_top" style="color:inherit; text-decoration:underline;">register at MusicBrainz</a> and fix it. A better MusicBrainz makes the data behind this blog richer and more accurate, and it helps everyone else who uses it too.</div>
</div>

<p class="phone-note">On a phone? Tap a dot or bar to see its details. These charts have more room on a laptop or tablet.</p>

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
  const tapPts = [];

  years.forEach((yr, yi) => {
    const px = x0 + (yi % perRow) * (panelW + gapX), py = 14 + Math.floor(yi / perRow) * (panelH + gapY + labelH);
    svg.append("text").attr("x", px).attr("y", py + 6).attr("fill", "#c9c8c3").attr("font-size", 12).attr("font-weight", 600).attr("opacity", yearOn.has(yr) ? 1 : 0.35).text(yr);
    const list = byYear.get(yr).slice().sort((a, b) => a.rank - b.rank);
    list.forEach((d, i) => {
      const cx = px + (i % cols) * pitch + pitch / 2, cy = py + labelH + Math.floor(i / cols) * pitch + pitch / 2;
      const c = category(d);
      const html = `<b>${yr} &middot; #${d.rank}</b><br>${d.artist_name}<br><i>${d.release_group_name}</i><br><span style="color:#898781">${swatch(c)}${c}</span>`;
      tapPts.push({x: cx, y: cy, html});
      svg.append("circle").attr("cx", cx).attr("cy", cy).attr("r", r).attr("fill", catColor[c]).attr("data-cat", c).attr("data-year", yr).attr("data-artist", d.artist_id)
        .style("transition", "opacity 0.15s")
        .on("pointerenter pointermove", (event) => tip.show(event, html, 92))
        .on("pointerleave", hideTip);
    });
  });

  enableTap(svg, tip, tapPts, 9);
  addLens(svg, {radius: 76, zoom: 3});

  const key = document.createElement("div");
  key.style.cssText = "display:flex;gap:10px;flex-wrap:wrap;margin:0.9rem 0 0.25rem;justify-content:center;";
  const buttons = new Map();
  function apply() {
    const sel = gridState.cat;
    svg.selectAll("circle[data-cat]")
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
  return wrap;
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;">

```js
waffleChart(selectedYears, selectedArtist)
```

</div>

```js
function artistTable(artistId, data) {
  const container = document.createElement("div");
  container.style.cssText = "margin:1rem 0 1.5rem;";

  if (!artistId) {
    container.style.cssText += "color:var(--theme-foreground-muted);font-size:14px;";
    container.textContent = "Search for an artist above to see every year they made the list, highlighted in the grid too.";
    return container;
  }

  const entries = data.filter((d) => d.artist_id === artistId).sort((a, b) => a.list_year - b.list_year);

  const heading = document.createElement("div");
  heading.style.cssText = "font-weight:600;font-size:15px;margin-bottom:0.5rem;";
  heading.textContent = `${entries[0].artist_name} — ${entries.length} appearance${entries.length === 1 ? "" : "s"} (${category(entries[0])})`;

  const tableWrap = document.createElement("div");
  tableWrap.style.cssText = "overflow-x:auto;";

  const table = document.createElement("table");
  table.style.cssText = "width:100%;max-width:520px;border-collapse:collapse;font-size:14px;";

  const thead = document.createElement("thead");
  const headRow = document.createElement("tr");
  for (const label of ["Year", "Rank", "Album"]) {
    const th = document.createElement("th");
    th.textContent = label;
    th.style.cssText = "text-align:left;padding:6px 12px 6px 0;border-bottom:1px solid var(--theme-foreground-faint);color:var(--theme-foreground-muted);font-weight:600;";
    headRow.append(th);
  }
  thead.append(headRow);

  const tbody = document.createElement("tbody");
  for (const d of entries) {
    const tr = document.createElement("tr");
    const tdYear = document.createElement("td");
    tdYear.textContent = d.list_year;
    tdYear.style.cssText = "padding:6px 12px 6px 0;border-bottom:1px solid var(--theme-foreground-faint);";
    const tdRank = document.createElement("td");
    tdRank.textContent = `#${d.rank}`;
    tdRank.style.cssText = "padding:6px 12px;border-bottom:1px solid var(--theme-foreground-faint);";
    const tdAlbum = document.createElement("td");
    tdAlbum.textContent = d.release_group_name;
    tdAlbum.style.cssText = "padding:6px 12px;border-bottom:1px solid var(--theme-foreground-faint);";
    tr.append(tdYear, tdRank, tdAlbum);
    tbody.append(tr);
  }
  table.append(thead, tbody);
  tableWrap.append(table);
  container.append(heading, tableWrap);
  return container;
}
```

```js
artistTable(selectedArtist, rows)
```

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

## Interesting observations

The grid above shows every album on every list. The charts below pull back to ask what they add up to.

### The share, year by year

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
    .on("pointerdown pointermove pointerenter", (event) => {
      const [mx] = d3.pointer(event);
      const i = Math.max(0, Math.min(years.length - 1, Math.round(((mx / pw) * (years[years.length - 1] - years[0])))));
      cursor.attr("x1", x(years[i])).attr("x2", x(years[i])).attr("opacity", 0.8);
      const lines = [...catOrder].reverse().map((k) => `<div style="display:flex;justify-content:space-between;gap:12px"><span>${swatch(k)}${k}</span><b>${(100 * (shares[i][k])).toFixed(0)}% <span style="font-weight:400;color:#898781">(${raw[i][k] || 0})</span></b></div>`);
      showTip(event, `<b>${years[i]}</b> &middot; ${tot[i]}<br>${lines.join("")}`);
    })
    .on("pointerleave", (event) => { cursor.attr("opacity", 0); hideTip(event); });
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

### Who gets to #1?

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
  const tapPts = [];
  const prev = {};   // last labeled #1 in each lane, so neighbors can alternate above/below
  ones.slice().sort((a, b) => a.list_year - b.list_year).forEach((d) => {
    const c = category(d), cx = x(d.list_year), cy = laneY[c];
    const html = `<b>${d.list_year}</b> &middot; ${d.artist_name}<br><i>${d.release_group_name}</i>`;
    tapPts.push({x: cx, y: cy, html});
    svg.append("circle").attr("cx", cx).attr("cy", cy).attr("r", 10).attr("fill", catColor[c])
      .on("pointerenter pointermove", (event) => showTip(event, html))
      .on("pointerleave", hideTip);
    if (c !== "Groups") {
      const near = prev[c] && d.list_year - prev[c].year <= 3;
      const side = near && prev[c].side === "below" ? "above" : "below";
      prev[c] = {year: d.list_year, side};
      svg.append("text").attr("x", cx).attr("y", side === "below" ? cy + 24 : cy - 17).attr("text-anchor", "middle").attr("fill", "#c9c8c3").attr("font-size", 10).text(d.artist_name);
    }
  });
  enableTap(svg, tip, tapPts, 26);
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;">

```js
numberOneLanes()
```

</div>

Bands took the top spot every year from 2001 to 2004. Sufjan Stevens broke the run in 2005, and then bands won it nine years straight. Since 2015, solo artists have hit #1 four times: Courtney Barnett twice, David Bowie, and Lizzo.

### Solo artists: counts, not just shares

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
  const endYs = cats.map((k) => y(data[data.length - 1].c[k] || 0));
  if (Math.abs(endYs[0] - endYs[1]) < 36) {   // push the two labels apart around their midpoint
    const mid = (endYs[0] + endYs[1]) / 2, lowFirst = endYs[0] < endYs[1];
    endYs[0] = mid + (lowFirst ? -18 : 18);
    endYs[1] = mid + (lowFirst ? 18 : -18);
  }
  cats.forEach((k, ci) => {
    [[2001, 2010], [2021, 2025]].forEach(([lo, hi]) => {
      const a = avg(k, lo, hi);
      g.append("line").attr("x1", x(lo)).attr("x2", x(hi)).attr("y1", y(a)).attr("y2", y(a)).attr("stroke", catColor[k]).attr("stroke-width", 1.5).attr("stroke-dasharray", "5 4").attr("opacity", 0.9);
    });
    g.append("path").attr("d", d3.line().x((d) => x(d.yr)).y((d) => y(d.c[k] || 0)).curve(d3.curveMonotoneX)(data)).attr("fill", "none").attr("stroke", catColor[k]).attr("stroke-width", 2.5);
    data.forEach((d) => g.append("circle").attr("cx", x(d.yr)).attr("cy", y(d.c[k] || 0)).attr("r", 3.4).attr("fill", catColor[k]));
    const endY = endYs[ci];
    g.append("text").attr("x", pw + 10).attr("y", endY).attr("dominant-baseline", "middle").attr("fill", catColor[k]).attr("font-size", 12).attr("font-weight", 600).text(k);
    g.append("text").attr("x", pw + 10).attr("y", endY + 14).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 10)
      .text(`${avg(k, 2001, 2010).toFixed(1)} → ${avg(k, 2021, 2025).toFixed(1)} a year`);
  });
  const cursor = g.append("line").attr("y1", 0).attr("y2", ph).attr("stroke", "#f0efec").attr("opacity", 0);
  g.append("rect").attr("width", pw).attr("height", ph).attr("fill", "transparent")
    .on("pointerdown pointermove pointerenter", (event) => {
      const [mx] = d3.pointer(event);
      const i = Math.max(0, Math.min(years.length - 1, Math.round((mx / pw) * (years[years.length - 1] - years[0]))));
      cursor.attr("x1", x(years[i])).attr("x2", x(years[i])).attr("opacity", 0.7);
      showTip(event, `<b>${years[i]}</b><br>${cats.map((k) => `<div style="display:flex;justify-content:space-between;gap:12px"><span>${swatch(k)}${k}</span><b>${data[i].c[k] || 0}</b></div>`).join("")}`);
    })
    .on("pointerleave", (event) => { cursor.attr("opacity", 0); hideTip(event); });
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

### Counting albums or counting artists?

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

### Who's behind the rise?

So where did all those solo women come from? One possibility is a handful of stars returning year after year. The other is a steady stream of new names. This chart counts the artists on each year's list and splits them in two: those appearing on a list for the first time (solid), and those who had been on an earlier year's list (faded).

```js
// ---- first appearance vs. returning, counted by artist (each artist once per year) ----
const firstYear = d3.rollup(rows, (v) => d3.min(v, (d) => d.list_year), (d) => d.artist_id);
const yearsOf = d3.rollup(rows, (v) => d3.sort(new Set(v.map((d) => d.list_year))), (d) => d.artist_id);
const catOfArtist = new Map(rows.map((d) => [d.artist_id, category(d)]));
const artistYear = (() => {
  const out = new Map(), seen = new Set();
  for (const d of rows) {
    const key = d.artist_id + "|" + d.list_year;
    if (seen.has(key)) continue;
    seen.add(key);
    const k = category(d) + "|" + d.list_year;
    const o = out.get(k) ?? {nNew: 0, nRet: 0};
    if (d.list_year === firstYear.get(d.artist_id)) o.nNew++; else o.nRet++;
    out.set(k, o);
  }
  return out;
})();
const ay = (c, yr) => artistYear.get(c + "|" + yr) ?? {nNew: 0, nRet: 0};
const newPerYear = (c, lo, hi) => d3.sum(d3.range(lo, hi + 1), (yr) => ay(c, yr).nNew) / (hi - lo + 1);
const returningShare = (c, lo, hi) => {
  const n = d3.sum(d3.range(lo, hi + 1), (yr) => ay(c, yr).nNew), r = d3.sum(d3.range(lo, hi + 1), (yr) => ay(c, yr).nRet);
  return 100 * r / (n + r);
};
```

```js
function newVsReturning() {
  const panels = ["Solo women", "Solo men"];
  const width = 880, m = {l: 34, r: 12, t: 40, b: 30}, gap = 40;
  const pw = (width - m.l - m.r - gap) / 2, ph = 250, height = m.t + ph + m.b;
  const ymax = d3.max(panels, (c) => d3.max(years, (yr) => ay(c, yr).nNew + ay(c, yr).nRet));
  const y = d3.scaleLinear().domain([0, Math.ceil(ymax / 5) * 5]).range([ph, 0]);
  const x = d3.scaleBand().domain(years).range([0, pw]).padding(0.18);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  panels.forEach((c, pi) => {
    const g = svg.append("g").attr("transform", `translate(${m.l + pi * (pw + gap)},${m.t})`);
    g.append("text").attr("x", 0).attr("y", -18).attr("fill", catColor[c]).attr("font-size", 13).attr("font-weight", 600).text(c);
    y.ticks(5).forEach((t) => {
      g.append("line").attr("x1", 0).attr("x2", pw).attr("y1", y(t)).attr("y2", y(t)).attr("stroke", "#33322f");
      g.append("text").attr("x", -8).attr("y", y(t)).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 10).text(t);
    });
    years.forEach((yr) => {
      const a = ay(c, yr);
      g.append("rect").attr("x", x(yr)).attr("width", x.bandwidth()).attr("y", y(a.nNew)).attr("height", ph - y(a.nNew)).attr("fill", catColor[c]);
      g.append("rect").attr("x", x(yr)).attr("width", x.bandwidth()).attr("y", y(a.nNew + a.nRet)).attr("height", y(a.nNew) - y(a.nNew + a.nRet)).attr("fill", catColor[c]).attr("opacity", 0.38);
      g.append("rect").attr("x", x(yr) - 1).attr("width", x.bandwidth() + 2).attr("y", 0).attr("height", ph).attr("fill", "transparent")
        .on("pointerenter pointermove", (event) => showTip(event, `<b>${yr}</b> &middot; ${c}<br>${a.nNew} first-time artist${a.nNew === 1 ? "" : "s"}<br>${a.nRet} returning`))
        .on("pointerleave", hideTip);
      if ((yr - 2001) % 4 === 0) g.append("text").attr("x", x(yr) + x.bandwidth() / 2).attr("y", ph + 20).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 11).text(yr);
    });
  });
  const legend = document.createElement("div");
  legend.style.cssText = "display:flex;gap:20px;flex-wrap:wrap;margin:0.75rem 0 0.25rem;justify-content:center;";
  legend.innerHTML = [["#c9c8c3", 1, "First time on a list"], ["#c9c8c3", 0.38, "On an earlier list too"]].map(([c, o, t]) =>
    `<span style="display:flex;align-items:center;gap:6px;font-size:13px;color:#c9c8c3"><span style="width:12px;height:12px;border-radius:3px;background:${c};opacity:${o};display:inline-block"></span>${t}</span>`).join("");
  const wrap = document.createElement("div");
  wrap.append(svg.node(), legend);
  return wrap;
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.75rem;max-width:900px;margin:0 auto;">

```js
newVsReturning()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Each artist counts once per year. The lists start in 2001, so the earliest bars treat everyone as new, including veterans who had been recording for years. That's why the comparisons here start in 2011.</p>

```js
statTiles([
  {label: "New solo women per year", value: `${newPerYear("Solo women", 2011, 2015).toFixed(1)} → ${newPerYear("Solo women", 2021, 2025).toFixed(1)}`,
   caption: "Artists making a list for the first time, 2011–2015 compared with 2021–2025."},
  {label: "New solo men per year", value: `${newPerYear("Solo men", 2011, 2015).toFixed(1)} → ${newPerYear("Solo men", 2021, 2025).toFixed(1)}`,
   caption: "The same two periods. The door narrowed for men as it widened for women."},
  {label: "Returning solo women", value: `${returningShare("Solo women", 2011, 2015).toFixed(0)}% → ${returningShare("Solo women", 2021, 2025).toFixed(0)}%`,
   caption: `Share of each year's solo women who had been listed before. For solo men: ${returningShare("Solo men", 2011, 2015).toFixed(0)}% → ${returningShare("Solo men", 2021, 2025).toFixed(0)}%.`}
])
```

The answer is new names. About ${newPerYear("Solo women", 2011, 2015).toFixed(0)} solo women a year made a list for the first time in 2011&ndash;2015, and about ${newPerYear("Solo women", 2021, 2025).toFixed(0)} a year did in 2021&ndash;2025. For solo men it went the other way, from about ${newPerYear("Solo men", 2011, 2015).toFixed(0)} a year to about ${newPerYear("Solo men", 2021, 2025).toFixed(0)}. Once artists are in, women and men come back at about the same rate (more on that below), so the change is mostly in who gets through the door, not in who stays.

### The names behind the numbers

```js
const womenSince2016 = rows.filter((d) => d.list_year >= 2016 && category(d) === "Solo women");
const womenListed = new Set(womenSince2016.map((d) => d.artist_id)).size;
const coreWomen = repeatNames("Solo women");
const coreEntries = d3.sum(coreWomen, (a) => a.items.length);
```

New names are only half of the story, though. Once they arrive, many of them stay. By 2021&ndash;2025, ${returningShare("Solo women", 2021, 2025).toFixed(0)}% of the solo women on each year's list had been listed before, up from ${returningShare("Solo women", 2011, 2015).toFixed(0)}% in 2011&ndash;2015. And a small core does a lot of the work: the ${coreWomen.length} solo women with three or more albums on the lists since 2016 are only ${(100 * coreWomen.length / womenListed).toFixed(0)}% of the ${womenListed} different solo women listed in that stretch, but they account for ${(100 * coreEntries / womenSince2016.length).toFixed(0)}% of the entries. So the rise has two parts: a wider front door, and a group of artists who keep coming back through it.

Here are the solo artists who landed three or more albums on the lists since 2016: ${repeatNames("Solo women").length} women and ${repeatNames("Solo men").length} men. Each dot is an album, placed in the year it made the list. Hover to see which one.

```js
function repeatNames(c) {
  const by = d3.group(rows.filter((d) => d.list_year >= 2016 && category(d) === c), (d) => d.artist_id);
  return [...by].filter(([id, v]) => v.length >= 3)
    .map(([id, v]) => ({name: v[0].artist_name, items: v.slice().sort((a, b) => a.list_year - b.list_year)}))
    .sort((a, b) => b.items.length - a.items.length || a.items[0].list_year - b.items[0].list_year || a.name.localeCompare(b.name));
}
```

```js
function repeatArtists() {
  const panels = ["Solo women", "Solo men"].map((c) => ({c, list: repeatNames(c)}));
  const yrs = d3.range(2016, 2026);
  const rowH = 23, m = {l: 150, r: 96, t: 8, b: 8}, headH = 58;
  const width = 880, pw = width - m.l - m.r;
  const x = d3.scalePoint(yrs, [0, pw]).padding(0.5);
  const height = m.t + m.b + d3.sum(panels, (p) => headH + p.list.length * rowH);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const tapPts = [];
  let top = m.t;
  panels.forEach(({c, list}) => {
    svg.append("text").attr("x", 20).attr("y", top + 18).attr("fill", catColor[c]).attr("font-size", 13).attr("font-weight", 600).text(c);
    svg.append("text").attr("x", 20 + 90).attr("y", top + 18).attr("fill", "#898781").attr("font-size", 12).text(`${list.length} artists with three or more albums on the lists, 2016–2025`);
    yrs.forEach((yr) => svg.append("text").attr("x", m.l + x(yr)).attr("y", top + 46).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(yr));
    const g = svg.append("g").attr("transform", `translate(0,${top + headH})`);
    yrs.forEach((yr) => g.append("line").attr("x1", m.l + x(yr)).attr("x2", m.l + x(yr)).attr("y1", -4).attr("y2", list.length * rowH - 6).attr("stroke", "#2a2a27"));
    list.forEach((a, i) => {
      const cy = i * rowH + 8;
      g.append("text").attr("x", m.l - 14).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 12).text(a.name);
      g.append("line").attr("x1", m.l + x(a.items[0].list_year)).attr("x2", m.l + x(a.items[a.items.length - 1].list_year)).attr("y1", cy).attr("y2", cy).attr("stroke", catColor[c]).attr("stroke-width", 2).attr("opacity", 0.3);
      a.items.forEach((d) => {
        const html = `<b>${a.name}</b><br>${d.list_year} &middot; #${d.rank}<br><i>${d.release_group_name}</i>`;
        tapPts.push({x: m.l + x(d.list_year), y: top + headH + cy, html});
        g.append("circle").attr("cx", m.l + x(d.list_year)).attr("cy", cy).attr("r", 6).attr("fill", catColor[c])
          .on("pointerenter pointermove", (event) => showTip(event, html))
          .on("pointerleave", hideTip);
      });
      g.append("text").attr("x", m.l + pw + 18).attr("y", cy).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(`${a.items.length} albums`);
    });
    top += headH + list.length * rowH;
  });
  enableTap(svg, tip, tapPts, 14);
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 1rem;max-width:900px;margin:0 auto;">

```js
repeatArtists()
```

</div>

```js
// how bumpy each line is: the average change from one year to the next, 2011–2025
const countIn = (c, yr) => (byYear.get(yr) ?? []).filter((d) => category(d) === c).length;
const swing = (c) => d3.mean(d3.range(2012, 2026), (yr) => Math.abs(countIn(c, yr) - countIn(c, yr - 1)));
```

Soccer Mommy landed an album in 2018, 2020, 2022, and 2024, and Little Simz in 2019, 2021, 2023, and 2025, a new album every other year. Mitski and Beyonc&eacute; landed four each, and Angel Olsen landed five between 2016 and 2022. On the men's side, Ty Segall landed three years running (2016&ndash;2018) and then again in 2021, 2024, and 2025. Kevin Morby landed five times between 2016 and 2022 and hasn't since. In general the men's line is the bumpier one: from one year to the next, the number of solo men on the list moves by about ${swing("Solo men").toFixed(0)} albums on average since 2011, against about ${swing("Solo women").toFixed(0)} for solo women.

That raises a question about the men. Did they stop making albums, or did their albums stop landing?

### Did solo men stop making albums?

To find out, I took the solo artists who were already established, meaning first listed in 2015 or earlier, and looked up every studio album MusicBrainz has for them from 2016 to 2025, whether or not it made a list.

```js
const studio = FileAttachment("data/studio_albums_2016_2025.csv").csv({typed: true});
```

```js
const activity = Object.fromEntries(["Solo women", "Solo men", "Groups"].map((c) => {
  const ids = new Set([...firstYear].filter(([id, fy]) => fy <= 2015 && catOfArtist.get(id) === c).map(([id]) => id));
  const al = studio.filter((d) => ids.has(d.artist_id));
  const releasers = new Set(al.map((d) => d.artist_id)).size;
  const listed = d3.sum(al, (d) => d.on_list);
  return [c, {c, n: ids.size, releasers, albums: al.length, listed, pct: 100 * listed / al.length}];
}));
const albumsOf = (name) => {
  const id = rows.find((d) => d.artist_name === name)?.artist_id;
  const al = studio.filter((d) => d.artist_id === id);
  return {n: al.length, listed: d3.sum(al, (d) => d.on_list)};
};
```

```js
statTiles([
  {label: "Established solo women still releasing", value: `${activity["Solo women"].releasers} of ${activity["Solo women"].n}`,
   caption: `Put out at least one studio album in 2016–2025 (${(100 * activity["Solo women"].releasers / activity["Solo women"].n).toFixed(0)}%).`},
  {label: "Established solo men still releasing", value: `${activity["Solo men"].releasers} of ${activity["Solo men"].n}`,
   caption: `The same test (${(100 * activity["Solo men"].releasers / activity["Solo men"].n).toFixed(0)}%). They didn't go quiet.`},
  {label: "Albums that made a list", value: `${activity["Solo women"].pct.toFixed(0)}% vs ${activity["Solo men"].pct.toFixed(0)}%`,
   caption: `Solo women's albums compared with solo men's, 2016–2025.`}
])
```

```js
function releaseVsListed() {
  const cats = ["Solo women", "Solo men", "Groups"];
  const width = 880, m = {l: 150, r: 250, t: 14, b: 14}, rowH = 46, height = m.t + cats.length * rowH + m.b;
  const pw = width - m.l - m.r;
  const x = d3.scaleLinear().domain([0, 50]).range([0, pw]);
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const g = svg.append("g").attr("transform", `translate(${m.l},${m.t})`);
  cats.forEach((c, i) => {
    const a = activity[c], cy = i * rowH + 20;
    g.append("text").attr("x", -14).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 13).text(c);
    g.append("rect").attr("x", 0).attr("y", cy - 10).attr("width", pw).attr("height", 20).attr("rx", 3).attr("fill", "#232321");
    g.append("rect").attr("x", 0).attr("y", cy - 10).attr("width", x(a.pct)).attr("height", 20).attr("rx", 3).attr("fill", catColor[c])
      .on("pointerenter pointermove", (event) => showTip(event, `<b>${c}</b><br>${a.listed} of ${a.albums} albums made a list`))
      .on("pointerleave", hideTip);
    g.append("text").attr("x", pw + 14).attr("y", cy - 1).attr("dominant-baseline", "middle").attr("fill", "#f0efec").attr("font-size", 14).attr("font-weight", 600).text(`${a.pct.toFixed(0)}% made a list`);
    g.append("text").attr("x", pw + 14).attr("y", cy + 15).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(`${a.listed} of ${a.albums} albums · ${a.releasers} of ${a.n} artists`);
  });
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.75rem;max-width:900px;margin:0 auto;">

```js
releaseVsListed()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Studio albums released 2016&ndash;2025 by artists first listed in 2015 or earlier, as MusicBrainz records them. Reissues and unusual releases can slip in, so treat the percentages as approximate.</p>

So the men didn't go quiet. ${(100 * activity["Solo men"].releasers / activity["Solo men"].n).toFixed(0)}% of established solo men put out at least one studio album, about the same as the women, and together they released ${activity["Solo men"].albums} of them. Damien Jurado put out ${albumsOf("Damien Jurado").n} studio albums in that stretch and ${albumsOf("Damien Jurado").listed} made a list. Andrew Bird: ${albumsOf("Andrew Bird").n} and ${albumsOf("Andrew Bird").listed}. Neil Young: ${albumsOf("Neil Young").n} and ${albumsOf("Neil Young").listed}. Ty Segall shows the other outcome: ${albumsOf("Ty Segall").n} albums, ${albumsOf("Ty Segall").listed} of them on lists.

What changed is the odds. About ${activity["Solo men"].pct.toFixed(0)}% of those men's albums made a list, compared with ${activity["Solo women"].pct.toFixed(0)}% of the women's. I can't tell from this whether that is listener taste, what KEXP championed, or both. How much those albums were actually played is a separate question for a later post.

### Once they're in, do they come back?

The first post asked who sticks around, and this is the same question for these groups. Of the artists first listed from 2011 to 2020, how many came back to a later list within five years?

```js
// how long it takes returning artists to come back (artists first listed by 2015, so 10+ years are observable)
const _gaps = [...firstYear].filter(([id, fy]) => fy <= 2015).map(([id]) => yearsOf.get(id)).filter((ys) => ys.length >= 2).map((ys) => ys[1] - ys[0]);
const within = (k) => Math.round(100 * _gaps.filter((g) => g <= k).length / _gaps.length);
```

Why five years, and why start in 2011? Of the artists who ever came back, ${within(3)}% were back within three years and ${within(5)}% within five, so five years catches the large majority of comebacks and still lets me include artists who debuted as recently as 2020, just as the solo women's rise was taking off. Starting in 2011 skips the early years, when the lists had no history and almost every artist looked like a newcomer.

```js
function wilson(k, n, z = 1.96) {
  const p = k / n, d = 1 + z * z / n, c = p + z * z / (2 * n), a = z * Math.sqrt(p * (1 - p) / n + z * z / (4 * n * n));
  return [100 * (c - a) / d, 100 * (c + a) / d];
}
const backWithin = (id, k) => yearsOf.get(id).some((y) => y > firstYear.get(id) && y <= firstYear.get(id) + k);
const retention = ["Groups", "Solo women", "Solo men"].map((c) => {
  const ids = [...firstYear].filter(([id, fy]) => fy >= 2011 && fy <= 2020 && catOfArtist.get(id) === c).map(([id]) => id);
  const back = ids.filter((id) => backWithin(id, 5)).length;
  const [lo, hi] = wilson(back, ids.length);
  return {c, n: ids.length, back, p: 100 * back / ids.length, lo, hi};
});
const retOf = Object.fromEntries(retention.map((r) => [r.c, r]));

function retentionChart() {
  const width = 880, height = 250, m = {l: 120, r: 190, t: 20, b: 40};
  const pw = width - m.l - m.r;
  const x = d3.scaleLinear().domain([20, 80]).range([0, pw]);
  const rowH = 58;
  const tapPts = [];
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]).attr("width", width).attr("height", height).attr("style", CARD);
  const g = svg.append("g").attr("transform", `translate(${m.l},${m.t})`);
  [20, 30, 40, 50, 60, 70, 80].forEach((t) => {
    g.append("line").attr("x1", x(t)).attr("x2", x(t)).attr("y1", 0).attr("y2", retention.length * rowH - 10).attr("stroke", "#33322f");
    g.append("text").attr("x", x(t)).attr("y", retention.length * rowH + 6).attr("text-anchor", "middle").attr("fill", "#898781").attr("font-size", 10).text(t + "%");
  });
  retention.forEach((r, i) => {
    const cy = i * rowH + 20;
    g.append("text").attr("x", -14).attr("y", cy).attr("text-anchor", "end").attr("dominant-baseline", "middle").attr("fill", "#c9c8c3").attr("font-size", 13).text(r.c);
    g.append("line").attr("x1", x(r.lo)).attr("x2", x(r.hi)).attr("y1", cy).attr("y2", cy).attr("stroke", catColor[r.c]).attr("stroke-width", 6).attr("stroke-linecap", "round").attr("opacity", 0.45);
    const html = `<b>${r.c}</b><br>${r.back} of ${r.n} came back<br><span style="color:#898781">plausible range ${r.lo.toFixed(0)}–${r.hi.toFixed(0)}%</span>`;
    tapPts.push({x: m.l + x(r.p), y: m.t + cy, html});
    g.append("circle").attr("cx", x(r.p)).attr("cy", cy).attr("r", 9).attr("fill", catColor[r.c])
      .on("pointerenter pointermove", (event) => showTip(event, html))
      .on("pointerleave", hideTip);
    g.append("text").attr("x", pw + 16).attr("y", cy - 7).attr("dominant-baseline", "middle").attr("fill", "#f0efec").attr("font-size", 14).attr("font-weight", 600).text(`${r.p.toFixed(0)}% came back`);
    g.append("text").attr("x", pw + 16).attr("y", cy + 10).attr("dominant-baseline", "middle").attr("fill", "#898781").attr("font-size", 11).text(`range ${r.lo.toFixed(0)}–${r.hi.toFixed(0)}% · ${r.n} artists`);
  });
  enableTap(svg, tip, tapPts, 30);
  return svg.node();
}
```

<div class="card" style="background:#1a1a19;padding:1.5rem 1.5rem 0.75rem;max-width:900px;margin:0 auto;">

```js
retentionChart()
```

</div>

<p style="font-size:13px;color:var(--theme-foreground-muted);">Dots are the share of artists first listed in 2011&ndash;2020 who appeared on another year's list within five years. The line is the range the true figure could plausibly fall in, given how many artists there are. Where the lines overlap, the data can't tell the groups apart.</p>

About ${retOf["Solo women"].p.toFixed(0)}% of the solo women came back, compared with ${retOf["Solo men"].p.toFixed(0)}% of the solo men and ${retOf["Groups"].p.toFixed(0)}% of the bands. The solo women's dot sits a little higher, but the ranges overlap, so the data can't separate the three. That is the point. If the women's rise came from a few favorites returning far more often than anyone else, they would stand out clearly here. They don't. More women got on the lists, and once they did, they came back at a similar rate to everyone else.

<div style="border-left:3px solid #58cec8; padding:0.85rem 1.25rem; margin:1.25rem 0;">
  <div style="font-size:12px; text-transform:uppercase; letter-spacing:0.04em; color:var(--theme-foreground-faint); margin-bottom:0.4rem;">What this can't tell us</div>
  <div style="font-size:15px; line-height:1.6; color:var(--theme-foreground-muted);">Gender is only recorded for individual artists, so every gender figure here covers solo artists, about a third of everyone on the lists. I don't assign one to bands: lineups change from album to album, and MusicBrainz counts some solo-led projects, like Japanese Breakfast, as bands, so they show up as purple here. Five non-binary solo artists are too few to chart on their own, so they're left out of the gender percentages. &ldquo;New&rdquo; means new to these lists, which start in 2001, and the album counts in the last two sections come from MusicBrainz's studio album listings, so a few odd releases can slip in.</div>
</div>
