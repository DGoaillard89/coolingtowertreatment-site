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
]
