"""Blog posts. Only posts listed here get published, linked or put in the sitemap.

Keys: slug, title (H1/headline), seo_title (<=60 chars), date (YYYY-MM-DD), desc (<=155 chars),
tag (short category), topic (pre-fills the enquiry form), services (related service slugs), body (HTML).
{R} in body is replaced with "../" (relative root from /blog/).
Planned posts 3-12 are listed in _build-notes.md.
"""

POSTS = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "how-often-should-a-cooling-tower-be-cleaned",
        "title": "How often should a cooling tower be cleaned and disinfected?",
        "seo_title": "How Often Should a Cooling Tower Be Cleaned? | HSG274",
        "date": "2023-11-14",
        "desc": "HSG274 Part 1 says at least twice a year, but some towers need more. What the guidance expects, how a clean works and the signs yours is overdue.",
        "tag": "Cleaning",
        "topic": "Cooling tower cleaning and disinfection",
        "services": ["cooling-tower-cleaning-disinfection", "cooling-tower-monitoring-sampling", "cooling-tower-shutdown-start-up-commissioning"],
        "body": """
          <p>It's one of the first questions we get asked when we take on a new site, usually followed by "and when was ours last done?" The short answer is <strong>at least twice a year</strong>. The longer answer is that some towers need it more often, and a clean done badly can do more harm than good.</p>
          <p>November's a good time to think about it. The leaves are down, the summer's heat load is behind you, and plenty of towers are sitting on six months' worth of whatever the air has thrown at them. Here's what the guidance says, what a proper clean involves and how to tell if yours is overdue.</p>

          <h2>What the guidance actually says</h2>
          <p>The technical guidance for evaporative cooling is HSG274 Part 1, which sits alongside the Approved Code of Practice, ACOP L8. HSG274 Part 1 says cooling towers should be cleaned and disinfected <strong>at least twice a year</strong>. That's a minimum, not a target.</p>
          <p>Your own frequency should come from your <a href="{R}cooling-tower-legionella-risk-assessment.html">Legionella risk assessment</a> and be written into your written scheme. If the assessment says your tower needs cleaning every four months, that's what you're expected to do, and an inspector will check your records against it.</p>
          <p>For evaporative condensers, the frequency should also be set by the risk assessment, taking account of the guidance. They're often smaller and more enclosed than open towers, but they still collect sludge and biofilm, and they still produce aerosol.</p>

          <h2>Why chemistry alone isn't enough</h2>
          <p>A good treatment programme does a lot of heavy lifting. Inhibitors keep scale in solution, dispersants stop dirt settling, and biocides keep the bacterial count down. But no chemical programme removes what has already settled out.</p>
          <p>Cooling towers are very good air scrubbers. Over a few months they pull in dust, pollen, insects, leaves and whatever's blowing off the building site next door. That ends up as sludge in the pond and deposits on the fill. Biofilm builds up in the corners where water moves slowly. All of it soaks up biocide and gives bacteria, including <em>Legionella</em>, somewhere to hide. Physical cleaning is the only way to get it out.</p>

          <h2>What a proper clean and disinfection involves</h2>
          <p>HSG274 Part 1 describes a sequence, and the order matters:</p>
          <ol>
            <li><strong>Pre-clean disinfection.</strong> Before anyone opens the tower up, the water is disinfected, usually by chlorinating the system and holding a set level for a set contact time. This cuts the bacterial load so the cleaning itself doesn't spray contaminated water around.</li>
            <li><strong>Drain down and physical clean.</strong> The pond and sump are emptied and cleaned out. Strainers, distribution troughs or spray nozzles, fill and drift eliminators are cleaned, and debris is removed rather than washed into the drain.</li>
            <li><strong>Inspection.</strong> While it's open, it's the best chance you'll get to look at the condition of the fill, eliminators, casing and fan. Damaged eliminators, for example, let more drift escape.</li>
            <li><strong>Post-clean disinfection.</strong> The system is refilled and disinfected again, then flushed and brought back to normal treatment levels before going back into routine service.</li>
            <li><strong>Records.</strong> What was done, chemical levels and contact times, and what was found all go in the log book.</li>
          </ol>
          <p>A quick hose-down of the pond doesn't count. Neither does skipping the pre-clean disinfection to save a few hours. If the person doing the work isn't following that sequence, it's worth asking why.</p>

          <h2>When twice a year isn't enough</h2>
          <p>Plenty of towers need cleaning more often than the minimum. Your risk assessment should consider things like:</p>
          <ul>
            <li><strong>Dirty surroundings.</strong> Nearby construction, demolition, busy roads, trees or industrial processes all increase the amount of debris the tower pulls in.</li>
            <li><strong>Process contamination.</strong> Food, oil or other process leaks into the cooling water feed bacteria and foul the system fast.</li>
            <li><strong>Monitoring trends.</strong> If dip slide counts keep creeping up between cleans, or biocide demand keeps rising, the system's telling you something.</li>
            <li><strong>History.</strong> A system that's had positive <em>Legionella</em> results before deserves closer attention.</li>
            <li><strong>Who's nearby.</strong> Towers close to hospitals, care homes, air intakes or busy public areas carry a higher consequence if things go wrong.</li>
          </ul>

          <h2>Signs your tower is overdue</h2>
          <p>You don't need to be a water treatment engineer to spot most of these during a walk-round:</p>
          <ul>
            <li>Visible sludge or debris in the pond</li>
            <li>Slime or algae on the fill, eliminators or the inside of the casing</li>
            <li>White or brown scale on wetted surfaces</li>
            <li>Dip slide results drifting upwards over several weeks</li>
            <li>Biocide or inhibitor reserves dropping faster than usual</li>
            <li>A cleaning certificate in the log book that's more than six months old</li>
          </ul>
          <p>Any one of these is worth a conversation with whoever looks after your treatment. A few together usually means a clean is due now, not at the next scheduled date.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine an office building with a rooftop tower that's cleaned every spring and autumn like clockwork. Then a large construction project starts across the road. Within weeks the pond is visibly dirtier and dip slide counts are climbing. The right move is to review the risk assessment, bring the next clean forward and increase the cleaning frequency for as long as the dust keeps coming.</p>
          </div>

          <h2>Planning a clean on a site that can't switch off</h2>
          <p>The most common reason cleans slip is that the cooling can't easily be turned off. Data centres, hospitals and process sites all have this problem. It's solvable, though:</p>
          <ul>
            <li>Multi-cell towers can often be cleaned one cell at a time with the others carrying the load.</li>
            <li>Sites with N+1 redundancy can take one tower out while the standby runs.</li>
            <li>Spring and autumn cleans can be timed for lower heat loads, when there's more spare capacity.</li>
          </ul>
          <p>It just needs planning early, rather than squeezing it in when the certificate's already out of date. Our <a href="{R}cooling-tower-cleaning-disinfection.html">cleaning and disinfection</a> page explains how we approach this, and if a tower has been sitting idle, take a look at our notes on <a href="{R}cooling-tower-shutdown-start-up-commissioning.html">shutdown and start-up</a> too.</p>

          <h2>The bottom line</h2>
          <p>At least twice a year is the floor. Your risk assessment sets the real frequency, your <a href="{R}cooling-tower-monitoring-sampling.html">monitoring results</a> tell you whether it's working, and your records prove it was done. If you can't remember when your tower was last cleaned, or you're not sure the job's being done properly, that's the moment to get someone to take a look.</p>
""",
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "notifying-local-authority-cooling-tower",
        "title": "Do you need to notify the council about your cooling tower?",
        "seo_title": "Cooling Tower Notification: Telling Your Local Authority",
        "date": "2024-02-20",
        "desc": "The Notification of Cooling Towers and Evaporative Condensers Regulations 1992 explained: who notifies, what to send and when to update it.",
        "tag": "Compliance",
        "topic": "Cooling tower notification and compliance records",
        "services": ["cooling-tower-log-books-compliance", "cooling-tower-legionella-risk-assessment", "cooling-tower-shutdown-start-up-commissioning"],
        "body": """
          <p>Here's a compliance task that's easy to miss because it only comes up once in a blue moon. If you have a wet cooling tower or an evaporative condenser on your premises, the law says your local authority needs to know about it. In writing.</p>
          <p>It's a short form, it doesn't cost you much time, and it matters more than people think. We often find it's missing when we audit a site's records, usually because the tower was notified years ago by someone who's long since left, or never notified at all. Here's what you need to know.</p>

          <h2>The regulations in a nutshell</h2>
          <p>The rule comes from the <strong>Notification of Cooling Towers and Evaporative Condensers Regulations 1992</strong>. They apply to non-domestic premises and say that the person in control of the premises must notify the local authority, in writing, of any cooling towers and evaporative condensers on site.</p>
          <p>You notify the local authority for the area where the premises are, even if your site is one where the Health and Safety Executive, rather than the council, is the enforcing authority for health and safety. Most councils have a standard form on their website, often in the environmental health section.</p>
          <p>There's a narrow exception for a device that contains no water exposed to air and whose water and electricity supplies aren't connected. In plain terms, a tower that's been properly decommissioned and disconnected. If it's connected and could be run, it counts.</p>

          <h2>Why the council wants to know</h2>
          <p>This isn't paperwork for its own sake. When there's an outbreak of Legionnaires' disease, one of the first things investigators do is look for wet cooling systems in the area, because towers can spread contaminated drift over a surprising distance. The register built from these notifications lets environmental health officers find every tower nearby quickly, check records and take samples.</p>
          <p>If your tower isn't on that list, it can't be ruled in or out quickly, and the first contact you get from the council might be during an investigation. Not a great time to discover the paperwork was never sent.</p>

          <h2>What you'll usually need to provide</h2>
          <p>Forms vary a little between councils, but expect to give:</p>
          <ul>
            <li>The address of the premises where the devices are</li>
            <li>The name and contact details of the person in control of the premises</li>
            <li>How many cooling towers and evaporative condensers there are</li>
            <li>Where they are on the site, for example rooftop, plant compound or which building</li>
          </ul>
          <p>It's a good idea to keep a copy of what you sent, along with any acknowledgement, in your <a href="{R}cooling-tower-log-books-compliance.html">log book</a>. That way anyone picking up the site later can see it was done.</p>

          <h2>When you need to notify again</h2>
          <p>Notification isn't a one-off forever. You'll need to update the local authority when:</p>
          <ul>
            <li><strong>A new tower or condenser is installed.</strong> Notify before it's in use. This is easy to forget on a project where the M&amp;E contractor hands over and moves on.</li>
            <li><strong>A unit is permanently taken out of use.</strong> Tell the council when a notified device stops being a notifiable device, so the register stays accurate.</li>
            <li><strong>The details change.</strong> For example, a change in who controls the premises, or a change in the number of units.</li>
          </ul>
          <p>A unit that's switched off for winter but still connected is still a notifiable device. Seasonal shutdowns don't change your notification, though they do bring their own risks, which we cover in our <a href="{R}cooling-tower-shutdown-start-up-commissioning.html">shutdown and start-up</a> service.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Picture a business that takes a lease on a building with two rooftop towers. The previous occupier notified them a decade ago, under their own name. The new occupier now controls the premises, so the council's record is out of date. A short updated notification puts that right and gives the council the correct contact if anything happens in the area.</p>
          </div>

          <h2>What notification doesn't do</h2>
          <p>It's worth being clear on this, because we sometimes hear "we're registered with the council, so we're fine." Notifying the local authority:</p>
          <ul>
            <li>isn't an approval or a licence,</li>
            <li>doesn't mean anyone has inspected your system, and</li>
            <li>doesn't replace any of your other duties.</li>
          </ul>
          <p>You still need a suitable and sufficient <a href="{R}cooling-tower-legionella-risk-assessment.html">Legionella risk assessment</a> and a written scheme under ACOP L8, a treatment programme, monitoring and cleaning in line with HSG274 Part 1, and records to prove it. Notification just makes sure the authorities know your system exists.</p>

          <h2>What about dry coolers and adiabatic units?</h2>
          <p>Dry air coolers that don't use water aren't cooling towers, so they're outside the scope of the regulations. Hybrid and adiabatic coolers are where it gets less clear-cut, because some designs spray or wet surfaces in ways that can create aerosol. If you're not sure whether a unit on your site counts, ask your local authority or get competent advice. Whatever the answer on notification, HSG274 Part 1 still expects the Legionella risk from any unit that creates spray to be assessed.</p>

          <h2>A quick checklist</h2>
          <ol>
            <li>List every cooling tower and evaporative condenser on site, including standby and seasonal units.</li>
            <li>Check your records for a copy of the notification to the local authority.</li>
            <li>If you can't find one, or the details are out of date, contact the council and submit a fresh notification.</li>
            <li>File the copy and any acknowledgement in your log book.</li>
            <li>Add "notify the council" to your project checklist for any new installation or decommissioning.</li>
          </ol>
          <p>If you'd like us to check your records while we're looking at the rest of your compliance, we're happy to. It's one of the first things we look for when we take on a site.</p>
""",
        "cta_title": "Want us to check your compliance records?",
        "cta_text": "We'll look through your log book, notification, risk assessment and written scheme and tell you plainly what's missing.",
    },
]
