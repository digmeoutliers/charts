import * as d3 from "npm:d3";

// Shared hover/tap tooltip for the chart pages.
//  - stays inside the window (flips to the left of the cursor near the right edge)
//  - works on touch: a tap shows it and it stays until you tap somewhere else
// One tooltip element serves every chart on the page (only one is ever visible).
let el = null;
let lastShown = -1e9;

// A pinned card: the details of one clicked dot, left on the page until it is dismissed.
let pinEl = null, pinBody = null, pinClose = null, pinned = false;
export function isPinned() { return pinned; }
export function unpin() {
  if (pinEl) pinEl.style.display = "none";
  const done = pinClose; pinned = false; pinClose = null;
  if (done) done();
}
export function pin(event, html, onClose) {
  if (pinned) unpin();
  element().style.opacity = 0;   // the hover tooltip steps aside
  if (!pinEl) {
    pinEl = document.createElement("div");
    pinEl.style.cssText = "position:absolute;background:#1a1a19;color:#f0efec;border:1px solid #8a8985;border-radius:8px;padding:8px 30px 8px 10px;font-size:12px;line-height:1.35;font-family:var(--sans-serif);z-index:11;max-width:260px;box-shadow:0 4px 16px rgba(0,0,0,0.35);";
    pinBody = document.createElement("div");
    const x = document.createElement("button");
    x.type = "button"; x.textContent = "×"; x.setAttribute("aria-label", "Close");
    x.style.cssText = "position:absolute;top:2px;right:6px;border:0;background:transparent;color:#c9c8c3;font-size:18px;line-height:1;cursor:pointer;padding:2px;";
    x.addEventListener("click", (e) => { e.stopPropagation(); unpin(); });
    pinEl.append(pinBody, x);
    document.body.appendChild(pinEl);
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") unpin(); });
    // a click anywhere outside the card and outside any chart also takes it down
    document.addEventListener("click", (e) => { if (pinned && !pinEl.contains(e.target) && !(e.target.closest && e.target.closest("svg"))) unpin(); });
  }
  pinBody.innerHTML = html;
  pinEl.style.display = "block";
  const w = pinEl.offsetWidth, h = pinEl.offsetHeight, gap = 16, pad = 8;
  let x = event.clientX + gap, y = event.clientY + gap;
  if (x + w + pad > window.innerWidth) x = event.clientX - w - gap;
  if (y + h + pad > window.innerHeight) y = event.clientY - h - gap;
  pinEl.style.left = Math.max(pad, x) + window.scrollX + "px";
  pinEl.style.top = Math.max(pad, y) + window.scrollY + "px";
  pinned = true;
  pinClose = onClose || null;
}

function element() {
  if (el) return el;
  el = document.createElement("div");
  el.style.cssText = "position:fixed;pointer-events:none;background:#1a1a19;color:#f0efec;border:1px solid #383835;border-radius:8px;padding:8px 10px;font-size:12px;line-height:1.35;font-family:var(--sans-serif);opacity:0;transition:opacity 0.1s;z-index:10;";
  document.body.appendChild(el);
  // a tap elsewhere closes a tooltip that a tap opened (mouse tooltips close on pointerleave)
  document.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "touch" && event.timeStamp - lastShown > 400) el.style.opacity = 0;
  });
  return el;
}

export function makeTooltip({minWidth = 0, maxWidth = 260, gap: defaultGap = 14} = {}) {
  let gap = defaultGap;   // distance from the pointer; charts with a magnifying lens use a larger one
  function place(event) {
    const t = element(), pad = 8;
    const w = t.offsetWidth, h = t.offsetHeight;
    let x = event.clientX + gap, y = event.clientY + gap;
    if (x + w + pad > window.innerWidth) x = event.clientX - w - gap;
    if (y + h + pad > window.innerHeight) y = event.clientY - h - gap;
    t.style.left = Math.max(pad, x) + "px";
    t.style.top = Math.max(pad, y) + "px";
  }
  function hideNow() { element().style.opacity = 0; }
  return {
    show(event, html, customGap) {
      if (pinned) return;
      gap = customGap ?? defaultGap;
      const t = element();
      t.style.minWidth = minWidth + "px";
      t.style.maxWidth = maxWidth + "px";
      if (html != null) t.innerHTML = html;
      t.style.opacity = 1;
      lastShown = event.timeStamp;
      place(event);
    },
    move(event) { if (!pinned) place(event); },
    hide(event) { if (!event || event.pointerType !== "touch") hideNow(); },
    hideNow
  };
}

// Touch screens: the dots are only a few pixels wide, so a tap picks the nearest dot.
// points = [{x, y, html}] in the SVG's own coordinates; svg is a d3 selection.
export function enableTap(svg, tip, points, threshold = 18, lens = null) {
  if (!points.length) return;
  const delaunay = d3.Delaunay.from(points, (p) => p.x, (p) => p.y);
  svg.on("pointerdown.tap", (event) => {
    if (event.pointerType !== "touch") return;
    const [px, py] = d3.pointer(event, svg.node());
    const p = points[delaunay.find(px, py)];
    if (Math.hypot(px - p.x, py - p.y) > threshold) return;
    tip.show(event, p.html);
  });
  // Mouse, on a chart with a lens: a click pins the details of the dot under the crosshair and
  // puts the lens away; a click on empty space (or Esc, or the x) takes the card down again.
  if (lens) svg.on("click.pin", (event) => {
    if (event.pointerType === "touch") return;
    const [px, py] = d3.pointer(event, svg.node());
    const p = points[delaunay.find(px, py)];
    if (Math.hypot(px - p.x, py - p.y) > threshold) { unpin(); return; }
    pin(event, p.html, () => lens.clearMark());
    lens.hide();
    lens.mark(p.x, p.y);
  });
}
