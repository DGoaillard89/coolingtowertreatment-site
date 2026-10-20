"""FAQ page content, grouped by topic. Used by pages.build_faqs (all groups) and the homepage (HOME_FAQS).

Rules: first sentence answers the question on its own. 40-120 words. Regulatory claims cite the source
with an ext() link. Every visible FAQ goes into FAQPage schema automatically (B.faq_ld).
Facts checked against L8 (4th edition, 2013) and HSG274 Part 1 (2nd edition, 2024) in October 2026.
"""

L8 = "https://www.hse.gov.uk/pubns/books/l8.htm"
HSG274 = "https://www.hse.gov.uk/pubns/books/hsg274.htm"
HSE_LEGIONELLA = "https://www.hse.gov.uk/legionnaires/"
HSE_COOLING = "https://www.hse.gov.uk/legionnaires/cooling-towers.htm"
NCTEC = "https://www.legislation.gov.uk/uksi/1992/2225/contents/made"
COSHH = "https://www.hse.gov.uk/coshh/"
HSWA = "https://www.legislation.gov.uk/ukpga/1974/37/contents"
RIDDOR = "https://www.hse.gov.uk/riddor/"
UKAS = "https://www.ukas.com/"


def ext(url, text):
    return f'<a href="{url}" rel="noopener">{text}</a>'


FAQ_GROUPS = [
    ("law", "The law and guidance", [
        ("Which laws and guidance apply to cooling towers?",
         f"Four main pieces. The {ext(HSWA, 'Health and Safety at Work etc. Act 1974')} and {ext(COSHH, 'COSHH')} set the general duty to control the risk from <em>Legionella</em>. {ext(L8, 'ACOP L8')} explains how to meet that duty, and {ext(HSG274, 'HSG274 Part 1')} gives the technical detail for evaporative cooling systems. On top of that, the {ext(NCTEC, 'Notification of Cooling Towers and Evaporative Condensers Regulations 1992')} say the local authority must know your tower exists."),
        ("What is ACOP L8?",
         f"{ext(L8, 'ACOP L8')} is the HSE's Approved Code of Practice for controlling <em>Legionella</em> bacteria in water systems. The current version is the fourth edition, published in 2013. It sets out what the dutyholder has to do: assess the risk, prepare a written scheme to control it, appoint a responsible person, put the controls in place, monitor them and keep records. Following it isn't compulsory, but if you don't, you'd need to show you've done something equally good."),
        ("What is HSG274 Part 1, and what changed in 2024?",
         f"{ext(HSG274, 'HSG274 Part 1')} is the HSE's technical guidance for controlling <em>Legionella</em> in evaporative cooling systems. It covers design, treatment, monitoring, action levels, cleaning and records. The second edition came out in 2024, and only Part 1 was updated. The biggest practical change is cleaning: instead of a fixed minimum, the frequency now comes from inspection and how quickly your system fouls. It also covers newer methods such as qPCR testing."),
        ("Do I need to notify the local authority about my cooling tower?",
         f"Yes. Under the {ext(NCTEC, 'Notification of Cooling Towers and Evaporative Condensers Regulations 1992')}, you must tell your local authority in writing about any wet cooling tower or evaporative condenser on your premises, and tell them again when one is taken out of use. Councils usually have a form for it. Our article on <a href=\"blog/notifying-local-authority-cooling-tower.html\">notifying the council</a> walks through it."),
        ("Do adiabatic or hybrid coolers need notifying?",
         f"Sometimes. The Regulations cover devices that cool water by direct contact with air, or cool a fluid through a heat exchanger wetted by water in an air stream. A truly dry cooler is outside that. Adiabatic and hybrid units sit in between: {ext(HSG274, 'HSG274 Part 1')} says to check them against the definitions, for example where water is sprayed directly onto the heat exchanger. Even if a unit isn't notifiable, any water spray still needs a risk assessment."),
        ("Who is the dutyholder, and who is the responsible person?",
         f"The dutyholder is the employer, or whoever is in control of the premises, and the legal duty sits with them. The responsible person is someone they appoint to manage the <em>Legionella</em> controls day to day. {ext(L8, 'ACOP L8')} says that person needs enough authority, competence and knowledge of the system. A contractor like us can do much of the work, but the dutyholder can't hand over the legal responsibility."),
        ("Is Legionnaires' disease reportable?",
         f"In some cases, yes. Doctors notify cases to public health authorities. Separately, under {ext(RIDDOR, 'RIDDOR')}, an employer must report a case of legionellosis to the HSE if a doctor tells them about it and the employee's job involves work on or near cooling systems or water systems at work that could be the source. A positive sample on its own isn't reportable, but you must act on it and record what you did."),
        ("Who enforces the rules on cooling towers?",
         f"Either the HSE or your local authority's environmental health team, depending on the type of premises. Factories, hospitals and similar sites usually fall to the HSE, while offices, shops, hotels and leisure venues usually fall to the council. Both can inspect your records and take action if controls aren't in place. The {ext(HSE_COOLING, 'HSE cooling towers page')} is a good starting point."),
    ]),
    ("testing", "Monitoring and testing", [
        ("How often should a cooling tower be tested for Legionella?",
         f"At least quarterly. {ext(HSG274, 'HSG274 Part 1')} says routine <em>Legionella</em> sampling should be done at least every three months, and more often in some situations: weekly at first when commissioning a system or starting a new treatment programme, after a positive result, or where the risk assessment calls for it because vulnerable people are nearby. See our <a href=\"cooling-tower-monitoring-sampling.html\">monitoring and sampling</a> service."),
        ("What are dip slides and how often should we do them?",
         f"Dip slides measure the general bacterial count in the water, and they should be done weekly. {ext(HSG274, 'HSG274 Part 1')} recommends weekly dip slides (or an equivalent test), ideally at the same time each week when the biocide level is at its lowest. They're not a <em>Legionella</em> test, but they're your early warning that the biocide regime is slipping. Our article on <a href=\"blog/dip-slides-tvc-cooling-tower.html\">reading dip slides and TVCs</a> explains more."),
        ("What do our TVC or dip slide results mean?",
         f"Up to 10,000 cfu/ml means good control. Between 10,000 and 100,000 cfu/ml, {ext(HSG274, 'HSG274 Part 1')} says to check the programme, adjust biocide if needed and resample after 24 hours. Above 100,000 cfu/ml, take corrective action: shot-dose or increase biocide, resample after 24 hours, and review the controls if it persists. Our <a href=\"positive-legionella-result-response.html\">positive result page</a> has the full table."),
        ("What Legionella count is a problem?",
         f"Anything above 100 cfu/litre needs action, and above 1,000 cfu/litre needs it immediately. Between 100 and 1,000, {ext(HSG274, 'HSG274 Part 1')} says to reassess the control programme, check treatment is working and resample. Above 1,000, or with persistent low-level positives, resample, shot-dose as a precaution, reassess the whole programme and resample again within 48 hours. A 'not detected' result doesn't mean there's no risk."),
        ("Does the laboratory need to be UKAS accredited?",
         f"For <em>Legionella</em> samples, yes, that's what the guidance expects. {ext(HSG274, 'HSG274 Part 1')} says <em>Legionella</em> samples should be tested by a laboratory accredited by {ext(UKAS, 'UKAS')} to ISO 17025, using the standard culture method. Our samples go to a UKAS-accredited lab and the certificate goes in your records. For general counts, the guidance says the lab must be competent, and accreditation is one way to show that."),
        ("What is qPCR testing, and should we use it?",
         f"qPCR is a rapid DNA-based test for <em>Legionella</em> that gives results in hours rather than days. {ext(HSG274, 'HSG274 Part 1')} sees it as useful for ruling out sources quickly in an outbreak, checking that cleaning and disinfection worked, and tracking trends alongside routine culture tests. It detects DNA from dead bacteria as well as live ones, so results need careful interpretation, and it doesn't replace quarterly culture samples."),
        ("What should be checked every week?",
         f"The physical condition of the system and a dip slide, as a minimum. {ext(HSG274, 'HSG274 Part 1')} also expects daily checks that the system is running normally and the water looks clean. Chemistry such as conductivity, pH, biocide and inhibitor levels is checked as your written scheme sets out, often weekly. Dosing pumps, drum levels and the controller should be checked too. Your team can do the routine checks if they're trained."),
    ]),
    ("cleaning", "Cleaning, shutdowns and start-up", [
        ("How often should a cooling tower be cleaned?",
         f"As often as inspection shows it's fouling. {ext(HSG274, 'HSG274 Part 1')} (2024) gives typical intervals of at least every three months for a tower in a dirty environment, at least twice a year for air conditioning comfort cooling, and at least every 12 months for a clean industrial system. Many sites clean six-monthly as a precaution. Your risk assessment sets the actual figure. More in our article on <a href=\"blog/how-often-should-a-cooling-tower-be-cleaned.html\">cleaning frequency</a>."),
        ("When does a tower need cleaning outside its normal schedule?",
         f"Whenever there's a significant change. {ext(HSG274, 'HSG274 Part 1')} says to inspect, disinfect and, if needed, clean a system before it's first commissioned, after a shutdown of a month or longer (or sooner if the risk assessment says so, especially in summer, and after as little as five days in healthcare premises), and after any physical alteration such as new pumps, pipework or heat exchangers. Contamination from construction or a process leak is another trigger."),
        ("What does a proper clean and disinfection involve?",
         "Disinfect, clean, disinfect again. The water is disinfected first so opening the tower doesn't spray contaminated water around. Then the system is drained and the pond, strainers, distribution, fill and drift eliminators are physically cleaned. It's refilled, disinfected again, flushed and brought back to normal treatment levels. Everything goes on a certificate for the log book. See our <a href=\"cooling-tower-cleaning-disinfection.html\">cleaning and disinfection</a> service."),
        ("Our tower will be out of use for a while. What should we do?",
         f"It depends how long. {ext(HSG274, 'HSG274 Part 1')} says that if a system will be idle for a week or more, up to about a month, biocide should still be dosed and circulated through the whole system at least weekly. Beyond a month, it should be drained and shut down, then recommissioned before it's used again. Your written scheme should spell this out. See <a href=\"cooling-tower-shutdown-start-up-commissioning.html\">shutdown and start-up</a>."),
        ("Why do drift eliminators matter so much?",
         f"Because they're the last line of defence against spray leaving the tower. Drift eliminators catch the fine droplets carried out by the air stream, and those droplets are how <em>Legionella</em> reaches people. {ext(HSG274, 'HSG274 Part 1')} says towers with fans should have them, and they need particular attention during maintenance. Gaps, damage or scale let more drift out, so we check them every time a tower is opened up."),
    ]),
    ("records", "Risk assessment and records", [
        ("How often should the risk assessment be reviewed?",
         f"Regularly, and whenever there's reason to think it's no longer valid. {ext(L8, 'ACOP L8')} lists triggers such as changes to the system or how it's used, new information about risks, checks showing controls aren't working, changes to key staff, and a case of Legionnaires' disease linked to the system. The assessment should record when the next review is due. See our <a href=\"cooling-tower-legionella-risk-assessment.html\">risk assessment</a> service."),
        ("How long do cooling tower records need to be kept?",
         f"At least five years for monitoring and inspection records. {ext(L8, 'ACOP L8')} and {ext(HSG274, 'HSG274 Part 1')} say other records, such as the risk assessment and written scheme, should be kept while they're current and for at least two years afterwards. Electronic records are fine as long as they're complete, easy to find and can't be quietly changed later."),
        ("What should be in a cooling tower log book?",
         "Everything that proves your controls are working: the risk assessment and written scheme, the names of the people responsible, weekly checks and dip slides, chemistry results, <em>Legionella</em> certificates, cleaning certificates, service reports, and every corrective action with what was done and when. Our article on <a href=\"blog/cooling-tower-log-book.html\">what goes in a log book</a> has a full checklist, and our <a href=\"cooling-tower-log-books-compliance.html\">log book service</a> can set it up for you."),
        ("What's the difference between a risk assessment and a written scheme?",
         "The risk assessment works out where the risk is and how serious it is. The written scheme is the practical plan for controlling it: what gets done, by whom, how often, and what happens when a result goes out of range. You need both, and they should agree with each other. An inspector will usually compare the scheme against your records first."),
    ]),
    ("results", "Positive results", [
        ("Do we have to shut the tower down after a positive Legionella result?",
         f"Not automatically. It depends on the count, the history and who's nearby. Many results are dealt with by resampling, reviewing controls and shot-dosing or disinfecting online. Sometimes shutting down or isolating is the right call. {ext(HSG274, 'HSG274 Part 1')} sets out the responses by count. Our <a href=\"positive-legionella-result-response.html\">positive result response</a> page explains how we help you decide quickly and record why."),
        ("Why did our count go up when nothing changed?",
         "Something usually did. Common causes are a dosing pump losing prime, a biocide drum running empty, a stuck bleed valve, warm weather, a spell of low load, or debris building up after nearby building work. Finding the cause matters as much as bringing the count down, otherwise it comes back. Our article on <a href=\"blog/cooling-tower-dosing-failures.html\">spotting dosing failures</a> covers the warning signs."),
    ]),
    ("us", "Working with us", [
        ("What does a cooling tower water treatment contractor actually do?",
         "We design and run the treatment programme, supply and look after the dosing equipment, do the monitoring and sampling, clean and disinfect the system, and keep the records in order. Put simply, we do the technical work that helps you meet your duties under ACOP L8 and HSG274 Part 1, and we explain what we're doing in plain English."),
        ("Do you cover evaporative condensers as well as cooling towers?",
         "Yes. Evaporative condensers, which are common on refrigeration and process cooling, carry a similar risk and need the same approach: treatment, monitoring, cleaning, risk assessment and records. They often hold less water than a tower, so chemistry can change quickly. Our article on <a href=\"blog/cooling-tower-vs-evaporative-condenser.html\">towers versus evaporative condensers</a> explains the differences."),
        ("Can you work alongside our in-house maintenance team?",
         "Yes. Lots of sites split the work, with their own team doing the daily and weekly checks while we handle the programme, chemistry, lab sampling, cleaning and records. We'll train your team and give them clear record sheets, so everyone knows who does what."),
        ("Can you take over from our current water treatment company?",
         "Yes. We start by reviewing your programme, dosing equipment, risk assessment and log book so nothing gets missed, then agree a handover date. If the current setup is fine, we'll say so rather than changing things for the sake of it. Our <a href=\"blog/cooling-tower-handover-checklist.html\">handover checklist</a> shows what we look at."),
        ("Where do you work?",
         "Nationwide. We're based in Chiswick, West London, and specialise in London and the Home Counties, but we look after sites across the UK too, which suits clients with plant in several regions."),
        ("How much does cooling tower water treatment cost?",
         "It depends on the size and number of systems, how often we visit and what's included. We'll look at your site and give you a clear, itemised quote with no obligation. Call us or use the quote form and tell us a bit about your system."),
    ]),
]

GENERAL_FAQS = [qa for _, _, items in FAQ_GROUPS for qa in items]
_BY_Q = {q: (q, a) for q, a in GENERAL_FAQS}
HOME_FAQS = [_BY_Q[q] for q in [
    "Which laws and guidance apply to cooling towers?",
    "Do I need to notify the local authority about my cooling tower?",
    "How often should a cooling tower be cleaned?",
    "How often should a cooling tower be tested for Legionella?",
    "What Legionella count is a problem?",
]]

SOURCES = [
    (L8, "Legionnaires' disease. The control of legionella bacteria in water systems. Approved Code of Practice and guidance (L8), fourth edition, HSE, 2013"),
    (HSG274, "Legionnaires' disease: Technical guidance, HSG274 Part 1: The control of legionella bacteria in evaporative cooling systems, second edition, HSE, 2024"),
    (HSE_LEGIONELLA, "HSE: Legionnaires' disease guidance hub"),
    (HSE_COOLING, "HSE: Cooling towers and evaporative condensers"),
    (NCTEC, "The Notification of Cooling Towers and Evaporative Condensers Regulations 1992 (SI 1992/2225)"),
    (HSWA, "Health and Safety at Work etc. Act 1974"),
    (COSHH, "HSE: Control of Substances Hazardous to Health (COSHH)"),
    (RIDDOR, "HSE: Reporting of Injuries, Diseases and Dangerous Occurrences Regulations 2013 (RIDDOR)"),
    (UKAS, "United Kingdom Accreditation Service (UKAS)"),
]
