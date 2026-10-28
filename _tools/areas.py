"""Area landing pages (/areas/) and the areas hub.

Each area page must stay genuinely local: different sites, water, access and council notes per place.
Don't copy sentences between area pages, don't invent clients, local offices or response times.
Plain '&' in name/title/desc (escaped on output); HTML allowed in lede, body, towns and FAQ answers.
{R} in HTML is replaced with the relative root path ("../" from /areas/).
"""
import build as B

esc = B.esc

NOTIFY_REGS = "https://www.legislation.gov.uk/uksi/1992/2225/contents"
HSG274 = "https://www.hse.gov.uk/pubns/books/hsg274.htm"
TW_CHECKER = "https://www.thameswater.co.uk/help/water-and-waste-help/water-quality/check-your-water-quality"


def ext(url, text):
    return f'<a href="{url}" rel="noopener">{text}</a>'


AREAS = [
    # ------------------------------------------------------------------ London
    {
        "slug": "london",
        "name": "London",
        "ld_type": "City",
        "icon": "office",
        "code": "AREA · LDN",
        "title": "London Cooling Tower Water Treatment & Legionella Control",
        "desc": "Cooling tower and evaporative condenser treatment across London, from City rooftops to Docklands data halls. Based in Chiswick, W4.",
        "h1": "Cooling tower water treatment in London",
        "lede": "Rooftop towers in the City, hospital plant floors, Docklands data halls and cold stores in Park Royal. We're based in Chiswick, W4, and London is where most of our work happens.",
        "card": "City and West End rooftops, Docklands data halls, hospitals and industrial sites in all 32 boroughs and the Square Mile.",
        "body": f"""
          <h2>Where London's wet cooling lives</h2>
          <p>Most of London's cooling towers are hidden in plain sight. They sit on the roofs of City and West End office blocks, behind louvres on hospital plant floors, in basement plant rooms with ducted air paths, and on the podium decks of the bigger Canary Wharf buildings. Out in Park Royal, along the Lea Valley and beside the river in the east, you'll find the industrial side: food production, cold stores with evaporative condensers on the refrigeration plant, and warehouses that need chilled space all year.</p>
          <p>Then there are the data halls. Docklands has been a data centre hub for a long time, and there are more out west towards Hayes and Heathrow. Plenty of newer halls use dry or adiabatic coolers, but a good number still reject heat through open towers.</p>
          <p>Each setting changes how the job gets done. An office tower is usually close to openable windows, fresh-air intakes or a busy pavement, so drift control and a clean, well-treated pond matter to the people below. A hospital wants results passed straight to its Water Safety Group. A data hall wants every intervention booked through change control. We plan the programme around the building, not the other way round.</p>

          <h2>Hard London water and what it does to a tower</h2>
          <p>London's mains water is mostly hard to very hard. Thames Water supplies most of the capital, with Affinity Water in parts of the north and west, Essex &amp; Suffolk Water in parts of the east and SES Water in parts of the south. A lot of it starts life in the Thames, the Lee and the chalk, which is where the calcium comes from.</p>
          <p>In a cooling tower, that hardness concentrates every time water evaporates. Push the cycles of concentration too far and calcium carbonate plates out on condenser tubes and fill, cutting heat transfer and giving biofilm somewhere to hide. So London towers usually run at fewer cycles than a soft-water site could, which means more bleed, more make-up and a scale inhibitor matched to the water. Some buildings soften the make-up to claw back water savings, but fully softened water can be harder on some metals, so corrosion then needs a closer eye. Our article on <a href="{{R}}blog/cooling-tower-bleed-conductivity-control.html">bleed and conductivity control</a> explains the balance.</p>
          <p>We test your make-up water rather than assume. You can check the published hardness for your postcode with {ext(TW_CHECKER, "Thames Water's water quality checker")} or your own supplier's equivalent.</p>

          <h2>Getting to roof plant in the capital</h2>
          <p>Chiswick is on the western edge of inner London, so most sites are a short trip for us. The journey is rarely the hard part. Reaching the tower is. Expect us to ask about:</p>
          <ul>
            <li><strong>Roof access and permits.</strong> Many City towers are behind a locked hatch or plant-room door that needs a permit to work, a working-at-height plan and sometimes a check of the edge protection or fall-arrest system.</li>
            <li><strong>Goods lifts and loading bays.</strong> Treatment chemicals come in drums. In a tall building that means booking the goods lift and a loading-bay slot, and sometimes agreeing a route through the building with security.</li>
            <li><strong>Out-of-hours work.</strong> Cleans are noisy and wet, so some buildings prefer them at weekends or early in the morning before tenants arrive.</li>
            <li><strong>Parking and charges.</strong> Central London means controlled parking zones, the Congestion Charge and the ULEZ. We sort the route and parking before the visit so nobody's circling the block with a van full of chemicals.</li>
          </ul>
          <p>Send us your building's contractor rules and RAMS template up front and the first visit goes much more smoothly.</p>

          <h2>Notifying the council in London</h2>
          <p>The {ext(NOTIFY_REGS, "Notification of Cooling Towers and Evaporative Condensers Regulations 1992")} say you must tell the local authority, in writing, about every wet cooling tower and evaporative condenser on your premises. In London that means the borough council your site is in, or the City of London Corporation if you're in the Square Mile. Your local council's environmental health team is the place to start. Our guide to <a href="{{R}}blog/notifying-local-authority-cooling-tower.html">notifying the local authority</a> walks through what to send.</p>
""",
        "towns_h2": "London boroughs we cover",
        "towns": ["City of London", "Westminster", "Camden", "Islington", "Kensington &amp; Chelsea", "Hammersmith &amp; Fulham", "Hounslow", "Ealing", "Brent", "Hillingdon", "Harrow", "Barnet", "Haringey", "Enfield", "Hackney", "Tower Hamlets", "Waltham Forest", "Newham", "Redbridge", "Barking &amp; Dagenham", "Havering", "Greenwich", "Lewisham", "Southwark", "Lambeth", "Wandsworth", "Merton", "Sutton", "Croydon", "Bromley", "Bexley", "Kingston upon Thames", "Richmond upon Thames"],
        "towns_note": "That's every London borough plus the City. West London is on our doorstep; we plan routes into central and east London around traffic and parking.",
        "faqs": [
            ("Who do we notify about a cooling tower in London?",
             f"Your local council's environmental health team, for the borough your premises are in, or the City of London Corporation in the Square Mile. The {ext(NOTIFY_REGS, 'Notification of Cooling Towers and Evaporative Condensers Regulations 1992')} require written notification of each wet cooling tower and evaporative condenser on non-domestic premises, and you should tell them again if a unit is taken out of use."),
            ("Does London's hard water mean our tower needs more treatment?",
             "It usually means more careful scale control rather than simply more chemical. Hard water limits how many cycles of concentration a tower can safely run, so bleed rates are higher and the inhibitor has to suit the water. We set the conductivity setpoint from an analysis of your make-up water and check it on every visit."),
            ("Can you work on rooftop towers in occupied office buildings?",
             "Yes, that's most of our London work. We follow the building's permit-to-work and RAMS process, book goods lifts and loading bays in advance, and schedule cleans out of hours where the building manager prefers. Drift near windows and air intakes gets particular attention in the risk assessment."),
            ("Do you cover the whole of Greater London?",
             "Yes, every one of the 32 boroughs, plus the Square Mile. We're based in Chiswick, W4, so West London is close by, and we plan visits into central and east London around parking, the Congestion Charge zone and building access times."),
        ],
        "posts": ["notifying-local-authority-cooling-tower", "cooling-tower-bleed-conductivity-control", "cooling-tower-heatwave-legionella-risk"],
    },
    # ------------------------------------------------------------------ Thames Valley
    {
        "slug": "thames-valley-berkshire",
        "name": "Thames Valley & Berkshire",
        "ld_type": "AdministrativeArea",
        "ld_names": ["Berkshire", "Slough", "Reading", "Thames Valley"],
        "icon": "datacentre",
        "code": "AREA · M4",
        "title": "Slough & Berkshire Cooling Tower Treatment | Thames Valley",
        "desc": "Cooling tower water treatment for data centres, business parks and logistics in Slough, Reading and the Thames Valley. Up the M4 from Chiswick.",
        "h1": "Cooling tower treatment in Slough, Berkshire and the Thames Valley",
        "lede": "Data halls on the M4 corridor, campuses in Reading and Bracknell, cold stores by Heathrow. The M4 starts just down the road from our Chiswick office, so this patch is a straight run west.",
        "card": "Slough's data centre cluster, Reading and Bracknell business parks, and logistics around Colnbrook and Poyle.",
        "body": f"""
          <h2>The M4 corridor runs on cooling</h2>
          <p>Follow the M4 west out of London and you're soon in one of the busiest stretches of cooling plant in the country. Slough is one of the UK's best-known data centre clusters, with many halls on or near the Slough Trading Estate and new ones still being built. Reading, Bracknell and Maidenhead add business parks and corporate campuses running chilled-water systems, and the Heathrow side of the patch, around Colnbrook and Poyle, is full of warehousing and cold storage.</p>
          <p>Not every site here has an open tower. Lots of the newer halls use dry coolers or adiabatic units, and those still need a Legionella risk assessment if they wet a surface or make spray. {ext(HSG274, "HSG274 Part 1")} is clear that any unit able to produce aerosol needs its risk assessing. But open towers and evaporative condensers are still common on older halls, process sites and food distribution, and they're the ones that need a full treatment programme.</p>

          <h2>Working inside data centre change control</h2>
          <p>If you run a data hall you'll know the drill: method statements, change requests, approved windows, escorts and badge access. We work within it rather than around it. In practice that means:</p>
          <ul>
            <li>cleaning one cell or one tower at a time while the N+1 capacity carries the load,</li>
            <li>raising dosing changes and setpoint adjustments as changes, not quiet tweaks,</li>
            <li>taking samples at agreed times with escorts booked ahead,</li>
            <li>writing reports in a format your auditors and operations team already use.</li>
          </ul>
          <p>Vetting and inductions take time on a first visit, so we build them into the start of the programme. Our article on <a href="{{R}}blog/data-centre-cooling-tower-water-treatment.html">data centre water treatment</a> goes into more detail.</p>

          <h2>Water in the Thames Valley</h2>
          <p>Reading, Newbury and most of Maidenhead get their water from Thames Water. Slough is split, with Affinity Water serving parts of the town and its surroundings, and South East Water supplies parts of east Berkshire around Bracknell and Wokingham. Most of the area's water is hard, drawn from the Thames and the chalk. Your supplier's postcode checker will tell you which side of the line you're on.</p>
          <p>For a large data centre tower, hardness has a real cost. On a hot day evaporation is heavy, and every litre that goes up the stack leaves its calcium behind. Set the bleed too tight and you waste water and chemical. Set it too loose and condenser tubes scale up on plant you can't easily take offline. Many larger sites here soften or otherwise pre-treat the make-up. If yours does, the softener needs watching too, because one missed regeneration sends hard water into a system tuned for soft.</p>

          <h2>Notification in Berkshire</h2>
          <p>Berkshire has no county council. It's six unitary councils: Slough, Reading, Wokingham, Bracknell Forest, Windsor and Maidenhead, and West Berkshire. Notification under the {ext(NOTIFY_REGS, "1992 regulations")} goes to whichever one your site sits in, through your local council's environmental health team. On a campus with several towers, every one goes on the notice, and towers added during an expansion need notifying as well.</p>

          <h2>Getting there</h2>
          <p>From Chiswick we're on the M4 within minutes, which makes Slough and the Heathrow side easy to reach for routine visits, with Reading and Newbury further along the same road. Business parks usually have parking and ground-level plant yards. Data centres are the opposite: everything goes through the gatehouse, so we agree vehicle details and visit slots in advance.</p>
""",
        "towns_h2": "Towns we cover in the Thames Valley",
        "towns": ["Slough", "Langley", "Colnbrook", "Poyle", "Iver", "Windsor", "Maidenhead", "Reading", "Theale", "Wokingham", "Bracknell", "Ascot", "Twyford", "Newbury", "Thatcham", "Henley-on-Thames", "Marlow", "High Wycombe", "Beaconsfield", "Gerrards Cross"],
        "towns_note": "We cover all six Berkshire unitary areas plus south Buckinghamshire and the Henley side of Oxfordshire.",
        "faqs": [
            ("Can you treat data centre cooling towers in Slough without risking uptime?",
             "Yes. We plan cleans cell by cell or around N+1 capacity, raise dosing and setpoint changes through your change control, and book sampling visits and escorts in advance. Monitoring and records follow HSG274 Part 1, presented in a way your audit and operations teams can use."),
            ("Which council do we notify about a cooling tower in Slough or Reading?",
             f"The unitary council your site sits in, through its environmental health team. Berkshire has six: Slough, Reading, Wokingham, Bracknell Forest, Windsor and Maidenhead, and West Berkshire. The {ext(NOTIFY_REGS, 'Notification of Cooling Towers and Evaporative Condensers Regulations 1992')} require written notice of each wet tower and evaporative condenser."),
            ("Do adiabatic coolers on the M4 corridor need Legionella control?",
             f"If they spray water or wet a surface in the air stream, the risk needs assessing. {ext(HSG274, 'HSG274 Part 1')} asks you to check adiabatic and hybrid units against the definitions in the Notification Regulations, and to assess any unit that can make aerosol even if it isn't notifiable. We can help you work out where yours sit."),
            ("Is the water hard in Slough and Reading?",
             "Mostly, yes. Thames Water supplies much of the area and Affinity Water serves parts of Slough, and both draw heavily on the Thames and chalk. That limits safe cycles of concentration, so bleed control and inhibitor choice matter. Check your postcode with your supplier and we'll test the make-up on site."),
        ],
        "posts": ["data-centre-cooling-tower-water-treatment", "cooling-tower-dosing-failures", "cooling-tower-bleed-conductivity-control"],
    },
    # ------------------------------------------------------------------ Hertfordshire
    {
        "slug": "hertfordshire",
        "name": "Hertfordshire",
        "ld_type": "AdministrativeArea",
        "icon": "food",
        "code": "AREA · HERTS",
        "title": "Hertfordshire Cooling Tower Water Treatment & Legionella",
        "desc": "Cooling tower and evaporative condenser treatment for Hertfordshire distribution parks, labs, hospitals and offices, from Watford to Stevenage.",
        "h1": "Cooling tower water treatment in Hertfordshire",
        "lede": "Distribution parks off the M1 and M25, labs around Stevenage, hospitals and offices in Watford and St Albans. Plenty of evaporative cooling, and quite a lot of it on cold stores.",
        "card": "Distribution parks off the M1 and M25, cold store condensers, labs around Stevenage and offices in Watford and St Albans.",
        "body": f"""
          <h2>Cooling plant along the M1, M25 and A1(M)</h2>
          <p>Hertfordshire's wet cooling is spread out rather than clustered. The big distribution parks off the M1 and M25, such as the Maylands area of Hemel Hempstead and the sites around Hatfield and Welwyn, often have cold stores and chilled warehouses with evaporative condensers on the refrigeration plant. Stevenage and the towns along the A1(M) have a strong life sciences and engineering presence, with lab buildings that need steady temperature control. Add hospitals, college and university campuses, and office buildings in Watford and St Albans, and there's a lot of plant across the county.</p>

          <h2>Evaporative condensers on cold stores</h2>
          <p>Evaporative condensers are easy to overlook. Site teams tend to call it "the condenser on the cold store" rather than a cooling tower, but it carries the same Legionella risk and the same duties: it must be notified, treated, monitored and cleaned. Our article on <a href="{{R}}blog/cooling-tower-vs-evaporative-condenser.html">towers versus condensers</a> explains why.</p>
          <p>A few things make them trickier than a big tower. The water volume is small, so biocide and inhibitor levels move quickly and a dosing hiccup shows up fast. The coil runs hot, so in hard water scale can build on the tubes within weeks if bleed falls behind. And they often sit beside loading bays or yards where drivers wait with their windows down, which puts people right in the path of any drift.</p>

          <h2>Chalk water, consistently hard</h2>
          <p>Affinity Water supplies most of Hertfordshire, and a large share of its water comes from boreholes in the chalk. The result is hard water that tends to be fairly steady through the year. That steadiness is useful: once a bleed setpoint is right, it tends to stay right. The hardness itself still means conservative cycles of concentration and an inhibitor chosen to suit. A few fringe areas are supplied by neighbouring companies, so check with yours. If your site tops up from a private borehole instead of the mains, that water can be quite different and needs its own analysis before we set anything.</p>

          <h2>Getting on site</h2>
          <p>From Chiswick, most of the county is a straightforward run up the M25, M1 or A41, so regular visits are easy to keep to. Distribution sites bring their own rules: booked arrival slots, yard marshals, hi-vis, reversing lorries, and plant reached by ladder onto a gantry or the flat roof over the cold store. We do the site induction, stick to agreed walking routes and keep our van where the yard team wants it. Lab and hospital sites usually want RAMS and COSHH information in advance, which we send ahead of the first visit.</p>

          <h2>Who to notify in Hertfordshire</h2>
          <p>Hertfordshire has a county council and ten district and borough councils: Broxbourne, Dacorum, East Hertfordshire, Hertsmere, North Hertfordshire, St Albans, Stevenage, Three Rivers, Watford and Welwyn Hatfield. Environmental health sits with the district or borough, not the county, so that's who you notify under the {ext(NOTIFY_REGS, "Notification of Cooling Towers and Evaporative Condensers Regulations 1992")}. Your local council's environmental health team will have the form.</p>
""",
        "towns_h2": "Towns we cover in Hertfordshire",
        "towns": ["Watford", "Hemel Hempstead", "St Albans", "Harpenden", "Hatfield", "Welwyn Garden City", "Stevenage", "Hitchin", "Letchworth Garden City", "Baldock", "Royston", "Hertford", "Ware", "Bishop's Stortford", "Cheshunt", "Hoddesdon", "Borehamwood", "Potters Bar", "Rickmansworth", "Berkhamsted", "Tring"],
        "towns_note": "We also cover the neighbouring parts of Bedfordshire and Buckinghamshire.",
        "faqs": [
            ("Does an evaporative condenser on a cold store need notifying to the council?",
             f"Yes. The {ext(NOTIFY_REGS, 'Notification of Cooling Towers and Evaporative Condensers Regulations 1992')} cover evaporative condensers as well as cooling towers, so each one on your premises needs a written notification to the local authority. In Hertfordshire that's your district or borough council's environmental health team."),
            ("Who do we notify about a cooling tower in Hertfordshire?",
             "The district or borough council for your site, not Hertfordshire County Council. There are ten: Broxbourne, Dacorum, East Hertfordshire, Hertsmere, North Hertfordshire, St Albans, Stevenage, Three Rivers, Watford and Welwyn Hatfield. Contact your local council's environmental health team."),
            ("Is Hertfordshire water hard enough to cause scale in a cooling tower?",
             "Yes, without the right control. Most of the county gets hard water from the chalk, and evaporation concentrates it further. A sensible conductivity setpoint, working bleed and a matched scale inhibitor keep it in solution. Evaporative condensers, with their hot coils and small volumes, need watching most closely."),
            ("Can you work around delivery schedules at a distribution site?",
             "Yes. We book arrival slots, follow your yard rules and induction, and plan cleans for quieter periods so condensers can be taken out of service without affecting the cold chain. Routine visits are kept short and predictable."),
        ],
        "posts": ["cooling-tower-vs-evaporative-condenser", "cooling-tower-handover-checklist", "cooling-tower-dosing-failures"],
    },
    # ------------------------------------------------------------------ Surrey
    {
        "slug": "surrey",
        "name": "Surrey",
        "ld_type": "AdministrativeArea",
        "icon": "office",
        "code": "AREA · SURREY",
        "title": "Surrey Cooling Tower Water Treatment & Legionella Control",
        "desc": "Cooling tower water treatment for Surrey business parks, hospitals, campuses and hotels, from Staines and Woking to Guildford and Redhill.",
        "h1": "Cooling tower water treatment in Surrey",
        "lede": "Business parks and corporate campuses along the M3 and M25, research buildings around Guildford, hospitals and hotels across the county. Mostly comfort cooling, and mostly busy in summer.",
        "card": "Business parks along the M3 and M25, campuses around Guildford and Woking, hospitals, hotels and conference venues.",
        "body": f"""
          <h2>Business parks, campuses and hospitals</h2>
          <p>Surrey's cooling plant is mostly commercial. There are corporate headquarters and business parks along the M3 and M25 at places like Weybridge, Staines, Egham and Camberley, office and research buildings around Guildford, Woking, Leatherhead and Redhill, and a good spread of hospitals, private clinics, universities, hotels and conference venues. Most cool with chillers, and the larger sites reject heat through rooftop or ground-level towers.</p>
          <p>Surrey business parks have one particular quirk: the neighbours. Plenty of them back onto housing, footpaths or schools, and a tower in the corner of a car park can be closer to someone's garden than to the office it serves. That puts extra weight on drift eliminators in good condition, sensible siting notes in the risk assessment and treatment that keeps counts consistently low.</p>

          <h2>Comfort cooling and the winter lay-up</h2>
          <p>Many Surrey towers serve comfort cooling. They work hard from late spring to early autumn and may be turned down or switched off over winter, and that on-off pattern is where trouble tends to start. {ext(HSG274, "HSG274 Part 1")} expects a system idle for between a week and a month to be dosed and circulated at least weekly, and one idle for longer to be drained and properly recommissioned before it runs again. We write the lay-up and restart into your scheme so it isn't left to memory. Our post on <a href="{{R}}blog/cooling-tower-start-up-after-shutdown.html">restarting after a shutdown</a> covers the sequence.</p>
          <p>Cleaning frequency follows the same thinking. For a typical comfort-cooling tower, HSG274 Part 1 suggests at least twice a year as a guide, with the real figure set by inspection, your treatment history and the tower's surroundings. A park next to a building site or a busy road will foul faster than one surrounded by lawns. See <a href="{{R}}blog/how-often-should-a-cooling-tower-be-cleaned.html">how often a cooling tower should be cleaned</a>.</p>

          <h2>Four water suppliers, one county</h2>
          <p>Surrey is shared between several water companies. SES Water supplies much of the east, including Redhill, Reigate, Leatherhead and Dorking. Affinity Water covers parts of the north-west such as Woking, Staines and Chertsey. Thames Water and South East Water supply other parts of the county. Most of it is hard, but because two sites a few miles apart can be on different supplies, we never copy a setpoint from one Surrey site to the next. We test the make-up water at each, and you can check yours on your supplier's postcode checker.</p>

          <h2>Travel and access</h2>
          <p>From Chiswick, north and east Surrey are a short drive down the A316, A3 or M3, and the M25 takes us round to the rest. Access is often easier than in central London: there's usually parking on site and the tower may be at ground level behind a fenced compound. Roof-mounted units on older office buildings can still mean fixed ladders, hatches and a permit to work, so we check the arrangements before the first visit.</p>

          <h2>Notification in Surrey</h2>
          <p>Environmental health in Surrey is run by the district and borough councils, such as Guildford, Woking, Runnymede, Spelthorne, Elmbridge, Reigate and Banstead, and the others across the county. Under the {ext(NOTIFY_REGS, "Notification of Cooling Towers and Evaporative Condensers Regulations 1992")} you notify the council your premises are in. Contact your local council's environmental health team for the form.</p>
""",
        "towns_h2": "Towns we cover in Surrey",
        "towns": ["Guildford", "Woking", "Staines-upon-Thames", "Egham", "Chertsey", "Addlestone", "Weybridge", "Walton-on-Thames", "Esher", "Cobham", "Leatherhead", "Epsom", "Banstead", "Redhill", "Reigate", "Dorking", "Caterham", "Oxted", "Camberley", "Farnham", "Godalming", "Haslemere"],
        "towns_note": "We also cover the south-west London boroughs that border Surrey, such as Kingston, Sutton and Richmond.",
        "faqs": [
            ("Who do we tell about a cooling tower in Surrey?",
             f"Your local council's environmental health team, at the district or borough council for your site rather than Surrey County Council. The {ext(NOTIFY_REGS, 'Notification of Cooling Towers and Evaporative Condensers Regulations 1992')} require written notice of each wet cooling tower and evaporative condenser on the premises."),
            ("Our tower is only used in summer. What should happen over winter?",
             f"It needs a plan, not just an off switch. {ext(HSG274, 'HSG274 Part 1')} expects a system idle for a week to a month to be dosed and circulated at least weekly, and one off for longer to be drained, cleaned and recommissioned before restart. We write this into your scheme and handle the spring restart."),
            ("How often should an office cooling tower in Surrey be cleaned?",
             "As often as it fouls. For comfort cooling, HSG274 Part 1 gives at least twice a year as a typical guide, but the frequency should come from inspections and your risk assessment. A tower near construction work or a main road may need cleaning more often."),
            ("Which water company supplies our Surrey site?",
             "It depends where you are. Four companies share Surrey between them (SES Water, Affinity Water, Thames Water and South East Water), and most of what they supply is hard. Check your supplier's postcode checker, and we'll test the make-up water ourselves before setting the treatment."),
        ],
        "posts": ["cooling-tower-start-up-after-shutdown", "how-often-should-a-cooling-tower-be-cleaned", "notifying-local-authority-cooling-tower"],
    },
    # ------------------------------------------------------------------ Kent
    {
        "slug": "kent",
        "name": "Kent",
        "ld_type": "AdministrativeArea",
        "icon": "factory",
        "code": "AREA · KENT",
        "title": "Kent Cooling Tower Water Treatment & Legionella Control",
        "desc": "Cooling tower and evaporative condenser treatment for Kent warehouses, packhouses, factories and hospitals, from Dartford to Dover.",
        "h1": "Cooling tower water treatment in Kent",
        "lede": "Warehouses and industry at the Thames Gateway end, engineering in the Medway towns, packhouses and cold stores across the county, and coastal sites where salt gets into the water.",
        "card": "Thames Gateway warehouses, Medway industry, fruit packhouses and cold stores, and coastal sites dealing with salt air.",
        "body": f"""
          <h2>From the Thames Gateway to the coast</h2>
          <p>Kent's cooling plant follows its industry. In the north-west, around Dartford, Ebbsfleet and Gravesend, there are large warehouses, industrial units and business parks serving London. The Medway towns have engineering and manufacturing sites. Across the county there are fruit packhouses, cold stores and food processors, many with refrigeration plant that rejects heat through evaporative condensers. Then add the hospitals, business parks such as Kings Hill and those around Ashford, and port-related logistics near Dover and along the estuary.</p>

          <h2>Sea air and salt</h2>
          <p>Coastal and estuary sites have a problem inland towers don't: salt. A tower near the sea pulls salt-laden air through its fill, which raises the chloride level in the water and makes corrosion more likely, especially on galvanised casings and older steelwork. It also pushes conductivity up, which can fool a bleed controller set purely on conductivity into dumping more water than it needs to. On coastal sites we add chloride checks to routine testing and choose the inhibitor with that in mind.</p>

          <h2>Packhouses and seasonal peaks</h2>
          <p>Fruit and food sites often run hardest during harvest and the months after, when the cold stores are full. That's when an evaporative condenser carries its heaviest load, and when a failed dosing pump or an empty biocide drum would do the most harm. So we plan cleans and bigger jobs for the quieter part of the year, check more closely through the peak, and make sure someone on site knows what the weekly checks are looking for. Our guide to <a href="{{R}}blog/dip-slides-tvc-cooling-tower.html">dip slides and TVCs</a> is a good starting point for site teams.</p>

          <h2>Water supply in Kent</h2>
          <p>Southern Water and South East Water supply much of Kent, with Affinity Water around Folkestone and Dover and SES Water in a small part of the west. Much of it is pumped from the chalk under the North Downs and East Kent, and it's generally hard. Hard make-up plus a hot condenser coil is a classic recipe for scale, so bleed control has to keep up. If you're not sure which company you're with, the water bill or a postcode search on the supplier's website will settle it. Some farms and factories also draw from their own boreholes, and that water needs testing in its own right.</p>

          <h2>Getting around the county</h2>
          <p>Kent is big, and east Kent is a fair drive from Chiswick, so we plan visits in runs and agree regular days with each site. The M25, M20, M2 and A2 do most of the work, with the Dartford Crossing for anything coming from Essex. When cross-Channel traffic backs up, Operation Brock can slow the M20, so we allow extra time for east Kent visits. That's our planning problem to solve, not something that changes what your scheme requires.</p>

          <h2>Notifying the council in Kent</h2>
          <p>Kent has twelve district, borough and city councils, plus Medway Council, a unitary authority covering Chatham, Rochester, Gillingham and Strood. Notification under the {ext(NOTIFY_REGS, "Notification of Cooling Towers and Evaporative Condensers Regulations 1992")} goes to the council your premises are in, through its environmental health team. That applies at port and industrial sites too, even where HSE rather than the council enforces health and safety.</p>
""",
        "towns_h2": "Towns we cover in Kent",
        "towns": ["Dartford", "Swanley", "Gravesend", "Ebbsfleet", "Sevenoaks", "Tonbridge", "Tunbridge Wells", "West Malling", "Maidstone", "Chatham", "Rochester", "Gillingham", "Sittingbourne", "Faversham", "Canterbury", "Whitstable", "Herne Bay", "Margate", "Ramsgate", "Ashford", "Folkestone", "Dover"],
        "towns_note": "We also cover the south-east London boroughs next door, such as Bexley and Bromley.",
        "faqs": [
            ("Does a coastal cooling tower need different water treatment?",
             "Often, yes. Salt-laden air raises chloride levels in the circulating water, which increases corrosion risk and pushes conductivity up. We add chloride checks on coastal and estuary sites, choose an inhibitor that copes with it and make sure the bleed setpoint reflects what's really in the water."),
            ("Do evaporative condensers on fruit cold stores need Legionella control?",
             f"Yes. They create spray and warm water just like a cooling tower, so ACOP L8 and {ext(HSG274, 'HSG274 Part 1')} apply. That means a risk assessment, a written scheme, treatment, monitoring, cleaning and notification to the local council. Small water volumes mean dosing problems show up fast, so weekly checks matter."),
            ("Who do we notify about a cooling tower in Medway or elsewhere in Kent?",
             "Your local council's environmental health team. In Chatham, Rochester, Gillingham and Strood that's Medway Council; elsewhere it's the district, borough or city council for your site, not Kent County Council. Notification is in writing and covers each tower and evaporative condenser."),
            ("Do you cover east Kent as well as the Dartford end?",
             "Yes. We cover all of Kent, travelling out from Chiswick. Sites further east are visited on planned days, and we build travel time, including the M20 when Operation Brock is in place, into our schedule rather than yours."),
        ],
        "posts": ["cooling-tower-vs-evaporative-condenser", "dip-slides-tvc-cooling-tower", "positive-legionella-result-cooling-tower"],
    },
    # ------------------------------------------------------------------ Essex
    {
        "slug": "essex",
        "name": "Essex",
        "ld_type": "AdministrativeArea",
        "icon": "contractor",
        "code": "AREA · ESSEX",
        "title": "Essex Cooling Tower Water Treatment & Legionella Control",
        "desc": "Cooling tower and evaporative condenser treatment for Essex ports, cold stores, factories and offices, from Thurrock to Chelmsford and Harlow.",
        "h1": "Cooling tower water treatment in Essex",
        "lede": "Port-side warehouses and cold stores in Thurrock, industrial estates in Basildon and Harlow, offices and hospitals in Chelmsford and Southend. In one of the driest parts of the country, with hard water to match.",
        "card": "Thurrock ports and cold stores, Basildon and Harlow industry, Stansted logistics, and offices and hospitals in Chelmsford and Southend.",
        "body": f"""
          <h2>Ports, logistics and a lot of cold storage</h2>
          <p>South Essex along the Thames is one of the busiest logistics areas in the south-east, with the ports at Tilbury and London Gateway and the warehouses that gather around them in Thurrock. A good share of that space is chilled or frozen, and the refrigeration plant behind it often uses evaporative condensers. Further in, there are industrial estates around Basildon, Harlow and Chelmsford, logistics near Stansted Airport, and hospitals, universities and office buildings in Chelmsford, Southend, Colchester and Brentwood.</p>

          <h2>A dry county with hard water</h2>
          <p>Essex is one of the driest parts of the UK, so the water a cooling tower uses gets more attention here than in most places. Towers lose water three ways: evaporation, drift and bleed. Evaporation is the job the tower is there to do, and drift should be tiny if the eliminators are in good order. Bleed is the one you can adjust, and it's tempting to cut it right back.</p>
          <p>The catch is that Essex water is generally hard, and squeezing too many cycles out of hard water is a quick route to scale. The sensible approach is to find the highest cycles of concentration your water and inhibitor can safely support, keep the conductivity probe clean and calibrated, and fix leaks and overflows that waste water without doing anything useful. If water use matters for your sustainability reporting, we can record make-up and bleed meter readings on every visit so you have real figures. Our article on <a href="{{R}}blog/cooling-tower-bleed-conductivity-control.html">cycles of concentration</a> explains the trade-off.</p>

          <h2>Who supplies your water</h2>
          <p>Essex &amp; Suffolk Water serves much of south and central Essex. Anglian Water supplies much of the north, including Colchester. Affinity Water covers parts of the west around Harlow, Epping and Saffron Walden, and an area in the north-east around Manningtree. Hardness and chemistry vary between them, so check your supplier's postcode checker and expect us to test the make-up water on site before setting a programme.</p>

          <h2>Getting to Essex sites</h2>
          <p>We reach Essex from Chiswick on the M25, then the A13 for Thurrock and Southend, the A12 for Chelmsford and Colchester, or the M11 for Harlow and Stansted. Port and terminal sites run their own security, pass and induction systems, so we book these early and send RAMS and COSHH information ahead. Cold stores bring their own hazards for an engineer: refrigeration plant rooms, forklift traffic and ladders up to condensers on a roof or gantry. We follow the site's rules on all of it.</p>

          <h2>Notification in Essex</h2>
          <p>Essex has a county council, twelve district, borough and city councils, and two unitary councils, Southend-on-Sea and Thurrock. Environmental health sits with the district, borough, city or unitary council, so that's who gets your written notification under the {ext(NOTIFY_REGS, "Notification of Cooling Towers and Evaporative Condensers Regulations 1992")}. Contact your local council's environmental health team for the form, and keep a copy in your <a href="{{R}}blog/cooling-tower-log-book.html">log book</a>.</p>
""",
        "towns_h2": "Towns we cover in Essex",
        "towns": ["Thurrock", "Grays", "Tilbury", "Stanford-le-Hope", "Basildon", "Billericay", "Wickford", "Brentwood", "Southend-on-Sea", "Rayleigh", "Canvey Island", "Chelmsford", "Witham", "Braintree", "Maldon", "Colchester", "Harwich", "Clacton-on-Sea", "Harlow", "Epping", "Loughton", "Saffron Walden", "Stansted"],
        "towns_note": "We also cover the east London boroughs on the Essex border, such as Havering and Redbridge.",
        "faqs": [
            ("Can we cut our cooling tower's water use in Essex without causing scale?",
             "Usually a bit, but not by simply closing the bleed. Essex water is generally hard, so the safe number of cycles is limited. We work out the highest cycles your water and inhibitor will support, keep the conductivity control accurate and look for leaks and overflows, which often waste more water than the bleed."),
            ("Who do we notify about a cooling tower in Thurrock or Southend?",
             "Thurrock Council or Southend-on-Sea City Council, through their environmental health teams, as both are unitary authorities. Elsewhere in Essex it's the district, borough or city council for your site, not Essex County Council. Notification is in writing and covers each tower and evaporative condenser."),
            ("Do you work on port and terminal sites?",
             "Yes. We complete the site's induction and pass process, send RAMS and COSHH information in advance and work within its permit system. Evaporative condensers on port-side cold stores get the same treatment, monitoring and cleaning as any other unit under ACOP L8 and HSG274 Part 1."),
            ("Which water company supplies our site in Essex?",
             "Essex &amp; Suffolk Water, Anglian Water or Affinity Water, depending on where you are. Each one has a postcode checker on its website. Most Essex water is hard, and we test the make-up water at your site before setting a treatment programme."),
        ],
        "posts": ["cooling-tower-bleed-conductivity-control", "cooling-tower-log-book", "cooling-tower-vs-evaporative-condenser"],
    },
]

AREA_BY_SLUG = {a["slug"]: a for a in AREAS}

WIDER = ["Buckinghamshire", "Oxfordshire", "Bedfordshire", "Hampshire", "West Sussex", "East Sussex", "Cambridgeshire", "Suffolk",
         "Northamptonshire", "The Midlands", "The North West", "Yorkshire", "The North East", "The South West", "Wales", "Scotland"]


def where_line(root):
    """Short 'Where we work' line for service pages."""
    links = ", ".join(f'<a href="{root}areas/{a["slug"]}.html">{esc(a["name"])}</a>' for a in AREAS[:-1])
    last = AREAS[-1]
    return (f'        <p class="where-line"><strong>Where we work:</strong> we cover the whole UK from our base in Chiswick, with most of our work in '
            f'{links} and <a href="{root}areas/{last["slug"]}.html">{esc(last["name"])}</a>. '
            f'<a href="{root}areas/">See all areas we cover</a>.</p>')


def _area_ld(a):
    names = a.get("ld_names", [a["name"]])
    t = a["ld_type"]
    return [{"@type": t, "name": n} for n in names] if len(names) > 1 else {"@type": t, "name": names[0]}


def build_area(a):
    root = "../"
    path = f'areas/{a["slug"]}.html'
    crumbs = [("Home", ""), ("Areas we cover", "areas/"), (a["name"], None)]
    topic = f'Cooling tower treatment, {a["name"]}'
    body = a["body"].replace("{R}", root)
    aside_links = "\n".join(
        f'            <li><a href="{root}{s["slug"]}.html">{B.icon(s["icon"], root)}{esc(s["short"])}</a></li>' for s in B.SERVICES
    )
    towns = "".join(f"<li>{t}</li>" for t in a["towns"])
    faqs = [(q, ans.replace("{R}", root)) for q, ans in a["faqs"]]
    posts = [B.POST_BY_SLUG[s] for s in a["posts"] if s in B.POST_BY_SLUG]
    others = " · ".join(f'<a href="{root}areas/{o["slug"]}.html">{esc(o["name"])}</a>' for o in AREAS if o["slug"] != a["slug"])
    main = f"""{B.page_hero(crumbs, "Area", a["h1"], a["lede"], root, a["icon"], a["code"], topic)}

    <section class="section section--white">
      <div class="wrap article-layout">
        <article class="article">
{body}
        </article>
        <aside class="aside-box" aria-labelledby="aside-title">
          <h2 id="aside-title">Our services</h2>
          <ul>
{aside_links}
          </ul>
          <div class="aside-phone">Got plant in {esc(a["name"])}? Call <a href="{B.TEL}">{B.PHONE}</a>
            <button class="btn btn--dark" type="button" data-open-enquiry="{esc(topic)}">Ask for a quote</button>
          </div>
        </aside>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Coverage</span>
          <h2>{a["towns_h2"]}</h2>
          <p>We're based in Chiswick, W4, and visit sites here from there. {a["towns_note"]}</p>
        </div>
        <ul class="areas areas--plain">{towns}</ul>
        <p>Other areas: {others} · <a href="{root}areas/">All areas</a></p>
      </div>
    </section>

    <section class="section section--white">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">Questions</span>
          <h2>Cooling towers in {esc(a["name"])}: common questions</h2>
        </div>
{B.faq_block(faqs)}
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <h2 class="block-title">Related articles</h2>
{B.post_cards(posts, root)}
      </div>
    </section>

{B.cta_band(root, f"Looking after cooling towers in {esc(a['name'])}?", "Tell us about your site and system and we'll come back with a clear, itemised quote and an honest view of what it needs.", topic)}"""
    service_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f'Cooling tower water treatment in {a["name"]}',
        "serviceType": "Cooling tower and evaporative condenser water treatment",
        "description": a["desc"],
        "url": B.url_for(path),
        "areaServed": _area_ld(a),
        "provider": {"@id": B.DOMAIN + "/#business"},
    }
    lds = [service_ld, B.breadcrumb_ld([("Home", ""), ("Areas we cover", "areas/"), (a["name"], path)]), B.faq_ld(faqs)]
    B.page(path, a["title"], a["desc"], path, main, "areas", lds, root)
    return path


def build_areas_hub():
    root = "../"
    crumbs = [("Home", ""), ("Areas we cover", None)]
    cards = "\n".join(
        f"""          <a class="service" href="{a["slug"]}.html">
            <span class="service__top">{B.icon(a["icon"], root)}<span class="service__num">{a["code"].split("· ")[1]}</span></span>
            <h3>{esc(a["name"])}</h3>
            <p>{a["card"]}</p>
            <span class="link-arrow">Cooling towers in {esc(a["name"])}</span>
          </a>"""
        for a in AREAS
    )
    wider = "".join(f"<li>{w}</li>" for w in WIDER) + "<li>Anywhere else in the UK</li>"
    main = f"""{B.page_hero(crumbs, "Areas", "Areas we cover", "We look after cooling towers and evaporative condensers right across the UK. London and the Home Counties are our speciality, and everything starts from our base in Chiswick, W4.", root, "tower", "AREAS", "Coverage enquiry")}

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <span class="eyebrow">London and the Home Counties</span>
          <h2>Where most of our work happens</h2>
          <p>These are the areas we know best. Each page covers the kind of sites that run wet cooling there, the local water, getting access to the plant and who to notify.</p>
        </div>
        <div class="services services--areas">
{cards}
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="wrap local">
        <div>
          <span class="eyebrow">UK-wide</span>
          <h2>Further afield</h2>
          <p>Coverage is UK-wide. If you manage plant in several regions, one contractor for the lot keeps treatment, records and reporting consistent, and the standards are the same wherever the tower is: ACOP L8, HSG274 Part 1 and a log book that's always up to date.</p>
          <ul class="areas areas--plain">{wider}</ul>
          <p>Not sure whether we cover your site? Call us or send a postcode through the form and we'll tell you straight.</p>
        </div>
        <div class="contact-card">
          <h3>Talk to an engineer</h3>
          <dl>
            <div><dt>Phone</dt><dd><a class="big-phone" href="{B.TEL}">{B.PHONE}</a></dd></div>
            <div><dt>Office</dt><dd><address>The Lightbox G16, 111 Power Road<br />Chiswick, London W4 5PY</address></dd></div>
            <div><dt>Coverage</dt><dd>UK-wide, specialising in London &amp; the Home Counties</dd></div>
          </dl>
          <button class="btn btn--primary" type="button" data-open-enquiry="Coverage enquiry">Request a quote</button>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <h2 class="block-title">Popular services</h2>
{B.related_services(["cooling-tower-water-treatment", "cooling-tower-cleaning-disinfection", "cooling-tower-monitoring-sampling", "cooling-tower-legionella-risk-assessment"], root)}
        <p class="where-line"><a href="{root}services.html">See all eight services</a></p>
      </div>
    </section>

{B.cta_band(root)}"""
    lds = [
        B.breadcrumb_ld([("Home", ""), ("Areas we cover", "areas/")]),
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "Areas we cover",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": a["name"], "url": B.url_for(f'areas/{a["slug"]}.html')} for i, a in enumerate(AREAS)
            ],
        },
    ]
    B.page("areas/index.html", "Areas We Cover | Cooling Tower Treatment, UK-Wide",
           "Cooling tower water treatment UK-wide, specialising in London, Thames Valley, Hertfordshire, Surrey, Kent and Essex. Based in Chiswick, W4.",
           "areas/", main, "areas", lds, root)
