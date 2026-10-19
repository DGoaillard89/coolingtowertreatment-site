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
    # ------------------------------------------------------------------ 3
    {
        "slug": "cooling-tower-start-up-after-shutdown",
        "title": "Bringing a cooling tower back into service after a shutdown",
        "seo_title": "Restarting a Cooling Tower After a Shutdown | HSG274",
        "date": "2024-05-08",
        "desc": "Restarting an idle cooling tower? Why stagnant water is a Legionella risk, what HSG274 Part 1 expects before restart and a practical start-up sequence.",
        "tag": "Start-up",
        "topic": "Cooling tower start-up after a shutdown",
        "services": ["cooling-tower-shutdown-start-up-commissioning", "cooling-tower-cleaning-disinfection", "cooling-tower-monitoring-sampling"],
        "body": """
          <p>May is when a lot of towers wake up. Comfort cooling that's been off since October gets switched back on, seasonal process lines start running, and someone in facilities gets asked to "just turn the tower on" before the first warm week arrives.</p>
          <p>That last bit is where it can go wrong. A cooling tower that's been sitting idle is at one of the riskiest points in its year, and flicking the fans on without a plan can throw out exactly the aerosol you've spent all year trying to control. Here's why, and how to bring a tower back properly.</p>

          <h2>Why an idle tower is a risk</h2>
          <p>When a tower stops, so does everything that keeps it under control. No circulation means no fresh biocide reaching the water, and whatever was in there slowly breaks down or gets used up. Water sits still in the pond, pipework and dead legs. Sludge settles. Biofilm carries on growing quietly on the fill and in the corners.</p>
          <p>Then, on restart, the pumps stir all of that up and the fans blow it out as drift. ACOP L8 and HSG274 Part 1 both treat start-up after an idle period as something that needs managing, not something you do on autopilot. Your written scheme should say what happens while the system is idle and what has to be done before it runs again.</p>

          <h2>Short break or long shutdown?</h2>
          <p>The right approach depends on how long the tower has been off and how it was left. Broadly there are two situations:</p>
          <ul>
            <li><strong>Short idle periods with treatment maintained.</strong> If the system has been kept topped up with treatment going, and circulated regularly so the chemicals reach everywhere, it may only need checks before it goes back into full service: chemical levels, a dip slide, a look at the pond and the dosing kit.</li>
            <li><strong>Longer shutdowns, or idle periods with no treatment.</strong> HSG274 Part 1 expects a system that's been out of use for an extended period to be cleaned and disinfected before it goes back into service. If the tower was drained and left dry, it still needs cleaning and disinfecting before restart, because dry doesn't mean clean.</li>
          </ul>
          <p>Where exactly the line sits between the two should be set out in your risk assessment and written scheme, not decided on the day. If your scheme is vague on it, that's worth fixing before the next shutdown. Our <a href="{R}cooling-tower-shutdown-start-up-commissioning.html">shutdown and start-up</a> page covers how we help sites plan this.</p>

          <h2>A sensible start-up sequence</h2>
          <p>Every site's a bit different, but a typical restart after a longer shutdown looks something like this:</p>
          <ol>
            <li><strong>Check the records.</strong> When did the tower stop? Was it drained, or left wet? Was treatment kept going? When was the last clean and the last <em>Legionella</em> sample? The answers decide how much work is needed.</li>
            <li><strong>Inspect before anything turns.</strong> Look in the pond, check the fill, drift eliminators and distribution, and make sure nothing has moved in over winter. Birds and their droppings are a classic spring find.</li>
            <li><strong>Check the kit.</strong> Make sure dosing pumps are primed, chemical drums are in date and full, the conductivity controller is calibrated and the bleed valve works. A pump that's sat for months may not deliver what the display says.</li>
            <li><strong>Clean and disinfect where needed.</strong> Follow the sequence in HSG274 Part 1: disinfect, drain and clean, refill, disinfect again, then flush and bring the water back to normal treatment levels. Chemical levels and contact times come from your written scheme or the method statement for the work.</li>
            <li><strong>Re-establish treatment before full load.</strong> Get biocide and inhibitor levels where the programme wants them before the tower is running hard.</li>
            <li><strong>Monitor closely.</strong> Dip slides and chemistry checks soon after restart tell you whether the system has settled down. Many schemes also call for a <em>Legionella</em> sample after a restart, timed so the result means something.</li>
            <li><strong>Write it all down.</strong> Dates, what was found, what was done, chemical readings and results, all in the log book.</li>
          </ol>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a building where the tower only runs from late spring to early autumn. Each October it's switched off and left full, and each spring the first warm day prompts someone to turn it straight back on. Nobody's being careless, it's just never been written down. The fix is simple: agree a proper end-of-season routine (drain and clean, or keep it circulating with treatment) and a start-up routine, with the clean and disinfection booked a couple of weeks before the cooling's needed.</p>
          </div>

          <h2>Better still: plan the shutdown properly</h2>
          <p>The easiest restart is one that was planned when the tower stopped. Before you switch off for a long period, decide which approach you're taking:</p>
          <ul>
            <li><strong>Keep it wet and treated.</strong> Water stays in, treatment stays on and the system is circulated regularly so biocide reaches the whole system. How often should come from your risk assessment.</li>
            <li><strong>Drain it down.</strong> Drain the system, clean it, and leave it dry with drains open so water can't collect. Then clean and disinfect again before restart.</li>
          </ul>
          <p>What you don't want is the halfway house: full of water, no circulation, no dosing, for months. That's the one that turns into a problem in spring.</p>

          <h2>Don't forget the standby units</h2>
          <p>Shutdowns aren't just seasonal. Standby towers, duty-assist cells and towers on sites with N+1 redundancy can sit idle for weeks while the duty unit does the work. A standby tower that's full of water but never runs is effectively a stagnant system. Your scheme should cover rotating duty and standby, or circulating the standby regularly, so it's ready to go and under control when it's called on.</p>
          <p>It's also worth checking whether a long shutdown changes anything with the council. A tower that's switched off but still connected is still notifiable. If it's being permanently taken out of use, that's a different matter, and we cover it in our post on <a href="{R}blog/notifying-local-authority-cooling-tower.html">notifying the local authority</a>.</p>

          <h2>The short version</h2>
          <p>Don't just flick the switch. Check how the tower was left, inspect it, get the dosing working, clean and disinfect if the scheme calls for it, and keep a close eye on <a href="{R}cooling-tower-monitoring-sampling.html">monitoring results</a> for the first few weeks. For more on what a proper clean involves, see <a href="{R}blog/how-often-should-a-cooling-tower-be-cleaned.html">how often a cooling tower should be cleaned</a>.</p>
          <p>If you'd like a hand planning this year's restart, or writing a proper shutdown routine into your scheme, give us a ring. Booking it in a few weeks ahead makes everyone's life easier, including ours.</p>
""",
        "cta_title": "Tower been sitting idle?",
        "cta_text": "Tell us how it was left and when you need it running. We'll plan the inspection, clean and disinfection so it's back in service safely and on time.",
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "positive-legionella-result-cooling-tower",
        "title": "Positive Legionella result in a cooling tower: the first 48 hours",
        "seo_title": "Positive Legionella Result in a Cooling Tower: First Steps",
        "date": "2024-08-22",
        "desc": "Got a positive Legionella result from your cooling tower? A calm, practical guide to the first 48 hours: what HSG274 Part 1 expects and who to call.",
        "tag": "Results",
        "topic": "Positive Legionella result in a cooling tower",
        "services": ["positive-legionella-result-response", "cooling-tower-monitoring-sampling", "chemical-dosing-biocide-control"],
        "body": """
          <p>The email from the lab arrives, and there it is: <em>Legionella</em> detected in the cooling tower sample. Your stomach drops a bit. That's normal. The good news is that a positive result is something the guidance plans for, and if you act quickly and sensibly, it's very manageable.</p>
          <p>Late summer is when you'd expect more of these. Warm water, high heat loads and heavy evaporation all put a treatment programme under pressure. Here's what to do in the first couple of days, in roughly the order you'll need it.</p>

          <h2>Hour one: read the result properly</h2>
          <p>Before anything else, look at what the certificate actually says:</p>
          <ul>
            <li><strong>The count.</strong> Results are reported in cfu/litre (colony forming units per litre). The number matters, because HSG274 Part 1 sets different responses for different levels.</li>
            <li><strong>The sample point and date.</strong> Which system, which tower, and when it was taken. On multi-tower sites, make sure you know exactly which one it is.</li>
            <li><strong>Any typing information.</strong> Some labs report whether it's <em>Legionella pneumophila</em> serogroup 1 or another type. Note it down, as it helps your adviser judge the risk.</li>
          </ul>
          <p>Then check it against your written scheme, which should set out exactly what happens at each level. As a plain-English summary of HSG274 Part 1 for cooling systems:</p>
          <ul>
            <li><strong>Above 100 and up to 1,000 cfu/litre:</strong> resample. If the result is repeated, or most samples come back positive, review the control measures and risk assessment and carry out the remedial actions identified, which may include disinfection.</li>
            <li><strong>Above 1,000 cfu/litre:</strong> resample, and immediately review the control measures and risk assessment, with remedial action that may include disinfecting the system.</li>
          </ul>
          <p>Our <a href="{R}positive-legionella-result-response.html">positive result response</a> page sets these out in a table alongside the TVC levels. Your written scheme and the guidance itself have the full wording.</p>

          <h2>The first few hours: tell the right people</h2>
          <p>A positive result shouldn't sit in one person's inbox. Let your responsible person for Legionella control know straight away, along with your water treatment contractor and whoever runs the plant. If your scheme names other people, such as a site health and safety lead, include them too.</p>
          <p>A positive sample on its own isn't generally something you have to report to anyone. What you must do is act on it and record what you did. Things change if there's a suspected case of Legionnaires' disease linked to the site. The local authority or UKHSA may then get in touch, and if the person affected is a worker whose illness is linked to their work, there may be reporting duties under RIDDOR. If you find yourself anywhere near that situation, get competent advice quickly.</p>

          <h2>Day one: find the likely cause</h2>
          <p>A count doesn't go up for no reason. Fixing the number without finding the cause just means you'll be back here in three months. The usual suspects:</p>
          <ul>
            <li><strong>Dosing.</strong> Is the biocide pump running and primed? Is the drum empty, or the wrong product connected? Is the inhibitor going in?</li>
            <li><strong>Bleed and chemistry.</strong> Has the conductivity controller or bleed valve failed, letting the water concentrate?</li>
            <li><strong>Recent dip slides.</strong> Have TVCs been creeping up over the last few weeks?</li>
            <li><strong>Cleanliness.</strong> When was the last clean and disinfection? Is the pond visibly dirty?</li>
            <li><strong>Operating pattern.</strong> Has the tower been idle, on low load, or running much harder than usual in hot weather?</li>
          </ul>
          <p>An engineer on site, looking at the tower and the <a href="{R}chemical-dosing-biocide-control.html">dosing kit</a> with the records in hand, will usually spot the likely cause quickly.</p>

          <h2>Day one to two: corrective action</h2>
          <p>What you do depends on the count, the history and what the investigation turns up. Typical actions include:</p>
          <ul>
            <li>Fixing the dosing fault or bleed problem straight away</li>
            <li>An online disinfection of the system, at the level and contact time set out in your written scheme or method statement</li>
            <li>Bringing forward a full clean and disinfection if the system is dirty</li>
            <li>Stepping up dip slides and chemistry checks for a while</li>
          </ul>
          <p>Should you shut the tower down? Not automatically. Many results are dealt with by resampling, fixing the cause and disinfecting while the system keeps running. In some situations, particularly at higher counts or where vulnerable people are nearby, isolating or shutting down the tower is the right call. Bear in mind that switching off and leaving water stagnant can make things worse, so if you do shut down, have a plan for what happens next. Make the decision with your adviser, and write down why.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a quarterly sample comes back above 100 cfu/litre during a hot August. The records show the biocide drum ran low a fortnight earlier and wasn't swapped for several days, and dip slides have been edging up since. The response is clear: replace the drum, check the pump is delivering, carry out an online disinfection as the scheme sets out, step up monitoring and resample. The risk assessment review then asks why a low drum wasn't flagged sooner.</p>
          </div>

          <h2>Resample, and time it sensibly</h2>
          <p>A resample tells you whether control has been restored. Timing matters. Sample too soon after a disinfection and the result may look clean while the underlying problem is still there. Your written scheme or adviser should set the timing, and samples should go to a UKAS-accredited laboratory, the same as routine ones. Keep resampling as the scheme requires until results show the system is back under control.</p>

          <h2>Record everything</h2>
          <p>This is the part that gets forgotten once the adrenaline wears off. Your <a href="{R}cooling-tower-log-books-compliance.html">log book</a> should show the original result, who was told and when, what the investigation found, what was done (with chemical readings and dates), the resample results and any changes to the risk assessment or written scheme. If an inspector or environmental health officer ever asks, that record is your evidence that you took it seriously and acted promptly.</p>

          <h2>In short</h2>
          <p>Read the result, check it against your scheme, tell the right people, find the cause, fix it, resample and record. It's a process, not a crisis. If a dirty system turns out to be the cause, our post on <a href="{R}blog/how-often-should-a-cooling-tower-be-cleaned.html">cleaning frequency</a> is worth a read, and if the tower had recently been idle, see <a href="{R}blog/cooling-tower-start-up-after-shutdown.html">restarting after a shutdown</a>.</p>
          <p>Got a result in front of you right now and not sure what to do next? Give us a ring and we'll talk it through.</p>
""",
        "cta_title": "Got a positive result in front of you?",
        "cta_text": "Call us or send the details through the form. We'll help you work out the cause, the right response and the resample plan.",
    },
    # ------------------------------------------------------------------ 5
    {
        "slug": "cooling-tower-dosing-failures",
        "title": "Dosing failures: spotting a struggling dosing system early",
        "seo_title": "Cooling Tower Dosing Failures: Early Warning Signs",
        "date": "2024-11-12",
        "desc": "Cooling tower dosing systems fail quietly. The common causes, the warning signs to look for in your weekly checks and what to do when you spot one.",
        "tag": "Dosing",
        "topic": "Cooling tower dosing problems",
        "services": ["chemical-dosing-biocide-control", "cooling-tower-water-treatment", "cooling-tower-monitoring-sampling"],
        "body": """
          <p>Dosing systems rarely fail with a bang. There's no alarm bell, no cloud of smoke. A pump loses prime, a drum runs dry over a weekend, or a controller drifts out of calibration, and the tower carries on looking perfectly normal. Weeks later the dip slides start climbing, or a <em>Legionella</em> sample comes back positive, and everyone's wondering what happened.</p>
          <p>The good news is that most dosing problems leave clues long before they become a crisis. Here's what tends to go wrong, how to spot it during routine checks and what to do about it.</p>

          <h2>What the dosing system is actually doing</h2>
          <p>A typical cooling tower treatment set-up has a few parts working together:</p>
          <ul>
            <li><strong>Biocide dosing</strong> to keep bacteria, including <em>Legionella</em>, under control. Often two biocides are used, either alternated or one continuous and one shot-dosed.</li>
            <li><strong>Inhibitor dosing</strong> to stop scale and corrosion, usually dosed in proportion to the make-up water or controlled by a sensor.</li>
            <li><strong>Bleed control</strong>, normally a conductivity controller and a solenoid valve that dumps concentrated water so fresh water can come in.</li>
          </ul>
          <p>If any one of these stops working, the others can't fully make up for it. Our <a href="{R}chemical-dosing-biocide-control.html">chemical dosing and biocide control</a> page explains the kit in more detail.</p>

          <h2>The usual culprits</h2>
          <p>Most dosing problems come down to a fairly short list:</p>
          <ul>
            <li><strong>Empty or nearly empty drums.</strong> The simplest one, and still one of the most common. Particularly over holidays and long weekends.</li>
            <li><strong>Loss of prime or air locks.</strong> Diaphragm pumps can click away happily while delivering very little, especially after a drum change.</li>
            <li><strong>Blocked injection points or foot valves.</strong> Chemical deposits and debris build up over time and restrict flow.</li>
            <li><strong>Wrong drum on the wrong line.</strong> Easy to do when drums look alike. It can mean no biocide going in, or two incompatible products ending up in one line.</li>
            <li><strong>Controller faults or drifting probes.</strong> A dirty conductivity probe reads wrong, so the bleed stays shut or runs all the time.</li>
            <li><strong>Stuck bleed valves.</strong> A solenoid stuck shut lets the water concentrate. One stuck open wastes water and washes treatment out.</li>
            <li><strong>Power or timer issues.</strong> A tripped supply, or a timer that resets after a power cut, can stop shot dosing without anyone noticing.</li>
            <li><strong>Old or badly stored chemicals.</strong> Some products lose strength over time, or if they're stored too hot or too cold.</li>
          </ul>

          <h2>Warning signs in your weekly checks</h2>
          <p>You don't need a lab to catch most of these. Build a few simple checks into your routine:</p>
          <ol>
            <li><strong>Drum levels.</strong> Note the level on the record sheet each week. If a drum isn't going down, the pump probably isn't pumping. If it's going down much faster than usual, something else is wrong.</li>
            <li><strong>Pump operation.</strong> Look at the pump while it should be running. Is it stroking? Is chemical actually moving up the line?</li>
            <li><strong>Controller readout.</strong> Compare the conductivity on the display with previous readings. A sudden jump, or a reading that never moves, is worth questioning.</li>
            <li><strong>Bleed.</strong> Check the bleed valve opens when it should, and that water isn't running to drain constantly.</li>
            <li><strong>Dip slides and chemistry.</strong> Rising TVCs, low biocide or inhibitor residuals and creeping conductivity are often the first measurable sign that dosing has slipped. Our <a href="{R}cooling-tower-monitoring-sampling.html">monitoring and sampling</a> page covers what to check and how often.</li>
          </ol>
          <p>Write it all down. A single reading doesn't tell you much. A trend over several weeks tells you a lot.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Picture a site where the biocide drum level has barely moved for three weekly checks running, but the pump display looks fine. Nobody's thought much of it, because the tower looks clean. The fourth dip slide comes back noticeably higher. A closer look shows the foot valve is partly blocked and the pump has been delivering a fraction of what it should. Spotting that flat drum level on the record sheet a fortnight earlier would have avoided the high count altogether.</p>
          </div>

          <h2>What to do when you spot a problem</h2>
          <ul>
            <li><strong>Fix the obvious first.</strong> Swap an empty drum, re-prime the pump, reset a tripped supply. Only do this if you're trained and have the right PPE, and follow your COSHH assessment and the product's safety data sheet. Treatment chemicals can be hazardous.</li>
            <li><strong>Tell your treatment contractor.</strong> They'll want to know, and they may want to check residuals or add a shot dose to bring levels back up.</li>
            <li><strong>Step up monitoring for a while.</strong> An extra dip slide or chemistry check after a dosing fault shows whether the system has recovered.</li>
            <li><strong>Record it.</strong> What you found, what you did and when. A dosing fault that's spotted, fixed and written down is good evidence your system works. One that's found later with no record looks very different.</li>
          </ul>
          <p>If counts are already high, or a <em>Legionella</em> result has come back above your scheme's action level, follow your written scheme and see our guide to <a href="{R}blog/positive-legionella-result-cooling-tower.html">the first 48 hours after a positive result</a>.</p>

          <h2>Preventing it in the first place</h2>
          <p>A few habits make a big difference:</p>
          <ul>
            <li>Label every drum and every line clearly, so the right product goes on the right pump.</li>
            <li>Keep a spare drum of each product on site, stored as the safety data sheet says.</li>
            <li>Check drum levels before long weekends and holidays. Christmas is a few weeks away, so now's a good time.</li>
            <li>Have probes cleaned and calibrated, and pumps checked, on every service visit.</li>
            <li>Consider remote monitoring or alarms for low drum level, no flow and high conductivity, especially on critical systems.</li>
          </ul>
          <p>As the nights draw in, it's also worth making sure dosing kit and chemical lines are protected from frost. A frozen line is a dosing failure too, and it tends to happen on the coldest night of the year when nobody's around.</p>
          <p>Our <a href="{R}cooling-tower-water-treatment.html">water treatment service</a> includes routine checks and calibration of all of this. If you've got a dosing set-up that never seems quite right, or the tower's been idle and the kit needs a once-over (see <a href="{R}blog/cooling-tower-start-up-after-shutdown.html">restarting after a shutdown</a>), we're happy to take a look.</p>
""",
        "cta_title": "Dosing system playing up?",
        "cta_text": "Tell us what you're seeing. We'll check the kit, the chemistry and the records, and get the programme back on track.",
    },
    # ------------------------------------------------------------------ 6
    {
        "slug": "cooling-tower-log-book",
        "title": "What should be in a cooling tower log book?",
        "seo_title": "What Should Be in a Cooling Tower Log Book? | ACOP L8",
        "date": "2025-02-18",
        "desc": "What a cooling tower log book should contain under ACOP L8 and HSG274 Part 1, how long to keep records and the gaps inspectors tend to find.",
        "tag": "Records",
        "topic": "Cooling tower log book and records",
        "services": ["cooling-tower-log-books-compliance", "cooling-tower-legionella-risk-assessment", "cooling-tower-monitoring-sampling"],
        "body": """
          <p>If an inspector or environmental health officer visits your site to talk about your cooling towers, the first thing they'll ask for probably won't be to see the tower. It'll be the log book. That folder (or folder of PDFs) is how you prove the treatment programme is happening, not just that it was planned.</p>
          <p>A good log book is also just useful. It's where trends show up, where problems get spotted early and where the next person to look after the site finds out what's been going on. February is a quiet month for most towers, so it's a good time to give yours a once-over. Here's what should be in it.</p>

          <h2>What ACOP L8 says about records</h2>
          <p>ACOP L8 expects the duty holder to keep records that show Legionella risks are being managed. In broad terms, that means records of:</p>
          <ul>
            <li>the people responsible for carrying out the risk assessment and managing and implementing the written scheme,</li>
            <li>the significant findings of the risk assessment,</li>
            <li>the written scheme and details of how it's being put into practice, and</li>
            <li>the results of any monitoring, inspection, tests or checks, with the dates they were done.</li>
          </ul>
          <p>On how long to keep them: ACOP L8 says monitoring, inspection, test and check records should be kept for at least five years. Records such as the risk assessment and written scheme should be kept for as long as they're current and for at least two years after that. If in doubt, keep them. Storage is cheap; missing records aren't.</p>

          <h2>A sensible layout</h2>
          <p>There's no single official format, but a log book that's laid out logically makes life easier for everyone. Here's how we'd suggest organising it.</p>

          <h3>1. Contacts and responsibilities</h3>
          <p>The duty holder, the responsible person appointed to manage Legionella control (and their deputy), your water treatment contractor and anyone else with a defined role. Include how to reach them out of hours. If the responsible person changes, update it the same week.</p>

          <h3>2. System description and drawings</h3>
          <p>What you've got: number and type of towers or evaporative condensers, where they are, approximate water volumes, what they serve, dosing and bleed arrangements, and sample points. A simple schematic is worth a lot, especially to a new engineer on their first visit.</p>

          <h3>3. Risk assessment and written scheme</h3>
          <p>The current <a href="{R}cooling-tower-legionella-risk-assessment.html">Legionella risk assessment</a> and written scheme, with any action plan and evidence that actions have been closed out. Keep superseded versions too, filed separately.</p>

          <h3>4. Notification</h3>
          <p>A copy of the notification to the local authority under the Notification of Cooling Towers and Evaporative Condensers Regulations 1992, plus any updates. We wrote about this in <a href="{R}blog/notifying-local-authority-cooling-tower.html">do you need to notify the council?</a></p>

          <h3>5. Routine monitoring</h3>
          <p>This is the bulk of the book:</p>
          <ul>
            <li>Weekly dip slide or TVC results, with the date taken and date read</li>
            <li>Chemistry results: conductivity, pH, biocide and inhibitor levels, hardness and so on, as your scheme specifies</li>
            <li>Dosing checks: drum levels, pump operation, controller readings and bleed operation</li>
            <li><em>Legionella</em> sample certificates from the UKAS-accredited lab</li>
            <li>Visual inspection notes on the tower's condition</li>
          </ul>
          <p>Results are much more useful with the action levels printed next to them, so whoever fills in the sheet can see straight away if something's out of range.</p>

          <h3>6. Cleaning and disinfection</h3>
          <p>Certificates or reports for every clean and disinfection, showing what was done, chemical levels and contact times, and what was found. HSG274 Part 1 expects cooling towers to be cleaned and disinfected at least twice a year, so an inspector will look for at least two of these each year.</p>

          <h3>7. Corrective actions</h3>
          <p>Every out-of-range result or fault, what was done about it, by whom, and when it was closed out. This section often tells an inspector more about your site than anything else.</p>

          <h3>8. Service visits and maintenance</h3>
          <p>Service reports from your treatment contractor, calibration records for controllers and probes, and records of repairs to fill, drift eliminators, fans and pumps.</p>

          <h3>9. Training and competence</h3>
          <p>Evidence that the people doing the checks know what they're doing: training records for site staff who take dip slides or check dosing, and for the responsible person.</p>

          <h3>10. Chemical safety</h3>
          <p>COSHH assessments and safety data sheets for the treatment chemicals on site.</p>

          <h2>The gaps we see most often</h2>
          <ul>
            <li><strong>Blank weeks.</strong> A missing weekly check is hard to explain afterwards. If a check couldn't be done, write down why.</li>
            <li><strong>Results with no action.</strong> A high dip slide recorded, and then nothing. Every out-of-range result needs a note of what happened next.</li>
            <li><strong>Out-of-date risk assessments.</strong> The assessment refers to plant that's been replaced, or people who've left.</li>
            <li><strong>Missing cleaning certificates.</strong> The clean happened, but nobody filed the paperwork.</li>
            <li><strong>No notification on file.</strong> Especially on sites that have changed hands.</li>
          </ul>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a site where the weekly checks are done faithfully by the maintenance team, but the results live on a clipboard in the plant room and the lab certificates sit in the contractor's online portal. Nothing's actually missing, yet nobody can show the full picture in one place. Pulling it together into a single, logically ordered log book, paper or digital, turns a stressful inspection into a straightforward one.</p>
          </div>

          <h2>Paper or digital?</h2>
          <p>Either is fine, as long as records are complete, legible, dated, and can be produced when someone asks. Digital log books make trends easier to spot and are harder to lose. Paper is simple and always in the plant room. Plenty of sites use a mix. What matters is that the records exist and someone actually reads them.</p>

          <h2>Read it, don't just fill it</h2>
          <p>The most valuable thing a log book does is show trends. A dip slide that creeps up over six weeks, or a biocide drum that's being used more slowly than usual, is your early warning. Ten minutes a month looking back over the last few pages can save a lot of trouble.</p>
          <p>Our <a href="{R}cooling-tower-log-books-compliance.html">log books and compliance</a> service sets up and maintains the log book for you, updated on every visit. If yours has got a bit messy, or you've inherited one you don't trust, we're happy to go through it with you.</p>
""",
        "cta_title": "Log book in a state?",
        "cta_text": "We'll go through what you've got, tell you plainly what's missing and set up a log book that's easy to keep on top of.",
    },
    # ------------------------------------------------------------------ 7
    {
        "slug": "data-centre-cooling-tower-water-treatment",
        "title": "Data centre cooling towers: water treatment without risking uptime",
        "seo_title": "Data Centre Cooling Tower Water Treatment & Legionella",
        "date": "2025-05-06",
        "desc": "How data centres can stay on top of cooling tower water treatment, cleaning and Legionella control without putting uptime at risk.",
        "tag": "Sectors",
        "topic": "Data centre cooling tower water treatment",
        "services": ["cooling-tower-water-treatment", "cooling-tower-cleaning-disinfection", "chemical-dosing-biocide-control"],
        "body": """
          <p>Data centres have a slightly awkward relationship with cooling towers. The towers are essential to keeping the halls cool, so nobody wants to touch them. But leaving them alone is exactly what you can't do. ACOP L8 and HSG274 Part 1 apply to a data centre's towers in just the same way as an office block's, and the cleaning, monitoring and treatment still have to happen.</p>
          <p>The good news is that keeping on top of water treatment and keeping the lights on aren't in conflict. It just takes more planning than most sites. Here's how to approach it, with summer heat loads just around the corner.</p>

          <h2>Why data centres are a bit different</h2>
          <ul>
            <li><strong>Continuous load.</strong> Towers often run around the clock, all year. There's no natural winter shutdown to fit a clean into.</li>
            <li><strong>Change control.</strong> Any work on cooling plant usually needs a method statement, a risk assessment, a change request and an agreed window.</li>
            <li><strong>Access and security.</strong> Contractors need inductions, escorts and pre-booked access. A "quick visit" isn't really a thing.</li>
            <li><strong>Equipment protection.</strong> Scale and corrosion don't just waste energy, they threaten heat exchangers and condensers that the whole facility relies on.</li>
            <li><strong>Reputational risk.</strong> A Legionella problem at a well-known facility is a story nobody wants to be in.</li>
          </ul>
          <p>None of these are reasons to do less. They're reasons to plan earlier.</p>

          <h2>Use the redundancy you've already got</h2>
          <p>Most data centres are designed with spare cooling capacity, whether that's N+1 towers, multi-cell towers or standby chillers. That redundancy is your friend when it comes to cleaning. Typical approaches:</p>
          <ul>
            <li>Clean one cell at a time while the others carry the load.</li>
            <li>Take one tower out of service while the standby runs, then swap.</li>
            <li>Time cleans for spring and autumn, when outside temperatures give you more headroom.</li>
          </ul>
          <p>Bear in mind that a standby tower sitting full of water and never running is effectively a stagnant system. Rotating duty and standby, or circulating the standby regularly with treatment, keeps it ready and under control. We wrote more about that in <a href="{R}blog/cooling-tower-start-up-after-shutdown.html">bringing a tower back after a shutdown</a>.</p>

          <h2>Make the dosing as reliable as the power</h2>
          <p>Data centres put a lot of thought into backup power. Dosing deserves some of the same thinking, because a quiet dosing failure is one of the most common routes to a high count. Things worth considering:</p>
          <ul>
            <li>Alarms for low drum level, no flow and high conductivity, linked into the BMS so someone actually sees them</li>
            <li>Spare chemical stock on site, stored safely in line with the safety data sheets</li>
            <li>Regular calibration of conductivity probes and controllers</li>
            <li>Clear labelling of drums and lines, so a drum change can't connect the wrong product</li>
          </ul>
          <p>Our post on <a href="{R}blog/cooling-tower-dosing-failures.html">spotting dosing failures early</a> goes through the common causes in more detail.</p>

          <h2>Get the monitoring routine right</h2>
          <p>Monitoring on a data centre tower is the same in principle as anywhere else: dip slides or TVCs at least weekly, chemistry checks as your scheme sets out, and <em>Legionella</em> sampling at least quarterly to a UKAS-accredited lab. The difference is making it fit the site's way of working:</p>
          <ul>
            <li>Agree standing access for routine monitoring visits so they don't need a fresh change request each time.</li>
            <li>Put sample points where they can be reached safely without entering restricted areas unnecessarily.</li>
            <li>Make sure results reach the facilities team quickly, with clear action levels, so a high result isn't sitting in someone's inbox.</li>
          </ul>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a facility with three towers in an N+1 arrangement. Cleans keep slipping because nobody wants to raise the change request in summer, and by autumn the certificates are overdue. A better pattern is to fix the cleaning dates a year ahead, one tower at a time in spring and autumn, with the change requests drafted well in advance. The work becomes routine instead of a recurring argument.</p>
          </div>

          <h2>Plan for a positive result before you get one</h2>
          <p>On a site where you can't easily shut the cooling down, the time to decide what happens after a high <em>Legionella</em> result is now, not when the certificate arrives. Your written scheme should cover:</p>
          <ul>
            <li>Who gets told, including out of hours</li>
            <li>How an online disinfection would be done without disrupting cooling</li>
            <li>How a tower could be isolated if the risk called for it, and what that means for capacity</li>
            <li>Pre-approved method statements, so emergency work doesn't wait on paperwork</li>
          </ul>
          <p>Our <a href="{R}blog/positive-legionella-result-cooling-tower.html">first 48 hours guide</a> explains the response in general terms.</p>

          <h2>What about adiabatic and hybrid coolers?</h2>
          <p>Plenty of newer data centres use adiabatic or hybrid coolers instead of, or alongside, open cooling towers. They use far less water, but where a unit sprays or wets surfaces it can still create aerosol. HSG274 Part 1 expects the Legionella risk from any unit that can produce spray to be assessed, so don't assume they're automatically out of scope. Whether they need notifying to the local authority depends on the design, and it's worth getting a clear answer for your units.</p>

          <h2>The short version</h2>
          <p>Use your redundancy to clean on schedule, make dosing as resilient as everything else on site, agree access for routine monitoring and plan your response to a high result in advance. Our <a href="{R}cooling-tower-water-treatment.html">water treatment</a> and <a href="{R}cooling-tower-cleaning-disinfection.html">cleaning and disinfection</a> services are built around sites that can't switch off. If you'd like to talk through how that could work on yours, we're happy to.</p>
""",
        "cta_title": "Running cooling towers on a critical site?",
        "cta_text": "Tell us about your plant and how much redundancy you've got. We'll suggest a treatment and cleaning plan that works around your uptime.",
    },
    # ------------------------------------------------------------------ 8
    {
        "slug": "dip-slides-tvc-cooling-tower",
        "title": "Dip slides and TVCs explained: reading your weekly checks",
        "seo_title": "Cooling Tower Dip Slides and TVCs Explained",
        "date": "2025-08-19",
        "desc": "How cooling tower dip slides work, how to take and read one properly, what TVC results mean against HSG274 Part 1 action levels and common mistakes.",
        "tag": "Monitoring",
        "topic": "Dip slides and TVC monitoring",
        "services": ["cooling-tower-monitoring-sampling", "positive-legionella-result-response", "cooling-tower-log-books-compliance"],
        "body": """
          <p>The weekly dip slide is probably the most-done and least-understood check on a cooling tower. Someone dunks a little plastic paddle in the water, pops it in an incubator, reads it a couple of days later and writes a number in the log book. But what is that number actually telling you, and what should you do with it?</p>
          <p>August is a good month to ask. Warm weather and heavy loads mean counts can move quickly, and the dip slide is usually the first place you'll see it. Here's a plain-English guide.</p>

          <h2>What a dip slide measures</h2>
          <p>A dip slide is a plastic paddle coated with a growth medium. You dip it in the cooling water, incubate it, and bacteria in the water grow into visible spots (colonies) on the surface. By comparing the slide with a chart supplied by the manufacturer, you get an estimate of the total viable count, or TVC: roughly how many bacteria per millilitre were in the water.</p>
          <p>Two important points:</p>
          <ul>
            <li><strong>It's a general count, not a <em>Legionella</em> test.</strong> A dip slide tells you how active the bacterial population is overall, which shows whether the biocide regime is keeping up. <em>Legionella</em> needs a separate lab test, which HSG274 Part 1 expects at least quarterly.</li>
            <li><strong>It's an estimate.</strong> Dip slide results are read in broad bands, usually powers of ten. That's fine, because what you're looking for is which band you're in and whether it's changing.</li>
          </ul>

          <h2>How often?</h2>
          <p>HSG274 Part 1 expects microbiological activity in cooling water to be checked at least weekly, and dip slides are the usual way of doing it. Your written scheme should set the exact frequency and say who does it.</p>

          <h2>Taking a dip slide properly</h2>
          <p>Small details make a big difference to whether the result means anything:</p>
          <ol>
            <li><strong>Check the slide.</strong> Make sure it's in date and has been stored as the manufacturer says. Don't touch the agar surface.</li>
            <li><strong>Sample the right water.</strong> Take it from a point that represents the circulating water, not right next to where biocide is injected, and not from a dead leg.</li>
            <li><strong>Watch the timing.</strong> Avoid sampling straight after a shot dose of biocide, or you'll be measuring the dose, not the system. Your scheme should say when in the dosing cycle to sample.</li>
            <li><strong>Dip, drain and label.</strong> Immerse the slide for the time the instructions say, let excess water drain, put it back in its tube and label it with the system, date and time.</li>
            <li><strong>Incubate.</strong> Follow the manufacturer's instructions and your scheme for temperature and time. That's commonly around two days in an incubator.</li>
            <li><strong>Read and record.</strong> Compare both sides of the slide with the chart, record the result and the date it was read, and note anything unusual, such as fungi or a slide that's completely covered.</li>
          </ol>

          <h2>What the results mean</h2>
          <p>HSG274 Part 1 sets action levels for TVC in cooling water. As a simplified summary, which matches our <a href="{R}positive-legionella-result-response.html">positive result response</a> page:</p>
          <ul>
            <li><strong>Up to 10<sup>4</sup> cfu/ml:</strong> under control. Carry on with the programme and routine monitoring.</li>
            <li><strong>Above 10<sup>4</sup>, up to 10<sup>5</sup> cfu/ml:</strong> review the programme and dosing, and re-test to confirm the count.</li>
            <li><strong>Above 10<sup>5</sup> cfu/ml:</strong> take corrective action straight away, review the controls and re-test.</li>
          </ul>
          <p>Your written scheme should have the exact responses for your site. Write the action levels at the top of the record sheet so whoever reads the slide knows straight away whether it's a normal week.</p>

          <h2>Trends matter more than single results</h2>
          <p>A single reading in the lower band is reassuring. But a run of readings tells you far more. Watch for:</p>
          <ul>
            <li><strong>A slow creep.</strong> Counts edging up band by band over several weeks often means dosing is slipping or the system's getting dirty.</li>
            <li><strong>A sudden jump.</strong> Usually something specific: an empty drum, a failed pump, a process leak, a change in operation.</li>
            <li><strong>Counts that don't come down.</strong> If a high result doesn't improve after corrective action, the cause hasn't been found yet.</li>
          </ul>
          <p>Our post on <a href="{R}blog/cooling-tower-dosing-failures.html">dosing failures</a> covers the common causes of a rising count.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a tower where dip slides have read in the lowest band all year. Then, over three hot weeks, they step up one band and stay there. Nothing's over an action level yet, but the trend is clear. A check finds the bleed valve sticking and the water more concentrated than it should be, which has been eating into the biocide. Fixing the valve brings the counts back down before anything needed escalating.</p>
          </div>

          <h2>Common mistakes</h2>
          <ul>
            <li>Reading the slide too early, or forgetting it in the incubator for a week</li>
            <li>Using out-of-date slides, or ones stored somewhere hot</li>
            <li>Sampling right after a biocide dose, which gives a falsely low result</li>
            <li>Recording "OK" instead of the actual band</li>
            <li>Writing down a high result and taking no action</li>
          </ul>

          <h2>Dip slides or lab TVCs?</h2>
          <p>Some sites send TVC samples to a lab instead of, or as well as, using dip slides. Lab counts are more precise but take longer to come back and cost more. Dip slides are quick and cheap, and done properly they're a perfectly good weekly early warning. Many sites use dip slides weekly and lab samples at set intervals or after a high reading.</p>

          <h2>In short</h2>
          <p>Take the slide from the right place at the right time, incubate it properly, record the actual result and watch the trend. Our <a href="{R}cooling-tower-monitoring-sampling.html">monitoring and sampling</a> service can do it for you, or train your team and pick up the chemistry and lab work. All results go straight into your <a href="{R}cooling-tower-log-books-compliance.html">log book</a>, and anything out of range gets a clear next step.</p>
""",
        "cta_title": "Not sure what your dip slides are telling you?",
        "cta_text": "Send us a few weeks of results and we'll talk you through them, or take the weekly checks off your hands altogether.",
    },
    # ------------------------------------------------------------------ 9
    {
        "slug": "cooling-tower-vs-evaporative-condenser",
        "title": "Cooling tower or evaporative condenser? What it means for Legionella control",
        "seo_title": "Cooling Tower vs Evaporative Condenser: Legionella Control",
        "date": "2025-11-11",
        "desc": "How cooling towers and evaporative condensers differ, why both carry a Legionella risk, and what changes for treatment, cleaning and monitoring.",
        "tag": "Systems",
        "topic": "Evaporative condenser treatment",
        "services": ["cooling-tower-water-treatment", "cooling-tower-legionella-risk-assessment", "cooling-tower-cleaning-disinfection"],
        "body": """
          <p>"We haven't got a cooling tower, it's just the condenser for the cold store." We hear some version of this fairly often. And it's an understandable mix-up, because from the outside an evaporative condenser can look like a smallish cooling tower, and in day-to-day conversation the names get used loosely.</p>
          <p>The difference matters less than people hope, though. Both use evaporation to reject heat, both create spray, and both are covered by the same law and guidance on Legionella. Here's how they differ, and what that means for keeping them under control.</p>

          <h2>How a cooling tower works</h2>
          <p>A wet cooling tower cools water. Warm water comes back from whatever it's been cooling (usually a chiller's condenser or a process heat exchanger), is sprayed or distributed over fill inside the tower, and a fan pulls air through it. A small amount of the water evaporates, which takes heat with it, and the cooler water collects in the pond at the bottom before being pumped back round.</p>
          <p>The key point: the water in the tower circulates through pipework to equipment elsewhere on site. So the "system" isn't just the tower. It's the pond, the pumps, the pipework, the heat exchangers and any dead legs along the way.</p>

          <h2>How an evaporative condenser works</h2>
          <p>An evaporative condenser cuts out the middle step. Instead of cooling water and sending it off to a separate condenser, the refrigerant itself runs through a coil inside the unit. Water is sprayed over the outside of the coil, a fan pulls air across, some water evaporates, and the refrigerant inside condenses. The spray water drops into a sump and is pumped back up to the sprays.</p>
          <p>You'll often find evaporative condensers on industrial refrigeration, cold stores, food and drink sites and some larger air conditioning plant. Closed-circuit coolers work on a similar idea, with a process fluid in the coil instead of refrigerant.</p>

          <h2>What's the same</h2>
          <p>From a Legionella point of view, quite a lot:</p>
          <ul>
            <li><strong>Warm water and spray.</strong> Both have recirculating water at temperatures that can suit bacterial growth, and both throw out aerosol that people nearby could breathe in.</li>
            <li><strong>Same law and guidance.</strong> The Health and Safety at Work etc. Act 1974, COSHH, ACOP L8 and HSG274 Part 1 all apply. HSG274 Part 1 covers both types of system.</li>
            <li><strong>Same notification duty.</strong> The Notification of Cooling Towers and Evaporative Condensers Regulations 1992 cover both, as the name suggests. We explain how that works in <a href="{R}blog/notifying-local-authority-cooling-tower.html">do you need to notify the council?</a></li>
            <li><strong>Same building blocks.</strong> A risk assessment, a written scheme, a treatment programme, regular monitoring, cleaning and disinfection, and records.</li>
          </ul>

          <h2>What's different in practice</h2>
          <p>The differences are mostly about how the control measures work day to day:</p>
          <ul>
            <li><strong>Smaller water volume.</strong> Evaporative condensers often hold much less water than a cooling tower system. Chemistry can change quickly, so a dosing fault or a stuck bleed shows up faster, and dosing needs to be well matched to the system.</li>
            <li><strong>The coil is the heat transfer surface.</strong> Scale or biofilm on the coil goes straight to refrigeration performance and energy use. Good inhibitor control and bleed management pay for themselves.</li>
            <li><strong>Cleaning access.</strong> Getting to the coil, sprays and sump for a proper clean can be fiddlier than on an open tower, and some units need panels removed or specific access arrangements. That needs planning, especially on sites that can't lose refrigeration.</li>
            <li><strong>Cleaning frequency.</strong> HSG274 Part 1 expects cooling towers to be cleaned and disinfected at least twice a year. For evaporative condensers, the frequency should be set by your risk assessment, taking account of the guidance. Either way, it goes in the written scheme.</li>
            <li><strong>Different people looking after it.</strong> Evaporative condensers are often maintained by refrigeration engineers rather than the building services team. Make sure someone's clearly responsible for the water side, not just the refrigerant side.</li>
          </ul>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a food distribution site with an evaporative condenser serving its cold rooms. The refrigeration contractor services the plant carefully, but water treatment has never been formally set up because everyone thought of it as "part of the fridge". There's no risk assessment covering it and it's never been notified. Getting it covered is simple: assess it, notify it, set up treatment and monitoring, and agree who does what between the refrigeration and water treatment contractors.</p>
          </div>

          <h2>And dry or adiabatic coolers?</h2>
          <p>A dry cooler with no water involved isn't a cooling tower or an evaporative condenser, so it's outside the notification regulations. Adiabatic and hybrid coolers sit in between. Some spray water onto pads or coils in hot weather, which can create aerosol in some designs. HSG274 Part 1 expects the Legionella risk from any unit that can produce spray to be assessed. If you're not sure where a unit sits, get competent advice rather than assuming.</p>

          <h2>How to tell what you've got</h2>
          <p>If you're not sure, a few quick questions usually settle it:</p>
          <ul>
            <li>Does water leave the unit and travel to equipment elsewhere on site? That's a cooling tower.</li>
            <li>Is there a coil inside with refrigerant or process fluid in it, and water sprayed over it? That's an evaporative condenser or closed-circuit cooler.</li>
            <li>Is there no water involved at all? That's a dry cooler.</li>
          </ul>
          <p>The nameplate and the manufacturer's literature will usually confirm it.</p>

          <h2>The bottom line</h2>
          <p>Whatever it's called, if it recirculates water and makes spray, it needs a <a href="{R}cooling-tower-legionella-risk-assessment.html">Legionella risk assessment</a>, a <a href="{R}cooling-tower-water-treatment.html">treatment programme</a>, monitoring and regular <a href="{R}cooling-tower-cleaning-disinfection.html">cleaning and disinfection</a>. We look after evaporative condensers as well as cooling towers, and we're happy to work alongside your refrigeration contractor. If you've got a unit you're not sure about, give us a ring.</p>
""",
        "cta_title": "Got an evaporative condenser nobody's quite sure about?",
        "cta_text": "Tell us what's on site. We'll help you work out what it is, what it needs and who should be looking after the water.",
    },
    # ------------------------------------------------------------------ 10
    {
        "slug": "cooling-tower-bleed-conductivity-control",
        "title": "Bleed-off and conductivity control: getting cycles of concentration right",
        "seo_title": "Cooling Tower Bleed-Off & Cycles of Concentration",
        "date": "2026-02-24",
        "desc": "What cycles of concentration mean, how bleed-off and conductivity control work, and what happens when the setpoint is too high or too low.",
        "tag": "Chemistry",
        "topic": "Cooling tower bleed and conductivity control",
        "services": ["chemical-dosing-biocide-control", "cooling-tower-water-treatment", "cooling-tower-monitoring-sampling"],
        "body": """
          <p>Of all the bits of kit on a cooling tower, the bleed valve gets the least love. It's a small solenoid valve and a probe, tucked away in the pipework, quietly letting water go to drain. But get it wrong and you'll either be pouring water and chemicals down the drain, or slowly scaling up the system and making life easier for bacteria.</p>
          <p>February is a good time to look at it. Loads are low, the tower's ticking over, and it's a sensible moment to check your setpoints before the summer heat arrives. Here's how it all works.</p>

          <h2>Why towers need bleeding at all</h2>
          <p>A cooling tower loses water by evaporation. But only the water evaporates. The dissolved minerals and salts that came in with the mains water stay behind. Top the tower up with fresh water, more minerals come in, more water evaporates, and the concentration keeps rising.</p>
          <p>Left alone, the water would eventually get so concentrated that minerals start coming out of solution as scale. Bleed-off (sometimes called blowdown) deliberately drains some of the concentrated water away so it can be replaced with fresher make-up water. That keeps the concentration where you want it.</p>

          <h2>What "cycles of concentration" means</h2>
          <p>Cycles of concentration is just a way of saying how concentrated the tower water is compared with the make-up water. It's usually worked out from conductivity, which goes up as dissolved solids go up.</p>
          <p>To keep the maths simple: if your make-up water reads 500 µS/cm and the tower water reads 2,000 µS/cm, the tower water is four times as concentrated, so you're running at four cycles. That's an illustration, not a target. The right number for your tower depends on your water and your treatment programme.</p>

          <h2>How conductivity control works</h2>
          <p>Most towers use a conductivity controller. A probe in the circulating water measures conductivity continuously. When it rises above a setpoint, the controller opens the bleed valve and concentrated water goes to drain. Make-up water comes in through the ball valve or level control to replace it, conductivity drops, and the bleed valve closes again.</p>
          <p>On many systems the inhibitor is dosed in proportion to make-up water, using a pulsing water meter, so as fresh water comes in, the right amount of inhibitor goes in with it. Biocide dosing is often linked to the bleed too, with the bleed locked out for a period after a shot dose so the biocide isn't drained away before it's had time to work. Those timings come from your treatment programme.</p>

          <h2>What happens when the setpoint is wrong</h2>
          <h3>Too high (not enough bleed)</h3>
          <ul>
            <li>Scale forms on heat exchangers, fill and pipework, cutting efficiency and raising energy use</li>
            <li>Deposits give bacteria somewhere to settle and make biocides less effective</li>
            <li>Corrosion can increase in some water chemistries</li>
            <li>Suspended solids build up, adding to sludge in the pond</li>
          </ul>
          <h3>Too low (too much bleed)</h3>
          <ul>
            <li>Water use and water bills go up</li>
            <li>Treatment chemicals go down the drain before they've done their job, so chemical costs go up too</li>
            <li>Inhibitor levels can drop if dosing doesn't keep pace</li>
          </ul>
          <p>The setpoint is a balance, and it should be set by whoever designs your treatment programme based on your make-up water quality (things like hardness and alkalinity) and the inhibitor you're using. Hard water areas, which include much of London and the South East, need particular care. Some sites soften the make-up water to allow more cycles.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Picture a tower where the conductivity controller shows a steady, healthy reading week after week. It all looks fine, but the water bill is creeping up and there's white scale appearing on the fill. A handheld meter tells a different story: the probe is coated and reading low, the actual conductivity is well above setpoint, and meanwhile the bleed valve has been opening at odd times. Cleaning and recalibrating the probe, and fixing the valve, gets things back where they should be.</p>
          </div>

          <h2>Simple checks you can build in</h2>
          <ol>
            <li><strong>Compare readings.</strong> Check the controller reading against a calibrated handheld meter regularly. If they disagree, believe the handheld and get the probe looked at.</li>
            <li><strong>Watch the bleed operate.</strong> Does the valve open when conductivity reaches the setpoint and close again afterwards? Is water running to drain when it shouldn't be?</li>
            <li><strong>Read the water meters.</strong> If you have meters on make-up and bleed, record them. Sudden changes in water use are an early sign of a problem.</li>
            <li><strong>Keep an eye on chemistry.</strong> Conductivity, pH, hardness and inhibitor levels, as your written scheme sets out. Our <a href="{R}cooling-tower-monitoring-sampling.html">monitoring</a> page covers the usual frequencies.</li>
            <li><strong>Look for scale.</strong> White or crusty deposits on the fill, pond walls or around the distribution are a visual clue that concentration has been too high.</li>
          </ol>
          <p>Record it all in the log book. As we said in our post on <a href="{R}blog/cooling-tower-log-book.html">what goes in a log book</a>, trends are where the value is.</p>

          <h2>Don't forget the low-load months</h2>
          <p>In winter, many towers run at low load. There's less evaporation, so less make-up, less bleed and less inhibitor going in if dosing is proportional to make-up. Biocide still needs to reach the whole system, and low flow can leave parts of it stagnant. It's worth checking with your treatment contractor that the programme still works at low load, not just in summer.</p>

          <h2>In short</h2>
          <p>Bleed control keeps the water from getting too concentrated, and the setpoint is a balance between scale and waste. Keep the probe clean and calibrated, check the valve works, and watch the trends. A stuck bleed valve is one of the classic causes of trouble, alongside the others in our post on <a href="{R}blog/cooling-tower-dosing-failures.html">dosing failures</a>. Our <a href="{R}chemical-dosing-biocide-control.html">dosing and control</a> service includes calibration and checks on every visit, and if you'd like your setpoints reviewed before summer, just ask.</p>
""",
        "cta_title": "Want your bleed and setpoints checked?",
        "cta_text": "We'll check the controller, probe and valve, compare the chemistry with your make-up water and suggest sensible setpoints.",
    },
    # ------------------------------------------------------------------ 11
    {
        "slug": "cooling-tower-handover-checklist",
        "title": "Taking over a site with cooling towers: a handover checklist",
        "seo_title": "Taking Over a Site With Cooling Towers: Handover Checklist",
        "date": "2026-05-13",
        "desc": "New FM contract, new lease or newly acquired site with cooling towers? A practical handover checklist covering records, roles, notification and the plant.",
        "tag": "Compliance",
        "topic": "Cooling tower site handover",
        "services": ["cooling-tower-log-books-compliance", "cooling-tower-legionella-risk-assessment", "cooling-tower-water-treatment"],
        "body": """
          <p>You've just taken over a site. Maybe it's a new facilities management contract, a new lease, or a building your company has bought. There's a lot to get your head around, and somewhere on the roof (or in the plant yard) there are cooling towers. They come with their own set of legal duties, and those duties don't pause while the handover is going on.</p>
          <p>Handovers are where things fall through the cracks. The outgoing team knew how it all worked, the paperwork was "somewhere", and the treatment contract ended on Friday. Here's a practical checklist to make sure your towers stay under control from day one.</p>

          <h2>First, work out who the duty holder is</h2>
          <p>Under ACOP L8, the duty to manage Legionella risk sits with the employer or the person in control of the premises. On a leased or managed site, that can be split between landlord, tenant and facilities manager, depending on the lease and contracts. Before anything else, get clear on who holds the duty for the cooling towers, and make sure it's written down. Everything else follows from that.</p>

          <h2>The handover checklist</h2>

          <h3>People and responsibilities</h3>
          <ul>
            <li>Has a responsible person been appointed to manage Legionella control, and a deputy? If the previous one has left with the outgoing contract, appoint a new one in writing.</li>
            <li>Do they have the training and authority to do the job?</li>
            <li>Who's the water treatment contractor? Is the contract continuing, ending or being retendered?</li>
          </ul>

          <h3>The plant</h3>
          <ul>
            <li>How many cooling towers and evaporative condensers are there, including standby, seasonal and "disused" units? Are the disused ones actually disconnected?</li>
            <li>Is there a schematic showing towers, pumps, dosing, bleed and sample points?</li>
            <li>What state is it all in? A walk-round with someone who knows towers is worth booking early.</li>
          </ul>

          <h3>Risk assessment and written scheme</h3>
          <ul>
            <li>Is there a current <a href="{R}cooling-tower-legionella-risk-assessment.html">Legionella risk assessment</a> covering the towers?</li>
            <li>Does it reflect the plant as it is now, and the current people and contracts? A change of management is itself a reason to review it.</li>
            <li>Is there a written scheme, and is anyone actually following it?</li>
            <li>Are actions from the last assessment closed out?</li>
          </ul>

          <h3>Records</h3>
          <ul>
            <li>Is there a log book, and is it complete? Look for weekly dip slides, chemistry, dosing checks, <em>Legionella</em> results from a UKAS-accredited lab, and corrective actions.</li>
            <li>When was the last clean and disinfection? Is there a certificate? HSG274 Part 1 expects cooling towers to be done at least twice a year.</li>
            <li>When was the last <em>Legionella</em> sample, and what did it show? Any recent high results, and were they followed up?</li>
          </ul>
          <p>Our post on <a href="{R}blog/cooling-tower-log-book.html">what should be in a cooling tower log book</a> is a useful companion here.</p>

          <h3>Notification</h3>
          <ul>
            <li>Is there a copy of the notification to the local authority under the Notification of Cooling Towers and Evaporative Condensers Regulations 1992?</li>
            <li>Is it in the right name and up to date? If control of the premises has changed, the council's record may need updating. See <a href="{R}blog/notifying-local-authority-cooling-tower.html">do you need to notify the council?</a></li>
          </ul>

          <h3>Chemicals and safety</h3>
          <ul>
            <li>What treatment chemicals are on site, and are there COSHH assessments and safety data sheets for them?</li>
            <li>Is chemical storage safe, bunded where needed and clearly labelled?</li>
            <li>Is there safe access to the towers, with any permits, working at height arrangements and isolations documented?</li>
          </ul>

          <h2>Avoid the gap</h2>
          <p>The single biggest risk at handover is a gap in service. The outgoing contractor's last visit is on the 28th, the new contractor's first visit is "sometime next month", and in between nobody is checking the dosing or taking dip slides. Plan it so there's no break: agree the end date of one contract and the start date of the next, make sure chemical stock won't run out in between, and get the records handed over before the outgoing team leaves.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a new FM provider starting on a multi-building site. The outgoing provider's treatment contract ends on the same day. The log book turns up a fortnight later, with the last month of entries missing and a cleaning certificate that's eight months old. The new team's first jobs are clear: get monitoring going straight away, book a clean, review the risk assessment and update the notification in the new duty holder's name.</p>
          </div>

          <h2>Your first 30 days</h2>
          <ol>
            <li>Confirm the duty holder and appoint the responsible person in writing.</li>
            <li>Make sure monitoring and dosing carry on without a break.</li>
            <li>Gather every record you can find and identify the gaps.</li>
            <li>Get a competent person to inspect the towers and the treatment kit.</li>
            <li>Book anything that's overdue, such as a clean, a <em>Legionella</em> sample or a risk assessment review.</li>
            <li>Update the local authority notification if needed.</li>
            <li>Brief site staff who'll be doing weekly checks, and give them simple record sheets.</li>
          </ol>

          <h2>How we can help</h2>
          <p>Taking on a new site is exactly when a fresh pair of eyes helps. We can audit the records, inspect the plant, review the risk assessment and set up a <a href="{R}cooling-tower-water-treatment.html">water treatment</a> and <a href="{R}cooling-tower-log-books-compliance.html">compliance</a> programme that starts on the right day. If you've just inherited some towers and you're not sure where you stand, give us a call.</p>
""",
        "cta_title": "Just inherited some cooling towers?",
        "cta_text": "We'll audit the records, look at the plant and give you a clear list of what needs doing first, with no gap in treatment.",
    },
    # ------------------------------------------------------------------ 12
    {
        "slug": "cooling-tower-heatwave-legionella-risk",
        "title": "Heatwaves and cooling towers: why hot spells test your controls",
        "seo_title": "Heatwaves and Cooling Towers: Managing Legionella Risk",
        "date": "2026-08-18",
        "desc": "Why hot weather puts cooling tower Legionella controls under pressure, what tends to go wrong in a heatwave and a practical checklist before the next one.",
        "tag": "Seasonal",
        "topic": "Cooling tower heatwave preparation",
        "services": ["cooling-tower-water-treatment", "chemical-dosing-biocide-control", "cooling-tower-monitoring-sampling"],
        "body": """
          <p>When the weather turns properly hot, everyone notices the air conditioning. Fewer people think about what's happening on the roof. But a heatwave is one of the toughest tests a cooling tower faces all year, and it's when small weaknesses in a treatment programme tend to show up.</p>
          <p>Here's why hot spells put pressure on Legionella control, what tends to go wrong, and how to get ready before the next one, whether that's next week or next summer.</p>

          <h2>Why heat matters</h2>
          <p><em>Legionella</em> bacteria grow best in water between roughly 20 and 45°C, which is the range ACOP L8 and HSG274 highlight. Cooling tower water sits in or near that range for much of its working life. In a heatwave, the water returning from the plant is warmer, the pond is warmer and the whole system spends more time in the zone bacteria like.</p>
          <p>At the same time, the tower is working harder than usual. That changes almost everything about how the treatment programme behaves.</p>

          <h2>What a heatwave does to your system</h2>
          <ul>
            <li><strong>More evaporation.</strong> The tower evaporates more water, so it needs more make-up water and the water concentrates faster. The bleed valve works harder to keep conductivity in check.</li>
            <li><strong>Chemicals get used faster.</strong> More make-up and more bleed mean more inhibitor and biocide going in. Drums that normally last a month can empty much sooner.</li>
            <li><strong>Higher biocide demand.</strong> Warm water and more organic material mean bacteria grow faster and use up biocide more quickly.</li>
            <li><strong>More dirt.</strong> Dry weather means more dust and pollen in the air, and the tower's moving more air through it. More debris ends up in the pond.</li>
            <li><strong>Fans at full speed.</strong> Towers running flat out move more air, so the drift eliminators are working harder too. Damaged or poorly fitted eliminators let more aerosol escape.</li>
            <li><strong>Standby units called into service.</strong> On sites with spare capacity, towers that have been sitting idle may be switched on to cope with the load. If they've been standing full of untreated water, that's a real risk.</li>
          </ul>

          <h2>What tends to go wrong</h2>
          <p>Put those together and the classic heatwave problems are:</p>
          <ul>
            <li>A chemical drum running dry earlier than expected, often over a weekend</li>
            <li>Bleed not keeping up, so the water over-concentrates and scale starts to form</li>
            <li>Dip slide counts stepping up as biocide levels struggle to keep pace</li>
            <li>A standby tower switched on without the checks it needed first</li>
          </ul>
          <p>None of these is unusual, and all of them can be prevented or caught early. We cover the common faults in our post on <a href="{R}blog/cooling-tower-dosing-failures.html">dosing failures</a>, and how to read rising counts in <a href="{R}blog/dip-slides-tvc-cooling-tower.html">dip slides and TVCs explained</a>.</p>

          <div class="callout">
            <span class="callout__k">A typical scenario</span>
            <p>Imagine a building where a long hot spell pushes the main tower hard for two weeks. The biocide drum, which usually lasts the whole month between service visits, runs out on day ten. Over the same period the facilities team switches on the standby tower to help with the load, straight from idle. A week later the dip slides from both towers are up. A pre-summer check, with extra chemical stock on site and a plan for the standby tower, would have headed off both problems.</p>
          </div>

          <h2>A pre-heatwave checklist</h2>
          <p>Ideally, do this in late spring, before the first hot week. If the forecast is already looking warm, do it now:</p>
          <ol>
            <li><strong>Check chemical stock.</strong> Make sure there's enough on site to cover heavier use, stored safely in line with the safety data sheets.</li>
            <li><strong>Check the dosing kit.</strong> Pumps primed and delivering, lines clear, controllers calibrated, bleed valve working.</li>
            <li><strong>Inspect the tower.</strong> Pond clean, fill in good condition, drift eliminators intact and properly seated.</li>
            <li><strong>Check when the last clean was.</strong> If a clean is due soon, consider doing it before the hot weather rather than in the middle of it.</li>
            <li><strong>Plan for standby units.</strong> If a standby tower might be needed, make sure it's been kept circulating with treatment, or cleaned and disinfected, so it's ready to run. See <a href="{R}blog/cooling-tower-start-up-after-shutdown.html">bringing a tower back after a shutdown</a>.</li>
            <li><strong>Agree extra checks.</strong> Your risk assessment may call for more frequent monitoring during periods of high load. Agree with your treatment contractor what that looks like.</li>
          </ol>

          <h2>During the heatwave</h2>
          <ul>
            <li>Check drum levels more often than usual, and before weekends.</li>
            <li>Keep weekly dip slides going without fail, and look at the trend, not just the number.</li>
            <li>Watch conductivity and make sure the bleed is coping.</li>
            <li>If something looks wrong, act on it quickly and record what you did.</li>
          </ul>
          <p>If a result comes back above an action level, follow your written scheme. Our guide to <a href="{R}blog/positive-legionella-result-cooling-tower.html">the first 48 hours after a positive result</a> walks through it.</p>

          <h2>After the hot spell</h2>
          <p>Once things cool down, take a look back. Did anything run out or fail? Did counts move? Is there more scale or sludge than before? If so, it might be time to bring a clean forward or review the treatment programme and risk assessment before next summer. With hot spells becoming a regular part of British summers, it's worth building heatwave planning into your written scheme rather than treating it as a one-off.</p>
          <p>Our <a href="{R}cooling-tower-water-treatment.html">water treatment</a> and <a href="{R}chemical-dosing-biocide-control.html">dosing</a> services include pre-summer checks as standard. If you'd like us to look over your system before the next heatwave, give us a ring.</p>
""",
        "cta_title": "Want your towers ready for the next hot spell?",
        "cta_text": "We'll check the dosing, chemical stock, bleed and tower condition, and agree a sensible monitoring plan for high-load periods.",
    },
]
