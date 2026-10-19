"""Service page content. Plain '&' in short/title/desc (escaped on output); HTML allowed in h1, lede, intro, included, faqs, extra.
{R} in HTML is replaced with the relative root path."""

SERVICES = [
    # ------------------------------------------------------------------ 01
    {
        "slug": "cooling-tower-water-treatment",
        "short": "Water treatment programmes",
        "icon": "programme",
        "code": "SVC 01",
        "service_type": "Cooling tower water treatment",
        "title": "Cooling Tower Water Treatment Programmes | UK",
        "desc": "Cooling tower and evaporative condenser water treatment programmes to ACOP L8 and HSG274 Part 1. Scale, corrosion and Legionella control, nationwide.",
        "h1": "Cooling tower &amp; evaporative condenser water treatment",
        "lede": "A treatment programme that keeps scale, corrosion, fouling and bacteria in check, written around your system and run by engineers who'll explain what the numbers mean.",
        "card": "A programme built around your plant: chemistry, dosing, bleed control, monitoring and visits, all set out in plain English.",
        "eyebrow": "The programme",
        "intro_h2": "Your tower is warm, wet and full of air. Bacteria love that.",
        "intro": [
            "A cooling tower or evaporative condenser works by evaporating water. That's brilliant for rejecting heat, but it concentrates everything in the water, scrubs dust and organic matter out of the air, and keeps the whole lot at a temperature bacteria are very happy in. Left alone, you get scale on the heat exchangers, corrosion in the pipework, slime on the fill and, worst of all, conditions where <em>Legionella</em> can grow and be carried out in the drift.",
            "A water treatment programme is how you keep a lid on all four. Under ACOP L8 and HSG274 Part 1, anyone in control of a wet cooling system needs one, and it needs to be monitored, recorded and reviewed. We set it up, supply and look after the dosing, visit on a fixed schedule and tell you straight away when something drifts out of range.",
            "Already got a contractor and not sure the programme's right? We're happy to review what you have. See also our <a href=\"{R}chemical-dosing-biocide-control.html\">dosing and biocide control</a> and <a href=\"{R}cooling-tower-monitoring-sampling.html\">monitoring</a> pages.",
        ],
        "included": [
            ("Water survey and system review", "We look at your make-up water, system volume, materials, heat load and how the plant actually runs before choosing any chemicals."),
            ("Scale and corrosion inhibitor", "Chosen to suit your water and metallurgy, with a target reserve we check on every visit."),
            ("Two-biocide regime", "Usually an oxidising biocide plus a non-oxidising one, alternated so bacteria don't get comfortable."),
            ("Bleed and conductivity control", "Set so the water is cycled up enough to save water without tipping into scaling."),
            ("Agreed visit schedule", "Weekly, fortnightly or monthly visits depending on your risk assessment and on-site resources."),
            ("Clear reporting", "A short report after every visit: what we tested, what we found, what we changed and what's next."),
        ],
        "extra": """
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">What we control</span>
          <h2>Four things a programme has to keep on top of</h2>
          <p>Get one wrong and the others usually follow. Scale shelters bacteria, corrosion products feed them, and fouling soaks up biocide before it can do its job.</p>
        </div>
        <div class="detail-grid">
          <div class="detail"><span class="detail__k">01 / Scale</span><h3>Hardness salts</h3><p>As water evaporates, calcium and magnesium salts concentrate and plate out on hot surfaces. Inhibitor and sensible bleed rates keep them in solution.</p></div>
          <div class="detail"><span class="detail__k">02 / Corrosion</span><h3>Metal loss</h3><p>Steel, copper and galvanised surfaces all corrode at different rates. The inhibitor package is matched to what your system is made of.</p></div>
          <div class="detail"><span class="detail__k">03 / Fouling</span><h3>Dirt and debris</h3><p>Towers scrub dust, pollen and leaves out of the air. Dispersants, filtration where fitted, and regular cleaning stop it settling.</p></div>
          <div class="detail"><span class="detail__k">04 / Microbiology</span><h3>Bacteria and biofilm</h3><p>Biocides keep the general bacterial count down and stop biofilm forming, which is where <em>Legionella</em> likes to live.</p></div>
          <div class="detail"><span class="detail__k">05 / Records</span><h3>Proof it's working</h3><p>Every check and result goes into your log book, so you can show an inspector the programme is doing its job.</p></div>
          <div class="detail"><span class="detail__k">06 / Review</span><h3>Adjusting as you go</h3><p>Seasons, heat loads and water quality change. We review the programme and tweak it rather than leaving it on autopilot.</p></div>
        </div>
      </div>
    </section>
""",
        "faqs": [
            ("Do we legally need a water treatment programme for our cooling tower?", "If you have a wet cooling tower or evaporative condenser, ACOP L8 expects you to have a written scheme for controlling the Legionella risk, and in practice that means a water treatment programme with monitoring and records. HSG274 Part 1 sets out what that programme should cover."),
            ("Do you treat evaporative condensers as well as cooling towers?", "Yes. Evaporative condensers (common on refrigeration and process cooling) carry the same kind of risk and need the same approach: treatment, monitoring, cleaning and records."),
            ("Can you take over from our existing contractor?", "Yes. We'll review your current programme, dosing kit and records first, so nothing gets lost in the handover. If the current setup is fine, we'll say so rather than changing things for the sake of it."),
            ("Will you supply the chemicals?", "Yes. We supply the treatment chemicals as part of the programme, along with safety data sheets and the information you need for your COSHH assessments."),
        ],
        "related": ["chemical-dosing-biocide-control", "cooling-tower-monitoring-sampling", "cooling-tower-legionella-risk-assessment"],
    },
    # ------------------------------------------------------------------ 02
    {
        "slug": "chemical-dosing-biocide-control",
        "short": "Chemical dosing & biocide control",
        "icon": "dosing",
        "code": "SVC 02",
        "service_type": "Cooling tower chemical dosing and biocide control",
        "title": "Cooling Tower Chemical Dosing & Biocide Control",
        "desc": "Cooling tower dosing equipment supplied, installed and maintained. Biocide control, inhibitor dosing and conductivity bleed control to HSG274 Part 1.",
        "h1": "Chemical dosing &amp; biocide control",
        "lede": "Dosing pumps, controllers, bleed valves and probes: supplied, set up and looked after, so the right amount of chemical goes in at the right time.",
        "card": "Dosing equipment supply and maintenance, biocide regimes and conductivity-controlled bleed that actually does what it says.",
        "eyebrow": "Dosing &amp; control",
        "intro_h2": "A great programme on paper is no use if the pump's stopped.",
        "intro": [
            "Most cooling tower problems we're asked to look at come down to dosing. A pump that's lost its prime. A suction lance sitting in an empty drum. A conductivity probe so coated it reads half what it should. A bleed valve stuck shut. None of it is dramatic, but any of it can let things slide quickly.",
            "We supply and install dosing equipment, set it up for your system, and maintain it on every visit. That includes the controller that decides when to bleed, the timers that run your biocide shots, and the probes that tell it what's going on.",
            "If you'd like to know what goes wrong most often, our engineers talk about it in the <a href=\"{R}blog/\">blog</a>, and the <a href=\"{R}cooling-tower-water-treatment.html\">treatment programme</a> page explains how dosing fits into the bigger picture.",
        ],
        "included": [
            ("Dosing equipment supply and installation", "Pumps, controllers, injection points, bunded chemical storage and pipework, sized for your system."),
            ("Conductivity and bleed control", "Probes and controllers that bleed off concentrated water at a set point, so you don't scale up or waste water."),
            ("Biocide dosing regimes", "Alternating oxidising and non-oxidising biocides on timers or proportional to make-up, with pre-bleed lockout where needed."),
            ("Inhibitor dosing", "Dosed in proportion to make-up water, so the reserve stays where it should be."),
            ("Routine equipment maintenance", "Pump checks, calibration of probes, cleaning of injection points and replacing worn parts."),
            ("Chemical stock checks", "We keep an eye on drum levels so you don't run dry between visits."),
        ],
        "faqs": [
            ("How do I know if my dosing system is working?", "Your weekly checks should include a quick look at drum levels, pump operation and the controller readout. Falling biocide or inhibitor reserves and rising dip slide counts are the usual warning signs. We check and calibrate the kit on every service visit."),
            ("Why use two different biocides?", "HSG274 Part 1 recognises that alternating biocides helps stop a bacterial population adapting to one chemical. A common approach is an oxidising biocide plus a non-oxidising one, but the right choice depends on your system and water."),
            ("What is bleed control and why does it matter?", "As water evaporates, dissolved solids build up. The controller measures conductivity and bleeds off some system water when it gets too high, replacing it with fresh make-up. Too little bleed and you get scale; too much and you waste water and chemicals."),
            ("Can you service dosing equipment another company installed?", "Usually, yes. We'll check what's fitted, confirm it's suitable and tell you honestly if anything needs replacing."),
        ],
        "related": ["cooling-tower-water-treatment", "cooling-tower-monitoring-sampling", "positive-legionella-result-response"],
    },
    # ------------------------------------------------------------------ 03
    {
        "slug": "cooling-tower-monitoring-sampling",
        "short": "Monitoring & Legionella sampling",
        "icon": "monitor",
        "code": "SVC 03",
        "service_type": "Cooling tower monitoring and Legionella sampling",
        "title": "Cooling Tower Monitoring & Legionella Sampling",
        "desc": "Weekly and monthly cooling tower checks, dip slides and TVCs, and quarterly Legionella sampling analysed by a UKAS-accredited lab. To HSG274 Part 1.",
        "h1": "Routine monitoring &amp; Legionella sampling",
        "lede": "Weekly and monthly checks, dip slides, chemistry testing and quarterly Legionella samples sent to a UKAS-accredited laboratory. The evidence that your programme is working.",
        "card": "Weekly and monthly checks, dip slides and TVCs, and quarterly Legionella samples analysed by a UKAS-accredited lab.",
        "eyebrow": "Monitoring",
        "intro_h2": "You can't control what you don't measure.",
        "intro": [
            "Monitoring is how you, and anyone inspecting you, know the treatment programme is actually working. HSG274 Part 1 sets out what should be checked and how often: microbiological activity at least weekly, chemistry on a regular cycle, and <em>Legionella</em> sampling at least quarterly.",
            "We can do all of it, or split it with your site team. Plenty of clients have their own engineers run the weekly dip slides while we handle the chemistry, the lab samples and the interpretation. Either way, every result goes in the <a href=\"{R}cooling-tower-log-books-compliance.html\">log book</a> and anything out of range gets a clear next step.",
            "Legionella samples go to a UKAS-accredited laboratory, and we explain the results in plain English when they come back. If a result is high, our <a href=\"{R}positive-legionella-result-response.html\">positive result response</a> service kicks in.",
        ],
        "included": [
            ("Dip slides and TVC testing", "Total viable counts to track general bacterial activity, read and recorded against HSG274 action levels."),
            ("Water chemistry testing", "Conductivity, pH, hardness, inhibitor and biocide reserves, checked against the targets in your programme."),
            ("Quarterly Legionella sampling", "Samples taken correctly, chilled and sent to a UKAS-accredited lab, with results explained when they arrive."),
            ("Visual inspection", "A look at the tower, pond, drift eliminators, fill and dosing kit on every visit."),
            ("Site team training", "If your engineers do the weekly checks, we'll show them how and give them simple record sheets."),
            ("Trend reporting", "Results tracked over time, so slow drifts get spotted before they become problems."),
        ],
        "extra": """
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Typical schedule</span>
          <h2>What gets checked, and how often</h2>
          <p>Your written scheme sets the actual frequencies, based on your risk assessment. This is the kind of baseline HSG274 Part 1 describes.</p>
        </div>
        <div class="table-wrap">
          <table>
            <thead><tr><th scope="col">Check</th><th scope="col">Typical frequency</th><th scope="col">What it tells you</th></tr></thead>
            <tbody>
              <tr><td>Dip slide / TVC</td><td><span class="tag tag--freq">At least weekly</span></td><td>General bacterial activity and whether the biocide regime is keeping up.</td></tr>
              <tr><td>Biocide and inhibitor reserve</td><td><span class="tag tag--freq">Weekly to monthly</span></td><td>Whether dosing is delivering what the programme needs.</td></tr>
              <tr><td>Conductivity, pH, hardness</td><td><span class="tag tag--freq">Weekly to monthly</span></td><td>How concentrated the water is and whether it's heading towards scaling or corrosion.</td></tr>
              <tr><td>Legionella sample (UKAS-accredited lab)</td><td><span class="tag tag--freq">At least quarterly</span></td><td>Direct check for <em>Legionella</em>. More often after a positive result or at commissioning.</td></tr>
              <tr><td>Cleaning and disinfection</td><td><span class="tag tag--freq">At least six-monthly</span></td><td>Removes the sludge, scale and biofilm that monitoring can't fix.</td></tr>
            </tbody>
          </table>
        </div>
        <p class="table-note">Frequencies are a guide. Your risk assessment may call for more, for example on a system with a history of high counts.</p>
      </div>
    </section>
""",
        "faqs": [
            ("How often should a cooling tower be tested for Legionella?", "HSG274 Part 1 says Legionella sampling should be carried out at least quarterly, and more often in some situations, such as when commissioning, after a positive result or when the system has been out of control."),
            ("What's the difference between a dip slide and a Legionella test?", "A dip slide measures the general bacterial count (TVC) and gives a result in a couple of days on site. A Legionella test is a lab analysis for <em>Legionella</em> specifically. You need both: dip slides weekly as an early warning, Legionella samples at least quarterly."),
            ("Can our own maintenance team do the weekly checks?", "Yes, as long as they're trained and the results are recorded properly. We can train your team and supply record sheets, then pick up the chemistry, lab sampling and interpretation ourselves."),
            ("Which lab do you use?", "Legionella samples are analysed by a UKAS-accredited laboratory, which is what HSG274 expects. The certificate is added to your records."),
        ],
        "related": ["positive-legionella-result-response", "cooling-tower-log-books-compliance", "cooling-tower-water-treatment"],
    },
    # ------------------------------------------------------------------ 04
    {
        "slug": "cooling-tower-cleaning-disinfection",
        "short": "Cleaning & disinfection",
        "icon": "clean",
        "code": "SVC 04",
        "service_type": "Cooling tower cleaning and disinfection",
        "title": "Cooling Tower Cleaning & Disinfection | HSG274",
        "desc": "Cooling tower and evaporative condenser cleaning and disinfection, at least six-monthly in line with HSG274 Part 1. Planned around your operations.",
        "h1": "Cooling tower cleaning &amp; disinfection",
        "lede": "A proper clean and disinfection at least every six months, as HSG274 Part 1 expects. Planned around your operations, with before-and-after records for the log book.",
        "card": "Six-monthly (or more frequent) clean and disinfection: pond, fill, drift eliminators, distribution and casing.",
        "eyebrow": "Cleaning",
        "intro_h2": "Chemistry can't shift what's already settled.",
        "intro": [
            "Even with a good treatment programme, towers collect sludge in the pond, scale on the fill and biofilm in the places water doesn't move much. That's why HSG274 Part 1 expects cooling towers to be cleaned and disinfected at least twice a year, and more often if your risk assessment says so or the system is particularly dirty.",
            "We follow the sequence the guidance describes: disinfect the water before anyone opens the tower up, so the clean itself doesn't throw contaminated spray around; then physically clean; then disinfect again before the system goes back into normal service.",
            "We plan the work with you, which matters a lot on sites where the cooling can't simply be switched off. Not sure how often your system really needs doing? Our article on <a href=\"{R}blog/how-often-should-a-cooling-tower-be-cleaned.html\">how often a cooling tower should be cleaned</a> covers it.",
        ],
        "included": [
            ("Pre-clean disinfection", "Online chlorination (or a suitable alternative) to cut the bacterial load before the tower is opened."),
            ("Drain down and physical clean", "Pond, sump, strainers, distribution, fill and drift eliminators cleaned and debris removed."),
            ("Inspection while it's open", "Condition of the fill, eliminators, casing, fan and pipework noted, with photos for your records."),
            ("Refill and post-clean disinfection", "The system is disinfected again, then flushed and brought back to normal treatment levels."),
            ("Resilient-site planning", "For sites that can't lose cooling, we plan around N+1 towers, cell-by-cell isolation or quieter periods."),
            ("Certificate and report", "A record of what was done, chemical levels, contact times and findings, ready for the log book."),
        ],
        "faqs": [
            ("How often does a cooling tower need cleaning?", "HSG274 Part 1 says cooling towers should be cleaned and disinfected at least twice a year. Your risk assessment may call for more frequent cleaning, for example in a dusty environment or if monitoring shows problems."),
            ("Can you clean one cell while the others keep running?", "Often, yes. On multi-cell towers or sites with standby units, we can isolate and clean one at a time. We'll look at the layout and plan the safest way to do it."),
            ("Do evaporative condensers need cleaning too?", "Yes. They need regular cleaning and disinfection as part of the written scheme. The frequency should come from your risk assessment, taking account of the guidance in HSG274 Part 1."),
            ("What happens if you find damage while the tower's open?", "We'll record it with photos and tell you what we've found and how urgent it is. Repairs or replacement parts are quoted separately, so there are no surprises."),
        ],
        "related": ["cooling-tower-shutdown-start-up-commissioning", "cooling-tower-water-treatment", "positive-legionella-result-response"],
    },
    # ------------------------------------------------------------------ 05
    {
        "slug": "cooling-tower-legionella-risk-assessment",
        "short": "Risk assessments & written schemes",
        "icon": "assessment",
        "code": "SVC 05",
        "service_type": "Legionella risk assessment for cooling systems",
        "title": "Cooling Tower Legionella Risk Assessment",
        "desc": "Legionella risk assessments and written control schemes for cooling towers and evaporative condensers, carried out to ACOP L8 and HSG274 Part 1.",
        "h1": "Legionella risk assessments &amp; written schemes for cooling systems",
        "lede": "A site-specific risk assessment of your evaporative cooling system, and a written scheme that sets out exactly how the risk is controlled, who does what and how often.",
        "card": "Site-specific Legionella risk assessments for evaporative cooling, plus a written scheme your team can actually follow.",
        "eyebrow": "Risk assessment",
        "intro_h2": "The document everything else hangs off.",
        "intro": [
            "ACOP L8 requires the dutyholder to identify and assess the risk from <em>Legionella</em>, and where there's a reasonably foreseeable risk, to prepare a written scheme for controlling it. With a cooling tower or evaporative condenser on site, there almost always is.",
            "Our assessors look at the whole system: the towers and condensers themselves, their location relative to air intakes, windows and the public, the make-up and bleed arrangements, dosing and controls, dead legs, management arrangements and records. Then we write it up in plain English with prioritised actions.",
            "The written scheme follows from it. It tells your team and your <a href=\"{R}cooling-tower-water-treatment.html\">treatment contractor</a> what needs doing to keep the system under control, how often, and what to do when results go out of range.",
        ],
        "included": [
            ("Site survey", "The cooling system, its surroundings, the plant room and the controls, inspected in person."),
            ("Management review", "Who's the responsible person, who's competent, what training is in place, and how records are kept."),
            ("Prioritised action plan", "Clear actions ranked by risk, so you know what to fix first."),
            ("Written scheme of control", "Monitoring, treatment, cleaning and inspection tasks, with frequencies and responsibilities."),
            ("Schematic drawing", "A simple diagram of the system, as ACOP L8 expects the written scheme to include."),
            ("Review whenever things change", "We'll review it if the plant, the use or the people change, or if monitoring suggests the controls aren't working."),
        ],
        "faqs": [
            ("How often should a cooling tower risk assessment be reviewed?", "ACOP L8 says the assessment should be reviewed regularly and whenever there's reason to think it's no longer valid: for example, changes to the plant or its use, changes in key personnel, a positive Legionella result or a case of Legionnaires' disease. Many sites review at least every two years as good practice, and more often for cooling systems."),
            ("Who is the 'responsible person'?", "Someone appointed by the dutyholder to take day-to-day responsibility for managing the Legionella risk. They need enough authority, competence and knowledge of the system to do the job. We can help you set out the roles in the written scheme."),
            ("Does the risk assessment cover the rest of the building's water?", "This service focuses on the evaporative cooling system. If you need hot and cold water systems assessed too, let us know and we'll quote for both."),
            ("What's the difference between the risk assessment and the written scheme?", "The risk assessment identifies and evaluates the risk. The written scheme is the practical plan for controlling it: what's done, by whom and how often."),
        ],
        "related": ["cooling-tower-log-books-compliance", "cooling-tower-water-treatment", "cooling-tower-monitoring-sampling"],
    },
    # ------------------------------------------------------------------ 06
    {
        "slug": "cooling-tower-log-books-compliance",
        "short": "Log books & compliance records",
        "icon": "logbook",
        "code": "SVC 06",
        "service_type": "Cooling tower log books and compliance records",
        "title": "Cooling Tower Log Books & Compliance Records",
        "desc": "Cooling tower log books and compliance records set up and kept current: monitoring results, lab certificates, cleaning records and notifications.",
        "h1": "Log books &amp; compliance records",
        "lede": "Every check, result, clean and action, recorded in one place and kept up to date. So when an inspector or insurer asks, you can show them in minutes.",
        "card": "Log books set up and kept current, with results, certificates, cleaning records and actions in one place.",
        "eyebrow": "Records",
        "intro_h2": "If it isn't written down, it didn't happen.",
        "intro": [
            "ACOP L8 expects the dutyholder to keep records of the risk assessment, the written scheme, and the results of monitoring, inspection, testing and checks. Monitoring records should be kept for at least five years. In practice, the log book is often the first thing an inspector asks to see.",
            "We set up a log book that's laid out logically, then update it on every visit: dip slide and chemistry results, lab certificates from the UKAS-accredited lab, cleaning and disinfection certificates, dosing equipment checks and any corrective actions with the date they were closed out.",
            "We'll also make sure your notification under the Notification of Cooling Towers and Evaporative Condensers Regulations 1992 is on file. More on that in our article on <a href=\"{R}blog/notifying-local-authority-cooling-tower.html\">notifying the local authority</a>.",
        ],
        "included": [
            ("Log book set-up", "A clear structure: contacts, risk assessment, written scheme, schematic, results, certificates and actions."),
            ("Updated every visit", "Our engineers record results and actions on site, so the book never falls behind."),
            ("Lab and cleaning certificates", "Legionella results and cleaning and disinfection records filed in date order."),
            ("Corrective action tracking", "Anything out of range is logged with what was done and when it was closed out."),
            ("Records audit", "Taking over a site? We'll review existing records and flag gaps before anyone else does."),
            ("Notification check", "We'll confirm your towers and condensers have been notified to the local authority."),
        ],
        "faqs": [
            ("How long do cooling tower records need to be kept?", "ACOP L8 says records of monitoring, inspection, testing and checks should be kept for at least five years. Records of the risk assessment and written scheme should be kept while they're current and for at least two years afterwards."),
            ("Can records be kept electronically?", "Yes. ACOP L8 doesn't insist on paper. What matters is that the records are complete, accurate, easy to find and can't be quietly altered later."),
            ("We've inherited a messy log book. Can you help?", "Yes, that's a common one. We'll audit what's there, tell you what's missing and set up a clean structure going forward."),
            ("Who should sign off the log book?", "Entries are made by whoever carried out the work. The responsible person should review the records regularly and make sure actions are closed out."),
        ],
        "related": ["cooling-tower-legionella-risk-assessment", "cooling-tower-monitoring-sampling", "cooling-tower-water-treatment"],
    },
    # ------------------------------------------------------------------ 07
    {
        "slug": "positive-legionella-result-response",
        "short": "Positive result response",
        "icon": "alert",
        "code": "SVC 07",
        "service_type": "Response to positive Legionella and high TVC results",
        "title": "Positive Legionella Result in a Cooling Tower? Act Now",
        "desc": "High TVC or positive Legionella result in your cooling tower? We help you review controls, disinfect, resample and record it, in line with HSG274 Part 1.",
        "h1": "Positive Legionella or high TVC result? Here's what happens next.",
        "lede": "A high count doesn't mean panic, but it does mean action. We'll help you work through it calmly: review, disinfect where needed, resample and record everything.",
        "card": "A clear plan when results come back high: review controls, disinfect if needed, resample, record.",
        "eyebrow": "Out-of-range results",
        "intro_h2": "Calm, quick and properly recorded.",
        "intro": [
            "HSG274 Part 1 sets action levels for both general bacteria (TVC) and <em>Legionella</em> in cooling water. Go over them and you're expected to do something: resample, review the control measures and risk assessment, and in some cases disinfect the system.",
            "Call us as soon as you get the result. We'll look at the recent history (dosing, dip slides, chemistry, recent shutdowns), get an engineer out to check the system and agree the right response with you. That might be a dosing fix and a resample, or it might be an online disinfection and a full clean.",
            "Every step gets recorded, including resample results, so your log book tells the whole story. If you'd like to read up first, our <a href=\"{R}cooling-tower-monitoring-sampling.html\">monitoring and sampling</a> page explains how results are taken and tested.",
        ],
        "included": [
            ("Rapid review of the data", "Recent dosing, chemistry and dip slide records checked to find the likely cause."),
            ("Site visit and system check", "Dosing kit, bleed, biocide reserve and the tower itself inspected."),
            ("Online disinfection", "Where the result calls for it, a controlled disinfection of the system."),
            ("Resampling", "Follow-up samples to the UKAS-accredited lab to confirm control has been restored."),
            ("Risk assessment review", "We'll check whether the risk assessment and written scheme need updating."),
            ("Full record of actions", "What was found, what was done and the follow-up results, filed in the log book."),
        ],
        "extra": """
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Action levels</span>
          <h2>What HSG274 Part 1 says about high results</h2>
          <p>A simplified summary for cooling systems. Your written scheme should set out the exact responses for your site, and the guidance itself has the full wording.</p>
        </div>
        <div class="table-wrap">
          <table>
            <thead><tr><th scope="col">Result</th><th scope="col">Status</th><th scope="col">Typical response</th></tr></thead>
            <tbody>
              <tr><td>TVC up to 10<sup>4</sup> cfu/ml</td><td><span class="tag tag--ok">Under control</span></td><td>Carry on with the programme and routine monitoring.</td></tr>
              <tr><td>TVC above 10<sup>4</sup>, up to 10<sup>5</sup> cfu/ml</td><td><span class="tag tag--warn">Review</span></td><td>Review the programme and dosing, and re-test to confirm the count.</td></tr>
              <tr><td>TVC above 10<sup>5</sup> cfu/ml</td><td><span class="tag tag--act">Act now</span></td><td>Take corrective action straight away, review the controls and re-test.</td></tr>
              <tr><td><em>Legionella</em> above 100, up to 1,000 cfu/litre</td><td><span class="tag tag--warn">Review</span></td><td>Resample. If the result repeats, or most samples are positive, review the controls and risk assessment and consider disinfection.</td></tr>
              <tr><td><em>Legionella</em> above 1,000 cfu/litre</td><td><span class="tag tag--act">Act now</span></td><td>Resample and immediately review the controls and risk assessment, with remedial action that may include disinfecting the system.</td></tr>
            </tbody>
          </table>
        </div>
        <p class="table-note">cfu = colony forming units. This table is a plain-English summary, not a replacement for HSG274 Part 1 or your written scheme.</p>
      </div>
    </section>
""",
        "faqs": [
            ("We've had a positive Legionella result. Do we have to shut the tower down?", "Not automatically. It depends on the count, the history and the risk. Many results are dealt with by resampling, reviewing controls and disinfecting online. In some situations shutting down or isolating is the right call. We'll help you make that decision quickly and record why."),
            ("Do we need to tell anyone about a positive result?", "A positive sample on its own isn't generally something you have to report, but you must act on it and record what you did. If there's a suspected case of Legionnaires' disease linked to your site, the local authority or UKHSA may get in touch and you'll need your records to hand."),
            ("How quickly can you resample?", "As soon as practical after any corrective action, timed so the result tells you something useful. Samples go to a UKAS-accredited lab."),
            ("Why did our count go up when nothing changed?", "Something usually did: a dosing pump losing prime, a biocide drum running out, warm weather, a period of low load, or debris building up. Finding the cause matters as much as fixing the result."),
        ],
        "related": ["cooling-tower-monitoring-sampling", "cooling-tower-cleaning-disinfection", "chemical-dosing-biocide-control"],
        "cta_title": "Got a high result back? Call us now.",
    },
    # ------------------------------------------------------------------ 08
    {
        "slug": "cooling-tower-shutdown-start-up-commissioning",
        "short": "Shutdown, start-up & commissioning",
        "icon": "power",
        "code": "SVC 08",
        "service_type": "Cooling tower shutdown, start-up and commissioning",
        "title": "Cooling Tower Shutdown, Start-Up & Commissioning",
        "desc": "Safe cooling tower shutdown, start-up after idle periods and commissioning of new systems, with cleaning, disinfection and treatment in line with HSG274.",
        "h1": "Shutdown, start-up &amp; commissioning",
        "lede": "Idle towers and new systems carry their own risks. We plan shutdowns properly, bring systems back safely and commission new plant so it starts life under control.",
        "card": "Safe shutdowns, start-up after idle periods and commissioning of new or refurbished cooling plant.",
        "eyebrow": "Shutdown &amp; start-up",
        "intro_h2": "Standing water is where the trouble starts.",
        "intro": [
            "A cooling tower that's sitting idle with water in it is a problem waiting to happen. With no circulation and no dosing, biocide levels fall away and bacteria get going. Then the day it's switched back on, it can throw the lot out as drift.",
            "For short idle periods the usual answer is to keep water circulating with treatment running. For longer shutdowns, the system is normally drained, cleaned and left dry, then cleaned and disinfected again before it comes back into service. Your risk assessment and written scheme should spell out which applies, and we'll help you follow it.",
            "New towers and refurbished systems need commissioning too. HSG274 Part 1 expects new systems to be cleaned and disinfected before they're put into use, with treatment and monitoring in place from day one. See our <a href=\"{R}cooling-tower-cleaning-disinfection.html\">cleaning and disinfection</a> page for how we go about it.",
        ],
        "included": [
            ("Planned shutdown", "Drain down or keep circulating, depending on how long it'll be idle and what your risk assessment says."),
            ("Start-up after idle periods", "Cleaning and disinfection where needed, refill, treatment established and checks before full load."),
            ("Commissioning of new plant", "Pre-commission clean and disinfection, dosing set up, baseline samples and records opened."),
            ("Seasonal systems", "Towers that only run in summer, planned around the start and end of the season."),
            ("Notification reminders", "New towers need notifying to the local authority; decommissioned ones need notifying too."),
            ("Records for the log book", "What was done, when, and the follow-up monitoring results."),
        ],
        "faqs": [
            ("How long can a cooling tower sit idle before it's a problem?", "There's no single safe number. Stagnant water quickly loses its biocide reserve, so even a few days without circulation can matter. Your written scheme should say what happens for short and long idle periods. If it doesn't, we'd recommend getting that added."),
            ("Do we need to disinfect before restarting?", "After an extended shutdown, HSG274 Part 1 expects the system to be cleaned and disinfected before it goes back into service. For short breaks with treatment maintained, a check of chemical levels and a dip slide may be enough. We'll advise based on your system."),
            ("We're installing a new tower. When should you get involved?", "As early as you can. We can advise on dosing points, sample points and access for cleaning before it's built, then commission it with a clean, disinfection and baseline sampling."),
            ("Does a new tower need notifying?", "Yes. The Notification of Cooling Towers and Evaporative Condensers Regulations 1992 require you to notify the local authority in writing. You also need to tell them if a notified tower or condenser is taken out of use for good."),
        ],
        "related": ["cooling-tower-cleaning-disinfection", "cooling-tower-legionella-risk-assessment", "cooling-tower-water-treatment"],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
