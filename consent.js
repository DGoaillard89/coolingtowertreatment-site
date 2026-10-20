// ---------------------------------------------------------------------------
// Cookie consent, Google Tag Manager and conversion events.
//
// GTM_ID: paste the marketing agency's container ID here, e.g. "GTM-ABC1234".
// While it's empty, nothing loads, no banner shows and no cookies are set.
//
// "Basic" Google Consent Mode v2: GTM is only loaded after the visitor accepts.
// Defaults are all denied; the choice is kept in localStorage "cookie_consent".
//
// dataLayer events (pushed whether or not GTM is loaded, harmless if not):
//   generate_lead  { enquiry_type, form_id, page_path }   - enquiry.js, on success
//   phone_click    { link_location }                       - any tel: link
//   enquiry_open   { topic }                               - enquiry dialog opened
// Ad attribution (gclid, gbraid, wbraid, utm_*) is read from the landing URL and
// appended to the enquiry message as a "How they found us" line.
// ---------------------------------------------------------------------------
const GTM_ID = "";

(() => {
  const KEY = "cookie_consent";
  const ATTR_KEY = "ad_attrib";
  const ATTR_PARAMS = ["gclid", "gbraid", "wbraid", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"];
  const root = document.body.dataset.root || "";

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  gtag("consent", "default", {
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    analytics_storage: "denied",
    functionality_storage: "granted",
    security_storage: "granted",
    wait_for_update: 500,
  });

  // ---- stored choice
  function readChoice() {
    try {
      const c = JSON.parse(localStorage.getItem(KEY));
      return c && c.v === 1 ? c : null;
    } catch {
      return null;
    }
  }
  function saveChoice(analytics, ads) {
    const c = { v: 1, analytics, ads, ts: new Date().toISOString() };
    try {
      localStorage.setItem(KEY, JSON.stringify(c));
    } catch {}
    return c;
  }

  // ---- attribution: kept in memory, saved to sessionStorage only with consent
  let attrib = {};
  try {
    attrib = JSON.parse(sessionStorage.getItem(ATTR_KEY)) || {};
  } catch {}
  const params = new URLSearchParams(location.search);
  const fresh = {};
  ATTR_PARAMS.forEach((k) => {
    const v = params.get(k);
    if (v) fresh[k] = v.slice(0, 200);
  });
  if (Object.keys(fresh).length) attrib = fresh;
  function persistAttrib(choice) {
    if (!choice || !(choice.analytics || choice.ads) || !Object.keys(attrib).length) return;
    try {
      sessionStorage.setItem(ATTR_KEY, JSON.stringify(attrib));
    } catch {}
  }

  // ---- GTM
  let gtmLoaded = false;
  function applyChoice(c) {
    gtag("consent", "update", {
      ad_storage: c.ads ? "granted" : "denied",
      ad_user_data: c.ads ? "granted" : "denied",
      ad_personalization: c.ads ? "granted" : "denied",
      analytics_storage: c.analytics ? "granted" : "denied",
    });
    persistAttrib(c);
    if (!GTM_ID || gtmLoaded || !(c.analytics || c.ads)) return;
    gtmLoaded = true;
    window.dataLayer.push({ "gtm.start": Date.now(), event: "gtm.js" });
    const s = document.createElement("script");
    s.async = true;
    s.src = `https://www.googletagmanager.com/gtm.js?id=${encodeURIComponent(GTM_ID)}`;
    document.head.appendChild(s);
  }

  // ---- public helpers for enquiry.js
  window.siteTrack = {
    event(name, data = {}) {
      window.dataLayer.push({ event: name, ...data });
    },
    attributionNote() {
      const keys = ATTR_PARAMS.filter((k) => attrib[k]);
      return keys.length ? `\n\n--\nHow they found us: ${keys.map((k) => `${k}=${attrib[k]}`).join(", ")}` : "";
    },
  };

  // ---- phone clicks
  document.addEventListener("click", (e) => {
    const a = e.target.closest('a[href^="tel:"]');
    if (!a) return;
    let where = "body";
    if (a.closest(".mobile-bar")) where = "mobile_bar";
    else if (a.closest(".site-header")) where = "header";
    else if (a.closest(".site-footer")) where = "footer";
    else if (a.closest(".page-hero, .hero")) where = "hero";
    window.siteTrack.event("phone_click", { link_location: where });
  });

  // ---- banner
  const settingsBtns = document.querySelectorAll("[data-cookie-settings]");
  if (!GTM_ID) return; // nothing to consent to yet
  settingsBtns.forEach((b) => (b.hidden = false));

  const saved = readChoice();
  if (saved) applyChoice(saved);

  let banner;
  function build() {
    document.body.insertAdjacentHTML(
      "beforeend",
      `<div class="cookie-banner" role="dialog" aria-modal="false" aria-labelledby="cookie-title" aria-describedby="cookie-text" hidden>
        <div class="cookie-banner__inner">
          <h2 id="cookie-title">Cookies on this site</h2>
          <p id="cookie-text">We'd like to use Google Analytics and Google Ads cookies to see how the site is used and to show our ads to people who've visited. They're off unless you say yes. <a href="${root}privacy.html#cookies">More about cookies</a></p>
          <div class="cookie-banner__choose" hidden>
            <label class="cookie-toggle"><input type="checkbox" name="analytics" /> <span><b>Analytics</b> Counting visits and seeing which pages help.</span></label>
            <label class="cookie-toggle"><input type="checkbox" name="ads" /> <span><b>Advertising</b> Measuring our Google Ads and showing them to past visitors.</span></label>
          </div>
          <div class="cookie-banner__actions">
            <button class="btn btn--primary" type="button" data-cookie="accept">Accept all</button>
            <button class="btn btn--primary" type="button" data-cookie="reject">Reject all</button>
            <button class="btn btn--line" type="button" data-cookie="choose" aria-expanded="false">Choose</button>
            <button class="btn btn--line" type="button" data-cookie="save" hidden>Save choices</button>
          </div>
        </div>
      </div>`
    );
    banner = document.body.lastElementChild;
    const choose = banner.querySelector(".cookie-banner__choose");
    const chooseBtn = banner.querySelector('[data-cookie="choose"]');
    const saveBtn = banner.querySelector('[data-cookie="save"]');
    banner.addEventListener("click", (e) => {
      const act = e.target.closest("[data-cookie]")?.dataset.cookie;
      if (!act) return;
      if (act === "choose") {
        const open = choose.hidden;
        choose.hidden = !open;
        saveBtn.hidden = !open;
        chooseBtn.setAttribute("aria-expanded", String(open));
        if (open) choose.querySelector("input").focus();
        return;
      }
      let c;
      if (act === "accept") c = saveChoice(true, true);
      if (act === "reject") c = saveChoice(false, false);
      if (act === "save") c = saveChoice(choose.querySelector('[name="analytics"]').checked, choose.querySelector('[name="ads"]').checked);
      applyChoice(c);
      hide();
    });
    banner.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && readChoice()) hide();
    });
  }
  let returnTo = null;
  function show(e) {
    if (!banner) build();
    const c = readChoice();
    banner.querySelector('[name="analytics"]').checked = !!c?.analytics;
    banner.querySelector('[name="ads"]').checked = !!c?.ads;
    banner.hidden = false;
    document.body.classList.add("has-cookie-banner");
    if (e) {
      returnTo = e.currentTarget;
      banner.querySelector("button").focus({ preventScroll: true });
    }
  }
  function hide() {
    banner.hidden = true;
    document.body.classList.remove("has-cookie-banner");
    returnTo?.focus();
    returnTo = null;
  }

  settingsBtns.forEach((b) => b.addEventListener("click", show));
  if (!saved) show();
})();
