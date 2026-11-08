"""Seed content, part 1: Import, Export, General Merchant, General Contractor,
Travel & Tours, Immigration Consultancy.

Edit freely, or change the same text later from the Django admin.
Regulatory details change; always confirm current requirements at engagement.
"""

SERVICES_PART1 = [
    # ------------------------------------------------------------------ IMPORT
    {
        "title": "Import Services",
        "slug": "import-services",
        "icon": "🚢",
        "order": 1,
        "tagline": "Source, ship and clear goods into Nigeria without the headaches.",
        "summary": "From supplier sourcing and documentation to freight, customs clearance and last-mile delivery, we manage the full import chain for businesses and individuals.",
        "overview": """Importing into Nigeria can be a rewarding way to access quality goods, machinery, raw materials and consumer products that are not available locally, or that are available only at much higher prices. It can also be a maze of paperwork, regulatory approvals, port procedures, shipping timelines and costs that surprise first-time importers. Our import service exists to take that complexity off your shoulders so you can focus on selling, using or distributing what you bring in.

We work with importers at every stage: individuals buying a single container of goods for resale, established companies replenishing stock on a schedule, and foreign manufacturers who want a reliable local partner to receive and distribute their products in Nigeria. Whether your cargo is coming from China, India, Europe, the Middle East, the Americas or another African market, we help you plan the route, choose sensible shipping terms and anticipate the costs before money changes hands.

Our approach is practical and transparent. Before you pay a supplier, we help you check that the supplier is genuine, that the goods can lawfully enter Nigeria, and that the landed cost still leaves you a healthy margin. During shipment we keep you informed at each milestone. On arrival we coordinate with licensed clearing and forwarding agents, port and terminal operators, inspection services and transporters so that your cargo moves from the port to your warehouse or shop as smoothly as possible.

Because we also operate in general merchandise, FMCG, wines and spirits and pharmaceuticals, we understand the specific rules attached to regulated product categories, such as agency registrations and permits, and we can guide you on what to prepare before the goods leave the supplier's warehouse rather than after they arrive at the port.""",
        "offerings": """Supplier identification, verification and negotiation support
Product eligibility checks and import-permit guidance
Pro-forma invoice review and landed-cost estimates
Guidance on Form M and other pre-shipment documentation through your bank
Sea freight (FCL and LCL) and air freight coordination
Marine cargo insurance arrangements
Customs clearance through licensed agents and duty guidance
Port, terminal and inspection coordination
Inland haulage and last-mile delivery to your warehouse or shop
Regulatory guidance for NAFDAC, SON and other agency-controlled goods
Ongoing sourcing programmes for repeat importers""",
        "process": """Discovery call|We learn what you want to import, quantities, budget, timeline and your destination within Nigeria.
Sourcing and checks|We help identify and verify suppliers, compare quotations and confirm the goods can lawfully be imported.
Costing and documents|We prepare a landed-cost estimate and guide you through the required pre-shipment documentation.
Shipping|We coordinate freight, insurance and shipment tracking, keeping you updated on each milestone.
Clearance|Licensed agents clear your cargo with customs and other agencies, with us supervising the process.
Delivery|Goods are transported from the port to your chosen location, with a final handover and document pack.""",
        "audience": """First-time importers who want guidance from start to finish
Retailers and wholesalers restocking on a regular schedule
Contractors and factories importing machinery, equipment and spare parts
Foreign suppliers seeking a dependable local receiving partner
Individuals importing personal or household goods""",
        "faqs": [
            ("Do I need a company to import goods into Nigeria?", "Commercial importation is normally done through a registered business with the relevant tax registrations. If you do not have one yet, we can help you register a business first through our business registration service, then proceed with your import."),
            ("Can you help me avoid fake suppliers?", "We cannot offer a guarantee against every risk, but we follow a verification process: checking the supplier's business records, requesting product samples and references where possible, and recommending safer payment structures instead of paying the full amount upfront to an unknown party."),
            ("How long does an import take?", "It depends on the origin, the shipping method and how quickly documents and approvals are in place. Sea freight is generally slower and cheaper than air freight. We give you a realistic timeline for your specific shipment at the costing stage."),
            ("Can you handle regulated goods such as drugs, food or alcohol?", "Yes, we can guide you through the extra registrations and permits that regulated goods require. See our FMCG, Wines & Spirits and Pharma pages for details."),
        ],
    },
    # ------------------------------------------------------------------ EXPORT
    {
        "title": "Export Services",
        "slug": "export-services",
        "icon": "📦",
        "order": 2,
        "tagline": "Take Nigerian and African products to buyers around the world.",
        "summary": "We help producers and traders prepare, certify, package and ship products to international buyers while meeting export compliance requirements.",
        "overview": """Nigeria and the wider African continent produce commodities and goods that the world wants: agricultural produce, solid minerals, processed foods, leather, textiles, handcrafts, cocoa, sesame, cashew, ginger, hibiscus flowers, shea products and much more. Turning that potential into real export revenue, however, requires more than a good product. Buyers expect consistent quality, proper packaging, correct paperwork, reliable delivery dates and compliance with the rules of their own country as well as Nigerian export regulations.

Our export service helps producers, cooperatives, small manufacturers and trading companies bridge that gap. We start by understanding what you produce, in what volume and to what standard. We then help you identify target markets and genuine buyers, align your product with the buyer's specifications, and prepare the commercial and regulatory documents the shipment needs.

We pay particular attention to the issues that cause rejected shipments and delayed payments: moisture levels and quality grading for agricultural goods, product testing and certification, labelling and packaging for the destination market, and clear commercial terms. We also advise on secure payment methods so that you are not exposed to unnecessary risk when dealing with a buyer you have not met in person.

For foreign buyers, we act as your trusted local partner on the ground: aggregating products from verified farms and producers, inspecting goods before loading, arranging export documentation and coordinating shipment so that what you ordered is what arrives at your port.""",
        "offerings": """Market and buyer identification support
Product and packaging readiness reviews
Guidance on export registrations, permits and certifications
Documentation: commercial invoice, packing list, certificate of origin and others as required
Aggregation and sourcing of agro-commodities from verified producers
Pre-shipment inspection and quality control coordination
Freight forwarding, container booking and customs export processing
Guidance on secure international payment methods
Export-proceeds and Nigerian export documentation guidance
Local representation for foreign buyers purchasing from Nigeria and Africa""",
        "process": """Product review|We assess your product, capacity, quality level and certifications you already hold.
Market matching|We help you identify suitable markets and buyers and understand their requirements.
Compliance|We guide you through registrations, testing, certifications and labelling needed for your product and destination.
Packing and inspection|Goods are packed to export standard and inspected before they are loaded.
Shipping and documents|We coordinate freight, customs export procedures and the full document pack.
Payment follow-up|We guide you through receiving payment securely and completing export documentation.""",
        "audience": """Farmers, cooperatives and agro-processors ready to sell abroad
Small and medium manufacturers entering export markets
Traders aggregating commodities for international buyers
Foreign buyers looking for reliable sourcing partners in Nigeria and Africa
Artisans and craft producers targeting overseas customers""",
        "faqs": [
            ("Do I need a licence to export from Nigeria?", "Most exporters register their business and obtain the relevant export registrations, and some products need additional permits or certifications. We will tell you what applies to your particular product and destination."),
            ("Can you find buyers for me?", "We help you reach and screen potential buyers and present your product properly. We cannot promise a sale, because that depends on price, quality and market demand, but we can improve your chances through preparation and the right introductions."),
            ("How do I protect myself from non-paying buyers?", "We recommend secure payment structures, such as letters of credit or staged payments, and proper documentation rather than shipping goods on trust alone."),
            ("Can you ship small quantities?", "Yes, for suitable products we can arrange air freight, groupage or consolidated shipments, although unit costs are normally lower at larger volumes."),
        ],
    },
    # ------------------------------------------------------------------ GENERAL MERCHANT
    {
        "title": "General Merchant",
        "slug": "general-merchant",
        "icon": "🏪",
        "order": 3,
        "tagline": "One reliable supplier for a wide range of goods and commodities.",
        "summary": "A broad trading service: we source, supply and deliver general goods, equipment and commodities to businesses, institutions and individuals.",
        "overview": """A general merchant is, at its heart, a problem solver: someone who finds what you need, from a trusted source, at a fair price, and gets it to you when you need it. Our general merchant service covers a wide range of goods and supplies, which means that instead of managing a dozen different vendors, you can come to one point of contact and let us handle the sourcing, negotiation, quality checks and delivery.

Our clients include companies that need office and industrial supplies, institutions that require bulk purchases, contractors who need building and finishing materials, retailers who want to broaden their stock, and foreign firms who need someone in Nigeria to procure on their behalf. If you can describe the item, the specification and the quantity, we will go and find the best way to supply it.

Because trading is a relationship business, we focus on reliability. We confirm specifications before purchase, inspect goods where appropriate, agree clear prices and delivery schedules in writing, and keep you informed about anything that could change timing or cost. Where it makes sense, we combine this service with our import, export and contracting services, so you can source internationally, clear goods at the port and have them delivered to a job site under one coordinated arrangement.

We also offer ongoing supply agreements. If you need the same categories of goods every month or quarter, we can structure a supply arrangement that gives you predictable pricing, reserved stock where possible and a single invoice, saving your team time and procurement effort.""",
        "offerings": """Procurement of general goods, supplies and equipment
Bulk supply for businesses, institutions and project sites
Office, industrial and building-material sourcing
Price comparison and negotiation on your behalf
Specification checks and pre-delivery inspection
Warehousing and logistics coordination
Local procurement agent services for foreign companies
Recurring supply agreements with consolidated invoicing
Combined sourcing, import and delivery under one arrangement""",
        "process": """Brief|You tell us what you need, the specification, quantity, budget and deadline.
Sourcing|We source from vetted suppliers and manufacturers and compare options.
Quotation|You receive a clear quotation with prices, lead times and terms.
Purchase and inspection|On approval we purchase and, where appropriate, inspect the goods.
Delivery|We deliver to your location and provide supporting documents.
Follow-up|We review the supply and set up repeat orders if you need them.""",
        "audience": """Businesses that want one dependable procurement partner
Institutions and organisations with bulk purchasing needs
Contractors and project managers needing materials on schedule
Foreign companies without a local purchasing team
Retailers and resellers seeking new product lines""",
        "faqs": [
            ("What kinds of goods can you supply?", "We supply a broad range of general goods. If your item is not something we normally handle, we will tell you honestly and, where possible, point you to a reliable source."),
            ("Do you supply on credit?", "Terms are agreed case by case. Many orders are paid in advance or in agreed instalments; established clients on recurring supply may qualify for other arrangements."),
            ("Can I get a quotation before committing?", "Yes. Every engagement starts with a written quotation so you know the cost and timeline before you decide."),
        ],
    },
    # ------------------------------------------------------------------ GENERAL CONTRACTOR
    {
        "title": "General Contractor",
        "slug": "general-contractor",
        "icon": "🏗️",
        "order": 4,
        "tagline": "Reliable project delivery from planning to handover.",
        "summary": "We coordinate construction, renovation, supply and installation projects, managing people, materials, timelines and quality on your behalf.",
        "overview": """A project succeeds or fails on coordination. A general contractor is the person who brings together designers, artisans, suppliers, inspectors and the client, and who is accountable for the end result being safe, on budget and on time. Our general contractor service takes that responsibility for a range of residential, commercial and institutional projects.

We handle new builds, renovations and refurbishments, finishing works, fit-outs, fencing and site works, electrical and plumbing installations, and supply-and-install contracts. For specialist work, we bring in qualified professionals and subcontractors, while remaining your single point of accountability. Every project starts with a clear scope, a bill of quantities and a realistic schedule so that you know what you are paying for and when each stage will be completed.

Cost control is central to how we work. We source materials directly through our supply network, avoiding unnecessary middlemen, and we tell you early if a change in specification or a rise in material prices is likely to affect the budget. Regular progress updates, site photos and milestone-based payments keep you in control throughout.

We also support clients who are bidding for contracts: helping prepare quotations, bills of quantities and the supporting documents expected in tenders, as well as supply contracts for companies and institutions that need a registered contractor to deliver goods or services.""",
        "offerings": """Residential and commercial construction coordination
Renovation, refurbishment and interior fit-out
Finishing works: painting, tiling, ceilings, flooring, roofing
Electrical, plumbing and mechanical installations through qualified professionals
Fencing, paving, drainage and external works
Bill of quantities and project budgeting
Material sourcing and supply-and-install contracts
Site supervision, progress reports and quality checks
Tender and quotation preparation support
Project management for diaspora and foreign clients who are not on site""",
        "process": """Site visit and brief|We inspect the site, listen to your requirements and agree the scope.
Design and costing|Drawings, a bill of quantities and a project schedule are prepared for your approval.
Contract|Scope, price, milestones and responsibilities are agreed in writing.
Execution|We mobilise skilled workers, procure materials and begin works under supervision.
Progress reporting|You receive regular updates with photographs and milestone reports.
Handover|Final inspection, snag-list completion and handover with all relevant documents.""",
        "audience": """Homeowners building or renovating
Property investors and developers
Businesses fitting out offices, shops, hotels and warehouses
Diaspora clients who need someone trustworthy on site
Companies and institutions awarding supply or works contracts""",
        "faqs": [
            ("Can you manage a project while I am abroad?", "Yes. We provide regular photo and video updates, documented progress reports and milestone-based payments, so you stay informed and in control from anywhere."),
            ("How do you control costs?", "We start with a detailed bill of quantities, purchase materials directly from suppliers, and report any variation before it is carried out, so there are no surprise charges at the end."),
            ("Do you provide architectural or engineering design?", "We work with qualified architects and engineers for design and approvals, and include their fees transparently in the project cost."),
        ],
    },
    # ------------------------------------------------------------------ TRAVEL & TOURS
    {
        "title": "Travel & Tours",
        "slug": "travel-and-tours",
        "icon": "✈️",
        "order": 5,
        "tagline": "Flights, hotels, tours and complete itineraries, planned with care.",
        "summary": "Business and leisure travel arrangements: flight tickets, accommodation, airport transfers, guided tours, and tailor-made packages across Nigeria, Africa and the world.",
        "overview": """Good travel is about more than a ticket. It is about arriving relaxed, being in the right place at the right time and having someone to call if something changes. Our travel and tours service handles the planning and booking, so that whether you are travelling for business, a family event, a pilgrimage, a holiday or a study programme, the journey is smooth.

For business travellers and visiting investors, we arrange flights, hotels, airport pick-up, ground transport, interpreters and meeting logistics in Lagos and other Nigerian cities, as well as onward travel across Africa. For leisure travellers, we design itineraries around your interests and budget: beach breaks, city tours, cultural experiences, safaris, honeymoon packages and family holidays.

We also assist groups: companies sending staff to conferences and trade fairs, churches and associations organising pilgrimages and retreats, schools running excursions and families travelling together. Group planning means getting many details right at the same time, from flights and rooming lists to transport schedules, and we handle those details for you.

Because we also provide immigration consultancy, we can help you understand which visa you need for your destination and guide you in preparing a complete and honest application, including supporting documents such as itineraries and accommodation bookings. We will always tell you plainly that visa decisions are made by the embassy or immigration authority and cannot be guaranteed.""",
        "offerings": """Domestic and international flight bookings
Hotel, serviced-apartment and resort reservations
Airport pick-up, drop-off and private car hire
Visa-support documents: itineraries and accommodation bookings
Business-trip planning for visiting investors and delegations
Trade-fair, conference and exhibition travel packages
Holiday, honeymoon and family packages
Pilgrimage and group travel arrangements
Guided city and cultural tours
Travel insurance guidance
Study and medical-travel logistics""",
        "process": """Tell us your plans|Share your destination, dates, budget and preferences.
Options|We present suitable flight, hotel and package options with clear prices.
Booking|After your approval, we confirm all reservations and send your documents.
Pre-travel support|We provide a checklist covering travel documents, health requirements and transfers.
On the trip|You have a contact person if plans change or help is needed.
After the trip|We welcome your feedback to improve your next journey.""",
        "audience": """Business executives and visiting foreign delegations
Families planning holidays or travelling for events
Companies, churches and associations with group travel needs
Students and professionals travelling abroad
Diaspora travellers returning to Nigeria""",
        "faqs": [
            ("Can you book tickets for a group?", "Yes. We arrange group fares where available, consolidate rooming lists and coordinate transport for the whole group."),
            ("Do you guarantee visa approval?", "No. Visa decisions belong to the embassy or immigration authority. We help you prepare a complete, accurate application and supporting travel documents."),
            ("Can I change or cancel a booking?", "That depends on the fare rules of the airline or hotel. We explain the conditions before you pay, and help with changes within those rules."),
        ],
    },
    # ------------------------------------------------------------------ IMMIGRATION
    {
        "title": "Immigration Consultancy",
        "slug": "immigration-consultancy",
        "icon": "🛂",
        "order": 6,
        "tagline": "Guidance on all visa types, from tourist to work and residence.",
        "summary": "Clear, honest guidance on visa and immigration processes, including tourist, business, student, work and residence applications, and expatriate documentation for Nigeria.",
        "overview": """Immigration rules are detailed, they change often, and small mistakes in an application can cause long delays or refusals. Our immigration consultancy service gives you clear, honest, up-to-date guidance so that you understand your options, prepare strong and accurate applications and avoid common pitfalls.

We assist people travelling out of Nigeria, including tourists, business visitors, students, skilled workers and families, and we assist foreign nationals and companies who need to come into, work in or reside in Nigeria. For travellers, we help you identify the right visa category, prepare a document checklist, review your supporting documents for consistency and guide you through forms, fees, biometrics and interview preparation.

For foreign companies and expatriates, our service connects with our business registration support. We guide you on business visas, work and residence permissions, expatriate documentation, and the corporate requirements that sit behind them, so that your staff can move to Nigeria and work lawfully.

We believe in honest advice. We will never promise guaranteed approvals, sell fake documents or encourage false statements; those practices put you at serious risk, including bans from future travel. What we will do is help you present your genuine case clearly and completely, within the law, and tell you early if we think an application is likely to face difficulty so that you can decide how to proceed.""",
        "offerings": """Visa eligibility assessment and category advice
Tourist, visitor and business visa application support
Student visa and admission-related documentation guidance
Work and skilled-worker visa guidance
Family, spouse and dependent visa guidance
Document checklists, form completion support and consistency review
Interview and biometrics preparation
Invitation-letter and supporting-document guidance
Expatriate documentation and residence guidance for Nigeria
Support for companies relocating foreign staff to Nigeria
Guidance on reapplying after a refusal""",
        "process": """Consultation|We review your situation, travel purpose, history and goals.
Visa strategy|We identify the best visa category and explain the requirements and likely timelines.
Document preparation|We provide a checklist and review your documents for completeness and consistency.
Application support|We guide you through forms, fees, appointments and biometrics.
Interview preparation|We prepare you to explain your case clearly and truthfully.
Follow-up|We help you understand the decision and plan next steps, including reapplication where appropriate.""",
        "audience": """Individuals travelling for tourism, business, study or work
Families seeking to join relatives abroad
Foreign nationals planning to live or work in Nigeria
Companies relocating foreign employees to Nigeria
Applicants who have been refused and want to reapply properly""",
        "faqs": [
            ("Can you guarantee my visa?", "No legitimate consultant can. Visa decisions are made solely by the embassy or immigration authority. We improve the quality and completeness of your application; we do not promise outcomes."),
            ("Which countries do you cover?", "We advise on a wide range of destinations, and we also cover Nigerian immigration processes for foreign nationals. Requirements vary by country and change often, so we verify current rules at your consultation."),
            ("Do you help after a visa refusal?", "Yes. We help you understand the reasons, decide whether to reapply or appeal and strengthen the application honestly."),
            ("Are my documents kept confidential?", "Yes. We treat your personal documents and information as confidential and use them only for your application."),
        ],
    },
]
