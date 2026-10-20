"""Homepage, services hub, sectors, FAQs, privacy and 404."""
import build as B
from services import SERVICES
from faqs import FAQ_GROUPS, GENERAL_FAQS, HOME_FAQS, SOURCES

esc = B.esc
TEL, PHONE, BRAND = B.TEL, B.PHONE, B.BRAND

SCHEMATIC = """<svg class="schematic" viewBox="0 0 520 360" role="img" aria-labelledby="sch-title">
  <title id="sch-title">Schematic of an induced-draught cooling tower showing the fan, drift eliminators, spray distribution, fill pack, pond, dosing and bleed, and the recirculating loop to the cooling load</title>
  <!-- airflow out of fan -->
  <path class="sch-flow" d="M232 30V8M260 30V4M288 30V8" />
  <!-- fan cowl -->
  <path class="sch-line" d="M206 62V40h108v22M216 40c0-8 10-12 44-12s44 4 44 12" />
  <path class="sch-line" d="M224 51h72M260 44v14" />
  <!-- casing -->
  <path class="sch-line" d="M150 62h220v228H150Z" />
  <!-- drift eliminators -->
  <path class="sch-line" d="M150 84h220" opacity=".5" />
  <path class="sch-line" d="M156 94l8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8 8-8 8 8" />
  <!-- spray header + nozzles -->
  <path class="sch-line" d="M160 112h200M190 112v6M230 112v6M270 112v6M310 112v6M340 112v6" />
  <path class="sch-spray" d="M190 122l-8 12M190 122v14M190 122l8 12M230 122l-8 12M230 122v14M230 122l8 12M270 122l-8 12M270 122v14M270 122l8 12M310 122l-8 12M310 122v14M310 122l8 12M340 122l-8 12M340 122v14M340 122l8 12" />
  <!-- fill pack -->
  <path class="sch-line" d="M160 146h200v70H160Z" />
  <path class="sch-line" d="M160 160l40 40M180 146l70 70M215 146l70 70M250 146l70 70M285 146l70 70M320 146l40 40M360 160l-40 40M340 146l-70 70M305 146l-70 70M270 146l-70 70M235 146l-70 70M200 146l-40 40" opacity=".35" />
  <!-- air inlet louvres -->
  <path class="sch-line" d="M150 232l-12 8M150 246l-12 8M150 260l-12 8M370 232l12 8M370 246l12 8M370 260l12 8" />
  <path class="sch-flow" d="M104 250h28M416 250h-28" />
  <!-- pond -->
  <path class="sch-water" d="M151 272h218v17H151Z" />
  <!-- recirculation: pond -> pump -> load -> spray header -->
  <path class="sch-line" d="M369 282h41v40h46" />
  <circle class="sch-line" cx="468" cy="322" r="12" />
  <path class="sch-line" d="M462 322l10-6v12Z" />
  <path class="sch-line" d="M480 322h20V230" />
  <path class="sch-line" d="M440 150h70v80h-70Z" />
  <path class="sch-line" d="M448 168h54M448 182h54M448 196h54M448 210h54" opacity=".45" />
  <path class="sch-line" d="M475 150v-38H360" />
  <path class="sch-flow" d="M410 300v16M490 300v-40M475 140v-20M430 112h-50" />
  <!-- make-up + dosing + bleed (left) -->
  <path class="sch-line" d="M40 278h110M40 300h22v-10h10" />
  <path class="sch-line" d="M60 196h34v44H60Z" />
  <path class="sch-line" d="M77 240v38" stroke-dasharray="3 3" />
  <path class="sch-line" d="M151 288h-20v22h-80" />
  <path class="sch-line" d="M100 304l8 6-8 6M108 304l-8 6 8 6" />
  <!-- labels -->
  <g class="sch-labels">
    <text x="300" y="18">AIR OUT</text>
    <text x="96" y="242">AIR IN</text>
    <text x="398" y="242">AIR IN</text>
    <text x="92" y="272">MAKE-UP</text>
    <text x="40" y="330">BLEED</text>
    <text x="56" y="188">DOSING</text>
    <text x="446" y="142">LOAD</text>
    <text x="372" y="130">WARM RETURN</text>
    <text x="380" y="276">COOLED FLOW</text>
  </g>
  <!-- tags + leaders -->
  <path class="sch-leader" d="M372 90h32" />
  <g class="sch-tags">
    <rect x="404" y="80" width="30" height="18" rx="2" /><text x="419" y="93">01</text>
    <rect x="114" y="104" width="30" height="18" rx="2" /><text x="129" y="117">02</text>
    <rect x="114" y="172" width="30" height="18" rx="2" /><text x="129" y="185">03</text>
    <rect x="245" y="296" width="30" height="18" rx="2" /><text x="260" y="309">04</text>
    <rect x="20" y="210" width="30" height="18" rx="2" /><text x="35" y="223">05</text>
    <rect x="378" y="324" width="30" height="18" rx="2" /><text x="393" y="337">06</text>
  </g>
  <path class="sch-leader" d="M144 113h40M144 181h16M260 296v-8M50 219h10M408 333h2v-14" />
</svg>"""

SECTORS = [
    ("datacentre", "Data centres", "Uptime matters more than anything, so treatment, cleaning and sampling are planned around redundancy and change control.",
     "Data halls run cooling around the clock, and nobody wants to explain an outage. We work within your change control process, plan cleans cell by cell or around N+1 capacity, and keep the paperwork tidy for audits. Treatment is set up to cope with high heat loads and the big swings that come with seasonal free-cooling."),
    ("hospital", "Hospitals and healthcare", "Vulnerable people nearby means less room for error. We support your Water Safety Group with clear records and quick escalation.",
     "Healthcare sites often have patients, staff and visitors close to cooling plant, and some of those people are at higher risk from <em>Legionella</em>. We fit into your Water Safety Group arrangements, report results promptly and keep records in a way that stands up to scrutiny."),
    ("factory", "Manufacturing and process", "Process cooling, evaporative condensers and plant that can't easily stop. We treat for the process as well as the Legionella risk.",
     "Process cooling brings its own quirks: contamination from the process, oil, high solids or unusual metallurgy. We design the programme around what's actually in the water and plan cleaning around production schedules."),
    ("food", "Food and drink processing", "Evaporative condensers on refrigeration plant are common here. We keep them clean and treated without disrupting cold chain.",
     "Refrigeration and chilling plant often relies on evaporative condensers that sit close to loading bays and staff areas. We look after treatment, cleaning and records with an eye on food safety audits and keeping the cold chain intact."),
    ("office", "Commercial buildings", "Offices, retail and mixed-use buildings with rooftop towers, often near air intakes, windows and busy streets.",
     "City-centre towers are often close to air intakes, neighbouring windows and the street below, which makes good control especially important. We work with building managers and FM teams to keep the tower, the records and the landlord happy."),
    ("contractor", "M&amp;E contractors and FM companies", "We work as your specialist water treatment partner, on your sites, to your reporting standards.",
     "If you manage plant across several sites, we can slot in as your cooling water specialist. Our engineers follow your site rules and permits, report in a format that suits you and flag issues early, so you can keep your client informed."),
    ("leisure", "Leisure, hotels and venues", "Large buildings with seasonal cooling loads and lots of people about.",
     "Hotels, venues and leisure buildings tend to run cooling hardest in summer, when the most people are around. We plan start-ups, cleans and sampling around the season and your event calendar."),
]

def services_grid(root):
    cards = "\n".join(
        f"""          <a class="service" href="{root}{s["slug"]}.html">
            <span class="service__top">{B.icon(s["icon"], root)}<span class="service__num">{s["code"].split()[1]}</span></span>
            <h3>{esc(s["short"])}</h3>
            <p>{s["card"]}</p>
            <span class="link-arrow">Find out more</span>
          </a>"""
        for s in SERVICES
    )
    return f'        <div class="services">\n{cards}\n        </div>'


REGS = """        <div class="regs">
          <div class="reg"><span class="reg__code">HSE · L8</span><h3>ACOP L8</h3><p>The Approved Code of Practice for controlling <em>Legionella</em> in water systems. It sets out the dutyholder's responsibilities: assess the risk, have a written scheme, appoint a responsible person, monitor and keep records.</p></div>
          <div class="reg"><span class="reg__code">HSE · HSG274 Pt 1</span><h3>HSG274 Part 1</h3><p>The technical guidance for evaporative cooling systems. It covers treatment, monitoring frequencies, action levels for TVC and <em>Legionella</em>, and how to decide how often to clean and disinfect. The second edition was published in 2024.</p></div>
          <div class="reg"><span class="reg__code">SI 1992/2225</span><h3>Notification Regulations 1992</h3><p>The Notification of Cooling Towers and Evaporative Condensers Regulations 1992 require you to tell your local authority, in writing, about wet cooling towers and evaporative condensers on your premises.</p></div>
        </div>"""


def build_home():
    root = ""
    latest = B.POSTS_SORTED[:3]
    sectors = "\n".join(
        f"""          <li class="sector">{B.icon(i, root)}<div><h3>{n}</h3><p>{short}</p></div></li>""" for i, n, short, _ in SECTORS[:6]
    )
    home_faqs = HOME_FAQS
    posts_html = ""
    if latest:
        posts_html = f"""
    <section class="section">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">From the blog</span>
            <h2>Latest advice</h2>
          </div>
          <p>Practical guidance on cooling tower compliance, written the way we'd explain it on site. <a class="link-arrow" href="blog/">All articles</a></p>
        </div>
{B.post_cards(latest, root)}
      </div>
    </section>
"""
    main = f"""    <section class="hero blueprint on-dark">
      <div class="wrap">
        <div>
          <span class="eyebrow">Cooling tower water treatment · Nationwide</span>
          <h1>Cooling tower water treatment, <span>done properly</span>.</h1>
          <p class="hero__lede">We look after cooling towers and evaporative condensers for facilities teams, data centres, hospitals and industry. Treatment, dosing, monitoring, cleaning and records, all to ACOP L8 and HSG274 Part 1, explained in plain English.</p>
          <div class="hero__actions">
            <button class="btn btn--primary" type="button" data-open-enquiry>Get a quote</button>
            <a class="btn btn--line" href="{TEL}">{B.icon("phone", root)}Call {PHONE}</a>
          </div>
          <ul class="hero__specs">
            <li><b>Guidance</b>ACOP L8</li>
            <li><b>Technical</b>HSG274 Part 1</li>
            <li><b>Samples</b>UKAS-accredited lab</li>
          </ul>
        </div>

        <figure class="drawing" style="margin:0">
          <div class="drawing__head"><span><b>DWG CTT-01</b> Induced-draught tower</span><span>Not to scale</span></div>
          {SCHEMATIC}
          <ul class="legend">
            <li><span>01</span>Fan &amp; drift eliminators</li>
            <li><span>02</span>Spray distribution</li>
            <li><span>03</span>Fill pack</li>
            <li><span>04</span>Pond &amp; strainers</li>
            <li><span>05</span>Dosing &amp; bleed control</li>
            <li><span>06</span>Sample point</li>
          </ul>
          <figcaption class="drawing__foot"><span>Every point we treat, test or clean</span><span>Rev. A</span></figcaption>
        </figure>
      </div>
    </section>
    <div class="scale" aria-hidden="true"></div>

    <section class="section section--white">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">The rules</span>
            <h2>Three documents your cooling tower lives by.</h2>
          </div>
          <p>If you're the dutyholder for a site with wet cooling, these are the ones that matter. We work to all three, and we'll happily walk you through what they mean for your site.</p>
        </div>
{REGS}
      </div>
    </section>

    <section class="section" id="services">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Services</span>
          <h2>Everything your cooling system needs, from one team.</h2>
          <p>Use us for the lot, or just the parts you need. Either way you get engineers who know evaporative cooling inside out and won't bury you in jargon.</p>
        </div>
{services_grid(root)}
      </div>
    </section>

    <section class="section blueprint blueprint--steel on-dark">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">What treatment controls</span>
          <h2>Four ways a cooling system goes wrong.</h2>
          <p>A good programme keeps all four in balance. They're connected, so fixing one while ignoring another rarely works for long.</p>
        </div>
        <ul class="factors">
          <li class="factor"><span class="factor__label"><span>01</span><span>Inhibitor + bleed</span></span><h3>Scale</h3><p>Hardness salts concentrate as water evaporates and coat the hottest surfaces, cutting efficiency and sheltering bacteria.</p></li>
          <li class="factor"><span class="factor__label"><span>02</span><span>Inhibitor</span></span><h3>Corrosion</h3><p>Pipework, heat exchangers and casings slowly eaten away. Corrosion products also feed bacterial growth.</p></li>
          <li class="factor"><span class="factor__label"><span>03</span><span>Dispersant + cleaning</span></span><h3>Fouling</h3><p>Dust, pollen and debris pulled in from the air settle in the pond and fill, soaking up biocide.</p></li>
          <li class="factor"><span class="factor__label"><span>04</span><span>Biocides</span></span><h3>Microbiology</h3><p>General bacteria, biofilm and <em>Legionella</em>. Kept down with a biocide regime and checked by dip slides and lab samples.</p></li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head section-head--split">
          <div>
            <span class="eyebrow">Sectors</span>
            <h2>Built for sites where cooling can't fail.</h2>
          </div>
          <p>Different buildings, different pressures. We plan the work around how your site actually runs. <a class="link-arrow" href="sectors.html">All sectors</a></p>
        </div>
        <ul class="sectors">
{sectors}
        </ul>
      </div>
    </section>

    <section class="section blueprint on-dark" id="process">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">How it works</span>
          <h2>From first call to a system that's under control.</h2>
          <p>No drawn-out onboarding. Here's what happens when you bring us in.</p>
        </div>
        <ol class="process">
          <li><h3>Talk it through</h3><p>A quick call about your plant, how it's used and what's worrying you. We'll ask for any existing records.</p></li>
          <li><h3>Site survey</h3><p>An engineer looks at the system, the dosing kit and the log book, and checks your risk assessment is current.</p></li>
          <li><h3>Programme and quote</h3><p>We set out the treatment, visit schedule and monitoring we recommend, with a clear, itemised price.</p></li>
          <li><h3>Set up</h3><p>Dosing commissioned, chemicals delivered, log book organised, and a clean and disinfection booked if it's due.</p></li>
          <li><h3>Routine visits</h3><p>Testing, sampling, adjustments and a short report every time. If something's off, you'll hear from us straight away.</p></li>
        </ol>
      </div>
    </section>

    <section class="section section--white">
      <div class="wrap split">
        <div>
          <span class="eyebrow">Working with us</span>
          <h2>What you can count on.</h2>
          <p class="lede">We're not going to promise you the moon. What we will do is turn up when we say, do the job properly, and tell you plainly what we've found.</p>
          <p class="lede">If you've ever had a treatment report that was just a page of numbers with no explanation, you'll notice the difference.</p>
          <div class="hero__actions"><button class="btn btn--primary" type="button" data-open-enquiry>Talk to us about your site</button></div>
        </div>
        <ul class="checklist">
          <li><div><h3>Results explained, not just emailed</h3><p>Every visit report says what we tested, what it means and what happens next.</p></div></li>
          <li><div><h3>Lab samples to a UKAS-accredited lab</h3><p><em>Legionella</em> samples are analysed by an accredited laboratory, with certificates for your file.</p></div></li>
          <li><div><h3>Log book kept current</h3><p>We update your records on every visit, so you're always ready for an inspection.</p></div></li>
          <li><div><h3>One team for the whole system</h3><p>Treatment, dosing, cleaning, risk assessments and records, without juggling contractors.</p></div></li>
          <li><div><h3>Straight answers when something's wrong</h3><p>A high count gets a phone call and a plan, not a line buried in a report.</p></div></li>
        </ul>
      </div>
    </section>
{posts_html}
    <section class="section section--white">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">FAQs</span>
          <h2>Quick answers</h2>
          <p>The questions we get asked most. There are more on our <a class="link-arrow" href="faqs.html">FAQs page</a></p>
        </div>
{B.faq_block(home_faqs)}
      </div>
    </section>

    <section class="section" id="contact">
      <div class="wrap local">
        <div>
          <span class="eyebrow">Coverage</span>
          <h2>West London roots, towers looked after up and down the country.</h2>
          <p>We're based in Chiswick, West London, and most of our work is in London and the surrounding counties. We also look after sites across the rest of the UK, so if you manage plant in several regions, one contractor can cover the lot.</p>
          <ul class="areas">
            <li>Central London</li><li>West London</li><li>City &amp; Docklands</li><li>Surrey</li><li>Berkshire</li><li>Hertfordshire</li><li>Buckinghamshire</li><li>Kent</li><li>Essex</li><li>Middlesex</li><li>Slough &amp; the M4 corridor</li><li>Nationwide</li>
          </ul>
        </div>
        <div class="contact-card">
          <h3>Talk to an engineer</h3>
          <dl>
            <div><dt>Phone</dt><dd><a class="big-phone" href="{TEL}">{PHONE}</a></dd></div>
            <div><dt>Office</dt><dd><address>The Lightbox G16, 111 Power Road<br />Chiswick, London W4 5PY</address></dd></div>
            <div><dt>Coverage</dt><dd>Nationwide, specialising in London &amp; the Home Counties</dd></div>
          </dl>
          <button class="btn btn--primary" type="button" data-open-enquiry>Request a quote</button>
        </div>
      </div>
    </section>

{B.cta_band(root)}"""
    B.page(
        "index.html",
        "Cooling Tower Water Treatment | London & Nationwide",
        "Cooling tower and evaporative condenser water treatment, dosing, Legionella sampling and cleaning to ACOP L8 and HSG274. London and nationwide.",
        "",
        main,
        "home",
        [B.business_ld(), {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": B.DOMAIN + "/"}, B.faq_ld(home_faqs)],
        root,
    )


def build_services_hub():
    root = ""
    crumbs = [("Home", ""), ("Services", None)]
    main = f"""{B.page_hero(crumbs, "Services", "Cooling tower services", "Water treatment, dosing, monitoring, cleaning, risk assessments and records for cooling towers and evaporative condensers. Pick what you need, or hand us the whole lot.", root, "tower", "SERVICES")}

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">What we do</span>
          <h2>Eight services, one joined-up approach.</h2>
          <p>Each one stands on its own, but they work best together. A treatment programme is only as good as the monitoring that proves it and the records that show it.</p>
        </div>
{services_grid(root)}
      </div>
    </section>

    <section class="section section--white">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">The rules</span>
          <h2>What the guidance expects</h2>
        </div>
{REGS}
      </div>
    </section>

{B.cta_band(root)}"""
    lds = [
        B.breadcrumb_ld([("Home", ""), ("Services", "services.html")]),
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": s["short"], "url": B.url_for(s["slug"] + ".html")} for i, s in enumerate(SERVICES)
            ],
        },
    ]
    B.page("services.html", "Cooling Tower Services | Treatment, Dosing & Cleaning", "Cooling tower and evaporative condenser services: treatment programmes, dosing, monitoring, Legionella sampling, cleaning, risk assessments and records.", "services.html", main, "services", lds, root)


def build_sectors():
    root = ""
    crumbs = [("Home", ""), ("Sectors", None)]
    items = "\n".join(
        f"""          <div class="detail">{B.icon(i, root, "icon")}<h3>{n}</h3><p>{long}</p></div>""" for i, n, _, long in SECTORS
    )
    main = f"""{B.page_hero(crumbs, "Sectors", "Cooling tower treatment for every kind of site", "From data halls to hospital plant rooms to food factories, the rules are the same but the pressures aren't. We plan around how your site actually works.", root, "datacentre", "SECTORS")}

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Who we work with</span>
          <h2>Sectors we serve</h2>
          <p>If you've got a wet cooling tower or an evaporative condenser, the same duties apply under ACOP L8. What changes is how much downtime you can live with, who's nearby and how your team likes to work.</p>
        </div>
        <div class="detail-grid sector-grid">
{items}
          <div class="detail"><span class="detail__k">Not listed?</span><h3>Tell us about your site</h3><p>Universities, transport hubs, laboratories, retail parks: if it has evaporative cooling, we can help. <button class="link-arrow" type="button" data-open-enquiry="Other sector">Ask us</button></p></div>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="wrap">
        <h2 class="block-title">Popular services</h2>
{B.related_services(["cooling-tower-water-treatment", "cooling-tower-cleaning-disinfection", "cooling-tower-monitoring-sampling", "cooling-tower-legionella-risk-assessment"], root)}
      </div>
    </section>

{B.cta_band(root)}"""
    B.page("sectors.html", "Sectors | Cooling Tower Treatment for Data Centres & More", "Cooling tower water treatment for data centres, hospitals, manufacturing, food processing, commercial buildings and M&E contractors across the UK.", "sectors.html", main, "sectors", [B.breadcrumb_ld([("Home", ""), ("Sectors", "sectors.html")])], root)


def build_faqs():
    root = ""
    crumbs = [("Home", ""), ("FAQs", None)]
    jump = "\n".join(f'          <li><a href="#{gid}">{esc(h)}</a></li>' for gid, h, _ in FAQ_GROUPS)
    groups = "\n".join(
        f"""        <section class="faq-group" id="{gid}" aria-labelledby="{gid}-h">
          <h2 id="{gid}-h">{esc(h)}</h2>
{B.faq_block(items)}
        </section>"""
        for gid, h, items in FAQ_GROUPS
    )
    sources = "\n".join(f'            <li><a href="{u}" rel="noopener">{esc(t)}</a></li>' for u, t in SOURCES)
    main = f"""{B.page_hero(crumbs, "FAQs", "Cooling tower water treatment FAQs", "Straight answers to the questions facilities managers and engineers ask us most about cooling towers, evaporative condensers and Legionella control, with links to the HSE guidance behind them.", root, "assessment", "FAQ")}

    <section class="section section--white">
      <div class="wrap faq-page">
        <p class="faq-reviewed">Last reviewed: October 2026, against ACOP L8 (2013) and HSG274 Part 1 (second edition, 2024).</p>
        <nav class="faq-jump" aria-label="FAQ topics">
          <ul>
{jump}
          </ul>
        </nav>
{groups}
        <section class="faq-sources" aria-labelledby="sources-h">
          <h2 id="sources-h">Sources and further reading</h2>
          <p>Our answers are a plain-English summary. The official documents are free to read online:</p>
          <ul>
{sources}
          </ul>
        </section>
        <p class="empty-note">Can't see your question? Call us on <a href="{TEL}">{PHONE}</a> or <button class="link-arrow" type="button" data-open-enquiry="Question">send us a message</button></p>
      </div>
    </section>

{B.cta_band(root)}"""
    lds = [B.breadcrumb_ld([("Home", ""), ("FAQs", "faqs.html")]), B.faq_ld(GENERAL_FAQS)]
    B.page("faqs.html", "Cooling Tower FAQs | Legionella, Cleaning & Compliance", "Cooling tower FAQs: Legionella testing, cleaning frequency, notification, action levels and records, with links to ACOP L8 and HSG274 Part 1.", "faqs.html", main, "faqs", lds, root)


def build_about():
    root = ""
    crumbs = [("Home", ""), ("About us", None)]
    main = f"""{B.page_hero(crumbs, "About", "About Cooling Tower Treatment", "A Chiswick-based team that looks after the water in cooling towers and evaporative condensers, and explains what it's doing in plain English.", root, "tower", "ABOUT", "General enquiry")}

    <section class="section section--white">
      <div class="wrap split">
        <div>
          <span class="eyebrow">Who we are</span>
          <h2>Specialists in one kind of plant.</h2>
          <p class="lede">We do one thing: keep evaporative cooling systems clean, treated and safe from <em>Legionella</em>, with records that stand up to an inspection.</p>
          <p class="lede">That covers treatment programmes, chemical dosing, monitoring and sampling, cleaning and disinfection, risk assessments, log books, and help when a result comes back high. You can hand us the lot or just the parts your own team doesn't cover.</p>
          <p class="lede">Our office is at The Lightbox in Chiswick, West London. Most of our work is in London and the Home Counties, and we look after sites across the rest of the UK too.</p>
        </div>
        <div>
          <ul class="checklist">
            <li><div><h3>Straight answers</h3><p>If your current setup is fine, we'll tell you. If it isn't, we'll explain why and what it'll take to fix.</p></div></li>
            <li><div><h3>Records you can rely on</h3><p>Every visit, sample, clean and corrective action is written up for your log book.</p></div></li>
            <li><div><h3>Accredited lab analysis</h3><p><em>Legionella</em> samples go to a UKAS-accredited laboratory.</p></div></li>
            <li><div><h3>Planned around your site</h3><p>Cleans and start-ups are planned with you, so cooling stays available where it has to.</p></div></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">The guidance we work to</span>
          <h2>What our work is based on</h2>
          <p>Everything we do is built around the HSE's Approved Code of Practice and technical guidance. You can read them yourself on the HSE website; our <a class="link-arrow" href="faqs.html">FAQs</a> explain the key points.</p>
        </div>
{REGS}
      </div>
    </section>

    <section class="section section--white">
      <div class="wrap local">
        <div>
          <span class="eyebrow">Get in touch</span>
          <h2>Talk to us about your system.</h2>
          <p>Call us, or send a few details through the quote form and we'll come back to you. Tell us what kind of system you have, roughly how big it is and what you need help with.</p>
          <p><a class="link-arrow" href="services.html">See all our services</a></p>
        </div>
        <div class="contact-card">
          <h3>{BRAND}</h3>
          <dl>
            <div><dt>Phone</dt><dd><a class="big-phone" href="{TEL}">{PHONE}</a></dd></div>
            <div><dt>Office</dt><dd><address>The Lightbox G16, 111 Power Road<br />Chiswick, London W4 5PY</address></dd></div>
            <div><dt>Coverage</dt><dd>Nationwide, specialising in London &amp; the Home Counties</dd></div>
          </dl>
          <button class="btn btn--primary" type="button" data-open-enquiry>Request a quote</button>
        </div>
      </div>
    </section>

{B.cta_band(root)}"""
    lds = [
        B.breadcrumb_ld([("Home", ""), ("About us", "about.html")]),
        {"@context": "https://schema.org", "@type": "AboutPage", "name": "About Cooling Tower Treatment", "url": B.url_for("about.html"), "about": {"@id": B.DOMAIN + "/#business"}},
    ]
    B.page("about.html", "About Us | Cooling Tower Treatment, Chiswick, London", "Who we are: cooling tower and evaporative condenser water treatment specialists based in Chiswick, West London, working nationwide to ACOP L8.", "about.html", main, "about", lds, root)


def build_privacy():
    root = ""
    crumbs = [("Home", ""), ("Privacy notice", None)]
    main = f"""{B.page_hero(crumbs, "Privacy", "Privacy notice", "How we use the information you send us through this website.", root, "logbook", "PRIVACY", "General enquiry")}

    <section class="section section--white">
      <div class="wrap">
        <div class="prose">
          <h2 class="block-title">Who we are</h2>
          <p>{BRAND}, The Lightbox G16, 111 Power Road, Chiswick, London W4 5PY. Telephone {PHONE}.</p>
          <h3>What we collect</h3>
          <p>When you use our enquiry form, we collect your name, email address, phone number, site postcode and the details you tell us about your site or system.</p>
          <h3>Why we use it</h3>
          <p>We use your details only to respond to your enquiry, prepare a quote and, if you go ahead, arrange and deliver the work. Our lawful basis is taking steps at your request before entering into a contract, and our legitimate interest in responding to enquiries. We don't sell your information or use it for unrelated marketing.</p>
          <h3>Where it's stored</h3>
          <p>Enquiries are passed securely through Cloudflare and stored in our customer records system, Airtable. These providers process data on our behalf under their own data protection terms.</p>
          <h3>How long we keep it</h3>
          <p>If you don't become a customer, we delete enquiry details within 24 months. Customer records are kept for as long as we need them to meet our legal, insurance and compliance obligations.</p>
          <h3 id="cookies">Cookies and similar technologies</h3>
          <p>We only use analytics and advertising cookies if you say yes. When they're switched on, we use Google Tag Manager to load Google Analytics, which helps us see how many people visit and which pages are useful, and Google Ads, which lets us measure whether our adverts lead to enquiries and show our ads to people who've visited this site before. If you click one of our Google adverts, the ad click reference and campaign details from the web address are added to your enquiry so we can tell which adverts work.</p>
          <p>If you say no, none of these are loaded and no analytics or advertising cookies are set. Your choice itself is saved in your browser's local storage so we don't ask again on every page. You can change your mind at any time using the <button class="link-arrow" type="button" data-cookie-settings>Cookie settings</button> link at the bottom of every page.</p>
          <p>Google's own explanation of how it uses information from sites like ours is at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com/technologies/partner-sites</a>. Fonts are loaded from Google Fonts, which means your browser connects to Google's servers when you view a page.</p>
          <h3>Your rights</h3>
          <p>You can ask to see, correct or delete the information we hold about you, or object to how we use it. Call us on {PHONE} or write to us at the address above. If you're unhappy with how we've handled your data, you can complain to the Information Commissioner's Office at ico.org.uk.</p>
        </div>
      </div>
    </section>"""
    B.page("privacy.html", "Privacy Notice | Cooling Tower Treatment", "How Cooling Tower Treatment uses the information you send through our website enquiry form, where it's stored and your data protection rights.", "privacy.html", main, "privacy", [B.breadcrumb_ld([("Home", ""), ("Privacy notice", "privacy.html")])], root)


def build_404():
    root = "/"
    main = f"""    <section class="notfound blueprint on-dark">
      <div class="wrap">
        <span class="eyebrow">Error 404 · Reading out of range</span>
        <h1>This page has gone down the drain.</h1>
        <p>The page you were after doesn't exist, or it's been moved. Try one of these instead, or give us a ring on {PHONE}.</p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="/">Back to the homepage</a>
          <a class="btn btn--line" href="/services.html">See our services</a>
        </div>
      </div>
    </section>
    <div class="scale" aria-hidden="true"></div>"""
    B.page("404.html", "Page not found | Cooling Tower Treatment", "Sorry, we couldn't find that page. Head back to the Cooling Tower Treatment homepage or browse our cooling tower services.", "404.html", main, "404", [], root, noindex=True)
