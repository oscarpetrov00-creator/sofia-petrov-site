/* Live Google reviews via Places API (New), Place Details.
 *
 * Fill in both values to switch it on. Until then everything review-related
 * stays hidden, so the site never shows an empty box.
 *  - API_KEY: a browser key restricted to Places API (New) and to the site's
 *    domains (HTTP referrers). It is visible in page source by design.
 *  - PLACE_ID: the practice's Google place ID (starts with "ChIJ").
 *
 * Google's terms: no caching of review content (only the place ID may be
 * stored), every review credits its author, and the Google Maps logo is shown.
 */
(function () {
  var API_KEY = "AIzaSyAycDEDU7wHFBxztQeO67j8j-8RLtuJj54";
  var PLACE_ID = "ChIJcdsXyZu_j1QR1B-7F93P8NA";
  if (!API_KEY || !PLACE_ID) return;

  var writeUrl = "https://search.google.com/local/writereview?placeid=" + encodeURIComponent(PLACE_ID);
  document.querySelectorAll("[data-write-review]").forEach(function (el) {
    var a = el.tagName === "A" ? el : el.querySelector("a");
    if (a) a.href = writeUrl;
    el.hidden = false;
  });

  var badge = document.getElementById("g-rating");
  var section = document.getElementById("reviews");
  if (!badge && !section) return;

  var fields = "rating,userRatingCount,reviews,googleMapsUri,googleMapsLinks";
  var url = "https://places.googleapis.com/v1/places/" + encodeURIComponent(PLACE_ID) +
    "?fields=" + fields + "&languageCode=en&key=" + encodeURIComponent(API_KEY);

  fetch(url)
    .then(function (r) { if (!r.ok) throw new Error("Places " + r.status); return r.json(); })
    .then(render)
    .catch(function (e) { if (window.console) console.warn("Reviews unavailable:", e.message); });

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function stars(value) {
    var s = el("span", "stars");
    s.setAttribute("aria-label", value.toFixed(1) + " out of 5 stars");
    var fill = el("span", "stars-fill");
    fill.style.width = Math.max(0, Math.min(100, (value / 5) * 100)) + "%";
    s.appendChild(fill);
    return s;
  }

  function render(p) {
    if (!p || !p.rating) return;
    var links = p.googleMapsLinks || {};
    var reviewsUri = links.reviewsUri || p.googleMapsUri;
    var count = p.userRatingCount || 0;
    var countText = count + (count === 1 ? " review" : " reviews");

    if (badge) {
      var a = el("a", "g-rating-link");
      a.href = reviewsUri;
      a.appendChild(stars(p.rating));
      a.appendChild(el("strong", null, p.rating.toFixed(1)));
      a.appendChild(document.createTextNode(" on Google · " + countText));
      badge.appendChild(a);
      badge.hidden = false;
    }

    if (!section) return;
    var list = (p.reviews || []).filter(function (r) { return r.text && r.text.text; });
    if (!list.length) return;
    // Reviews that mention the laser work go first; otherwise keep Google's order.
    var mentions = function (r) { return /lanap|laser/i.test(r.text.text) ? 0 : 1; };
    list = list.map(function (r, i) { return [r, i]; })
      .sort(function (a, b) { return mentions(a[0]) - mentions(b[0]) || a[1] - b[1]; })
      .map(function (x) { return x[0]; })
      .slice(0, 3);

    section.querySelector("[data-summary]").textContent =
      p.rating.toFixed(1) + " out of 5 from " + countText + " on Google.";
    section.querySelector("[data-summary-stars]").appendChild(stars(p.rating));

    var grid = section.querySelector(".review-grid");
    list.forEach(function (r) {
      var card = el("figure", "review");
      var head = el("figcaption", "review-head");
      var who = r.authorAttribution || {};
      if (who.photoUri) {
        var img = el("img", "review-avatar");
        img.src = who.photoUri; img.alt = ""; img.width = 40; img.height = 40;
        img.loading = "lazy"; img.referrerPolicy = "no-referrer";
        head.appendChild(img);
      }
      var meta = el("div", "review-meta");
      var name = el(who.uri ? "a" : "span", "review-name", who.displayName || "Google user");
      if (who.uri) name.href = who.uri;
      meta.appendChild(name);
      var line = el("div", "review-line");
      line.appendChild(stars(r.rating || 0));
      if (r.relativePublishTimeDescription) line.appendChild(el("span", "review-when", r.relativePublishTimeDescription));
      meta.appendChild(line);
      head.appendChild(meta);
      card.appendChild(head);

      var body = el("blockquote", "review-text", r.text.text);
      card.appendChild(body);
      if (r.text.text.length > 320) {
        body.classList.add("clamped");
        var more = el("button", "review-more", "Read more");
        more.type = "button";
        more.addEventListener("click", function () {
          var open = body.classList.toggle("clamped") === false;
          more.textContent = open ? "Show less" : "Read more";
        });
        card.appendChild(more);
      }
      if (r.googleMapsUri) {
        var src = el("a", "review-source", "View on Google");
        src.href = r.googleMapsUri;
        card.appendChild(src);
      }
      grid.appendChild(card);
    });

    var all = section.querySelector("[data-all-reviews]");
    all.href = reviewsUri;
    all.textContent = "Read all " + countText + " on Google";
    var write = section.querySelector("[data-write]");
    write.href = links.writeAReviewUri || writeUrl;
    section.hidden = false;
  }
})();
