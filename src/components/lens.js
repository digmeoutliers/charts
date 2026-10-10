import * as d3 from "npm:d3";
import {isPinned, unpin} from "./tooltip.js";

// A magnifying lens for a dense SVG chart, like the zoom preview on a ticket site's seat map.
// Call it last, after everything else is drawn: it moves the chart's drawing into one group,
// then shows a zoomed copy of that group inside a round window that follows the pointer.
// Mouse: the lens sits under the cursor. Touch: tap, and the lens appears above the finger.
const disc = (r) => `M${r},0A${r},${r} 0 1,0 ${-r},0A${r},${r} 0 1,0 ${r},0Z`;

export function addLens(svg, {radius = 64, zoom = 4, touchLift = 1.6} = {}) {
  const node = svg.node();
  const id = "lens" + Math.random().toString(36).slice(2, 8);

  const content = svg.append("g").attr("id", id + "-content");
  [...node.childNodes].forEach((child) => { if (child !== content.node()) content.node().appendChild(child); });

  svg.append("defs").append("clipPath").attr("id", id + "-clip").append("path").attr("d", disc(radius));
  const lens = svg.append("g").attr("pointer-events", "none").style("display", "none");
  lens.append("path").attr("d", disc(radius + 2)).attr("fill", "#1a1a19").attr("stroke", "#f0efec").attr("stroke-width", 1.5);
  const use = lens.append("g").attr("clip-path", `url(#${id}-clip)`).append("use").attr("href", `#${id}-content`);
  lens.append("path").attr("d", "M-7,0H7M0,-7V7").attr("stroke", "#f0efec").attr("stroke-width", 0.8).attr("opacity", 0.55);

  // a ring that marks the dot a click pinned (drawn with the chart, so it scrolls and scales with it)
  const ring = content.append("path").attr("fill", "none").attr("stroke", "#f0efec").attr("stroke-width", 1.6).style("display", "none");
  unpin();   // a redraw (new filter, new search) clears any card left from the old drawing

  const vb = node.viewBox.baseVal;
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
  let frame = 0;
  function show(px, py, lift) {
    if (isPinned()) return;
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(() => {
      const lx = clamp(px, radius + 2, vb.width - radius - 2);
      const ly = clamp(py - lift, radius + 2, vb.height - radius - 2);
      lens.attr("transform", `translate(${lx},${ly})`).style("display", null);
      use.attr("transform", `scale(${zoom}) translate(${-px},${-py})`);
    });
  }
  function hide() { cancelAnimationFrame(frame); lens.style("display", "none"); }

  svg.on("pointermove.lens pointerenter.lens", (event) => {
    if (event.pointerType === "touch") return;
    const [px, py] = d3.pointer(event, node);
    show(px, py, 0);
  });
  svg.on("pointerleave.lens", (event) => { if (event.pointerType !== "touch") hide(); });
  svg.on("pointerdown.lens", (event) => {
    if (event.pointerType !== "touch") return;
    const [px, py] = d3.pointer(event, node);
    show(px, py, radius * touchLift);
  });
  // a tap anywhere else closes a lens that a tap opened
  const away = (event) => {
    if (!node.isConnected) return document.removeEventListener("pointerdown", away);
    if (event.pointerType === "touch" && !node.contains(event.target)) hide();
  };
  document.addEventListener("pointerdown", away);

  return {
    hide,
    mark(x, y, r = 8) { ring.attr("d", disc(r)).attr("transform", `translate(${x},${y})`).style("display", null); },
    clearMark() { ring.style("display", "none"); }
  };
}
