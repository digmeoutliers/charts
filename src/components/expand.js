// "Expand" buttons for the chart cards: opens one chart, big, in a pop-up over the whole window.
// The pop-up is this same page loaded with ?chart=<id> (a page that shows only that chart, scaled up).
// Inside the blog post the chart sits in an iframe too small to grow, so it asks the post page to open
// the pop-up instead (the post's footer script does that). If nothing answers, it opens its own.

const ICON = '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 1.5h3.5V5M5 11.5H1.5V8M11.5 1.5 7.5 5.5M1.5 11.5l4-4"/></svg>';

function chartUrl(id, mode) {
  const u = new URL(location.href);
  u.search = ""; u.hash = "";
  u.searchParams.set("chart", id);
  if (mode) u.searchParams.set("mode", mode);
  return u.href;
}

let closeOverlay = null;
export function showOverlay(url) {
  if (closeOverlay) closeOverlay();
  const wrap = document.createElement("div");
  wrap.style.cssText = "position:fixed;inset:0;z-index:2147483000;background:rgba(10,10,10,0.82);display:flex;align-items:center;justify-content:center;padding:2.5vh 2.5vw;";
  const frame = document.createElement("iframe");
  frame.src = url;
  frame.title = "Expanded chart";
  frame.style.cssText = "width:100%;height:100%;max-width:1900px;border:0;border-radius:12px;background:#1a1a19;";
  const x = document.createElement("button");
  x.type = "button"; x.textContent = "×"; x.setAttribute("aria-label", "Close");
  x.style.cssText = "position:absolute;top:8px;right:14px;border:0;background:transparent;color:#f0efec;font-size:30px;line-height:1;cursor:pointer;padding:4px 8px;";
  wrap.append(frame, x);
  const prevOverflow = document.documentElement.style.overflow;
  document.documentElement.style.overflow = "hidden";
  const onKey = (e) => { if (e.key === "Escape") closeOverlay(); };
  closeOverlay = () => {
    wrap.remove();
    document.documentElement.style.overflow = prevOverflow;
    document.removeEventListener("keydown", onKey);
    window.removeEventListener("message", onMsg);
    closeOverlay = null;
  };
  const onMsg = (e) => { if (e.data && e.data.dmoCollapse) closeOverlay(); };
  x.onclick = () => closeOverlay();
  wrap.addEventListener("click", (e) => { if (e.target === wrap) closeOverlay(); });
  document.addEventListener("keydown", onKey);
  window.addEventListener("message", onMsg);
  document.body.appendChild(wrap);
  frame.focus();
}

export function openChart(id, mode) {
  const url = chartUrl(id, mode);
  if (window.self === window.top) return showOverlay(url);
  let answered = false;
  const onAck = (e) => { if (e.data && e.data.dmoExpandAck) answered = true; };
  window.addEventListener("message", onAck);
  window.parent.postMessage({dmoExpand: {url}}, "*");
  setTimeout(() => {
    window.removeEventListener("message", onAck);
    if (!answered) showOverlay(url);
  }, 400);
}

// getMode: returns the current value of the page's own switch, if it has one, so the pop-up opens in the same state
export function addExpandButtons(getMode) {
  for (const card of document.querySelectorAll("[data-chart]")) {
    if (card.querySelector(".dmo-expand")) continue;
    const b = document.createElement("button");
    b.type = "button";
    b.className = "dmo-expand";
    b.setAttribute("aria-label", "Expand this chart");
    b.innerHTML = ICON + "<span>Expand</span>";
    b.style.cssText = "position:absolute;top:10px;right:10px;z-index:5;display:flex;align-items:center;gap:6px;font-size:12px;color:#c9c8c3;background:#232321;border:1px solid #383835;border-radius:999px;padding:4px 10px;cursor:pointer;font-family:var(--sans-serif);";
    b.onclick = () => openChart(card.dataset.chart, getMode ? getMode() : undefined);
    card.append(b);
  }
}
