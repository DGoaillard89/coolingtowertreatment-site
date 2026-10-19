#!/usr/bin/env python3
"""Generates the static HTML for coolingtowertreatment.co.uk.

Run from anywhere:  python3 _tools/build.py
Edit content in services.py / posts.py / this file, then re-run. Never hand-edit the output HTML.
"""
import datetime
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from services import SERVICES, SERVICE_BY_SLUG  # noqa: E402
from posts import POSTS  # noqa: E402

DOMAIN = "https://coolingtowertreatment.co.uk"
BRAND = "Cooling Tower Treatment"
PHONE = "020 3633 6064"
TEL = "tel:+442036336064"
TODAY = datetime.date.today().isoformat()
OG_IMAGE = DOMAIN + "/assets/og-image.png"
LOGO_PNG = DOMAIN + "/assets/logo.png"
AREAS = ["London", "Home Counties", "United Kingdom"]

POSTS_SORTED = sorted(POSTS, key=lambda p: p["date"], reverse=True)
POST_BY_SLUG = {p["slug"]: p for p in POSTS}

LOGO_SVG = (
    '<svg viewBox="0 0 40 44">'
    '<path class="logo__body" fill-rule="evenodd" d="M8 3h24c-4.5 9.5-4.5 17.5 2 28H6c6.5-10.5 6.5-18.5 2-28ZM18.4 27.5V18.6H14L20 10.8l6 7.8h-4.4v8.9Z" />'
    '<path class="logo__base" d="M3 36c2.8 0 2.8-2 5.7-2s2.8 2 5.7 2 2.8-2 5.6-2 2.9 2 5.7 2 2.8-2 5.7-2 2.8 2 5.6 2M3 41.2h34" />'
    "</svg>"
)

ADDRESS_LD = {
    "@type": "PostalAddress",
    "streetAddress": "The Lightbox G16, 111 Power Road",
    "addressLocality": "Chiswick, London",
    "postalCode": "W4 5PY",
    "addressCountry": "GB",
}


def esc(s):
    return html.escape(s, quote=True)


def url_for(path):
    return f"{DOMAIN}/{path}"


def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def icon(name, root, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="{root}assets/icons.svg#{name}" /></svg>'


def home_href(root):
    return root if root else "./"


# ---------------------------------------------------------------- schema
def org_ld():
    return {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/", "logo": {"@type": "ImageObject", "url": LOGO_PNG, "width": 512, "height": 512}}


def business_ld():
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": DOMAIN + "/#business",
        "name": BRAND,
        "url": DOMAIN + "/",
        "logo": LOGO_PNG,
        "image": OG_IMAGE,
        "telephone": "+44 20 3633 6064",
        "address": ADDRESS_LD,
        "geo": {"@type": "GeoCoordinates", "latitude": 51.4935, "longitude": -0.2760},
        "areaServed": AREAS,
        "priceRange": "Quoted per site",
        "description": "Cooling tower and evaporative condenser water treatment: treatment programmes, chemical dosing, monitoring and Legionella sampling, cleaning and disinfection, risk assessments and compliance records.",
        "knowsAbout": ["ACOP L8", "HSG274 Part 1", "Legionella control", "Cooling tower water treatment", "Evaporative condensers"],
    }


def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url_for(path)} for i, (name, path) in enumerate(items)
        ],
    }


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs
        ],
    }


# ---------------------------------------------------------------- chrome
def head(title, desc, path, lds, root, og_type="website", noindex=False):
    if len(title) > 60:
        print(f"  !! title too long ({len(title)}): {title}")
    if len(desc) > 155:
        print(f"  !! description too long ({len(desc)}): {desc}")
    url = url_for(path)
    ld_html = "\n".join(
        f'  <script type="application/ld+json">\n{json.dumps(ld, indent=2, ensure_ascii=False)}\n  </script>' for ld in lds
    )
    robots = '  <meta name="robots" content="noindex" />\n' if noindex else ""
    canonical = "" if noindex else f'  <link rel="canonical" href="{url}" />\n'
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
{robots}{canonical}  <meta property="og:site_name" content="{BRAND}" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{OG_IMAGE}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Cooling Tower Treatment: water treatment and Legionella control for cooling towers" />
  <meta property="og:locale" content="en_GB" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(title)}" />
  <meta name="twitter:description" content="{esc(desc)}" />
  <meta name="twitter:image" content="{OG_IMAGE}" />
  <meta name="theme-color" content="#0b1a2a" />
  <link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml" />
  <link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..800&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{root}styles.css" />
{ld_html}
</head>"""


NAV = [
    ("services", "Services", "services.html"),
    ("sectors", "Sectors", "sectors.html"),
    ("process", "How it works", "index.html#process"),
    ("faqs", "FAQs", "faqs.html"),
    ("blog", "Blog", "blog/"),
]


def header(root):
    links = "\n".join(f'        <a href="{root}{href}" data-nav="{key}">{label}</a>' for key, label, href in NAV)
    return f"""  <a class="skip" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="wrap">
      <a class="logo" href="{home_href(root)}" aria-label="{BRAND} home">
        <span class="logo__mark" aria-hidden="true">{LOGO_SVG}</span>
        <span class="logo__text"><span class="logo__name">Cooling Tower</span><span class="logo__sub">Treatment</span></span>
      </a>

      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">
        <svg class="icon" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" /></svg>
      </button>

      <nav class="nav" id="site-nav" aria-label="Main">
{links}
      </nav>

      <div class="header-cta">
        <a class="header-phone" href="{TEL}" aria-label="Call {PHONE}">
          {icon("phone", root)}
          <span>{PHONE}</span>
        </a>
        <button class="btn btn--primary" type="button" data-open-enquiry>Get a quote</button>
      </div>
    </div>
  </header>"""


def footer(root):
    svc = "\n".join(f'            <li><a href="{root}{s["slug"]}.html">{esc(s["short"])}</a></li>' for s in SERVICES)
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <a class="logo" href="{home_href(root)}" aria-label="{BRAND} home">
            <span class="logo__mark" aria-hidden="true">{LOGO_SVG}</span>
            <span class="logo__text"><span class="logo__name">Cooling Tower</span><span class="logo__sub">Treatment</span></span>
          </a>
          <p class="footer-blurb">Water treatment and Legionella control for cooling towers and evaporative condensers. Working nationwide, specialising in London and the Home Counties.</p>
          <a class="footer-phone" href="{TEL}">{PHONE}</a>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
{svc}
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="{root}services.html">All services</a></li>
            <li><a href="{root}sectors.html">Sectors we work in</a></li>
            <li><a href="{root}index.html#process">How it works</a></li>
            <li><a href="{root}faqs.html">FAQs</a></li>
            <li><a href="{root}blog/">Blog</a></li>
            <li><a href="{root}privacy.html">Privacy notice</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <address>
            {BRAND}<br />
            The Lightbox G16<br />
            111 Power Road<br />
            Chiswick, London W4 5PY
          </address>
          <p style="margin-top:14px"><a href="{TEL}"><strong>{PHONE}</strong></a></p>
          <p style="margin-top:14px"><button class="link-arrow" type="button" data-open-enquiry>Request a quote</button></p>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year>{datetime.date.today().year}</span> {BRAND}. All rights reserved.</span>
        <span>Nationwide · Specialising in London &amp; the Home Counties</span>
      </div>
    </div>
  </footer>"""


def page(out_path, title, desc, canonical_path, main, page_key, lds, root="", og_type="website", noindex=False):
    doc = f"""{head(title, desc, canonical_path, lds, root, og_type, noindex)}
<body data-page="{page_key}" data-root="{root}">
{header(root)}

  <main id="main">
{main}
  </main>

{footer(root)}

  <script src="{root}script.js" defer></script>
  <script src="{root}enquiry.js" defer></script>
</body>
</html>
"""
    full = os.path.join(SITE, out_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(doc)
    return out_path


# ---------------------------------------------------------------- shared blocks
def cta_band(root, title="Need a treatment contractor who explains things properly?", text=None, topic=""):
    text = text or "Tell us about your system and we'll come back with a clear, itemised quote. No hard sell, just a straight answer on what your site needs."
    t = f' data-open-enquiry="{esc(topic)}"' if topic else " data-open-enquiry"
    return f"""    <section class="cta-band blueprint on-dark">
      <div class="wrap">
        <div>
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <div class="hero__actions">
          <button class="btn btn--primary" type="button"{t}>Get a quote</button>
          <a class="btn btn--line" href="{TEL}">Call {PHONE}</a>
        </div>
      </div>
    </section>"""


def faq_block(faqs):
    items = "\n".join(
        f"""          <details>
            <summary>{esc(q)}</summary>
            {a if a.startswith("<p>") else "<p>" + a + "</p>"}
          </details>"""
        for q, a in faqs
    )
    return f'        <div class="faq">\n{items}\n        </div>'


def post_cards(posts, root, heading_level="h3"):
    cls = "posts" if len(posts) >= 3 else "posts posts--list"
    cards = "\n".join(
        f"""          <li><a class="post-card" href="{root}blog/{p["slug"]}.html">
            <span class="post-card__meta"><b>{esc(p["tag"])}</b><time datetime="{p["date"]}">{fmt_date(p["date"])}</time></span>
            <{heading_level}>{esc(p["title"])}</{heading_level}>
            <p>{esc(p["desc"])}</p>
            <span class="link-arrow">Read article</span>
          </a></li>"""
        for p in posts
    )
    return f'        <ul class="{cls}">\n{cards}\n        </ul>'


def related_services(slugs, root):
    links = "\n".join(
        f'          <a href="{root}{s}.html">{icon(SERVICE_BY_SLUG[s]["icon"], root)}{esc(SERVICE_BY_SLUG[s]["short"])}</a>' for s in slugs
    )
    return f'        <div class="related">\n{links}\n        </div>'


def page_hero(crumbs, eyebrow, h1, lede, root, plate_icon=None, plate_label="", topic="", extra=""):
    crumb_html = "".join(
        f'<li><a href="{root}{path}">{esc(name)}</a></li>' if path is not None else f'<li aria-current="page">{esc(name)}</li>'
        for name, path in crumbs
    )
    t = f' data-open-enquiry="{esc(topic)}"' if topic else " data-open-enquiry"
    plate = (
        f'<div class="page-hero__plate" aria-hidden="true">{icon(plate_icon, root)}<span>{plate_label}</span></div>' if plate_icon else ""
    )
    return f"""    <section class="page-hero blueprint on-dark">
      <div class="wrap">
        <div>
          <nav aria-label="Breadcrumb"><ol class="crumbs">{crumb_html}</ol></nav>
          <h1>{h1}</h1>
          <p>{lede}</p>
{extra}          <div class="hero__actions">
            <button class="btn btn--primary" type="button"{t}>Get a quote</button>
            <a class="btn btn--line" href="{TEL}">Call {PHONE}</a>
          </div>
        </div>
        {plate}
      </div>
    </section>
    <div class="scale" aria-hidden="true"></div>"""


def related_posts_for_service(slug):
    return [p for p in POSTS_SORTED if slug in p["services"]][:3]


# ---------------------------------------------------------------- pages


def build_service(s):
    root = ""
    crumbs = [("Home", ""), ("Services", "services.html"), (s["short"], None)]
    included = "\n".join(
        f"""            <li><div><h3>{h}</h3><p>{p}</p></div></li>""" for h, p in s["included"]
    )
    intro = "\n".join(f'          <p class="lede">{p}</p>' for p in s["intro"])
    rel_posts = related_posts_for_service(s["slug"])
    posts_html = ""
    if rel_posts:
        posts_html = f"""        <h2 class="block-title" style="margin-top:48px">Related articles</h2>
{post_cards(rel_posts, root)}
"""
    extra = s.get("extra", "").replace("{R}", root)
    main = f"""{page_hero(crumbs, s["code"], s["h1"], s["lede"], root, s["icon"], s["code"], s["short"])}

    <section class="section section--white">
      <div class="wrap split">
        <div>
          <span class="eyebrow">{s["eyebrow"]}</span>
          <h2>{s["intro_h2"]}</h2>
{intro.replace("{R}", root)}
        </div>
        <div>
          <ul class="checklist">
{included}
          </ul>
        </div>
      </div>
    </section>
{extra}
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Questions</span>
          <h2>{esc(s["short"])}: common questions</h2>
        </div>
{faq_block(s["faqs"])}
      </div>
    </section>

    <section class="section section--white">
      <div class="wrap">
        <h2 class="block-title">Related services</h2>
{related_services(s["related"], root)}
{posts_html}      </div>
    </section>

{cta_band(root, s.get("cta_title", "Want a second pair of eyes on your cooling system?"), topic=s["short"])}"""
    service_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": s["short"],
        "serviceType": s["service_type"],
        "description": s["desc"],
        "url": url_for(s["slug"] + ".html"),
        "areaServed": AREAS,
        "provider": {"@type": "ProfessionalService", "@id": DOMAIN + "/#business", "name": BRAND, "telephone": "+44 20 3633 6064", "address": ADDRESS_LD, "url": DOMAIN + "/"},
    }
    lds = [service_ld, breadcrumb_ld([("Home", ""), ("Services", "services.html"), (s["short"], s["slug"] + ".html")]), faq_ld(s["faqs"])]
    return page(f'{s["slug"]}.html', s["title"], s["desc"], s["slug"] + ".html", main, "services", lds, root)


def word_count(body):
    return len(strip_tags(body).split())


def build_post(p):
    root = "../"
    body = p["body"].replace("{R}", root)
    words = word_count(body)
    mins = max(3, round(words / 200))
    path = f'blog/{p["slug"]}.html'
    crumbs = [("Home", ""), ("Blog", "blog/"), (p["title"], None)]
    meta = f"""          <ul class="post-meta">
            <li><b>Published</b><time datetime="{p["date"]}">{fmt_date(p["date"])}</time></li>
            <li><b>Reading time</b>{mins} min</li>
            <li><b>By</b>{BRAND}</li>
          </ul>
"""
    aside_links = "\n".join(
        f'            <li><a href="{root}{s}.html">{icon(SERVICE_BY_SLUG[s]["icon"], root)}{esc(SERVICE_BY_SLUG[s]["short"])}</a></li>' for s in p["services"]
    )
    others = [q for q in POSTS_SORTED if q["slug"] != p["slug"]]
    others.sort(key=lambda q: (len(set(q["services"]) & set(p["services"])), q["date"]), reverse=True)
    others = others[:3]
    rel_html = ""
    if others:
        rel_html = f"""
    <section class="section">
      <div class="wrap">
        <h2 class="block-title">Related articles</h2>
{post_cards(others, root)}
      </div>
    </section>
"""
    main = f"""{page_hero(crumbs, p["tag"], esc(p["title"]), esc(p["desc"]), root, topic=p["topic"], extra=meta)}

    <section class="section section--white">
      <div class="wrap article-layout">
        <article class="article">
{body}
          <div class="article-cta">
            <h2>{p.get("cta_title", "Want us to take a look at your system?")}</h2>
            <p>{p.get("cta_text", "Tell us a bit about your cooling towers or evaporative condensers and we'll come back with honest advice and a clear quote.")}</p>
            <div class="hero__actions">
              <button class="btn btn--primary" type="button" data-open-enquiry="{esc(p["topic"])}">Get a quote</button>
              <a class="btn btn--line" href="{TEL}">Call {PHONE}</a>
            </div>
          </div>
        </article>
        <aside class="aside-box" aria-labelledby="aside-title">
          <h2 id="aside-title">Related services</h2>
          <ul>
{aside_links}
          </ul>
          <div class="aside-phone">Questions about your own system? Call <a href="{TEL}">{PHONE}</a>
            <button class="btn btn--dark" type="button" data-open-enquiry="{esc(p["topic"])}">Ask us a question</button>
          </div>
        </aside>
      </div>
    </section>
{rel_html}
{cta_band(root, topic=p["topic"])}"""
    ld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p["title"],
        "description": p["desc"],
        "datePublished": p["date"],
        "dateModified": p.get("modified", p["date"]),
        "author": org_ld(),
        "publisher": org_ld(),
        "image": {"@type": "ImageObject", "url": OG_IMAGE, "width": 1200, "height": 630},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url_for(path)},
        "url": url_for(path),
        "inLanguage": "en-GB",
        "wordCount": words,
    }
    lds = [ld, breadcrumb_ld([("Home", ""), ("Blog", "blog/"), (p["title"], path)])]
    page(path, p["seo_title"], p["desc"], path, main, "blog", lds, root, og_type="article")
    return path, words


def build_blog_index():
    root = "../"
    crumbs = [("Home", ""), ("Blog", None)]
    main = f"""{page_hero(crumbs, "Blog", "Cooling tower advice from the people who treat them", "Practical, plain-English guidance on keeping cooling towers and evaporative condensers safe, compliant and running well. Written by our team, for the people who look after the plant.", root, "logbook", "ADVICE", "Blog enquiry")}

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Latest articles</span>
          <h2>Newest first</h2>
        </div>
{post_cards(POSTS_SORTED, root, "h2")}
      </div>
    </section>

{cta_band(root, "Got a question we haven't covered yet?", "Give us a ring or drop us a line through the form. We're happy to talk through a dip slide result, a dosing problem or a looming inspection.")}"""
    lds = [
        {
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": f"{BRAND} blog",
            "url": url_for("blog/"),
            "publisher": org_ld(),
            "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": url_for(f'blog/{p["slug"]}.html'), "datePublished": p["date"]} for p in POSTS_SORTED],
        },
        breadcrumb_ld([("Home", ""), ("Blog", "blog/")]),
    ]
    page("blog/index.html", "Cooling Tower Water Treatment Blog | Advice & Guidance", "Practical advice on cooling tower water treatment, Legionella control, cleaning, dosing and compliance from the Cooling Tower Treatment team.", "blog/", main, "blog", lds, root)


def build_sitemap(entries):
    rows = "\n".join(f"  <url><loc>{url_for(p)}</loc><lastmod>{d}</lastmod></url>" for p, d in entries)
    with open(os.path.join(SITE, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n')
    with open(os.path.join(SITE, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")


def main():
    from pages import build_home, build_services_hub, build_sectors, build_faqs, build_privacy, build_404

    entries = [("", TODAY)]
    build_home()
    build_services_hub()
    entries.append(("services.html", TODAY))
    for s in SERVICES:
        build_service(s)
        entries.append((s["slug"] + ".html", TODAY))
    build_sectors()
    entries.append(("sectors.html", TODAY))
    build_faqs()
    entries.append(("faqs.html", TODAY))
    build_privacy()
    entries.append(("privacy.html", TODAY))
    build_404()
    build_blog_index()
    entries.append(("blog/", POSTS_SORTED[0]["date"] if POSTS_SORTED else TODAY))
    for p in POSTS_SORTED:
        path, words = build_post(p)
        entries.append((path, p.get("modified", p["date"])))
        print(f"  post {p['date']} {words:>5} words  {p['slug']}")
    build_sitemap(entries)
    print(f"Built {len(entries)} indexable pages + 404.")


if __name__ == "__main__":
    main()
