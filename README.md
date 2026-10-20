# Building Products in the AI & Cloud Era

*Deciding What to Build*

<small>© 2026 Oleksiy Pylypenko · Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — share and adapt freely, non-commercially, with attribution. Source on [GitHub](https://github.com/oleksiyp/buildproducts-book). Also in the series: [*Software Architecture in the AI & Cloud Era*](https://oleksiyp.github.io/arch-book/), [*Building Software at Scale in the AI & Cloud Era*](https://oleksiyp.github.io/buildsoftware-book/), [*Building Resilient Systems in the AI & Cloud Era*](https://oleksiyp.github.io/resilienteng-book/) and [*Operating Production Systems in the AI & Cloud Era*](https://oleksiyp.github.io/prodsys-book/).</small>

## Preface

Every piece of software begins as a decision that something ought to exist. Most of the decisions we make in building it afterwards concern how: which structure, which language, which database, which way to divide the work among teams. The first decision is of another kind, because it concerns other people. It is a guess about what they need, what they will do and what they will pay, made before anyone can know whether the guess is right. Frederick Brooks wrote in 1986 that the hardest single part of building a software system is deciding precisely what to build. Forty years of practice have not made him wrong. They have mostly taught us how many ways there are to avoid making that decision deliberately, by building whatever the loudest customer asked for, whatever the competitor shipped last quarter, or whatever a new library happened to make possible.

This book is about making the decision well. Its thesis is that a product is a long-lived bet on how customers will behave, and that deciding well what to build is the hardest part of building software, a part that grows as a share of the whole as construction gets cheaper. When building a feature took a team a quarter, the cost of building the wrong one was at least partly paid in the building, and the slowness of construction forced a kind of selection on us. As code becomes cheaper to produce, that brake comes off. An organization can now build the wrong thing faster than ever, and it will then own what it built, because software that ships must be maintained, explained, supported and eventually retired, whether or not anyone uses it. The economics of the last decade have shifted the scarce resource from the hands that write code to the judgment that decides what code is worth writing.

That judgment is not a gift. It is a practice, with methods that have been tested and a history that explains why they work, and few of those methods began in software. Ronald Fisher learned to separate the effect of a fertilizer from the noise of soil and weather in the field trials at Rothamsted in the 1920s, and every online experiment still rests on what he worked out there. Intuit learned in the 1980s that following a buyer home from the shop and watching the first evening with its product taught more than asking customers what they wanted. A punch-card ballot in Palm Beach County showed in 2000 how a layout approved by officials could send thousands of votes to the wrong candidate, and a binder of signage standards for the New York subway showed in 1970, and in the two decades of neglect that followed, that a standard is worth something only while someone maintains it. I have come to believe that the newest product practices are best used by someone who knows the older lessons beneath them. A team that runs A/B tests without understanding randomization, or interviews customers without knowing why stories about the past are better evidence than predictions about the future, has the method without its reason, and it will misuse the method the first time its situation departs from the textbook.

This book is written for the reader who wants both the method and the reason. That reader might be a product manager who has inherited a roadmap and suspects it is a list of requests, a designer who wants research to change decisions instead of decorating them, or an engineer, a tech lead perhaps, who has noticed that the most expensive mistakes on their team were made before anyone wrote a line of code. AI appears where it really changes the practice and nowhere else. Chapter 1 weighs the young and mixed evidence on what AI assistance does to the cost of building, and what that implies for the cost of deciding. Chapter 3 shows prototypes that once took days produced in hours, and is honest that this practice is still emerging. Chapter 6 designs an AI feature into a product, with its errors written down before its prompt. Everywhere else, AI gets a sentence at most, because a book that put it into every chapter would be teaching fashion. The tools will keep changing, and the work of deciding what deserves to be built will remain.

The book belongs to a series that asks one question from several sides, and it follows one fictional company through all of them. *Software Architecture in the AI & Cloud Era*, which these pages call the Architecture book, asks how to shape a system. This book, the Products book, asks how to decide what the system should do for the people who use it. *Building Software at Scale in the AI & Cloud Era*, the Software book, which is forthcoming, asks how 40 teams build what has been decided. *Building Resilient Systems in the AI & Cloud Era*, the Resilience book, and *Operating Production Systems in the AI & Cloud Era*, the Operations book, ask how the result is engineered for production and kept running. Each book stands on its own, and they were written to be read together.

### Influences & Attribution

Much of this book's method comes from others, and I want to be plain about where. Each chapter's references point to the original works, which are always the better read; this book's job is to connect them and to show them working together at one company. The idea of the product operating model, of empowered teams given problems instead of features, and of the four risks a product must retire comes from Marty Cagan's *INSPIRED*, *EMPOWERED* and *TRANSFORMED*, the last two written with colleagues at the Silicon Valley Product Group. Melissa Perri's *Escaping the Build Trap* named the failure the book opens with, and Josh Seiden's *Outcomes Over Output* sharpened the measure. Discovery follows Teresa Torres's *Continuous Discovery Habits*, Ryan Singer's *Shape Up*, Jeff Patton's *User Story Mapping* and Eric Ries's *The Lean Startup*, with Intuit's long practice of following customers home as its oldest example.

Strategy draws on Richard Rumelt's *Good Strategy Bad Strategy*, on Michael Porter and on A. G. Lafley and Roger Martin's *Playing to Win*. The account of the progress customers seek follows Clayton Christensen's *Competing Against Luck* and the field work of Bob Moesta and Chris Spiek, with Tony Ulwick's outcome-driven school as its rival. Multi-sided markets draw on Jean-Charles Rochet and Jean Tirole, on David Evans and Richard Schmalensee's *Matchmakers*, and on Geoffrey Parker, Marshall Van Alstyne and Sangeet Paul Choudary's *Platform Revolution*; maps of the landscape follow Simon Wardley, and objectives follow Andy Grove and John Doerr, with Edwin Locke and Gary Latham's research on goal setting beneath them. Measurement rests on Ronald Fisher's *The Design of Experiments* and, for its modern online form, on Ron Kohavi, Diane Tang and Ya Xu's *Trustworthy Online Controlled Experiments*, together with the work of Aleksander Fabijan, Kerry Rodden, Alberto Abadie and David Holtz and their colleagues on what can go wrong in an experiment and what to do when none is possible. Pricing follows Madhavan Ramanujam and Georg Tacke's *Monetizing Innovation*, with Andrew Odlyzko on why buyers resent being charged differently for the same thing.

The second half of the book draws on design. Don Norman's *The Design of Everyday Things* is its foundation, with Alan Cooper and colleagues' *About Face*, Steve Krug's books on testing, and Jakob Nielsen and Thomas Landauer's model of how many users a test needs. AI features follow Saleema Amershi and colleagues' guidelines for human–AI interaction and Google's *People + AI Guidebook*, and accessibility follows the W3C's guidelines and the European Accessibility Act. Design systems draw on Brad Frost's *Atomic Design*, Alla Kholmatova's *Design Systems*, Nathan Curtis's writing on design-system teams and Luca Mezzalira's *Building Micro-Frontends*; mobile draws on Gergely Orosz's *Building Mobile Apps at Scale* and the published release practices of Facebook and Spotify. APIs as products follow Arnaud Lauret's *The Design of Web APIs*, James Higginbotham's *Principles of Web API Design*, JJ Geewax's *API Design Patterns* and *Continuous API Management* by Mehdi Medjaoui and colleagues. The capstone leans on Colin Bryar and Bill Carr's account of working backwards at Amazon, Gary Klein's premortem, Annie Duke on bets and quitting, and Baruch Fischhoff on hindsight. The real cases (HealthCare.gov, Apple's grid of 1997, Amazon's DVD price test, the butterfly ballot, the subway manual, the App Store, Twitter's API rules and the Gmail launch) are described as history, from the public record.

Several terms used in this book as common vocabulary were coined by specific people or groups, and they deserve the credit: the build trap (Melissa Perri), the four big risks and the product operating model (Marty Cagan), the product trio and the opportunity solution tree (Teresa Torres), the kernel of strategy and the proximate objective (Richard Rumelt), the switch interview and its four forces (Bob Moesta and Chris Spiek), Wardley maps (Simon Wardley), objectives and key results (Andy Grove, popularized by John Doerr), appetite and shaping (Ryan Singer), story mapping (Jeff Patton), the walking skeleton (Alistair Cockburn), the Wizard of Oz test (J. F. Kelley), the HEART framework (Kerry Rodden, Hilary Hutchinson and Xin Fu), feature shock, minivation, hidden gems and the undead (Madhavan Ramanujam and Georg Tacke), the gulfs of execution and evaluation (Don Norman and colleagues), posture and perpetual intermediates (Alan Cooper), atomic design and the interface inventory (Brad Frost), and design tokens (Jon Levine and Jina Anne at Salesforce).

### Authorship & Disclaimer

This book was written and directed by Oleksiy Pylypenko, with AI assistance (Anthropic's Claude). The judgment in it comes from twenty-plus years of practice: platform engineering inside a large bank, API architecture in fintech, and a decade of maintaining a widely used open-source library. The author chose the thesis, the structure, the examples and the trade-offs, edited every chapter, and takes responsibility for every claim, errors included. Encore and every kata company are fictional, and historical events are described from the public record. The content is provided as-is, without warranty of any kind. It is educational material, not professional, legal or financial advice for any specific product, and the license's full disclaimer of warranties applies.

## How to Read This Book

One company runs through all ten chapters. **Encore** sells tickets to live concerts across the European Union, and its traffic can rise 500× in minutes when a major tour goes on sale, which makes it a demanding place to learn how to build software. Readers of the Architecture book watched Encore grow from nine engineers to 400, and readers of the Resilience and Operations books watched it prepare for, fight and learn from one bad Friday morning. This book picks the company up a few months after that morning, in the winter of its ninth year, and asks a question the earlier books took for granted: given that Encore can build and run almost anything, how does it decide what is worth building? Chapter 1 introduces Encore for readers meeting it for the first time, each later chapter adds the parts of the company it needs, and an appendix gathers all of them on one page for reference.

One product decision runs through the book: **Verified Resale**, a bet that fans who cannot attend a show should be able to resell their tickets through authorized partners at no more than face value, with Encore reissuing every resold ticket under a new barcode and organizers setting the rules and sharing the fee. Part I follows the decision from a proposal on the table to a funded bet: its strategy, its riskiest assumptions, how its success will be measured and what it will cost. Part II designs it for the people who will meet it, on screens, on phones and through the interfaces partners build on. Chapter 10 then follows the whole bet through 18 months, from the memo that proposed it to a staged launch in France and the review that asked whether it paid.

Each chapter closes with a **kata**, a practice brief for a different company with its own scale and constraints, together with a rubric to check your work against. The word comes from the martial arts, where a kata is a set form practiced until it becomes second nature, and the idea is much the same as a musician's scales: the value lies in repetition in a place where mistakes are cheap, so that the moves are familiar when mistakes become expensive. Every section ends with a short recap and an exercise. The exercises work best done against a product you actually work on, because the point is to see the idea in your own organization rather than in Encore's. Each chapter's references list the field's standard works, and those marked *free online* cost nothing to read.

The chapters build on one another, but each can be read on its own. A reader whose team is drowning in requests may start with Chapter 1, a reader about to set a price may start with Chapter 5, and a reader whose partners keep breaking on every release may start with Chapter 9. Chapters 1 and 3 are the ones I would ask every reader to make time for, because the first explains why deciding is hard at scale and the second explains how to learn before paying to build.

This book tells only half of Verified Resale's story. The Software book follows the same 18 months from the engineering side: the eight-year-old code that issues barcodes and had to learn to reissue a ticket, the tests and platforms that made changing it safe, and the organization of 40 teams that built it. Its capstone traces the same first resold ticket, bought by a fan in Lyon, through the code that this book's Chapter 10 traces through the product. Where the two books meet, each points to the other and does not repeat it, so a reader of both will find two views of one decision, and a reader of either will find a complete book.

## The Arc

The ten chapters fall into two parts and a capstone. They move from deciding what to build, through designing what was decided for the people who will use it, to one bet followed from idea to launch.

**Deciding what to build (Chapters 1–5):** the product and the system at 400 engineers, product strategy, discovery, measurement and experimentation, and pricing and monetization.

**Designing the experience (Chapters 6–9):** design for people, including accessibility and AI features; design systems and the frontend at scale; mobile and many channels; and APIs as products.
{: .flush}

**The capstone (Chapter 10):** Verified Resale from the bet memo to a staged launch and the review of the bet.
{: .flush}

## Contents

1. [The Product and the System — Deciding What to Build at 400 Engineers](#ch1)
2. [Product Strategy — Choosing Where to Play](#ch2)
3. [Product Discovery — Learning Before Building](#ch3)
4. [Measuring Products — Analytics and Experimentation](#ch4)
5. [Pricing, Packaging, and Monetization](#ch5)
6. [Designing for People — Usability, Accessibility, and AI Features](#ch6)
7. [Design Systems and the Frontend at Scale — One Product from Forty Teams](#ch7)
8. [Mobile and Many Channels — Software You Cannot Recall](#ch8)
9. [APIs as Products — Designing, Governing, and Supporting the Interfaces Others Build On](#ch9)
10. [Capstone — Verified Resale from Idea to Launch](#ch10)

[Appendix: Encore at a Glance](#encore-glance)
{: .toc-appendix}

---

## Chapter 1: The Product and the System — Deciding What to Build at 400 Engineers {#ch1}

> "The hardest single part of building a software system is deciding precisely what to build." — Frederick P. Brooks Jr.

A company with 400 engineers can build almost anything it decides to build. That is its strength, and it is also the source of a quiet danger, because the capacity to build makes the decision about what to build feel cheaper than it is. Forty teams will always have work. Their boards will be full, their releases frequent and their roadmaps confident, and none of that tells us whether the work is changing anything for the people it was meant to serve. The question of this chapter, and of the whole book, is whether an organization of this size can decide well what to build: how it notices that it has been measuring the wrong things, who in it should own the decision, how the decision is tested before the money is spent, and what changes now that writing code has become cheaper than it has ever been.

We begin with a failure that had every output a project plan could ask for. On 1 October 2013 the United States government opened HealthCare.gov, the website through which millions of Americans were to buy health insurance. Dozens of contracts had been let, the code had been written, and the site went live on the day the White House had promised. On that first day, according to the government's own inspector general, six people managed to submit an application and select a plan. The repair that followed, and the government agency that grew out of the repair, teach the central lesson of this chapter more plainly than any framework could. A product can be delivered on time while its outcome fails, and the difference between the two is a matter of ownership and measurement far more than of engineering skill.

Encore, the concert-ticketing company we follow through this series, has never had a day like that, and this chapter will not invent one. Its trouble is milder and more common. Encore reached 400 engineers in its seventh year, and it has stayed at about that size since. It is now the winter of its ninth year, a few months after the Vesper Hale on-sale and the added stadium dates that the Operations book followed. Some of its teams decide well what to build; others work through a queue of requests that nobody ever checks against what customers then did. And on the table is a proposal that will test all of them. It is called **Verified Resale**: fans who cannot attend a show would resell their tickets through authorized partners, Encore would reissue every resold ticket under a new barcode, and organizers would set the rules and share the fee. This chapter introduces Encore for readers who start here, sets out the proposal, and asks what Encore would have to be good at to decide whether it should exist. Chapter 2 takes up whether it should.

### 1.1 The Build Trap

#### Six people on the first day {#c1-healthcare-gov}

HealthCare.gov was built to let people in 36 states, those that had not set up an exchange of their own, compare and buy health insurance under the Affordable Care Act. The Centers for Medicare & Medicaid Services (CMS), part of the Department of Health and Human Services (HHS), was responsible for it. The law required that coverage begin on 1 January 2014. It did not require the website to open on 1 October 2013. That date came from a public commitment by the White House, and the HHS Office of Inspector General (OIG) later found that some staff and contractors worked under "the misimpression that the deadline for website functionality was statutory." Nobody among CMS's leadership, the OIG reported, seriously discussed moving it.

The work was divided among about 60 contracts, 55 of them awarded under contracts that already existed for other purposes. CGI Federal built the core of the marketplace. No contractor was hired to act as the systems integrator, the party responsible for making the pieces work together, because CMS believed it was doing that job itself. And nobody owned the whole. "CMS senior leadership never declared a clear 'business owner' with overall responsibility for the Federal Marketplace," the OIG wrote, and when its investigators asked staff which division had led the project, they named four different ones. The Government Accountability Office (GAO) reached a similar conclusion in 2014, finding that CMS had issued task orders while key technical requirements were still unknown. The costs grew as such projects' costs do: six key contracts estimated at $464 million had reached $824 million by early 2014.

On the morning of 1 October about 250,000 people tried to use the site at once, far more than it had been built to carry, and it began failing within two hours. "In the end," the OIG wrote, "only six consumers were able to submit an application and select a plan on the first day." Notice the precise wording, because the popular retelling blurs it. Six people did not enroll and pay; six managed to apply and choose. Every output in the plan had been delivered. The contracts had been let and fulfilled, the code had been written and deployed, and the launch date had been met. The outcome, people able to buy insurance, had not happened at all.

The repair is the more instructive half of the story. Steven Brill's account in *Time*, published in February 2014, describes a small group of engineers from outside government, among them Mikey Dickerson, on leave from Google's site reliability engineering, who arrived in the third week of October under Jeff Zients and the US chief technology officer, Todd Park. One of their first discoveries was that nobody could see what users were experiencing: the site had no dashboard of its own health, so the first thing the newcomers did was build one. Dickerson's rules for the daily stand-up meeting, as Brill reports them, are worth quoting, because they describe a culture as much as a process: "The ones who should be doing the talking are the people who know the most about an issue, not the ones with the highest rank." By early December, by Brill's account, the site could serve at least 50,000 people at once, and its uptime had risen from 43% to 95%. The first open enrollment ended with 5.4 million people having selected a plan through the federal marketplace.

It is tempting to tell this as the story of a brilliant small team rescuing a failed large one, and the OIG's report, based on 86 interviews, takes care to correct that version. What it credits is a reorganization of everyone already involved: a "badgeless" culture in which CMS staff and contractors worked together as one team, whatever their employer, together with "ruthless prioritization" of the work that mattered most. Its summary of the cause is a single sentence: "Most critical was the absence of clear leadership." In August 2014 the White House founded the US Digital Service (USDS), with Dickerson as its administrator, and published the *Digital Services Playbook* the same day. Its sixth play states the lesson of the whole affair in a paragraph: "Assign one leader and hold that person accountable. There must be a single product owner who has the authority and responsibility to assign tasks and work elements; make business, product, and technical decisions; and be accountable for the success or failure of the overall service."

Read as a product failure, HealthCare.gov had four faults, and each will recur in this book in a milder form. A date was mistaken for the goal. The work was organized as contracts with deliverables, so that every party could succeed while the whole failed. Nobody measured what users experienced, so bad news had no road to travel up. And nobody owned the product from end to end. The repair restored each missing piece: an owner, a measure of outcomes and one team across organizational boundaries.

#### Outputs and outcomes {#c1-outputs-outcomes}

The distinction at the heart of that story needs precise names. An **output** is something an organization produces and ships: a feature, a release, a completed contract, a closed ticket. An **outcome** is a change in what customers do that creates value for them and for the business. Josh Seiden, whose short book *Outcomes Over Output* (2019) gave the distinction its plainest form, defines an outcome as a change in human behavior that drives business results. The definition is demanding on purpose. It excludes things we produce, because those are outputs, and it excludes the business results themselves, such as revenue, because those arrive too late and are caused by too many things to steer a team. What remains is behavior: organizers setting up events in half the time, fans who come back for a second show, partners whose integrations stop breaking.

Melissa Perri, in *Escaping the Build Trap* (2018), named the condition that follows when an organization loses this distinction. The **build trap** is an organization's habit of measuring its success by what it ships rather than by what its customers then do. The trap is comfortable, which is why it is common. Outputs are easy to count, they arrive on a schedule, and they belong clearly to the team that made them, while outcomes are slow, noisy and shared. A roadmap of features can be finished, and finishing it feels like success. An organization in the trap is rarely idle; it is usually busier than its neighbors.

The evidence that outputs are a poor proxy is old and consistent. At Microsoft, Ron Kohavi and his colleagues ran controlled experiments on ideas that teams had already judged worth building, and they reported in 2012 that "only one third of ideas tested at Microsoft improved the metric(s) they were designed to improve." The other two-thirds were neutral or made things worse, and without the experiments every one of them would have counted as a delivered feature. A vendor study points the same way from a different angle. Pendo's *Feature Adoption Report* of 2019 estimated that 80% of features in the average software product are rarely or never used. That figure comes from one company's analysis of its own customers' products, so it indicates a direction and does not measure the industry. Taken together, the two sources suggest that a team which ships and moves on is, most of the time, unaware of whether its work did anything at all.

Encore's organizer console shows the symptoms clearly enough to be useful. Over the last four quarters the seven teams that build for organizers shipped 61 items from a shared request queue. Forty-four of them entered the queue from the organizer sales team, usually attached to a contract being negotiated, and they arrived as solutions: a new export format, a second approval step for price changes, a dashboard tile. Only for five of the 61 did anyone look afterwards at whether organizers used the result. The teams are capable and hard-working, and nothing here is anyone's fault in particular. The trouble lies in the queue itself, which records what was asked for and what was shipped, and holds no place for what happened afterwards.

#### The value exchange system {#c1-value-exchange}

Perri's account of why organizations fall into the trap rests on a simple model. A company and its customers are in a **value exchange**: customers have problems and desires, and when the company's products solve them, the customers give something back, usually money, loyalty or attention. The company captures value only by creating it for customers first. The model sounds too obvious to need stating, until we notice how many forces inside a company push it out of shape. Perri names three kinds of organization in which one force dominates, and Figure 1.1 sets them beside Encore's own history.

| Kind of organization | What drives the roadmap | How the exchange distorts | An example from Encore's history |
|---|---|---|---|
| Sales-led | Contracts being negotiated | The largest customer's request becomes everyone's product | The organizer console's request queue |
| Visionary-led | One leader's conviction | Works while the leader is right, and fails when the leader leaves or is wrong | The founders' early years, when nine engineers built what two founders believed in |
| Technology-led | What new technology makes possible | Features exist because they can, with no market behind them | "View from your seat", a 3D preview built in year five because a new rendering library allowed it, which few fans ever opened |

*Figure 1.1 — Perri's three distorted organizations, with an Encore example of each. Each kind trades the customer's problem for a different proxy.*

Perri's own example of the visionary-led company is Apple under Steve Jobs, which she treats as the rare exception that works while the visionary is present. Chapter 2 tells the story of Jobs's return to Apple in 1997, so here we note only her warning: a company whose product judgment lives in one person has a single point of failure in the place it can least afford one. The framework itself is a practitioner's lens, drawn from experience; nobody has tested it in a controlled study. It earns its place because it lets a team name the force bending its own roadmap, and once the force is named, the team can argue about whether it should prevail.

#### Projects, products and services {#c1-projects-products}

A deeper cause of the trap lies in how work is organized and funded. A **project** is a bounded piece of work with a scope, a budget and an end date; it succeeds when its scope is delivered. A **product** is a long-lived capability with an owner, which succeeds when it changes what its customers do and goes on succeeding only as long as it keeps doing so. A **service**, in Perri's sense, delivers value mainly through people's labor, each instance done afresh. The three shapes reward different things. A project rewards finishing, a product rewards the outcome, and a service rewards the hours its people put in.

HealthCare.gov was the project shape at its most expensive: some 60 contracts, each with deliverables, none responsible for whether a family could buy insurance. Encore's own example is milder and instructive in a different way. Onboarding a new venue onto Encore's SaaS platform is still partly a service, since a person on the Tenant Onboarding team configures each new venue's seat maps and branding by hand. Perri's point is that a service which needs a person in every instance is not yet a product, and that it becomes one only when the organization decides to own the outcome, venues live and selling, and invests in making it repeatable. Mik Kersten's *Project to Product* (2018) adds a way of seeing what a product team actually spends its time on, by sorting work into four flow items: features, defects, risks and debt. The funding mechanics that follow from his argument belong to the Software book's Section 10.4, and we leave them there.

#### The hardest single part {#c1-hardest-part}

The Architecture book introduced Fred Brooks's distinction between essential complexity, which belongs to the problem, and accidental complexity, which we bring to it, and this book does not redefine either. What it adds is the passage from the same essay, "No Silver Bullet" (1986), that the Architecture book did not quote, and which is this book's starting point. "The hardest single part of building a software system is deciding precisely what to build," Brooks wrote, and a few sentences later: "No other part of the work so cripples the resulting system if done wrong. No other part is more difficult to rectify later." He went on to say why: "the client does not know what he wants." His remedy was the iterative extraction and refinement of requirements, through rapid prototypes put in front of the people who would use the system.

Brooks called deciding what to build the hardest single part. This book goes a step further and argues that most of a product's essential complexity is decided there, in the choice of which problem to solve and for whom, and that everything built afterwards inherits the quality of that choice. The claim is ours, and Brooks should not be held to it. But it explains the shape of this book, which spends its first part on deciding before it spends its second on designing. It also explains why Brooks's remedy reads, forty years later, like a description of what product teams now call discovery.

#### Diagnosing the trap {#c1-diagnosing}

How does an organization tell whether it is caught? Perri closes her book with a short set of diagnostic questions, and two of them do most of the work. One asks who came up with the last feature the team built. The other asks what was the last product the company decided to kill. A company that cannot answer the second has no mechanism for learning that something failed, because outputs, once shipped, are never examined again. Marty Cagan's essay contrasting good and bad product teams, first published in 2007 and collected in *INSPIRED* (2017), and John Cutler's "12 Signs You're Working in a Feature Factory" (2016) offer longer lists of symptoms. None of these is a validated instrument. They are checklists drawn from experience, useful because the honest answers are uncomfortable.

At Encore the answers differ by team, and that is itself the most useful finding. The fan storefront teams run experiments, watch what fans do and retire features that fail. The organizer console teams, as we saw, work through a queue, and when asked what they last decided to kill, they could not name anything. The same company, with the same leaders and the same engineering platform, can be product-led in one part and caught in the trap in another, because the trap lives in how each team's work arrives and how it is judged.

The simplest proven tool for changing how work arrives is to ask, before it starts, what outcome it serves. Cagan's opportunity assessment in *INSPIRED* does this with four questions, asked of any proposed piece of work: what business objective it addresses, how we will know it succeeded, what customer problem it solves, and for which customers. The Organizer Console team now attaches a filled-in assessment to every item that enters its queue. Here is one, for a request that arrived from sales.

```text
OPPORTUNITY ASSESSMENT: OC-212 "Second approval step for price changes"
Requested by     Organizer sales, for a festival promoter's renewal
Objective        Retain mid-size promoters at renewal (team objective 2)
Customer problem Promoters' finance staff fear unauthorized price changes
                 by event staff; two incidents reported in the last year
Target customers Promoters with separate finance and events staff
                 (about 120 of our 900 active organizers)
Success measure  Share of those promoters using price-change approval
                 after 90 days; renewal rate in the segment
Alternatives     Audit log with alerts; per-role permission on prices
Decision         Discovery first: interview four promoters, test alternatives
Review           Outcome check booked for 90 days after release
```

The last line matters as much as the others. An assessment written before work begins is only half the discipline. The other half is the review after release, when someone looks at the success measure and decides whether the work stays, changes or goes. That review is how a company comes to have an answer to Perri's question about the last thing it killed. Measuring the outcome well is the subject of Chapter 4; here it is enough that the review is booked, with a date and the people who will attend, at the moment the work is accepted.

**Recap.** HealthCare.gov delivered its outputs on time and failed its outcome, because nobody owned the product end to end and nobody measured what users experienced. The build trap is the habit of judging work by what is shipped, and the evidence that most shipped work moves nothing is old and consistent. Sales-led, visionary-led and technology-led organizations each bend the exchange of value in their own way, and the project shape rewards finishing over outcomes. The cure begins with two habits: ask what outcome a piece of work serves before it starts, and look afterwards at whether it did.

**Exercise 1.1.** Take your team's last ten shipped items. Label each with the outcome it was meant to move, and with whether anyone checked afterwards that it did. Then answer Perri's question for your own organization: what was the last thing you decided to kill?

### 1.2 Encore at 400

#### The products {#c1-products}

For readers meeting Encore for the first time, a short introduction. Encore sells concert tickets across the European Union, in euros, and also sells its ticketing platform to venues as software as a service (SaaS). Three facts have shaped everything it has built. When a famous artist's tour goes on sale, traffic rises 500× within minutes. Every seat must be sold exactly once. And bots arrive before the fans do. The Architecture book followed Encore from nine engineers to 400, the Resilience book showed how it prepares for its biggest mornings, and the Operations book showed one of those mornings, the Vesper Hale on-sale, going wrong and being recovered. This book asks a different question of the same company: given that it can build and run almost anything, how does it decide what is worth building?

At 400 engineers Encore has four kinds of customer, and it serves each with a product of its own. Fans use the storefront on the web and the native app, to find events, buy tickets and carry them to the door. Organizers, the promoters and festival companies whose events Encore sells, use the organizer console to set up events, set prices and watch sales. Partners, among them venues, a festival app and the resale partner Rowmate, call the public and partner application programming interfaces (APIs) at `api.encore.com`. And more than 500 venues run their own box offices on Encore's platform as SaaS tenants, in three tiers. A fifth product serves only Encore itself: the internal platform, the paved roads on which its teams build and deploy. Each of these products has different customers, different measures of success and different economics, and each has one product leader accountable for its outcome. That last fact is USDS's sixth play, applied to a company: whatever else changes, someone can always say who owns the product.

#### The 40 teams on one map {#c1-roster}

Figure 1.2 places Encore's teams by the product and customer they serve. It is the roster this book keeps; the Software book reads the same roster as code ownership and as team types, in its Sections 1.2 and 9.2. Encore has 40 stream-aligned teams, each owning a slice of a product or a shared domain end to end, with about nine engineers each, and a platform group of nine teams and 40 people beneath them. The platform group sits at the top of the 5–10% of engineering that the Architecture book's Section 15.2 gave as a common rule of thumb.

| Product | Its customers | Stream-aligned teams | Examples | One outcome it watches |
|---|---|---|---|---|
| Fan storefront and app | Fans | 9 | Fan Discovery, Seat Map, Checkout, Mobile App, Design System | Share of admitted fans who complete a purchase |
| Organizer console | Organizers | 7 | Organizer Console, Event Setup, Pricing & Presales, Festivals, Forecasting | Time from contract to first event on sale |
| Partner and public APIs | Partners | 3 | Public API, Partner APIs, Embeds & Channels | Partner integrations certified and live |
| Encore SaaS for venues | Venue tenants | 7 | Tenant Onboarding, Tenant Configuration, Box Office, Venue Entry | Days from signature to a venue's first sale |
| Shared domains | All four | 14 | On-Sale, Bot Screening, Inventory, Orders & Payments, Fan Messaging | Each domain's service levels, set with its consumers |
| Internal platform | Encore's own teams | 9 platform teams, 40 people | Reliability, Runtime, Developer Portal, AI Platform | Share of services on the golden path |

*Figure 1.2 — Encore's products, customers and teams on one map. Forty stream-aligned teams serve four kinds of customer, directly or through the 14 shared domains, and the platform group serves the teams.*

The shared domains need a word of explanation, because they are where the map stops being a simple tree. The Inventory team owns Seat Inventory & Ticketing, the service that sells each seat exactly once, and every product depends on it. So do Orders & Payments, Bot Screening and Fan Messaging, which delivers tickets to phones. These teams have customers in every column, and their outcomes are the service levels the Resilience book taught Encore to set with the teams that consume them. A map like this is never neutral. It records which customers have a team of their own and which are served only on the way to someone else, and the exercise at the end of this section asks the reader to draw one for that reason.

#### How Encore got here {#c1-how-encore-got-here}

Every stage of Encore's growth made product decisions by default, through the shape of the organization, without anyone choosing them. When Encore had nine engineers in one team, the two founders decided what to build in conversation. They were, without using the word, a product trio of the kind Section 1.3 describes, and they were close enough to fans and organizers to be right most of the time. The decision they made by default was that the organizer side would be built when someone had time. For three years, organizers were served by whatever the fan product needed them to have.

Three years later Encore had 70 engineers in nine teams, each owning one service. Product decisions now followed service boundaries: whoever owned a service decided what it did, and nobody owned journeys that crossed several services. The public API opened in this period because partners asked for it, and in its sixth year Encore agreed to a request from partners that became, without anyone deciding so, a product. Under **Partner Listings**, authorized partners could read Encore's event listings and post resale offers that showed as links on sold-out event pages, while the ticket itself changed hands outside Encore. It was approved as an integration and owned by nobody as a product, and nobody measured what it did to fans. Chapter 2 reads the consequences.

By its seventh year Encore had 400 engineers in 40 teams, the shape Figure 1.2 shows, and the decision made by default at this size was the request queue. Where a product had a strong leader and good data, as the fan storefront did, teams were given problems. Where the loudest input came from contracts being negotiated, as on the organizer side, teams were given lists. The Software book's Section 9.1 tells the organizational history in full. Here the point is narrower: at each size, the decisions Encore made by default were product decisions, and it only noticed them afterwards.

#### The new bet: Verified Resale {#c1-verified-resale}

The proposal came from Encore's chief product officer and its head of partnerships, in the weeks after the Vesper Hale on-sale, when tickets for the tour appeared on unofficial resale sites within a day at prices well above face value and fans who bought them were turned away at the door. Its parts answer the four weaknesses of Partner Listings that Chapter 2 sets out: a barcode could be sold to several buyers, organizers had no control, organizers took no share, and buyers went unscreened.

Fans may list tickets they bought through the Sale Gate, Encore's admission controller for on-sales, on Encore's own app or on an authorized partner. Rowmate would be the first partner and Tessera the second. Partners are marketplaces where fans list their tickets; no partner owns inventory, and Encore admits no professional resellers. When another fan buys a listing, that buyer passes the same Bot Screening as any primary buyer, and Encore **reissues** the ticket: it issues a new ticket identity to the buyer and revokes the seller's old barcode at every gate. The price is capped at face value, meaning what the seller originally paid, and organizers can only tighten the rules for their events: by setting a lower cap, disabling resale, shortening the resale window or lowering the per-fan limits. The buyer pays a 10% fee on top of the resale price, split four points to the partner through which the ticket was bought, three to the organizer and three to Encore; when the buyer buys in Encore's own app, Encore keeps the partner's four points as well. A €60 ticket resold at face value costs the buyer €66; the partner receives €2.40, the organizer €1.80 and Encore €1.80, and the seller gets the full €60.

Reissue on transfer is established practice in the industry, and Encore did not invent it. When Ticketmaster announced its SafeTix system in May 2019, it described a mobile barcode that refreshes every few seconds and a new digital ticket issued to the recipient whenever a ticket is transferred. What Encore proposes to add is the rest of the system around reissue: the partners, the organizer's rules, the cap and the shared fee.

It is important to say what the proposal is at this point, because the rest of Part I depends on it. Nothing has yet been decided. Leadership has asked for a written bet memo by the end of the winter, and has asked three people to spend the weeks until then finding out whether the bet deserves to be made. Chapter 2 tests its strategy, Chapter 3 its assumptions, Chapter 4 how its success would be measured and Chapter 5 its price. Verified Resale will be built in the end, and Chapter 10 follows it from the memo to its launch and review. But at this moment nobody at Encore knows that, and the chapters that follow should be read as the company finding out.

#### What already exists {#c1-what-exists}

Verified Resale does not start from nothing, and an honest assessment of a bet begins with the assets it can reuse. When Encore opened its public API, in the Architecture book's Chapter 7, resale partners were among the first to ask for a feed of available inventory, and Partner APIs has served such feeds ever since. Since the Rowmate key leak, which the Resilience book's Section 7.2 tells, every partner has authenticated with short-lived tokens bound to a client certificate, so the partner credentials a new product would need already exist and have already been tested by an incident. Fan Messaging delivers tickets to phone wallets and updates passes. And since the eighth year, the barcode in Encore's app has rotated, generated on the phone from a secret held for each ticket, so a screenshot of a ticket stops working within seconds. Each of these was built for another purpose, and each lowers the cost of the bet. The mechanics stay in the books where they were built; what matters here is that the trio can count them as assets when it estimates what Verified Resale would cost.

**Recap.** Encore serves four kinds of customer with four products, plus an internal platform, and each product has one accountable leader. Its 40 stream-aligned teams and nine platform teams sit on one map, which shows which customers have teams of their own. At each stage of its growth Encore made product decisions by default, Partner Listings among them. Verified Resale is proposed to replace that arrangement, as a bet still to be tested.

**Exercise 1.2.** Draw your own organization's products, customers and teams on one page, in the manner of Figure 1.2. Mark every team that serves no customer you can name, and every product with no single accountable owner.

### 1.3 The Four Risks and the Product Trio

#### Value, usability, feasibility, viability {#c1-four-risks}

Every product idea is a bundle of guesses, and a useful way to sort them is by what could make the idea fail. Marty Cagan's essay "The Four Big Risks" (2017) gives the standard sorting. **Value risk** is the risk that customers will not buy the product or choose to use it. **Usability risk** is the risk that they cannot figure out how to use it. **Feasibility risk** is the risk that the engineers cannot build it with the time, skills and technology the company has. **Business viability risk** is the risk that the solution does not work for the other parts of the business: sales, finance, legal, partners, brand. **Discovery**, the work this book teaches in Chapter 3, is the activity of reducing these four risks before the cost of delivery is spent.

The four risks reward being written down for a particular idea, because each idea carries them in different proportions. Figure 1.3 does this for Verified Resale, as the trio first wrote it.

| Risk | The question for Verified Resale | Owner in the trio | Evidence at the start |
|---|---|---|---|
| Value | Will fans trust a reissued ticket, and will organizers switch resale on? | Product manager | Support cases about failed resold tickets; no evidence that organizers want it |
| Usability | Can a seller tell that the old ticket is dead, and can a buyer tell that the new one is real? | Designer | None |
| Feasibility | Can Encore revoke a ticket that already sits in a fan's phone? | Tech lead | Rotating in-app barcodes exist; wallet passes unknown |
| Viability | Will partners accept the cap, will the fee survive consumer law, can Encore carry the money? | Product manager | Rowmate's interest; no legal review yet |
| Ethics | Should a company that fights scalpers run a resale market at all? | All three | An argument inside the company, unresolved |

*Figure 1.3 — The four risks of Verified Resale, with the fifth question added, as the trio first wrote them. The last column is mostly empty, and saying so plainly is the point of the exercise.*

#### Viability is many stakeholders {#c1-viability}

Viability is the risk teams most often see last, because it does not show up in a prototype. A fan can be shown a resale screen and asked what she thinks; a regulator cannot. Cagan spells viability out as a set of constraints from the rest of the business: whether the product can be sold and marketed, whether it fits existing contracts, whether it is legal, whether it can be paid for and whether it keeps the brand's promises. For Verified Resale each of these has a name. Consumer law constrains resale prices in some markets: Ireland's Sale of Tickets Act 2021, in force since 31 July 2021, bans resale above the original price for designated events and venues, and Chapter 5 takes up what that means for Encore's fee. Finance must decide how a fee shared among three parties is recognized as revenue. Organizers' contracts must be amended to give them rules and a share. The European Union's Digital Services Act treats Encore, for resale, as an online marketplace, which is another reason to admit fans and no professional resellers, since traders would bring obligations to trace and verify them. And Encore must not end up holding other people's money, which would require a payment license; the trio's early answer is to route resale payments through the primary payment provider's marketplace product.

None of these constraints is an engineering question, and every one of them could kill the product. Cagan and his co-authors argue in *TRANSFORMED* (2024) that the people who hold these constraints, in legal, finance, sales and partnerships, are partners of the product team, to be brought into discovery early; a team that visits them only at the end for approval learns their constraints when it is most expensive to meet them. The way they actually join a team's discovery is the Software book's Section 9.3. Here it is enough to say that viability is a whole list of risks, each owned by a different part of the company, and that the product manager's job is to know them all before the memo is written.

#### The ethical risk {#c1-ethical-risk}

There is a fifth question, older in Cagan's writing than is often assumed. The second edition of *INSPIRED* (2017) already asks, in a short passage on ethics, whether we should build something at all, and *TRANSFORMED* returns to it under the heading of ethical risk. Teresa Torres, in *Continuous Discovery Habits* (2021), lists ethical assumptions as one of five kinds a team should test. The question differs from the other four. Value, usability, feasibility and viability ask whether the product will work. The ethical question asks whether it should, and who bears the cost if it does.

For Verified Resale the ethical question is sharp. Encore's brand rests on fighting scalpers, on the promise that real fans get a fair chance at seats. Even a resale market with a face-value cap, run only for fans, could be read as normalizing the secondary market Encore has always opposed. And if bots get through the screening, it is a real fan who is outbid for a seat that should have been hers. The trio cannot answer this question with an interview or a prototype. It is a strategic question as much as an ethical one, and Chapter 2 gives it the strategic answer the company eventually reached. What this chapter insists on is that it is asked out loud, in the memo, by the people proposing the product, before anyone else has to ask it for them. Encore has already settled one ethical question permanently: it will never run individual price experiments on fans.

#### The trio {#c1-trio}

Who carries these risks? Cagan's answer is that each belongs to a role. The product manager owns value and viability, the product designer owns usability, and the tech lead owns feasibility. The three together are what Torres calls the **product trio**: the product manager, the designer and the tech lead who share responsibility for discovering what their team should build. The definition contains its own instruction. The three work as one unit from the first interview, and none of them waits for another to finish. A designer who receives requirements from a product manager and passes screens to an engineer is in a relay, and each handover loses what the previous runner learned.

A surgical team is a useful picture, up to a point. The surgeon, the anesthetist and the scrub nurse each own a different risk to the patient, and none of them could take over another's job. Yet they work on the same patient at the same time, each watching what the others are doing, and an operation in which they took turns would be absurd. The analogy breaks where the trio's work is least like surgery: the surgical team knows what operation it is performing, and the trio is still finding out. That uncertainty is exactly why the three must be in the same conversations, since each will notice different things in the same interview.

Encore's resale trio was formed for the winter's work. Amira, the product manager, came from the Partner APIs team, where she had inherited Partner Listings and its complaints. Paolo, the designer, came from the Organizer Console team, and knew organizers' working days better than anyone else at Encore. Katrin, the tech lead, came from Orders & Payments, where she had worked on the purchase saga, and had worked against the barcode core from the purchase side for years, which made her one of the few people outside the Inventory team who understood it. All three keep their old teams for now; if the bet is made, they will form the core of a new Resale team. Cagan and Torres both treat the trio as practitioner consensus, without a controlled study behind it, and this book presents it the same way. It recommends the trio because a relay loses, at each handover, what the previous role learned, and because discovery depends on what each role notices.

#### The tech lead in discovery {#c1-tech-lead}

Of the three, the tech lead is the one most often left out of discovery, and leaving her out costs the most. Engineers who join only when delivery begins arrive after the product has been shaped, and the most valuable thing they know, what has recently become possible and what is harder than it looks, arrives too late to change the shape. Cagan's tool for bringing it in early is the **feasibility prototype**: a small piece of throwaway code written to answer one question about whether something can be built, before anyone commits to building it.

Katrin's first question was the one Figure 1.3 records: once a ticket is resold, can Encore make the seller's copy stop working? In Encore's own app the answer was already yes, because the barcode there rotates and the app can be told to stop generating it. Wallet passes were less certain, so she spent a week finding out. For Google Wallet, an issuer can mark a ticket pass as expired, and the pass moves to the expired section, but only once the phone has synchronized. For Apple Wallet, the update mechanism is a push notification asking the phone to fetch the new pass, and Apple's own documentation warns that such notifications are not guaranteed to be delivered. The prototype's finding was therefore that no phone could be trusted to remove the old ticket. The only place where revocation could be guaranteed was the gate, by giving every venue's scanners a list of revoked barcodes they hold even when offline.

That one finding changed the product before any of it was built. It added the Venue Entry team, which owns the door scanners, to the teams the bet would touch. It changed what the seller would be told, since the honest message is that the old ticket will be refused at the door, whatever the phone still shows. And it turned a promise the trio had been about to make in the memo, that the old ticket would vanish from the seller's phone, into one Encore could keep. The engineering of revocation belongs to the Software book; Chapter 3 returns to this prototype as an example of its kind.

#### Discovery and delivery as two tracks {#c1-two-tracks}

If discovery reduces risk before delivery, it is tempting to treat the two as phases: first we discover, then we build. Practice has settled on a different arrangement, and its origin is worth knowing. In 2007 Desirée Sy described in the *Journal of Usability Studies* how her team at Alias, later part of Autodesk, ran user research and design one iteration ahead of development, in parallel tracks, so that designs were tested before they were built while the previous iteration's designs were being built. Jeff Patton, in an essay of 2017 that credits Sy and notes that Cagan spread the term, calls the arrangement **dual-track development**: one team running discovery, which produces validated ideas, alongside delivery, which produces releasable software, continuously and at the same time. His summary of why it matters is hard to improve: "The most expensive way to test your idea is to build production quality software." Patton insists on one condition. The two tracks are not two teams and not two phases; the same people work in both, every week.

A touring production offers a good picture of the arrangement. While the crew loads in and runs tonight's show, an advance team is already at next week's venues, checking the stage dimensions, the power supply and the loading dock, so that problems are found while they are still cheap to solve. The analogy holds for the rhythm: the advance work never stops while the tour is running. It breaks on one important point. The advance team visits venues that already exist, while discovery explores products that do not exist yet, and much of what it learns is that the planned destination should change. Feasibility questions, such as Katrin's, are where architecture work enters discovery; the Architecture book's Chapter 1 showed how the characteristics a system must have are heard in what the business says, and the tech lead is the person in the trio who listens for them.

**Recap.** Cagan's four risks, value, usability, feasibility and viability, sort what could make a product fail, and the ethical question asks whether it should be built at all. The product manager, designer and tech lead own the risks together as a trio, working as one unit from the first interview. A tech lead in discovery can change a product before it is built, as Katrin's wallet prototype did. Discovery and delivery run as two continuous tracks worked by the same people.

**Exercise 1.3.** For one feature on your roadmap, write one sentence per risk naming the evidence you have, or saying plainly that you have none. Then add a sentence for the ethical question, and name who in your organization would answer it if you did not.

### 1.4 The Product Operating Model

#### Three changes {#c1-three-changes}

Most companies that adopt the practices of this chapter adopt them one at a time, and get less from each than they expected, because the practices depend on one another. Cagan and his co-authors, in *TRANSFORMED* (2024), describe the whole as the **product operating model**: a way of building, solving problems and deciding which problems to solve, in which teams are given problems to solve and judged by outcomes. They describe the move to it as three changes. The first changes how a company builds: small, frequent, independent releases instead of large and infrequent ones. The second changes how it solves problems: discovery before delivery, by the team that will build the solution. The third changes how it decides which problems to solve: from a list of features chosen by stakeholders to a strategy, made from insight and turned into objectives for teams.

The evidence behind these three changes is uneven, and it is worth being exact about it. The first change has strong quantitative support from a decade of research by DORA (DevOps Research and Assessment), which the Software book's Section 1.1 examines. The second and third rest on case stories, many of them gathered in *TRANSFORMED* itself, and on long practice; nobody has run a comparative study. The best large-scale demonstration is public. In 2014 the British government made the same three changes into policy with its Digital by Default Service Standard, and its current version, of 2019, has 14 points, among them "Understand users and their needs", "Have a multidisciplinary team", "Iterate and improve frequently" and "Define what success looks like and publish performance data". Central government services in the United Kingdom are expected to meet the standard, and many are formally assessed against it before they go live. Encore has made the first change thoroughly; it deploys about 180 times a working day. It has made the second change only where trios exist, and the third only in parts of the company.

#### Empowered teams, feature teams, delivery teams {#c1-empowered-teams}

The difference that matters most is what a team is given. Cagan's essay "Product vs. Feature Teams" (2019), developed in *EMPOWERED* (2020) with Chris Jones, names three kinds of team, and Figure 1.4 sets them side by side.

| | Delivery team | Feature team | Empowered product team |
|---|---|---|---|
| What it is given | A backlog | A roadmap of features | A problem and an outcome |
| Who owns value and viability | The stakeholder who asked | The stakeholder who asked | The team |
| Product role | A product owner as "backlog administrator" | A project manager in all but name | A product manager in a trio |
| What it is judged by | Velocity | Features shipped on time | The outcome |

*Figure 1.4 — Three kinds of team, after Cagan and Jones. The difference lies in what leaders assign, and the same people can work in any of the three.*

An **empowered product team** is a cross-functional team given a problem to solve and an outcome to reach, and trusted to find the solution. Cagan's description of feature teams as "all about output" is exact: they deliver what is asked of them, and someone else carries the risk that it will not work. The most important observation in his essay is about cause. A team is usually a feature team, he writes, because "the leadership does not yet trust that particular team." Whether a team is empowered is decided by what its leaders assign, and that is why a team cannot simply decide to become empowered. At Encore the fan storefront's teams are given problems such as "more admitted fans complete a purchase", and the organizer console's teams have been given lists. The difference between them lies in what each was given to do, whatever the talent of the people.

#### Strategic context {#c1-strategic-context}

Empowerment alone is dangerous at scale. Forty teams, each solving its own problem in its own way, will pull in forty directions unless something holds them together. Cagan and Jones's answer is **strategic context**: the shared knowledge, provided by leaders, that lets empowered teams make decisions consistent with each other and with the company's direction. They name five elements, and this book uses their names and gives each a precise meaning.

A **product vision** is the future the company is trying to create for its customers, described far enough ahead, usually several years, to inspire and to guide many teams at once. **Product principles** are the beliefs that guide trade-offs when the vision does not settle them; one of Verified Resale's will be that the fan never pays more than the organizer allows. The **team topology** is how the teams are divided, and what each is responsible for, the subject of Figure 1.2. The **product strategy** is the choice of which problems to solve, in what order, to move toward the vision; it is the subject of Chapter 2. And **team objectives** are the specific problems each team is asked to solve, with the outcomes by which progress will be judged, which Section 2.5 turns into practice.

Of the five, strategy is the one most often missing, and its absence is the hardest to see. A company can have an inspiring vision, sensible principles and a well-drawn topology, and still hand its teams a list of features each quarter, because nobody has decided which problems matter most. That gap is where the organizer console's queue came from. The Software book's Section 9.3 covers the engineering roles that make strategic context work across 40 teams; the context itself, and the strategy at its heart, are this book's subject.

#### Working with sales, finance and leadership {#c1-sales-finance}

A product team does not decide alone, and the product operating model changes its relation to the rest of the company in three ways. With sales, commitments to customers become inputs to discovery, and stop being placed directly on a team's work. The organizer sales team still hears what organizers want, and its knowledge is invaluable, but what it brings back is now a problem to be assessed, as in the opportunity assessment of Section 1.1, where it used to be a solution with a date. Chapter 3 shows how such requests are handled in discovery. Organizer sales is Encore's hard case, because its requests are attached to contracts with renewal dates, and saying "we will look into the problem" to a commercial director with a renewal on Friday takes nerve and support from above.

With finance, the change is from funding projects to funding teams, so that a team can stay with a problem long enough to solve it. Anyone who has lived through a large bank's annual budget round, as I have, knows how strongly the project shape is held in place by the way money is approved. The mechanics of the change are the Software book's Section 10.4. With leadership, the change is from reviewing roadmaps to reviewing outcomes, and from approving features to providing context. Verified Resale's leaders will see it as a bet memo, with a diagnosis, the outcome it aims for, the guardrails it must not break and the conditions under which it would be stopped. Amazon's PR/FAQ, the press release and questions written before any work begins, which Colin Bryar and Bill Carr describe in *Working Backwards* (2021), is a heavier form of the same document. Chapter 10 follows Encore's memo from the day it is written.

#### Innovation theater {#c1-innovation-theater}

There is a failure that looks like success, and it deserves a name. A company can adopt the whole vocabulary of this chapter, trios, outcomes, discovery and objectives, and change nothing about who decides what is built. *TRANSFORMED* warns of it in a passage on what it calls "innovation theatre", and the term is in wide use for visible innovation activity, labs and hackathons among them, that never reaches the product teams. I use **theater** here, in a slightly broader sense, for any adoption of the product operating model's language without its transfer of decisions.

The signs are recognizable. A roadmap renamed an "outcome roadmap" still lists features, each with a metric attached after the fact. Discovery is run after the decision has been made, to confirm it. Objectives are set for teams and then overridden whenever a large customer asks. The trio exists on the organization chart, but the product manager's real job is to take requests from stakeholders and turn them into tickets. Each sign is a gap between what the company says and who actually decides. Encore's organizer console was showing two of them when the Verified Resale proposal arrived: its teams had trios and objectives, and their work still arrived through the queue.

**Recap.** The product operating model consists of three changes, in how a company builds, solves problems and decides which problems to solve, and only the first has strong quantitative evidence. Empowered teams are given problems and outcomes; feature teams are given features; the difference is set by leaders. Strategic context, made of vision, principles, topology, strategy and objectives, keeps empowered teams pulling the same way. Theater is adopting the vocabulary without moving the decisions.

**Exercise 1.4.** List everyone in your company who can add an item to a team's work without that team's agreement. For each path, decide whether it should remain a direct path or become an input to discovery, and say who would have to agree to the change.

### 1.5 What the AI Era Changes, and What It Does Not

#### Cheaper construction, unchanged essence {#c1-cheaper-construction}

AI assistance has lowered the cost of producing code, and the Architecture book's Section 15.4 argued what that means for architecture: as code gets cheaper to produce, judgment becomes the scarce part of the work. The product consequence follows directly, and it is the only new thing this section adds. If building gets cheaper while deciding stays as hard as it was, then building the wrong thing becomes a larger share of what a product costs. Brooks's remedy for the hardest part, prototypes put in front of the people who will use the system, becomes cheaper to apply. It does not become unnecessary, because the prototype still has to be shown to someone, and someone still has to decide what it showed.

#### The build trap, faster {#c1-build-trap-faster}

An organization caught in the build trap measures itself by what it ships. Give it tools that make shipping cheaper, and we should expect it to ship more: more features, more surface area, more for users to learn and more for teams to own. The cost of ownership is already known. Robert Glass's widely cited estimate, which the Architecture book's Section 13.3 uses, puts maintenance at 40% to 80% of software's cost, about 60% on average. If two-thirds of ideas fail to move the metric they were meant to move, as Microsoft's experiments found, then an organization that ships twice as many ideas without examining them acquires twice as many unused features to maintain. No published study has yet measured whether AI assistance inflates feature counts in this way, so this is an expectation, drawn from known costs. It is a reason to put the outcome review of Section 1.1 in place before the cheaper tools arrive in force.

#### The evidence so far, in brief {#c1-ai-evidence}

The evidence on AI assistance and developer productivity is young, mixed and moving, and the Software book's Section 5.1 examines it in full. In a laboratory task, Peng and colleagues found in 2023 that developers with GitHub Copilot finished one programming task 55.8% faster. In field experiments with 4,867 developers at three companies, Cui and colleagues, in *Management Science* in 2026, found about 26% more completed tasks, with larger gains for less experienced developers. In contrast, METR's study of 16 experienced open-source developers working in their own mature repositories found them 19% slower in early 2025, although they believed they had been faster; METR has since marked that result out of date, and reported in February 2026 that its newer data are too weak to size the effect. DORA's report of September 2025 linked AI adoption to higher delivery throughput, a reversal of its 2024 finding, while delivery stability still declined. The honest summary is that the gains are real but uneven, and that perceived speed tends to run ahead of measured speed.

#### Where AI helps deciding {#c1-ai-deciding}

For product work, the most promising effect of AI is on discovery itself: prototypes that once took a sprint can now be produced in hours, so a trio can put more versions of an idea in front of customers before choosing. That practice is young, and Section 3.5 presents it as emerging, with the practitioner accounts it rests on. AI also changes the four risks when the product itself contains an AI feature, and here the practice is established. Feasibility then includes whether the feature passes evaluations against a set of real cases, and viability includes what each use costs in model tokens, which Encore already counts in its cost per ticket, as the Resilience book's Section 2.5 shows. Verified Resale will have one such feature, an assistant that turns an organizer's plain-language rules into the typed rules the platform enforces, and Chapter 6 designs it.

#### The rule for this book {#c1-rule}

Every claim this book makes about practice, AI or otherwise, is held to one rule, which the Software book shares: proven practices only; anything emerging is labelled and carries a real, specific account of use. For AI claims in particular, that means treating each one as a product team treats a hypothesis. It needs a named source, a stated setting and a measured result, and the reader should be told whether it is proven or emerging. The rule applies to the book the same discipline the book asks of product teams.

**Recap.** Cheaper construction leaves the hardest part, deciding what to build, as hard as it was, so the cost of deciding wrongly grows as a share of the whole. An organization in the build trap will use cheaper tools to ship more unexamined work, and the remedy is the outcome review, installed early. The evidence on AI productivity is mixed and moving, and this book labels every claim as proven or emerging.

**Exercise 1.5.** Find one claim about AI productivity made inside your company. Trace it to its evidence: which study or measurement, in what setting, measuring what. If it traces to nothing, write down what measurement would settle it.

### Kata: The Policy Factory

> **Your brief: "Haverlock Insurance."** Haverlock sells home and motor insurance in three EU countries, through its own website and app and through 2,000 independent brokers who use a broker portal. Its 150 engineers work in 22 teams, and every one of them is funded project by project. Each autumn the business units bid for the next year's projects, a steering committee ranks them, and teams are assembled to deliver the winners and disbanded when the projects close. Last year Haverlock delivered 31 of its 34 approved projects on schedule, and the steering committee called it the best year on record. In the same year online quotes that became policies fell from 14% to 11%, broker complaints about the portal doubled, and nobody could say which of the 31 projects had been meant to change either number. The largest broker network has threatened to move its business unless the portal "gets the features we were promised". The chief executive has asked you to explain what went wrong in a year when everything was delivered, and to propose a different way of working for three areas: online quotes, the broker portal and claims.

**Deliverables:**

1. **The diagnosis** — A one-page account of Haverlock's build trap. Name its outputs and the outcomes nobody measured, say which of Perri's three distortions dominates in each area, and answer her two questions: who came up with the last feature built, and what was the last thing killed.
2. **The product map** — A map of Haverlock's products, customers and teams in the manner of Figure 1.2, marking which customers have teams of their own and which products lack a single accountable owner.
3. **Three empowered teams** — For online quotes, the broker portal and claims, the problem each team would be given, the outcome by which it would be judged and the trio that would lead it.
4. **The four risks** — For the broker network's demand, an opportunity assessment and a table in the manner of Figure 1.3, stating the evidence for each risk or its absence.
5. **The strategic context** — A draft of Haverlock's product vision, three product principles and the objective for each of the three teams.
6. **The outcome review** — A one-page procedure for reviewing every release against its outcome, with who attends, when, and what happens to work that moved nothing.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Outcomes over outputs | Could each team's outcome be measured as a change in what customers or brokers do, rather than as something delivered? |
| Ownership | Does every product on the map have one accountable owner, as USDS's sixth play demands? |
| Honest risk | Does the risk table admit where there is no evidence, especially for viability and for the broker network's demand? |
| Context | Would the three teams, given your vision, principles and objectives, make decisions consistent with each other without a steering committee? |
| Closing the loop | Would your review procedure have told Haverlock, by spring, that the quote rate was falling and which work had been meant to stop it? |
| Realism | Can a company funded project by project make this change within a year, and have you said what finance must change for it to last? |

#### Where you now stand

You can now tell an output from an outcome, and recognize the build trap in a team's work by how that work arrives and whether it is ever judged afterwards. You can draw an organization's products, customers and teams on one map, sort a product idea's risks into value, usability, feasibility, viability and ethics, and say who in a trio owns each. You can name the elements of strategic context, and tell a company that has adopted the product operating model from one that has adopted its vocabulary. What you cannot yet do is decide whether Verified Resale deserves to exist, because that depends on a question this chapter has deliberately left open: what problem Encore is trying to solve, and what it will refuse to do in order to solve it. That is a question of strategy, and Chapter 2 takes it up, beginning with four words on an Apple whiteboard in 1997.

### References

- HHS Office of Inspector General — [*HealthCare.gov: Case Study of CMS Management of the Federal Marketplace*, OEI-06-14-00350](https://oig.hhs.gov/oei/reports/oei-06-14-00350.pdf). US Department of Health and Human Services, 2016 — free online.
- Melissa Perri — [*Escaping the Build Trap: How Effective Product Management Creates Real Value*](https://melissaperri.com/book). O'Reilly, 2018.
- Marty Cagan — [*INSPIRED: How to Create Tech Products Customers Love*, 2nd ed.](https://www.svpg.com/books/inspired-how-to-create-tech-products-customers-love-2nd-edition/). Wiley, 2017.
- Marty Cagan, Chris Jones — [*EMPOWERED: Ordinary People, Extraordinary Products*](https://www.svpg.com/books/empowered-ordinary-people-extraordinary-products/). Wiley, 2020.
- Marty Cagan, Lea Hickman, Christian Idiodi, Chris Jones, Jon Moore — [*TRANSFORMED: Moving to the Product Operating Model*](https://www.svpg.com/books/transformed-moving-to-the-product-operating-model/). Wiley, 2024.
- U.S. Digital Service — [*Digital Services Playbook*](https://github.com/usds/playbook). 2014 — free online.
- Steven Brill — [*Obama's Trauma Team*](https://time.com/10228/obamas-trauma-team/). *Time*, 2014 — free online.
- Frederick P. Brooks Jr. — [*No Silver Bullet: Essence and Accidents of Software Engineering*](https://www.cs.unc.edu/techreports/86-020.pdf). Information Processing 86, IFIP, 1986; reprinted in *The Mythical Man-Month*, anniversary ed., Addison-Wesley, 1995 — free online.
- Josh Seiden — *Outcomes Over Output: Why Customer Behavior Is the Key Metric for Business Success*. Sense & Respond Press, 2019.
- Marty Cagan — [*The Four Big Risks*](https://www.svpg.com/four-big-risks/). SVPG, 2017 — free online.
- Teresa Torres — [*Continuous Discovery Habits*](https://www.producttalk.org/continuous-discovery-habits/). Product Talk, 2021.
- Jeff Patton — [*Dual Track Development is not Duel Track*](https://www.jpattonassociates.com/dual-track-development/). Jeff Patton & Associates, 2017; and Desirée Sy, *Adapting Usability Investigations for Agile User-Centered Design*, *Journal of Usability Studies* 2(3), 2007, 112–132 — free online.
- Ron Kohavi, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, Ya Xu — [*Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained*](https://exp-platform.com/Documents/puzzlingOutcomesInControlledExperiments.pdf). KDD, 2012 — free online.
- Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz — [*The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers*](https://doi.org/10.1287/mnsc.2025.00535). *Management Science*, 2026.
- DORA — [*State of AI-assisted Software Development*](https://dora.dev/research/2025/dora-report/). Google Cloud, 2025 — free online.
- UK Government Digital Service — [*Service Standard*](https://www.gov.uk/service-manual/service-standard). GOV.UK, 2019 — free online.

---

## Chapter 2: Product Strategy — Choosing Where to Play {#ch2}

> "The essence of strategy is choosing what not to do." — Michael E. Porter

Every company that grows past a few teams discovers that it can build almost anything it chooses, and that this is the source of its trouble. A team of nine has no strategy problem worth the name, because its capacity decides for it: there is one product, one queue of work and one conversation about what comes next. A company of 400 engineers has capacity enough to pursue a dozen directions at once, and it will, unless someone decides which directions it will not pursue. The question of this chapter is how that decision is made well. What does a sound product strategy look like on the page, how do we tell it from the fluent documents that only resemble one, and how does it reach the 40 teams who must act on it without being flattened into a list of features?

The story we will use to answer it is a whiteboard. In 1997, newly returned to an Apple that was losing money at an alarming rate, Steve Jobs stopped a product review, drew two lines and wrote four words around them: consumer and professional, desktop and portable. Everything Apple made would fit in one of those four boxes, and everything that did not fit would go. The grid is famous because it is simple, but its simplicity was bought with a great deal of refusal, and it is the refusal that teaches. Section 2.1 tells it carefully, because the popular version blurs two accounts that teach different things.

Encore is about to write a strategy of its own. In Chapter 1 we left the company at about 400 engineers, with a proposal on the table called Verified Resale: fans who cannot attend a show would resell their tickets through authorized partners such as Rowmate, Encore would reissue each resold ticket under a new barcode, and organizers would set the rules and share the fee. The proposal carries an awkward tension. For years Encore's brand has rested on fighting scalpers, on the promise that real fans get a fair chance at seats, and now it proposes to host resale. Some people inside the company hear that as a betrayal. Others hear it as the only honest response to a market that already exists. A strategy has to reconcile the two, and it can do so only by saying precisely what problem Encore faces and what it will do about it.

This chapter follows the writing of that strategy in the late winter of Encore's ninth year, as the first page of the bet memo that Chapter 10 will return to. We begin with Richard Rumelt's account of what a strategy must contain (Section 2.1), and then look at the people the strategy serves through the lens of the jobs they are trying to get done (Section 2.2). Verified Resale is a market with several sides, and Section 2.3 examines what that means for strategy. Section 2.4 maps the landscape to show where Encore's advantage lies, and Section 2.5 turns the strategy into objectives that teams can own.

### 2.1 Good Strategy and Bad

#### The grid on the whiteboard {#c2-four-quadrants}

Apple bought NeXT in a deal announced on 20 December 1996 and completed in February 1997, and the purchase brought Steve Jobs back to the company he had co-founded. At first he came as an adviser. At Apple's Worldwide Developers Conference in May 1997 he took questions from a hall full of developers, some of them angry at the projects Apple had cancelled, and in answering one hostile question he said something close to "focusing is about saying no". In July the board removed Gil Amelio as chief executive. In August, at Macworld Boston, Jobs announced a $150 million investment by Microsoft, a rival's money that told the market Apple would survive the year, and in September he became interim chief executive.

The grid comes to us from Walter Isaacson's biography, *Steve Jobs* (2011). Isaacson describes weeks of product reviews of a Macintosh line of roughly a dozen models with confusing numbers. Then, at one large product strategy session, Jobs called a halt. In Isaacson's telling, Jobs shouted "Stop!", said "This is crazy", and drew "a horizontal and vertical line to make a four-squared chart". Atop the two columns he wrote "Consumer" and "Pro", and he labeled the two rows "Desktop" and "Portable". Their job, he told the room, was "to make four great products, one for each quadrant". Isaacson quotes Phil Schiller, who was in the room: "The room was in dumb silence."

Apple then took about two years to fill the grid, as Figure 2.1 shows.

| | Consumer | Pro |
|---|---|---|
| **Desktop** | iMac, announced May 1998, shipped August 1998 | Power Macintosh G3, announced November 1997 |
| **Portable** | iBook, unveiled at Macworld New York, 21 July 1999, at $1,599 | PowerBook G3 |

*Figure 2.1 — Apple's four-quadrant grid as it was filled. The consumer portable box stayed empty until the iBook arrived in July 1999.*

The empty box deserves a moment. When the technology newsletter TidBITS described the four-slot strategy in May 1998, the consumer portable slot had no product in it, and it would stay that way for more than a year. A company under pressure to show growth is tempted to put something in every slot, and Apple did not. The grid was a commitment about what Apple would make, and it was equally a commitment about how long Apple would wait. The results came quickly enough to be read as a verdict. Apple lost about $1.05 billion in fiscal 1997, and in fiscal 1998 it earned $309 million on $5.94 billion of revenue, its first profitable year since 1995. The iMac is generally credited with the turnaround.

Rumelt tells the same turnaround in the first chapter of *Good Strategy Bad Strategy* (2011), and his version is blunter. He does not mention the grid. He writes that by September 1997 Apple was "two months from bankruptcy", and that Jobs "cut Apple back to a core that could survive". Then comes the list: "Jobs cut all of the desktop models—there were fifteen—back to one. He cut all portable and handheld models back to one laptop. He completely cut out all the printers and other peripherals. He cut development engineers. He cut software development. He cut distributors and cut out five of the company's six national retailers. He cut out virtually all manufacturing, moving it offshore to Taiwan." Rumelt calls the response "obvious and, at the same time, unexpected", because analysts had expected either a push into advanced products or a sale of the company.

The two accounts do not match exactly. By late 1998 Apple sold both the Power Macintosh G3 and the iMac, which is more than Rumelt's "one desktop", and it is wise not to merge them into one tidy legend. Read together, they describe two halves of a single act. Isaacson's grid is the design of the focus, the frame that made most product decisions automatic, since anything outside the four boxes had no claim on the company's attention. Rumelt's list is the cuts that paid for it, and it reaches well beyond products, into retail, manufacturing and engineering headcount. The grid alone would have changed little without the cuts that enforced it.

Rumelt adds a coda that is easy to miss. In 1998 he asked Jobs about Apple's long-term prospects, given that it held less than 4 percent of the personal computer market and faced the network effects of the Wintel standard. Jobs, Rumelt reports, "just smiled and said, 'I am going to wait for the next big thing.'" The grid was never meant to beat Wintel. It was meant to keep Apple alive and coherent until a better opportunity appeared, and that modesty is part of why it worked. It is also the clearest picture we have of the epigraph's lesson, Porter's line from 1996, because nearly everything the grid decided was a decision about what Apple would stop making.

#### The kernel {#c2-kernel}

Rumelt's central contribution is a description of what any good strategy contains, whatever its subject. He calls it the kernel. The **kernel of a strategy** is three elements that work together: a diagnosis that defines the challenge, a guiding policy for dealing with it, and coherent action that carries the policy out. The diagnosis names what is really going on, and it simplifies a complicated situation by choosing which of its many facts matter. The guiding policy is an overall approach chosen to cope with the obstacles the diagnosis identified; it rules some actions in and many more out. The coherent action is a set of steps that reinforce one another, coordinated so that each makes the others more effective.

The kernel can be read against Apple's year with little effort. The diagnosis was that the product line had become too complicated to explain, build or sell, and that the company was running out of cash while it tried. The guiding policy was the grid: four great products and nothing else. The coherent actions were the cuts and the products, from the closure of retail channels to the move of manufacturing to Taiwan, and they made sense only together. Cutting retailers without cutting products would have left inventory nobody could sell, and cutting products without fixing manufacturing would have left factories nobody could use.

What makes the kernel useful is that it is hard to fake. A document can hold ambitious goals, eloquent values and many initiatives and still have no diagnosis, and once we look for the three parts their absence is obvious. A strategy without a diagnosis is only a wish, however well it is written, because it never says what obstacle it means to overcome. The other two parts fail in the same way when they stand alone: a diagnosis with no guiding policy leaves everyone agreeing about the problem and doing what they did before, and a guiding policy with no coherent action changes the vocabulary of meetings and little else.

#### Four hallmarks of bad strategy {#c2-bad-strategy}

Rumelt is at least as interesting on what goes wrong. He names four hallmarks of **bad strategy**, by which he means a document that occupies the place of a strategy without doing a strategy's work. The first is fluff: words that sound important and say little, such as superlatives and buzzwords, which give the appearance of insight. The second is failure to face the challenge, which means never naming the obstacle, so that nothing in the strategy can be checked against it. The third is mistaking goals for strategy, as when "grow revenue 20%" is presented as though announcing a goal were the same as finding a way to reach it. The fourth is bad strategic objectives, which Rumelt splits into two kinds: the "dog's dinner", a long list of things to do with no priority among them, and the "blue-sky" objective, which merely restates the wish in the form of a target.

Encore's first draft of a resale strategy came out of a leadership offsite and fits on one line: *become the most trusted resale destination in Europe*. Figure 2.2 checks it against Rumelt's four hallmarks.

| Hallmark | The question to ask | Encore's first draft |
|---|---|---|
| Fluff | Does any word do work, or only sound important? | Fails. "Most trusted" names no behavior anyone could check. |
| Failure to face the challenge | Does it name the obstacle? | Fails. It never mentions fraud, duplicated tickets or the conflict with Encore's anti-scalper brand. |
| Mistaking goals for strategy | Does it say how, or only what? | Fails. It is a destination with no route. |
| Bad strategic objectives | Is it a long, unordered list, or a wish restated as a target? | Not yet. There are no objectives to judge, which is itself a warning. |

*Figure 2.2 — Encore's first resale strategy against Rumelt's hallmarks of bad strategy. Three clear failures, and a fourth test that cannot even be applied.*

The draft was written by capable people who wanted to inspire, and a sentence like that can survive months of meetings, because it offends nobody and commits nobody. The repair has to start where the draft is silent, with the diagnosis.

#### Diagnosing Encore's resale problem {#c2-diagnosis}

The first fact in Encore's diagnosis is that resale of Encore tickets already happens, and has for years. Some of it happens on unofficial marketplaces, where Encore sees nothing. Some of it happens through Partner Listings, the arrangement from Encore's sixth year under which authorized partners could read Encore's event listings and post resale offers, shown as "resale available at Rowmate" links on sold-out event pages. Under Partner Listings the ticket itself changed hands outside Encore: the seller forwarded the original pass, and Encore checked nothing beyond the partner's word. That arrangement had four weaknesses, and the memo names each of them. A barcode could be duplicated and sold to several buyers. Organizers had no control over price or timing. Organizers received no share of the fee. And buyers went unscreened, so the bots that Encore stopped at the primary sale could buy freely in the resale.

The company had numbers to put behind those weaknesses, and the memo used them. In the twelve months before the memo, Encore's Support team handled about 3,400 cases from fans who arrived at a door, or tried to, with a resold ticket that had already been used or had never existed. About 7% of tickets to sold-out shows were transferred between accounts or scanned on a device the buyer had never used, a rough measure of how much resale already flowed through Encore's own tickets. And within a day of the Vesper Hale on-sale, Trust & Safety counted more than 9,000 tickets for the tour listed on unofficial sites, most of them well above face value. These are Encore's own figures, measured from its scan and support data, and the memo says how each was measured.

The harms fell on three parties. Fans were defrauded, and they blamed Encore, because Encore's name was on the ticket. Organizers lost control of who sat in their seats and at what price, and earned nothing from the trade. And Encore's brand absorbed complaints about transactions it had never seen. Reading those facts, the trio responsible for the proposal reached a diagnosis that changed the argument inside the company: **the harm comes from resale that nobody controls, and the existence of resale is the lesser part of it**. Fans who cannot attend will always pass on their tickets, by one route or another. The question is whether they do so through a channel where the rules can be enforced.

There is a well-documented reason why such a diagnosis meets suspicion, and the memo addressed it directly. On 2 February 2009, when Bruce Springsteen tickets went on sale, Ticketmaster's site showed "No Tickets Found" to many fans and steered them to its own resale subsidiary, TicketsNow, where the same tickets were listed at prices often several times face value. The US Federal Trade Commission settled with Ticketmaster in February 2010; Ticketmaster agreed to refund the difference to affected buyers, without admitting wrongdoing, and in September 2010 the FTC reported sending claim forms to 1,174 consumers. The case is the standard example of a primary seller that owned a resale market with the wrong incentives, and it is exactly the suspicion Encore's fans and organizers would bring to Verified Resale. (The later action by the UK's Competition and Markets Authority against Viagogo, which Section 5.5 tells, shows the same market from the other side.) A diagnosis that ignored this history would have failed Rumelt's second hallmark all over again.

#### A guiding policy and coherent actions {#c2-guiding-policy}

From that diagnosis the guiding policy follows almost directly: **bring resale inside Encore, where every rule can be enforced at the barcode**. Encore's position on resale is control, not prohibition. The policy settles in one sentence the argument between "we fight scalpers" and "we will now host resale", because it reframes the fight against scalpers as a fight against resale nobody controls, and the barcode is the one place where Encore can enforce rules that nobody else can.

The coherent actions then follow from the policy, and each reinforces the others. Every resold ticket is reissued under a new ticket identity, and the seller's old barcode is revoked at every gate, so a ticket cannot be sold twice or used by the seller after the sale. The price is capped at face value, and organizers may only tighten the rules: disable resale, shorten the window or lower the per-fan limits. Only tickets bought through the Sale Gate, within the event's per-fan limit, may be listed. Every resale buyer passes the same Bot Screening as a primary buyer. Only certified partners may list, and the buyer's fee is shared with the partner and the organizer. Remove any one of these and the others weaken. Reissue without screening would hand clean tickets to bots; screening without the cap would let speculators in through a polite door; the cap without reissue could not be enforced, because a ticket sold outside the system would carry no record of its price.

The policy is not untested in the world. In August 2018 Ticketmaster announced that it would close its European secondary sites, Seatwave and GetMeIn. New listings stopped on 13 August, the sites closed in the United Kingdom and Ireland that October, and the rest of Europe followed. In their place fans got an exchange inside Ticketmaster, where tickets resell at face value or less. Ticketmaster's UK managing director, Andrew Parsons, said the move "had always been the long-term plan", and contemporary coverage connected it with the CMA's investigation and with Irish legislation. Whatever the motive, it is a large primary ticketer carrying out the same guiding policy that Encore's memo proposes: resale brought inside, where the seller of record can enforce its rules.

A. G. Lafley and Roger Martin, in *Playing to Win* (2013), gave us the phrase in this chapter's title, "where to play", together with its partner, "how to win", and their account of strategy at Procter & Gamble is a well-documented example of choices made as a connected set. One of their questions is especially useful at this point: what would have to be true for this choice to be a good one? For Verified Resale, several things would have to be true. Fans would have to trust a reissued ticket. Partners would have to accept a face-value cap that cuts their usual take. Organizers would have to want control enough to switch resale on. Each of those is an assumption, and Chapter 3 tests them one by one, beginning with the riskiest. The question turns a strategy into a list of claims that can be checked, which is the bridge from this chapter to the next.

The memo's first page records the kernel in a form short enough to be read in a minute and specific enough to be argued with.

```text
VERIFIED RESALE: STRATEGY KERNEL (bet memo, page 1, month 0)
Diagnosis       Encore tickets are already resold, off Encore and through Partner
                Listings, with no reissue, no organizer control or fee, and no
                screening. Fans are defrauded and blame Encore. The harm comes
                from resale nobody controls.
Guiding policy  Bring resale inside Encore, where every rule is enforced at the barcode.
Coherent        1. Reissue every resold ticket; the old barcode dies at every gate.
actions         2. Cap at face value; organizers may only tighten the rules.
                3. List only tickets bought through the Sale Gate, within limits.
                4. Screen every resale buyer as a primary buyer is screened.
                5. Certified partners only; the 10% buyer fee is split 4/3/3.
Not doing       Resale above face value. Professional resellers. Price tests on fans.
Proximate       One organizer, one partner (Rowmate), one market, end to end.
```

#### Leverage, focus and proximate objectives {#c2-proximate}

Rumelt's later chapters explain why some strategies gain force and others dissipate. He writes of leverage, the concentration of effort on a pivotal point where a modest action produces a large effect, and of focus, which is the refusal to spread effort across every opportunity at once. For Encore the pivotal point is the barcode. Encore issues it, Encore's door scanners check it, and no partner or unofficial marketplace can change that. A rule enforced at the barcode holds everywhere a ticket is used, which is why the guiding policy puts its weight there.

He also writes of proximate objectives. A **proximate objective** is a target close enough that the organization can see how to reach it, so that reaching it is a matter of execution rather than of hope. His example is President Kennedy's 1961 goal of landing a man on the Moon, which sounds like the most distant of objectives. Rumelt argues it was proximate, because the engineering it required was already largely understood, and what remained was a program of work the nation knew how to organize. The more uncertain the situation, Rumelt advises, the closer the objective should be. Encore's situation is very uncertain: it does not yet know whether organizers will switch resale on, or whether fans will trust a reissued ticket. So its proximate objective is small: one organizer, one partner and face-value resale working end to end, in one market, which the launch plan of Chapter 10 later widens to three organizers. "European resale" would have been a blue-sky objective in Rumelt's sense, a wish dressed as a target.

The proximate objective also gives the grid's lesson its sharpest form at Encore. Michael Porter's 1996 article "What Is Strategy?" argued that strategy requires trade-offs: activities that are incompatible, so that choosing one position means giving up another. The kernel's last lines are Encore's trade-offs, written down. There will be no resale above face value, even though partners would earn more from it. There will be no professional resellers who own inventory. There will be no individual price experiments on fans, ever. Each refusal gives up something real, revenue or volume or the freedom to test, and that cost is what makes it a trade-off in Porter's sense.

#### Strategy as deployment {#c2-deployment}

A strategy that exists on page one of a memo has not yet changed anything. It must reach the people who will act on it, and Stephen Bungay's *The Art of Action* (2011), which Melissa Perri builds on in *Escaping the Build Trap*, is useful here. Bungay describes three gaps that open between plans and results. The knowledge gap is the difference between what we would like to know and what we actually know. The alignment gap is the difference between what we want people to do and what they actually do. The effects gap is the difference between what we expect our actions to achieve and what they actually achieve. His remedy draws on Helmuth von Moltke's practice of mission command in the Prussian army: tell people the intent and the reason for it, and let them decide how to act when circumstances change. The Software book's Sections 9.3 and 10.1 take up what that means for forty teams. Perri turns the idea into a cascade, from a company's vision through strategic intents and product initiatives down to the options teams explore. Marty Cagan and Chris Jones, in *Empowered* (2020), describe product strategy in four parts (focus, insights, actions and management) that cover much the same ground. Both are frames drawn from practice. Neither has evidence beyond the record of the companies that use them, and we use them as frames.

Both frames treat strategy as intent to be deployed. The memo tells the Inventory and Partner APIs teams what problem the company is solving and why, and leaves the how to them. Section 2.5 shows how that intent becomes objectives teams can own. Rumelt also insists that a strategy is a hypothesis, and so Encore reviews the kernel twice a year against what the proximate objective has taught it. A diagnosis that was right in late winter can be wrong by autumn.

**Recap.** A good strategy has a kernel: a diagnosis that names the challenge, a guiding policy that rules most actions out, and coherent actions that reinforce one another. Apple's grid was the design of a focus, and the cuts Rumelt lists were what paid for it. Encore's diagnosis is that harm comes from resale nobody controls, so its policy is to bring resale inside and enforce the rules at the barcode, starting with a proximate objective small enough to reach.

**Exercise 2.1.** Take one strategy document from your own organization and rewrite it into Rumelt's three parts. Mark which part was missing or weakest in the original, and write down two things the strategy now rules out that the original did not.

### 2.2 Jobs to Be Done

#### Progress in a circumstance {#c2-progress}

A strategy decides where to play. It cannot decide well without a clear picture of the people it will serve, and the picture an analytics dashboard draws is a poor one for this purpose. Dashboards describe customers by their attributes: age, city, device, how often they buy. Clayton Christensen and his co-authors, in *Competing Against Luck* (2016), argue that attributes correlate with what people buy but do not cause it. People buy a product because something in their life calls for it. They define a **job** as the progress a person is trying to make in a particular circumstance. The circumstance is part of the definition, because the same person has different jobs at different moments, and the product that suits one moment can be useless at another.

The book's most famous story is the milkshake, from field work by Bob Moesta that Christensen reports. A fast-food chain trying to sell more milkshakes found that many were bought early in the morning by commuters, who wanted something to make a long, dull drive more bearable and to keep them full until lunch. In that circumstance, as Harvard Business School's account of the work puts it, the milkshake was hired in place of a bagel or a doughnut, because it was tidy to eat at the wheel and kept hunger away, and a thick drink through a thin straw gave the driver something to do. None of those rivals appeared in the chain's research about milkshakes, which compared its shake only with other shakes. The job has three dimensions, and Christensen insists on all three. There is the functional dimension (stay full until noon), the social dimension (how the choice looks to others), and the emotional dimension (how it feels). A product designed for the functional dimension alone can win the first purchase and still lose the habit.

A better-documented case, also from the book, is Southern New Hampshire University's online program. The university found that adult learners were hiring it to do a very different job from the one eighteen-year-olds hired a campus for: to improve their careers, with as little friction as possible, around jobs and families. Its leaders mapped the admissions process from a prospective student's first inquiry onward and rebuilt it around that job, removing the delays and paperwork that had stopped working adults before, and its online program grew rapidly, as the book recounts. The lesson for us is the integration. Once the job is understood, every part of the operation is arranged around it, including parts that no product team owns.

Jobs to be done is a lens, and an honest account should say so. Its evidence is a strong record of practitioner case studies, with no controlled studies behind it, and there are rival schools. Tony Ulwick's Outcome-Driven Innovation (*What Customers Want*, 2005) turns jobs into quantified outcome statements, and Alan Klement's *When Coffee and Kale Compete* (2016) frames a job around the change a customer wants in themselves. The schools disagree about method and agree on the central claim: we should study the progress people seek, and treat their attributes as clues.

A box-office clerk understands this without the vocabulary. A fan who comes to the window saying "I need to return these" might want money back, or might want the seats to go to someone who will enjoy them, or might simply want not to feel foolish about a purchase they cannot use. The clerk who hears which job is meant can help; one who hears only "refund request" can only apply the policy. The analogy holds until scale enters. A clerk hears one fan at a time and adjusts, while a product serves millions with one design, so the jobs it serves must be chosen in advance and written down, with the risk that the choice is wrong for many.

#### The four parties and their jobs {#c2-four-parties}

Verified Resale serves four parties, and the trio wrote a job statement for each before the memo. They wrote them as hypotheses, to be tested by the discovery work of Chapter 3, and the memo labels them that way.

The first is **the fan who cannot go**. Their functional job is to get their money back, safely and quickly. They also have a social job that the trio heard in nearly every early conversation: not to let down the friends who bought the seats next to theirs, which means the seat should go to someone decent and the group should not be left beside an empty chair or a stranger who paid three times the price. Today this fan's competition is an unofficial marketplace, a ticket passed to a friend of a friend, or, most often, doing nothing at all.

The second is **the fan who wants in**: someone who missed the on-sale and wants a real ticket to a show that sold out, at a price that does not feel like extortion. The functional job is simple. What Encore's interviews found, as the next subsection describes, is that the emotional side of this job weighs more heavily for these fans: the fear of being turned away at the door with a ticket that does not scan.

The third and fourth parties are businesses, and their jobs partly conflict. **The partner**, a marketplace such as Rowmate, wants listings it can trust, a share of the fee and no chargebacks from buyers who were sold a dead ticket. **The organizer** wants control over resale price and timing, a share of the upside, and real fans in the seats, since an arena full of people who paid triple is an arena full of people who will remember it. A partner earns more when more tickets are resold, and an organizer often wants fewer resold tickets, on stricter terms. That conflict is the reason the product's rules matter so much: the rules are where Encore decides, in advance and in public, how the conflict is settled. Figure 2.3 summarizes the four jobs.

| Party | The job, as a hypothesis | What it competes with today | What the product must never break |
|---|---|---|---|
| Fan who cannot go | Get my money back safely and soon, and do not let my friends down | Unofficial sites, a forwarded pass, doing nothing | Payment that arrives, and a buyer who is a real fan |
| Fan who wants in | Get a real ticket to a sold-out show at a fair price, without fear at the door | Unofficial sites, a stranger on social media, giving up | A ticket that scans |
| Partner (Rowmate, later Tessera) | Sell listings I can trust, earn a share, carry no chargebacks | Its own unverified resale | Listings backed by real tickets |
| Organizer | Keep control of price and timing, share the upside, fill seats with fans | Banning resale in its terms, and hoping | Rules that can only tighten |

*Figure 2.3 — The four parties of Verified Resale and the jobs the trio wrote for them. The last column states what each party would never forgive.*

#### The forces behind a switch {#c2-four-forces}

A job statement says what people want. It does not say why they keep doing what they do now, which is usually the harder question. Bob Moesta and Chris Spiek, of the Re-Wired Group, developed the **switch interview** to answer it. A switch interview reconstructs the timeline of a real purchase, the moment a person stopped using one solution and started using another, from the first thought to the final decision. Christensen popularized their method in *Competing Against Luck*, and Moesta set it out himself, with Greg Engle, in *Demand-Side Sales 101* (2020). Their model has four forces. Two pull a person toward a new solution: the push of the current situation, which has become intolerable, and the pull of the new solution, which promises something better. Two hold the person back: the anxiety of the new, the fear that it will not work, and the habit of the present, the comfort of the familiar even when it is bad. A switch happens only when push and pull together outweigh anxiety and habit.

In the six weeks before the memo, the trio interviewed 18 fans who had bought or sold a ticket off Encore in the previous six months. Thirteen of them named, in one form or another, the same anxiety: being turned away at the door with a ticket that did not scan. The trio drew a conclusion that shaped the product. For the fan who wants in, the strongest force is anxiety, so the product's most important promise is certainty at the door, ahead of price or choice. The memo labels this a small-sample Encore result. It is consistent with what Moesta reports more generally, that anxiety about the new solution is the force that most often blocks a switch.

The forces are taught here. The craft of the interview itself, how to ask about the last time something happened and how to avoid asking people to predict their own behavior, belongs to Chapter 3, where Section 3.1 makes such interviews a weekly habit.

#### Non-consumption {#c2-non-consumption}

The most instructive line in Figure 2.3 is the one that says "doing nothing". Christensen and Michael Raynor, in *The Innovator's Solution* (2003), called this **non-consumption**: the situation in which people who have a job to be done hire no product at all, because every available option is too expensive, too difficult or too risky. It is easy to miss, because it leaves no transactions to count, and it is often the largest market there is.

Encore had a way to see it. Its scan data shows which tickets are used and which are not. About 4% of tickets to sold-out shows are never scanned, and almost none of those tickets had been offered for resale anywhere Encore could see. Each one is a seat that a fan paid for and could not use, beside a fan who wanted it and could not get it, at a show the organizer had sold out. The memo used that figure, rather than any industry estimate, to size the opportunity. The fans who already resell are the market Verified Resale would take from unofficial sites. The fans who absorb the loss are the market it could create, provided it removes the anxiety and effort that keep them doing nothing.

**Recap.** A job is the progress a person seeks in a particular circumstance, with functional, social and emotional dimensions, and it is a lens with a strong practitioner record. Encore wrote jobs for the four parties of Verified Resale as hypotheses, found in its switch interviews that anxiety at the door was the dominant force for buying fans, and sized the bet from the fans who resell nothing at all.

**Exercise 2.2.** Write the job statement for your product's most important customer, including its social and emotional dimensions. Then name the real competitor in the customer's circumstance, and if it is "nothing", estimate from your own data how many people choose it.

### 2.3 Multi-Sided Markets

#### Pipelines and platforms {#c2-pipelines-platforms}

Most businesses that engineers have worked in are pipelines. A **pipeline** creates value in a line: it acquires inputs, transforms them and sells the result to customers at the end, and value flows in one direction. A **multi-sided platform** creates value differently, by enabling exchanges between two or more distinct groups who need one another, and its value lies largely in the matches it makes. The economics of such platforms were set out formally by Jean-Charles Rochet and Jean Tirole in "Platform Competition in Two-Sided Markets" (2003), work that the citation for Tirole's 2014 Nobel Prize in economics names. Geoffrey Parker, Marshall Van Alstyne and Sangeet Paul Choudary, in *Platform Revolution* (2016), turned the economics into a practitioner's account. They contrast the pipeline's linear chain with the platform's job of orchestrating interactions, and they describe that job as three functions: pulling participants in, facilitating their exchanges and matching them well.

Publishing offers the oldest familiar example. A newspaper that carried classified advertisements was two businesses in one building. As a pipeline, it gathered news, printed it and sold it to readers. As a platform, it connected people with things to sell to people who wanted to buy them, and readers and advertisers each came because the other did. The second business grew only as both sides grew together, and it collapsed quickly once buyers and sellers found a better place to meet online. The analogy breaks at the point that matters most for Encore. A newspaper never had to guarantee that the bicycle in the advertisement existed. Encore must guarantee that the ticket does.

Encore's primary sale is mostly a pipeline. Encore takes an organizer's event, sells its seats and delivers tickets, and the value flows in one direction, from organizer to fan, with Encore in the middle. A platform has always sat inside it, since organizers and fans need each other, but Encore never had to balance one side against the other. Verified Resale changes the shape of the business. It adds new sides, fans who sell and partners who list, and it makes Encore responsible for matching them: a listing tied to one real ticket at an allowed price, matched to a screened fan who wants it. A platform's **core interaction** is the single exchange it exists to make happen, described by its participants, the unit of value they exchange and the filter that decides which of them meet. The sentence above is the core interaction of Encore's new market. Its design, the participants, the unit of value and the filter as the system enforces them, belongs to the Software book's Section 8.1. What matters for strategy is the recognition that Encore is becoming a different kind of business, one whose value depends on the health of several groups at once.

#### Network effects of both signs {#c2-network-effects}

A **network effect** exists when the value of a product to one participant depends on how many others use it. Parker and his co-authors, and David Evans and Richard Schmalensee in *Matchmakers* (2016), distinguish two kinds. Same-side effects act within one group, as when more fans in a fan club make the club more valuable to each fan. Cross-side effects act between groups, as when more listings make a resale market more valuable to buyers and more buyers make it more valuable to sellers. Both can be positive or negative, and the negative ones are the ones strategies forget.

In Verified Resale the main positive effect is cross-side and plain to see. More listings bring more choice for buyers, and more buyers make it more likely that a listing sells before the show. The main negative effect is cross-side too, and it is the reason Encore hesitated to build the product at all. More listings help buyers only until a growing share of them come from speculators: fans who buy in order to resell above cost, or buyers assisted by bots who acquire tickets the way scalpers do. Once speculators are a visible part of supply, genuine fans stop trusting the market and organizers switch resale off, and the market loses the participants it was built for. The TicketsNow episode of 2009 showed this negative effect on the fan side. When a primary seller and a resale market are mixed without rules, fans conclude that the game is rigged.

What keeps a negative network effect in check is curation. Encore curates through the coherent actions of Section 2.1: the face-value cap, which removes the profit that attracts speculators; per-fan limits on listing and buying; and Bot Screening for every resale buyer. Curation costs some volume, because it turns some participants away, and the strategy accepts that cost openly.

#### Which side is hard {#c2-ignition}

Evans and Schmalensee observe that most matchmakers fail for one reason: they never reach critical mass on both sides at the same time. Buyers will not come until there are listings, and sellers will not list until there are buyers, and a platform that cannot break this circle in time simply fizzles. Parker and his co-authors catalog eight ways to break it, among them seeding one side, attracting a marquee participant, and piggybacking on an existing base of users.

The strategic question is which side is hard. For Encore it is not the buyers, because Encore already holds the primary market and the fans who use it. Every sold-out event page already draws fans who missed the on-sale, which is the piggyback in its purest form, and Rowmate brings buyers of its own who already shop for resale tickets there. Ticketmaster's 2018 exchange worked the same way, by offering resale to the buyers it already had. The hard side is supply, and it is hard in two parts. The first is partner marketplaces willing to accept a face-value cap and reissue, which cuts their usual take and constrains how they run their storefronts. The second is enough fan supply on each event for a buyer to find something, since a resale market with three listings for a 20,000-seat show teaches buyers not to come back. The ignition tactics and the measures of liquidity, how many listings sell and how fast, are the Software book's subject in its Section 8.2. The strategy's contribution is to identify the hard side and to concentrate effort there.

#### Who pays {#c2-who-pays}

In a pipeline the customer pays. In a multi-sided market the question of who pays is open, and Rochet and Tirole's central finding is that the price structure, how charges are divided between the sides, matters as much as the overall level. Platforms routinely subsidize one side to attract the other. Thomas Eisenmann, Parker and Van Alstyne made the point for practitioners in "Strategies for Two-Sided Markets" (2006): the side whose participation is most valuable to the other side, and most sensitive to price, is usually the one that pays least.

Encore's answer follows that logic. The fan who sells pays nothing, because supply is the scarce side, and any fee on sellers would push them back toward doing nothing. The buyer pays a 10% service fee on top of the resale price, shown in the all-in price from the start. The fee is split three ways: 4 points to the partner through which the buyer purchased, 3 points to the organizer and 3 points to Encore, whose share carries the payment fees, fraud losses and support that the service costs. A €60 ticket resold at €60 costs the buyer €66; the partner receives €2.40, the organizer €1.80, Encore €1.80 and the seller the full €60. When the buyer purchases through Encore's own app, no partner is involved and Encore keeps the partner's 4 points as well. Each share pays for something the market needs. The partner's share pays for supply and storefronts, and the organizer's share pays for willingness to switch resale on, which is the permission without which no listing exists. Encore's share pays for the guarantee.

Whether 10% is the right level, and how it compares with other fee models, is a pricing question, and Chapter 5 takes it up in Section 5.2. The strategic decision is the structure: the seller pays nothing, the buyer pays, and both business sides are paid for what they bring.

#### Rules are part of the product {#c2-rules}

Evans and Schmalensee devote a chapter to "fakesters and fraudsters", the participants who exploit a platform at the expense of everyone else, and Parker and his co-authors devote one to governance. Both reach the same conclusion: in a multi-sided market, rules and their enforcement are part of what the platform sells. A buyer on a well-governed market is paying, in part, for the rules that keep fraud out. A buyer on a poorly governed one is paying for the risk.

For Encore this is the strategic heart of Verified Resale. Encore's position on resale, control in place of prohibition, becomes a set of platform rules: face-value caps that organizers may tighten but never loosen, resale windows, per-fan limits, screening for every buyer, and reissue for every ticket. These rules are the product as much as any screen is. The Software book's Section 1.3 states them as the five fairness invariants that Encore tests in every build, and its Section 8.1 turns them into the system's design. Here the point is only the strategic one. A competitor can copy Encore's screens in a quarter. It cannot copy rules enforced at a barcode it does not issue.

**Recap.** Verified Resale turns part of Encore's pipeline into a multi-sided market, whose value depends on the health of several groups at once. Its main network effect is positive until speculators arrive, and curation keeps that negative effect in check at some cost in volume. The hard side is supply, the seller pays nothing because supply is scarce, and the rules that govern the market are part of what it sells.

**Exercise 2.3.** Draw the sides of a platform you use or build, and write its core interaction in one sentence. Name one negative network effect it must curate, what the curation costs, and which side pays for what.

### 2.4 Mapping the Landscape

#### A chain from a user need {#c2-value-chain}

The kernel says what Encore will do. It does not yet say which parts of the work give Encore its advantage and which could be done by anyone. Simon Wardley's maps, published freely from 2016, are a widely used way to see that. A **Wardley map** is a diagram of the components needed to meet a user need, arranged on two axes: vertically by how visible each component is to the user, and horizontally by how far it has evolved, from novel to standardized. The Architecture book's Section 13.2 introduced the horizontal axis, the evolution road from genesis through custom and product to commodity, together with the idea of posture lag, and its Figure 13.1 draws it. We use that road here as it stands. What this chapter adds is the rest of the map: the anchor in a user need, the chain of components beneath it, and the reading of the whole as a landscape on which a company has to move.

A map begins with an anchor, the need the whole chain exists to meet. For Verified Resale the anchor is *a fan holds a guaranteed ticket*. Beneath it sit the components that meet the need: a listing on a partner's storefront or in Encore's app, a purchase with the all-in price, payment and the payouts that follow, screening of the buyer, reissue under a new ticket identity, revocation of the old barcode at the gate, delivery to the buyer's phone, and the organizer's rules that govern every step. Each component depends on the ones below it, and the further down the chain we go, the less of it the fan ever sees.

A touring crew's stage plot works in a similar way, starting from what the audience must hear and see and working down to the cables, power and rigging beneath. It shows what depends on what, which is half of what a map does. The analogy breaks on the second axis. A stage plot has no sense of time, while a Wardley map shows that every component on it is moving, and the movement is what makes the map strategic.

Wardley mapping is a thinking tool. Many practitioners use it, and parts of the UK government took it up early; in 2014 the chief information officer of High Speed Two described on a government technology blog how mapping shaped its technology strategy. There are, however, no empirical studies of its effect on outcomes, and its value lies in the conversation it forces: people who place the same component in different stages discover that they disagree about the business.

#### Reading the map {#c2-reading-map}

Figure 2.4 records where Encore's trio placed each component. The placements are judgments, and the map's purpose is to expose them to argument.

| Component | Visible to the fan? | Stage | What the placement says |
|---|---|---|---|
| A fan holds a guaranteed ticket | the need itself | — | The anchor of the map |
| Listing and storefront | yes | product | Partners already run good ones; leave them open |
| Checkout with the all-in price | yes | product | Reuse the primary checkout |
| Payments, split payouts | no | commodity to product | The primary PSP's marketplace product carries it |
| Wallet passes | yes | product | Apple and Google supply them |
| Buyer screening | no | custom, on rented signals | Reuse Bot Screening as it is |
| Reissue under a new ticket identity | no | custom | Encore's advantage; own it |
| Rotating barcodes and gate revocation lists | at the door | custom, moving toward product | Own it now, and watch it evolve |
| Organizer resale rules | to organizers | genesis to custom | Own it, and expect to learn fast |
| Fee split in the finance ledger | no | custom, on a commodity ledger | Extend what exists |

*Figure 2.4 — The components of Verified Resale placed on the evolution road. Advantage lives in the custom middle of the chain, where Encore controls the barcode.*

Read from top to bottom, the map tells Encore where its differentiation lives. The parts the fan sees most, the storefront and the checkout, are products that partners and Encore already run, and nothing about Verified Resale requires them to be special. The parts nobody sees, reissue and revocation at the gate, are custom, specific to Encore, and the reason any fan can trust a resold ticket. The organizer rules sit near genesis: nobody yet knows the right way to express them, and Encore will learn by building. (The organizer rule assistant, the AI feature of Verified Resale that Section 6.5 designs, sits on top of those rules and is newer still.) What Encore should build, adopt, buy or rent for each component is the Architecture book's question in its Chapter 13, and the answer follows the posture that book attaches to each stage. Here the map's job is to say where the advantage lies, so that effort goes there.

#### The climate {#c2-climate}

Wardley calls the forces that move a map, whatever any one player does, climatic patterns. His published list has about thirty of them, and three bear directly on Encore. The first is that everything evolves through supply and demand competition. Reissue with revocation at the gate is custom today, but Ticketmaster's SafeTix, introduced in 2019 with rotating barcodes bound to the ticket holder, shows that the capability is known and is moving toward product. Encore's advantage in reissue is real and temporary, and the memo says so.

The second pattern is that success breeds inertia. Encore's anti-scalper brand is a genuine success, and it is the reason hosting resale feels like betrayal to many inside the company. It comes from people protecting something that worked, and a map shows it for what it is: a force resisting a move the landscape has made necessary.

The third is that competitors' actions change the game. When a large primary ticketer moved resale inside its own walls, as Ticketmaster did in Europe in 2018, it changed what fans and organizers expect of every primary seller. The open question for Encore became one of timing.

Regulation is not one of Wardley's patterns, but it is a feature of this landscape that Encore must anticipate. Several EU countries already restrict resale above face value, Ireland among them. A face-value cap built in from the start means that a new law of that kind asks little of the product. Section 5.5 sets out the laws and what they demand of the product.

#### Partners who compete {#c2-partners-compete}

Rowmate is Encore's launch partner, and it also runs its own resale marketplace, where it sells tickets for other ticketing companies on its own terms. That makes it a partner and a competitor at once, and the map clarifies how to live with both. Encore must own the components that make the guarantee: reissue, revocation at the gate and the rules. It can leave open the components where partners add value and where competition among them helps fans: listing, storefront and the way each partner presents and sells. Parker and his co-authors treat openness as a deliberate lever, and Encore pulls it carefully: certified partners only, and on their side of the line, freedom to compete for buyers.

Ticketmaster's 2018 exchange illustrates why this division holds. Because the primary seller owns reissue and entry, no partner can undercut the guarantee: a partner that broke the rules would be selling tickets that do not scan. How Encore runs its partner program, what partners may see and how it handles a partner that competes, is the Software book's material in its Sections 8.1 and 8.3. The strategic reading is enough here: own what makes the ticket trustworthy, and open what makes it easy to find.

#### Doctrine and methods {#c2-doctrine}

Wardley also writes of doctrine, principles that apply whatever the landscape, and one of them speaks directly to how Encore should organize the work: use methods appropriate to each stage of evolution. A component near genesis needs exploration, quick experiments and tolerance for being wrong. A component near commodity needs efficiency, standards and caution. Wardley developed this into a model of pioneers, settlers and town planners, drawing on Robert X. Cringely's "commandos, infantry and police" in *Accidental Empires* (1992). The model has Wardley's own account behind it and few published adoptions, so we take it as a lens. Read that way, it explains why the people building the organizer rules and the people changing Seat Inventory's barcode issuance should not be asked to work the same way, even inside the same program. The first are exploring, and the second are changing eight-year-old code that every ticket depends on. How Encore designs the teams themselves is the Software book's subject in its Section 9.2.

**Recap.** A Wardley map anchors the chain of components in a user need and places each on the evolution road, and its value is the disagreement it exposes. For Verified Resale, the advantage lies in the custom middle of the chain, in reissue, revocation and rules, and Encore owns those while leaving listing open to partners who may also compete. The climate moves the map: reissue is evolving toward product, Encore's own success breeds inertia, and competitors' moves have already changed what fans expect.

**Exercise 2.4.** Map one user need of your product to at least six components, and place each on the evolution road. Circle the one component you would never outsource, and write one sentence on how long your advantage in it is likely to last.

### 2.5 From Strategy to Objectives

#### Problems down, results up {#c2-problems-down}

A strategy reaches teams in one of two ways. In the familiar way, leaders turn the strategy into a roadmap of features and hand each team its share. In the way Cagan and Jones describe in *Empowered*, leaders give each team a problem to solve, the team proposes the results it believes it can achieve, and the two negotiate until the team's ambition and the company's needs meet. Leaders keep the right to say that a proposed result is not ambitious enough, and teams keep the right to say how they will reach it. This is a practitioner model, from the Silicon Valley Product Group's work with many companies, with no studies behind it. It fits the case for empowered teams that Chapter 1 made, and it is the model Encore follows.

When the Resale team formed in the fourth month of the bet, three teams received the problem. The Resale team was asked to make face-value resale work end to end for fans, organizers and Rowmate. The Inventory team, which owns the Seat Inventory & Ticketing service and the barcode issuance inside it, was asked to make reissue safe and atomic. The Partner APIs team was asked to let a certified partner list and sell through Encore with no access to anything else. None was given a feature list. Each came back with key results, and two of the three were sent back once to sharpen them.

#### OKRs as Doerr wrote them {#c2-okrs}

The form those results took has a history. Andy Grove ran Intel with a system of objectives and key results, and he described it in *High Output Management* (1983). John Doerr learned it at Intel in the 1970s, and in 1999, after Kleiner Perkins invested $12.5 million in Google, he introduced it to Google's founders. His book *Measure What Matters* (2018) is the standard account. An **objective** is a qualitative statement of what we want to achieve, significant and inspiring enough to be worth committing to. A **key result** is a measurable statement of how we will know the objective has been reached, specific enough that at the end of the period nobody can argue about whether it was met. An objective typically has three to five key results.

Doerr adds rules that matter more than the format. Committed OKRs, which a team is expected to achieve in full, are kept apart from aspirational OKRs, which stretch beyond what the team is sure it can do; Google's guidance has been that reaching 60 to 70% of an aspirational key result is a good outcome. OKRs are public across the company, so that any team can see what any other is trying to achieve. A large share of them are set from the bottom up, by the teams themselves. And they are kept separate from compensation, because a goal tied to pay will be set low and met.

The evidence for goals of this kind comes from goal-setting theory, and it predates OKRs. Edwin Locke and Gary Latham, summarizing 35 years of research in 2002, found that specific and difficult goals lead to higher performance than vague or easy ones, provided people are committed to the goals and receive feedback on their progress. That finding, and not Google's success, is the reason to take OKRs seriously. Doerr's celebrity cases are best read with care, since we hear about the organizations that succeeded and rarely about those that used the same method and failed.

#### OKRs without theater {#c2-okr-theater}

Goal-setting has a dark side as well, and the research describes it too. Lisa Ordóñez and her co-authors, in "Goals Gone Wild" (2009), documented the side effects of goals pushed too hard: narrowed attention that ignores everything outside the goal, unethical behavior to meet a target, and the erosion of cooperation between people with competing goals. Locke and Latham replied in the same journal, and the exchange is worth reading for its honesty: both sides agree that goals are powerful, and they disagree about how often the power goes wrong. The Software book's Section 10.5 tells the best-known recent case, the Wells Fargo sales-target scandal of 2016.

At Encore, four failures appeared in the first round of drafts, and each had a repair. The first was the key result written as an output: "ship the resale rules console". It describes something the team will build, and it would be met even if no organizer ever used the console. The repair was to name the behavior the console should cause: "at least two of the three pilot organizers set their own resale rules without help from Support". The second was the cascade that removes choice, in which a director's key results were copied, word for word, into the objectives of each team below. The teams below had nothing left to decide, and the repair was to give them the problem and ask for their results. The third was scale. Forty teams with seven or eight key results each produce some three hundred numbers that nobody reads, and Encore's rule since is that a team proposes no more than four. The fourth was the quietest and the most damaging: an engineering manager who began to cite key results in performance reviews. Within a quarter the team's proposals had become noticeably safer, which is exactly what Doerr's rule predicts, and the practice was stopped.

The Resale team's objective for its first live quarter shows the form after those repairs.

```text
Objective  Fans who cannot go pass their seats to real fans at face value,
           and everyone at the door trusts the result.        (aspirational)
KR1  Verified resales completed per eligible pilot event: from 0 to 40
KR2  Share of listings that sell before the resale window closes: ≥ 55%
KR3  Resold tickets refused at the door because of a reissue fault: 0  (committed)
KR4  Pilot organizers who set their own rules unaided: 2 of 3
Guardrails (watched only): primary sell-through on pilot events,
           bot-block rate on resale buyers, Support cases per 1,000 resales
```

KR1 counts only the eligible events of the three pilot organizers; it is a narrower measure than the month-18 target the memo sets across every eligible event, which Section 10.5 reports. KR3 is committed, and the rest are aspirational. Its committed status follows from the strategy: a reissued ticket that fails at the door breaks the one promise that the whole bet rests on, so it is not something the team is allowed to fall short on. The guardrails sit outside the key results, because a team that meets its targets by harming primary sales or letting bots in has not met them. Chapter 4 makes them into measures.

#### Three kinds of outcome {#c2-outcome-levels}

Teresa Torres, in *Continuous Discovery Habits* (2021), gives the clearest account of which outcomes a team should own. She distinguishes three. **Business outcomes** measure the health of the business, such as revenue or retention, and they lag: by the time they move, the causes are months old, and many teams contribute to them. **Product outcomes** measure changes in what customers do inside the product, and a single team can move them directly. **Traction metrics** measure the use of one particular feature, and they suit work on a feature already known to matter, or a new trio still learning its product. Torres recommends that trios own product outcomes, because those are close enough to influence and meaningful enough to matter.

The Resale team therefore owns verified resales completed per eligible event, a product outcome. Resale revenue is a business outcome, and it depends on Encore's pricing, on the economy and on which tours happen to sell out. A verified resale counts as completed only when the reissued ticket is scanned at the door. That definition matters, because it ties the team's outcome to the fan's real experience and makes it the main input to the north-star measure, resold tickets that scan at the door, that Section 4.1 builds. The share of listings that sell is close to a traction metric, and the team watches it as a leading signal.

#### Roadmaps and the one commitment {#c2-commitments}

If teams own outcomes, what becomes of the roadmap, the dated list of features that sales and leadership have long relied on? Cagan's answer, and the one set out at length by C. Todd Lombardo, Bruce McCarthy and their co-authors in *Product Roadmaps Relaunched* (2017), is to replace the dated list with problems in priority order, each linked to the outcome it serves. Such roadmaps rest on practitioners' experience, and they tell sales what Encore is working on and in what order without promising features that discovery may yet show to be wrong.

Some dates are real, and pretending otherwise helps nobody. Cagan's name for them is **high-integrity commitments**: the few promises made with a fixed date, typically because another party depends on them, made only after enough discovery to know what is being promised and what it will cost. In this book, Encore's high-integrity commitment for Verified Resale is the organizer contract season. Every autumn, mid-size promoters sign the ticketing terms for the following year's tours and festivals. If Verified Resale terms, the face-value cap, the fee share and a working rules console that organizers can try, are not ready to include in those contracts, the first live events slip by a full year. The commitment was made in the fourth month, after discovery, and it is Encore's only dated promise to organizers. The Software book's Section 10.2 follows a different date, the partner API's availability to Rowmate, which is the commitment as the engineering teams experience it. Both dates are real; each book follows the one that matters to its readers.

#### The Product Kata {#c2-product-kata}

Quarterly objectives and weekly work need something to connect them, or a team will set its objectives in January and rediscover them in March. Melissa Perri adapted a practice from manufacturing for that purpose. Mike Rother's *Toyota Kata* (2009) described the Improvement Kata, the routine by which Toyota's managers taught improvement: understand the direction, grasp the current condition, establish the next target condition, and experiment toward it. Perri's Product Kata, first published on her blog in 2015 and expanded in *Escaping the Build Trap*, applies the same four steps to product work. The team restates the direction it has been given, analyzes where its product stands today, sets the next goal it can reach within weeks, and chooses experiments to move toward it. The Improvement Kata has a long record in manufacturing. The Product Kata is a practitioner adaptation without published evaluations, and Encore uses it as a habit, without making it a ceremony. Each pass through the loop asks whether the last experiment moved the outcome, and each answer feeds the weekly discovery work that Chapter 3 describes.

**Recap.** Leaders give teams problems, and teams propose the results they can achieve. OKRs work when they follow Doerr's rules, which goal-setting research supports and whose failures the same research describes. Teams own product outcomes, roadmaps list problems in order, and the few real dates become high-integrity commitments made after discovery, which for Encore means the organizer contract season.

**Exercise 2.5.** Take one of your team's key results and decide whether it is an output, a traction metric, a product outcome or a business outcome. Rewrite it one level up or down, and say who in your organization would object to the rewrite and why.

### Kata: The Empty Court

> **Your brief: "Courtside."** Courtside runs a booking marketplace for sports courts in eight cities: tennis, padel and five-a-side pitches. It has 60 engineers in eight teams, and its market has three sides. About 900 clubs list their courts and set their prices. About 400,000 players book courts by the hour, and some 3,000 coaches book courts in blocks for their lessons. Coaches now want to resell the slots they have booked and cannot use, which happens often when lessons are cancelled. Clubs are split: some welcome the extra bookings, and others fear that coaches will block-book prime evening hours cheaply and resell them at a premium, which a few already do through group chats. Players complain that the best slots are never available. Courtside's leadership has a one-line strategy, "become every player's home for sport", and wants a resale feature in the next quarter.

**Deliverables:**

1. **Strategy kernel** — One page in the form of Section 2.1's kernel: a diagnosis that names the real problem with coach resale today, a guiding policy, five or fewer coherent actions, an explicit list of what Courtside will not do, and a proximate objective.
2. **The jobs** — A job statement for clubs, players and coaches, each with its functional, social and emotional dimensions, its real competitor, and the questions a round of switch interviews would need to answer.
3. **The market's shape** — The core interaction of coach resale in one sentence, its main negative network effect and how you would curate it, which side is hard, and who pays what.
4. **A map** — A Wardley map anchored on one player need, with at least six components placed on the evolution road, and the one component Courtside must own.
5. **A team objective** — An objective with three or four key results for the first quarter, marked committed or aspirational, with the guardrails you would watch alongside.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Diagnosis | Does the kernel name an obstacle that someone could disagree with, and does everything else follow from it? |
| Refusal | Does the "will not do" list cost Courtside something real? |
| Jobs | Would a coach recognize the job you wrote, and is "doing nothing" considered as a competitor? |
| Market health | Does your curation stop block-booking for profit without driving the coaches away? |
| Map | Is your advantage placed in a component that a rival could not copy within a year? |
| Outcomes | Is each key result a change in what people do, owned by a team that can move it? |

#### Where you now stand

You can now tell a strategy from a statement of ambition, by asking for its diagnosis, its guiding policy and the coherent actions that follow, and you can write one with a proximate objective and a list of refusals. You can describe the people a product serves by the progress they seek, and you can reason about a market with several sides: its network effects, the side that is hard to attract, and who should pay. You can map where an advantage lies and how the landscape is moving, and you can turn the whole into objectives that teams propose and own. What you cannot yet do is know whether any of it is true. Every job in Figure 2.3 is a hypothesis, and so is every assumption behind Encore's guiding policy: that fans will trust a reissued ticket, that organizers will switch resale on, that partners will accept the cap. Chapter 3 takes those assumptions to the people who can confirm or refute them, beginning with the cheapest test that could prove the strategy wrong.

### References

- Richard P. Rumelt — [*Good Strategy Bad Strategy: The Difference and Why It Matters*](https://www.penguinrandomhouse.com/books/208668/good-strategy-bad-strategy-by-richard-rumelt/). Crown Business, 2011.
- Richard P. Rumelt — [*The perils of bad strategy*](https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/Strategy%20and%20Corporate%20Finance/Our%20Insights/The%20perils%20of%20bad%20strategy/The%20perils%20of%20bad%20strategy.pdf). McKinsey Quarterly, 2011 — free online.
- Walter Isaacson — *Steve Jobs*. Simon & Schuster, 2011.
- Michael E. Porter — [*What Is Strategy?*](https://hbr.org/1996/11/what-is-strategy). Harvard Business Review, November–December 1996.
- Clayton M. Christensen, Taddy Hall, Karen Dillon, David S. Duncan — *Competing Against Luck: The Story of Innovation and Customer Choice*. HarperBusiness, 2016.
- Carmen Nobel — [*Clay Christensen's Milkshake Marketing*](https://www.library.hbs.edu/working-knowledge/clay-christensens-milkshake-marketing). HBS Working Knowledge, 2011 — free online.
- Geoffrey G. Parker, Marshall W. Van Alstyne, Sangeet Paul Choudary — [*Platform Revolution*](https://wwnorton.com/books/9780393249132). W. W. Norton, 2016.
- David S. Evans, Richard Schmalensee — *Matchmakers: The New Economics of Multisided Platforms*. Harvard Business Review Press, 2016.
- Jean-Charles Rochet, Jean Tirole — [*Platform Competition in Two-Sided Markets*](https://doi.org/10.1162/154247603322493212). Journal of the European Economic Association 1(4), 2003.
- Simon Wardley — [*Wardley Maps*](https://learnwardleymapping.com/book/). Self-published, 2016 onward — free online.
- John Doerr — [*Measure What Matters*](https://www.penguinrandomhouse.com/books/546304). Portfolio/Penguin, 2018.
- Edwin A. Locke, Gary P. Latham — [*Building a Practically Useful Theory of Goal Setting and Task Motivation: A 35-Year Odyssey*](https://doi.org/10.1037/0003-066X.57.9.705). American Psychologist 57(9), 2002.
- Marty Cagan, Chris Jones — [*Empowered: Ordinary People, Extraordinary Products*](https://www.wiley.com/en-us/-p-9781119691297). Wiley, 2020.
- Teresa Torres — [*Continuous Discovery Habits*](https://www.producttalk.org/continuous-discovery-habits/). Product Talk, 2021.
- Melissa Perri — *Escaping the Build Trap*. O'Reilly, 2018.
- A. G. Lafley, Roger L. Martin — *Playing to Win: How Strategy Really Works*. Harvard Business Review Press, 2013.

---

## Chapter 3: Product Discovery — Learning Before Building {#ch3}

> Every product begins as a guess about other people's lives.

Chapter 2 chose where Encore would play. Its strategy for Verified Resale has a diagnosis, a guiding policy and a set of coherent actions, and it reads well. Yet every sentence in it rests on beliefs about how other people will behave, and nobody has yet checked those beliefs. Will an organizer who has spent years fighting touts sit down and set resale rules for a show? Will a fan believe that a ticket reissued an hour ago, under a new barcode, will open the gate? A strategy cannot answer such questions, because they are about behavior, and behavior is found out by watching. This chapter is about how a team does that watching, and how it turns what it sees into a decision before 12 teams have spent a year building. **Product discovery** is the work of finding out, quickly and cheaply, whether a proposed product is worth building and what form it should take, before the cost of building it is paid. The Architecture book separated the essential complexity of a problem from the accidental complexity we add to it, and Chapter 1 argued that most of a product's essential complexity lives in the decision about what to build. Discovery is where we meet that complexity directly.

Our touchstone is one of the longest-running habits in the history of software products. From Quicken's early days, employees of Intuit waited in computer shops for someone to buy their product, then asked to follow the buyer home and watch. The program has outlived every method that was fashionable around it, and it teaches what this chapter develops: the people who build a product should see its customers regularly, in the customers' own setting, because what people do is better evidence than what they say they will do.

Encore stands at month zero of the bet. The bet memo that Chapter 10 examines has funded a first tranche of work, and that tranche is for discovery. The resale trio introduced in Chapter 1, Amira as product manager, Paolo as designer and Katrin as tech lead, has four months to learn whether the bet deserves the next tranche. It has a history to learn from: Partner Listings, which since Encore's sixth year has linked sold-out event pages to Rowmate and checked nothing beyond the partner's word; the Rowmate key leak, which showed what that trust was worth; and the grey market around the Vesper Hale tour. Over the four months the trio interviews fans, organizers and Rowmate every week, recruits six promoters as design partners, runs a hand-operated resale for four real shows, and shapes the first release as a written pitch. Along the way it finds that organizers care far more about controlling resale than about the size of their share, and that finding changes what Encore builds first.

### 3.1 Continuous Discovery

#### Following customers home {#c3-follow-me-home}

Intuit began in 1983, when Scott Cook, a former Procter & Gamble marketing manager, met Tom Proulx, a Stanford student, after posting flyers near the university library in search of a programmer. The idea came from Cook's kitchen table, where he had watched his wife pay the household bills and dislike every minute of it. Quicken shipped in 1984. The software market of that year had no appetite for an unknown company's first product, so Intuit sold Quicken through banks at first, starting with Bank of Hawaii. By September 1988 it was the best-selling consumer software product. Cook later described his method plainly: he had taken the Procter & Gamble playbook, with its long tradition of studying how consumers really use soap and detergent, and applied it to a new category.

The practice that came to be called "Follow Me Home" was that playbook made concrete. An Intuit employee would wait beside the Quicken shelf until someone bought a copy, then ask to come home with the buyer and watch the first installation. The rule of the visit, as Fortune reported it in 2017, was "You don't interview the customer; you just observe." The struggle was the data, and observers debriefed at once. Intuit's own history says that Cook started the program in Quicken's early days and that the company reinstated it in 1989. By 2017 Intuit reported some 10,000 hours of these visits a year. The figure is hours of observation, and secondary sources that turn it into 10,000 visits misquote it.

The best-known product to come out of this attention needs telling carefully. Intuit's regular customer surveys asked whether people used Quicken at home or in the office, and about half said in the office. Cook first assumed they were doing personal finances at work. "It just bugged me," he told Fortune. "Why were people answering that question wrong?" When Intuit went and looked, it found small-business owners running their companies on Quicken, because accounting software built for accountants was too hard for them. Intuit built QuickBooks, released in 1992, as, in Cook's words, "an accounting product that didn't seem to have any accounting." It passed the market leader, DacEasy, within two months, at twice the price and with fewer features. A number raised the question, and watching people answered it. Neither would have been enough alone, and the rest of this chapter, together with Chapter 4, is built on that partnership.

#### The definition and the habit {#c3-weekly-habit}

The modern name for Intuit's habit comes from Teresa Torres, whose *Continuous Discovery Habits* (2021) defines **continuous discovery** as "at a minimum, weekly touchpoints with customers, by the team building the product, where they conduct small research activities in pursuit of a desired outcome." "Weekly" sets a rhythm short enough that what the team hears can still change what it does next. "By the team building the product" excludes the arrangement, common in large companies, where a research department studies customers and hands the builders a report. And "in pursuit of a desired outcome" keeps discovery from becoming a pleasant habit of chatting to customers. Torres herself calls the weekly cadence a benchmark to aspire to. What she insists on is continuity: contact with customers that never stops for long, so that no decision waits months for its evidence.

The habit is older than the name. Intuit's visits are one ancestor. Another is Desirée Sy's 2007 account of usability work at Alias, later part of Autodesk, which is the earliest peer-reviewed description of designers working a cycle ahead of developers, investigating the next iteration's questions while the current one was being built. Chapter 1 introduced that arrangement as discovery and delivery running as two tracks. What continuous discovery adds is a cadence for the first track. Occasional large studies do not replace the cadence, and the cadence does not replace them either. A survey of 5,000 fans or an experiment on a checkout page can measure what weekly conversations can only suggest, and Chapter 4 does the measuring. The two kinds of evidence answer different questions, much as Intuit's survey and Intuit's visits did.

Civil engineering learned the same lesson about structures. A bridge is not inspected once, when it opens, and then trusted for half a century; since the collapse of the Silver Bridge over the Ohio River in 1967, American highway bridges have been inspected on a fixed cycle, because traffic, weather and corrosion change a structure in ways no design calculation foresees. Customers change in the same way, as competitors, prices and habits move around them, and a team that interviewed its customers once, at the start of a project, is trusting an inspection that has expired. The analogy breaks at an instructive point. An inspector's gauges report what the structure is doing now. A customer asked about their own future behavior answers sincerely, and often wrongly, and so interviewing customers needs a technique of its own.

#### Interviewing well {#c3-interviewing}

The central rule of discovery interviewing is to ask about the past. "Would you use a feature that let you resell your ticket safely?" invites a fan to imagine a better version of themselves, one who plans ahead, reads terms and acts on good intentions, and the fan will answer for that imagined person. "Tell me about the last time you couldn't go to a show you had a ticket for" invites a story, and a story is full of facts the teller did not choose to emphasize: when they realized, who they asked, what they tried first, what they gave up on, how the money moved. Torres builds her interviews around that prompt, and the method has deep roots. In 1954 the psychologist John Flanagan published "The Critical Incident Technique", which collected specific, recent episodes of behavior instead of general opinions, a method that grew out of aviation psychology and has been used widely in research ever since. Hugh Beyer and Karen Holtzblatt's *Contextual Design* (1998) took the same principle into the customer's workplace, where the researcher watches real work as an apprentice watches a master and asks questions only about what is happening in front of them. Follow Me Home is contextual inquiry with the questions removed.

Chapter 2 taught Clayton Christensen's switch interviews, which reconstruct the timeline of a real purchase and the forces of push, pull, anxiety and habit acting on it. Those forces need no reteaching here. What this section adds is the discipline that turns such interviews into a weekly practice. Interviews are short, about 30 minutes, and each is captured the same day on a single page. Torres calls the page an **interview snapshot**: a one-page summary of one interview, holding a memorable quote, the story as told, the opportunities it revealed and any follow-up. The snapshot matters more than it looks, because it fixes what the interviewer heard before the next interview overwrites it, and it gives the rest of the team something to read in two minutes. Here is one of the resale trio's, from the sixth week:

```text
Interview snapshot — fan who resold, F-17, week 6 (anonymized)
Quote          "I sent the screenshot and then just prayed."
Story          Couldn't attend an arena show bought from another ticketer last year.
               Sold to a stranger from a fan group at face value; paid by bank
               transfer. The buyer got in, but she checked her phone all evening.
Opportunities  Fear of being blamed if the ticket fails at the door.
               No safe way to be paid by a stranger.
Insight        Trust in the buyer mattered more to her than the price.
Follow-up      Did the event's own resale rules ever come up? (No; she didn't know any.)
```

Two cautions come with interviewing fans about resale. The first is that some stories describe resale that was unlawful where it happened, since several EU states restrict resale above face value. The snapshot therefore anonymizes the person and leaves out the place, because the team needs the behavior and has no use for evidence of an offence. The second is that a team that slips back into hypothetical questions will collect a great deal of enthusiasm and very little information; Rob Fitzpatrick's short book *The Mom Test* (2013) is a practical corrective.

#### Recruiting on autopilot {#c3-recruiting}

Weekly interviews stay weekly only if finding people to talk to costs the team nothing each week. Torres's advice is to automate recruitment: ask customers while they use the product, ask through colleagues who already talk to customers, and keep a standing pool of volunteers. Encore uses two channels. A short invitation on the post-purchase screen asks fans whether they would talk to the team for half an hour, and for organizers, the organizer success team, the account managers who speak to promoters every week, asks at the end of routine calls. Without such channels, interviews happen only when the team has spare time, which is rarely.

Automated recruitment has blind spots. A prompt after purchase reaches only buyers, yet the fans Chapter 2 called non-consumers, those who could not go and simply absorbed the loss, are exactly the people a resale product most needs to understand. The trio finds them among fans who asked for refunds the policy could not grant and fans who contacted Support about a ticket they could not use. Panels also tire, so the trio rotates participants and limits how often anyone is asked, and consent comes before any recording, as Section 3.5 explains. The shared panel and findings repository that serve all 40 teams belong to Chapter 6; this section concerns only the habit of one team.

Before the first interview, the trio also looks at what Encore already knows, since Torres recommends sizing opportunities with existing data. The support assistant's logs show how many conversations concern tickets a fan cannot use, and the fan app's search logs record how often people type "resell" into a box that has nothing to offer them. None of this explains anything, but it says where to look, and it costs an afternoon.

#### The opportunity solution tree {#c3-opportunity-tree}

Interviews produce stories, and stories pile up. Torres's answer is the **opportunity solution tree**: a diagram that starts from one desired outcome, branches into the opportunities that could move it, branches again into candidate solutions for each opportunity, and ends in the assumption tests that would show whether each solution works. An opportunity, in Torres's sense, is a customer need, pain point or desire, stated from the customer's side, such as "I'm afraid I'll be blamed if the ticket doesn't work." A solution is something the team might build. Keeping the two levels apart is most of the discipline, since teams naturally jump from a story to a feature and lose sight of the need in between.

Torres first described the tree in 2016, and it deserves a precise claim. No controlled study shows that teams using it build better products. Its value is that it makes a team's reasoning visible: a leader can see which outcome the team is pursuing, which needs it has heard, which it chose and what it is testing this week. In an organization of 40 teams, most of what leaders otherwise learn about a team's thinking arrives as a roadmap of features with the reasons removed. The root of the resale trio's tree is the product outcome Chapter 2 set: verified resales completed per eligible event. Figure 3.1 shows the upper branches as they stood at the end of the second month.

| Opportunity (whose) | Evidence so far | Candidate solutions | First assumption test |
|---|---|---|---|
| "I want to decide when and whether my shows are resold" (organizer) | raised unprompted in 19 of 22 organizer interviews, all six promoters | rules console with window, per-fan limits, off switch; rules set by account managers on request | clickable rules screen with six promoters |
| "Touts end up in my front rows" (organizer) | 14 of 22 organizer interviews | resale buyers pass Bot Screening; per-buyer limits | count rule breaches in the hand-run pilot |
| "I get nothing when my tickets are resold" (organizer) | 8 of 22 organizer interviews | a share of the resale fee | willingness-to-pay talks (Chapter 5) |
| "I'm afraid of being blamed if the ticket fails" (seller) | 17 of 31 fan interviews | reissue under a new barcode; "your ticket sold" confirmation | hand-run reissue at four shows |
| "I'm afraid the ticket won't open the gate" (buyer) | 21 of 31 fan interviews | Verified badge; guarantee wording | entry refusals in the pilot |
| "Duplicated tickets cost me chargebacks" (partner) | all six Rowmate conversations | reissue, so a ticket exists once | Rowmate's chargeback data from Partner Listings |

*Figure 3.1 — The upper branches of the resale trio's opportunity solution tree at the end of month two. The root outcome is verified resales completed per eligible event.*

#### Comparing opportunities {#c3-comparing}

The tree's second discipline is to compare. Torres asks teams to set opportunities side by side and choose among them, judging each by how many customers it touches, how much it matters to them, and how well it fits the company's strategy. Then it generates several solutions for the chosen opportunity and compares those too. The argument comes from decision research. Chip and Dan Heath's *Decisive* (2013) reports Paul Nutt's studies of organizational decisions, which found that decisions framed as "whether or not" to do a single thing failed considerably more often than decisions that weighed two or more alternatives. Most roadmaps are lists of "whether or not" decisions, and the tree is a device for turning them into choices.

When the trio compared its organizer opportunities, the evidence column did the arguing. Control over resale, meaning when it opens, how many tickets one fan may list or buy, and whether it happens at all, came up unprompted in almost every organizer interview, while the organizer's share came up in about a third, usually late and as a matter of principle more than money. One promoter put the hierarchy in a sentence the trio wrote on its wall: the fee would be pleasant, but the rules were the reason to say yes. The tree recorded control as a single opportunity, without separating its kinds: control of price, of timing and of quantity were all written down as "control", a simplification whose cost Chapter 10 counts at month 18. Even so, the finding changed the plan. The rules console moved into the first release, ahead of any work on fee reporting, and the organizer's share became something Encore would fix and explain, which Chapter 5 does, instead of something each organizer would negotiate.

**Recap.** Continuous discovery is a weekly habit of contact with customers, kept by the team that builds the product and aimed at an outcome. Interviews ask about specific past episodes and are captured the same day as one-page snapshots, and automated recruitment lets the habit survive a busy week. The opportunity solution tree keeps needs and solutions apart and makes the team's reasoning visible, and comparing opportunities, then solutions, produces better choices than deciding on one idea at a time.

**Exercise 3.1.** Hold one story-based interview this week with a customer of your product, beginning "Tell me about the last time…", and write its snapshot within the hour. Then add one opportunity from it to a tree whose root is your team's current outcome, stated in the customer's words.

### 3.2 Assumptions and Cheap Tests

#### Assumptions inside an idea {#c3-assumptions}

An idea that has survived the tree is still a bundle of beliefs, and some of those beliefs are more dangerous than others. Torres asks teams to unpack each idea into its assumptions and sort them into five types: **desirability** (do people want it?), **viability** (should the business do it?), **feasibility** (can we build it?), **usability** (can people use it?) and **ethics** (should we do it at all?). The five types line up with the four product risks and the ethical question of Chapter 1, Section 1.3: the risks are the dangers, and the assumptions are the particular beliefs that, if false, would make each danger real. The practical move is to rank the assumptions by how much the idea depends on each and how little evidence the team has for it, and to test the riskiest first.

That ranking is the core of cheap testing. A team that tests the whole idea by building it learns only whether the bundle worked, and if it fails, cannot tell which belief was false. Whole ideas do get tested eventually, through live-data prototypes and the controlled experiments of Chapter 4, but last, when the remaining doubts are cheap ones. Figure 3.2 shows the resale trio's map for the idea at the heart of Verified Resale.

| Type | Assumption | Evidence at month one | How it was tested |
|---|---|---|---|
| Desirability | Fans who cannot go will list through Encore instead of a fan group | search and support logs; interviews | hand-run pilot at four shows |
| Desirability | Buyers will trust a ticket reissued an hour ago | interviews only | entry results and buyer follow-up calls in the pilot |
| Viability | Organizers will set rules and keep resale switched on | interviews only | rules-screen prototype; pilot promoters' choices |
| Feasibility | The old barcode can be revoked at the gate before doors | Katrin's wallet prototype: phones cannot be trusted, gates can | feasibility prototype (Chapter 1); revocation lists in the pilot |
| Usability | Organizers can express their rules on one screen | none | clickable prototype with six promoters |
| Ethics | Resale through Encore will not reward touts | Bot Screening's record on primary sales | rule breaches counted in the pilot |

*Figure 3.2 — The assumption map for Verified Resale's central idea. Two assumptions ranked riskiest, that buyers will trust a reissued ticket and that organizers will set rules and keep resale switched on, because the idea depends on them entirely and the only evidence for either was interviews; the pilot and the rules-screen prototype tested them first.*

#### The MVP as an experiment {#c3-mvp}

Eric Ries gave the most widely used name to the cheapest kind of test. In *The Lean Startup* (2011) the **minimum viable product (MVP)** is the version of a new product that lets a team collect the most validated learning about customers with the least effort: an experiment that happens to look like a product. Many teams now use the phrase for a small first release, which loses the point, since the cheapest way to learn whether an assumption is true is often something that could never be shipped at all.

Ries describes two such variants. In a **concierge MVP**, the team delivers the service by hand to a few customers who know they are being served by people, as Food on the Table, an Austin meal-planning company founded in 2009, did when it began by serving its first customers in person, with the founders preparing their meal plans and shopping lists by hand. In a **Wizard-of-Oz MVP**, customers use what looks like a working product while people behind the scenes do the work the software will later do. Ries's example is Aardvark, a question-answering service bought by Google in 2010, which for months had people performing parts of its back end that software was later built to do. The technique is much older than the book. In 1983 John Gould, John Conti and Todd Hovanyecz tested a "listening typewriter", a speech-recognition system that did not yet exist, by having a hidden typist transcribe what users dictated, and in 1984 J. F. Kelley named the approach the "OZ paradigm" in a paper on natural-language interfaces. The name honors the man behind the curtain, and only the startup vocabulary is recent.

Theater makes the analogy obvious. The audience sees a storm on the heath, and the crew in the wings produces it with ropes, lights and timing; the illusion must hold from the audience's seat, so everything the audience can see must be real and everything behind it may be improvised. The analogy breaks at consent. A theater audience has bought tickets to an illusion and knows it, while a customer in a Wizard-of-Oz test usually does not know that a person is doing the software's job. That is acceptable only when the customer receives exactly what was promised, so that the hidden labor changes how the service is produced and nothing about what the customer gets. Paul Graham's essay "Do Things That Don't Scale" (2013) describes Stripe doing this in its early days, setting up merchant accounts by hand behind an interface that looked automatic. Ries's measure of a team is how quickly it turns his build-measure-learn loop, and a Wizard of Oz turns it fast because it skips most of the building.

#### Prototypes of every fidelity {#c3-prototypes}

Not every assumption needs a working service, even a hand-operated one. Marty Cagan's *INSPIRED* (2017) distinguishes four kinds of prototype, each suited to a different risk. A **feasibility prototype** is throwaway code that answers an engineering question. A **user prototype** is a simulation, from paper sketches to a clickable mock-up, that shows people what the product would be like without doing anything real. A **live-data prototype** is a limited implementation that handles real data and real traffic, enough to see how people actually behave. A **hybrid prototype** combines elements, and a Wizard-of-Oz test is a hybrid: a real front end with simulated machinery behind it.

Chapter 1 told how Katrin's feasibility prototype answered whether the seller's old ticket could be made to stop working. No phone could be trusted to remove it, but a gate could refuse it, if every venue's scanners held a list of revoked barcodes even when offline. Because that answer pointed to a known mechanism, owned by Venue Entry, feasibility does not top the risk list in Figure 3.2. The more instructive prototype in this period was the designer's. The trio built a clickable rules screen for organizers, with a resale window, per-fan limits and an off switch, and took it to all six design-partner promoters within two weeks. The screen did nothing, which was the point: it cost three days, and it answered whether organizers could express their rules without help. Mostly they could. Two of the six read "resale window" as the dates during which a buyer may attend, and every promoter wanted a plain-language sentence summarizing what they had set, which foreshadows the rule assistant of Chapter 6. Usability testing as a monthly practice is also Chapter 6's subject.

#### Encore's Wizard of Oz {#c3-wizard-of-oz}

The riskiest assumption on the fans' side of Figure 3.2, that buyers would trust a reissued ticket, needed real fans, real money and real gates, and so did its companion, that fans would list at all. They did not need a Resale service, which would have taken most of a year to build. So the trio ran a Wizard of Oz.

Two design-partner promoters offered four shows: two dates of a mid-size tour at a 3,000-capacity hall in Lyon, and two at a hall of similar size in Antwerp, about 11,200 tickets in all. Everything a fan touched was real. Ticket holders for those shows saw "Resell this ticket" in My Tickets, and buyers saw verified resale listings on the sold-out event pages, inside Encore's own app and website. No partner was involved, since a partner integration would have added months of work to a six-week test. Buyers passed Bot Screening and the per-buyer limits as they would in a primary sale, and paid the face value plus a 10% fee, shown in the all-in price from the first screen. Their payment was authorized at purchase and captured only after the reissue had been completed, so if Support could not finish a resale within 12 hours, the authorization lapsed and the listing returned.

Behind the screens, a rota of four Support agents was the machinery. For each sale, an agent checked that the seller had bought the ticket through the Sale Gate and within the per-fan limit, checked the promoter's rules (resale closing 24 hours before doors, two tickets per fan), used Support's long-standing lost-ticket replacement screen to cancel the seller's ticket and issue a new one to the buyer, and confirmed that the old ticket appeared on the show's revocation list. Sellers were paid by hand after the show. The agents did by hand what the barcode core could not yet do by machine: written in Encore's first year, for a world in which a ticket had one holder for life, it had no notion of transfer, and Lena, its last remaining author, is the only person who fully understands it. The Software book tells how that code was made safe to change (Sections 2.4 and 11.2); for a discovery test, a careful person with an old admin screen was enough. The trio wrote its decision rule in the first week and had the bet's sponsor sign it:

```text
Pilot pre-registration — Verified Resale, Wizard of Oz (signed before day one)
Shows        Four: two dates in Lyon, two in Antwerp; about 11,200 tickets.
Measures     Resales completed; median Support minutes per completed resale;
             completed resales that broke an organizer rule; entry refusals.
Stop at once Any fan holding a reissued ticket is refused entry.
             Any payment is captured for a resale that was not completed.
Stop after a show   Median Support time above 30 min at any show after the first.
Redesign     More than 5% of completed resales broke an organizer rule.
Demand       Read qualitatively: four shows cannot measure it.
Decision     The trio and the sponsor, within one week of the last show.
```

The demand line deserves a word. Four shows produce a few hundred resale attempts, enough to measure Support time, rule breaches and gate results, which are properties of individual resales. They cannot estimate how many fans across Encore's catalog would list, because demand varies with artist, venue, price and season, and four shows sample almost none of that variation. Saying so in advance protected everyone from reading more into a good result than it could bear. Figure 3.3 shows what the four shows produced.

| Measure | Result | Stopping rule | Verdict |
|---|---|---|---|
| Listings created | 268 (about 2.4% of tickets) | — | qualitative signal only |
| Resales completed | 191; 61 expired unsold, 16 withdrawn | — | — |
| Median Support minutes per completed resale | 26 at the first show, 9 at the fourth; 14 overall | above 30 at any show after the first | passed |
| Completed resales that broke an organizer rule | 6 of 191 (3.1%), all over the per-fan limit | above 5% | passed, with a finding |
| Listings blocked by agents for rule breaches | 37 | — | — |
| Fans with reissued tickets refused entry | 0 | any | passed |
| Seller's old passes presented at the gate | 3, all refused | — | revocation worked |
| Payments captured for incomplete resales | 0 | any | passed |

*Figure 3.3 — Results of the hand-run pilot against the rule written before it began. These numbers feed the business case of Chapter 5.*

Two results mattered more than the rest. Agents caught 37 attempts to list outside the promoter's rules and missed six, all cases of one fan listing tickets bought across two orders, which their checklist did not cover. Six in 191 is under the threshold, but the finding was plain: people checking rules by hand miss things, and a product that promises organizers their rules will hold must enforce them in software, at the point of listing, every time. That became one of the five fairness invariants that the Software book puts under test. The second was the three old passes refused at the gate: Apple Wallet passes, which do not rotate, forwarded by sellers to friends before the sale. The revocation lists held, and the fans involved were confused, a design problem that Chapter 6 takes up.

#### Demand and value tests {#c3-demand-tests}

Because the pilot could not measure demand, the trio added a test that could suggest it across many events. Cagan describes a family of **demand tests**, of which the best known is the **fake door**: a button for a feature that does not yet exist, which explains that the feature is coming and counts the visit. Its partner is the qualitative **value test**, in which a person is shown a prototype and the team learns, by watching and asking, whether they find it valuable. The first asks how many people reach for something, the second why.

Fake doors raise an ethical question, which Cagan treats as one, and on a ticketing site it is sharper still, because a fan who reaches for a ticket is reaching for money and a seat. EU consumer law has a view. Annex I of the Unfair Commercial Practices Directive (2005/29/EC) lists practices that are unfair in all circumstances, and point 5 is "bait advertising": inviting people to buy a product at a stated price without disclosing that the trader has reason to think it cannot supply it at that price. A fake door that showed a resale ticket for a particular seat at a particular price would sit uncomfortably close to that line. Encore's rule is therefore strict. A fake door never shows a specific seat or price, never takes a payment and never holds a seat, and the screen behind it says plainly that the feature does not exist yet. The trio's fake door was a "Resell this ticket" entry in My Tickets for events outside the pilot, leading to a page that said resale was being tested and offered to notify the fan when it arrived. Over three weeks, about 3,300 fans across 280 events tapped it, which shows that sellers look for such a feature where they expect it, and says nothing about whether they would complete a resale. Chapter 4 sets out the ethics of experimenting on customers, including Encore's absolute rule against individual price experiments on fans, which is why no fake door ever mentions a price.

#### Pivot or persevere {#c3-pivot-or-persevere}

Ries closes his loop with a decision. After each round of testing, a team should choose deliberately whether to **persevere** with its strategy or **pivot**, changing one fundamental part of it while keeping what it has learned. He wraps the decision in what he calls **innovation accounting**: establish a baseline with the MVP, try to move it, and judge progress against that baseline instead of against vanity metrics such as sign-ups or page views, which rise whether or not the product is working. The evidence Ries offers is a set of case histories, IMVU's among them, which is good practitioner evidence and no more.

The strongest part of the idea has much older support. Writing down the decision criteria before running a test is the logic of pre-registration in experimental science, where researchers state their hypothesis and analysis in advance so that the results cannot quietly reshape the question. The reason it matters is human. A team that has spent six weeks on a pilot wants it to have worked, and after the fact almost any result can be read as encouraging. A rule signed beforehand does not care what the team wants, and it also prevents the opposite failure, a promising idea dropped because one number disappointed someone who had never agreed what disappointing meant.

Encore's decision, taken within the week as the pre-registration required, was to persevere, with one change of course. Fans listed, reissued tickets opened gates and the Support cost fell quickly, while enforcing organizers' rules by hand proved inadequate, so rule enforcement moved onto the list of things the first release must do in software. The form of the pilot's stopping rule, a state and a date written in advance, carries forward into the kill criteria of the bet memo, which Chapter 10 examines.

**Recap.** An idea is a bundle of assumptions of five types, and testing the riskiest first lets a team learn in days what building would teach in months. An MVP is an experiment, and its concierge and Wizard-of-Oz forms, the second of which is almost 30 years older than Ries's book, let real customers meet a service whose machinery is still people. Each kind of prototype answers a different risk, fake doors must never show a seat or a price, or take money, and the decision to persevere or pivot is only as honest as the criteria written down before the test.

**Exercise 3.2.** Take one item from your roadmap and list every assumption inside it, labelled with Torres's five types. Mark the one whose failure would hurt most and for which you have the least evidence, and design a test for it that takes less than a week. Write the decision rule before you run it.

### 3.3 Discovery in B2B and with Partners

#### Customers who sign contracts {#c3-buying-center}

A fan who buys is the fan who uses. Organizers are businesses, so discovery with them is business-to-business (B2B) discovery, and a business buys differently. A promoter has a commercial director who signs contracts and a box-office manager who spends every day in Encore's organizer console, and a product that pleases one can fail with the other. Marketing scholars mapped this half a century ago. In 1972 Frederick Webster and Yoram Wind described the **buying center**, the set of people involved in an organization's purchase: users, influencers, buyers, deciders and gatekeepers. Product teams keep rediscovering the idea, usually after a feature that users loved failed to renew a contract.

Medicine offers a close analogy. A prescription drug has a patient who takes it, a physician who chooses it and a payer that decides whether it will be paid for, and a drug can work beautifully for patients and still fail because payers will not fund it. The analogy breaks in a way that matters for Encore: in medicine the three parties rarely sit in the same building, whereas in a promoter's office the box-office manager and the commercial director may share a coffee machine and still not share a view of what resale is for. One thinks about revenue and the artist relationship, the other about the angry emails the morning after a sale.

So the trio's interviews with promoters were arranged in pairs, one with the person who would use the rules console and one with the person who would sign the contract amendment that enables resale. The two conversations often disagreed, and the disagreements were among the most useful things the trio learned. The Architecture book's Section 14.5 showed the same pattern with an enterprise tenant's checklist of single sign-on, customer-managed keys and contractual service levels: none of it came from the staff who use the product daily, and all of it arrived through the people who sign.

#### Design partners {#c3-design-partners}

Cagan's answer to discovery in a business market is the **customer discovery program**: a team builds a product together with a small set of hand-picked customers, until those customers are running it in production and willing to say so publicly. The target in *INSPIRED* is six such customers, all from the same target market, and Cagan is specific about why. Two or three customers from each of two or three markets, he warns, will not give the team focus, because each market's needs pull the product a different way and no market ends up properly served. A **reference customer**, in his sense, is a real, paying customer, using the product in production, who is willing to tell others that it works for them.

The trio's first plan had three organizers and two resale partners, precisely the mixture Cagan warns against. The plan Encore adopted has six design partners, all mid-size festival and tour promoters: three in France, two in Belgium and one in the Netherlands, each running between 40 and 200 shows a year on Encore. One of the French three, a promoter of arena tours, is openly hostile to resale and said so in the first meeting: in his view it rewards people who never meant to come. The trio kept him deliberately, because a design partner who wants the product to fail will find the places where it can. Rowmate takes part in a separate, smaller program, for reasons the last part of this section gives. The same six promoters reappear in Chapter 5's conversations about fees, which keeps the evidence connected across the book.

Design partnership asks something of both sides. The promoters give a monthly working session, access to their box-office staff and a willingness to try unfinished things on real shows; Encore gives influence over the product, early access and hands-on help. That help is itself a discovery method. Graham's essay describes Stripe's founders setting new users up on the spot, a habit Y Combinator came to call the "Collison installation," and Airbnb's founders going door to door in New York to improve their hosts' listings. Encore's account managers sat with each pilot promoter's box-office manager while the rules were set, and the trio's designer sat with them, watching where the conversation stalled.

#### Sales-led requests {#c3-sales-requests}

Chapter 1 stated the principle that commitments made by sales become inputs to discovery. The mechanism is best seen in a single case. Early in the period, Encore's organizer sales team relayed a request from several promoters: "Can resale be turned off per show?" Instead of adding an off switch to the backlog, the trio asked the promoters why. Some artists' contracts forbid resale for intimate shows; one promoter had promised a fan club that its presale tickets would not reappear at any price; another wanted resale available only in the final week, when it would fill seats that would otherwise be empty. The underlying opportunity was "I must be able to honor what I have promised the artist and the fans," and an off switch was only one of its solutions. Resale windows and per-fan limits served it too, often better.

The distinction has a practical edge in Encore's markets. In Ireland, section 19 of the Sale of Tickets Act 2021 voids contract terms that prevent a ticket from being resold at or below face value, so an organizer there may not switch resale off entirely. A team that understood the opportunity could offer Irish organizers what the law allows, a lower cap, a window and per-fan limits, and still serve the promise behind the request. I spent a decade maintaining a widely used open-source library, and the most durable lesson of that work was that an issue titled "please add option X" almost always describes the reporter's workaround for some problem they have not mentioned. Cagan's *Transformed* (2024) describes how product and sales teams can work this way together, on the evidence of practitioners' experience across many companies.

#### The loudest customer {#c3-loudest-customer}

Business customers differ greatly in size, and size brings volume. Encore's largest tenant, the venue chain that runs in its own silo as `venue-chain-a`, has an account team, quarterly business reviews and a long list of requests, and early in the period it asked that resale for its venues run only through its own box office, under its own brand. It is a reasonable request, and it describes a different product from the one the strategy chose.

Christensen's *The Innovator's Dilemma* (1997) is the best-documented account of where that road leads. Studying the disk-drive industry, he found that established manufacturers listened carefully to their largest existing customers, who wanted more capacity in the existing form, and so missed each new, smaller drive architecture until entrants using it had taken the market. The lesson for discovery is modest and practical. The opportunity solution tree should record, for each opportunity, how many interviews and which segments it came from, so that a need heard loudly from one large customer can be seen beside a need heard quietly from many. On the trio's tree, `venue-chain-a`'s request sits as an opportunity with one source. Verified Resale is offered to organizers on every tier, and the venue chain gets the same rules console as everyone else.

#### Partners as a side {#c3-partners-as-a-side}

Rowmate is easy to think of as a channel, a pipe through which fans reach resale listings. Chapter 2's treatment of multi-sided markets suggests a better view. In Verified Resale, partners are one of the sides: marketplaces where fans list tickets they bought through the Gate, with their own economics, their own customers and their own risks. They are customers of Encore's platform as well as integrators of its interface, and discovery with them has to cover the business as well as the technology.

The trio's six conversations with Rowmate in this period concerned three things. The first was money: four points of the buyer's 10% fee on every sale made through it, against the margins it had earned on uncapped listings. The second was fraud. Under Partner Listings, Rowmate had absorbed chargebacks whenever a ticket sold through it turned out to have been sold twice, so reissue, a ticket that exists exactly once, was a benefit it could price. The third was support: who answers the fan when a reissued ticket has not arrived. These questions had to be settled before anyone discussed endpoints, and the key leak, caused by Rowmate's own contractor, hung over all of them. The design of the partner interface belongs to Chapter 9, and the partner program, with its agreements, certification and support, to the Software book's Section 8.3.

**Recap.** Business customers buy through a buying center, so discovery must reach the people who sign as well as the people who use the product. Six design partners from one segment, including one who opposes the idea, give a product focus and its first references, while partners on another side of the market need a program of their own. Sales requests are stories not yet heard, and the opportunity beneath them is what should be built for. Recording the source and segment of each opportunity keeps the loudest customer from setting the strategy.

**Exercise 3.3.** Take the last three requests from your largest customer. For each, write the problem you believe lies beneath it, then check your interview notes, support data or account records for any other customer with the same problem. Mark which requests turn out to be single-source opportunities.

### 3.4 Shaping the Work

#### Appetite {#c3-appetite}

Discovery tells a team which problem is worth solving, but not how much of the company's time the solution deserves, and asking engineers for an estimate gets that question backwards: an estimate starts from a solution, and the solution grows to fill whatever answer comes back. Ryan Singer's *Shape Up* (2019), which documents how Basecamp plans its work, inverts the question. **Appetite** is "the amount of time we want to spend on a project, as opposed to an estimate," and it is set first, by people with the authority to cut scope. The team then shapes a solution that fits the time. Singer's phrase for the principle is "fixed time, variable scope," and Basecamp works in two sizes: a small batch, one designer and one or two programmers for a week or two, and a big batch, the same team for six weeks.

Newspaper editors have always worked this way. An editor does not ask a reporter how many words the story needs; she assigns 800 words and a deadline, and the reporter decides which 800 words carry the story best. The analogy breaks at the point of cutting. A story cut from 1,200 words to 800 is still a story, since prose degrades gracefully. A product cut carelessly can lose a piece the others depend on, a ticket listed with no way to be reissued, and so cutting product scope needs the shaping work described next.

Encore's appetite needs a precise statement, because it is easy to misread. The trio set an appetite of six weeks for two small teams, lent from Orders & Payments and Partner APIs, and that appetite covered the discovery and prototype stage only: the hand-run pilot, the rules-screen prototype and the fake door. It did not cover building Verified Resale. The full product touches 12 teams, and a six-week appetite for that would be a fiction, since Shape Up's unit is a single small team and its six weeks are sized for one. The bet memo that Chapter 10 examines states its own appetite at a different scale, 12 months from the memo to the first ticket scanned at a gate, and the build is funded in tranches released against learning, as the Software book's Section 10.4 describes: discovery, then the first partner live, then all partners. At that scale appetite survives as an idea, a fixed budget against which a forecast is compared and scope is cut (the Software book, Section 10.3).

#### Shaping and the pitch {#c3-pitch}

Between a problem and a team's work, Singer places **shaping**: a short period in which a few senior people work out the solution at the right level of abstraction, concrete enough that the team knows what to build and rough enough that it can still make the detailed decisions. Two techniques keep the level right. A **breadboard**, borrowed from electronics, shows places, the things a user can act on in each, and the connections between them, with no visual design at all. A **fat-marker sketch** is a drawing made with a pen so thick that no fine detail is possible. Both are ways of deciding the elements of a solution without deciding its appearance.

Shaping ends in a **pitch**, a short document with five parts: the problem, the appetite, the solution, the rabbit holes (the details that could swallow the time and must be settled in advance), and the no-gos (what the work deliberately excludes). The evidence for the format is Basecamp's own published practice and its wide adoption by other teams, which is practitioner evidence and should be weighed as such. The format's strength is that it makes the boundaries of the work explicit before the work starts, when they are cheapest to argue about. Here is the trio's pitch for the discovery and prototype stage, as presented to the bet's sponsor:

```text
Pitch — Verified Resale, discovery and prototype stage
Problem      Resale of Encore tickets happens off Encore, unchecked. We don't know
             whether organizers will set rules or fans will trust a reissued ticket.
Appetite     Six weeks, two small teams (lent from Orders & Payments, Partner APIs).
Solution     Real listing and purchase screens for four pilot shows; reissue,
             revocation and rule checks done by Support by hand. A clickable
             rules screen tested with the six design-partner promoters.
Rabbit holes Automating reissue in the barcode core. Updating wallet passes.
             Seller payouts: pay by hand after each show.
No-gos       Dynamic or organizer-set resale prices. Any partner integration.
             Any change to primary checkout.
```

The no-gos carry as much weight as the solution. Dynamic resale prices were excluded because the strategy caps resale at face value, and every hour spent on pricing would have been an hour taken from the question of trust. Written down once, before the work began, each no-go spared the team from arguing the same point again in every planning meeting.

#### Betting at 40 teams {#c3-betting}

Shape Up also describes how Basecamp decides which pitches to fund. A small **betting table**, at Basecamp the chief executive, the chief technology officer, a senior programmer and a product strategist, meets between six-week cycles and chooses which pitches to bet on. Between cycles there is a two-week cool-down for fixing and exploring. And a **circuit breaker** ends any project that does not ship within its cycle by default, instead of extending it by default, so that no bet outgrows its appetite without a fresh decision.

It is worth being exact about where this evidence comes from. The book's appendix, "Adjust to Your Size," describes Basecamp as about 50 people in the whole company, with roughly a dozen in the product team. It does not describe a company of 40 product teams with dependencies running between them, and no well-documented public account of Shape Up's full calendar at Encore's size was found in preparing this book. Encore therefore borrows the mechanisms that travel, appetite, the pitch and the circuit breaker, and keeps its own quarterly planning cycle, which the Software book's Section 10.2 compares with the alternatives.

Large companies have their own long-running way of shaping a bet. Amazon's practice of "working backwards," described by Colin Bryar and Bill Carr in *Working Backwards* (2021), begins a proposal with a press release and a list of frequently asked questions (the PR/FAQ), written as though the product had already launched, so that the customer benefit is stated before anything is built. It is a closer precedent for a company of Encore's size, and Encore's bet memo, examined in Chapter 10, borrows from it.

#### The story map {#c3-story-map}

A pitch bounds a piece of work, while a release needs a picture of the whole journey. Jeff Patton's **user story map**, first described in 2005 and set out fully in *User Story Mapping* (2014), lays out the activities of a user's journey from left to right, in the order the user does them, as a **backbone**, with the details of each activity listed beneath it, most essential first. It reads as a narrative across and a priority list down, and it keeps the whole journey in view.

Verified Resale's map is unusual in having three sides on one backbone, since the journey passes from organizer to fan to fan to partner and back to the organizer's books. Figure 3.4 shows it, with the release slices drawn as rows.

| | Organizer sets rules | Fan lists through a partner | Another fan buys | Ticket is reissued | Buyer enters | Money is paid out |
|---|---|---|---|---|---|---|
| **First slice** | window and per-fan limits; face-value cap only | Rowmate only; one organizer's events | Bot Screening and per-buyer limits | new barcode issued, old one revoked | one venue in Lyon | split recorded; payouts after the event |
| **Launch slice** | off switch; lower cap | Encore's own app as well | all-in price with fee shown up front | wallet pass replaced, "your ticket sold" message | three organizers' venues in France | organizer share on every tier |
| **Later** | plain-language rule assistant | Tessera | — | — | more markets | — |

*Figure 3.4 — The story map for Verified Resale, with its backbone of six activities and three release slices. Each row is a complete journey, thinner above and fuller below.*

#### Slicing releases {#c3-slicing}

Patton's map is drawn to be cut horizontally. A line across it selects a **minimum viable release**: a release in which every step of the journey exists, each in its simplest useful form. Building each activity completely before starting the next produces months of work in which nothing can be used, because the journey does not yet connect.

The engineering counterpart is the **walking skeleton**, a term from Alistair Cockburn's *Crystal Clear* (2004): the thinnest slice of real function that can be built, deployed and tested from end to end. Patton adopts it, and the credit belongs to Cockburn. Verified Resale's first slice in Figure 3.4 is what its walking skeleton must carry: one organizer, with a resale window and per-fan limits and the face-value cap; fans listing only through Rowmate; buyers screened as in a primary sale; reissue and revocation in software; entry at one venue in Lyon; and the fee split recorded in the ledger. Everything in it is thin, and nothing is missing. The launch slice that Chapter 10 follows widens it to three organizers across France. How the skeleton is built belongs to the Software book (Sections 3.2 and 11.3), and how it is released safely, behind flags and in rings, to the Resilience book (Sections 4.3 and 4.4).

#### Stories are for telling {#c3-stories}

Patton's book carries a warning that is easy to agree with and hard to practice: shared documents aren't shared understanding. A story on a card or in a tracking tool is a reminder of a conversation, and cannot carry on its own the understanding the conversation produced. Ron Jeffries said the same in 2001 with three words from Extreme Programming: card, conversation, confirmation. The card is a token, the conversation is where the detail lives, and the confirmation, the acceptance tests, records what the two sides agreed.

The warning matters most where context must cross a team boundary. Within the trio, understanding passes easily; between teams it does not. When the first slice reached planning, its central story read, in effect, "when a resale completes, the seller's ticket is revoked and a new one issued to the buyer." To the Partner APIs team that was a single call. To the Inventory team, which owns the eight-year-old barcode core, it was a change to the oldest and least understood code Encore runs, with a question of ownership attached: should Resale reissue tickets itself, or ask Inventory to do it? It took two working sessions, with the trio's tech lead present to say what the product needed, before the story meant the same thing to both teams. The ownership question was settled by a written request for comments and a decision record, which the Software book's Section 9.5 describes.

**Recap.** Appetite fixes the time a problem deserves and lets scope vary, and Encore's six weeks for two small teams applied to discovery and prototyping only, with the build funded in tranches. A pitch states the problem, appetite, solution, rabbit holes and no-gos before work begins, and Basecamp's betting mechanisms travel to a large company better than its calendar does. A story map keeps the whole journey in view, a minimum viable release cuts across it, and its stories are prompts for conversations that must still take place, especially between teams.

**Exercise 3.4.** Write a one-page pitch for something on your roadmap with all five parts. Give it an appetite that someone with authority would sign, and at least two no-gos that a reasonable colleague might want included. Then show it to that colleague and record which no-go they argued with.

### 3.5 Discovery with AI

#### Prototypes in hours {#c3-ai-prototypes}

Of everything in this chapter, prototyping has been changed most by generative AI. A designer or engineer can describe a screen to a coding assistant and have a working, clickable version within hours, where a user prototype once took days and a live-data prototype weeks. Addy Osmani's *Beyond Vibe Coding* (2025) gives a practitioner's account of AI-driven prototyping, and in April 2025 Shopify's chief executive, Tobi Lütke, published a memo to staff which said that "the prototype phase of any GSD project should be dominated by AI exploration," GSD being Shopify's internal process for planning and running projects. Neither measures whether teams that prototype this way learn more or decide better, so this is emerging practice with practitioner evidence behind it. The broader evidence on AI and software work is in the Software book's Section 5.1.

The proven part is older than the tools. A prototype exists to answer a question, and once the question is answered it should be thrown away; Cagan makes the point for every kind of prototype, and Cockburn draws the same line between a throwaway spike and a skeleton meant to grow. Cheap generation makes the line more important, because a prototype built in an afternoon looks finished and invites someone to suggest shipping it, and code written to learn something, with no tests and no owner, is exactly the code that should never reach production. The Software book's Section 5.2 sets out where throwaway code belongs, and the Architecture book's Section 15.4 explains what cheap code does to systems it drifts into. Encore's rule is that prototypes live in a separate repository, are deleted when their question is answered, and are never promoted.

#### Synthesis with a trail {#c3-ai-synthesis}

After a few months of weekly interviews, a trio has dozens of snapshots and hours of transcripts. Large language models (LLMs) can help find the patterns, and here the evidence is young but real. Ziang Xiao and colleagues reported in 2023 that GPT-3, given an expert-written codebook, coded qualitative data with fair to substantial agreement with expert human coders. The limit matters: that is **deductive coding**, applying categories the researchers already defined, and asking a model to discover the themes on its own is a harder task with weaker evidence.

The safeguard comes from qualitative research's own standards. Yvonna Lincoln and Egon Guba's *Naturalistic Inquiry* (1985) made the **audit trail**, a traceable path from each conclusion back to the raw data that supports it, one of the tests of whether qualitative findings can be trusted. A model's summary has no such trail unless the team builds one. Encore's rule is that every opportunity on the tree links to the snapshots it came from, every quotation that reaches the tree or a slide is checked against the transcript before it is used, and a model's clustering is treated as a suggestion for the trio to examine. The checking matters, because a summary can merge two people's stories into one fluent paragraph that neither of them told.

#### Synthetic users {#c3-synthetic-users}

A more ambitious idea is to skip the interviews and ask a model to answer as a customer would. The research here is clearer, and mostly cautionary. Lisa Argyle and colleagues showed in 2023 that GPT-3, conditioned on the backstories of real survey respondents, reproduced some aggregate attitudes of American subgroups with what they called "algorithmic fidelity." A year later, James Bisbee and colleagues tested the idea against the American National Election Studies and found that while the synthetic averages tracked the real ones, the responses were far less varied than real people's, relationships between variables often differed significantly, results shifted with small changes in prompt wording, and the same prompt gave significantly different answers three months apart. The Nielsen Norman Group reran three of its own earlier studies with synthetic users in 2024 and found answers that were shallow and over-agreeable; synthetic learners claimed to have finished online courses that real learners had abandoned.

Aviation offers a fair comparison. A flight simulator is an extraordinary tool for rehearsal, but it is built from data recorded in real aircraft and can say nothing about an aircraft that has never flown. A synthetic user is a simulator built from the average of what people have written, and it cannot tell a team how its own customers will respond to something new, which is the question discovery exists to answer. The comparison even flatters synthetic users, since a flight simulator is validated against the aircraft it models and a synthetic customer has no equivalent check. Encore accepts synthetic users for one purpose, rehearsing an interview guide to find confusing questions before a real person hears them, and never as evidence of what customers need or will do.

#### Consent and data {#c3-consent}

Recording and transcribing interviews, and passing the transcripts through a model, are processing of personal data, and the General Data Protection Regulation (GDPR) applies to all of it. The team needs a lawful basis under Article 6, which for research interviews is usually consent meeting the conditions of Article 7. It must tell participants at the outset what will be recorded, why, by whom and for how long, as Article 13 requires. A transcription or AI service that processes the recordings on Encore's behalf is a processor, which needs a data processing agreement under Article 28. And if that service runs its models outside the EU, the transfer rules of Chapter V apply. A recording of a voice is personal data. It becomes biometric data, with the stricter rules of Article 9, only if it is processed to identify people, which ordinary transcription does not do. Teams should be precise here, since both ignoring the rule and overstating it lead to bad decisions. Organizer staff interviewed as employees of a business customer are data subjects in exactly the same way as fans.

Encore keeps its research repository in EU-1, under the same residency rules as its other personal data, and runs model-assisted synthesis through its AI gateway, so that transcripts reach only models approved for that data. The consent workflow across all 40 teams belongs to Chapter 6, and data residency in general to the Architecture book's Chapters 9 and 10.

#### What the trio still does in person {#c3-in-person}

Everything in this section makes some part of discovery cheaper. None of it changes what discovery is for, which is to put the people who build a product in contact with the people who use it, and the scarce resource in that contact has always been attention. Cheaper prototypes make that attention more valuable, since a team that can test more ideas needs more real people to test them with.

Intuit's chief executive Brad Smith, interviewed by Fortune in 2017, put the conviction in one sentence: "What you get from a follow-me-home you can't get from a data stream." In the four months of discovery, the resale trio's most consequential observations did not come from interviews at all. They came from evenings spent with the box-office staff of two design-partner promoters on show nights, watching how resale questions actually reached them: by phone, by fans at the door holding forwarded screenshots, and by an artist's tour manager asking why a fan-club ticket had appeared on a marketplace. Those evenings are why the first message the trio designed for sellers was about the old ticket rather than the money. I have come to believe that the measure of a discovery practice is how often the people who build the product are in the room when their customers struggle, and that no tool yet built changes the answer.

**Recap.** AI makes prototypes far cheaper, which is emerging practice with practitioner evidence, and the proven rule that prototypes are thrown away matters more as they get easier to make. Models can help sort research notes, provided every finding keeps an audit trail to its source, while synthetic users can rehearse an interview guide and are never evidence of demand. Consent and data protection apply to every recording, and the human work of discovery, watching real customers in their own setting, becomes more valuable as everything around it gets cheaper.

**Exercise 3.5.** Take one AI-generated summary of customer research from your organization. Pick three of its claims and trace each one back to the raw notes or transcripts. Count how many survive unchanged, how many survive in weaker form, and how many have no source at all.

### Kata: The Empty Chair

> **Your brief: "Clinicly."** Clinicly sells appointment-scheduling software to private clinics in Germany, Austria and the Netherlands: about 1,400 clinics, from single physiotherapy practices to dental groups of 200 sites. It has 90 engineers in 11 teams. Receptionists use the product all day; patients book through a web page and an app; clinic groups sign the contracts, through an operations director and, in the larger groups, a procurement team. No-shows are Clinicly's customers' biggest complaint: on average, 14% of booked appointments go unattended, and an empty chair costs a clinic the full fee. The largest dental group, a fifth of Clinicly's revenue, has asked for automatic double-booking of risky slots, and sales has promised a waitlist that fills cancelled slots automatically in order to close a deal with a physiotherapy chain. The chief executive has offered three clinic groups places as design partners: the dental group, the physiotherapy chain and a dermatology group. Nobody on the product teams has spoken to a patient this year. Patients' booking histories reveal health information, which is special-category data under the GDPR.

**Deliverables:**

1. **A six-week discovery plan** — the weekly cadence for one trio, automatic recruitment of receptionists, patients and clinic managers, how to reach patients who never booked, and consent and data handling for each, given that appointment histories are health data.
2. **An opportunity solution tree** — rooted in one product outcome about attended appointments, with at least five opportunities from at least three kinds of participant, each with its source and segment. Show where the double-booking request and the promised waitlist sit once their underlying problems are written down.
3. **An assumption map and one cheap test** — for your top-ranked solution, list its assumptions by Torres's five types and design a test for the riskiest that takes under a week. If it is a Wizard of Oz or a fake door, say what the patient sees, what happens behind it, and why no patient can be left with a booking that does not exist.
4. **A design-partner program** — Clinicly's three groups span three segments. Argue for one segment and a set of six clinics within it, saying what to do about the three groups already promised places, and name the clinic you would recruit because it doubts the idea.
5. **A pitch** — for the first piece of work to come out of discovery, with all five parts, an appetite sized for one small team, and at least two no-gos, one of which the sales team will dislike.
6. **A pre-registered decision rule** — the measures, thresholds and decision-makers for your test, written as it would be signed before the test begins.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Contact | Will someone who builds the product speak to a receptionist or a patient every week, and how will the plan survive a busy week? |
| Needs before features | Does every solution on the tree hang from an opportunity stated in a customer's words, including the two requests from sales and the largest customer? |
| Riskiest first | Is the test aimed at the assumption the idea most depends on, and could it be run before anything is built? |
| Focus | Do the design partners come from one segment, and would the hostile one actually find the weak points? |
| Honesty | Does every test treat patients truthfully, with no booking, price or slot shown that does not exist? |
| Commitment in advance | Was the decision rule written before the data, and does it say who decides and by when? |

#### Where you now stand

You can now keep contact with customers as a weekly habit, interview for stories about the past instead of predictions, and organize what you hear into a tree that shows leaders your reasoning. You can unpack an idea into its assumptions, test the riskiest one cheaply, with a Wizard of Oz if need be, and decide what to do next against criteria written before the test. You can run discovery with business customers who buy through many hands, keep the loudest of them in proportion, and shape the result into a pitch and a release slice that cut across a whole journey. Discovery, though, mostly tells us what people do and why. It is weaker at telling us how much, how often and whether a change caused the difference we see, and the pilot's four shows could not say how many fans across Encore's catalog would resell. Those are questions of measurement, and the most rigorous answers to them were first worked out in agricultural field trials, where Ronald Fisher learned to tell a real effect from the noise of weather and soil. Chapter 4 takes up metrics, instrumentation and controlled experiments.

### References

- Teresa Torres — *Continuous Discovery Habits: Discover Products that Create Customer Value and Business Value*. Product Talk LLC, 2021.
- Marty Cagan — *INSPIRED: How to Create Tech Products Customers Love*, 2nd ed. Wiley, 2017.
- Ryan Singer — [*Shape Up: Stop Running in Circles and Ship Work that Matters*](https://basecamp.com/shapeup). Basecamp, 2019 — free online.
- Eric Ries — *The Lean Startup*. Crown Business, 2011.
- Jeff Patton, Peter Economy — *User Story Mapping: Discover the Whole Story, Build the Right Product*. O'Reilly Media, 2014.
- Geoff Colvin — [*How Intuit Reinvents Itself*](https://fortune.com/2017/10/20/how-intuit-reinvents-itself/). Fortune, 2017 — free online.
- Intuit Inc. — [*From Kitchen Table to Boardroom Table: History of Quicken*](https://http-download.intuit.com/http.intuit/CMO/intuit/press_room/vpk_quicken_win/History_of_Quicken.doc). Press kit, 2006 — free online.
- J. F. Kelley — [*An Iterative Design Methodology for User-Friendly Natural Language Office Information Applications*](https://doi.org/10.1145/357417.357420). ACM Transactions on Office Information Systems 2(1), 1984.
- Paul Graham — [*Do Things That Don't Scale*](https://paulgraham.com/ds.html). 2013 — free online.
- Marty Cagan, Lea Hickman, Christian Idiodi, Chris Jones, Jon Moore — *Transformed: Moving to the Product Operating Model*. Wiley, 2024.
- James Bisbee, Joshua D. Clinton, Cassy Dorff, Brenton Kenkel, Jennifer M. Larson — [*Synthetic Replacements for Human Survey Data? The Perils of Large Language Models*](https://doi.org/10.1017/pan.2024.5). Political Analysis 32, 2024 — free online.
- Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, David Wingate — [*Out of One, Many: Using Language Models to Simulate Human Samples*](https://arxiv.org/abs/2209.06899). Political Analysis 31(3), 2023 — free online.
- Maria Rosala, Kate Moran — [*Synthetic Users: If, When, and How to Use AI-Generated "Research"*](https://www.nngroup.com/articles/synthetic-users/). Nielsen Norman Group, 2024 — free online.
- Ziang Xiao, Xingdi Yuan, Q. Vera Liao, Rania Abdelghani, Pierre-Yves Oudeyer — [*Supporting Qualitative Analysis with Large Language Models: Combining Codebook with GPT-3 for Deductive Coding*](https://arxiv.org/abs/2304.10548). IUI '23 Companion, ACM, 2023 — free online.
- Clayton M. Christensen — *The Innovator's Dilemma*. Harvard Business School Press, 1997.
- Desirée Sy — *Adapting Usability Investigations for Agile User-Centered Design*. Journal of Usability Studies 2(3), 2007.

---

## Chapter 4: Measuring Products — Analytics and Experimentation {#ch4}

> "Every experiment may be said to exist only in order to give the facts a chance of disproving the null hypothesis." — R. A. Fisher

How do we know that something we built made a difference? In a small company the question often answers itself: the founders ship a change on Monday, watch the numbers on Tuesday, and believe what they see. At 400 engineers it grows harder in every direction. Forty teams ship changes in the same week, the season and the tour calendar move the numbers, and a team that wants its change to have worked will find a reading of the dashboard in which it did. We need a way of separating the effect of one change from everything else that is happening, and a discipline for choosing, before we look, which number will count as the effect. This chapter is about both: the metrics we choose, the instruments that record them, and the experiments that let us read them honestly.

The method we rely on was worked out in a field of wheat. In 1919 Ronald Fisher, then a schoolteacher, was hired by John Russell, the director of Rothamsted Experimental Station in Hertfordshire, to make sense of the decades of records from the station's long-running field trials. Agricultural experimenters of the day wanted to know whether a fertilizer raised the yield, but the soil varied from plot to plot in ways no one could list: a damp corner here, a richer strip there. However carefully an experimenter arranged the plots, the arrangement might line up with some unseen variation in fertility, and the fertilizer would then be credited or blamed for what the soil had done. Fisher's answer, set out from Rothamsted in "The Arrangement of Field Experiments" (1926), was to assign plots to treatments "deliberately at random". He refined the idea into the *randomized block*: divide the field into blocks of similar ground, and within each block assign the treatments "independently, and wholly at random". He knew his readers would resist. "Most experimenters on carrying out a random assignment of plots", he wrote, "will be shocked to find how far from equally the plots distribute themselves." Chance distributes the plots unevenly, but its unevenness is the kind probability can measure, whereas the experimenter's own arrangement errs in ways nobody can measure at all.

Fisher left Rothamsted in 1933 to become Galton Professor at University College London, and there he wrote *The Design of Experiments* (1935). Its second chapter opens with a lady who "declares that by tasting a cup of tea made with milk she can discriminate whether the milk or the tea infusion was first added to the cup". As Fisher's daughter and biographer Joan Fisher Box told the story, the lady was Muriel Bristol, an algal biologist at Rothamsted, and popular accounts add that she named every cup correctly. Fisher's interest was in how to test her claim: eight cups, four of each kind, in random order, so that guessing all eight by luck has a probability of 1 in 70. The book then states the two ideas on which every online experiment still rests. The null hypothesis, the claim that the treatment does nothing, "is never proved or established, but is possibly disproved, in the course of experimentation". And "the simple precaution of randomisation will suffice to guarantee the validity of the test of significance". Fisher did not invent randomization; Charles Sanders Peirce and Joseph Jastrow had randomized the order of stimuli in a psychology experiment in 1884. His contribution was the argument that randomization is what *makes* a test valid, together with designs that made it practical. He was also a committed eugenicist all his life, which is why his Cambridge college removed a window commemorating him in 2020.

Encore needs Fisher now. Verified Resale, the bet this book follows, has a memo with a north star and guardrails in it, and the memo will be judged by them. Somebody has to decide exactly what those metrics mean, record the tracking events that compute them, and test the smaller changes along the way, such as whether showing verified listings on a sold-out event page keeps fans on it. Encore already runs experiments, and a team, Experimentation, owns the platform for them. But the bet as a whole cannot be tested the way a button color can, because fans, seats and organizers are shared between any test group and any control group: a seat resold to one fan is a seat another fan cannot buy. Section 4.1 chooses the metrics, Section 4.2 treats the events that feed them as contracts, Section 4.3 runs controlled experiments, Section 4.4 builds the platform that lets 40 teams run them, and Section 4.5 asks what to do when a clean experiment is impossible, a question Fisher's fields never had to answer.

### 4.1 Choosing Metrics

#### What makes a metric useful {#c4-good-metrics}

A metric earns its place by changing what someone does. Alistair Croll and Benjamin Yoskovitz, in *Lean Analytics* (2013), call this their most important rule: a number that will not change how we behave is a bad number, however interesting it looks on a screen. They give four properties of a good metric. It is *comparative*, so that we can set it against last month, another group or a target. It is *understandable*, so that people remember and discuss it. It is a *ratio or a rate*, because ratios survive changes in scale. And it *changes behavior*, the property the other three serve. Their sharpest distinction is between vanity metrics and actionable ones. Total registered fans is a vanity metric: it only ever rises, and no decision depends on it. The share of this month's buyers who bought again within 90 days is actionable, because it can fall, and when it falls someone has to find out why.

*Lean Analytics* also separates *leading* metrics, which predict what will happen, from *lagging* ones, which confirm what already has. Churn is lagging: by the time a customer has left, the number can only explain the departure. A fall in weekly logins among one cohort of organizers is leading, because it gives the account team time to act. We need both, and we need to know which is which, since a leading metric that is never checked against the lagging one it claims to predict is only a hope. Chapter 3 met a close relative of these ideas in Eric Ries's innovation accounting (Section 3.2); this section takes the general criteria further, because a company of 40 teams needs them to hold across every product.

Criteria tell us whether a metric is good; they do not tell us where to find one. The most tested bridge is the one Kerry Rodden, Hilary Hutchinson and Xin Fu described from Google in 2010, Goals–Signals–Metrics. We begin with a *goal* in plain words ("fans who cannot go can pass their ticket on safely"), ask what behavior would *signal* that the goal is being met ("listings are created, and they sell before the show"), and only then choose a *metric* that counts the signal. The same paper offered the HEART categories (happiness, engagement, adoption, retention and task success) as a checklist of goals. The order of the steps matters more than the categories, because a team that starts from the metrics its tools happen to offer ends up optimizing what is easy to count.

What a team should count also depends on its business model and its stage, and *Lean Analytics* devotes most of its length to that point. A two-sided marketplace watches its *liquidity*, the chance that a listing finds a buyer and a buyer finds a listing; a software-as-a-service business watches churn and expansion revenue. The book's benchmark figures come from startups of 2012 and 2013 and should not be quoted as current, and its stages assume a young company. Encore is not young, and it runs several models at once: a retailer of primary tickets, a SaaS vendor to venues, and now a resale marketplace, whose liquidity belongs to Section 2.3 and to the Software book's Sections 8.2 and 8.5. What every product shares is the weekly reading of *cohorts*, groups of customers who started in the same period, followed over time. A cohort table shows whether fans who first used resale in March behave differently from those who started in May, which an overall average cannot show, because it mixes old customers with new ones.

#### North star and its inputs {#c4-north-star}

A large organization needs one number that says what value the product delivers. A **north star metric** is a single measure of the value customers receive from a product, chosen so that growth in it means the business is growing for the right reason. The practice has a widely used playbook, John Cutler and Jason Scherschligt's *North Star Playbook* from Amplitude, but no controlled evidence behind it, so we should treat it as a communication device: a way of telling 40 teams which direction is north, so that each can work out its own heading. The playbook is candid that a north star "is not immediately actionable", which is why it pairs the star with **input metrics**, the few measures that teams can move directly and that together drive the star. It expects the star to be revised every one to three years in an established company.

The Verified Resale memo names its north star as verified resales completed per eligible event, and the work of this section is to say what "completed" means. Encore's answer is a resold ticket that scans at the door. A listing is an intention and an order is a payment; the scan is the moment the buyer actually walks into the concert. Counting at the door means that a resale reissued wrongly, revoked by mistake or blocked at a gate whose revocation list had gone stale does not count, even though every earlier step reported success. It also makes the metric lagging, since it completes only after the show. Three inputs give the teams something earlier to steer by: the **listing rate** (the share of eligible tickets that are listed), the **resale conversion** (the share of listings that sell before the resale window closes) and the **reissue success** (the share of sold listings whose reissued ticket is accepted at the gate). Resale owns the first two; Inventory, Venue Entry and Fan Messaging share the third.

The north star sits at the level of strategy. Objectives and key results, which turn strategy into quarterly commitments, belong to Section 2.5 and are not re-taught here. What this chapter adds is the step below: the metric that decides an individual experiment.

#### The overall evaluation criterion {#c4-oec}

Ron Kohavi, Diane Tang and Ya Xu, in *Trustworthy Online Controlled Experiments* (2020), define the **overall evaluation criterion (OEC)** as "a quantitative measure of the experiment's objective". In practice it is a metric, or a small weighted combination of metrics, agreed before an experiment runs, measurable within the experiment's few weeks, and believed to predict the long-term value the north star describes. The north star tells the company where it is going; the OEC tells one experiment whether it helped. Its great virtue is social. When the OEC is agreed in advance, an argument about a result becomes an argument about the metric, and that argument can be held calmly before anyone's work is on the line.

The trouble is that a metric can be a ratio, understandable and comparative, and still reward harm. Kohavi and colleagues reported a case from Bing at KDD 2012. A bug in an experiment showed users very poor search results, and two of Bing's key metrics went up: "distinct queries per user went up over 10%, and revenue per user went up over 30%". Users were searching more, and clicking more ads, because they could not find what they wanted. A team with queries per user as its OEC would have shipped the bug. Bing put sessions per user in its OEC instead, on the reasoning that a user who finds answers comes back more often, while one who cannot simply searches harder.

Medicine has learned the same lesson at a higher price. A trial that waits to count deaths may take years, so trials often measure a **surrogate endpoint**, a quicker measurement believed to predict the outcome that matters, such as blood pressure. In the late 1980s the Cardiac Arrhythmia Suppression Trial tested drugs that suppressed the irregular heartbeats known to predict sudden death after a heart attack. The drugs did suppress them, and patients on two of them also died at a higher rate than patients on placebo; that part of the trial was stopped early in 1989. An OEC is a surrogate endpoint for the north star and carries the same risk. The analogy has a limit, in our favor: a software company can run thousands of experiments and check, across them, whether movements in its OEC were later followed by movements in its long-term outcomes, a check few clinicians can make.

For experiments on the resale flow, Encore's OEC is resale conversion within an experiment's triggered population, read alongside the reissue success, because an experiment that sells more listings but produces more failed reissues has only moved a problem from one screen to another. Experiments elsewhere in the fan app use their own OECs, and Section 4.4 explains how the definitions are kept consistent.

#### Guardrails {#c4-guardrails}

An OEC says what we hope to improve. A **guardrail metric** is a metric that must not get worse, however much the OEC improves. Kohavi, Tang and Xu distinguish two kinds. *Organizational guardrails* protect the business and its customers: latency, errors, revenue, the experience of groups the experiment was not aimed at. *Trust guardrails* protect the experiment itself, by checking that it was run correctly, and Section 4.3 takes them up. Latency is the classic organizational guardrail, because almost any feature can be made more engaging by making it heavier. When Kohavi and Stefan Thomke reported a Bing experiment, discussed again in Section 4.3, that raised revenue by 12% "without hurting key user-experience metrics", it was the guardrails that entitled them to the second half of the sentence.

The word "guardrail" means something else in the Architecture book's Section 12.4 and the Resilience book's Chapter 8, where it names runtime safety checks on AI models; here it means a metric. For Verified Resale the guardrails come from the bet's own risks: resale must not eat primary sales, reopen the door to bots or fraud, drive organizers away or flood Support. One guardrail Encore did not have to invent. The Resilience book's checkout objective (Section 1.2), 99.9% of checkout attempts ending well within 3 s, already describes what fans expect of any purchase, and reusing it keeps one meaning for "checkout works" across the company. Figure 4.1 gathers the set.

| Metric | Kind | Definition | Why it is there |
|---|---|---|---|
| Verified resales completed per eligible event | North star | Resold tickets that scan at the door, per event with resale open | Counts value at the moment it is delivered, at the door |
| Listing rate | Input | Eligible tickets listed ÷ eligible tickets | Supply: are fans who cannot go using it? |
| Resale conversion | Input; OEC for resale-flow experiments | Listings sold before the window closes ÷ listings | Liquidity seen from the listing's side |
| Reissue success | Input | Sold listings whose reissued ticket is accepted at the gate ÷ sold listings | The promise "verified" makes |
| Primary sell-through | Guardrail | Primary tickets sold ÷ capacity, against matched events | Resale must not eat the primary sale |
| Bot and fraud rate | Guardrail | Resale purchases blocked or charged back per 1,000 | Resale must not reopen the door to bots |
| Organizer opt-out rate | Guardrail | Organizers disabling resale ÷ organizers eligible | Organizers must keep wanting it |
| Support contacts per resale | Guardrail | Support cases tagged resale ÷ completed resales | The cost of confusion |
| Checkout objective | Guardrail (reused) | The Resilience book's checkout SLO, applied to resale checkouts | One meaning of "checkout works" |

*Figure 4.1 — Verified Resale's metrics. The north star is lagging by design; the inputs give teams something earlier to steer by, and the guardrails name what the bet must not cost.*

The share of resales sold at the face-value cap is not in the table, and its absence is deliberate. Encore watches it, because it says something about demand for each event, but it is neither good nor bad in itself, and a metric with no direction cannot guard anything.

**Recap.** A good metric is comparative, understandable, a ratio, and changes what someone does; Goals–Signals–Metrics finds such metrics by starting from what users are trying to achieve. A north star tells many teams which way is north, its inputs give them something to steer by, and the OEC decides each experiment. The Bing ranking bug shows that a sensible-looking OEC can reward harm, which is why it travels with guardrails, both for the business and for the experiment's own trustworthiness.

**Exercise 4.1.** For a product you know, write a north star, three input metrics and three guardrails, using Figure 4.1 as a model. For the north star, name the moment at which value is actually delivered, and check whether your current metric counts that moment or an earlier one. Then name the case, like the Bing bug, in which your OEC would improve while users were worse off.

### 4.2 Instrumentation as a Contract

#### Tracking events are an API {#c4-tracking-events-api}

A word first, because Encore's vocabulary forces it. At a ticketing company an *event* is a concert (`encore.event_id`, in the Operations book's registry, names one). So this book calls the records that product analytics collects **tracking events**: structured records, emitted when a person or the system does something of interest to the product, that downstream metrics, experiments and models consume. Their names follow one grammar, set for both books: snake_case, an object and a past-tense action, with the domain as a prefix. `resale_listing_created` records that a listing came into being; `resale_ticket_reissued` records that the barcode core issued a new ticket identity. The past tense matters because a tracking event records a fact that has happened, the same reason the Architecture book names its domain events `SeatSold` and `OrderPlaced`.

Once named, a tracking event is an interface with consumers the producing team will never meet: experiment scorecards, Organizer Insights dashboards, forecasting models, and next year's analyst. The Architecture book has already argued that a published event is a contract, evolved by addition (Section 6.1), that a stream such as `ticket-sales.v2` should be run as a product (Section 6.5), and that data products follow the same logic (Section 9.4). Tracking events add something particular to that argument, which is the way they fail. When a backend team renames a field in an API, a client breaks and somebody is paged. When a frontend team renames `listing_created` to `listing_published` in a refactor, nothing breaks. A dashboard line falls to zero, or an experiment's treatment arm quietly loses a third of its conversions, and the number that comes out is wrong without being absent.

Surveyors have a practice that captures what is at stake. Across Britain, the Ordnance Survey cut *bench marks* into the walls of churches and bridges, each a known height from which other heights could be measured. If a builder chiselled one off and recut it a foot lower, every level taken from it afterward would still produce a figure, and every figure would be wrong by a foot. A silent rename is a recut bench mark. The comparison breaks in one useful place: a bench mark is cut in stone so that it cannot change, whereas tracking events must change as the product does. So they change in public, with a version, an owner and a review, and every consumer learns of the change before it lands.

#### The tracking plan {#c4-tracking-plan}

The **tracking plan** is the reviewed list of a product's tracking events: for each one, its name, its properties and their types, the trigger that emits it, its owner, and the question it exists to answer. The last field is the one most often left out and the one I would least like to lose, because an event whose question nobody can state collects data nobody will use, which a company must still secure, retain and eventually erase. The tracking plan as a reviewed artifact is common practice, supported by vendor tools such as Segment's Protocols and Snowplow's schemas, though not by peer-reviewed study; *Trustworthy Online Controlled Experiments* states the principle behind it, that logging is designed and reviewed with the feature.

Here is one entry from the Resale team's plan:

```yaml
- name: resale_listing_created
  owner: Resale team
  trigger: Resale service accepts a listing, after organizer rules pass (server side)
  question: How many eligible tickets do fans offer, and through which channel?
  properties:
    encore.event_id:   {type: string, required: true}
    listing_id:        {type: string, required: true}
    seller_pseudonym:  {type: string, required: true}
    channel:           {type: enum, values: [encore_app, rowmate, tessera]}
    price_to_face:     {type: number, min: 0, max: 1}
    seats:             {type: integer, min: 1}
  consumers: [listing_rate, organizer_insights_resale]
  version: 1
```

Three choices in the entry are worth reading closely. The trigger is server-side and fires only after the organizer's rules pass, so the event counts listings that exist, and partner listings from Rowmate and Tessera are counted by the same code as Encore's own. The identifiers reuse the names in the Operations book's attribute registry (Section 4.2 of that book), so `encore.event_id` means the same concert in a tracking event, a trace and a sales report, and the three can be joined. And the seller is a pseudonym, never a name or an email address, for reasons the next subsection gives.

Encore checks the plan in continuous integration: a change that emits an event not in the plan, or changes a property's type, fails its build, and a change to the plan itself needs a review from the event's listed consumers. This is Encore's choice, and a sound one at its size, but the evidence for it is practitioners' reports. The tracking-event schemas sit in the schema registry that the Event Backbone team runs, beside the domain events, and the Experimentation team owns the plan's format and the check.

#### Instrumentation in the platform {#c4-instrumentation-platform}

Where an event is logged matters as much as what it records. Kohavi, Tang and Xu give separate chapters to client-side experiments and to instrumentation, and the lesson of both is that clients and servers see different things. A server knows for certain that a listing was created, because it created it. Only the client knows whether a fan actually saw the verified-listings panel, which may have loaded below the fold or after the fan left. Outcomes therefore belong on the server, and *exposures*, the moments at which a person actually met a variant, on the client. Client logging also loses data in ways server logging does not: browsers close, phones go offline, ad blockers drop requests, and each loss can differ between the arms of an experiment.

The best evidence that this matters comes from Microsoft. Aleksander Fabijan and colleagues reported at KDD 2019 that about 6% of Microsoft's experiments showed a sample ratio mismatch, a split between the arms that differed from the one designed, and one cause in their taxonomy was a faster variant. Because the treatment loaded faster, its telemetry had more time to be sent before users left, so the experiment recorded more users in the faster arm. The logging had counted them more completely, and a bug in instrumentation had become a bias in the result.

That is the argument for putting logging in the platform. If every team writes its own code to batch, retry and send tracking events, every team will lose data in its own way. Encore's web and mobile shells carry one tracking SDK, owned by the Experimentation team, which batches events, queues them while offline, stamps the registry identifiers and active experiment assignments on each one, and enforces the consent state described below. The same reasoning shaped the Operations book's account of OpenTelemetry (its Section 4.2): a shared vocabulary stays shared only if the code that writes it is shared too. The SDK's behavior on phones is Section 8.4's subject.

#### Consent and the fans we cannot see {#c4-consent}

European law makes consent part of the instrument. The ePrivacy Directive (2002/58/EC, Article 5(3), as amended in 2009) requires consent before information is stored on or read from a user's device unless it is strictly necessary for the service the user asked for, and the European Data Protection Board's Guidelines 2/2023 extend this to pixels, URL tracking and similar techniques. The GDPR requires a lawful basis for processing (Article 6), limits retention (Article 5(1)(e)), and says in Recital 26 that pseudonymized data is still personal data. In *Planet49* (2019) the Court of Justice of the EU held that a pre-ticked box is not valid consent. The ePrivacy Regulation meant to replace the Directive was withdrawn in February 2025, so the Directive still governs; the Commission's November 2025 "Digital Omnibus" proposal to move cookie rules into the GDPR remains a proposal.

Within those rules there is one well-documented path for measurement without consent. France's data protection authority, the CNIL, exempts audience measurement from consent under strict conditions: users are informed and can object; the purpose is limited to audience measurement and A/B testing; the data is not combined with other processing; the tracker is first-party; the last byte of the IP address is truncated; and trackers live no longer than 13 months. Encore built a narrow first-party channel to those conditions, which counts exposures and outcomes for experiments and nothing else. It uses the channel in France, where the CNIL's guidance applies, and wherever else a national regulator accepts the same scope; everything beyond it waits for consent. Raw tracking events are kept for 13 months, pseudonymously, in Encore's EU regions, and the erasure machinery of the Architecture book (Sections 6.2 and 9.5) reaches every copy when a fan asks to be forgotten.

The design question most teams skip is what consent does to the numbers. Where consent is required, between 52% and 78% of Encore's fans grant it, depending on the country. Those who refuse are not a random sample; in Encore's data they skew toward desktop users, so a metric computed from consented fans describes a different population from the one Encore serves, and differently in each country. Consent can also differ between the arms of an experiment. If a treatment moves or delays the consent banner, a different share of each arm consents, and the consented population splits unevenly, which the trust checks of Section 4.3 exist to catch. Encore's rule is that no experiment may change the consent experience except one designed to study it, and that the exempt channel carries the OEC wherever the law allows.

#### Two kinds of telemetry {#c4-two-telemetries}

Operational telemetry, the traces, metrics and logs of the Operations book's Chapter 4, answers the question "is the system working?". Product telemetry answers "is the product worth it?". The first is read by on-call engineers in minutes, kept for weeks and sampled heavily; the second is read by product trios over weeks, kept for months, and never sampled in a way that would bias an experiment. The boundary blurs, and honestly so: latency is an operational signal and also, as Kohavi's book shows, one of the most powerful product metrics there is. Encore's resolution is that the two kinds share identifiers, so that `encore.event_id` and `encore.country` mean the same in both and can be joined, while keeping separate owners, retention and contracts. The Reliability team owns the operational registry, the Experimentation team owns the tracking plan, and each reviews the other's additions to the shared names.

**Recap.** A tracking event is an interface whose consumers its producer never meets, and its characteristic failure is silent: a renamed event yields wrong numbers instead of errors. A tracking plan names each event, its owner, its trigger and the question it answers, and a shared SDK makes 40 teams log alike, because instrumentation bugs become biased results. Consent law shapes the instrument, and refusals bias the sample in ways that differ by country and can differ between arms.

**Exercise 4.2.** Write the tracking plan for one feature you own: five tracking events, their properties, their triggers, their owners and the question each answers. Mark each event as server-side or client-side and say why. Then find one event in your current analytics whose question nobody can state, and decide whether to delete it.

### 4.3 Online Controlled Experiments

#### Most ideas fail {#c4-most-ideas-fail}

The strongest argument for experimentation is how often our ideas turn out to be wrong. In a 2009 paper for Microsoft's ThinkWeek, of which a public version was released, Kohavi and colleagues reported that of experiments designed to improve a key metric, "only about one-third were successful at improving the key metric". Kohavi and Thomke wrote in 2017 that "at Google and Bing, only about 10% to 20% of experiments generate positive results", and that at Microsoft as a whole a third prove effective, a third are neutral and a third are negative. These are ideas that experienced people believed in enough to build. A company that ships without testing is therefore shipping a great deal of neutral and harmful work, with no way of knowing which part.

Kohavi gave the opposing habit a name. In a KDD paper of 2007 he and his co-authors urged readers to listen to their customers and not to the HiPPO, the HIghest-Paid Person's Opinion. The joke has lasted because it names a real force. In the absence of evidence, decisions go to rank, and rank is no better at predicting what users will do than anyone else.

The same evidence cuts the other way, and that half is less often told. At Bing, an employee proposed lengthening ad titles by moving text from the line beneath into the title. The idea sat in the backlog "for more than six months", judged low priority, until an engineer tried it in a cheap experiment. Revenue rose 12%, worth more than $100 million in the United States alone by the authors' account, and it became, in their words, "the best revenue-generating idea in Bing's history". Intuition does not only overvalue bad ideas. It also buries good ones, and here it was a cheap test that brought one back.

#### Designing one experiment {#c4-designing-experiment}

An **online controlled experiment**, or A/B test, randomly assigns units, usually users, to two or more variants of a product, and compares a metric between them, so that any difference beyond chance can be attributed to the variant. It is Fisher's randomized block with fans for plots. The design has six parts, and each must be written down before the experiment starts: a hypothesis, a unit of randomization, a trigger, an OEC with its guardrails, a sample size, and an analysis plan.

Encore's first experiment on Verified Resale is planned for the weeks after the launch widens across France. Its hypothesis is that showing verified listings on a sold-out event page reduces the share of fans who leave with no next step: they neither open a listing, join the event's alerts nor move to another event. The unit is the fan, identified by account when signed in and by device otherwise. The **trigger** is the condition that admits a unit into the analysis, here reaching the sold-out page of an event with resale open; it matters because most visitors never see a sold-out page, and analyzing everyone would bury a real effect among millions of fans the change could not have touched. One caution belongs in the plan. The test changes what fans see, but if treated fans buy listings that control fans would otherwise have bought, the arms are no longer independent. Section 4.5 takes that problem up; for a display test in which few fans convert, Encore judges the bias small, and says so in writing.

The sample size follows from a short calculation that every product team should be able to do. For a test at the usual 5% significance level and 80% power, the number of units needed in each arm is approximately 16σ²/δ², where σ² is the variance of the metric and δ is the smallest change worth detecting. The 16 is not magic: it is twice the square of the sum of the two normal quantiles involved, 2 × (1.96 + 0.84)², which comes to 15.7. For a rate *p*, the variance is *p*(1 − *p*). On the sold-out pages, about 80% of fans currently leave with no next step, so σ² is 0.8 × 0.2, or 0.16. Figure 4.2 works the arithmetic for the roughly 70,000 fans a week Encore expects to trigger in France.

| Smallest change worth detecting (δ) | Fans per arm | Fans in total | Weeks at 70,000 a week |
|---|---|---|---|
| 2 points (80% to 78%) | 6,400 | 12,800 | under 1 (run 2) |
| 1 point | 25,600 | 51,200 | under 1 (run 2) |
| 0.5 points | 102,400 | 204,800 | about 3 |
| 0.25 points | 409,600 | 819,200 | about 12 |

*Figure 4.2 — Sample size for the sold-out-page experiment. Halving the effect we want to detect quadruples the fans we need; the two-week minimum covers two full weekly cycles of on-sales.*

The table shows the most important fact about experiments: sample size grows with the square of the precision we ask for. A team that wants to detect a quarter-point change at this traffic must wait three months, and probably should not try. One well-proven method buys precision cheaply. Alex Deng, Ya Xu, Ron Kohavi and Toby Walker described CUPED at WSDM 2013: it uses each unit's behavior before the experiment to remove variance unrelated to the treatment, and on Bing it cut variance by about half, halving the traffic or time an experiment needs. Every major platform now offers it, and Encore's applies it by default where a fan has history.

The analysis plan is the part most often written afterward and most in need of being written before. Fisher's null hypothesis, that the panel makes no difference, can be disproved by the data but never proved, and the plan says in advance what disproving it will look like: which test, which metric, which threshold, which duration, and what decision follows from each outcome. Once results are visible, there are many reasonable-looking analyses to choose from, and the one we choose tends to be the one we hoped for. Here is the Resale team's pre-registration, as it sits in the experiment's record:

```yaml
experiment: resale-soldout-listings-v1
hypothesis: Verified listings on a sold-out page reduce the no-next-step rate
unit: fan (account id; device id if signed out)
trigger: fan reaches sold-out page of an event with resale open
variants: {control: current sold-out page, treatment: verified listings panel}
oec: no_next_step_rate          # lower is better
guardrails: [checkout_slo, resale_support_contacts, bot_fraud_rate, page_latency_p75]
trust_checks: {srm: "chi-squared, halt if p < 0.001", aa_preperiod: true}
design: {alpha: 0.05, power: 0.8, mde: 1 point absolute, variance_reduction: cuped}
duration: 14 days fixed; no decision before day 14
decision: ship if OEC improves and no guardrail degrades beyond its threshold
interference_note: display only; listing sell-out by arm monitored daily
```

#### Trusting the result {#c4-trust}

A surprising result deserves suspicion before celebration. Kohavi and his co-authors call this **Twyman's law**, after the British audience researcher Tony Twyman: "Any figure that looks interesting or different is usually wrong." The law is a statement about base rates. Because most changes have small effects, a large one is more likely to come from an error in logging, assignment or analysis than from a breakthrough, and the right first response to a large effect is to look for the error.

Two checks do most of the work. The first is the **A/A test**, an experiment in which both arms receive the same experience. At a 5% threshold it should show a significant difference about 5% of the time, and a platform whose A/A tests do so more often has something wrong with its assignment or its statistics. Encore runs A/A tests continuously on a slice of traffic and over each new experiment's pre-period. The second is the **sample ratio mismatch (SRM)** check, a test of whether the number of units in each arm matches the designed split. If an experiment designed as 50/50 records 50.8% in one arm across a million units, chance is a very unlikely explanation: something, a redirect, a crash, a logging difference, a consent banner, has removed users from one arm selectively, and no statistics afterward can repair the comparison. Fabijan's study found SRMs in about 6% of Microsoft's experiments, and observed that "a product running ten thousand experiments in a year can expect to see at least one SRM per day". On Encore's scorecards an SRM hides the results until someone has explained it.

Twyman's law is a check, and it can be passed. Within hours of starting, the ad-title experiment at Bing was producing such abnormally high revenue that it triggered a "too good to be true" alert. Such alerts usually signal a bug, Kohavi and Thomke wrote, but not in this case: the analysis that followed showed the gain was real, and that it came without hurting key user-experience metrics. The law did its job by forcing the second look, and the result survived it.

#### Novelty, peeking and the long run {#c4-peeking}

Three habits undermine well-designed experiments. The first is *peeking*: watching the p-value every day and stopping as soon as it falls below 0.05. Each look is another chance for noise to cross the line, so a team that looks daily and stops at the first crossing declares far more false winners than its 5% threshold promises. The proven remedies are of two kinds. One is a fixed horizon, as in Encore's pre-registration. The other is a sequential method built for repeated looks, such as the group sequential tests that Spotify's engineers compared and recommended in 2023 where the maximum sample size can be estimated, or the always-valid inference of Ramesh Johari and colleagues. Each family is sound when its conditions hold.

The second habit is mistaking novelty for improvement. Users react to change itself: a new panel attracts clicks because it is new, and the effect fades as it becomes familiar. The opposite also happens, when experienced users resist a change they will come to prefer. Plotting the treatment effect day by day shows both: an effect that shrinks steadily is novelty, and one that grows may be learning.

The third is forgetting the long run. Henning Hohnhold, Deirdre O'Brien and Diane Tang reported at KDD 2015 how Google measured the long-term effects of the ads on its search pages. Short experiments suggested that fewer ads would cost revenue, but long-running holdouts showed that users learn, growing blind to ads when shown many, so that the effect of a change in ad load keeps developing for months. Google applied the method to a 50% reduction in ad load on mobile search, a change a short test would have rejected. Encore's lesson is to keep a small, long-lived **holdout**, a group deliberately kept without a change for months. For Verified Resale it is nine French organizers whose events go without resale for the first six months after launch. Because that affects their fans, the organizers are told what the holdout is for, consent to it, and may leave at any time.

#### What Encore will not test {#c4-ethics}

Experiments are done to people, and people have interests the experimenter does not share. *Trustworthy Online Controlled Experiments* takes its ethics from *The Belmont Report* (1979), written for research on human subjects in the United States after the abuses of the Tuskegee syphilis study had come to light. The report asks for respect for persons, beneficence and justice: people should be treated as able to decide for themselves, the risks they bear should be weighed against the benefits, and the burdens and benefits of research should be fairly shared. Most product experiments raise none of these questions, because both arms are reasonable experiences and the risk to anyone is small.

The case that taught the industry otherwise was published in 2014. Adam Kramer, Jamie Guillory and Jeffrey Hancock reported in the *Proceedings of the National Academy of Sciences* an experiment in which, for one week, Facebook reduced the positive or the negative posts in the News Feeds of 689,003 users, to see whether their own posts shifted in the same direction. The journal later published an Editorial Expression of Concern about the study's consent. What made it a lesson was its subject. The treatment aimed to change people's emotional state, without their knowledge, and nothing in a terms-of-service agreement amounts to consent to that.

Encore's rules are stricter than the law requires, because selling scarce seats makes some experiments unfair by their nature. Encore never experiments on the price a fan pays, or on which fan gets a seat. Packaging and presentation may be tested, as Section 5.5 sets out: how the all-in price is explained, which listings appear first. In every such test each fan pays exactly what any other fan would pay for the same ticket, and a fee changes only by a deliberate, announced decision that applies to everyone. The cautionary history behind the first rule, Amazon's price test of 2000, has its home in Chapter 5, and the rules agree with Section 3.2's rule for demand tests: a fake door must never take money or hold a seat.

**Recap.** Most ideas fail to move the metrics they target, and some good ones are buried by intuition, so testing pays in both directions. An experiment is designed in writing before it runs: hypothesis, unit, trigger, OEC and guardrails, sample size and analysis plan, and the arithmetic of sample size makes precision expensive. Twyman's law, A/A tests and the sample ratio check protect against errors that look like discoveries, fixed horizons or sequential methods protect against peeking, and holdouts see what short tests cannot. Some experiments are not ours to run.

**Exercise 4.3.** For one change your team shipped last quarter, compute the sample needed per arm to detect a 2% relative change in its main metric at your traffic, using 16σ²/δ². Was an experiment ever possible? If it was, write the pre-registration you should have written; if it was not, say what you would have had to change, such as the trigger, the metric or the variance, to make it possible.

### 4.4 An Experimentation Platform for 40 Teams

#### Assignment as the substrate {#c4-assignment}

An experiment at a large company is one of hundreds running at once, and what makes that possible is the machinery of assignment. Each fan must land in an arm deterministically, seeing the same variant on every visit and device, without the platform storing a lookup for each fan. The standard technique is to hash the unit's identifier with an experiment-specific salt into buckets; Fabijan and colleagues describe Microsoft's ExP platform hashing users into 1,000 buckets of 0.1% each. Hashing is the modern form of what Fisher called "the physical act of randomisation": nothing about the fan, and nothing about the experimenter's hopes, influences which arm the fan lands in.

Encore's assignment runs through the same flag system the Resilience book describes for progressive delivery (its Section 4.3). A release flag and an experiment flag are evaluated by the same SDK, against the same targeting rules, and they differ in purpose and in lifetime. A release flag exists to roll a change out safely and is removed once the rollout ends; an experiment flag exists to answer a question and, in the Resilience book's words, "should live as long as its experiment". The Software book (Section 4.5) covers how flags are handled in development; what this section adds is the assignment discipline that turns a flag into an experiment.

That discipline has three parts. The first is the **unit of randomization**, the entity whose identifier is hashed: a fan, a device, an event or an organizer. It must be at least as large as what a variant can affect, or one fan may see both arms and contaminate both. The second is **layering**: running many experiments on the same fans at once, each with its own independent hash. Fisher argued for the same efficiency in 1926, against the advice of his day: "No aphorism is more frequently repeated in connection with field trials, than that we must ask Nature few questions, or, ideally, one question, at a time. The writer is convinced that this view is wholly mistaken." Layering works because independent randomization spreads each experiment's effect evenly across the arms of every other; where two experiments change the same screen in conflicting ways, the platform puts them in one exclusive layer. The third part is **exposure logging**, recording on the client the moment a fan actually met the variant, so that the analysis counts the fans who were exposed and not merely those assigned. Section 8.4 shows how this is done on phones.

#### Metrics defined once {#c4-metrics-once}

The commonest failure of experimentation at scale has nothing to do with statistics. It is that every team computes its own version of the same metric. One team's "conversion" divides orders by sessions, another's by visitors, and a third's excludes fans who arrived from a partner. Each is defensible on its own. Together they make the experiments of different teams impossible to compare, and they turn every leadership meeting into a debate about whose number is right.

The history of measurement offers a parallel. Before the metric system, neighboring French towns might use different feet, and a merchant trading between them could be cheated by either. Revolutionary France defined the metre in the 1790s so that one length would mean the same everywhere, kept by a central authority with a physical standard. A metric definition kept in one place does the same work across teams. The analogy breaks because a metre was meant never to change, whereas a metric definition must sometimes change with the product, and so it needs versions, owners and a record of why each version replaced the last.

Airbnb's Minerva platform is the best-documented case of a company solving this. It grew out of the metric repository behind Airbnb's experiments, on the principle of "define once, use everywhere": a metric is defined in one place, in code, and every experiment scorecard, dashboard and report computes it from that definition. Encore's version is a metric catalog owned by the Experimentation team, in which each metric is a reviewed definition:

```yaml
metric: resale_conversion
owner: Resale team; reviewed by Experimentation
definition: listings sold before window close ÷ listings created
numerator:   count(resale_order_completed) by listing_id, dedup
denominator: count(resale_listing_created) where window_closed
unit_of_analysis: listing; aggregated to the experiment's unit
direction: higher is better
used_as: [input metric, OEC for resale-flow experiments]
version: 2   # v1 counted orders, including those later reversed
```

Every experiment's scorecard then shows three things together: the OEC with its confidence interval, the guardrails with theirs, and the trust checks, the sample ratio test and the A/A pre-period. Putting them on one page is a design choice with a purpose. A team reading only the OEC will ship a win that broke a guardrail, and a team that never sees the trust checks will trust a result that should have been discarded.

#### Crawl, walk, run, fly {#c4-maturity}

Organizations do not adopt experimentation all at once. The clearest description of how they grow is by Aleksander Fabijan, Pavel Dmitriev, Helena Holmström Olsson and Jan Bosch (ICSE 2017), who drew on case studies centered on Microsoft and named four phases: crawl, walk, run and fly. Early on, specialists set up and analyze a few experiments by hand; in the middle, a platform, standard metrics and trust checks appear and more teams test; later, experimentation becomes the default way to ship a change, an OEC is agreed, and the organization learns from its accumulated results. The model is descriptive: it shows what growth looked like in the companies studied, and promises nothing about following it elsewhere.

By its own judgment Encore is at walk. Last year it ran about 310 experiments, two-thirds of them from seven of its 40 teams; the rest of the company tests rarely or never. The platform, the metric catalog and the trust checks exist. What Encore lacks for the next phase is an agreed OEC for each main product, the habit of testing ordinary changes as well as headline features, and the institutional memory described next. Those are matters of practice and agreement more than of software, which is why moving from walk to run is usually slower than building the platform was.

#### Memory and review {#c4-memory}

An experiment's result is worth more than the decision it informs, because it tells the next team something about how fans behave. Most companies throw that value away: the results live in a slide deck, and two years later another team pays for the same lesson. Raphael Lopez Kaufman, Jegar Pitchforth and Lukas Vermeer described in 2017 how Booking.com spread experimentation across its teams, naming among the ingredients a shared archive of past results, a reusable code library, monitoring of data pipelines, and safeguards that let individuals own their experiments end to end. Kohavi, Tang and Xu give a chapter to the same idea, institutional memory and meta-analysis across many experiments.

Encore's archive is the experiment record itself: the pre-registration, the scorecard and a short written conclusion, kept together and searchable by product area, metric and screen. Before an experiment starts, a reviewer from another team reads its pre-registration and asks whether the OEC, the unit and the trigger fit the hypothesis. The archive's most valuable entries are its failures, recorded with their reasoning, and they are also the entries most likely to be lost, since nobody presents a failure at the quarterly review.

#### Build, buy or rent {#c4-build-or-rent}

Experimentation platforms are now products a company can buy, and the decision is the kind the Architecture book's Section 13.1 maps, with its four options (build, adopt, buy or rent) and its key term, *dependence*: how much of our ability to act we place in someone else's hands. Encore builds assignment, the metric catalog and the integration with its tracking plan, because those are tied to its own data contracts, consent rules and flag system. It rents the statistics engine, which computes intervals, variance reduction and sequential tests, because that part is the same for every company and specialists maintain it better than a team of Encore's size could.

The dependence is real, and recent history shows how quickly it can change. In May 2025 Datadog announced that it had acquired Eppo, one of the leading independent experimentation vendors, and in September 2025 OpenAI acquired Statsig, another; within four months, both had new owners with priorities of their own. Open-source platforms such as GrowthBook offer a different form of dependence. Encore's split is a judgment, not a finding, and its main defense is that the rented part is replaceable: the statistics engine reads Encore's assignments and metric definitions, and a different engine could read them too.

**Recap.** Deterministic hashing makes assignment reproducible and impartial, and layering lets many experiments share the same fans, as Fisher's factorial designs once shared the same field. Metrics defined once, in code, keep 40 teams' numbers comparable, and the scorecard shows the OEC, the guardrails and the trust checks together. Maturity grows from a few experiments to a default practice, and what holds most organizations back is agreement and memory more than software. Build what is tied to your own contracts and rent what is generic, keeping the rented part replaceable.

**Exercise 4.4.** Find where your organization's experiment results live today. Ask a colleague on another team to find last year's least successful experiment in your area, with its hypothesis and result, and time how long it takes. If they cannot find it, write down what an archive entry would have needed to contain.

### 4.5 When You Cannot A/B Test

#### When the plots touch {#c4-interference}

Fisher's method rested on an assumption so natural in a wheat field that he hardly needed to state it: the fertilizer on one plot does not change the yield of the next. Statisticians later gave the assumption a name. The **stable unit treatment value assumption (SUTVA)** says that each unit's outcome depends only on its own treatment, never on the treatments of other units. Online experiments inherit it, and for most of them it holds well enough: whether one fan sees a new search box has no effect on what another fan finds.

Marketplaces break it. Thomas Blake and Dominic Coey showed at ACM EC 2014 how an eBay email-marketing experiment went wrong for this reason. Treated and control bidders competed in the same auctions, so when the treatment made some bidders more active, they won items that control bidders would otherwise have won. The treatment group looked better partly because the control group had been made worse, and the naive comparison overstated the effect. Kohavi, Tang and Xu give the problem its own chapter, on leakage and interference between variants.

At Encore the interference is literal. A resold seat goes to exactly one fan. If an experiment made resale more attractive to fans in the treatment arm, they would buy listings that control fans would otherwise have bought; the treatment would show more completed resales, the control fewer, and the difference would be mostly a transfer between arms, not an effect of the product. The same applies to sellers, who list into one pool that both arms buy from, and to organizers, whose rules govern every fan of their events. A user-level A/B test of Verified Resale itself would measure something real, but not the thing the memo needs to know: whether resale, available to everyone, makes the market better. The question is how to choose units large enough to contain the interference.

#### Randomizing clusters {#c4-cluster}

The standard answer is **cluster randomization**: randomizing groups of units that interact, so that the interference stays inside each group. The best marketplace evidence for it comes from Airbnb. David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich and Sinan Aral ran a meta-experiment around a *fee increase*, published in *Management Science* in 2025, in which the same change was evaluated both by randomizing individual listings and by randomizing clusters of listings that compete for the same guests. At least 20% of the effect the individual-level design estimated was interference bias, which the cluster design removed, and there was suggestive, though not significant, evidence that the bias was larger where demand was constrained. The case could hardly be closer to Verified Resale: a fee, in a marketplace, with the bias measured.

The price of clusters is statistical power. An experiment's precision depends on the number of independent units, and an experiment with 500 clusters has the precision of something nearer 500 units than of the millions of fans inside them. Clusters must also actually contain the interference. For seats, the event is a natural cluster, because fans buying resale for one concert do not compete with fans buying for another. But fans browse several events, and a fan who finds no listing for one concert may buy for another, so interference leaks across clusters at their edges, and the design reduces the bias without removing it.

Encore's cluster experiment uses events as units, and it asks a narrow question: how the resale fee should be shown. One version shows the all-in price as a single figure; the other shows the same all-in price with the fee and its split among partner, organizer and Encore itemized beneath it. The total is identical in both, so no fan pays a different price from any other, as Section 4.3's rule requires. When the launch widens to all consenting French organizers, 38 of them agree to let about 520 of their events be randomized between the two presentations, so that every fan of a given event sees one presentation and fans comparing notes about one concert see the same thing. The outcomes are completed purchases and the Support contacts that ask where the money went. With 520 clusters the experiment can detect only large effects, and the pre-registration says so.

#### Switchbacks and geography {#c4-switchback-geo}

When interference runs through a whole market, two other designs become useful. A **switchback** experiment applies the treatment to an entire market for a window of time, then switches it off and on again in a randomized sequence of windows, and compares the windows. DoorDash described the method in 2018 for changes to how deliveries are assigned to couriers: every order in a region during a window receives the same policy, so treated and control orders never compete for the same couriers, and the analysis is at the level of region and window. It works only when the treatment's effect dies out well within one window, so that windows do not carry over into each other, and when there are many windows, because each window is one observation.

Those conditions decide where Encore can use switchbacks, and for Verified Resale the answer is nowhere yet. A one-off on-sale defeats them, because its whole effect falls within one window. The resale market looks more promising at first, since it runs continuously across thousands of events, and the Resale trio first proposed a switchback for the fee presentation, alternating it across the whole French market by the hour. They rejected it for two reasons. A fan who returned an hour later could find the same fee presented differently, which sits badly with Encore's rule on price integrity and with the EU's requirement that totals be shown clearly. And a resale listing persists from one window into the next, so what one hour's presentation did to the pool of unsold listings would carry into the following hour. Iavor Bojinov, David Simchi-Levi and Jinglong Zhao, who set out the theory of switchback designs in *Management Science* in 2023, show that such carryover must die out quickly relative to the window for the design to be valid. Neither condition held, which is why the fee presentation sits in the cluster design above. A delivery order is consumed within its window and a resale listing is not, and the analogy with DoorDash breaks exactly there.

**Geo experiments** randomize geographic regions instead of time. Jon Vaver and Jim Koehler described the method at Google in 2011 for measuring advertising: non-overlapping regions are randomly assigned to treatment or control. It needs many regions, and that is where it fails Encore. Encore sells in too few EU countries for a randomized design among them to have any power, and they differ too much in size and tour calendars to be exchangeable. Cities offer more units, but fans travel to concerts, and a resale in Lyon may be bought by a fan from Grenoble. Encore therefore runs no geo experiment on Verified Resale, and its evaluation plan says so, so that nobody later mistakes the market-level comparison below for one.

#### Quasi-experiments {#c4-quasi}

When the rollout itself was not randomized, as Encore's is not, a **quasi-experiment** estimates the effect by constructing a comparison the data did not supply. *Difference-in-differences* compares the change over time in the treated group with the change in an untreated group, so that anything affecting both, such as the season, cancels out. Its best-known use is David Card and Alan Krueger's 1994 study of a minimum-wage rise in New Jersey, compared with fast-food restaurants in neighboring Pennsylvania. The method depends on the two groups having moved in parallel before the treatment, and nothing in the data can prove they would have kept doing so.

*Synthetic control* builds the comparison more carefully. Alberto Abadie, Alexis Diamond and Jens Hainmueller introduced it in 2010 in a study of California's tobacco-control program of 1988. No single state resembled California well enough, so they built a weighted combination of other states that matched California's cigarette sales and their drivers before the program. Afterward the paths diverged, and by 2000 per-capita sales in California were about 26 packs lower than in its synthetic counterpart. Abadie's guide of 2021 sets out when the method fails: it needs a long pre-period, a donor pool the treatment did not reach, and no anticipation, in which people change their behavior because they expect the treatment.

Encore launches Verified Resale in France first, for business reasons: its design partners and its contract season. A market chosen for reasons cannot also be chosen at random, so Encore judges the market-level effect with a synthetic control instead, built from nine EU markets where it sells but has not launched resale. The question is the one the memo's guardrail asks, whether resale eats the primary sale, and the outcome is primary sell-through per eligible event, week by week, over a pre-period of 104 weeks. The memo's second kill criterion, K2, is written in the same terms: at month 18 the bet stops if primary sell-through in France has fallen more than 2 points below its synthetic counterpart (Section 10.1). Each of Abadie's conditions must be argued. Two years of weekly history give a long pre-period, and nine donors give a pool. Spillover cannot be taken for granted, because fans cross borders for tours, and resale in France could change what Belgian fans do, so Belgium is removed from the donor pool before the analysis begins. And the launch was announced in advance, so some French fans may have changed their buying in anticipation, which the plan names as a threat it cannot remove.

The fraud the memo's diagnosis described is harder to measure, because the grey market happens on sites and in messages Encore never sees. The closest measurement Encore owns is at its own doors: the rate of duplicate-ticket rejections at the gate per 10,000 scans, which Venue Entry has recorded everywhere for years. Encore reads a fall in that rate on resale-enabled events as supporting evidence, and claims nothing it cannot measure about displacement of the grey market.

The rollout across countries brings one more caution, which the plan for Verified Resale originally lacked. When a change reaches different countries in different months, the usual regression for difference-in-differences, with fixed effects for country and period, can produce biased and even wrongly signed estimates, because it implicitly uses already-treated countries as controls for later ones. Andrew Goodman-Bacon, and Brantly Callaway and Pedro Sant'Anna, showed this in 2021 and offered estimators that avoid it. Encore will use one of those estimators as the launch widens beyond France, and it will record the choice in the evaluation plan before the second country goes live.

#### Deciding without certainty {#c4-deciding}

None of these designs gives the certainty of a clean randomized test, and the temptation is to pretend that one of them does. The honest alternative is to combine several imperfect methods, each strong where another is weak, and to decide against criteria written before any of them reports; *Trustworthy Online Controlled Experiments* devotes chapters to the complementary and observational methods that support this. Fisher's standard from 1926 still applies: "A scientific fact should be regarded as experimentally established only if a properly designed experiment rarely fails to give this level of significance." His emphasis was on replication, and a result that keeps appearing across different designs deserves more trust than any single one. Figure 4.3 shows how Encore's evaluation plan for Verified Resale assigns each question to a design.

| Question | Design | Unit | What it can show | Main threat |
|---|---|---|---|---|
| Does the sold-out panel keep fans engaged? | A/B test | Fan | Effect of display on the no-next-step rate | Small leakage through shared listings |
| How should the fee be shown? | Cluster randomization | Event | Effect of itemizing the split on purchases and Support contacts | Low power; only large effects visible |
| Does Verified Resale eat primary sales? | Synthetic control | Market-week | Change in primary sell-through in France (the K2 guardrail) | Spillover into donors; anticipation |
| Does it cut fraud at the door? | Before-and-after reading | Event | Fall in duplicate rejections on resale-enabled events | Supporting evidence only; grey market unseen |
| What does resale do over months? | Consenting holdout | Organizer | Long-run difference for nine organizers' events | Few units; organizers may leave |
| Do organizers and fans trust it? | Interviews (Chapter 3) | Person | Reasons behind the numbers | Small, self-selected samples |

*Figure 4.3 — Encore's evaluation plan for Verified Resale. Each question gets the strongest design its interference allows, and the plan names each design's main threat before any result arrives.*

Two rules make the plan honest. The first is that its decision criteria, the thresholds for each metric and what follows from each outcome, are written before launch, in the pivot-or-persevere discipline of Section 3.2 and beside the memo's kill criteria (Section 10.1). The second is that the decision record, in the form of the Architecture book's decision records (Section 1.4), states the residual uncertainty plainly: which conclusions rest on randomized evidence, which on quasi-experiments, and which on judgment. A combined judgment is weaker evidence than a randomized test, and the people who revisit the decision a year later need to know how much weight it can bear. I have come to think that the most dangerous moment in measuring a product is the one in which a quasi-experiment is reported as if it were an A/B test, because from then on everyone who reads it believes something more certain than anyone ever knew. Chapter 10 shows the plan in use when Verified Resale launched (Section 10.4).

**Recap.** When units compete for the same seats, the stable-unit assumption fails, and a user-level test measures transfers between arms more than effects. Clusters contain interference at a cost in power, as Airbnb's fee experiment measured; switchbacks need effects that die out within a window, which persistent resale listings do not, and geo experiments need more regions than Encore has countries. Quasi-experiments estimate effects from rollouts that were not randomized, under conditions that must be argued, and a decision built from several designs must record how uncertain it remains.

**Exercise 4.5.** Name one decision in your product where interference would bias an A/B test: who competes with whom, and for what? Choose the unit or design that would contain it, estimate how many independent units that leaves you, and write one sentence saying what the design cannot show.

### Kata: Two Baskets, One Courier

> **Your brief: "Pantry."** Pantry is a grocery-delivery marketplace with 150 engineers in 22 cities across four countries. Customers order from about 1,800 partner stores, and about 9,000 independent couriers deliver within an hour; at six in the evening in any one city, every courier on shift serves the same pool of orders. Operations wants to launch *batching*, in which one courier collects two orders from nearby stores and delivers both on one trip. A two-week pilot in one city reported 9% more orders delivered per courier-hour, and the product director wants it everywhere next month. But complaints about late deliveries rose 14% in the pilot city that fortnight, couriers' forums say batched trips pay less per hour, and nobody can say whether batching or the weather caused either change. An analyst has proposed an A/B test randomized by customer. The head of data has asked you to design the evaluation before anything ships, in the spirit of DoorDash's switchbacks, without copying them.

**Deliverables:**

1. **The metrics** — Write an OEC for the batching decision, and guardrails for all three sides: customers (delivery time against promise, late-order rate), couriers (earnings per hour on shift, including waiting time) and stores (order hand-off wait). Say which guardrail you would defend first if the OEC improved while it fell, and who should agree to that ordering.
2. **The interference map** — Explain in a paragraph why randomizing by customer would bias the result: who competes with whom, and for what. Then name the smallest unit that contains the interference.
3. **The design** — Specify a switchback: the market unit, the window length and why it exceeds the carryover (a courier mid-batch at a window's end), the number of windows, and how windows are randomized. Say what the design cannot show, and how a long-term holdout or a later city-level comparison would cover it.
4. **The sample** — Estimate how many windows are needed to detect a 3% change in the OEC, stating the variance you assumed and where it came from. Say whether variance reduction could shorten the experiment.
5. **The pre-registration** — Write the experiment's pre-registration in the form of Section 4.3: hypothesis, unit, trigger, OEC, guardrails, trust checks, duration and decision rule.
6. **The decision record** — Write the half-page record you would want the product director to sign before rollout: the criteria, the designs combined, and the uncertainty that remains.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Interference | Does your design keep treated and control orders from competing for the same couriers? |
| Both sides guarded | Would your guardrails catch a batching rule that makes customers wait or makes couriers earn less, even if throughput rises? |
| Carryover | Is every window long enough that a batch started in one cannot finish in the next? |
| Honest power | Does your sample estimate rest on a stated variance, and does it treat windows as the units of analysis? |
| Written in advance | Could the decision rule be applied by someone who did not design the experiment? |
| Residual doubt | Does the decision record say plainly what the evidence cannot show? |

#### Where you now stand

You can now choose a metric that changes behavior, name the moment at which value is delivered, and set guardrails beside it. You can treat tracking events as contracts, design an experiment in writing before it runs, compute what it needs, and recognize the errors that look like discoveries. And you can tell when a clean experiment is impossible, choose a design whose unit contains the interference, and record how certain the result really is. Every metric in this chapter took one thing for granted: the price was settled, and Encore measured what happened at it. For Verified Resale the price is part of the product. The fee, its split among partner, organizer and Encore, and the cap that protects fans decide whether three sides will join the market at all. Chapter 5 takes up pricing, and with it the kind of experiment this chapter has ruled out.

### References

- Ron Kohavi, Diane Tang, Ya Xu — [*Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*](https://doi.org/10.1017/9781108653985). Cambridge University Press, 2020.
- Ronald A. Fisher — [*The Design of Experiments*](https://archive.org/details/in.ernet.dli.2015.502684). Oliver and Boyd, 1935 — free online.
- Ronald A. Fisher — [*The Arrangement of Field Experiments*](https://doi.org/10.23637/rothamsted.8v61q). *Journal of the Ministry of Agriculture* 33, 1926 — free online.
- Alistair Croll, Benjamin Yoskovitz — [*Lean Analytics*](https://www.oreilly.com/library/view/lean-analytics/9781449335687/). O'Reilly, 2013.
- Ron Kohavi, Stefan Thomke — [*The Surprising Power of Online Experiments*](https://hbr.org/2017/09/the-surprising-power-of-online-experiments). *Harvard Business Review*, September–October 2017.
- David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich, Sinan Aral — [*Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb*](https://arxiv.org/abs/2004.12489). *Management Science* 71(1), 2025 — free online.
- Aleksander Fabijan, Jayant Gupchup, Somit Gupta, Jeff Omhover, Wen Qin, Lukas Vermeer, Pavel Dmitriev — [*Diagnosing Sample Ratio Mismatch in Online Controlled Experiments*](https://doi.org/10.1145/3292500.3330722). KDD, 2019.
- Ron Kohavi, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, Ya Xu — [*Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained*](https://doi.org/10.1145/2339530.2339653). KDD, 2012.
- Aleksander Fabijan, Pavel Dmitriev, Helena Holmström Olsson, Jan Bosch — [*The Evolution of Continuous Experimentation in Software Product Development*](https://doi.org/10.1109/ICSE.2017.76). ICSE, 2017.
- Alberto Abadie, Alexis Diamond, Jens Hainmueller — [*Synthetic Control Methods for Comparative Case Studies*](https://doi.org/10.1198/jasa.2009.ap08746). *Journal of the American Statistical Association* 105(490), 2010.
- Alberto Abadie — [*Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects*](https://www.aeaweb.org/articles?id=10.1257/jel.20191450). *Journal of Economic Literature* 59(2), 2021.
- Henning Hohnhold, Deirdre O'Brien, Diane Tang — [*Focusing on the Long-term: It's Good for Users and Business*](https://research.google/pubs/pub43887/). KDD, 2015 — free online.
- Ramesh Johari, Pete Koomen, Leonid Pekelis, David Walsh — [*Always Valid Inference: Continuous Monitoring of A/B Tests*](https://arxiv.org/abs/1512.04922). *Operations Research*, 2022 — free online.
- Jon Vaver, Jim Koehler — [*Measuring Ad Effectiveness Using Geo Experiments*](https://research.google/pubs/pub38355/). Google, 2011 — free online.
- David Kastelman, Raghav Ramesh — [*Switchback Tests and Randomized Experimentation Under Network Effects at DoorDash*](https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/). DoorDash Engineering, 2018 — free online.
- Kerry Rodden, Hilary Hutchinson, Xin Fu — [*Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications*](https://research.google/pubs/pub36299/). CHI, 2010 — free online.

---

## Chapter 5: Pricing, Packaging, and Monetization {#ch5}

> A price is the one line of a product that every customer reads.

Most teams decide what a product costs at the end, when the thing is built and someone in finance asks what to put on the invoice. By then the important choices have been made, quietly, by people who were not thinking about price at all: which features went into the first release, which customers it was shaped for, which events the system records and which it throws away. This chapter argues for the opposite order. What a product will cost, how it is cut into packages, how its use is counted and billed, and how its price may later change are product decisions in their own right, and they belong at the start, beside the questions of value and usability that Chapter 1 gathered under the four risks. Viability is settled as much by the price as by the product.

The case that has taught the industry most about getting this wrong is small, and it is now 26 years old. In September 2000 Amazon ran a five-day test on 68 DVD titles, in which the discount a customer saw on each title was set at random between 20% and 40%. Customers who talked about DVDs on an online fan forum compared notes and found that the same disc carried different prices for different people at the same moment; Computerworld reported one title at $25.97 in one browser and $23.97 in another. Amazon's first explanation, that it routinely tested aspects of the site "such as the navigation system, overall site design and product pricing", satisfied nobody, because a suspicion had already formed that loyal customers were paying more than new ones. Within days the company promised refunds. On 27 September it issued a statement that called the test a mistake that had "created uncertainty and complexity for our customers". It said it had refunded 6,896 customers an average of $3.10 each, and it made a promise about any future test: every buyer would automatically receive the lowest test price for that item. Jeff Bezos denied that demographics had played any part ("We've never tested and we never will test prices based on customer demographics"), and then went further than a denial: "What we did was a random price test, and even that was a mistake because it created uncertainty for customers rather than simplifying their lives."

The money was trivial, a little over $21,000 by the arithmetic of Amazon's own figures. The lesson has lasted, and it has three parts. A price is visible in a way that a button color is not, because customers compare prices with one another and read a difference as a statement about themselves. A random design, which an experimenter rightly regards as the fairest way to assign a treatment, is no defense against the charge of unfairness, since the customer who paid more does not care how the coin was tossed. And the remedy Amazon chose, that everyone in a test pays the lowest price tested, is a rule worth copying, because it turns a price test into a discount test. Andrew Odlyzko discussed the episode in his 2003 paper on privacy, economics and price discrimination on the internet, and it remains the standard example in that literature of how strongly buyers resent being charged differently for the same thing.

Encore meets these questions with Verified Resale, a bet to replace the old Partner Listings links with resale that Encore can vouch for: fans list tickets they bought through the Sale Gate, authorized partners such as Rowmate show those listings to buyers, a screened fan buys, and Encore reissues the ticket under a new barcode. The bet stands or falls on prices that three parties must accept at once. Fans must find the fee worth the certainty. Organizers must see enough control, and enough of the money, to switch resale on. Partners must earn enough to send their buyers. In the months of discovery that Chapter 3 followed, the product trio has to settle the fee, the organizer's share and the cap, decide which of Encore's tiers get resale, design the metering that pays organizers their share, and do all of it without ever running the kind of test Amazon apologized for. The chapter takes that work in order, from price before product in Section 5.1 to changing a price in public in Section 5.5.

### 5.1 Price Before Product

#### The willingness-to-pay conversation {#c5-wtp-conversation}

Madhavan Ramanujam and Georg Tacke, both of the pricing consultancy Simon-Kucher, put the argument of this section into the subtitle of their 2016 book *Monetizing Innovation*: how smart companies design the product around the price. The book distills a long consulting practice into a simple claim. Most new products fail commercially for reasons that were knowable before anything was built, and the cheapest way to learn them is to talk about price early, while the product is still a concept and every answer can still change its scope. The central instrument is a conversation. A customer's **willingness to pay (WTP)** is the highest price at which they would still choose a defined offer over going without it, and the willingness-to-pay conversation is the structured interview that estimates it for a segment before the offer exists.

The order of that conversation matters more than its questions. Ramanujam and Tacke run it from the problem, to the solution, to the value, and only then to the price. A physician taking a history works the same way: first the symptoms, then how they affect the patient's life, then what the patient has already tried, and only after all that a treatment. Asking about price first is like prescribing before the patient has finished describing the pain. The customer anchors on a number before either side knows what the number is for, and everything said afterwards bends toward defending it. Here the analogy breaks, and the break is the most important thing to know about the method. A patient has every reason to describe the pain honestly. A customer asked about price has a reason to understate it, and even an honest customer is a poor witness to their own future behavior. Jonas Schmidt and Tammo Bijmolt's meta-analysis of 77 studies, published in 2020, found that stated willingness to pay exceeded real willingness to pay by 21% on average, and by more for expensive and specialized goods.

So the answers from a willingness-to-pay conversation are inputs to scope, recorded as ranges, compared across segments and replaced by behavior whenever behavior can be had: a price charged in a pilot, a letter of intent, an organizer's signature on a term sheet. The conversation earns its place because it changes what gets built, and the arguments about what to leave out happen before the code exists.

Encore added the price questions to the discovery interviews that Chapter 3 described, with its design-partner organizers and with Rowmate. The organizers were asked first what resale cost them today, in duplicated barcodes turned away at the door and angry fans in their inboxes, then what verified resale would be worth, and only then about money. Most named a share of between 2% and 5% of each resale price as fair, none would pay a fee to have resale switched on, and several said they would switch it on only if they could close it well before doors. Rowmate's people, asked the same sequence, named three to five points of the resale price as an acceptable commission on capped, verified listings, because verified listings remove the refunds and chargebacks that duplicated barcodes cost them. Fans were not asked at all. The Wizard of Oz pilot of Section 3.2 gave something better than their opinions: at its four shows in Lyon and Antwerp, every resale buyer paid the same 10% fee, shown in the all-in price, and the trio watched what they did. Four shows and about 11,200 tickets could not measure demand, which the pilot read only qualitatively, but they could show whether buyers balked at the fee once the price was real.

Those conversations changed the product. The organizers' insistence on closing resale before doors became the default resale window, which runs from purchase until two hours before doors. A request from two promoters for a cap above face value was refused in the first month, because the cap is a platform rule that organizers may only tighten, and Section 5.5 shows the law moving the same way, so that nobody designed a console around a control that would never ship. Detailed resale analytics fell down the list when not one organizer said it was worth anything to them.

#### Four ways to fail {#c5-four-failures}

Ramanujam and Tacke name four ways in which new products fail to make money. **Feature shock** is a product with too many features, priced too high and too hard to explain. A **minivation** is the right product priced too low, so that it sells well and earns far less than it could. A **hidden gem** is a potential success that is never brought to market, usually because it sits outside what the company thinks of as its core. And the **undead** are products that nobody wants, kept alive because nobody is willing to say so. The taxonomy comes from consulting experience and has no independent research behind it, so it is best used as a lens and a shared vocabulary, which is how Encore uses it. Figure 5.1 maps each failure to something in Encore's own history.

| Failure | What goes wrong | Encore's example |
|---|---|---|
| Feature shock | Too many features, priced high, hard to explain | The organizer analytics pack of year five: 30 reports sold as one bundle at a price most organizers would not pay for the three reports they used |
| Minivation | The right product, priced too low | Presale codes, given away in every tier from year four, although organizers running fan-club presales valued them highly |
| Hidden gem | A likely success never taken to market | The seat-map builder, which two other ticketing companies asked to license and which Encore never offered, because selling software to rivals was nobody's job |
| Undead | A product nobody wants | Event chat rooms in the fan app, kept for two years while usage stayed near zero, then retired |

*Figure 5.1 — Ramanujam and Tacke's four failures, each mapped to an Encore product. All four were knowable before launch from a willingness-to-pay conversation that nobody held.*

The four names are most useful before a bet is funded, as a way to ask which failure it is most exposed to. Verified Resale's largest exposure is to the undead. If fans do not trust a reissued ticket, or organizers will not switch resale on, a well-built product will sit unused while the grey market carries on beside it, and the bet's kill criteria exist to catch exactly that. Its second exposure is feature shock. A rules engine with 40 options, each requested by one organizer in one interview, would be hard to explain, test and sell, so the trio cut the organizer's controls to the few that the fairness invariants allow: switching resale off, setting the window, lowering the cap and lowering the per-fan limits.

#### Segments drawn by need {#c5-segments}

The fifth chapter of *Monetizing Innovation* warns against defaulting to one offer for everyone, and it proposes segmenting customers by their needs and their willingness to pay before segmenting them by size. Size tells a company how much a customer might spend, while needs tell it what the customer will spend it on, and two customers of the same size may want opposite things from the same feature. Encore's tiers already segment organizers by size and by the isolation they require, as Section 5.2 will show. Verified Resale needed a second cut.

The interviews revealed two groups of organizers who wanted different things from resale. **Control-seeking** organizers, many of them festival and tour promoters who had fought touts for years, wanted resale closed until well after the on-sale, low per-fan limits and an early cut-off. **Revenue-seeking** organizers wanted the widest possible resale window and the largest number of resold tickets, because every one of them pays the organizer three points. A conventional segmentation would offer the second group a higher cap in exchange for a larger fee. Encore cannot, because its rules only tighten: the cap is face value at most, the fee split is fixed, and no organizer may loosen a default. So the two segments pay the same price and receive the same economics, and they differ only in configuration. The console therefore offers three starting presets, "Standard", which keeps the defaults, "Fan-first", which tightens the window and the per-fan limits, and "Resale off", and each can be adjusted within the platform's limits; in Ireland, where the law forbids it, "Resale off" is not offered (Section 5.5). Segmentation is usually presented as a way to charge different customers different amounts, and here, with the price fixed by principle, it did its work on the product's defaults instead.

#### The business case from the outside in {#c5-business-case}

Ramanujam and Tacke ask that the business case for a new product be built from the outside in, starting from validated willingness to pay and the sizes of the segments that showed it. A cost-plus case asks what the product will cost and adds a margin, which tells us what we would like to charge and nothing about whether anyone will pay it. A case built from the outside starts from what customers will pay and asks whether the product can be built and run for less.

Encore's case for Verified Resale starts from one resold ticket, because every term of the economics is defined per ticket. Take a ticket with a face value of €60, which in Encore's usage means the original price the seller paid, primary fees included. It resells at face value, the buyer pays a 10% fee on top and the €66 is split as Figure 5.2 shows. Encore's three points, €1.80, must carry the payment provider's charges on a €66 payment, fraud losses and the support each resale needs. Against that, the variable cost of serving one more ticket on Encore's platform is €0.12, the figure the Resilience book derives in its Section 2.5. That is the marginal cost, and the right one for a case about additional tickets; the blended €0.16 includes fixed costs that resale does not change. The Wizard of Oz pilot measured the remaining large term directly: with every reissue done by hand through Support's lost-ticket replacement screen, agents spent a median of 14 minutes on each completed resale, falling from 26 at the first show to nine at the fourth (Figure 3.3). Even nine minutes of an agent's time costs several times what Encore's three points could pay for, and the case therefore rests on an explicit condition: once reissue is automated, support per resale must fall to a fraction of the pilot's figure, or the product loses money on every ticket it sells.

The case reduces the bet's economics to a few things that must become true, each with a number attached and each testable before full launch: organizers switching resale on for enough events, partners bringing enough buyers that listings sell before doors, and support per resale falling far enough. The Software book's Section 8.5 computes the contribution margin per resold ticket once real data exists, and it finds what the pilot already hinted at: the cost of a dispute decides the margin far more than the level of the fee.

#### Saying what the price buys {#c5-communicating-value}

The tenth chapter of *Monetizing Innovation* is titled "The Innovation Won't Speak for Itself", and its argument is that value must be explained in the customer's terms, by the people who sell and by the product itself. For each of Encore's three parties the value is different, and so is the message. Organizers are offered control and a share of the money, and the fee is barely mentioned to them, since they never pay it. The console shows, event by event, how many tickets were resold through Verified Resale and what the organizer's three points have earned, so that the value accumulates where the organizer can see it. Fans are offered a ticket that will scan at the door, at no more than its face value, and the 10% fee is presented as the price of that certainty, inside an all-in price shown from the first screen, beside the Verified badge that the Design System team built and the reissue status that tells both buyer and seller where their ticket stands. Partners are offered inventory they can sell without fearing that it is fake, and a commission on every ticket their buyers take. Each message describes something the product actually does, which is the test a value message must pass.

**Recap.** Price belongs at the start because willingness to pay changes what is worth building, but stated willingness runs well above real willingness, so its answers are ranges that shape scope until behavior replaces them. The four failures are a vocabulary for asking where a bet is exposed, and needs-based segments shape a product's configuration even when the price is fixed. A business case built from the outside in reduces a bet to a few conditions that must become true.

**Exercise 5.1.** Choose one item on your roadmap that has not been built yet. Ask three customers, in the order problem, solution, value and price, what they would pay for it, and record each answer as a range. Then write down how the answers change the item's scope: what you would now leave out, what you would add, and which answer you would most like to replace with observed behavior.

### 5.2 Business Models

#### Five models and the behavior each rewards {#c5-five-models}

A business model, for our purposes, is the rule by which a product turns use into revenue, and every such rule rewards some behavior over others. Ramanujam and Tacke describe five monetization models. In a **subscription**, the customer pays a recurring price for continued access, which rewards the company for keeping customers and makes revenue predictable. In **dynamic pricing**, the price moves with demand, which invites the suspicion that the seller is exploiting demand. In **market-based pricing**, the price is discovered by bidding, as in an auction. In **pay-as-you-go**, the customer pays per unit of use, which ties the company's revenue to the customer's success. And in **freemium**, a basic version is free and a premium version is paid, which rewards converting free users.

Encore uses two of the five. Its software-as-a-service (SaaS) tiers for venues and organizers are subscriptions, and its per-ticket fees are pay-as-you-go. The self-service tier has no subscription at all and pays only through per-ticket fees, which makes it pay-as-you-go as well; it is not freemium, because every ticket sold pays. The three models Encore does not use were declined deliberately. Encore runs no dynamic pricing of its own, for reasons Section 5.5 gives. Resale is not market-based, since bidding under a ceiling of face value would be a queue in disguise. And nothing is given away, because every ticket sold on the platform costs something to serve. A model is a choice of incentives that outlasts the reasons for it: a company that charges per ticket comes to care about volume above everything, one that charges a subscription comes to care about renewal, and Encore, running both, has to keep each revenue line's incentives visible so that one does not quietly distort the other.

#### Per-ticket fees and the all-in price {#c5-per-ticket-fees}

The per-ticket service fee that fans pay on primary sales funds Encore's marketplace. It scales with demand, and it is the part of Encore's pricing that the most people see. In the European Union (EU) it is also regulated, and it is worth being precise about where the rules come from, because they are often misattributed. The duty to show the **all-in price**, the total a consumer will pay including every unavoidable fee and tax, comes from the Consumer Rights Directive of 2011, whose Article 6(1)(e) requires the trader to give "the total price of the goods or services inclusive of taxes" and all additional charges before the consumer is bound. Leaving a material charge out of the price is a misleading omission under the Unfair Commercial Practices Directive of 2005. The Omnibus Directive of 2019, which Member States had to apply from 28 May 2022, did not invent all-in pricing. What it added was sharper enforcement, requiring that the maximum fine for widespread infringements be at least 4% of the trader's annual turnover, or at least €2 million where turnover is unknown, together with several new duties that Section 5.5 meets.

The practice that the rules forbid has a name. **Drip pricing** is showing a headline price and adding unavoidable charges later in the purchase, one step at a time, so that the customer has committed time and attention before seeing the real total. The United Kingdom (UK), where Encore does not sell, banned drip pricing outright from 6 April 2025 under its Digital Markets, Competition and Consumers Act 2024, which shows which way the law is moving. Encore shows the all-in price from the first screen on which any price appears, for primary tickets and resale alike. How that price is rendered across locales and currencies is a design-system concern, and Section 7.5 treats it there.

#### What a venue pays for {#c5-venue-subscriptions}

The Architecture book's Section 14.5 has already priced Encore's tiers from the engineering side, and its Figure 14.4 pairs each tier with a deployment model, an isolation level and an objective. Self-service venues share a pool in serverless cells of about 50 and a single 99.9% objective. Professional tenants run in Kubernetes cells with a database each and an error budget of their own. The Enterprise tenant has a silo, and for it the isolation is the product. This section adds the commercial logic that the tier sheet leaves implicit: what a buyer pays for at each tier, and what makes a buyer move up.

Self-service venues pay a per-ticket platform fee, netted from their payouts, and no monthly subscription. Professional tenants pay a monthly subscription and a lower per-ticket fee. Enterprise terms are negotiated once a year. The structure creates three reasons to upgrade, and Encore designs each one on purpose. The first is volume. Because the professional subscription is paired with a lower per-ticket fee, there is a crossover point, a number of tickets a month, above which Professional costs less in total than Self-service, and the console tells a self-service venue when it has passed that point. The second is isolation. A venue that does not want its customer lists in tables shared with a rival's, or that wants an error budget no other tenant can spend, needs Professional, because only Professional provides them. The third is the enterprise checklist, from single sign-on to customer-managed keys, which the Architecture book showed to be a list of architectural commitments. An upgrade path can also be built from annoyance, from limits set low enough to irritate a customer into paying, and it produces upgrades and churn together, because the customer remembers the irritation. Each of Encore's three triggers corresponds to a real difference in what the platform does or costs to run, which is why the company can explain all three without embarrassment.

#### Pricing the resale fee {#c5-resale-fee}

Section 2.3 established that pricing in a multi-sided market is set for all sides together, and that the real question is who pays. David Evans and Richard Schmalensee, in *Matchmakers* (2016), describe the usual answer: platforms often charge one side little or nothing, because that side is the harder one to attract and its presence is what the other side pays for, and they recover the cost from the side that values the match more. Geoffrey Parker, Marshall Van Alstyne and Sangeet Paul Choudary make a similar case in the monetization chapter of *Platform Revolution* (2016). For Verified Resale the scarce side is the seller. A resale market is only as good as its listings, and a fan who cannot attend has the easy alternative of handing the ticket to a friend or selling it on the grey market. So sellers pay nothing and receive the resale price in full. Buyers, who came looking for a ticket that will scan, pay the fee.

The trio compared three structures for that fee. A flat fee per ticket is simple to explain and to account for, but it falls hardest on cheap tickets: a €5 fee is a quarter of a €20 club ticket and a fortieth of a €200 stadium ticket. A percentage of the resale price scales with the ticket and divides cleanly among the parties. A third structure, in which the rate falls as the resale price drops below face value, would spare sellers who are already taking a loss, but under a face-value cap prices can only fall, a percentage already shrinks in euros as they do, and a sliding rate would complicate the price display and the ledger for a small benefit. Encore chose a fixed 10% of the resale price, charged to the buyer and shown in the all-in price. The split is fixed as well, at four points to the partner that brought the buyer, three to the organizer and three to Encore, whose share carries the payment provider's charges, fraud losses and support. A listing is visible in Encore's own app and on every authorized partner, and when the buyer purchases in Encore's app there is no partner to pay, so Encore keeps those four points as well. Figure 5.2 follows one resale through each case.

| Case | Buyer pays | Seller receives | Partner | Organizer | Encore |
|---|---|---|---|---|---|
| €60 ticket bought through a partner | €66.00 | €60.00 | €2.40 | €1.80 | €1.80 |
| €60 ticket bought in Encore's app | €66.00 | €60.00 | — | €1.80 | €4.20 |
| €60 ticket, designated Irish event, through a partner | €60.00 | €54.00 | €2.40 | €1.80 | €1.80 |

*Figure 5.2 — One resale at face value, three ways. The 10% fee is split four, three and three points; Encore keeps the partner's four points when the buyer purchases in its own app. Where the law caps what the buyer pays, as for Ireland's designated events, the fee comes out of the seller's proceeds. The seller is paid five days after the event.*

The cap needs one more sentence of definition, because the law cares about it. The resale price may not exceed the original price the seller paid, including the primary fees on that purchase, and the buyer's 10% fee is charged on top. That is Encore's default in every market. Where the law caps the buyer's total, as Ireland's Sale of Tickets Act 2021 does for designated events, the fee is taken from the seller's proceeds instead, which is the third row of the figure. The split is the same in every case, and it is the same for every organizer, on every tier, whatever they negotiate elsewhere. Organizers may tighten the rules of resale, but the money has one rule, because a split that varies by contract would turn every payout into a special case and every partner statement into a negotiation.

One question about the fee belongs to finance, and the product must be ready for either answer. When a buyer pays €66, the payment provider sends €60 to the seller and €6 to Encore, and Encore pays €4.20 of that fee on to the partner and the organizer. Is Encore's revenue €66, €6 or €1.80? Under International Financial Reporting Standard (IFRS) 15, the accounting standard for revenue, the answer turns on whether Encore acts as principal, controlling the ticket before it passes to the buyer, or as agent, arranging a sale between others; its guidance on that distinction sits in paragraphs B34 to B38. Encore's finance team makes that judgment. The product's obligation is to record each party's share separately, on every resale, so that either answer can be reported without reconstructing anything.

#### Metrics follow the model {#c5-metrics-follow}

Alistair Croll and Benjamin Yoskovitz organize much of *Lean Analytics* (2013) around one question, what business are you in, because the business model decides which numbers matter. Section 4.1 drew the general lesson, that model and stage drive the choice of metric. Here we need only the mapping for Encore's three revenue lines, which Figure 5.3 gives.

| Revenue line | Model | What the model rewards | Metrics that follow |
|---|---|---|---|
| Primary ticket fee | Pay-as-you-go | Tickets sold | Fee revenue per ticket; sell-through per event |
| Venue and organizer tiers | Subscription | Customers who stay and grow | Monthly recurring revenue (MRR); churn; expansion revenue |
| Verified Resale | Transaction marketplace | Matches completed at the cap | Liquidity (share of listings sold before the resale window closes); take rate; dispute rate |

*Figure 5.3 — Each revenue line brings its own measures. The dashboards of Section 4.1 follow from this table; contribution margin per resold ticket is computed in the Software book's Section 8.5.*

One of these terms needs a definition, and one of the incentives a warning. **Take rate** is the share of the value of transactions that a platform keeps as revenue. For Verified Resale, measured against the resale price, it is three points when a partner brings the buyer and seven when the buyer purchases in Encore's app. That difference is where the model's incentive becomes dangerous. A team judged on take rate alone would have every reason to steer buyers toward Encore's app and away from the partners who brought the market liquidity in the first place, and the partners would notice. Encore guards against this by policy: every listing appears everywhere at the same all-in price, partners see their own channel's numbers, and the Resale team's dashboard puts partner-sourced sales beside take rate, so that nobody can improve one by quietly damaging the other.

**Recap.** Each monetization model rewards some behavior, and Encore runs two of the five deliberately, declining the others for reasons it can state. All-in pricing comes from the Consumer Rights and Unfair Commercial Practices Directives, and venue tiers carry upgrade triggers that follow real differences in value and cost. The resale fee is a fixed 10% on the buyer, split four, three and three, with a clear rule where the law caps the buyer's total, and the model chosen decides the metrics, which must be watched beside the relationships they could damage.

**Exercise 5.2.** List your product's revenue lines. For each, write down which of the five models it uses, which customer behavior that model rewards, and which behavior it rewards inside your own company. Then find one place where two of your revenue lines reward conflicting behavior, and say who in your organization is responsible for noticing.

### 5.3 Packaging into Tiers

#### Leaders, fillers and killers {#c5-leaders-fillers-killers}

A **tier** is a named package of features, limits and terms sold at one price, and the familiar arrangement of three tiers, often called good, better and best, is the commonest way to offer different segments different value without negotiating with each customer. The hard part is deciding what goes where. Ramanujam and Tacke sort features into three kinds. **Leaders** are the must-have features with the highest willingness to pay, the ones that decide which tier a customer chooses. **Fillers** are nice-to-haves that add perceived value without driving the choice. **Killers** are features most buyers would refuse to pay for, and forcing them into a package can sink the sale of the whole package. A tier is well designed when each one is built around a leader, carries fillers where they cost little, and contains no killers.

Packaging is older than software, and one of its earliest theorists saw its uncomfortable side clearly. The French engineer and economist Jules Dupuit, writing in 1849 about tolls on transport, observed that railway companies left their third-class carriages open to the weather, and that the reason was not the cost of a roof. It was to keep travelers who could afford second class from traveling third. Dupuit had described what pricing people now call a fence, a difference between packages that stops customers with a high willingness to pay from buying the cheaper one. The analogy teaches, and it also warns. A fence built from deliberate damage works, but it insults everyone on the cheap side of it, and they remember. Software makes deliberate damage easy, because withholding a feature costs nothing to build. The fences that last are built from real differences, in isolation, scale, support or cost to serve, which the customer on either side can accept as fair. Encore's tiers follow that principle, as the tier sheet in the Architecture book shows: what separates them is a pool, a database of one's own and a silo, each with a real cost behind it.

Verified Resale forced a packaging decision. Putting resale only in Professional and Enterprise looked like a leader, a reason to upgrade, and the trio rejected it for three reasons. Resale's fairness rules are platform rules, which hold for every event whatever its organizer pays, and selling fairness by tier would mean that the fans of small venues stayed on the grey market. Liquidity needs breadth, because a resale market that covers only the events of larger tenants gives partners too few listings to build a habit around. And in Ireland the law makes resale at or below face value impossible to forbid, so for Irish events a tier gate would have been unenforceable. Verified Resale is therefore available on every tier, and the organizer's three-point share is paid on all of them. What differs by tier is a filler, the detailed resale reports in Organizer Insights, which come with Professional. A mandatory resale analytics pack priced into the self-service tier was considered and dropped, because for a venue selling a few hundred tickets a month it would have been a killer.

#### Bundles, add-ons and conjoint {#c5-bundles}

Once features are sorted, a second choice remains: which to include in a tier and which to sell separately. The working rule is that a feature belongs in the bundle when most of the tier's segment values it, and in an add-on when a minority values it highly and the rest would resent paying for it. Where the stakes justify it, the choice can be measured. **Conjoint analysis** is a survey method in which respondents choose repeatedly between packages that differ in features and price, and the pattern of their choices reveals how much each feature is worth to them. Its roots are in the theory of conjoint measurement that R. Duncan Luce and John Tukey published in 1964, and Paul Green carried it into marketing in the early 1970s; Green, Abba Krieger and Jerry Wind looked back on three decades of its use in 2001. It is a mature method, and it has the same weakness as every survey of hypothetical money. Schmidt and Bijmolt found hypothetical bias in indirect methods such as conjoint as well as in direct questions, so a conjoint study's results are checked against real sales before anyone trusts them.

Encore reserves conjoint studies for its tier sheet, which it revisits once a year and where a misplaced feature affects every tenant's renewal. Verified Resale did not need one, because the one packaging question it left open, where the detailed reports belong, was small enough to settle from the interviews.

#### Entitlements in code {#c5-entitlements}

Packaging is a commercial decision, and it should be possible to change it without changing code. That is only true if the code never mentions a tier. An **entitlement** is a named right that a customer holds under its plan, such as a feature, a limit or a quota, recorded as data. A tier, seen from the code, is simply a set of entitlements, versioned and given an effective date, and product code checks the entitlement it needs and never the tier's name. A plan file in Encore's form looks like this:

```yaml
plan: professional
version: 7
effective_from: 2027-01-01        # rated and billed from this date
entitlements:
  features: [verified_resale, resale_rules_console, resale_reports_detailed, own_database]
  limits:
    staff_seats: 50
  quotas:
    rule_assistant_requests_per_month: 2000
# product code asks:   entitlements.allows(tenant, "resale_reports_detailed")
# product code never asks:   tenant.tier == "professional"
```

The rule matters for a reason of complexity, in the sense the Architecture book took from Brooks. The packaging of a business is essential complexity: Encore really does sell different things to different customers, and no design removes that. A tier name tested in a hundred places across 40 teams is accidental complexity, added by us, and its cost appears the first time packaging changes. Moving one feature to every tier then becomes a code change in every service that tested the name, released on every team's schedule. When code checks entitlements instead, the same move is one edit to versioned data, reviewed and rolled out like any other configuration.

The Software book's Section 7.3 builds the entitlements service, chooses how it fails (open for display, closed for anything involving money) and rolls entitlement changes out per tenant, and the same section explains why entitlements, release flags and configuration must be kept apart. Each entitlement is also covered by a contract test, of the kind the Software book's Section 3.3 describes, which checks that a tenant without it cannot reach the feature by any path.

#### Packaging cannot outrun the architecture {#c5-packaging-architecture}

The Architecture book's Section 14.5 states the principle that packaging and architecture must be designed together, and this chapter needs only one rule to put it into practice: every promise made to a customer must correspond to a cell of the tier sheet. A promise the deployment model cannot deliver is a debt that engineering pays later, usually during an incident.

The commonest form of the mistake is an objective sold to a tenant whose tier cannot honor it. Suppose a large self-service venue, negotiating hard, is promised 99.95% availability. Its tier runs in a shared pool with one error budget spent by about 50 venues together, and nothing about that venue's contract changes how the pool behaves. The promise can be kept only by luck, or by quietly moving the venue to a professional cell at Encore's expense, and neither is a plan. Encore's rule is that any commitment in a proposal that does not appear on the tier sheet goes to the Tenant Configuration team and the relevant product trio before signature, and the answer is either a different tier or a refusal.

**Recap.** Good tiers are built around leaders, contain no killers, and are separated by fences built from real differences. Verified Resale is on every tier because its fairness rules, its liquidity and Irish law all demand breadth. Packaging lives in code as entitlements held as data, so that it can change without code changes, and no customer may be promised anything the tier sheet cannot deliver.

**Exercise 5.3.** Find three places in a codebase you know that test a plan or tier name directly. Rewrite one of them as an entitlement check, and write down what packaging change the original code would have turned into a release across several teams.

### 5.4 Metering and Billing as Software

Billing systems have unforgiving users. A customer will forgive a slow page sooner than an invoice that charges them twice, and the practices of this section are correspondingly conservative, and old. In 1494 Luca Pacioli set out double-entry bookkeeping in his *Summa de arithmetica*, describing the Venetian merchants' method of recording every amount twice, as a debit in one account and a credit in another, so that the books must balance and an error shows itself as an imbalance. Five centuries later, the same principle runs through every serious billing system: record each fact once, derive everything else from the facts, and arrange matters so that a mistake cannot hide.

#### Billable events are facts {#c5-usage-events}

Metering starts with an event. A **usage event** is a record that something billable happened, written once by the domain in which it happened and carrying a key that makes a second write of the same fact harmless. That last property is **idempotency**, and it matters because in a distributed system every message may arrive twice. If the fact carries a key derived from what happened, the receiver can recognize the repeat and ignore it, and the meter counts each sale once however many times it is told about it. Stripe's application programming interface (API) documentation explains the practice for payment requests, and Brandur Leach's 2017 essay on implementing Stripe-like idempotency keys in Postgres shows how to build it.

For Verified Resale the billable fact is `ResaleCompleted`, and its timing is a product decision. A listing moves through listed, reserved, sold and reissued, the lifecycle the Software book's Section 8.2 describes, and the tempting moment to bill is the sale. Encore bills at the reissue instead. The Resale service emits `ResaleCompleted` only after the Inventory team's issuance code has revoked the seller's barcode and issued the buyer's, so a sale whose reissue fails is never billed, and nobody has to unwind a charge for a ticket that never changed hands. Two later moments are kept separate from it, because they answer different questions. The seller is paid five days after the event, when the reissued ticket can no longer be disputed, and the partner's commission, accrued at the sale, is released at the same moment and reversed if the sale is reversed, as the Software book's Section 8.3 describes. The event looks like this:

```json
{
  "type": "ResaleCompleted",
  "idempotency_key": "resale:lst_88412:reissue:1",
  "occurred_at": "2027-03-14T19:02:11Z",
  "tenant_id": "tnt_4471",
  "event_id": "evt_20931",
  "listing_id": "lst_88412",
  "channel": "rowmate",
  "resale_price": { "amount": 6000, "currency": "EUR" },
  "fee_payer": "buyer",
  "revoked_ticket_id": "tkt_5513c",
  "issued_ticket_id": "tkt_9f02a"
}
```

The event carries the facts and none of the money. It does not say what the fee was or how it was split, because those depend on the price book, and the price book can change. `fee_payer` records which rule applied, buyer or seller, because that is a fact about where this sale took place. Metering then aggregates these events per tenant, as the Architecture book's Section 14.5 describes for every other per-tenant resource.

#### Rating against the price in force {#c5-rating}

**Rating** is the step that turns usage into money, by applying to each event the price that was in force when the event happened. That clause is where most billing errors are born. A price book that holds only current prices cannot rate last month's usage correctly once anything has changed, and it cannot reproduce last month's invoice when a customer disputes it. So every price, fee rate, split and cap in Encore's price book carries two dates. Its valid-from date says when it applies to the world, and its recorded-at date says when Encore wrote it down. Martin Fowler's essays on temporal patterns gave this arrangement its common vocabulary, and the two-date form is usually called **bitemporal**. The first date lets the rating engine find the right price for any event. The second lets anyone ask what Encore knew when it issued a given invoice, so that a late correction is visible as one.

```yaml
price_book: verified-resale
entry: resale-fee
valid_from: 2027-01-01
recorded_at: 2026-10-02T09:14:00Z
fee_rate: 0.10                    # of the resale price
split: { partner: 0.04, organizer: 0.03, encore: 0.03 }
split_own_app: { organizer: 0.03, encore: 0.07 }
fee_payer_rule: buyer, except where local law caps the buyer's total
```

With facts in the events and prices in the book, invoices and payout statements become derived documents. Each can be recomputed at any time from the events and the price book as they stood, and if the recomputation disagrees with what was sent, something is wrong and can be found. The organizer's three points become a payout line, the partner's four points a line on its monthly statement, and every split is written to the finance ledger that the Architecture book's Section 9.1 separated from orders, where it is reconciled daily. The money itself never passes through Encore's hands. Resale payments run through the primary payment provider's split-payment product, which holds the seller's €60 in an account in the seller's name until the payout date and sends the €6 fee to Encore; Encore then pays the organizer's and the partner's shares out of its fee. Why Encore must never hold the buyer's money, and how it moves, is the subject of the Software book's Section 8.2.

#### When payment fails {#c5-dunning}

Payments fail for ordinary reasons. **Dunning** is the sequence of retries, notices and grace periods by which a company tries to collect a failed payment before it restricts service. It is standard practice, and the published statistics about how much revenue it recovers come almost entirely from billing vendors' marketing, so they are best left unquoted. What matters for a product team is the policy, because the policy decides how a customer is treated on a bad day.

Encore's policy follows its tiers. Self-service venues have nothing to dun, because their fees are netted from their payouts, which is one quiet advantage of pay-as-you-go; only a venue whose refunds exceed its sales in a period ends up owing money, and it is invoiced. Professional subscriptions are retried over 14 days with a notice at the first failure, another at a week and a third at two weeks, and the tenant then has a grace period to day 30. After that, a person in Billing & Payouts reviews the account with its commercial owner, and only a person may decide to suspend. Enterprise payments follow the contract and are never handled by automation at all.

A concert explains why. Imagine a promoter and a venue falling out over money on the night of a show. Any sensible house settles the dispute after the show, and nobody cuts the power during the encore, because the audience is not a party to the dispute. Encore's version is that a suspended organizer's fans are never harmed and that no on-sale is ever stopped without a person's decision. The analogy breaks in a way that makes the rule more urgent for software. Cutting the power at a concert requires someone to walk to a switch in front of thousands of witnesses, while a scheduled job can suspend a tenant at three in the morning with nobody watching. So suspension is a state that only a person can enter. How it works without collateral damage, with sold tickets staying valid and payouts held, is the subject of the Software book's Section 7.5.

#### Every line traces to an event {#c5-correctness}

Billing has a short list of correctness properties, and each can be checked. Every invoice and payout line must trace back to the events that produced it. No event may be counted twice, and none may be missed. The parts of every amount must add up to the whole. The billing system's totals must match the finance ledger's every day. And every change to a price, a split or a contract must leave a record of who made it and when. None of these is specific to Encore; they are what billing systems everywhere have learned to check, usually after failing to.

The most instructive public failure is a recent one. In May 2017 Uber disclosed that in New York City it had been taking its commission from drivers on the gross fare, which included taxes and the Black Car Fund fee, where it should have used the net fare. The company said the error came to light while it was overhauling driver receipts, and committed to repay drivers what they were owed, plus interest; the *Wall Street Journal* estimated the total at about $45 million. Nothing about the payments themselves was broken. The formula was applied to the wrong base on every trip, and nothing checked the base against the agreement. The positive proof of the practice comes from Stripe, which in 2024 described Ledger, its internal system for tracking and validating money movement: an immutable, double-entry-style log that checks fund flows across about 5 billion events a day.

Encore runs four checks every night. Every `ResaleCompleted` must have exactly one rated line, and every rated line one event. Every resale's parts must sum to what the buyer paid, so that €66 is exactly €60 to the seller and the three shares of the fee. The day's splits in the billing system must equal the day's entries in the finance ledger. And the price book entry applied to each line must be the one valid on the event's date. In platform work inside a large bank I learned to distrust any number that could not be recomputed from its inputs, and these checks exist so that every number Encore pays out can be.

#### Build the meter, buy the invoice {#c5-build-or-buy}

Billing engines are mature products, and the Architecture book's Chapter 13 gives the test for buying one: buy what is commodity, and build what differentiates the business or encodes knowledge nobody else has. Invoicing, tax calculation, payment collection and the mechanics of dunning are commodity, and Encore buys them for its subscriptions. Collecting and splitting resale payments is bought as well, from the primary payment provider, and Encore accepts the price of that choice: only that provider carries resale, so resale checkout pauses when it is degraded. The metering events and the revenue-share logic are Encore's own, because no vendor knows that a resale is billed at reissue, that a partner's four points move to Encore when the buyer purchases in the app, or that an Irish designated event takes the fee from the seller. Encore owns `ResaleCompleted`, the price book and the rating of resale fees, and hands the bought engine the subscription lines it has to invoice.

**Recap.** Billable usage is recorded as facts, once, with idempotency keys, by the domain where it happens, and Encore bills resale at reissue so that a failed reissue is never charged. Rating applies the price in force when the usage happened, from a bitemporal price book, which makes every invoice and payout reproducible. Dunning is a product policy in which only a person may suspend a customer, and correctness is a short list of checks run every day.

**Exercise 5.4.** Take one line of a real invoice your company has sent and trace it back to the usage events that produced it. Note every place along the way where a number could be counted twice or computed on the wrong base, and say which of them a nightly check would catch.

### 5.5 Changing Prices Safely

#### Price integrity {#c5-price-integrity}

A price is a promise to everyone who might pay it, and like any promise it is valuable only if it holds. **Price integrity** is the property that a company's prices mean the same thing to every customer and change only through announced, dated rules. Ramanujam and Tacke give it a chapter, warning against knee-jerk repricing: discounts granted quietly to whoever complains, increases sprung without notice. Each such move teaches customers that the price is negotiable for those who push.

Netflix provided the canonical case of a price change without integrity's protections. On 12 July 2011 it split its DVD and streaming services into separate plans, so that customers who had both saw their monthly price rise from $9.99 to $15.98, about 60%. New members paid the new prices at once, and every existing member moved to them on 1 September, seven weeks later, with no grandfathering. The reaction was fierce. On 18 September Reed Hastings apologized in a blog post and in the same post announced that the DVD business would be renamed Qwikster; on 10 October Netflix dropped Qwikster, but kept the new prices. On 24 October it reported that it had lost 800,000 US subscribers in the third quarter, leaving 23.8 million, against a forecast loss of 600,000. Netflix later recovered and grew far beyond its size in 2011, and the episode is remembered for its method more than its price: a large change imposed on every existing customer at once, with short notice and no path between the old price and the new.

The protection most companies now use is **grandfathering**: existing customers keep their old price for a stated period after a change, and the period ends on a published date, its sunset. Without a sunset, grandfathering slowly fills the billing system with prices nobody can explain. At Encore the price book is published, existing tenants keep old terms until a stated sunset, and discounts are granted only under written rules.

#### Price tests and their ethics {#c5-price-tests}

Amazon's DVD test returns here, because it marks the limit of what experimentation may do with a price. Online controlled experiments, the subject of Section 4.3, are the most reliable tool a product team has, and the temptation to point them at prices is strong. Ron Kohavi, Diane Tang and Ya Xu give a chapter of *Trustworthy Online Controlled Experiments* (2020) to the ethics of experiments, weighing risk against benefit and asking when participants must consent, and on a price those questions are sharper than anywhere else, because a price test changes what a person pays.

Three rules have emerged from practice, and Encore adopts all of them. Test packaging and presentation before price, since how an offer is described and bundled often matters more than its level, and testing it harms nobody. Test prices on new offers and new customers, never on what an existing customer already buys. And when a price is tested, everyone in the test pays the lowest price tested, Amazon's own remedy, which makes the test a discount for some and a loss for nobody.

The law has drawn a line of its own, and it is narrower than many people assume. The Omnibus Directive added a duty to the Consumer Rights Directive, in its Article 6(1)(ea), to tell consumers "where applicable, that the price was personalised on the basis of automated decision-making". Its Recital 45 is explicit about what that duty does not cover: it "should not apply to techniques such as 'dynamic' or 'real-time' pricing that involve changing the price in a highly flexible and quick manner in response to market demands when those techniques do not involve personalisation based on automated decision-making." So the Directive governs prices set for a person from what is known about them, and leaves demand-based pricing and randomized price tests outside its disclosure duty. Randomized tests sit in a grey zone, because they are not personalized on any characteristic of the consumer, and where personal data drives a decision, the General Data Protection Regulation's Article 22 on automated decisions applies as well. The practice the duty targets is real. The European Commission's 2018 study of personalized pricing and offers found that 61% of the 160 websites it mystery-shopped personalized the ranking of the offers they showed.

Encore's rule is stricter than the law, and it is absolute: no individual price experiments on fans, ever. Geographic and switchback designs, which Section 4.5 describes, may vary what a fan sees or when something happens, but never the price that a given fan pays. When Encore tests how the resale fee is displayed, as Chapter 10 recounts, every fan in every arm pays the same 10%, and only the presentation moves. The rule costs Encore some knowledge about price sensitivity, and the trio accepts that cost knowingly, because Verified Resale's whole proposition rests on fans believing that a price at Encore is the same for everyone.

#### Moving prices and public trust {#c5-moving-prices}

**Dynamic pricing** is setting a price that moves with demand, often automatically and within minutes, and in concert ticketing it has drawn more public anger than any other pricing practice. The case most often cited in Europe turned out, on investigation, to be about something else. When tickets for Oasis's reunion tour went on sale in the UK in August 2024, many fans believed they had been charged surge prices by an algorithm. The Competition and Markets Authority (CMA) opened an investigation into Ticketmaster in September 2024 and closed it with undertakings on 25 September 2025. It found that many fans believed dynamic pricing had been used, and stated that "the CMA has not found evidence that this was the case." What it did find was **tiered pricing** that fans in the queue had not been told about, with standing tickets sold at two prices and the higher released once the cheaper had sold out, and "platinum" tickets sold at almost two and a half times the price of standard tickets without any extra benefit being explained.

Ticketmaster undertook, without admitting wrongdoing or liability, to give at least 24 hours' notice when it would use tiered pricing, to show price ranges in queues and update them quickly as cheaper tickets sold out, to avoid misleading labels, and to report to the CMA for two years. The CMA's chief executive, Sarah Cardell, put the principle in one sentence: "Fans who spend their hard-earned money to see artists they love deserve to see clear, accurate information, upfront." Fans can accept prices that move. What they will not accept is a price that moves without their being told how.

Encore's position follows directly. The organizer sets the prices, through the price levels and ticket types that the Pricing & Presales team's tools provide, and Encore displays them truthfully. If an organizer releases a price level in stages, the event page says so before the on-sale and the waiting room shows the current range. Encore runs no algorithmic surge of its own. One more rule from the Omnibus Directive bears on the same screens: when a price reduction is announced, the prior price shown must be the lowest price of the previous 30 days, under the new Article 6a of the Price Indication Directive, so that an organizer's price-drop promotion cannot inflate the price it claims to cut.

#### Resale rules by country {#c5-resale-rules}

There is no EU-wide cap on resale prices. The one EU-wide rule specific to ticket resale is the point the Omnibus Directive added to the blacklist of unfair practices, point 23a of Annex I of the Unfair Commercial Practices Directive: reselling event tickets to consumers is always unfair "if the trader acquired them by using automated means to circumvent any limit imposed on the number of tickets that a person can buy". The Directive's Recital 50 leaves Member States free to go further, and several have, Belgium and Ireland among them. Ireland's law is the most precise, and it shows what a resale rule asks of a product.

The *Sale of Tickets (Cultural, Entertainment, Recreational and Sporting Events) Act 2021* was signed on 14 July 2021 and fully commenced on 31 July. Its cap is narrower than its reputation. Section 15 makes it an offence for a secondary seller to sell or advertise a ticket above the original sale price, but only for events in a designated venue and for designated events, designated on application by the venue operator or organizer under sections 7 to 9; designation is aimed mainly at venues with a capacity of 1,000 or more. By July 2022, 27 venues and 42 events had been designated, Croke Park and the Aviva Stadium among them. The "original sale price" includes "any additional charge or fee applying to the sale", which is why Encore takes the resale fee from the seller for these events. Two further provisions matter as much as the cap. Section 17 requires secondary sellers to state the original price and the seat or standing area, and requires operators of secondary marketplaces to make sure their listings carry that information. And section 19, which applies to every event, designated or not, makes void any term of a primary sale that excludes or limits transferring a ticket for nothing or reselling it at or below the original price, unless the term is justified by safety, public health or public order. An organizer may forbid resale above face value. An organizer may not forbid resale at or below it. Encore's console therefore offers Irish organizers a lower cap, a resale window and per-fan limits, and no switch to turn resale off.

The UK's long dispute with viagogo shows where regulators actually spend their effort. After an investigation that the Office of Fair Trading began in 2012 and the CMA took up in 2016, the High Court made an order on 27 November 2018 requiring viagogo to tell buyers the seat they would get, the risk that a ticket might be refused at the door and who the seller was, to stop misleading claims about availability and how fast tickets were selling, and to honor its guarantee. In March 2019 the CMA said viagogo was still not compliant; on 4 July 2019 it moved forward with contempt proceedings, and on 5 September 2019 it suspended them after viagogo addressed the outstanding concerns. The whole case concerned what a marketplace shows its buyers, and the same concern runs through Ireland's section 17 and the Omnibus Directive's requirement that online marketplaces tell consumers whether the seller is a trader. A resale cap is one rule among many, and the larger engineering requirement is that every listing carries its original price including fees, its seat or standing area and its seller's status.

The UK is now moving further, and Encore watches it as context, since it does not sell there. On 19 November 2025 the government announced that resale above face value would become illegal, with face value defined as the original price plus unavoidable fees, a cap on resale platforms' service fees "to prevent the price limit being undermined", and fines of up to 10% of global turnover. The King's Speech of 13 May 2026 promised a draft Ticket Tout Ban Bill for scrutiny. As this chapter is written, in October 2026, the cap has been announced and is not yet law. The design consequence for Encore is that rules arrive by country, change on dates set by legislatures, and sometimes cover the fee as well as the price. Figure 5.4 shows the shape of the configuration that follows.

| Scope | Rule | Who sets it | Encore's product response |
|---|---|---|---|
| Every market | Resale at most face value, fees included; bot-acquired tickets never resold | Platform | Enforced by the Resale service; listings carry original price and seat |
| Ireland, every event | No term may forbid resale at or below face value (s.19) | Law | Console offers no "Resale off" preset or switch for Irish events |
| Ireland, designated venues and events | Resale above the original sale price, fees included, is an offence (s.15) | Law, from the public register | Buyer's total held at face value; fee taken from the seller's proceeds; register imported and versioned |
| Per event or organizer | Lower cap, shorter window, lower per-fan limits, resale off where lawful | Organizer, tighten only | Typed rules in the console, effective from a set date |

*Figure 5.4 — Resale rules by scope. Platform and legal rules form a ceiling that organizers may lower but never raise; the configuration is versioned like the price book, so every past resale can be checked against the rules in force on its day.*

#### Rolling out a price change {#c5-rollout}

The best recent proof of how not to change a price comes from Unity. On 12 September 2023 the company announced a Runtime Fee, a charge per installation of games built with its engine, which would apply to games that were already shipped and selling, so that businesses planned under one unit of charge were moved to another after the fact. Developers objected loudly, and on 22 September, ten days later, Unity apologized and withdrew much of it, exempting games already made with current versions of the engine. In September 2024 its new chief executive, Matt Bromberg, wrote that "we've made the decision to cancel the Runtime Fee for our games customers, effective immediately," and Unity replaced it with seat price increases from 1 January 2025: 8% for Pro and 25% for Enterprise, while the revenue ceiling of the free Personal tier doubled from $100,000 to $200,000. The replacement changed the level of a familiar price, where the Runtime Fee had changed what was counted and applied the change to decisions customers had already made. Unity's customers accepted the higher seat prices, and the change to the unit of charge was the one Unity had to withdraw.

Encore's sequence for any price change has five steps. The change is announced to the affected customers with its effective date, well before that date. The price book gains a new version with that valid-from date, so that rating switches cleanly and nothing old is rewritten. Existing customers are grandfathered to a stated sunset. Support receives the announcement, the reasons and the answers to the questions that will come, before the customers do. And the guardrail metrics of Section 4.1, which for organizers include churn and the rate at which they switch resale off, are watched through the change and for a quarter after it. The unit of charge never changes retroactively. A change is recorded in a short form that lives beside the price book entry it creates:

```yaml
change: professional-subscription-2027
affects: plan professional, versions 6 to 7
announced: 2026-10-01             # to every affected tenant, in the console and by email
effective_from: 2027-01-01        # new tenants and renewals
grandfathered_until: 2027-06-30   # existing tenants keep version 6 terms until then
unit_of_charge_changed: false     # if true, the change needs the trio's sign-off and a full year's notice
support_briefed: 2026-09-24
guardrails: [professional churn, downgrade rate, resale disabled rate, support contacts]
owner: Billing & Payouts with the Tenant Configuration trio
```

The configuration side of the change, the new price book version reaching every service that reads it, travels in stages from internal tenants to a few friendly ones to all, with automatic rollback on a health signal, as the Resilience book's Section 4.3 and the Software book's Section 7.3, on rolling out configuration, describe. The commercial sequence and the technical one meet at the effective date, so that on the day a price changes, nobody is surprised.

**Recap.** Prices change only by announced, dated rules, with grandfathering that ends on a published sunset, and the unit of charge never changes retroactively. Price tests vary presentation before price and give everyone the lowest price tested, while Encore forbids individual price experiments on fans outright. Fans resent undisclosed price movements more than moving prices, so Encore shows every tier and change truthfully, and resale rules, which arrive by country, demand above all that every listing discloses what the buyer is getting.

**Exercise 5.5.** Draft the announcement and the grandfathering rules for a 10% price increase on your product's middle tier. State the effective date, the sunset, what support will be told and when, and the guardrail metrics you will watch for a quarter. Then ask whether any part of the change alters what you count, and if so, rewrite the plan.

### Kata: The Seat and the Meter

> **Your brief: "Sumwise."** Sumwise sells bookkeeping software to small shops in four EU countries: about 41,000 customers, from single-owner boutiques to bakeries with three branches, served by 70 engineers in eight teams. It has always charged per user seat, at €12, €25 and €45 a month across three tiers, but most shops have one or two users, so revenue barely grows when a customer does. Its costs, meanwhile, follow volume: bank-feed connections, receipt scanning and invoice sending are charged to Sumwise per item by its suppliers, and its heaviest 5% of customers generate over half those costs while paying the same seat price as everyone else. The board wants usage-based pricing by the next financial year. The founders fear a revolt from loyal small customers, sales has granted about 3,000 private discounts nobody can fully list, and the billing code tests the tier name in 140 places.

**Deliverables:**

1. **Willingness-to-pay findings** — A plan for the problem, solution, value and price conversation with three segments of your choosing, drawn by need, and the scope decisions you expect the answers to change. Say how you will discount for hypothetical bias and which behavior you will use to check the answers.
2. **The price model** — The unit of charge, the model it belongs to and the behavior it rewards, with a worked example for a small customer and a heavy one. Show that a typical small shop pays no more than today.
3. **Tier sheet with entitlements** — Three tiers built around leaders, with fillers and no killers, the fences between them and the real difference behind each fence, and the plan files that express each tier as entitlements.
4. **Metering design** — The billable events, where each is recorded, its idempotency key, and the bitemporal price book entry that rates it, with the nightly checks that tie Sumwise's own counts to the supplier invoices.
5. **Migration plan** — The announcement, the effective date, the grandfathering rules and sunset for existing customers, the treatment of the 3,000 private discounts, the support briefing and the guardrails you will watch.
6. **Test policy** — What Sumwise may test about the new pricing, on whom, and under what rule about the price each tested customer finally pays.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Evidence before price | Does every price rest on answers or behavior from a named segment, with the hypothetical bias acknowledged? |
| Incentives | Does the unit of charge reward what Sumwise wants its customers and its own teams to do, and have you named the behavior it might distort? |
| Honest fences | Is every difference between tiers a real difference in value or cost to serve that a small shop would accept as fair? |
| Traceable billing | Could any line of a future invoice be recomputed from events and the price book as they stood on its date? |
| Integrity of change | Would a loyal small customer reading the announcement learn the date, the reason and the path, and find nothing retroactive? |
| Restraint | Can eight teams, with other work to do, deliver the migration within a year? |

#### Where you now stand

You can now treat price as a product decision that comes before construction, find out what customers will pay without believing everything they say, and choose a business model knowing which behavior it will reward. You can package a product so that the fences between tiers are fair and the code never knows a tier's name, record billable usage as facts and rate them against the price in force, and change a price in public without repeating the mistakes of Amazon, Netflix and Unity. With these decisions Part I's question, what to build, has its answer. Part II asks how the thing we decided to build should meet the people who use it. Chapter 6 takes up design for people, where Verified Resale's three faces, the organizer's console, the buyer's flow and the seller's dying barcode, each have to make a fair price and a firm rule understandable at a glance.

### References

- Madhavan Ramanujam, Georg Tacke — [*Monetizing Innovation: How Smart Companies Design the Product Around the Price*](https://www.wiley.com/en-us/Monetizing+Innovation%3A+How+Smart+Companies+Design+the+Product+Around+the+Price-p-9781119240860). Wiley, 2016.
- Amazon.com — [*Amazon.com Issues Statement Regarding Random Price Testing*](https://press.aboutamazon.com/2000/9/amazon-com-issues-statement-regarding-random-price-testing). Press release, 27 September 2000 — free online.
- European Parliament and Council — [*Directive (EU) 2019/2161 (the Omnibus Directive)*](https://eur-lex.europa.eu/eli/dir/2019/2161/oj). Official Journal of the European Union, 2019 — free online.
- Government of Ireland — [*Sale of Tickets (Cultural, Entertainment, Recreational and Sporting Events) Act 2021*](https://www.irishstatutebook.ie/eli/2021/act/21/enacted/en/html). Irish Statute Book, 2021 — free online.
- Competition and Markets Authority — [*Secondary ticketing websites*](https://www.gov.uk/cma-cases/secondary-ticketing-websites). Case page, 2016–2021 — free online.
- Competition and Markets Authority — [*CMA secures changes from Ticketmaster following Oasis tickets investigation*](https://www.gov.uk/government/news/cma-secures-changes-from-ticketmaster-following-oasis-tickets-investigation). Press release, 25 September 2025 — free online.
- David S. Evans, Richard Schmalensee — *Matchmakers: The New Economics of Multisided Platforms*. Harvard Business Review Press, 2016.
- Geoffrey G. Parker, Marshall W. Van Alstyne, Sangeet Paul Choudary — [*Platform Revolution*](https://wwnorton.com/books/Platform-Revolution/). W. W. Norton, 2016.
- Alistair Croll, Benjamin Yoskovitz — [*Lean Analytics*](https://leananalyticsbook.com/). O'Reilly, 2013.
- Jonas Schmidt, Tammo H. A. Bijmolt — [*Accurately measuring willingness to pay for consumer goods: a meta-analysis of the hypothetical bias*](https://doi.org/10.1007/s11747-019-00666-6). Journal of the Academy of Marketing Science 48(3), 2020 — free online.
- Ron Kohavi, Diane Tang, Ya Xu — [*Trustworthy Online Controlled Experiments*](https://experimentguide.com/). Cambridge University Press, 2020.
- Tod Golding — [*Building Multi-Tenant SaaS Architectures*](https://www.oreilly.com/library/view/building-multi-tenant-saas/9781098140632/). O'Reilly, 2024.
- Ilya Ganelin — [*Ledger: Stripe's system for tracking and validating money movement*](https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement). Stripe, 2024 — free online.
- UK Government — [*Government bans ticket touting to protect fans from rip-off prices*](https://www.gov.uk/government/news/government-bans-ticket-touting-to-protect-fans-from-rip-off-prices). Press release, 19 November 2025 — free online.
- Andrew Odlyzko — [*Privacy, Economics, and Price Discrimination on the Internet*](https://www-users.cse.umn.edu/~odlyzko/doc/privacy.economics.pdf). Proceedings of ICEC 2003, ACM, 2003 — free online.
- European Commission — [*Consumer market study on online market segmentation through personalised pricing/offers in the European Union*](https://commission.europa.eu/publications/consumer-market-study-online-market-segmentation-through-personalised-pricingoffers-european-union_en). European Commission, 2018 — free online.

---

## Chapter 6: Designing for People — Usability, Accessibility, and AI Features {#ch6}

> Every interface teaches. The only question is whether it teaches what we meant.

The first five chapters of this book were about deciding what to build: which bet to place, how to learn before building, how to measure what happens and what to charge for it. A product can survive all five decisions and still fail at the last step, at the moment a person meets a screen and has to work out what to do next. That moment is the subject of this chapter. It is an odd subject for engineers, because its failures rarely show in our telemetry: a fan who could not find the button to list a ticket raises no exception, and a blind fan who gave up on the seat map at minute two of an on-sale leaves no trace at all. The logs record what people did and say nothing about what they meant to do, and the difference between the two is where design lives.

The plainest demonstration of that difference in modern memory was printed on paper. In November 2000, voters in Palm Beach County, Florida, used a punch-card ballot whose layout was approved by officials, mailed in advance to every registered voter and inspected in public. A year later, six political scientists showed that the layout caused more than 2,000 voters who meant to vote for Al Gore to vote for Pat Buchanan instead, in a state that George W. Bush carried by 537 votes. We will look closely at how that happened, because nearly every idea in this chapter can be read off that one sheet of card.

Verified Resale reaches this chapter with its bet made, its riskiest assumptions tested, its metrics chosen and its price set. What it does not yet have is a design that people can use. It has three faces. Organizers set resale rules in the console: whether resale is allowed, the price cap, the window and the per-fan limits. Fans buy reissued tickets that carry Encore's guarantee. And sellers list a ticket and must understand that their old barcode stops working the moment it sells. This chapter follows the Resale trio, and the teams around it, as they design those faces, test them every month, make them accessible under European law and add the product's one AI feature, an assistant that helps organizers write their rules.

### 6.1 The Psychology of Everyday Things

#### The butterfly ballot {#c6-butterfly-ballot}

Theresa LePore was the elected Supervisor of Elections for Palm Beach County, and in the autumn of 2000 she faced an ordinary design problem. Ten presidential tickets had qualified in Florida, and listed in one column the names would have needed type too small for many of the county's elderly voters. So she split the names across two facing pages, with a single column of punch holes running down the spine between them, and printed the names larger. The layout gave the ballot its nickname, the "butterfly". It was used only in that county, and only for the presidential race on election-day ballots; absentee voters received a conventional design.

The trouble lay in how the holes were assigned. They alternated between the pages. The first valid hole belonged to George W. Bush, listed first on the left page. The second hole belonged to Pat Buchanan of the Reform Party, listed first on the *right* page. Al Gore was listed second on the left page, but his hole was the third one down. A voter who found Gore's name second on the left and counted down to the second hole, as anyone reading a list would, punched a vote for Buchanan. Arrows on the ballot pointed from each name to its hole, and they were correct. But they contradicted the order in which the eye reads a list.

Nobody caught this in advance. According to a later account by Joe Janes of the University of Washington's Information School, the sample ballot had been sent to the candidates, the party chairs and all of the county's registered voters, and no complaints were raised. Looking at a ballot, it turned out, is a different act from voting on one.

The evidence came a year later, from statisticians. Jonathan Wand, Kenneth Shotts, Jasjeet Sekhon, Walter Mebane, Michael Herron and Henry Brady published "The Butterfly Did It" in the *American Political Science Review* in December 2001. Of the 3,053 counties in the United States where Buchanan was on the ballot, Palm Beach gave him the most anomalous excess of votes. His share of the county's election-day ballots, the butterfly ones, was about four times his share of its absentee ballots, and no other Florida county showed such a gap. The authors concluded that the ballot caused more than 2,000 Democratic voters to vote by mistake for Buchanan, a number larger than Bush's certified margin in Florida. Even Buchanan's campaign doubted the result: two days after the election his sister and campaign manager, Bay Buchanan, was reported to be startled by the claim that he had strong support in a county where his campaign had never bought an advertisement or paid a visit.

There was a second channel of error. A ballot-by-ballot review published by the *Palm Beach Post* in March 2001 found 5,330 discarded ballots punched for both Gore and Buchanan, and, after netting out comparable combinations for Bush, estimated about 6,600 votes lost to Gore through overvotes. These were voters who punched one hole, sensed something was wrong and punched a second, because a punched card offers no undo and no feedback until it is counted. The two numbers measure two different failures, and Figure 6.1 sets them side by side.

| Error | Size | What went wrong in the person's head | Which bridge was missing |
|---|---|---|---|
| A vote for Buchanan meant for Gore | more than 2,000 (Wand et al.) | the voter formed a wrong model of which hole belonged to which name | mapping between names and holes |
| An overvote, Gore and Buchanan both punched | about 6,600 net (*Palm Beach Post*) | the voter noticed something was off and tried to correct it | feedback after the act, and any way to undo it |

*Figure 6.1 — The butterfly ballot's two errors. One is a failure of execution, the other of evaluation; Section 6.1 names both.*

About 10,000 voters reportedly signed affidavits saying the ballot had confused them, and groups of voters sued. The Florida Supreme Court held that even if their allegations were true, the ballot did not amount to the "substantial noncompliance" with election law that would void the result. The measurement came instead from a natural experiment, two ballot designs used by the same voters in one county, of the kind Section 4.5 described. Congress passed the Help America Vote Act in 2002, and in 2007 the US Election Assistance Commission adopted *Effective Designs for the Administration of Federal Elections*, written by AIGA's Design for Democracy program.

We should be careful about what this story proves. It does not prove that the ballot changed the outcome of the presidential election; Wand and his colleagues claimed only that the error exceeded the margin, and no court ruled on causation. What it proves is narrower and more useful to us. The same voters, given a different design, did not make the error. "User error" at that scale was a property of the design, and LePore, to her credit, said as much two days after the election: "Hindsight is 20-20, but I'll never do it again."

#### Affordances and signifiers {#c6-signifiers}

The vocabulary for talking about this comes mostly from Don Norman, a cognitive scientist who published *The Psychology of Everyday Things* in 1988, retitled *The Design of Everyday Things* for its paperback edition and revised in 2013. Norman borrowed the word **affordance** from the perceptual psychologist James Gibson and used it for the relationship between an object and a person that determines what the person can do with it. A door affords pushing; a punch card affords punching any hole. In a 2008 column in *Interactions* he added a second word, because designers had begun using "affordance" for every visible cue. A **signifier** is a perceivable signal that tells people what action is possible and where to take it. The distinction matters because we rarely control affordances on a screen; almost anything can be clicked. What we control is what the screen signals.

The ballot's affordances were uniform: every hole could be punched equally well. Its signifiers were the arrows and the position of each name, and they disagreed with each other. The arrows said one thing in small print, while the reading order, a far stronger signal, said another. When signifiers conflict, people follow the stronger one, so a designer who adds a weak cue to correct a strong one has corrected nothing.

The Architecture book borrowed the word affordance for APIs, where it described the operations a well-designed interface makes natural. On a screen the idea returns to its original home. Verified Resale's "List for sale" button appears on a ticket in the fan app only when that ticket is eligible: bought through the Sale Gate, inside the organizer's resale window and within the per-fan limit. A ticket that cannot be listed carries a short line explaining why, such as "Resale opens 14 June" or "The organizer has turned resale off for this show". The line is a signifier that answers the question the fan would otherwise take to Support.

#### The two gulfs {#c6-two-gulfs}

Norman's most durable idea, which grew out of his work with Edwin Hutchins and James Hollan on direct-manipulation interfaces in the mid-1980s, describes what happens when a person uses anything. Norman divides it into seven stages. A person forms a goal, then plans an action, specifies it and performs it; then perceives the state of the world, interprets it and compares it with the goal. The first three after the goal make up the side of execution, and the last three the side of evaluation. Between the person and the system lie two gulfs. The **gulf of execution** is the distance between what a person wants to do and what the system lets them see they can do. The **gulf of evaluation** is the distance between the state the system is in and what the person can perceive and understand of it. Designers bridge the first with discoverability and mapping, and the second with feedback.

The butterfly ballot failed on both sides, which is why Figure 6.1 has two rows. The Buchanan votes were a gulf of execution: the mapping between names and holes misled. The overvotes were a gulf of evaluation: a voter who had punched a hole could not tell what the hole meant, and could do nothing about it once punched.

Verified Resale's seller flow had a gulf of evaluation of its own, and the trio found it only by watching people. When a listed ticket sold, the first design showed a green "Sold" badge on the ticket card and sent a notification that the payout was on its way. The badge was accurate. What it did not tell the seller was that the ticket she still saw in her phone was now worthless at the door. The old barcode had been revoked and added to the revocation lists the venue scanners hold, but nothing on the screen said so, and for fans who had saved the ticket to Apple Wallet, whose passes Encore cannot rotate and updates only on a best-effort basis, the old pass could linger looking exactly as it always had. A seller who sees a valid-looking ticket and a "Sold" badge must reconcile two signals, and in testing most reconciled them wrongly: perhaps the sale was provisional, perhaps the old ticket still worked as a backup. Section 6.3 tells how the trio found this.

#### Conceptual models {#c6-conceptual-models}

People act on a model of how a thing works, and they build that model from what the thing shows them. Norman calls the impression the product actually gives its **system image**. Alan Cooper and his co-authors, in *About Face*, sharpen this into three terms that are worth keeping apart. The **implementation model** is how the system actually works. The **mental model** is how the user believes it works. The **represented model** is how the designer chooses to show it. A good represented model sits close to the user's mental model and hides the implementation unless the implementation changes what the user should do.

Here Verified Resale faces a genuine difficulty. Most fans think of a ticket as an object, like a paper ticket in a drawer: it exists, it can be handed over, and whoever holds it gets in. Verified Resale's implementation is nothing like that. A resold ticket is reissued: the seller's ticket identity is revoked at every gate, and the buyer receives a new one, with a new barcode that rotates every few seconds inside Encore's app. The represented model has to bridge the two without teaching fans cryptography. The trio settled on a single sentence that appears in both flows. For the seller: "When your ticket sells, it is cancelled and a new ticket is issued to the buyer. Your copy will no longer get you in." For the buyer: "This is a new ticket issued in your name. The previous owner's copy no longer works." The word "reissued" is used consistently and nowhere else, and the old ticket is always shown in a cancelled state, with its barcode greyed and struck through. Fans need not know how revocation lists work, only that the ticket changed hands in a way that cannot be copied, which is what the guarantee rests on.

#### Slips, mistakes and designing for error {#c6-designing-for-error}

When people err at an interface, two quite different things can have happened. A **slip** is the right intention carried out wrongly, such as clicking the button next to the one we meant. A **mistake** is the wrong intention carried out correctly, as when a voter who believes the second hole is Gore's punches it precisely. Norman built this distinction on James Reason's taxonomy of human error, which the Operations book treats in its Section 2.2 for the people who run systems. Here we need only its consequence for screens. Slips are reduced by constraints, spacing and undo. Mistakes are reduced only by a better conceptual model, because the person who makes one is doing exactly what they meant to do.

Confirmation dialogs are the industry's habitual remedy for both, and they work poorly for either. A person who confirms dozens of dialogs a day learns to confirm without reading, so the dialog stops slips only for a while. Against mistakes it does nothing at all, because the person confirming believes they are right. Two public cases make the point. On 13 January 2018 a warning officer at the Hawaii Emergency Management Agency sent a ballistic missile alert to phones across the state. Officials first called it a slip, a wrong choice from a drop-down. The Federal Communications Commission's investigation, reported in April 2018, found that the officer had believed the drill was a real attack: it was a mistake, and the officer had clicked "yes" on the confirmation prompt. The correction took 38 minutes to reach phones. On 11 August 2020 Citibank, acting as loan agent for Revlon, meant to pay about $7.8 million of interest to lenders and instead wired about $900 million of principal from its own funds. Its loan software, Flexcube, could make such a payment only by treating it as a repayment of the whole loan and sending the principal to an internal "wash" account, and that required three fields to be set to the wash account. The operator who entered the payment set one of them, believing it was enough; a second person checked the entry and a senior manager approved it. A federal district court let many lenders keep about $500 million in February 2021, and the Second Circuit reversed that decision in September 2022. My own years in fintech API architecture left me with a conviction these two cases confirm: approval is a control on people's intentions, and it cannot repair an interface that misleads them about what they are approving.

Norman's prescription, and Cooper's, is to make actions reversible wherever possible and to reserve confirmation for the few that are not. Cooper calls the needless dialogs and steps an interface imposes **excise**: work the software demands that does nothing for the user's goal. Verified Resale applies this precisely. Listing a ticket is reversible: until it sells, the seller can withdraw the listing in one tap, with no confirmation, because nothing has happened that cannot be undone. Selling is not reversible: once a buyer has paid, the ticket is reissued and the seller's copy dies. But the sale happens later, at a moment the seller does not choose, so the only place to say so is at listing time. The listing flow says it once, in the sentence quoted above, beside the final "List for sale" button, and it says it in terms of consequences ("your copy will no longer get you in") rather than as a question ("Are you sure?").

#### Knowledge in the world {#c6-knowledge-in-world}

The last of Norman's ideas we need concerns where knowledge lives. Some of what we need to use a thing we carry in our heads, and some the thing itself shows us. Knowledge in the world is slower to use than knowledge in the head, because we must look for it, but it needs no learning and it is never forgotten. Steve Krug, writing for the web, gives the same advice in a sharper form, borrowing "omit needless words" from Strunk and White: a screen should say the rule at the point of action, in as few words as will carry it.

The resale price field is where Encore applied this most carefully. The rule is that the resale price may not exceed what the seller originally paid, including primary fees, and that an organizer may set a lower cap. The first prototype showed an error only after the seller pressed "Continue". The redesign puts the rule on the field itself: the field opens with the maximum already entered, a line beneath it reads "Up to €60.00, what you paid", and the stepper will not go higher. A second line shows what a buyer will pay: "Buyers pay €66.00 including fees". WCAG, which Section 6.4 introduces properly, asks for the same thing in two of its criteria: labels or instructions where input is required, and errors identified in text. The design meets them by making the error almost impossible to commit.

**Recap.** The butterfly ballot shows that "user error" at scale is a property of the design, measured afterward, and that review by eye is not the same as use. Norman's vocabulary of signifiers, gulfs, conceptual models and designing for error lets us see such failures in advance, and Verified Resale's seller flow needed all of it.

**Exercise 6.1.** Take one flow you own that ends in an action the user cannot undo. Walk it through the seven stages of action, and for each stage write what the screen shows and what a person must already know. Mark each gulf you find, and say whether its errors would be slips or mistakes.

### 6.2 Goals, Personas, and Posture

#### Designing for goals {#c6-goal-directed-design}

Most software is designed around tasks: the things the system can do, arranged in menus. Alan Cooper spent his career arguing that this is the wrong starting point. In *The Inmates Are Running the Asylum* (1999) and in successive editions of *About Face*, he proposed **goal-directed design**: design that begins from what a person is trying to achieve, separates their end goals from the tasks they currently perform to reach them, and judges every screen by whether it moves them toward those goals. Cooper distinguishes end goals, the outcome wanted, from experience goals, how the person wants to feel on the way. An organizer's end goal is that the people who bought tickets actually come to the show, and that touts do not profit; her experience goal is to feel in control of her event without spending an afternoon on it. "Configure the resale window" is a task in service of both.

This is close kin to the jobs to be done of Section 2.2. The jobs the Resale trio wrote there are the goals this chapter designs against, so nobody at Encore invents a second set.

Cooper's other contribution is more contested. To keep goals vivid, he proposed the **persona**: a short, specific portrait of an archetypal user, built from research, given a name and used to settle design questions by asking what that person would need. The evidence about how personas are used is sobering. Tara Matthews, Tejinder Judge and Steve Whittaker interviewed practitioners for a CHI 2012 paper and found that they used personas almost entirely for communication and hardly at all for design. The authors concluded that personas cannot replace immersion in real data about real users. That is the condition under which Encore uses them. A persona at Encore is a communication device: it is allowed to exist only if every trait in it traces back to interview notes from continuous discovery (Section 3.1), and each interface has one primary persona so that its trade-offs are made for someone in particular. The Resale trio has three: a mid-size festival promoter who sets rules for a dozen events a year, a fan who buys one or two resold tickets a season, and a fan who sells because plans changed.

#### Posture {#c6-posture}

Some software we live in, and some we visit. Cooper's term for the difference is **posture**: the way a product presents itself to users, determined by how long and how attentively they use it. His desktop postures are three. A **sovereign** application is used for long stretches as the user's main tool, and can afford density, keyboard shortcuts and rich controls, because its users learn it. A **transient** application is visited briefly to do one thing, and must be obvious at a glance, because its users will never learn it. A **daemonic** application runs in the background and is seldom seen at all.

Verified Resale has faces in all three postures, and the trio's early prototypes went wrong by using one posture's idioms in another. Figure 6.2 shows where each face settled.

| Face | User and rhythm | Posture | What the posture asks |
|---|---|---|---|
| Organizer console, resale rules | Event managers, at a desk, often all day across many events | sovereign | density, keyboard paths, bulk edits across events, rules visible beside sales |
| Fan buy flow | A fan on a phone, about 90 seconds, once or twice a season | transient | one decision per screen, the all-in price and the guarantee in the first glance |
| Seller flow | A fan on a phone, a few minutes, perhaps once a year | transient | the consequence of selling stated once, plainly; status visible afterward |
| Ticket in the app and wallet | Checked rarely, used once at the gate | close to daemonic | silent until it matters; its state, valid or cancelled, unmistakable when it does |

*Figure 6.2 — Verified Resale's faces by posture. The wallet row is our analogy; Cooper did not write about wallet passes.*

The early rules console was the clearest case of leakage. Its first prototype was a friendly step-by-step wizard, one question per screen, with large buttons and reassuring copy. It tested well with an organizer who set rules for one event and badly with the festival promoter, who manages dozens of events across a season, who wanted to see the rules for all of them in one table, and who found that applying one change to twelve events meant walking through the wizard twelve times. A transient idiom had been put into a sovereign tool. The console now opens on a dense table of events and their rules.

#### Perpetual intermediates {#c6-intermediates}

Cooper makes a further observation about the people who use software over time. Few remain beginners for long, because being a beginner is uncomfortable and people learn enough to escape it. Few become experts, because most people learn only what they need. Most users, therefore, are what Cooper calls **perpetual intermediates**, and he argues that software should be optimized for them: frequent actions first, the rest reachable but out of the way. This is an observation from long practice, without a published measurement of how expertise is distributed behind it, and it should be held as a strong heuristic.

It describes the organizer setting resale rules exactly. Organizers touch these rules a few times a year, enough to know roughly what they do and too seldom to remember the details. So the rule editor opens on presets, each described in one sentence of consequences: "Standard: resale at up to face value until two hours before doors"; "Fan-first: resale opens one week after the on-sale, two tickets per fan"; "Resale off". An "Advanced" link reveals the individual settings. Hiding rare options behind a disclosure link of this kind, **progressive disclosure**, is long-established and well-tested practice. One preset varies by market. In Ireland, section 19 of the Sale of Tickets Act 2021 voids terms that block resale at or below face value, so the console does not offer "Resale off" for Irish events. It shows the other presets with a line explaining why, which is knowledge put into the world.

#### Scanning, satisficing and the billboard {#c6-scanning}

People do not read screens; they scan them. Steve Krug's *Don't Make Me Think* (2000, revised 2014) made this the foundation of web usability, on an older idea. In 1956 Herbert Simon proposed that people facing complex choices do not search for the best option but take the first one that is good enough, and he called this **satisficing**. Krug observed the same behavior on the web: users glance, pick the first plausible link and muddle through. Eye-tracking work by Jakob Nielsen's group found people reading web content in an F-shaped pattern, the first lines and the left edge, and little else. Krug's advice follows directly. Design each page like a billboard seen from a moving car: a clear visual hierarchy, conventions people already know, obvious clickable areas and as few words as possible.

The resale listing page is the purest billboard in the product. Encore set itself a target: a fan should be able to tell, within five seconds of the page loading, what each ticket costs in total, where it is, and that it is guaranteed. Five seconds is a number Encore chose, with no research behind it, and the target is checked with a five-second test, a recognized quick method in which a participant sees a screen briefly and says what they remember. The first version of the page failed it. Participants remembered the seat and the price before fees, and none mentioned the guarantee. The redesign shows the all-in price first, in the largest type, puts the "Verified" badge beside it and moves the fee breakdown one tap down.

#### Visual hierarchy for screens no designer sees {#c6-visual-hierarchy}

At 40 teams, most screens are never touched by a designer. Internal tools and many organizer pages are built by engineers from the design system's components. Adam Wathan and Steve Schoger wrote *Refactoring UI* (2018) for exactly those engineers. Their central advice is that hierarchy comes from weight and color as much as from size: de-emphasize the secondary, rather than enlarging the primary until everything shouts, and choose sizes, spacing and colors from fixed scales instead of picking them screen by screen. It is practitioner guidance, with no empirical studies behind it. One of its rules, though, has a standard behind it: never rely on color alone to carry meaning, which is WCAG's criterion 1.4.1. The scales themselves, and the tokens that hold them, belong to the design system, which Chapter 7 treats in full.

**Recap.** Goals give design a purpose, and personas are useful only as faithful summaries of research, used to communicate what the research found. Posture decides the idioms a face may use, and the commonest error is carrying one posture's habits into another. Most users stay intermediates, and people scan and settle.

**Exercise 6.2.** Name the posture of three screens you ship. For each, find one idiom borrowed from the wrong posture, such as a wizard in a sovereign tool or a dense table in a transient flow, and sketch the change that would remove it.

### 6.3 Usability Testing Every Month

#### Why a few users are enough {#c6-few-users}

Everything in the previous two sections can be learned from books, and none of it is enough. The butterfly ballot was reviewed by people who knew how ballots work. What it lacked was a handful of voters asked to use it while someone watched. A **usability test** is exactly that: representative users attempt real tasks with a design while observers watch, so that the team can see where the design fails.

The usual objection is that a handful of users proves nothing. The answer depends on what the test is for. In 1993 Jakob Nielsen and Thomas Landauer modeled how usability problems are found as more users are tested. If each user reveals a given problem with probability L, then n users find a share 1 − (1 − L)^n of the problems. Averaged over Nielsen's projects, L was about 31%, which means five users find about 84% of problems, and the curve flattens quickly after that. Nielsen's popular summary in 2000, "Why You Only Need to Test with 5 Users", attached conditions that are often forgotten: the users must be comparable, distinct groups of users need three or four each, and three small tests in sequence beat one large one, because each round fixes problems that would otherwise hide others.

The model has been challenged, and the challenge sharpens it. Laura Faulkner tested 60 users in 2003 and drew random sets of five from them. The sets found anywhere between 55% and 99% of the problems; ten users raised the minimum to 80%, and twenty to 95%. Five users are usually enough, then, but not reliably so, and the remedy is the one Nielsen proposed, which is to test small and test again. Steve Krug's practice of three users, one morning a month, rests on the same reasoning, plus the observation that a test cheap enough to run monthly is one a team will actually run.

These are **formative** tests: they look for problems to fix, and they explain why people struggle. They are not measurements. A three-person test cannot tell us how many fans will complete a resale purchase, or whether a new layout raises conversion; those are questions for the experiments of Chapter 4, which can measure but cannot explain. The two methods answer different questions, and a mature team uses both.

#### Running a test without a lab {#c6-running-a-test}

Krug's *Rocket Surgery Made Easy* (2010) describes a method that needs no lab, no specialist and very little money, and Encore's teams run it nearly as written. One morning a month, a facilitator sits with three participants in turn, each for about an hour, sharing a screen or a phone. The participant attempts a few tasks and thinks aloud. The rest of the team, product manager, designer and engineers alike, watch from another room or a video call. At lunch the observers each name the three most serious problems they saw, the group agrees on the worst few, and the team commits to fixing them before the next round, using the smallest change that could work. The script is short, and its most important lines are the ones that stop the facilitator from helping. The seller-flow script for Verified Resale's July round looked like this:

```text
Round: resale seller flow, prototype v4 (fan app)
Participants: 3 fans who bought tickets in the last 6 months; none employed by Encore
Before: "We're testing the app, not you. Please think aloud. I can't answer
         questions while you work, but I'll answer them all at the end."
Task 1: "You can't go to Saturday's show. Sell one ticket through the app."
Task 2: "A message says your ticket sold. Show me the ticket you have now."
Follow-up: "If you went to the venue on Saturday, what would happen if you
            showed this?"  (ask only after Task 2; do not prompt before)
Observers note: hesitations, wrong taps, anything said about the old ticket
Debrief: 12:30, each observer brings their top 3; fix list agreed by 13:30
```

Task 2 is where the gulf of evaluation of Section 6.1 surfaced. All three participants found the "Sold" badge. Asked what would happen at the venue, two of the three said they thought their ticket would probably still work, and one said she would keep the old one "just in case the sale falls through". Nobody in the trio had predicted it: the screen showed a sold badge and an unchanged ticket, and people believed the ticket. The fix agreed at the debrief was small. The ticket card now changes on sale into a cancelled state, with the barcode greyed and struck through and the line "Sold and reissued to the buyer. This ticket will not get you in." Fan Messaging's "your ticket sold" notification says the same, and admits that a wallet copy may linger for a while. The August round repeated Task 2 with three new participants, and all three said the old ticket would not work.

#### Testing with organizers {#c6-testing-organizers}

Organizers are few, busy and commercially important, and testing with them needs different mechanics. Encore recruits organizer participants through account managers, but the account manager does not attend the session, because an account manager who watches will steer, and an organizer who knows their account manager is watching will be polite. Sessions are remote and moderated, the industry's standard approach for business users, and they run in the organizer's own context where consent allows, on their real events, because a rules table makes sense only with the organizer's own events in it. The round complements the discovery interviews of Section 3.3. The festival promoter's frustration with the rules wizard, described in Section 6.2, surfaced in the second organizer round.

Usability testing has a cheaper complement for the many organizer screens that no designer reviews. **Heuristic evaluation**, introduced by Jakob Nielsen and Rolf Molich at CHI in 1990, has a few evaluators inspect a design against a short list of established principles, such as visibility of system status, error prevention and recognition rather than recall. Encore's design-system team runs one each quarter on the organizer console, and the findings go into the owning teams' backlogs like any other defect.

#### Research operations at 40 teams {#c6-research-ops}

When 40 teams test monthly, they need infrastructure, or they will recruit the same fans repeatedly, lose their consent records and rediscover each other's findings. **Research operations** is the practice of providing that infrastructure: recruiting, consent, incentives, tooling and the storage of findings, so that the people doing research can concentrate on the research. Kate Towsey, who built research operations at the UK Government Digital Service (GDS) and at Atlassian and founded the ResearchOps Community, set out the practice in *Research That Scales* (2024). It is widespread at large companies, and its evidence is practitioner experience; no measured outcomes have been published.

At Encore it is a group of three people in the design organization, outside the engineering headcount, and they coach more than they conduct. They run an opt-in participant panel of fans and organizers, cap how often anyone is contacted, pay incentives and keep a findings repository tagged by flow and team. GDS makes regular user research, including research with disabled people, part of its Service Standard, and Encore borrowed that expectation: every fan-facing team tests monthly, and the research-operations group makes it cheap enough to keep.

One part of this is not optional. Under the General Data Protection Regulation (GDPR), consent forms, recordings and the panel itself are personal data, with a lawful basis, a purpose and a retention period. Data about a participant's disability is special-category data under Article 9 and needs explicit consent and stricter handling. Encore keeps recordings for 90 days, records only the assistive technology a participant uses, and no diagnosis, and holds even that only with explicit consent.

#### Settling design arguments {#c6-design-arguments}

Krug devotes a chapter of *Don't Make Me Think* to a familiar meeting, "The Farmer and the Cowman Should Be Friends". Most arguments about usability, he observes, are disputes about what users will do, conducted by people who each generalize from themselves. Encore's design reviews open with one question: what did the last test show? The rule has limits. A test settles questions of behavior. It does not settle strategy, brand or price, which belong to Chapters 2, 4 and 5.

**Recap.** Small, frequent tests find most of a design's problems because problem discovery saturates quickly, provided the users are comparable and the rounds repeat. A morning a month, watched by the whole team and followed by small fixes, found the seller flow's worst flaw before any seller met it. At 40 teams the practice needs research operations, and the panel it keeps is personal data, held under the GDPR.

**Exercise 6.3.** Run one three-person test this month on a flow you shipped last quarter. Write the script first, including the follow-up question you will not ask until the end. List the three fixes you agree on and how large each one is.

### 6.4 Accessibility as an Engineering Requirement

#### The law and the standard, precisely {#c6-law-and-standard}

The butterfly ballot was, among other things, an accessibility decision: the type was enlarged for older voters, and the layout that made room for it broke the ballot for everyone. Accessibility and usability cannot be designed separately. The Architecture book's Section 8.5 made the architectural case: accessibility belongs in the design system and in continuous integration (CI), because it cannot be bolted on later, and Encore's target is WCAG 2.2 at level AA. This section says what that target means for a team, beginning with the law.

The **Web Content Accessibility Guidelines (WCAG)** are the W3C's standard for accessible web content, written as testable success criteria at three levels, A, AA and AAA. WCAG 2.2 became a W3C Recommendation on 5 October 2023 and was adopted by ISO as ISO/IEC 40500:2025. It added nine criteria, six of them at levels A or AA, and removed criterion 4.1.1, Parsing, as obsolete. For a team already meeting 2.1 AA, those six are the new work.

The **European Accessibility Act (EAA)**, Directive (EU) 2019/882, has applied since 28 June 2025. It covers certain products placed on the market and certain services provided to consumers, among them e-commerce services: services provided at a distance, by electronic means, at a consumer's request, with a view to concluding a consumer contract. Selling concert tickets online falls squarely inside that definition, so Encore's fan storefront and apps are covered. Four details of the Act matter in practice, and each is commonly misread.

First, the Act covers services to *consumers*. Encore's organizer console is a business-to-business tool and is outside its scope. Encore makes the console accessible anyway, under its own policy and EU employment-equality law, and nobody at Encore should claim the EAA requires it. Second, **microenterprises** providing services are exempt; the Act defines one as an enterprise employing fewer than 10 people with an annual turnover *or* an annual balance-sheet total of no more than €2 million. Third, the transitional rules are narrower than many believe. Service providers may go on using products they lawfully used before 28 June 2025 until 28 June 2030, and service contracts agreed before that date may continue unchanged for at most five years. Neither covers a ticket storefront's own website or app. Fourth, a provider may claim that a requirement would impose a disproportionate burden or fundamentally alter the service, but only on the strength of a documented assessment against the criteria in the Act's Annex VI, kept for five years.

The relation between the Act and the standard is also widely misunderstood. Under Article 15, conforming to a harmonized standard whose reference has been published in the *Official Journal* creates a presumption of conformity with the Act. The European standard written for this purpose is EN 301 549. Version 3.2.1 of 2021, built on WCAG 2.1 AA, is cited only under the separate Web Accessibility Directive, which covers the public sector. Version 4.1.1, built on WCAG 2.2 AA and written for the EAA, was published on 2 September 2026. As of October 2026 it has not yet been cited in the *Official Journal* under the Act; Ireland's National Disability Authority expects that to happen in December 2026. Until it is, WCAG 2.2 AA is the sensible engineering target and the best evidence of conformity a team can offer, though it carries no legal presumption by itself.

Enforcement is national and has begun. In November 2025, French disability organizations brought urgent proceedings against four large retailers over the accessibility of their online shops, the first such actions under the Act. Verified Resale launches in France first.

#### The criteria that hit ticketing {#c6-ticketing-criteria}

A handful of criteria bear on ticketing with particular force, and two of them are often misread. Figure 6.3 lists them with Encore's resolution.

| Criterion | What it requires | Where it bites at Encore | Encore's resolution |
|---|---|---|---|
| 3.3.8 Accessible Authentication (Minimum), AA | no cognitive test to log in, unless there is an alternative or help such as paste and password managers | fan sign-in before an on-sale | passkeys and email links; paste and password managers always allowed |
| 2.2.1 Timing Adjustable, A | users can turn off, adjust or extend time limits, unless the limit is essential | the five-minute seat hold | the hold relies on the essential exception; Encore adds an optional extension |
| 2.5.8 Target Size (Minimum), AA | targets at least 24 by 24 CSS pixels, or spaced to match, or an equivalent control elsewhere | dense seat maps | "choose seats from a list" as the equivalent control |
| 2.5.7 Dragging Movements, AA | anything done by dragging can be done with a single pointer | pan-and-drag seat maps | zoom and pan buttons; the list view |
| 2.4.11 Focus Not Obscured (Minimum), AA | a focused control is never entirely hidden by author content | sticky checkout bars, cookie banners | scroll padding equal to the bar's height; banners that do not cover focus |
| 3.3.7 Redundant Entry, A | information already given in a process is not asked for again | the resale seller flow | ticket details and payout data prefilled from the original order and account |

*Figure 6.3 — The WCAG 2.2 criteria that bear hardest on ticketing, and how Encore meets each.*

Criterion 3.3.8 is often read as a ban on CAPTCHAs. It is narrower than that. It applies to the steps of an *authentication* process, and it allows object-recognition tests at level AA, prohibiting them only at AAA. Encore meets it with passkeys and email links, and by never blocking paste or password managers. Bot screening at checkout is not authentication, so 3.3.8 does not govern it. Other parts of WCAG do, though, and the W3C's note on the inaccessibility of CAPTCHAs is blunt: every interactive test of humanity excludes some humans, and the better alternatives are signals the user never sees, such as heuristics, honeypots, device attestation and anonymous tokens. That is what Encore's Bot Screening already relies on, with silent velocity rules, a challenge only when a session looks suspicious and always a way back. Here the accessibility requirement and the bot defense ask for the same design.

Criterion 2.2.1 is misread in the other direction. Teams assume that a seat hold must be extendable, and that a five-minute limit breaks the criterion. The W3C's own explanatory document uses, as its example of the essential exception, an online ticket site that gives a buyer two minutes to confirm a purchase before the seats return to the pool, because extending the hold for one buyer would defeat the purpose of holding seats fairly when they sell out quickly. Encore's five-minute hold can therefore rely on that exception. What Encore does beyond that is its own design choice. Everything that can happen before the timer starts, the account, a saved payment method and the attendees' names, is moved before it, which the W3C itself recommends. The remaining time is announced through a polite live region, so screen-reader users hear it without being interrupted. And fans who turn on "Extra time" in their profile get one five-minute extension per hold, a setting no fan has to justify.

Criterion 2.5.8 bears on the seat map, whose seats are often far smaller than 24 pixels on a phone. The criterion's equivalent-control exception is the honest route: Encore offers "choose seats from a list", filterable by price, section and accessible features, which builds on the keyboard and screen-reader seat picker the Architecture book described. The Seat Map team treats the list as a full alternative and tests it with the same rigor as the map.

#### Components as accessible contracts {#c6-component-contracts}

At 40 teams, accessibility succeeds or fails in the components. Heydon Pickering's *Inclusive Components* (2019) works through common components one by one, and its method can be summarized as a rule of order: use the native HTML element if one exists, and add Accessible Rich Internet Applications (ARIA) attributes only where HTML cannot express what the component is. The W3C's guidance on ARIA states the same rule first. The WebAIM Million survey of 2026 found that home pages using ARIA had on average 59.1 detected errors, against 42 for pages without it. WebAIM itself cautions that a correlation does not prove cause, but this is the best public evidence we have that ARIA added without care makes pages worse.

Encore's design system, Setlist, therefore specifies each component as an accessible contract: its accessible name, its role, the states it exposes, its keyboard behavior, what happens to focus, and what it announces. Here is the contract for the hold countdown, the component every checkout and resale purchase shows:

```yaml
component: HoldCountdown
element: <div role="timer"> inside a visible "Seats held for you" panel
name: "Time left to complete your purchase"
states: running | extended | expired
announce:                       # via a polite live region, never assertive
  - at 2:00 and 1:00 remaining: "2 minutes left" / "1 minute left"
  - on expiry: "Your seats have been released"
keyboard: "Add 5 minutes" button reachable by Tab, shown only if the
          fan's profile has Extra time and the hold is not yet extended
focus: never moved by the timer; on expiry focus goes to the panel heading
must_not: announce every second; convey state by color alone (WCAG 1.4.1)
tests: unit (states), axe scan in CI, manual screen-reader pass per release
```

The contract tells the component's builders what accessible means, in terms they can test, and tells the 40 teams that consume it what they may rely on. How the design system governs such contracts, and how it checks contributions, is Chapter 7's subject.

#### Testing that finds real barriers {#c6-testing-barriers}

Automated accessibility checkers are valuable and limited, and the most careful public measurement of the limits came from GDS. In February 2017 Mehmet Duran described how GDS built a deliberately inaccessible page with 143 barriers and ran ten automated tools against it. Together the tools found 71% of the barriers; 29% were missed by every tool. The best single tool found 41% when its prompts for manual inspection are counted, and the best tool counting only errors and warnings found 37%. GDS concluded that tools work best when combined with manual testing. The page was synthetic, and a 2021 vendor study by Deque, counting differently, reported 57% of issues by volume for its own tool. The fair summary is that automated tools find somewhere between a third and a half of accessibility problems, depending on how one counts, and that the rest need a person.

The problems they do find remain astonishingly common. The WebAIM Million of 2026 found detectable WCAG failures on 95.9% of the top million home pages, with an average of 56.1 errors per page, both worse than the year before. The six most common failures were low-contrast text, missing alternative text, missing form labels, empty links, empty buttons and a missing document language. Every one is cheap to prevent in a component library.

Encore's release checklist for any fan-facing flow therefore has three layers. Automated scans run in CI on every build and fail it on new violations. Before each release, someone on the team completes the flow with the keyboard alone and with a screen reader, VoiceOver on one platform and TalkBack or NVDA on another. And the monthly usability tests of Section 6.3 include disabled participants, recruited through the research-operations panel and disability organizations, paid like everyone else and testing on their own devices with their own assistive technology. The resale buy flow's first test with two screen-reader users found that the "Verified" badge was announced only as "badge, image", which no automated check had flagged, because the image did have alternative text. Native mobile accessibility, with Dynamic Type and the platform screen readers, has its own practice, which Section 8.5 takes up.

#### Accessibility beyond the screen {#c6-beyond-the-screen}

Some accessibility decisions in ticketing are not about interfaces at all. Accessible seats, wheelchair spaces and companion seats are a limited inventory with rules about who may buy them, and resale puts those rules under pressure: an accessible seat resold to a fan who does not need it is a seat lost to one who does. That is a product rule, enforced in the resale rules engine.

No EU law sets rules for selling accessible seats, so Encore had to choose its own, and it borrowed from the best-proven public model. Since 2011 the US Department of Justice's regulations under the Americans with Disabilities Act (ADA), at 28 CFR 36.302(f), "Ticketing", have required that people with disabilities can buy accessible seats through the same channels, at the same times and on the same terms as everyone else. Paragraph (f)(8) forbids sellers to demand proof of disability, such as a doctor's note; for single-event tickets a seller may ask only whether the buyer has a disability that requires the seat's accessible features, or is buying for someone who does. Paragraph (f)(7) reaches into the secondary market: a person with a disability who has bought an ordinary seat on resale must be allowed to exchange it for an accessible one, if one is vacant when they arrive.

Encore's rule follows that template, adapted to European law. Accessible-seat tickets may be listed on resale like any other, but they are sold only to buyers who attest, with a single checkbox, that they or someone in their party need the seat's features. Encore collects no proof of any kind, because evidence of disability is health data, special-category data under GDPR Article 9, and Encore has no lawful need to hold it. Organizers may honor the venue's own process at the gate, where a steward can help a fan who has bought the wrong kind of seat. The checkbox is an honor system, and it will sometimes be abused; the alternative, a proof-of-disability process, would be abused less and would humiliate and exclude far more people. The rule was drafted with disability organizations in two of Encore's markets, and the rules engine applies it to every listing, whichever partner it comes through.

#### Owning it {#c6-owning-it}

The EAA requires a provider to own accessibility in three ways. Article 13(2) and Annex V require the provider to publish information on how the service meets the accessibility requirements in the general terms and conditions or an equivalent document, in written and oral form, and in an accessible format. The formal "accessibility statement" many teams know is a requirement of the Web Accessibility Directive for public bodies; under the EAA, most providers meet the Annex V duty with an accessibility page linked from their terms, and Encore does the same. Article 13(3) requires procedures that keep the service conforming as it changes. And Article 13(4) requires a provider that finds its service non-conforming to correct it and to inform the national authorities immediately.

That last duty is why Encore triages accessibility defects with the same machinery as security bugs: a severity scale, a response time for each level, and a named owner. The owner of each fan-facing product's accessibility is its product manager, supported by an accessibility lead in the Design System team. Treating a keyboard trap in checkout as a P1, fixed before the next on-sale, is Encore's own policy and goes beyond anything the Act prescribes. For a fan shut out of a sale that lasts minutes, a keyboard trap is an outage.

**Recap.** The EAA covers Encore's consumer services, leaves the organizer console to Encore's own policy, exempts only microenterprises, and offers no presumption of conformity until EN 301 549 V4.1.1 is cited. The criteria that hit ticketing hardest are often misread: 3.3.8 governs login, and a seat hold can rely on 2.2.1's essential exception. Accessibility lives in component contracts, is tested by tools and people together, reaches into product rules, and needs a named owner.

**Exercise 6.4.** Complete one purchase on your own product with the keyboard alone and then with a screen reader. File every barrier you meet against the WCAG criterion it breaks, and say which of them an automated scan in your CI would have caught.

### 6.5 Designing AI Features

#### Whether AI belongs here {#c6-whether-ai}

Verified Resale has one AI feature, and the trio argued about whether it should have any. Google's People + AI Research (PAIR) group published the *People + AI Guidebook* in 2019, with a second edition in 2021, and its first chapter asks exactly this: start from the user's need, and determine whether AI adds value there. It advises rules where the problem is well defined and errors costly, and choosing between **automation**, in which the system does the task, and **augmentation**, in which it helps a person do the task, according to the cost of being wrong. The Operations book's Section 3.4 teaches the older human-factors lineage of this idea, levels of automation, for the people who run systems.

Applied to Verified Resale, the guidance gave a clear answer for most of the product. The price cap, the fee split, the five fairness invariants and the eligibility of a ticket for resale are all rules, typed configuration enforced by the Resale service, and none of them involves a model. A wrong answer there would break a promise Encore made to fans and organizers.

What the trio found in discovery was a different kind of difficulty. Organizers know what they want, and they say it in their own words: "no resale until a week after the on-sale, and two per fan", or "let people resell until the day before, but nothing for the VIP packages". Translating that into the console's settings is a small act of programming that organizers do a few times a year, and in the first organizer rounds of usability testing they often set rules that did not match what they had just said they wanted. That is a translation problem with a human check at the end, and it is where a language model helps. So the **organizer rule assistant** works like this. The organizer writes a request in plain language. The assistant drafts a typed rule set and a plain-language summary of it. The organizer reviews the draft and confirms it, and nothing applies until they do. It runs through Encore's AI gateway, and the Resale team owns it. It can produce only rules that the rule types allow, and those types can express only tightening, so invariant 3, that organizer caps and rules can only tighten, holds whatever the model says.

#### Guidelines with evidence {#c6-guidelines}

Most advice on AI interaction design has never been tested. One set has. In 2019, Saleema Amershi and twelve colleagues, most of them at Microsoft, published "Guidelines for Human-AI Interaction" at CHI. They distilled 18 guidelines from more than 150 AI-related design recommendations, then evaluated them in several rounds, including a study in which 49 design practitioners tested them against 20 popular AI-infused products. Microsoft's HAX Toolkit turns them into working materials. Together with the PAIR Guidebook they are the proven core of the subject, and newer patterns should be labeled as such until they acquire comparable evidence.

Five of Amershi's guidelines shaped the rule assistant directly. G1, make clear what the system can do: the assistant's input box says "Describe your resale rules, for example a start date, an end date or a per-fan limit", and lists what it cannot do, which includes changing fees or raising the cap. G2, make clear how well the system can do what it can do: the same box says that drafts must be checked, and the confirmation screen marks every value the assistant had to assume. G9, support efficient correction: every field of the draft is editable in place. G10, scope services when in doubt: when a request is ambiguous, the assistant asks one question before it drafts anything. G11, make clear why the system did what it did: each rule in the draft is shown beside the phrase of the request that produced it.

#### Setting expectations and calibrating trust {#c6-calibrating-trust}

The deepest problem with an AI assistant whose output a person confirms is that people confirm. Raja Parasuraman and Dietrich Manzey reviewed decades of research on this in 2010, under the name **automation bias**: the tendency to accept an automated recommendation without the scrutiny the person would apply to the same information from elsewhere. It produces errors of omission and of commission. It affects experts as much as novices, and neither training nor instructions remove it. For the rule assistant the consequence is plain: the organizer's confirmation is a safeguard only if the confirmation screen makes errors visible, because otherwise the organizer will do what the Hawaii warning officer and the three people at Citibank did, and approve what they believe they asked for.

So the confirmation screen is designed to be read. Its summary is rendered from the typed rules by the console's own templates, so the plain-language summary always says exactly what the rules do, and the model cannot describe one thing while drafting another. Every changed value is highlighted, with the old value beside it. Consequences are stated in dates and numbers, "Resale opens Friday 12 June at 10:00 and closes Saturday 4 July at 18:00", never in the organizer's own wording echoed back, which would confirm whatever the organizer meant rather than what the rules say. And the assistant shows confidence only where it changes what the organizer should do: a draft that rests on an assumption, such as which time zone "the day before" refers to, flags that assumption on the field. Asked for a suggestion, the assistant proposes rules based only on that organizer's own past events, and lists them. It never draws on other organizers' sales data, which would leak velocity, a quantity Encore keeps confidential.

The trio wrote down what each kind of error would cost before the first prompt was written. Figure 6.4 is that table.

| Assistant error | Example | Cost if it reaches an event | Control after the error |
|---|---|---|---|
| Rule stricter than intended | "two per fan" drafted as one per fan | fans who could have resold cannot; support contacts | highlighted on the confirmation screen; edit in place; rule history with one-step revert |
| Rule looser than intended, within the defaults | window left at the default, two hours before doors, instead of the day before | resale continues longer than the organizer wanted | as above; organizer can tighten at any time |
| Rule outside what the organizer may set | a cap above face value, a change to the fee split | none: such rules cannot be expressed in the rule types | not needed; the request is answered with what is not allowed |
| Request misunderstood entirely | a rule for the wrong event or ticket type | wrong event's rules changed | the event name is the confirmation screen's heading; nothing applies without confirmation |
| No draft at all | the model times out or the gateway sheds it | the organizer edits the rules by hand | the manual editor is always one tap away |

*Figure 6.4 — The rule assistant's error-cost table. The third row is why the assistant is safe to build at all.*

The draft the assistant produces is ordinary typed configuration. For the festival promoter's request, "no resale until a week after the on-sale, two per fan, nothing for VIP", it looks like this:

```json
{
  "event_id": "evt_8812",
  "resale_enabled": true,
  "window": { "opens": "onsale+P7D", "closes": "doors-PT2H" },
  "per_fan_listing_limit": 2,
  "per_fan_buying_limit": 2,
  "excluded_ticket_types": ["vip_package"],
  "price_cap": "face_value",
  "assumptions": ["closing time not stated; kept the default of 2 hours before doors"],
  "source_spans": { "window.opens": "a week after the on-sale",
                    "per_fan_listing_limit": "two per fan",
                    "excluded_ticket_types": "nothing for VIP" }
}
```

Nothing in it is new to the Resale service. The schema that validates it is the same schema the manual editor writes, and a request to raise the cap or change the fee has no field to land in.

#### Control, undo and graceful failure {#c6-graceful-failure}

An AI feature will be wrong, and its design is mostly the design of what happens next. The PAIR Guidebook and Amershi's guidelines G8 to G10 agree that a person should be able to accept, edit, reject or dismiss what the system proposes, and should always have a path forward when it fails. The Architecture book's Section 8.5 made the matching architectural point, that actions an AI proposes should come with a visible undo. For the rule assistant, the path forward is the manual editor, which never goes away, and the undo is the rule history, from which any earlier rule set can be restored in one step.

The harder case is an assistant that speaks to fans, because what it says can become a promise. In *Moffatt v. Air Canada*, decided by the British Columbia Civil Resolution Tribunal on 14 February 2024, Air Canada's website chatbot had told a grieving customer that he could claim a bereavement fare after travel, contradicting the airline's own policy page. Air Canada argued that the chatbot was responsible for its own statements. The tribunal rejected the argument, held the airline liable for negligent misrepresentation and awarded about C$650 in damages, plus interest and fees. The sum was small, but the principle reaches every company with an assistant: it owns what the assistant says.

Encore's support assistant, run by the Support Experience team, already answers fans' questions, and Verified Resale gives it new ones, the commonest being "why was my listing rejected?". The design takes the tribunal's principle literally. The assistant never decides or states eligibility from its own reading of the policy. It asks the resale rules engine why the listing was rejected and explains the engine's answer, citing the rule, such as "the organizer's resale window for this show closed on 3 July". Questions about fees, payouts or refunds are likewise answered from the systems of record, and a fan who is not satisfied reaches a person with one tap, the conversation carried along.

#### Feedback that teaches {#c6-feedback}

The last design question is what the product learns from use. Chip Huyen's *AI Engineering* (2025) gives a useful taxonomy. **Explicit feedback**, such as thumbs, ratings and comments, is easy to interpret and sparse, and it skews toward complaints, because satisfied people rarely bother. **Implicit feedback**, the signals people give by what they do, such as abandoning, regenerating or editing a response, is plentiful and ambiguous. The practical rule is to design both before launch, and to decide who reads them and how they reach the evaluation set.

For the rule assistant, the richest implicit signal is the organizer's edits. A draft confirmed unchanged is weak evidence that it was right. A draft whose per-fan limit the organizer changed from one to two is strong evidence that something was misread. Every such edit is logged with the original request, and the trio reviews a sample each week. Misreadings that recur become new cases in the assistant's golden set of organizer requests, labeled by an organizer-success lead, and those cases run on every change to the prompt or the model. How such evals are designed, and how they gate the build, is the Software book's Section 3.5; how they run in production belongs to the Resilience book's Section 8.3. The design question for this chapter is narrower and comes first: who will read each kind of feedback, named before launch.

**Recap.** An AI feature belongs where it helps people with a task whose errors are cheap to catch, and nowhere a rule would do. Because people confirm what they believe they asked for, the confirmation screen must make errors visible, the error-cost table must be written before the prompt, and the type system must make the worst errors impossible. A company owns what its assistant says, so answers about eligibility and money come from the systems of record, and feedback is designed as data with a named consumer.

**Exercise 6.5.** For one AI feature you know, write the error-cost table: each kind of error, an example, what it costs if it reaches a user, and the control the user has after it. Then mark the rows that a type, a rule or a schema could make impossible.

### Kata: The Replacement Bus

> **Your brief: "Ploverwick."** Ploverwick sells regional public-transport tickets in six EU countries, on behalf of the bus and rail operators of about 40 regions, with 60 engineers in seven teams. Riders plan journeys and buy mobile tickets in Ploverwick's app and on the web, about 90 million tickets a year, and some regional express trains also sell reserved seats. About 2,000 ticket inspectors check those tickets on Ploverwick's handheld inspection app through whole shifts. When a line is disrupted, riders must be re-planned onto replacement buses or later trains, and their tickets honored there. Today riders who try to re-plan themselves meet a reserved seat held for three minutes and an image CAPTCHA on login added after a bot attack last spring, while inspectors on the replacement services cannot see which tickets the disruption made valid and settle each case by conversation, one rider at a time. Ploverwick already has an AI trip assistant that answers riders' questions, and product wants it to suggest replacement journeys to riders and to tell inspectors which tickets a disruption has made valid. Assume that a rider buying a mobile ticket concludes a consumer contract, which brings the rider app under the European Accessibility Act as an e-commerce service; a transport authority's own public-sector app might instead fall under the Web Accessibility Directive, and the inspection app is outside the EAA altogether.

**Deliverables:**

1. **Two postures** — Redesign re-planning after a disruption twice: once for the rider (transient, on a phone, often standing on a platform) and once for the inspector (sovereign, checking a full replacement bus in the minutes between stops). Name one idiom each must not borrow from the other.
2. **The gulfs** — Walk the rider's current re-planning flow through the seven stages of action. Mark each gulf of execution and evaluation, say whether the errors it produces are slips or mistakes, and show the change that closes each one.
3. **A test plan** — Write the script for two three-person rounds, one with riders (including at least one screen-reader user) and one with inspectors, in the form of Section 6.3. Say how you will recruit inspectors without their supervisors present, and how you will hold participant data under the GDPR.
4. **Accessibility scoping and criteria** — State which of Ploverwick's surfaces the EAA covers and why, and what standard you will hold the rest to. Then resolve the three-minute seat hold under criterion 2.2.1 and the login CAPTCHA under criterion 3.3.8, saying for each whether the law requires a change and what you will change regardless. Write one component contract for the seat hold, in the form of Section 6.4.
5. **The AI trip assistant** — Decide whether it should automate or augment for riders and for inspectors, write its error-cost table in the form of Figure 6.4, and say which errors your design makes impossible rather than merely unlikely, including whether ticket validity should come from the assistant at all. Name the feedback signals and who reads them.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Posture | Would an inspector checking 40 riders on a replacement bus and a rider re-planning one journey each find their version fast, without either carrying the other's idioms? |
| Evidence before opinion | Does every design claim trace to a test you would run, a criterion you would meet or a case you can cite? |
| Legal precision | Have you scoped the EAA correctly, including the inspection app and the public-sector case, and read 2.2.1 and 3.3.8 as they are written? |
| Accessibility in the components | Is accessibility specified in contracts and tested by tools, people and disabled participants from the first build? |
| Error design for AI | Is the error-cost table written before the feature, and do the worst errors, such as a rider fined for a ticket the assistant called valid, have no path to a rider? |
| Ownership | Is there a named owner for accessibility and for the AI feature's feedback, with a response time for defects? |

#### Where you now stand

You can now read an interface the way Norman taught us to, find the gulfs in it before users fall into them, and test the design every month cheaply enough that the habit survives. You can choose idioms by posture, make accessibility a requirement that teams can engineer and test, with the law stated exactly, and design an AI feature whose errors are written down before its prompt and whose worst errors cannot happen at all. But the "Verified" badge, the capped price field, the cancelled-ticket state and the hold countdown must look and behave the same on every screen that shows them, built once and maintained by someone. That is the work of a design system, and of a frontend codebase that 40 teams can share without stepping on each other. Chapter 7 takes it up, beginning with a binder of signage standards that once let many crews sign a city's subway as one.

### References

- Jonathan N. Wand, Kenneth W. Shotts, Jasjeet S. Sekhon, Walter R. Mebane Jr., Michael C. Herron, Henry E. Brady — [*The Butterfly Did It: The Aberrant Vote for Buchanan in Palm Beach County, Florida*](https://websites.umich.edu/~wmebane/butterfly.pdf). *American Political Science Review* 95(4), 2001 — free online.
- Don Norman — *The Design of Everyday Things*, revised and expanded edition. Basic Books, 2013.
- W3C — [*Web Content Accessibility Guidelines (WCAG) 2.2*](https://www.w3.org/TR/WCAG22/). W3C Recommendation, 2023, updated 2024 — free online.
- European Parliament and Council — [*Directive (EU) 2019/882 on the accessibility requirements for products and services*](https://eur-lex.europa.eu/eli/dir/2019/882/oj). Official Journal L 151, 2019 — free online.
- ETSI, CEN and CENELEC — [*EN 301 549 V4.1.1: Accessibility requirements for ICT products and services*](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/). ETSI, 2026 — free online.
- Saleema Amershi et al. — [*Guidelines for Human-AI Interaction*](https://doi.org/10.1145/3290605.3300233). Proceedings of CHI 2019, ACM, 2019.
- Steve Krug — *Don't Make Me Think, Revisited*, 3rd ed. New Riders, 2014; and *Rocket Surgery Made Easy*. New Riders, 2010.
- Alan Cooper, Robert Reimann, David Cronin, Christopher Noessel — *About Face: The Essentials of Interaction Design*, 4th ed. Wiley, 2014.
- Heydon Pickering — [*Inclusive Components*](https://inclusive-components.design/). Smashing Media, 2019.
- Jakob Nielsen, Thomas K. Landauer — [*A Mathematical Model of the Finding of Usability Problems*](https://doi.org/10.1145/169059.169166). Proceedings of INTERCHI '93, ACM, 1993.
- Laura Faulkner — [*Beyond the Five-User Assumption*](https://doi.org/10.3758/BF03195514). *Behavior Research Methods, Instruments, & Computers* 35(3), 2003.
- Google PAIR — [*People + AI Guidebook*, 2nd ed.](https://pair.withgoogle.com/guidebook/) Google, 2021 — free online.
- Raja Parasuraman, Dietrich H. Manzey — [*Complacency and Bias in Human Use of Automation: An Attentional Integration*](https://doi.org/10.1177/0018720810376055). *Human Factors* 52(3), 2010.
- WebAIM — [*The WebAIM Million*](https://webaim.org/projects/million/). WebAIM, 2026 — free online.
- Mehmet Duran — [*What we found when we tested tools on the world's least-accessible webpage*](https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/). GOV.UK Accessibility blog, 2017 — free online.
- Chip Huyen — [*AI Engineering: Building Applications with Foundation Models*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/). O'Reilly, 2025.

---

## Chapter 7: Design Systems and the Frontend at Scale — One Product from Forty Teams {#ch7}

> Consistency is not something a product has. It is work that somebody keeps doing.

A fan who buys a ticket from Encore passes through screens built by perhaps a dozen teams. The event page belongs to Fan Discovery, the seat map to the Seat Map team, checkout to the Checkout team and the ticket in the app to Mobile App, while the hold timer on the screen counts down a hold that the Inventory team keeps. The fan sees none of those seams, or should not. To the fan there is one product, with one way of showing a price, one way of saying that something went wrong and one button that means "continue". Behind the screen, that single product is the joint work of 40 teams who plan separately, ship separately and are measured separately. The question of this chapter is how such an organization keeps its product whole, and how it keeps doing so as fast as each team wants to move, in every language its customers read.

Our touchstone is a binder. In 1970 the New York City Transit Authority issued the *Graphics Standards Manual* that Massimo Vignelli and Bob Noorda of Unimark International had designed for the subway. It specified how every sign in the system should be built and lettered, so that a passenger changing trains under three formerly separate companies' stations would read one system. What makes it useful to us is the less celebrated part of its history. A first proposal was built badly by people who had never been told how to build it, the manual itself was applied piecemeal for two decades, and the subway became coherent only when someone was finally paid to maintain the standard and migrate the stations to it. Every lesson of a modern design system is in that story, including the uncomfortable one: publishing the standard was the easy part.

Encore, at about 400 engineers, runs one design system, which it calls **Setlist**: tokens, tenant themes and accessible components, owned by the Design System team. The fan storefront is still the modular monolith the Architecture book chose, and the organizer console, which that book left as one separate application, has since become a shell with six remotes that load at runtime. Verified Resale now arrives with needs of its own. It needs new shared patterns, among them a "Verified" badge, a price breakdown that shows face value, fee and total, and a status for a ticket being reissued. It needs a resale page that sees a crowd the moment an on-sale sells out. And it needs prices, fees and dates that are correct, and lawful, in every language and market an organizer sells into, beginning with France at launch.

### 7.1 Design Systems

#### The binder at Bergen Street {#c7-graphics-standards-manual}

By the 1960s New York's subway was three systems wearing one name. The Interborough Rapid Transit (IRT), the Brooklyn–Manhattan Transit (BMT) and the city-owned Independent (IND) had been unified under city ownership in 1940, but each still signed its stations in its own manner, and the oldest signs were the ceramic mosaic tablets of 1904, made with no common typeface, no arrows and no borders. When the Chrystie Street Connection opened in November 1967 and joined IND and BMT services, the confusion became a public complaint. The Transit Authority had already engaged Unimark in 1966. Bob Noorda, who had designed the signage for Milan's first Metropolitana line, studied how passengers actually moved through the stations, and Unimark delivered a proposal.

What happened next is the part of the story a design-system team should read twice. According to Paul Shaw's history of the episode, the Authority thanked the designers and then, as far as anyone can tell, put the proposal away. Its own sign shop at Bergen Street began making signs from the proposal without instruction from the designers and without their inspection, and the result was a muddle that Vignelli himself described, by Shaw's account, as "the biggest mess in the world". The Authority rehired Unimark in 1968, and in 1970 it issued the *Graphics Standards Manual*: a binder of precise rules for modular sign panels built from one-foot units, for letter spacing, word spacing and line counts, for arrows and route symbols, and for a black band across the top of each sign. The band began as a way of hiding the black metal channels from which the signs hung, because the stations could not be rebuilt to suit the designers; the manual turned that constraint into a rule of the graphic language. The typeface was Standard Medium, the American name for Akzidenz-Grotesk. Legend gives the subway Helvetica from the start, but Shaw's research suggests that Helvetica, which Vignelli preferred, was simply not available to the sign shop, although he is candid that he cannot prove the reason.

Then came the drift. Around 1973 the signs were switched from black-on-white to white-on-black to resist graffiti. New signs went up beside decades-old ones from the three former companies, hand-lettered cardboard signs filled the gaps, and through the city's fiscal crisis the standard was applied wherever someone happened to have money and attention, which was not often. Writing in the *New York Times* in 1979, the architecture critic Paul Goldberger judged the signs so confusing that "one is tempted to wish they were not there at all". In December 1989 the Metropolitan Transportation Authority (MTA) made Helvetica its official typeface and hired Michael Hertz Associates to update the manual across its agencies, and the capital programs of the 1990s finally put a coherent system into the stations. The manual had an afterlife. A copy turned up in 2012 in the basement of Pentagram's New York office, two of its designers, Jesse Reed and Hamish Smyth, licensed a full reissue from the MTA, and their 2014 Kickstarter raised $802,812 from about 6,700 backers.

Figure 7.1 reads the manual as a design system, and it is worth reading in that direction, because almost everything we will say in this chapter about Setlist has a counterpart in the binder.

| In the 1970 manual | In a design system | At Encore |
|---|---|---|
| Typeface, black band, colored route discs | Tokens: named values for type, color and space | Setlist's token files and tenant themes |
| Modular panels in one-foot units | Components built from a shared grid | `Button`, `PriceBreakdown`, `SeatLegend` |
| Rules for spacing, arrows and placement | Usage guidance and patterns | The living pattern library |
| Bergen Street building from an uninstructed proposal | Teams building from a standard without guidance or review | The contribution path (Section 7.2) |
| Twenty years of piecemeal application | Version skew and abandoned migrations | The version dashboard and codemods |
| Standard Medium because the shop could make it | Tokens limited to what the platform can render | Tokens checked against what browsers and apps support |

*Figure 7.1 — The Graphics Standards Manual read as a design system. The binder had every part a modern system has; what it lacked for two decades was an owner with the mandate and budget to keep the stations on it.*

The story bears on this chapter in more than one way. A standard of this kind is a design system in every sense that matters, because it consists of named decisions, reusable parts and rules for combining them. Yet a standard is adopted only when the people who build from it are instructed and their work reviewed. The Bergen Street signs failed for want of both, and that is the problem of contribution and governance that Section 7.2 takes up. And a system that nobody maintains drifts one sign at a time, each departure defensible on the day it is made, until the whole has lost the coherence that was its reason for existing. The analogy with signage breaks in one place, and it breaks in our favor. A station sign is metal bolted to a wall and costs a crew a night to replace. A component in a design system can be replaced in every product that uses it by a release and an automated migration, so the two decades the subway needed can be shortened, for us, to the time it takes to run a well-planned migration.

#### From pages to systems {#c7-pages-to-systems}

A **design system** is the set of named decisions, reusable components and usage rules from which a product's interfaces are built, maintained by an owner as a product in its own right. The Architecture book's Section 8.2 introduced it as the frontend's shared kernel and warned that it must stay thin. This chapter takes that as settled and asks how such a thing is built and kept.

The most widely used way of thinking about the parts is Brad Frost's *atomic design*, first sketched on his blog in 2013 and set out in his book of 2016. Frost borrowed from chemistry. Atoms are the smallest useful pieces, such as a button; molecules are small groups of atoms that do one thing together, such as a search field with its button; organisms are larger sections, such as a list of resale offers. Templates arrange organisms into a layout, and pages fill templates with real content, which is where we find out whether the system works. Frost is careful to present this as a mental model, and it is best used that way. Teams that file every component into exactly one drawer end up arguing about whether a date picker is a molecule or an organism. Teams that use the hierarchy as a habit of mind gain something more valuable, which is the instinct to design "systems, not pages", as Frost puts it: to ask of every new screen what it is made of, and which of those parts already exist.

This is the oldest tool we have for mastering complexity, applied to pixels. Decomposition breaks the interface into parts small enough to reason about, abstraction lets a team use a `PriceBreakdown` without knowing how its alignment is computed, and hierarchy lets us see the whole at whichever level of detail the question needs. The GOV.UK Design System, the British government's public system, is a good public example of the hierarchy in practice: it publishes styles, components and patterns as separate layers, so that a team building a new service can see at a glance whether it needs a color, a button or a whole way of asking a citizen for their address. Encore's Setlist follows the same layering.

#### The interface inventory {#c7-interface-inventory}

Before a design system is built, someone usually has to prove it is needed, and the best proof is embarrassingly simple. Frost called it the **interface inventory**: a systematic collection of screenshots of every instance of each kind of interface element in a product, sorted by kind, so that its inconsistency becomes visible at a glance. He described it on his blog in 2013. The method is to capture every button, form field, error message and modal, group them by type in one document, and show the result to the people who pay for the product.

Encore did this at 70 engineers, in its fourth year, when the storefront and the organizer portal had been built by nine teams in a hurry. The inventory found 23 distinct button styles. Some differed in color, some in corner radius, some in the wording of the same action ("Continue", "Next", "Proceed to payment"), and two were nearly identical except that one had been copied from an older screen before a contrast fix was applied to the original. No one had chosen 23 buttons. Each had been a reasonable local decision, made by someone who could not see the other 22, which is the subway's drift in miniature. The inventory did what no argument about efficiency had managed: it turned an abstract cost into a page that a product director could look at for 30 seconds and understand. That page is why Setlist exists, and it is still shown to every engineer who joins the Design System team.

#### Tokens as named decisions {#c7-tokens}

The smallest parts of a design system are values: a color, a spacing step, a type size, a shadow, a corner radius. Adam Wathan and Steve Schoger, in *Refactoring UI* (2018), make the case that these should come from a deliberately constrained scale, a handful of spacing steps and a handful of type sizes chosen in advance, so that each new screen picks from the scale. Constraint here is a gift. A designer choosing between 16 and 24 pixels makes a better decision faster than one choosing among every integer, and a product built from eight spacing steps has a visible rhythm that a product built from 40 does not.

A **design token** is such a value given a name that records a decision, shared by design tools and code so that both draw from the same source. The term came from Salesforce, where Jon Levine and Jina Anne used it around 2014; the repository for Salesforce's token tool, Theo, dates from February of that year. The idea's strength is the name. `color.action.primary` says what the color is for, which is a decision, while `#D9482B` says only what it is. When the brand changes, or a tenant wants its own color, or the contrast rules tighten, the decision can be changed in one place and every component that used the name follows. It is a small irony that Salesforce has since moved its own system from token files to custom properties in Cascading Style Sheets (CSS): the concept outlived its first implementation, which is a fair sign that the concept was the valuable part.

For most of the decade each tool had its own token format, and moving tokens between a design tool and a build pipeline meant writing translators. That changed on 28 October 2025, when the Design Tokens Community Group published the first stable version of its format, 2025.10, in three modules: Format, Color and Resolver. The status is worth stating precisely. It is a Final Community Group Report of a group hosted by the World Wide Web Consortium (W3C), and it is not a W3C standard nor on the W3C standards track, but its editors declare it stable, and the group lists design tools such as Figma, Penpot and Sketch and token pipelines such as Style Dictionary among its adopters. Setlist's tokens are written in that format. A fragment shows the shape: a base color, a decision that refers to it, and a tenant theme that overrides the decision.

```json
{
  "color": {
    "vermilion": { "$type": "color",
      "$value": { "colorSpace": "srgb", "components": [0.851, 0.282, 0.169], "hex": "#d9482b" } },
    "action": {
      "primary": { "$type": "color", "$value": "{color.vermilion}",
        "$description": "Primary call to action. Must reach 4.5:1 on surface.default." }
    }
  }
}
```

The Resolver module matters more to Encore than the format itself, because it formalizes a base set of tokens plus modifiers that apply in a given context. That is exactly what a tenant theme is: the `venue-chain-a` storefront at `tickets.venuechain.com` resolves `color.action.primary` to the chain's own color, and everything else follows. Dark mode and a high-contrast mode are modifiers of the same kind, which is why Setlist builds them on the same mechanism and checks every resolved combination against the contrast rules of Section 6.4. Where the theme is stored, and how a tenant's configuration is rolled out, belongs to the Software book's Section 7.3; here the point is that a theme is data on top of named decisions, so a tenant can never choose a value the system has not anticipated.

#### Function, feel and names {#c7-function-feel-names}

Alla Kholmatova's *Design Systems* (2017) offers a distinction that helps a team decide what to document and how. **Functional patterns** are the tangible parts of the interface, defined by what they let people do: a seat picker, a price breakdown, a countdown. **Perceptual patterns** are the qualities that make a product feel like itself across all of those parts: its tone of voice, its use of motion, its color and its density. The two need different kinds of documentation. A functional pattern can be specified as a component with properties and states. A perceptual pattern lives in principles and examples, and it is learned more than looked up. Kholmatova's framework is one author's lens, untested in any formal sense, but it explains a common failure well. Teams that document only functional patterns end up with a consistent set of components that still produce screens which feel unrelated, because nobody wrote down how Encore speaks to a fan who has just lost a seat.

Kholmatova's other argument concerns names. She holds that a shared language does more to prevent duplication than any tool, because two teams that call the same thing by two names will build it twice, and her remedy is to name patterns by their purpose, with designers and engineers settling the names together. That is her argument, and nobody has measured it, but anyone who has searched a component library for the thing they need and failed to find it under the name they expected will recognize the problem. Encore applied the practice to Verified Resale. The resale trio and the Design System team held one naming session for the new patterns and agreed three names. `VerifiedBadge` marks a listing whose ticket will be reissued by Encore. `ReissueStatus` shows the fan where a reissue stands, from "sold" through "new ticket issued" to "in your wallet". `PriceBreakdown` already existed for primary checkout and gained an optional line for the resale cap.

The third name hides an architectural decision that is easy to get wrong. The early sketches proposed a new component called "price with cap", and the first prototype computed the cap from the face value it was given. That is business logic in the kernel, the failure the Architecture book's Section 8.2 warns against: the moment an organizer sets a lower cap, or Irish law bounds the buyer's total, the component would have to change with the business, and every team using it would wait for the Design System team's release. So the teams extended `PriceBreakdown` instead. It displays a face value, a fee and a total that it is given, and the Resale service computes them. The component knows how to show a capped price legibly and accessibly; it does not know what a cap is.

**Recap.** The 1970 *Graphics Standards Manual* had every part of a modern design system, and its history shows that a standard without instruction, review and maintenance drifts one sign at a time. A design system decomposes the interface into a hierarchy of parts, proves its necessity with an inventory, encodes its decisions as named tokens in a now-stable shared format, and names its patterns by purpose. It displays what the business computes and keeps the computing out.

**Exercise 7.1.** Choose one kind of element in your product, such as buttons or error messages, and inventory every instance across the product. Count the variants, and for each variant beyond the first, find out whether anyone chose it on purpose.

### 7.2 Running a Design System as a Product

#### Its users are teams {#c7-users-are-teams}

A design system is an internal product, and it fails in the ways internal products fail. Its users are designers and frontend engineers in other teams. They have deadlines and an alternative, which is to build the thing themselves. Everything Part I of this book said about deciding what to build applies, pointed inward: the Design System team needs a roadmap tied to the problems of the teams it serves, regular research with those teams, a support channel that answers within a day, and a measure of whether its product is being used. The Software book's Chapter 6 treats internal platforms as products, and its Section 6.4 on adoption applies here unchanged. What is particular to a design system is the measure of use and the way its users contribute back.

The measure is **adoption**: the share of a product's interface that is drawn by the design system's components and tokens, as opposed to local code. Pinterest published an unusually honest account of how its design systems team measures this for its Gestalt library. A nightly job scans the team's design files, counting only files edited in the previous two weeks and only pages marked as ready for handoff to engineering, and computes the share of layers that come from the library; in Pinterest's worked example, seven of 15 layers came from Gestalt, a little under half. Adoption varied from about half on some teams to 2% on others. The team's conclusion was that adoption begins in the design phase, before any code exists, which is why it measures the design files. On the code side, practitioner guides recommend a different count: for each component, the number of products that use it at all, gathered by scanning imports, because raw instance counts reward a team for drawing one button many times.

Setlist measures both. A nightly scan of the storefront and the console counts the interactive elements rendered by Setlist components as a share of all interactive elements, per surface and per team, and a weekly scan of design files does the same for screens in progress. The figures at the start of the resale work were 86% on the fan storefront and 71% on the organizer console, with the Festivals remote furthest behind at 44%, because it had inherited components from the festival app integration years before Setlist existed. The figure that matters most is the lowest one, because it tells the Design System team where its product is failing its users. When they asked the Festivals team why, the answer was not resistance. Setlist had no component for a multi-day pass selector, and the Festivals team had stopped asking after their first request sat in a queue for a quarter.

#### Governance {#c7-governance}

Every design system must answer who decides what goes into it, and the answers fall into a small number of shapes. Nathan Curtis of EightShapes named three team models in 2015. In a **solitary** model, one product team builds a system for its own needs and makes it available to others, who take it as it is. In a **centralized** model, a dedicated team owns the system and serves everyone. In a **federated** model, designers and engineers from several product teams build and maintain the system together, without a dedicated team. Kholmatova adds three dimensions along which any system can be placed: strict or loose in how far teams may depart from it, modular or integrated in how freely its parts combine, and centralized or distributed in who maintains it. Figure 7.2 sets the models side by side.

| Model | Who builds it | Strength | Typical failure |
|---|---|---|---|
| Solitary | One product team, for itself | Fast start, real use from day one | Serves its owner's needs; others fork it |
| Centralized | A dedicated team | Coherence, quality, accessibility done once | Becomes a queue every team waits in |
| Federated | Contributors from product teams | Patterns come from real work | No one has time to say no; quality drifts |
| Core plus federated contributors | A small dedicated core, with contributions reviewed by it | Coherence with a path for teams to add what they need | Needs a contribution path people actually use |

*Figure 7.2 — Design-system team models, after Nathan Curtis (2015). Most large systems settle on the last row; the work is in making its contribution path real.*

Few large organizations end up in a pure form. Curtis's own follow-up in 2016 described Salesforce running a central core team with federated contributors from product teams, and that hybrid is the model Encore uses. The Design System team, six engineers and three designers, owns tokens, the core components, accessibility, documentation and releases. Setlist is strict about tokens and accessibility, where departures harm fans, and looser about layout, where a sovereign tool like the organizer console legitimately needs density that a transient fan flow does not. The model has a known weakness, which the Festivals story illustrates: a central core becomes a queue. The defense is to make contribution the normal way that a missing pattern gets built, so that a team that needs a pass selector builds it and brings it to the core.

#### The path from local to shared {#c7-contribution}

A **contribution path** is the defined sequence of steps by which a component built by one team for its own needs becomes part of the shared system. The best public model is the GOV.UK Design System's contribution criteria. A proposal must first show that the pattern is useful, meaning there is evidence that services need it, and unique, meaning nothing already in the system serves the purpose. Before publication, the implementation must be usable, with research showing that it works for people; consistent with the rest of the system; and versatile enough to serve more than the service that proposed it. The criteria are short, public and applied by a named team, and that combination is what makes them work. A contributor knows in advance what will be asked.

Encore's path follows the same shape, with one step added before the first. Most new patterns begin as **pattern candidates**: components that one team builds in its own code, in Setlist's style, and registers in the library as candidates. A candidate is visible to every team but owned by the team that made it, and it carries no promise of support. If a second team needs it, the two teams and the core review it against Setlist's criteria: useful, unique, accessible to the component contract of Section 6.4, documented, and free of business logic. Then the core team takes ownership and releases it. The arrangement solves two problems at once. The team that needs something now is never blocked by the core, and the core never absorbs a component that only one team will ever use. It is InnerSource applied to the interface, and the Software book's Section 8.4 describes the trusted-committer practice that makes such contributions sustainable.

Verified Resale went through this path twice. `VerifiedBadge` and `ReissueStatus` began as candidates in the Resale team's code during the prototype stage, and both were promoted after Mobile App needed them for the app's resale module and Fan Messaging needed `ReissueStatus` for the "your ticket sold" email. The accessibility review caught one thing that the Resale team had missed: the badge conveyed "verified" by color and an icon alone, with no text for a screen reader, and the reviewed version carries a visible label.

#### Versions, codemods and the dashboard {#c7-versioning}

A design system that cannot change becomes the subway in 1975, so the question is how it changes without breaking 40 teams. The answer has three parts, and each is established practice. The first is **semantic versioning**, as Tom Preston-Werner specified it: a major version for changes that break consumers, a minor version for compatible additions and a patch for compatible fixes, so that a team can read from the number alone whether an upgrade needs work. The second is a **deprecation window**: a component or property to be removed is first marked deprecated, with a warning in the console and in the documentation, and stays working for a stated period. Setlist's window is two minor releases and never less than six months.

The third part is the one that changes the economics. A **codemod** is a program that rewrites source code automatically to carry out a migration, usually by parsing the code into a syntax tree and transforming it. Addy Osmani and Hassan Djirdeh's *Building Large Scale Web Apps* (2024) gives the technique a chapter, and Shopify's design system, Polaris, offers the clearest public example of its use. Polaris's guide for migrating from version 11 to version 12 states that the bulk of the migration is automated through its migrator command-line tool, with a named transform for each breaking change and a dry-run mode to preview the result. Encore adopted the same rule: Setlist ships a breaking change only with the codemod that migrates consumers in the same release, and the core team runs it first against every consumer in the monorepo before tagging the release. A breaking change whose migration cannot be automated needs a stronger case, and it usually waits for the next major version. The mechanics of large-scale change belong to the Software book's Section 2.5.

I spent a decade maintaining a widely used open-source library, and the lesson I took from it is that a maintainer who cannot see who is running which version is guessing every time they decide what to break. Setlist answers that with a **version dashboard**, which shows for each storefront context and each console remote the Setlist version it runs, how far behind the current release it is, and which deprecated components it still uses. The dashboard makes migration a visible, finite piece of work. It also protects the core team from its own optimism, because it shows how long the last migration actually took.

One further practice guards the releases themselves. Every Setlist component is rendered in each of its states, in every theme, by a component workshop in continuous integration (CI), and the screenshots are compared against the previous release. This **visual regression testing** catches the change that passes every unit test and still moves a button two pixels into the hold timer. It is standard practice in mature design systems, because no other automated test looks at the rendered screen.

#### Documentation that stays true {#c7-living-docs}

The *Chicago Manual of Style* has gone through many editions since its first in 1906, and its authority comes from that revision as much as from its rules: an editor trusts it because it is current. A design system's documentation earns trust the same way, and the established way to keep it current is to generate it from the code. Setlist's pattern library is built by the same component workshop that runs the visual tests, so every example on the documentation site is the real component at its current version. Each entry adds what the code cannot say: when to use the component and when not to, examples of correct and incorrect use, the accessibility contract, and a list of the places in the product where it is used, taken from the nightly scan.

Keeping design files in step with code is harder, and the honest description is that the practice is maturing. Design tools gained variables, programmatic interfaces and token import between 2023 and 2025, and the stable token format makes the exchange cleaner. What works reliably today is a one-way flow. Setlist's token files in the repository are the source; the build pipeline generates the platform outputs for web, iOS and Android, and a scheduled job updates the design tool's variables from the same files. Designers do not edit tokens in the design tool; they propose changes to the token files through the same review as any other change. Two-way synchronization is offered by several tools, and Encore does not use it, because two sources of truth for one decision eventually disagree. The same tokens and the same governance serve the native apps, whose shared design system is the subject of Section 8.5.

**Recap.** A design system's users are other teams, so it needs research, support and an adoption measure, and the lowest adoption figure is the most informative one. Most large systems settle on a central core with federated contributors, which works only if contribution is a real path with public criteria. Breaking changes ship with their codemods, a version dashboard shows the debt that remains, and documentation stays true when it is generated from the code it describes.

**Exercise 7.2.** Measure what share of your product's interface is drawn by design-system components, per team. Take the team furthest behind and ask them, without defending the system, what it lacks.

### 7.3 The Frontend Codebase in Practice

#### What was settled, and what changed {#c7-what-changed}

The Architecture book's Chapter 8 settled the frontend's structural decisions, and nothing in Encore's growth since has unsettled them. Rendering is chosen per page class. State is sorted into local interface state, server cache and genuine global client state. Code is divided by bounded context, with boundaries checked in the build. Micro-frontends must clear a bar measured in waiting. And whoever runs a shell runs a product. This section is about living with those decisions at 40 teams.

One decision did change, in the way that book said it should. In its eighth year Encore had seven teams shipping into the organizer console, which was still the single separate application the Architecture book had described. The Organizer Console team did what Section 8.3 of that book asked and counted release collisions over a quarter. About two releases in five had been held back by another team's unfinished change, and two teams had begun batching their work to avoid the release train. That was the evidence of waiting. The console moved to runtime module federation: a shell owned by the Organizer Console team, with the organizer backend for frontend (BFF), and six remotes owned by Organizer Onboarding, Event Setup, Pricing & Presales, Festivals, Organizer Insights and Forecasting. Each remote now ships on its owner's schedule. The fan storefront did not follow. Its teams share one deploy without the same contention, and duplicated payload would cost its on-sale crowds dearly, so it remains a modular monolith with context boundaries, its shell and server rendering owned by the Web Storefront team. Verified Resale's rules console will become the console's seventh remote, built by the Organizer Console team, and the fan resale page will be a new `resale/` context in the storefront, owned by the Resale team.

#### The shell as a product {#c7-shell}

Runtime federation became practical when webpack 5, released in October 2020, shipped Module Federation, created by Zack Jackson with Marais Rossouw and Tobias Koppers. It lets a running application load code that another team built and deployed separately. The **shell** is the host application that loads those remotes and owns everything they share: routing between them, the organizer's session, the current tenant and its theme, error boundaries so that a failing remote shows a contained error while the rest of the console keeps working, and the frame of navigation that makes seven remotes feel like one tool. Luca Mezzalira's *Building Micro-Frontends* (second edition, 2025) is the best practical account of operating one.

The shell needs to know which version of each remote to load, and here there is a choice. The remotes' locations can be compiled into the shell, which couples every remote release to a shell deploy and gives back the waiting that federation was meant to remove. They can be listed in an import map, a browser-native mechanism. Or they can be served by a **frontend discovery** service, a pattern Mezzalira and colleagues at Amazon Web Services have published with an open schema, in which the shell fetches at startup a manifest naming the current version of each remote. Encore uses a discovery manifest. It is one good answer among several, since no industry standard has emerged, and its value lies in what it decouples: a remote's owner can release, and roll back, by changing one entry, without touching the shell. Progressive delivery of remotes, the canary that sends a new version to a fraction of organizers first, works through the same manifest and is described in the Resilience book's Chapter 4.

The Organizer Console team runs the shell as a product, with a changelog, a weekly office hour for the remote teams and a service level objective (SLO): 99.9% of console page loads render the shell and the requested remote without an error boundary firing, over a rolling 28 days. A remote that throws is the remote's problem; a shell that fails to load any remote is the shell's.

#### Shared dependencies and version skew {#c7-version-skew}

Federation gives each remote its own build, and with it the freedom to bring its own copy of everything. That freedom has two costs. The first is payload: a remote that bundles its own framework makes the organizer's browser download the framework again. The second is subtler and worse. Some libraries hold state that must be single for the page to work, such as the framework's renderer, the router, and Setlist's theme context, and two copies of them produce errors that appear only in the browser, only in certain combinations of remote versions, and never in any one team's tests. Mezzalira names the antipatterns that lead here, among them what he calls micro-frontend anarchy, in which each team picks its own framework and versions. The cure is an explicit and short list of shared dependencies, each declared as a **singleton**, a library loaded once for the whole page, with a version range that every remote must accept. Encore's console remotes declare the same block, generated from one file the shell team owns:

```js
// Generated from shell/shared-deps.json — do not edit by hand.
new ModuleFederationPlugin({
  name: "eventSetup",
  filename: "remoteEntry.js",
  exposes: { "./App": "./src/App" },
  shared: {
    react:              { singleton: true, requiredVersion: "^19.0.0" },
    "react-dom":        { singleton: true, requiredVersion: "^19.0.0" },
    "@encore/setlist":  { singleton: true, requiredVersion: "^14.2.0" },
    "@encore/session":  { singleton: true, requiredVersion: "^3.0.0" },
  },
});
```

Four entries is a deliberate number. Everything else, from date libraries to charting, each remote may bundle for itself, accepting the payload in return for independence. The short list makes the hard question visible, which is who decides when a shared dependency moves. At Encore, the shell team proposes and the remote teams agree, and the move is run as a campaign with a deadline. The framework's last major-version upgrade ran across the storefront and all six remotes as a tracked campaign over two quarters, with a dashboard of who had moved, a codemod for the mechanical part of the change, and a date after which the shell stopped accepting the old version. Remotes that missed the date did not break; the shell kept loading their last compatible release until they caught up.

The tooling around the code needs an owner too, as the Architecture book observed of the monorepo build. At Encore the Web & API Paths team in the platform group owns the frontend build paths, the workspace tooling and the generation of typed API clients from the OpenAPI contracts, so that a change to a backend contract shows up as a type error in the frontend that calls it. Large refactors across the frontend run as codemods, never by hand. The general arguments for the monorepo and for automated change at scale are made in the Software book's Sections 4.2 and 2.5, and the frontend adds nothing to them except the scale of its imports.

#### Fitness functions for forty teams {#c7-frontend-fitness}

The Architecture book introduced fitness functions for the frontend: performance budgets and cycle checks between contexts. At Encore's present scale the same idea carries four kinds of check in CI. Boundary checks fail a build when one storefront context imports another's internals, or when a console remote imports another remote's code directly, bypassing the shell's published interface. Bundle budgets, one per remote and one per storefront route, fail a build that exceeds them. Automated accessibility checks fail a build on the errors a tool can detect, knowing that tools catch only a minority of problems and that Section 6.4's manual testing remains on the release checklist. And design-system usage checks, lint rules that reject raw color values and hand-built copies of Setlist components, warn on new code.

The last kind deserves a caveat. Lint rules that enforce design-system use are common practice, and the reasoning behind them is sound, but there is no published evidence of how much they improve consistency, and a rule that blocks a build for a hard-coded color can tempt a team to disable the rule and leave the cause in place. Encore runs them as warnings on new code and reports them on the adoption dashboard, and it blocks only the two cases where a departure harms fans: raw colors that bypass the contrast-checked tokens, and custom focus styles. Keeping 40 teams' code coherent through checks and dashboards, with no review board for screens, is Encore's choice, made in the spirit of the platform's golden paths, and it depends on the checks being few, fast and explained.

**Recap.** Encore moved its organizer console to federated remotes when release collisions showed the waiting, and left the fan storefront as a modular monolith because the evidence there did not. The shell is a product with an owner, a changelog and an objective, and a discovery manifest lets remotes release without it. A short list of singleton dependencies keeps version skew manageable, upgrades run as campaigns, and a few explained checks in CI keep the codebase coherent.

**Exercise 7.3.** List the shared dependencies of your frontend and mark which ones must be a single version on the page. For each, write down who decides when it moves, and how long the last move took.

### 7.4 Performance as a Feature

#### Reading the evidence that speed sells {#c7-speed-evidence}

The idea that speed is a property of the product as much as of its servers has a clear lineage. Steve Souders's *High Performance Web Sites* (2007) argued from measurements at Yahoo that most of the time a user waits is spent in the browser and on the network after the server has answered, and that a short list of rules about requests, caching and script placement recovered most of it. Ilya Grigorik's *High Performance Browser Networking* (2013) opened its first chapter with a section titled "Speed Is a Feature". Google's Core Web Vitals, which the Architecture book's Section 8.1 defined along with their thresholds, turned the argument into three numbers that anyone can measure. This section takes those numbers and thresholds as given and asks a different question: how do we know that being faster is worth the work, and how do we make it a habit at 40 teams?

The evidence most often cited comes in two kinds, and they should not be read the same way. The first kind is an experiment. In 2021 Vodafone published, with Google, the results of an A/B test on a landing page: traffic from paid media was split evenly between the existing page and an optimized version, and the optimized version had a field largest contentful paint (LCP) 31% better, 5.7 s against 8.3 s. It produced 8% more sales. Because the traffic was randomized, the difference can be attributed to the change, and the result is as close to proof as a single published case gets, for that page, those visitors and that size of improvement. The second kind is a correlation. *Milliseconds Make Millions*, a 2020 study by Deloitte Digital with Fifty-Five, commissioned by Google, examined the mobile sites of 37 brands and reported that a 0.1 s improvement in mobile speed went with an 8.4% rise in conversions for retail and 10.1% for travel. It should be quoted with its nature attached: it is observational, so faster sites may also be better in other ways, and it was commissioned by a company with an interest in a faster web. That does not make it false. It makes it a reason to test, and the Vodafone result shows what a test can establish.

The reasoning that carries over to Encore is modest and firm. Speed has been shown, in at least one controlled experiment, to move sales, and the size of the effect varies with the starting point, the page and the audience. So Encore treats speed as a feature to be designed and measured like any other, uses Chapter 4's experimentation platform where a change is large enough to test, and does not promise anyone a revenue figure from a percentage borrowed from someone else's site.

#### Latency, radios and the car park {#c7-latency}

Grigorik's central argument is the one most engineers still find counterintuitive: for most page loads, latency matters more than bandwidth. Beyond a few megabits per second, more bandwidth barely shortens a page load, because a page is assembled from many small requests, and each is bounded by the time a round trip takes, which no faster connection reduces. Mobile networks add a second effect. A phone's radio goes idle to save battery, and a radio that has gone idle must be woken and granted resources before the first byte moves, so the first request after a pause pays a cost the next one does not. The remedies follow from the diagnosis: make fewer round trips, reuse connections, put content closer to the user through the content delivery network (CDN), and cache whatever can be cached. Grigorik's book predates HTTP/3, which runs over QUIC (standardized in 2021 and 2022) and removes some of the head-of-line blocking that slowed lossy mobile connections, but the principle it serves is the same.

Encore's design target is the fan the Architecture book's Chapter 8 began with: on a phone, in a stadium car park, on a congested mobile network. That fan matters most on the resale page, because a resale page is opened in exactly the circumstances where networks are worst, outside a sold-out venue an hour before doors, or in the minute after an on-sale sells out, when every fan who missed out reaches for their phone at once.

#### The field is the truth {#c7-field-data}

**Real-user monitoring (RUM)** is the collection of performance measurements from users' own browsers as they use the product, reported in aggregate. The Architecture book drew the line between lab and field. At 40 teams, the field data is useful only once it is segmented. A single p75 for the whole site hides the fan in Sofia on a three-year-old phone behind the fan in Amsterdam on a new one, so Encore reports its Core Web Vitals at p75, the 75th percentile, on phones by country, by device class and by route. Interaction to next paint (INP), which replaced first input delay as a Core Web Vital on 12 March 2024, turns out to matter most on the organizer console, a sovereign tool in the sense of Section 6.2, where an organizer types and clicks all day and notices every sluggish response. On the fan side, LCP on the event and seat-map routes matters most.

The resale page is measured separately from the rest of the storefront. Its traffic arrives in spikes, after sell-outs, on worse networks than average, and from fans who are more likely to be on the page for the first time. Blended into the storefront's figures, a bad resale experience would disappear inside a good average.

#### Budgets that someone owns {#c7-owned-budgets}

A **performance budget** is a limit on a measurable property of a page, such as its JavaScript weight or its LCP, enforced in the build. The Architecture book introduced Encore's checkout budget, 150 KB of compressed JavaScript with LCP no worse than 2 s in the lab on a mid-tier phone, and it explained how budgets stop a page from getting slower one dependency at a time. What changes at 40 teams is the question of who owns each budget. A budget that belongs to everyone is a red build that someone eventually learns to ignore. That is an observation from practice, without a study behind it, but few teams who have lived with an unowned budget would dispute it. Encore assigns every budget to one team, as Figure 7.3 shows (JS in the figure is JavaScript).

| Budget | Owner | Lab gate (CI) | Field target, p75 on phones |
|---|---|---|---|
| Storefront shell and shared code | Web Storefront | 90 KB compressed JS | — |
| Checkout route | Checkout | 150 KB JS; LCP ≤ 2 s, mid-tier phone | LCP ≤ 2.5 s; INP ≤ 200 ms |
| Resale route | Resale | 120 KB JS; LCP ≤ 2 s, mid-tier phone | LCP ≤ 2.0 s; INP ≤ 200 ms |
| Console shell | Organizer Console | 110 KB JS | — |
| Each console remote | The remote's team | 80 KB JS per remote, beyond shared singletons | INP ≤ 200 ms |
| Third-party scripts | Web Storefront (inventory); requesting team (each script) | Each script listed with a cost | — |

*Figure 7.3 — Encore's frontend budgets and their owners. Each row has one team; the resale route's field target is tighter than Google's threshold because its users arrive on the worst networks.*

When a field metric regresses, the owning team is told the same day by the RUM dashboards, and Encore's policy is that every regression has a named owner within a working day, even if the fix takes longer. The alerting itself is part of observability, which the Operations book covers; what this chapter adds is that every alert names an owning team.

The last row of the figure covers the most common cause of regressions that no team's code review sees. Analytics tags, marketing pixels, chat widgets and payment-provider scripts are added through a tag manager, often by people outside engineering, and each adds weight and main-thread work to every page it touches. Encore keeps an inventory of every third-party script: who asked for it, which pages it runs on, what it costs in kilobytes and in main-thread time, and when it was last reviewed. A script with no owner is removed. Checkout and the resale route admit no third-party script except the payment provider's, which is the strictest form of the rule and the one where it matters most.

#### Peak pages {#c7-peak-pages}

Some pages see their year's traffic in an hour. For Encore these are the event page at an on-sale, and now the resale page for an event in the minutes after it sells out. A **peak page** is a page whose demand arrives as a sudden spike, so that its performance on the worst minute matters more than its average. Before launch, the Web Storefront team and the owning team review each peak page with three questions. Can the page be static, or mostly static? The resale page's frame, event details and seat-map geometry are rendered ahead of time and served from the CDN, and only the listings themselves are fetched live. Can its next step be fetched before the fan asks? When a fan's pointer rests on a listing, or a listing scrolls into view, its detail is prefetched; the newer Speculation Rules interface, which can prerender whole pages, works only in Chromium-based browsers, so Encore treats it as an enhancement. And what can be removed? On the resale route the answer was every third-party script, a promotional carousel and a web font that was used for one heading.

The review covers what the fan's device has to do. The capacity behind the page, the services that must answer when a hundred thousand fans open it in the same minute, is a capacity question, and it belongs to the Resilience book's Chapter 2.

**Recap.** One controlled experiment and one widely cited correlation together justify treating speed as a feature, and they should be read for what each is. Latency, more than bandwidth, bounds most page loads, especially on mobile radios. Field data at p75, segmented by country, device and route, is the truth, and every budget needs one owning team, including the budget for scripts that no team wrote. Peak pages get a review: static where possible, prefetched on intent and stripped of everything they do not need.

**Exercise 7.4.** Pull your product's p75 LCP and INP on phones for your slowest country. Find the largest single contributor to each, and name the team that owns it.

### 7.5 Internationalization

#### Separate the dimensions {#c7-locale-dimensions}

On 18 November 1883 the railroads of the United States and Canada stopped keeping the local solar time of each town and adopted a handful of standard time zones. Before that, a railway timetable had to reconcile dozens of local times, and a traveler changing trains had to know which town's clock a departure was listed in. The railroads' solution was to separate two things that had always been fused: where you are and what time it is there. Internationalization requires the same kind of separation, applied to several things at once. **Internationalization** is the engineering of a product so that it can be adapted to many languages, regions and conventions without changes to its code; **localization** is the adaptation itself, for one particular market.

The dimensions are easy to fuse by accident, because in the developer's own country they usually coincide. Language and region are identified together by a BCP 47 language tag, the Internet's standard for naming languages (RFC 5646, 2009): `fr-FR` is French as written in France, `fr-BE` French in Belgium, `nl-BE` Dutch in Belgium. The tag carries language, script and region. Currency and time zone are not part of the basic tag. The Unicode standards define extensions that can carry them, but most products, Encore among them, store them as separate settings, and number and date formats follow from the locale unless the user overrides them. Figure 7.4 takes one Verified Resale purchase apart along these lines.

| Dimension | Whose setting | Source of truth | One resale purchase |
|---|---|---|---|
| Language | The fan's | Fan profile, else browser, with fallback | Finnish (`fi`) |
| Region and formats | The fan's | BCP 47 tag `fi-FI`, via the Common Locale Data Repository (CLDR) | "66,00 €"; dates as "12. kesäkuuta 2026" |
| Currency | The event's | Event setup; ISO 4217 code | EUR, two minor units |
| Time zone for the show | The venue's | Venue record; IANA time zone name | `Europe/Lisbon`: doors 19:00 |
| Legal display rules | The market of sale | Market configuration, owned with legal | All-in price shown first; resale fee itemized |

*Figure 7.4 — One fan in Helsinki buying a resale ticket for a show in Lisbon. Five settings, owned by three different parties, combine on one screen.*

Each row has a different owner, which is the point of separating them. A fan in Helsinki chooses Finnish; the organizer's event is priced in euros; the venue is in Lisbon. The fan's language and number formats follow the fan, while the show's time follows the venue. Encore applies one subtle rule here. The time of the show is displayed in the venue's zone, with the zone named, because the fan will be standing in Lisbon when it matters. The time an on-sale opens is displayed in the fan's own zone, because the fan will be at a keyboard at home. A fan in Helsinki sees doors at "19:00 Lisbon time" and an on-sale at "11:00" Helsinki time for a sale that opens at 10:00 Central European Time.

Three practical matters complete the foundation. Locale negotiation needs a **fallback chain**: when a fan asks for a locale Encore does not support, it falls back by stages, from `fr-LU` to `fr` and only then to the default, in the manner the matching standard (RFC 4647) describes, so that a French speaker in Luxembourg still reads French. Text is UTF-8 everywhere, from the database to the email, so that a Polish ł or a Greek σ survives every hop; Unicode, first published in 1991, is what made that possible. And fonts must cover every script a product displays, which for Encore means Latin, Greek and Cyrillic for Bulgarian, each subset so that a fan downloads only the characters their language needs. Encore's storefront today is available in 18 languages.

#### Messages and plurals {#c7-messages}

The first rule of internationalized code is that no user-visible text lives in the code. Every string is externalized into a message catalog under a stable key, and translators work on the catalog. The second rule is that strings are never built by concatenation. "You have " plus a number plus " tickets" works in English and fails in nearly every other language, because word order, agreement and plural forms differ, and a translator given three fragments cannot reorder them.

The established answer is the **ICU MessageFormat**, the message syntax of the International Components for Unicode (ICU) libraries, which has run in ICU, Java, Android and most JavaScript internationalization libraries for decades. A message is a complete sentence with placeholders and selectors for plurals, grammatical gender and other choices, and the plural categories come from CLDR, which records for each language which forms its plurals take. English needs two categories, one and other. Polish needs four: one, few, many and other. Arabic needs six: zero, one, two, few, many and other. The source message and its Polish translation show why the selector belongs in the message itself.

```text
# en
resale.listings.count = {count, plural,
    one {# resale ticket at face value}
  other {# resale tickets at face value}}

# pl
resale.listings.count = {count, plural,
    one {# bilet z odsprzedaży w cenie nominalnej}
    few {# bilety z odsprzedaży w cenie nominalnej}
   many {# biletów z odsprzedaży w cenie nominalnej}
  other {# biletu z odsprzedaży w cenie nominalnej}}
```

The English source has two branches; the Polish translator adds two more without any change to the code that calls it. That is the property to insist on: a language's grammar is the translator's to express, and the code supplies only the count. Mozilla's Fluent, whose version 1.0 was announced in 2019, was designed around the same principle, which its authors called asymmetric localization: each language adds whatever grammatical logic it needs, without the source language or the code having to anticipate it.

The format's successor deserves a careful sentence. **MessageFormat 2.0** became a stable Unicode specification in CLDR 47, in March 2025, as part of the Locale Data Markup Language standard. Its implementations are still maturing: ICU's Java implementation has a core interface at draft status, its C++ implementation remains a technology preview, a JavaScript library implements the specification, and the proposal to build it into browsers as `Intl.MessageFormat` is at Stage 1 in TC39, the committee that evolves JavaScript. So the specification is stable, and using it in browsers in production still means shipping a library. Encore uses ICU MessageFormat today and has written its new messages so that they convert mechanically when the time comes.

#### Formatting from data {#c7-formatting}

Dates, times, numbers and currencies are never formatted by hand. In browsers they go through the ECMAScript Internationalization API (ECMA-402, the `Intl` objects), and on servers through ICU, both of which draw on CLDR's data for each locale. The currency's minor units come from ISO 4217, which is how a formatter knows that euros have two decimal places while Japanese yen have none and Kuwaiti dinars three. Times are computed in the IANA Time Zone Database's named zones, which record every change to every region's clocks, including the daylight-saving changes that a fixed offset gets wrong twice a year.

The resale price shows why this matters even in a single currency. A €60 ticket resold at face value costs the buyer €66, the face value plus the 10% buyer fee. The Resale service computes those amounts in the event's currency, as integer minor units, and the storefront formats them for the fan's locale. The same 66 euros appears as "66,00 €" in French, German and Finnish, as "€66.00" in Irish English and as "€ 66,00" in Dutch, and the French form puts a no-break space before the symbol, so that the amount and the symbol never fall on separate lines, a detail that a hand-written format reliably forgets. Each form is correct for its readers, and only a formatter driven by locale data produces all of them.

#### Direction and layout {#c7-bidi}

Arabic and Hebrew are written from right to left, and an interface for them mirrors its layout: navigation moves to the right, progress runs leftward, and icons whose meaning depends on direction, such as a "back" arrow, are flipped, while icons that depict real objects, such as a clock or a ticket, are not. The Unicode Bidirectional Algorithm (UAX #9) governs how text of mixed direction is displayed, and the W3C's internationalization guidance explains how to mark it up. The modern technique that makes mirroring cheap is the use of CSS logical properties. They describe space by the start and end of a line, which is left and right in French and right and left in Arabic, so that one stylesheet serves both directions.

Encore sells only in the EU, and none of its 18 languages is written from right to left. Setlist uses logical properties throughout anyway, for two reasons. The first is cost: written in from the start they cost nothing, and retrofitted they mean revisiting every component. The second is that mixed-direction text appears even in a product with no right-to-left language. An artist's name in Arabic script, or a venue's name in Hebrew, set inside a French sentence can reorder the punctuation and numbers around it in ways that confuse a reader. Setlist's text components isolate user- and organizer-supplied names with the HTML `bdi` element and `dir="auto"`, so that a name's direction cannot disturb the sentence it sits in. Such a decision belongs in the design system, because made there once it protects every screen that displays a name.

#### The translation pipeline {#c7-translation-pipeline}

**Continuous localization** is the practice of translating a product string by string, as it is built. At Encore, every merged change that adds or edits a message has its new strings extracted by CI and sent to the translation platform, together with a screenshot of the screen where the string appears, because a translator who sees "Hold" without context cannot know whether it is a verb or a noun. The platform keeps a translation memory, so that a sentence translated once is offered again wherever it recurs, and a glossary, so that "face value" and "reissue" are translated the same way on every screen. Product copy is translated by machine and reviewed by a human translator before release, which is now common practice. Legal text, terms of sale and anything that states a price or a fee are translated by people, because a mistranslated fee is a compliance failure.

The cheapest test in internationalization is **pseudo-localization**: an automatic transformation of the source language into a readable but altered form, with accented characters, text lengthened by a third or more, and brackets marking the start and end of each string. Microsoft ships pseudo-locales in Windows, and the technique is long established. Run in development, it reveals at a glance every string that was hard-coded (it appears without accents), every label that was concatenated (the brackets break in the middle), and every button whose text will be truncated in German or Finnish. Encore's developers can switch any environment to a pseudo-locale, and the visual regression tests of Section 7.2 run Setlist's components in it.

#### Prices the law can read {#c7-regulated-display}

In the EU, how a price is displayed is a legal matter, and an internationalized price display is therefore a compliance surface. The obligation to show the total price, including taxes and all unavoidable charges, comes from three instruments: the Consumer Rights Directive (2011/83/EU), for contracts at a distance and otherwise; the Unfair Commercial Practices Directive (2005/29/EC), which requires an invitation to purchase to state the total price; and the Price Indication Directive (98/6/EC). The Omnibus Directive (EU) 2019/2161, applicable from 28 May 2022, added rules that matter to Encore in other ways. It blacklisted the resale of event tickets acquired by automated means that get around purchase limits, which is the practice Bot Screening exists to stop, and it required disclosure of personalized pricing, which Encore does not use. Section 5.2 sets out Encore's fee policy and the reasoning behind all-in pricing; this section is about rendering it.

For Verified Resale this means that the first price a fan sees for a listing is the total, €66 in our example, with the face value and the fee itemized beneath it by `PriceBreakdown`, formatted for the fan's locale and translated by people. National law adds conditions. Where Ireland's Sale of Tickets Act 2021 caps the buyer's total at face value for designated events, the fee comes out of the seller's proceeds and the breakdown shows it so. Some rules are temporary. When Bulgaria adopted the euro on 1 January 2026, its law required prices to be shown in both lev and euro until 8 August 2026. Rules of this kind are why Encore keeps each market's display rules as configuration owned with the legal team, and why the formatter, not the page, applies them.

**Recap.** Internationalization begins by separating dimensions that coincide at home: language and region in a BCP 47 tag, currency with the event, time zone with the venue, and legal display with the market. Messages are complete sentences with plural selectors driven by CLDR, and MessageFormat 2.0 is a stable specification whose runtimes are still maturing. Formatting comes from data, bidirectional text is isolated in the design system, translation runs continuously with pseudo-localization as the first test, and the all-in price is rendered as the law of each market requires.

**Exercise 7.5.** Pseudo-localize one screen of your product and count what breaks: truncated labels, concatenated strings and hard-coded formats. For each break, find the line of code responsible and say which of the five dimensions of Figure 7.4 it fused.

### Kata: The Departures Board

> **Your brief: "Wayfare."** Wayfare is a travel-booking marketplace that sells rail, ferry and coach tickets and short-stay rooms from about 3,000 operators across Europe, the Middle East and North Africa. Its web product is built by 25 frontend teams. Five years ago it built a design system, and adoption has been stuck at about 40% for two years; the core team of four answers requests in a queue that is three months deep, and the three largest teams maintain their own component libraries. The product runs in 32 locales, including Arabic and Hebrew, and prices in 14 currencies. Its operator console was split into nine federated remotes last year; its consumer site is a single application. Two pages carry its peaks: search results during the January sale, when traffic rises 20× for three days, and the seat-and-cabin selection page when a popular overnight ferry opens bookings. Field data shows p75 LCP on phones above 4 s on both pages in four markets. Wayfare's legal team has just reported that two markets display fees only at the last step of checkout.

**Deliverables:**

1. **Governance model** — Choose a team model from Figure 7.2 and justify it from Wayfare's numbers. Define the contribution path, including what a pattern candidate is and the criteria for promotion, and say what the core team stops doing to make room for review.
2. **Migration plan** — Plan the move of the three private component libraries onto the design system: the order, the codemods each step needs, the deprecation windows, and the version dashboard that will show progress. State the adoption figure you expect after two quarters, and how you will measure it.
3. **Peak-page budgets** — For the search-results and seat-and-cabin pages, set a lab budget and a p75 field target on phones, name the owning team for each, and list what a pre-peak performance review would remove, prerender or prefetch. Keep capacity out of scope.
4. **Federation hygiene** — Write the operator console's list of shared singleton dependencies, with version ranges, and the rule for who decides when each one moves.
5. **Internationalization audit** — Apply the five dimensions of Figure 7.4 to one booking: a traveler reading Arabic, booking a ferry priced in euros between two ports in different time zones. Identify where Wayfare's code fuses dimensions, how its messages handle Arabic's six plural categories, how bidirectional text is isolated, and how the all-in price will be displayed in the two non-compliant markets.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Adoption as evidence | Does the plan start from why the three largest teams left, and would they recognize their reasons in it? |
| Migration realism | Does every breaking change ship with a codemod, and does the dashboard show what remains? |
| Owned budgets | Does every budget have exactly one owning team, including the third-party scripts on both peak pages? |
| Skew control | Is the singleton list short enough that the console's teams can keep it, and long enough that the page works? |
| Locale separation | Could a new currency, time zone or right-to-left language be added as data, without changing code? |
| Lawful display | Would a fan in every one of the 32 locales see the total price first? |

#### Where you now stand

You can now treat a design system as what the 1970 manual turned out to be: a set of named decisions that is worth something only while an owner keeps the product on it. You can measure its adoption, govern it with a core and a contribution path, change it with codemods and a dashboard, and keep a federated frontend coherent with a short list of shared dependencies and a few checks. You can make performance a habit with owned budgets and field data, and you can build an interface that reads correctly in any language and displays prices as the law of each market requires. All of this assumed that a fix reaches every user at the next page load. Encore's most important channel does not work that way. Its fans carry the app in their pockets, updated when they choose to update it, through stores whose review Encore does not control, and some of them will open a build next spring that was compiled three summers ago. Chapter 8 takes up software that cannot be recalled.

### References

- Brad Frost — [*Atomic Design*](https://atomicdesign.bradfrost.com/). Self-published, 2016 — free online.
- Alla Kholmatova — [*Design Systems: A Practical Guide to Creating Design Languages for Digital Products*](https://www.smashingmagazine.com/design-systems-book/). Smashing Media, 2017.
- Paul Shaw — [*Helvetica and the New York City Subway System: The True (Maybe) Story*](https://mitpress.mit.edu/books/helvetica-and-new-york-city-subway-system). MIT Press, 2011.
- Design Tokens Community Group — [*Design Tokens Format Module 2025.10*](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/), with the Color and Resolver modules. W3C Community Group Final Report, 2025 — free online.
- Nathan Curtis — [*Team Models for Scaling a Design System*](https://medium.com/eightshapes-llc/team-models-for-scaling-a-design-system-2cf9d03be6a0). EightShapes, 2015 — free online.
- Luca Mezzalira — [*Building Micro-Frontends*, 2nd ed.](https://www.oreilly.com/library/view/building-micro-frontends-2nd/9781098170776/) O'Reilly, 2025.
- Addy Osmani, Hassan Djirdeh — [*Building Large Scale Web Apps: A React Field Guide*](https://www.largeapps.dev/). Self-published, 2024.
- Ilya Grigorik — [*High Performance Browser Networking*](https://hpbn.co/). O'Reilly, 2013 — free online.
- Google — [*Vodafone: A 31% improvement in LCP increased sales by 8%*](https://web.dev/case-studies/vodafone). web.dev, 2021 — free online.
- Deloitte Digital, Fifty-Five, for Google — [*Milliseconds Make Millions*](https://web.dev/case-studies/milliseconds-make-millions). 2020 — free online.
- Ravi Lingineni — [*How Pinterest's design systems team measures adoption*](https://www.figma.com/blog/how-pinterests-design-systems-team-measures-adoption/). Figma blog, 2023 — free online.
- Unicode Consortium — [*UTS #35: Unicode Locale Data Markup Language, Part 9: Message Format*](https://www.unicode.org/reports/tr35/tr35-messageFormat.html). Unicode, 2025 — free online.
- Unicode Consortium — [*UAX #9: Unicode Bidirectional Algorithm*](https://www.unicode.org/reports/tr9/) and [*Unicode CLDR*](https://cldr.unicode.org/). Unicode, continuously updated — free online.
- A. Phillips, M. Davis (eds.) — [*BCP 47: Tags for Identifying Languages*](https://www.rfc-editor.org/info/bcp47) (RFC 5646 and RFC 4647). IETF, 2006–2009 — free online.
- Adam Wathan, Steve Schoger — [*Refactoring UI*](https://www.refactoringui.com/). Self-published, 2018.
- European Union — [*Directive 2011/83/EU on consumer rights*](https://eur-lex.europa.eu/eli/dir/2011/83/oj) and [*Directive (EU) 2019/2161*](https://eur-lex.europa.eu/eli/dir/2019/2161/oj). Official Journal of the EU, 2011 and 2019 — free online.

---

## Chapter 8: Mobile and Many Channels — Software You Cannot Recall {#ch8}

> A release we cannot recall has to be designed as though it will never be corrected.

Every chapter so far has assumed, without quite saying so, that a mistake can be taken back. A confusing page on the fan storefront is changed on Tuesday and gone by Tuesday evening, and the next fan who loads it never sees the old version. That assumption fails the moment our software lives in a fan's pocket. A native app is a binary that we hand over and cannot take back. It runs on a device we do not own, updates when its owner decides, and keeps calling our servers for years, and between the build and the phone stands a store run by another company under rules that company writes. This chapter asks what deciding and designing a product looks like when part of it cannot be recalled, and when the same fan reaches us through an app, a mobile browser, a wallet pass, an email and a partner's app, each with its own reach and its own failures.

The moment that made this the ordinary condition of consumer software can be dated. On 10 July 2008 Apple opened the App Store, as a section of iTunes 7.7, the day before iPhone OS 2.0 and the iPhone 3G went on sale. It opened with more than 500 native applications, and four days later Apple announced 10 million downloads in the first weekend; Steve Jobs called the store "a grand slam, with a staggering 10 million applications downloaded in just three days." The path to that weekend is worth remembering. When the first iPhone shipped in June 2007 it had no third-party native apps at all, and Apple's answer to developers that summer was that they could write web applications running in Safari. Developers were not persuaded, and some jailbroke their phones to run native code. In March 2008 Apple announced a software development kit and a store in which developers would set their own prices and keep 70% of the revenue, while Apple hosted, signed and reviewed every app before it reached anyone. The question of web or native, which Section 8.1 takes up, is therefore as old as the platform itself.

We should be careful about what the opening changed. The App Store was not the first gate between a company's software and its customers' devices. Carrier storefronts, Qualcomm's BREW among them, had certified and sold phone software for years, and console makers had licensed and approved games since the 1980s. What 2008 changed was scale and reach. One platform owner's review now stood in front of all third-party software on a mass-market, general-purpose device, Google's Android Market opened that October, and within a few years store review and binary distribution had become the normal path from a company's build to its customers. Three consequences followed, and each is the root of a section of this chapter. A reviewer now stood between the build and the user, so every fix now had to pass through a submission. A version, once installed, stayed until its owner replaced it, which gave rise to the long tail of old versions, to forced upgrades and to remote switches that can change a binary's behavior after it has shipped. And the rules governing payments, notifications, wallet passes and data collection became a dependency written and revised by someone else. The staged rollouts we now take for granted came years later; in 2008 an approved version went to everyone at once.

Encore feels each of these consequences sharply, because its most important artifact, the ticket, lives on the phone. Most fans hold their tickets in the fan app, many of the rest in Apple Wallet or Google Wallet, and they present them at stadium gates where thousands of phones compete for one overloaded cell. Verified Resale adds a demand the web never had to meet. When a ticket is resold through Rowmate or Tessera, Encore reissues it under a new ticket identity, and the seller's ticket must stop working while the buyer's starts, on app versions up to two years old, on phones that may be offline, without the gate ever accepting both. Every section that follows is, in the end, about whether that one guarantee holds.

### 8.1 Choosing How to Build Mobile

#### The channel map {#c8-channel-map}

Before we choose how to build an app, we should ask which of the customer's jobs it is for. A fan's relationship with Encore is carried by many channels at once. A link in a message opens the mobile web; the fan buys in the app or on the web; the ticket arrives by email and is added to the app, a wallet or both; a push notification says when doors open; and on the night the fan holds up the phone at the gate. If the fan cannot go, a partner's app may be where the ticket is listed. Each channel has its own reliability, speed of change and owner, and a product that does not decide which channel does which job will find every channel attempting every job.

A **channel map** is a table that assigns each customer job to the channel that owns it, and names a fallback channel for when the owner fails. There is no famous method behind the name. It is ordinary omnichannel practice, written down so that a product trio and forty teams can argue about the same thing. Its value lies in two columns that are easy to omit. The first is ownership: when the ticket view in the app and the ticket in the wallet disagree, one of them is the truth and the other is a convenience, and the team needs to know which before the disagreement happens. The second is the fallback. Every job has to survive the failure of its owning channel, because every channel fails: push notifications are dropped, email lands in spam, wallets update late, and apps are deleted to free space the night before a festival.

A touring production thinks about its show in the same way. The stage manager's book assigns each cue to one person and one desk, and for the cues that would stop the show if missed it names a backup: the second follow-spot, the manual fly line. Nobody on a touring crew believes the lighting desk will never crash. The analogy breaks over control. A stage manager owns every desk in the building, while Encore owns only some of its channels: Apple and Google own the wallets, Rowmate and Tessera their apps, and the fan's email provider decides what reaches the inbox. The fallbacks matter most exactly where Encore's control is weakest.

| Fan job | Owning channel | Fallback | Notes |
|---|---|---|---|
| Discover an event | Mobile web | Fan app | Links from messages and search land on the web; the app opens them when installed |
| Buy a primary ticket | Fan app or web (equal) | Either | Same checkout behind one fan backend for frontend (BFF); no in-app purchase, as Section 8.2 explains |
| Hold and show the ticket | Fan app (rotating barcode) | Wallet pass; box-office reprint with ID | The app is the credential of record; the wallet is a convenience |
| Learn the ticket was sold or transferred | Push and in-app inbox | Email | Never push alone; Section 8.3 explains why |
| List a ticket for resale | Fan app, Rowmate, Tessera | Web | Every listing enters one resale pool |
| Change organizer resale rules | Organizer web console | None needed | The organizer works at a desk |

*Figure 8.1 — Encore's channel map for the jobs Verified Resale touches. The third row is the one the whole chapter defends.*

Figure 8.1 records a decision Encore took in its eighth year, when it built rotating barcodes for every mobile ticket. Today about 70% of tickets are presented from the fan app, about 15% from Google Wallet, about 12% from Apple Wallet and about 3% on paper from the box office, for fans without a usable smartphone. The printable PDF ticket was retired for mobile orders that year, because a static image that can be forwarded to five people is precisely the credential Verified Resale exists to replace. The consequence for resale is plain: reissue must work on every channel that can hold a ticket, and a resale that updates the app but not the wallet, or tells the buyer by push but not by email, has broken a row of the table. Even the convenience channel exists on terms Encore did not write: Apple's guidelines limit wallet passes to uses such as "movie tickets, coupons, and VIP credentials," and warn that "other uses may result in the rejection of the app and the revocation of Wallet credentials."

#### Native, cross-platform, or web {#c8-native-or-web}

With the jobs assigned, the next decision is how to build the app that owns the most important of them. Native apps are written separately for each platform, in Swift and Kotlin; cross-platform frameworks such as React Native and Flutter drive both platforms from one codebase; and the web runs in a browser or a thin native shell. Native gives the best fidelity to each platform at the cost of building most features twice. Cross-platform shares most of the work at the cost of a layer that must be debugged, upgraded and occasionally fought. The web reaches every device with one deploy and no store, at the cost of weaker access to the device. Gergely Orosz's *Building Mobile Apps at Scale* (2021), drawn from his years at Uber and from interviews across the industry, spends five chapters on these trade-offs and declines, rightly, to declare a winner.

The published record is more instructive than any comparison table. In June 2018 Gabriel Peal published "Sunsetting React Native" on Airbnb's engineering blog, one of a series in which Airbnb explained why, after two years, it was moving its React Native screens back to native code. The reasons the series gave were technical and organizational together. Sharing code did not hide the platforms as much as hoped, since text rendered differently on each and keyboards behaved differently; starting the React Native runtime before the first screen took several seconds in an app of Airbnb's size; and shipping consistently good work required engineers with expertise in three environments, which was hard to staff. Airbnb was candid that the verdict was not unanimous: by its own survey, 63% of its engineers would have chosen React Native again. In January 2020 Shopify went the other way. "After years of native mobile development," Farhan Thawar wrote, "we've decided to go full steam ahead building all of our new mobile apps using React Native." Shopify had tried React Native in 2015 and rejected it, so the 2020 decision was a deliberate reversal made on new evidence. Five years later its engineers reported, in a January 2025 retrospective, that the bet had largely paid off, with screens loading in under 500 ms at the 75th percentile, while naming debugging and the effort of upgrading the framework as the persistent costs.

The story has a third act, and it is the one place in this chapter where the AI era changes a mobile decision. On 10 September 2026 Shopify Engineering published "Native is now the future of mobile at Shopify," by Mustafa Ali, announcing a move back to Swift and Kotlin. The post does not say React Native is slow. Its argument is economic: "LLMs changed one of the core assumptions behind our 2020 decision, so we reevaluated our mobile stack from first principles," and "agents have reduced the advantages of sharing implementation, while the advantages of building for each platform remain." Shopify reports rebuilding its Shop app natively in 12 weeks, with the main Shopify app, more than 300 screens, still in progress. We should read this as what it is: one large company's published reasoning, weeks old, by the same company that made the opposite case in 2020. It is not yet a trend, and the general evidence about coding assistants, which Section 1.5 summarizes and the Software book's Section 5.1 examines in full, is more mixed than any single account. What the Shopify story does show, unmistakably, is that the native-versus-shared decision rests on an assumption about the cost of writing code twice, and that a decision resting on a cost assumption should be revisited when the cost moves.

A middle path has also matured. Kotlin Multiplatform, which shares business logic between Android and iOS while leaving each interface native, was declared stable in November 2023, and Compose Multiplatform extended sharing to the interface on iOS in May 2025. Shared logic suits code that must behave identically on both platforms, and Encore has exactly such code.

#### Backend-driven UI {#c8-backend-driven-ui}

A further option cuts across the first three. In **backend-driven UI**, the server describes a screen as a structure of known components, and the app renders whatever structure it receives. Airbnb's Ghost Platform, described by Ryan Brooks in a 2021 post on Airbnb's engineering blog, is the best documented example: screens are composed of sections, served through a shared data layer, and rendered by the same component vocabulary on web, iOS and Android. The appeal is obvious. A screen defined on the server can change on the server's schedule, which for a native app means changing without a release, without review and without waiting for fans to update.

The price is paid in native feel, in testing, since the space of screens the app may be asked to render is no longer fixed at build time, and in old apps, which can break when a server sends a component they do not know. Backend-driven UI therefore works only under three conditions together: a component library already exists on every client; old clients can skip unknown components without failing; and the screens genuinely change faster than the release train can carry them.

Encore uses it for one screen, the event page, which differs by organizer: a festival wants a lineup grid and a camping map, a stadium tour a date picker across 12 cities. The variety changes weekly. The Design System team's native components already cover the building blocks, and the fan BFF, which the Architecture book's Section 8.4 gave to each experience, already versions its responses by app version, so old clients simply omit what they cannot draw. Everything else stays native and fixed in the binary, the ticket view above all, because the moment it most needs to render is the moment the network is least likely to be there.

#### The decision record {#c8-decision-record}

The Architecture book's Section 1.4 taught the architecture decision record (ADR), after Michael Nygard's 2011 essay, and the format need not be taught again. Mobile decisions add one element that deserves more emphasis than it gets: **reversal conditions**, the observable facts that would make us reopen the decision. Shopify's 2026 post is a reversal condition being triggered, "a core assumption changed," and the decision was reopened on that ground. A mobile platform decision commits forty teams for years, and the cheapest moment to say what would change our minds is the day we decide.

Encore's record for the fan app is short, and its last section is the part most teams leave out.

```
ADR-031  How Encore builds the fan app            Status: accepted, year 7
Decision: Native apps (Swift, Kotlin) for fans; web for organizers.
  Shared Kotlin Multiplatform module only for ticket rendering and
  barcode rotation (identical behavior is a correctness requirement).
  Backend-driven UI only for the organizer-specific event page.
Because: the ticket must open offline and fast on every supported phone;
  rotation must match the gate's validator exactly on both platforms;
  the organizer console is desk work and needs no store.
Reversal conditions (reviewed each January):
  - a shared-logic defect ships to fans twice in one quarter;
  - building a typical feature twice costs more than 1.5× building it once,
    measured over two quarters;
  - a platform drops a capability the ticket view depends on.
Owner: Mobile App team, with the Design System and Venue Entry teams.
```

The second condition is the one the Shopify story bears on. Encore measures it, imperfectly, by comparing the recorded effort for the two halves of features built twice; it has not been triggered.

**Recap.** A channel map assigns each customer job to one owning channel and names a fallback, because every channel fails and several belong to other companies. Native, cross-platform and web each buy something real, and the published record, from Airbnb in 2018 to Shopify in 2020 and again in 2026, shows that the right choice depends on costs that move. Backend-driven UI earns its keep only where components already exist, old clients degrade safely and screens change faster than releases. A decision record for mobile should say in advance what would reopen it.

**Exercise 8.1.** Write your own channel map. List every customer job your product supports, the channel that owns each, and the fallback when that channel fails. Mark every channel you do not control. For any job without a fallback, write one sentence on what a customer experiences on the day its owning channel fails.

### 8.2 Releasing Through a Store

#### Mistakes are not reversible {#c8-not-reversible}

On the web, a defect has a lifetime measured from the deploy that introduced it to the deploy that removed it, and with a good pipeline that lifetime is minutes. A defect in a native app has a lifetime with three parts, and only the first is under our control. We must build and test a fix. We must then pass review: Apple states that on average 90% of submissions are reviewed in less than 24 hours, though developers report longer waits at busy times; an expedited review exists for critical fixes. And then, longest of all, we must wait for fans to update. Some update the same day, many within a week, and a stubborn minority never do. Orosz gives an early chapter to exactly this point, under the title "Mistakes Are Hard to Revert," and it is the root from which most of mobile release engineering grows. The honest figure for a mobile defect is a day or more to ship the fix, then days to weeks before most users have it, and months before nearly all of them do.

Publishing has lived with this for centuries. Once a print run leaves the bindery, an error is permanent in every copy sold, so printers invest heavily in proofs: a mistake caught at proof costs a pencil mark, and one caught in the bookshop costs a reprint. The analogy breaks in an instructive direction. A printed book is inert, while a shipped app keeps executing and keeps reacting to whatever data we send it, so an old version can begin to fail long after it shipped, without any change to its own code.

The clearest public demonstration came on 6 May 2020. A change on Facebook's servers caused many apps that embedded Facebook's iOS software development kit (SDK), Spotify, TikTok, Pinterest and Tinder among them, to crash at launch, including for users who had never logged in with Facebook. The apps' own code had not changed. Code already on millions of phones had read a remote response it could not handle, and none of the affected companies could ship a fix faster than Facebook could revert its server change. It happened again on 10 July 2020. The lesson for release engineering is broader than third-party libraries, though Section 8.4 returns to those. A binary we cannot recall is exposed to every remote input it parses, so what a mobile app reads at launch is part of its release surface, and it must fail safe.

That is why testing and flagging are worth more on a phone than on the web. The Architecture book's Section 8.4 called the seam between the fan app and its backend a contract measured in years; the release engineer's corollary is that the levers which shorten a defect's life after shipping are only the ones designed in beforehand.

#### The release train {#c8-release-train}

A **release train** is a fixed release cadence on which a new version leaves at a scheduled time with whatever is ready, and features that are not ready wait for the next one. Like a railway timetable, it does not wait for a late passenger. The alternative, a release that waits for a set of features, turns every late feature into a late release and every late release into pressure to cut testing. A feature that misses a weekly train loses a week, which is cheap, but only if it was built to be switched on separately from its arrival, as Section 8.4 explains.

The best evidence for trains comes from Facebook. In a peer-reviewed paper at the 2016 Foundations of Software Engineering conference, Chuck Rossi, Kent Beck and colleagues reported that Facebook's Android app had moved over four years from a release every eight weeks to one every week, and that across seven years of data, more frequent releases had not reduced either productivity or quality. They singled out dogfooding, the practice of employees using pre-release builds every day, and alpha and beta feedback, as critical to release quality. Spotify described its own weekly train in 2025 in unusual detail. The release branch is cut on Friday, after which "only critical bug fixes are permitted"; a public beta is built from the branch; the build goes to the stores the following Monday; roughly 1% of users receive it first and the rest the next day; and Spotify reports that it is "able to roll out more than 95% of releases to all our users." Each release, by Spotify's account, carries perhaps three to five blocking bugs that must be fixed on the branch before it ships. The two accounts, nearly a decade apart, describe the same arrangement: a fixed cadence, a short stabilization period on a branch, and a gradual exposure.

The beta tracks are where the train earns its safety. TestFlight on iOS and the testing tracks on Google Play put a build into real hands before review. A staff beta catches what automated tests cannot imagine, and a public beta of volunteer fans catches what staff cannot, because staff phones are newer, staff networks better and staff know where the buttons are.

Encore runs a weekly train, and its week is arranged around the one day the company cannot afford surprises. Figure 8.2 shows it.

| Day | Step | Who |
|---|---|---|
| Monday 12:00 | Branch cut; only fixes for blocking bugs after this | Mobile App team runs the cut |
| Monday–Tuesday | Staff beta (about 600 Encore staff) and public beta (about 20,000 fans) | Module owners triage |
| Wednesday | Regression pass on the critical journeys; go or no-go | Release captain, a rotating role |
| Wednesday | Submit to both stores | Release captain |
| Thursday | Begin rollout if review has cleared | Release captain |
| Friday | No rollout step widens while a major on-sale is running | Calendar, as for server canaries |
| Following Monday | Widen, if the halt criteria of Figure 8.3 are clear | Release captain |

*Figure 8.2 — Encore's weekly app train. A missed train costs a feature one week; it never delays the train.*

The Friday rule is the mobile form of the Resilience book's policy (Section 4.3) that server canaries take no steps during on-sales: a rollout step on an on-sale morning would mix two sources of change in the hour that can tolerate the fewest surprises.

#### Staged rollout and halting {#c8-staged-rollout}

A train that delivers every release to every fan at once would turn each defect into a defect for everyone. Both stores therefore let a new version reach users gradually, and the mechanics differ in ways that matter. The general theory of progressive delivery, canaries and their analysis belongs to the Resilience book's Section 4.3; this section adds only what the stores allow and what they do not.

Apple's phased release spreads an update over seven days, at 1%, 2%, 5%, 10%, 20%, 50% and 100%, but only among users with automatic updates on; Apple's documentation is explicit that the update "can be manually downloaded from the App Store by anyone at any time." The phasing can be paused for up to 30 days in total, or ended early, but never reversed: a paused version stays on the store and on every phone that has it, and restarting a controlled rollout means withdrawing the version and submitting another. Google Play gives more control, since the developer sets the percentage and halting stops new users from receiving the version, but users who already received it "will remain on that version."

Neither store, then, offers a rollback. A mobile "rollback" is always a roll forward, either a new build that undoes the defect or a remote switch that disables it, and it is the Resilience book's roll-forward principle in its strictest form. A staged rollout limits how many fans a defect reaches before we notice it. It does not undo the defect for the fans it has reached.

Halt criteria must be written before the rollout begins, for the reason the Resilience book gave for error budget policies: decisions made in calm weather are better than decisions made in an incident channel. Google publishes two thresholds with consequences. A user-perceived crash rate above 1.09% overall, or 8% on any single phone model, or a user-perceived rate of "application not responding" (ANR) events above 0.47% overall, or 8% on any model, measured over 28 days, may lead Google Play to reduce the app's visibility and warn on its store listing. Those lines separate unacceptable apps from merely poor ones, so Encore treats them as distant ceilings. Its own criteria, in Figure 8.3, sit well inside them and add the one measure no store can compute.

| Signal (new version, versus the previous one) | Halt when | Why |
|---|---|---|
| Crash-free sessions | Below 99.8%, or 0.1 points below the previous version | Encore's own floor |
| Android user-perceived crash rate | Above 0.5% on any day | Half of Google's 1.09% line |
| Android user-perceived ANR rate | Above 0.25% on any day | Half of Google's 0.47% line |
| Ticket opens successfully, online or offline | Below 99.95% of attempts | The job of the third row of Figure 8.1 |
| Checkout completion | Down by more than 1 point at equal traffic | Guardrail from Chapter 4 |

*Figure 8.3 — Encore's halt criteria for a staged app rollout. Any single line halts; widening needs all of them clear.*

The fourth row matters most. A version in which the ticket fails to render offline would show up nowhere in the store's numbers, because the app would not crash; it would show a spinner to a fan in a queue. So the Mobile App team records every attempt to open a ticket and whether a barcode appeared within a second, queuing the measure on the device until the network returns.

#### The long tail and forced upgrades {#c8-long-tail}

A web product has one version in production, or two during a deploy. A mobile product has dozens, and the shape of their distribution is a long tail: most sessions come from the last few versions, and a thin but stubborn fraction comes from versions many months old. At Encore, the oldest version still above 1% of sessions is about 14 months old, and versions up to two years old still open the app on match days, usually on phones that were used for one festival and then forgotten in a drawer. Every one of those versions still calls the fan BFF, which is why the Architecture book's Section 8.4 had that BFF version its responses, track live app versions and keep a forced-upgrade floor. The architecture is settled there. What remains is a set of product decisions, which architecture cannot make.

The car industry knows this tail. A manufacturer recalling a car can write to every registered owner but cannot drive the cars to the workshop, and some owners never bring them in. Aviation shows the other end. An airworthiness directive legally obliges every operator of the affected aircraft to make a correction by a deadline, and an aircraft that has not complied may not fly. A **version floor** is the app's directive: the minimum app version the backend will serve, below which the app must update before it can continue. Like the directive, it should be used rarely, and the analogy breaks over who bears the cost. An airline pays for its own grounded aircraft; a fan blocked by a hard floor pays for ours.

So Encore distinguishes two floors. Below the **soft floor**, the app shows a prompt explaining why an update is worth having and lets the fan continue. Below the **hard floor**, the app refuses everything except one thing, and the exception is the heart of the policy: **the ticket must still open**. A fan whose app is too old to buy, list or browse can still show a valid ticket at the gate, because the ticket view and its rotation logic are deliberately the most stable code in the app. Android offers a system mechanism for prompting updates, the Play in-app updates API with its "immediate" and "flexible" flows, which correspond roughly to the hard and soft floors; iOS has no equivalent, so the app checks its version against the backend and deep-links to the store.

The authority to raise the floor sits with the Mobile App team's product manager, who must consult the product trio of any module whose users the change strands, and it is exercised for three reasons only: security, a store requirement, or one of the fairness invariants. Verified Resale supplied the third reason. A fan running a version that predates reissue would, as a seller, go on seeing a ticket the gate will refuse, and, as a buyer, could not display the new one at all. The gate's revocation list keeps that from becoming a fairness failure, as Section 8.3 explains, but it would still be a fan turned away with a ticket that looked valid on the phone. So Encore did two things. It raised the soft floor to the first version carrying the reissue-aware ticket view three months before launch, and watched the share of active ticket holders below it fall week by week. And it made that version a requirement for taking part in resale at all: an app below it cannot list a ticket or buy one, and offers the update instead. The general hard floor did not move, because no fan who merely holds a ticket needed to be stranded for resale to be safe.

A quieter piece of the same work concerns the cached ticket on the phone, with its rotation secret, seat and status. It has a schema of its own, and Orosz's chapter on client-side data migrations draws the tedious rule: every new version must migrate every older cache it may find, because there is no knowing which version a fan is updating from.

#### Store policy as a dependency {#c8-store-policy}

The last consequence of 2008 is the one most often discovered too late. A store's rules are an API owned by someone else, with no versioning promise, and like any such API it deserves an owner who reads its changelog. Several rules bear on Encore directly, and the useful habit is to check them before design, while they can still shape it.

The first concerns payment. Apple's guideline 3.1.3(e) states: "If your app enables people to purchase physical goods or services that will be consumed outside of the app, you must use purchase methods other than in-app purchase to collect those payments, such as Apple Pay or traditional credit card entry." A concert is consumed outside the app, so in-app purchase does not apply to Encore's primary or resale sales. The check was made before the resale checkout was designed, and recorded so that it can be revisited if the rule changes. No guideline mentions ticket resale at all, which is itself worth knowing.

Other rules impose a calendar. Google Play requires apps to target a recent Android API level by 31 August each year, which forces a yearly Android update whatever the roadmap says. Apple's privacy manifests, enforced from 1 May 2024, require apps and many SDKs to declare the data they collect. And in the European Union the Digital Markets Act has, since iOS 17.4 in 2024, allowed alternative app marketplaces and payment providers on iOS; the fee terms have changed more than once, and Encore has no need of them.

At Encore, the Mobile App team keeps a **policy watch**: a short register of the store rules the app depends on, each with the guideline number, the date last checked and the decision it supports, reviewed monthly and whenever Apple or Google publishes changes. It is the same discipline a team applies to a vendor's API, applied to a vendor that also reviews every release.

**Recap.** Store review and binary distribution give a mobile defect a long life that only the binary's owners can end, which is why testing, trains and switches are worth more on phones than on the web. A weekly train with beta tracks, as Facebook and Spotify have documented, keeps the cadence regular and the cost of a missed feature small. Staged rollouts limit exposure but never undo it, so halt criteria must be written in advance and must include the product's most important job. The version floor is a rarely used instrument whose policy matters more than its mechanism, and store rules are a dependency to be read before design.

**Exercise 8.2.** Plot the share of your app's sessions by version for the last 30 days. How old is the oldest version above 1%? Then write down what a user on that version can still do if you raise your hard floor tomorrow, and who in your organization has the authority to decide it.

### 8.3 What Only Phones Do

#### Tickets offline {#c8-tickets-offline}

A stadium gate is one of the worst network environments a consumer product will ever meet: tens of thousands of phones on the same cell in the same half hour, and a fan at the front of the queue who needs the ticket now. The first rule of the ticket view follows: it must open with no network at all. Everything the phone needs to display a valid ticket must already be on the phone, and the gate must be able to check it without asking anyone.

That rule collides with the second requirement, which is that a ticket should be hard to copy. A static barcode, the kind printed on a PDF, is just an image, and an image can be screenshotted and sent to five friends, of whom the first to reach the gate gets in. (The Architecture book's Section 3.1 called Encore's entry credential a QR code; it is the same thing that this book, following the trade, calls a barcode.) The industry's answer is the **rotating barcode**: a code generated on the device from a per-ticket secret and the current time, so that it changes every few seconds and a screenshot expires almost as soon as it is taken. Ticketmaster introduced the best-known version, SafeTix, in 2019, with a barcode that refreshes every 15 seconds. The mechanism underneath is the time-based one-time password of RFC 6238, published in 2011 for two-factor login codes: a shared secret and a clock produce the same short code on two machines that never talk to each other.

What rotation buys is narrower than the marketing suggests. In 2024 an independent researcher writing as conduition published a reverse-engineering of SafeTix which found, as the design implies, that the codes are computed from secrets the app downloads in advance, so anyone who extracts the secrets can generate them too. Rotation stops the screenshot and the forwarded image, which is most of the problem in practice, but not a determined holder, and so it is only half of Encore's design.

The other half is the **revocation list**: a list, held by every gate scanner, of ticket identities that are no longer valid, so that the scanner can refuse them without a network. Each scanner, run by the Venue Entry team's software, holds the per-ticket secrets it needs to validate codes and the list of revoked identities for its event, syncs both every 30 seconds while it has a connection, and may run offline for up to four hours. When Encore reissues a resold ticket, the old identity joins the revocation list, the buyer receives a new identity with a new secret, and from that moment the seller's phone can generate perfectly well-formed codes that every gate will refuse. A scanner's clock is part of the system too. RFC 6238 advises validators to accept a small window of adjacent time steps, and Encore's scanners accept one step either side; the app corrects for a fan's wrong phone clock by recording the server's time at each sync and computing codes from the corrected time, so that a fan who set the clock by hand still gets in.

One canonical rule makes the arrangement tight. Encore's default resale window closes two hours before doors open, and organizers may only shorten it. Every revocation for an event therefore exists before the first fan reaches a gate, and a scanner that has synced once after the window closed holds a complete list. A scanner that has not, perhaps because it was switched on in a basement, shows an amber status to the gate supervisor, who knows to move it. The guarantee that the gate never accepts both rests on the list and the window together; nothing the fan's phone does is part of it.

#### Wallet passes {#c8-wallet-passes}

Wallet passes are the convenience channel of Figure 8.1. Apple announced Passbook on 11 June 2012 and shipped it with iOS 6 that September; it became Wallet in 2015. From the beginning a pass could be updated after issue: the device registers the pass with the issuer's web service, the issuer's server sends an empty push when the pass changes, and the device asks what changed and downloads it. Google Wallet offers the same through its own API.

The mechanism works only when the device is online, and its notifications are delivered on a best-effort basis; a phone in airplane mode or in a stadium cell that has given up receives the update later. That draws a hard line around what a wallet update may be trusted with. When a ticket is resold, Fan Messaging, the team that owns the Notifications service, pushes an update that marks the seller's pass "Transferred" and removes its barcode, and delivers a new pass to the buyer. Both are courtesies. The seller's pass might go on displaying its old barcode for hours, and the gate will refuse it, because the revocation list is the guarantee.

The two wallets also differ in what they can show. Google Wallet supports rotating barcodes for event tickets through a `rotatingBarcode` field built on RFC 6238, and Google's guidance keeps the secret out of the token used to save the pass and lists fallbacks in order: its Smart Tap NFC protocol, then the rotating barcode, then a static barcode, noting that the static fallback weakens security. Apple Wallet does not display rotating barcodes; Ticketmaster's rotating tickets in Apple Wallet use near-field communication (NFC), which requires Apple-approved NFC passes. Encore has no such approval. Its Apple Wallet passes therefore carry a static barcode, which is the weakest credential Encore issues, and the company accepts it knowingly: the pass is a convenience, the app is the credential of record, and a forwarded copy of a static pass is defeated at the gate by the same revocation list that defeats a reissued ticket. The cost is that two people holding copies of one unresold static pass race to the gate, which is the old problem in a smaller form. The Resilience book's Section 7.2 holds the signing keys for passes and their rotation.

The buyer's side has a promise attached. The Resilience book's Section 1.2 set Encore's ticket-delivery objective: 99.5% of orders with the ticket in the wallet within five minutes, over a rolling 28 days, measured by Notifications and confirmed by a wallet receipt. A reissued ticket is an order like any other for this purpose, and Verified Resale was designed to meet the existing objective, with no weaker one of its own.

#### Push notifications {#c8-push}

Push notifications are cheap to send, and their costs are borne by someone else, which is why they are so often misused. Both platforms now require the user's permission; Android made it a runtime permission in Android 13, in 2022. Apple's Human Interface Guidelines advise that an app "request permission only when your app clearly needs access to the data or resource," and warn that asking too early "can make it hard for people to trust your app." Encore's app asks the first time a fan buys a ticket, explaining that it will say when doors open and when anything changes about the ticket, and never on first launch, when the fan has no reason to agree.

Apple's guideline 4.5.4 adds two constraints that are product decisions in disguise. Push "must not be required for the app to function," and must not be "used for promotions or direct marketing purposes unless customers have explicitly opted in." Encore therefore keeps two kinds of notification apart. Transactional messages, about a ticket the fan holds, rest on the permission alone. Marketing messages, from the Fan Growth team, need a separate opt-in, recorded with its consent language and revocable in the app.

Underneath both lies a technical fact that settles a design question. When a device is offline, Apple's push service stores only the most recent notification for each app and discards it after a limited time, and Google's equivalent service makes no promise of delivery either. Push delivery is best effort by design. So nothing critical depends on push alone. When a fan's ticket sells, the news travels three ways at once: by push, by email, and as an entry in the app's inbox, which the app fetches whenever it opens. A fan who missed the push, never granted permission or deleted the email will still find the message the next time they look.

#### Deep links {#c8-deep-links}

A **deep link** is a URL that opens a specific screen inside an app when the app is installed and falls back to the same content on the web when it is not. Apple's universal links, from iOS 9, and Android's app links, from Android 6.0, both introduced in 2015, made this reliable by having the app and the website vouch for each other through files the website serves, so that no other app can claim the links. For Encore the deep link is how other channels hand a fan to the app. A link in an email opens the ticket; a link from Rowmate's listing opens the resale checkout with Rowmate's attribution carried in the URL, so that the partner earns its four points of the fee when its link produced the sale.

The history of deep links offers a lesson in the dependency risk of Section 8.2. Many companies built their links on Firebase Dynamic Links, a Google service that handled the install-then-open dance for them. Google deprecated the service and shut it down on 25 August 2025, after which every such link, including those on custom domains, stopped working. Every email ever sent and every partner page ever published with one of those links broke on the same day. Encore owns its link domain and uses the platforms' own verified links, so that the links it prints in emails and hands to partners will work for as long as Encore exists. Partner attribution and the partner API itself belong to Chapter 9.

#### Biometrics and device security {#c8-biometrics}

A completed resale cannot be undone, since the ticket has been reissued to someone else, so Encore asks the fan to confirm a sale with Face ID, a fingerprint or the device passcode. That is sound interface design, and there are two common mistakes in its engineering.

The first is to treat the biometric check as proof. An app that checks the fingerprint locally and sends the server a flag saying "authenticated" has told the server nothing a modified app could not forge. The check proves something only when it unlocks a key held in the phone's secure hardware, the Secure Enclave or the Android Keystore, and that key signs the request. Encore's app registers such a key's public half when the fan signs in and signs each sale confirmation with it. The surrounding rules, no long-lived secrets in the binary and authorization-code sign-in with proof keys, are the Architecture book's Section 7.4.

The second mistake is to confuse this step with the European rules on payment. Strong customer authentication under the revised Payment Services Directive (PSD2), in force since September 2019 and enforced for online card payments in the European Economic Area from the end of 2020, requires two of three factors, knowledge, possession and inherence, and it is carried out by the card issuer or the payment provider, through 3-D Secure or through wallets such as Apple Pay and Google Pay that bundle it. Encore's Face ID on "sell" is Encore's own step-up for an irreversible transfer of a ticket, and not a regulatory requirement; the buyer's payment carries its own strong authentication through Orders & Payments, as every Encore payment does.

**Recap.** A ticket must open with no network, and rotation computed from a pre-delivered secret makes copying harder without making it impossible, so the guarantee against double entry belongs to revocation lists held by the gates and to a resale window that closes before doors. Wallet updates and push notifications are best effort, so they are courtesies that never carry a guarantee, and anything a fan must know travels by several channels. Deep links should rest on domains we own, and a biometric check means something to a server only when it unlocks a key that signs the request.

**Exercise 8.3.** Put your phone in airplane mode and try to use your product's most important artifact: the ticket, the boarding pass, the receipt, the document. Write down what fails, and what the user would have to do at that moment. Then name the component that would have to hold the guarantee if the phone could not.

### 8.4 Flags, Experiments, and Telemetry on Devices

#### Remote configuration {#c8-remote-config}

If a binary cannot be recalled, the next best thing is a binary whose behavior can be changed from outside. **Remote configuration** is a set of flags and parameters the app fetches from a server and applies to code already in the binary, so that a feature can be switched on, tuned or switched off without a release. The kinds of flag and their lifetimes, release, experiment, operational and permission, are taught in the Resilience book's Section 4.3 and the Software book's Section 4.5, and this section adds only what changes when the code reading the flag sits on a phone.

Two things change. The first is that the app cannot count on reaching the server. Firebase's guidance for its remote configuration service is blunt: "Don't rely on network connectivity to obtain Remote Config values," and "Do set in-app default parameter values." Every flag therefore has a default compiled into the binary, and for a risky new feature the safe default is off. The second is timing. Of the loading strategies Firebase describes, the gentlest and most common applies at the next launch the values fetched during this one, and Firebase advises against changing the interface mid-session. The consequence, often discovered in an incident, is that a switch flipped now reaches most users only when they next open the app.

A **kill switch** is a remote flag whose only purpose is to disable a feature quickly when it misbehaves, and a kill switch is only as fast as its slowest path to the phone. Encore's app applies values at the next launch for ordinary flags, and listens for real-time updates to kill switches while it is in the foreground, so that about 80% of active sessions see a flipped switch within 15 minutes. Every risky feature ships behind one, and resale had several: one for listing, one for buying, and one for the reissue-aware ticket view's new status display, which could fall back to the old display without hiding the ticket.

The Facebook SDK crashes of 2020 add a requirement. What the app fetches at launch can itself be the hazard, and third-party SDKs often fetch remote data at launch on their own. Encore's Mobile App team keeps an approved list of SDKs, each with an owner, a privacy manifest and a budget for app size and launch time, and initializes each one behind a kill switch of its own, so that a vendor's bad day can be switched off without a release. Orosz gives a chapter to third-party libraries, and Encore's list rests on the same view: a library inside the binary ships in Encore's release, whoever wrote it.

#### Experiments on clients {#c8-client-experiments}

The statistics of online experiments belong to Chapter 4, and nothing about them changes on a phone. What changes is the plumbing, and Kohavi, Tang and Xu give a chapter of *Trustworthy Online Controlled Experiments* (2020) to the difference between thin clients such as browsers and thick clients such as native apps. Four practical points follow for a team running experiments in an app.

First, every variant must already be in the binary. The server can choose which variant a fan sees, but it cannot send code, so an experiment that needs a new interface waits for a train and then for adoption. Second, assignment must be stable across sessions and devices, which Encore achieves by hashing the fan's account through the same flag service that Chapter 4 described for the web, and caching the assignment on the device so that an offline session shows the same variant as the last online one. Third, exposure should be logged when the fan actually sees the variant, because many fans whose app fetched the configuration never reach the screen, and counting them dilutes the effect; this is the triggering that Kohavi and his co-authors treat at length. Fourth, the population on a new version is not a random sample. Fans who update early differ from those who update late, so an experiment that starts with a new version runs at first on a skewed population, and the app version belongs in the analysis as a covariate. Logs, too, arrive late from offline phones, and their timestamps are only as good as the phone's clock, so the analysis should wait for the stragglers.

Chapter 4's rule for Encore holds on every channel: no experiment ever varies the price an individual fan pays.

#### Crash and performance reporting {#c8-crash-reporting}

The Operations book treats crash triage on call, but it has no mobile material, so the client measures that Encore's halt criteria depend on are defined here. A **crash-free session rate** is the share of app sessions that end without a crash; a **crash-free user rate** is the share of users who experienced no crash over a period. The two answer different questions. Sessions weight heavy users heavily and are the better guide to how the app behaves; users weight everyone equally and are the better guide to how many people were hurt. Google's user-perceived crash rate and the related rate of "application not responding" events, the measures behind the thresholds in Figure 8.3, are counted per daily user and only for crashes the user could notice. Alongside them sit the measures of speed: the time from tapping the icon to a usable first screen, the share of frames drawn late enough for the eye to catch a stutter, and network failures broken down by carrier and country, which at Encore is how a fault in one mobile network shows up before anyone files a complaint.

None of this works without symbolication, the translation of a crash's raw addresses back into function names and lines. The files that make it possible, dSYM files on iOS and mapping files on Android, come from the build and cannot be recreated later, so Encore's pipeline uploads them with every release build and fails the build if the upload fails. Spotify gates store submission on "crash rates and key metrics" below defined thresholds, and Encore's Wednesday go or no-go does the same.

#### Product analytics on devices {#c8-analytics}

Chapter 4 set out Encore's tracking plan and the consent rules under the General Data Protection Regulation (GDPR) and the ePrivacy Directive, and they apply to the app unchanged. It is worth correcting a common confusion about the platform rules, because it leads teams to the wrong checklist. Apple's App Tracking Transparency (ATT), required since iOS 14.5 in April 2021, governs tracking a user across other companies' apps and websites, and access to the advertising identifier. Encore does neither, and if it ever did, ATT would apply. Its own first-party analytics fall under the European rules, under Article 5(3) of the ePrivacy Directive for anything stored on or read from the device, and under Apple's guideline 5.1.1(ii), which says that apps "must secure user consent for the collection, even if such data is considered to be anonymous," and that "paid functionality must not be dependent on or require a user to grant access to this data."

The device adds mechanics of its own. Events are batched to save battery and data, and queued when the phone is offline, with a maximum age, after which they are dropped, since an event that arrives days late would distort analyses already run. Consent is stored on the device and honored before the first event is recorded, which means the consent screen must come before any analytics initialization, a sequencing bug that is easy to ship and hard to notice. Event times are recorded on the phone's clock and corrected with the same server offset the ticket view uses. And each third-party SDK that collects anything appears in the app's privacy manifest.

One feedback channel is particular to apps: the store reviews, prompted sparingly through the platforms' rate-limited in-app rating requests. Each module's trio reads its reviews weekly as one input to the continuous discovery of Chapter 3.

#### Flag debt on clients {#c8-flag-debt}

Flags accumulate, and Orosz's chapter title for the result, "Feature Flag Hell," describes it well enough. The cleanup disciplines, an owner for every flag, an expiry date and removal as part of done, are the Software book's (Section 4.5) and the Resilience book's (Section 4.3). A phone adds one constraint that changes the arithmetic. A flag in a shipped binary is read by that binary for as long as the binary is in use, so the server cannot stop serving the flag, or change its meaning, while any version that reads it remains above the version floor. Removing the code from the next release is easy; retiring the flag takes as long as the long tail takes to drain.

Encore therefore ties every client flag's expiry to a version, and records it in a manifest that the app's build reads and a linter checks:

```yaml
flag: resale.listing.enabled
owner: resale-team
kind: release                  # release | experiment | operational | permission
default_in_binary: false       # safe value when config is unreachable
kill_switch: true              # real-time while app is in foreground
first_version: 9.14.0
code_removed_in: 9.40.0        # planned; linter warns 4 trains before
retire_server_value_when: hard_floor >= 9.40.0
```

The last line is the mobile-specific idea in compact form: **the version floor is the flag's expiry date**. A flag cannot be retired from the server until no supported version reads it, and so every client flag's true lifetime is set by the floor policy of Section 8.2. Encore counts the flags its app reads at launch each quarter. When resale launched there were 212, of which 31 had no named owner; the count of ownerless flags is the number the Mobile App team now reports, because retiring a flag needs someone whose job it is.

**Recap.** Remote configuration lets a fixed binary change its behavior, provided every flag has a safe compiled default and every kill switch has a known reach time. Experiments on devices keep the statistics of Chapter 4 and add their own plumbing: variants in the binary, stable cached assignment, exposure logged on sight and version as a covariate. Client crash and performance measures, defined here because no other book in the series defines them, set the halts of the release train. And the version floor decides when a client flag can finally be retired.

**Exercise 8.4.** Count the remote flags your app reads at launch. For each, record its owner, its default in the binary and the oldest supported version that reads it. How many have an owner and an expiry date? How many could you retire from the server today without breaking a version you still support?

### 8.5 Mobile at Many Teams

#### Modularization {#c8-modularization}

A web storefront can be split among forty teams in several ways, as Chapter 7 showed. A native app offers fewer. In the end it is one binary, built by one pipeline and shipped on one train, and every team's code shares its memory, its launch time and its crash rate. The tool that lets many teams work in one binary is the same one the Architecture book's Section 1.3 recommended for any large system, modules whose boundaries match team boundaries, applied with rules the compiler can enforce.

The published accounts agree on the shape. Uber described its move to a single iOS repository in 2017, and by 2022 its Android app was built from more than 10,000 modules. Slack spent a year from February 2021 breaking its mobile codebases into modules of three kinds, features, services and libraries. Airbnb's iOS engineers described in 2021 a scheme of module types with visibility rules, under which a feature module may not depend on another feature and the two talk only through small interface modules. The common rule is that features never import each other. They depend downward, on shared services and libraries, and sideways only through interfaces, so that a team can change its feature without rebuilding or breaking anyone else's.

Encore's fan app has a thin shell and 14 feature modules, each owned by one team: Discover, Search, Event, Waiting Room, Seat Map, Checkout, Payment Completion, My Tickets, Account, Inbox & Preferences, Help & Refunds, Presales, Festivals and Following. The shell, owned by the Mobile App team, holds navigation, the version check and the wallet ticket view, and very little else. Ownership is enforced where review happens, in a CODEOWNERS file at the root of the repository:

```
# Fan app: one owner per module; shell and build belong to Mobile App
/app-shell/                     @encore/mobile-app
/build-logic/  /ci/             @encore/mobile-app
/features/my-tickets/           @encore/fan-accounts
/features/checkout/             @encore/checkout
/features/payment-completion/   @encore/checkout
/features/inbox/                @encore/fan-messaging
/features/resale/               @encore/resale
/shared/ticket-core/            @encore/mobile-app @encore/venue-entry
/shared/design-system/          @encore/design-system
```

The `ticket-core` line deserves a word. The shared Kotlin Multiplatform module that renders tickets and computes rotating codes has two owners, because its behavior must match the validator in Venue Entry's scanners exactly, and a change that one side reviews alone is a change that can turn fans away at the gate.

#### The mobile platform team {#c8-mobile-platform}

Every published account of mobile at scale ends up with a team whose users are the other mobile engineers; Orosz devotes a chapter to such teams. At Encore that role belongs to the Mobile App team, a stream-aligned team of nine in the fan group which, for the other module teams, behaves as a platform. The Software book's Chapter 6 treats the internal platform as a product in full, and everything it says applies here. The charter is specific to mobile. The team owns the build and its speed; the continuous integration pipeline; the train and the release captain rotation; release tooling and the halt criteria; the version floor; the policy watch; and review of every new third-party SDK. It does not own features, because a platform team that also builds features is tempted, under deadline, to put its own first.

#### Build and test pipeline {#c8-build-pipeline}

Build time is the quiet tax on a large app. Encore's median clean build of the fan app takes about 24 minutes on a developer laptop and its median incremental build about 90 seconds; both are reported monthly as developer-experience measures (the Software book, Section 6.5), and caching, sharding and continuous integration as a product are its Sections 4.2 and 4.4. Two points are particular to mobile. Real-device tests are slow and costly, so Encore's device farm runs only the critical journeys, buying a ticket, opening it offline, listing it and receiving a reissued one, on the oldest and newest supported operating systems. And snapshot tests, which compare a rendered screen with a stored image, break whenever the operating system changes its fonts, so their simulator image is pinned and upgraded deliberately. Spotify lets teams with enough automated coverage opt out of manual regression, and Encore applies the same rule module by module.

#### Shared native design system {#c8-native-design-system}

Chapter 7 described Encore's design system, its tokens and its governance, and Chapter 6 the accessibility requirements, including the European Accessibility Act, which since 28 June 2025 covers consumer e-commerce apps as well as websites. On native platforms the Design System team shares the tokens with the web, colors, spacing and type scales generated from one source, and builds the components natively for each platform. It never wraps web components inside the app, because a wrapped web control behaves like neither platform. Where a platform's conventions conflict with a token, the convention wins: navigation follows iOS and Android patterns, and text follows Dynamic Type on iOS and font scaling on Android, so that a fan who has set large text gets large text. Every component is tested with VoiceOver and TalkBack before release, and the governance is Chapter 7's, unchanged.

#### Who owns a cross-cutting change {#c8-cross-cutting}

Verified Resale is the kind of change modules are designed to resist. It added a fifteenth module, Resale, and it reached into three that belong to other teams: the shell's wallet ticket view, which the Mobile App team owns; the inbox and pass updates of Fan Messaging; and the Design System's components for the Verified badge, the capped price and the reissue status. My Tickets and Checkout were touched only through interfaces they already exposed, so their teams were consulted and asked for nothing. Encore's answer, which no textbook names but which fits the collaboration mode Skelton and Pais describe in *Team Topologies*, was to give the change one owner, the Resale team, and to ask each module owner for a time-boxed contribution: a reviewed interface for the Resale module to call, or a small change made by the owning team on an agreed train. Team design in general is the Software book's Section 9.2, and cross-team planning its Section 10.2. The capstones of both books trace the same change from the product side and the engineering side.

What made the plan workable was that it was **train-aware**, which is to say laid out backward from the launch on the weekly calendar of Figure 8.2. The resale code shipped dark, behind the kill switches of Section 8.4, eight trains before launch, so that it could ride to fans' phones well before anyone used it. The reissue-aware ticket view shipped first of all, because it had to precede the soft floor by enough weeks for adoption to begin. The soft floor rose three months before launch. Staff and the public beta exercised listing and buying on real events for four trains. Only then, with the code already on the great majority of phones and the floor already in place, was the flag turned on for three organizers in France. No train was held for resale, and no feature had to arrive on the day it was switched on.

**Recap.** Many teams can share one binary when modules match teams, features never import one another and CODEOWNERS enforces the boundaries. A mobile platform team owns the build, the train, the floor and the rules of the store, and never features. Build time, device tests and snapshot tests need deliberate care, and a native design system shares tokens with the web while building every component natively and accessibly. A change that crosses modules needs one owner, time-boxed help from the others and a plan laid out on the train's calendar, with code shipped dark long before it is switched on.

**Exercise 8.5.** Measure your app's median clean and incremental build times over the last month. Estimate the engineer-hours a year they cost, and what halving each would require. Then take your largest recent cross-module change and draw it on your release calendar: when did its code reach phones, and when was it switched on?

### Kata: Unlocking Underground

> **Your brief: "Pedal."** Pedal runs bike sharing in 12 European cities, with about 40,000 bikes and 1.6 million monthly riders, and its app is the only way to unlock a bike. Eight mobile teams of about six engineers each build one native app on a fortnightly release that slips about one time in three, and a ninth team builds the lock firmware, which updates over the air and is just as hard to recall as the app. About 9% of unlocks happen in underground garages and stations with no signal, where the app currently waits for the server and times out; riders walk away, and support tickets peak every rainy Monday. Last spring a parsing bug in one version made the app crash whenever a city added a new bike type, and it took five weeks for crashes to fall below 1% of sessions, because the version floor had never been used and nobody knew who could raise it. The fleet team also wants stolen or reported bikes refused at the lock even when lock and phone are both offline. Pedal's leadership is debating a cross-platform rewrite.

**Deliverables:**

1. **Channel map and decision record** — Map every rider job (find, unlock, pay, end the ride, report a fault) to its owning channel and fallback, as in Figure 8.1. Write the ADR for how Pedal builds its app, including what would be shared between platforms and the reversal conditions that would reopen the decision.
2. **Offline unlock design** — Design an unlock that works with no network on the phone or the lock: what secret each holds, how time is handled, and how long a pre-delivered credential lives. Say how a stolen bike is revoked when nothing is online, and how the window between revocation and the lock's next sync is kept short.
3. **Release train and halt criteria** — Lay out a weekly train with a branch cut, beta tracks and staged rollout on both stores. Write halt criteria that include the unlock success rate, offline and online, alongside the store's crash and responsiveness lines.
4. **Version floor and flag policy** — Write who may raise the soft and hard floors and for what reasons, and what a rider below the hard floor can still do. Write a flag manifest entry, like the one in Section 8.4, for the new bike-type parser, with its expiry tied to the floor.
5. **Firmware and app together** — Explain how an app release and a lock firmware release that depend on each other are sequenced so that neither ever has to arrive before the other.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Fallbacks | Does every rider job survive the failure of its owning channel, including the network itself? |
| Honest security | Does the offline design say what a determined attacker with a rooted phone can and cannot do? |
| Irreversibility | Do the train, rollout and halt criteria assume that a shipped version cannot be withdrawn? |
| Floor policy | Would last spring's crash have been contained within days, and does the policy name the person who decides? |
| Flag lifetimes | Does every flag's retirement depend on a version floor, and is someone named to retire it? |
| Sequencing | Are firmware and app changes shipped dark and switched on only once both are in place? |

#### Where you now stand

You can now map a product's jobs to channels with a fallback for each, choose how to build an app and say in advance what would change your mind, run a release train whose halts include the job that matters most, and set a version floor that strands as few people as possible. You can design an artifact that works offline, say honestly what its security buys, keep guarantees out of best-effort channels, and organize many teams around one binary. One question has hovered at the edge of the chapter. Rowmate hands fans to Encore through deep links, partners list tickets through Encore's interfaces, and the fan app itself is, as the Architecture book put it, a public API consumer that happens to be Encore's own code. Interfaces that others build on are products in their own right, with users, versioning promises and support, and Chapter 9 takes them up.

### References

- Gergely Orosz — [*Building Mobile Apps at Scale: 39 Engineering Challenges*](https://www.mobileatscale.com/). The Pragmatic Engineer, 2021.
- Chuck Rossi, Elisa Shibley, Shi Su, Kent Beck, Tony Savor, Michael Stumm — [*Continuous Deployment of Mobile Software at Facebook (Showcase)*](https://www.eecg.utoronto.ca/~stumm/Papers/Rossi-FSE-16.pdf). Proceedings of FSE 2016, ACM, 2016 — free online.
- Jacob Vesterlund — [*A Behind-the-Scenes Look at How We Release the Spotify App (Part 1)*](https://engineering.atspotify.com/2025/4/how-we-release-the-spotify-app-part-1). Spotify Engineering, 2025 — free online.
- Ron Kohavi, Diane Tang, Ya Xu — [*Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*](https://experimentguide.com/). Cambridge University Press, 2020.
- Mustafa Ali — [*Native is now the future of mobile at Shopify*](https://shopify.engineering/back-to-native). Shopify Engineering, 2026 — free online.
- Farhan Thawar — [*React Native is the Future of Mobile at Shopify*](https://shopify.engineering/react-native-future-mobile-shopify). Shopify Engineering, 2020 — free online.
- Gabriel Peal — [*Sunsetting React Native*](https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a). Airbnb Engineering, 2018 — free online.
- Apple — [*Release a version update in phases*](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/) and [*App Store Review Guidelines*](https://developer.apple.com/app-store/review/guidelines/). Apple Developer documentation — free online.
- Google — [*Release app updates with staged rollouts*](https://support.google.com/googleplay/android-developer/answer/6346149) and [*Android vitals*](https://developer.android.com/topic/performance/vitals). Google Play and Android documentation — free online.
- Apple — [*Adding a Web Service to Update Passes*](https://developer.apple.com/documentation/walletpasses/adding-a-web-service-to-update-passes). Apple Developer documentation — free online.
- Google — [*Rotating Barcodes*](https://developers.google.com/wallet/tickets/events/resources/rotating-barcodes). Google Wallet documentation — free online.
- conduition — [*Reverse Engineering TicketMaster's Rotating Barcodes (SafeTix)*](https://conduition.io/coding/ticketmaster/). conduition.io, 2024 — free online.
- D. M'Raihi, S. Machani, M. Pei, J. Rydell — [*RFC 6238: TOTP: Time-Based One-Time Password Algorithm*](https://www.rfc-editor.org/rfc/rfc6238). IETF, 2011 — free online.
- Ryan Brooks — [*A Deep Dive into Airbnb's Server-Driven UI System*](https://medium.com/airbnb-engineering/a-deep-dive-into-airbnbs-server-driven-ui-system-842244c5f5). Airbnb Engineering, 2021 — free online.
- Firebase — [*Remote Config loading strategies*](https://firebase.google.com/docs/remote-config/loading). Firebase documentation — free online.
- Apple — [*iPhone App Store Downloads Top 10 Million in First Weekend*](https://www.apple.com/newsroom/2008/07/14iPhone-App-Store-Downloads-Top-10-Million-in-First-Weekend/). Apple Newsroom, 14 July 2008 — free online.

---

## Chapter 9: APIs as Products — Designing, Governing, and Supporting the Interfaces Others Build On {#ch9}

> The endpoints tell a partner what it can build. The terms tell it whether building was wise.

Chapter 8 dealt with software we cannot recall: an app on a fan's phone keeps calling our backend long after we have shipped something better. An application programming interface (API) puts us in the same position at one remove, because there the code we cannot recall belongs to someone else. A partner builds its product against our contract and plans its year around it, and from then on every change we make lands in a business we do not run. The Architecture book's Chapter 7 settled how Encore's public API at `api.encore.com` is shaped, evolved, secured and governed. This chapter asks a product question about the same interface. What does it take for an API to be something other companies choose to build on, and go on building on, year after year? The sections that follow answer in turn: design from the consumer's job outward, adopt patterns once, keep 40 teams consistent without a review board, run the partner API as a product with its terms, and run the webhooks that tell partners what happened.

The terms deserve particular attention, and the clearest lesson in why comes from Twitter. Twitter launched in July 2006 and opened its API early, and for several years it let outside developers invent much of what people came to think of as Twitter. The Iconfactory's Twitterrific, released for the Mac in January 2007, was among the first third-party clients; it gave Twitter its first bird icon and was the app that popularized the word "tweet". Other clients followed, and Twitter began to buy them: Tweetie in 2010, which became the official iPhone app, and TweetDeck in May 2011, reportedly for about $40 million.

The turn came in stages. On 11 March 2011 Ryan Sarver, Twitter's head of platform, told developers on Twitter's developer mailing list that they should not "build client apps that mimic or reproduce the mainstream Twitter consumer client experience". On 16 August 2012 Twitter's Michael Sippey published "Changes coming in Version 1.1 of the Twitter API". Part of it was ordinary engineering: authentication on every endpoint, and limits per endpoint, 60 calls an hour for most and 720 for a few, in place of a flat 350. The rest changed the Developer Rules of the Road. Display guidelines became Display Requirements, backed by "we reserve the right to revoke your application key". Client apps pre-installed on devices would need Twitter's certification. And any app that used the home timeline, account settings, direct messages or User Streams "will need our permission if your application will require more than 100,000 individual user tokens". Apps already past that line could grow to 200% of their token count as of that day and then add no more users without permission.

Notice what did not change in 2012. Every endpoint kept working. What changed was who could call them, how many people an app could serve and how a tweet had to look on screen, and those rules lived in a policy document. They reached far into other companies' businesses. When Tapbots shipped Tweetbot for Mac on 18 October 2012, it priced the app at $19.99, because its allotment of user tokens was fixed and Twitter would not raise it; a clause in one company's API policy had set the retail price of another company's product. Still, the 2012 changes came with notice. They were announced weeks ahead, existing apps kept room to grow, and the old API's retirement was extended twice. The second act had no notice at all. Elon Musk's ownership of Twitter began in late October 2022, and around 12 and 13 January 2023 Tweetbot, Twitterrific, Echofon and other clients simply stopped working. On 17 January @TwitterDev said that "Twitter is enforcing its long-standing API rules". Two days later the Developer Agreement gained a clause against using Twitter's content to "create or attempt to create a substitute or similar service or product to the Twitter Applications", and the Iconfactory discontinued Twitterrific after 16 years, describing "an unannounced and undocumented policy change by an increasingly capricious Twitter".

The strategic question of how far a company should open its platform belongs to Chapter 2 and to the Software book's Section 8.1. This chapter takes from Twitter one narrower lesson, about contracts: what a partner depends on includes the terms around the endpoints, and what most decides whether a partner can live with those terms is notice. Since its sixth year Encore has run Partner Listings, a one-way arrangement in which authorized partners read Encore's event listings and post links to resale offers held on their own sites. Verified Resale turns that into a two-way product. Partners will read each organizer's resale rules, list tickets that fans bought through the Sale Gate, receive orders when another screened fan buys, and learn the result of the reissue that gives the buyer a new barcode. Rowmate is the launch partner, and Tessera follows. The Partner APIs team owns this surface over the Resale service, and the chapter follows it from its first job story to a certified partner and the `listing.sold` webhook.

### 9.1 Designing from the Outside In

#### Job stories to capabilities {#c9-job-stories}

Most APIs are designed from the inside out. A team has a service, the service has tables, and the API appears as a set of doors into those tables. The Architecture book's Section 7.1 warned against exporting the schema, but a warning tells us what to avoid without telling us where to begin. Designing from the outside in begins with the consumer's situation and works inward until it reaches the resources and verbs, so that the shape of the API is decided by the work it supports.

The most useful starting form is the **job story**: a requirement written from the consumer's situation, in the form "When [situation], I want to [motivation], so I can [outcome]". Alan Klement described the format in 2013 and credited it to the product team at Intercom. Section 2.2 taught jobs to be done, and we will not teach it again here. The step this chapter adds is the move from a job to an API. James Higginbotham's *Principles of Web API Design* (2021) calls the thing in between a **digital capability**: something the API lets a consumer accomplish, named in the consumer's words, before any resource, path or verb has been chosen. His process has four phases, which he calls ADDR: Align, Define, Design and Refine. Job stories and capabilities are the alignment phase, the point at which the API is tied to the discovery work of Chapter 3.

Rowmate's first job story came straight out of the discovery interviews. "When a fan lists a ticket on our site, I want to know at once whether the organizer allows it, so the listing never fails later." Everything that matters in that sentence is about timing and failure. The capability it yields is "check whether a ticket may be listed, and at what price", and it says nothing yet about endpoints. A second story, from the same interviews, was "When a listing sells, I want to know before the buyer leaves our checkout page, so I can show them their ticket is on its way". Its capability is "learn that a sale completed and what happened to the ticket". Holding capabilities in the consumer's words for a while keeps the team from reaching too early for the nouns it already owns.

The touring world has an old instrument for this. A touring act sends every venue a technical rider listing what the show needs: power, rigging points, stage size, hands at load-in. The venue that reads the rider before the trucks arrive builds what the show needs, and the one that does not finds out at four in the afternoon. Job stories are an API's rider, written from the consumer's side. The analogy breaks on the number of authors. A venue reads one rider from one act it has booked. An API serves many consumers, most of whom never write anything down, so the provider has to write the riders on their behalf and then check its drafts with real consumers. Job stories are widely used but have no outcome studies behind them; their value here is that they make the consumer's situation the first thing written down and tie the API to the discovery evidence that justified it.

#### Walking the paths {#c9-capabilities-canvas}

A capability is a goal; an API needs operations. The bridge between them is to walk the consumer's journey step by step and ask, at each step, what the consumer needs from us. Arnaud Lauret's *The Design of Web APIs* (second edition, 2025) gives this a one-page tool, the API Capabilities Canvas, on which a team writes the journey's steps, the actors, the inputs and outputs and the operations that fall out. The canvas is one author's method. The practice beneath it is much older. Alistair Cockburn's *Writing Effective Use Cases* (2000) taught a generation of analysts to write the main success scenario first and then its extensions, the alternative and failure paths, because the main path finds the obvious operations and the extensions find everything else.

The nominal path for Verified Resale is short. A fan lists a ticket at Rowmate. Rowmate checks the organizer's rules and creates the listing. Another fan finds it, passes Bot Screening and buys. Encore reissues the ticket under a new barcode, the new ticket reaches the buyer's phone, and five days after the event the seller is paid. Walking that path yields the operations everyone expected: read the rules, create a listing, receive an order, learn the reissue result.

The failure paths are where design earns its keep. One question asked at the canvas was simple: what happens when the organizer changes the rules after a ticket is listed? Organizers may only tighten, so the change is always toward fewer listings: a lower cap, a shorter window, resale switched off for the event. A ticket listed at its €60 face value is now above a new €50 cap. Nobody had planned an operation for that moment. Walking the path showed two. Encore needed a way to tell partners the rules had changed, which became a `rules.changed` event, and it needed a defined fate for listings that no longer complied. The team chose to withdraw them, with the reason `rule_change`, and let the seller list again within the new rules, which kept the listing lifecycle to its existing six states instead of inventing a seventh.

| Path | Step | Capability | Operation |
|---|---|---|---|
| Nominal | Fan starts a listing at the partner | Check whether a ticket may be listed, and at what price | Create a listing with `validateOnly` |
| Nominal | Fan confirms | List the ticket | Create a listing |
| Nominal | Another fan buys on the partner's site | Sell a listed ticket to a screened buyer | Create an order |
| Nominal | Encore reissues the ticket | Learn that the sale completed and what happened to the ticket | `listing.sold` event; read the reissue operation |
| Alternative | Seller changes their mind | Take a listing down | `:withdraw` |
| Failure | Organizer lowers the cap after listing | Learn that the rules changed, and which listings they affect | `rules.changed` event; listings withdrawn with reason `rule_change` |
| Failure | Reissue cannot deliver to the buyer's phone | Learn that delivery is delayed, and what Encore is doing | Reissue operation reports a failed stage and its retry |

*Figure 9.1 — Part of the capabilities canvas for Verified Resale's partner API. The three nominal rows were on the whiteboard before the session began; the failure rows came from walking the paths.*

#### From capabilities to API boundaries {#c9-api-boundaries}

With operations in hand, the next decision is how to group them into APIs. The Architecture book's Chapter 3 already taught the workshop for this, EventStorming, and the bounded contexts it draws, and we take those contexts as given. What Higginbotham adds is the step from a context to an API boundary, and two ways of getting it wrong. One is the **mega-API**, a single surface that gathers every capability of several contexts and so couples teams who should change independently. The other is the **per-entity API**, one API for each noun, which leaves the consumer to orchestrate a dozen calls across surfaces that were never designed to be used together.

For Verified Resale, rules, listings, orders and the operations that track reissue form one Resale API, because a partner uses them together in one journey and they change for the same reasons. Reissue itself stays inside the Inventory team's internal interface; partners see its progress through an operation resource and never call barcode issuance directly. Separate rule, price and listing APIs would have been the per-entity mistake, and folding resale into a general "tickets API" the mega-API one, since tickets belong to the Ticketing context, which changes on a different rhythm.

#### The contract as the first deliverable {#c9-contract-first-mocks}

The Architecture book's Section 7.1 stated the rule that the contract comes first: the OpenAPI document is written, reviewed and linted before anyone writes the code behind it. This chapter adds one thing to that rule. A contract written first is also something we can hand to a partner first, and for a partner a contract with examples and a mock server behind it is far more useful than a contract alone.

The pieces are standard. The OpenAPI Specification, at version 3.1 since February 2021, can carry worked examples for every request and response, and a mock server, such as Stoplight's open-source Prism, can serve those examples as though the API were already running. Zalando's public guidelines open with this principle under the name "API First", and Lauret and Higginbotham each give a chapter to mocking.

Rowmate integrated against the mock for three weeks before the Resale service reached the sandbox. In those three weeks its engineers found two things that would have been expensive later. The listing response gave the face value and the cap, but not the all-in price a buyer would pay including the 10% fee, so Rowmate's checkout would have had to compute Encore's fee itself and would one day have computed it wrongly. And the `validateOnly` response said only "accepted" or "rejected", where Rowmate needed the rule that caused a rejection in order to tell the fan what to change. Both were fixed with an edit to the contract. Found in production, either would have been a migration.

Publishers know this economy well. An author corrects galley proofs before the print run, because a change on the galley costs a pencil mark and a change after printing costs a reprint. The mock is a galley that the partner's code reads. The analogy breaks in a way that matters: a galley cannot drift from the book it previews, but a mock can drift from the service it imitates, and then the partner learns the wrong contract with great confidence. So Encore generates the mock from the contract and runs the same examples as tests against the real service on every build. Contract tests and simulators as engineering practice belong to the Software book's Section 3.3.

#### The consumer in the room {#c9-consumer-in-room}

Section 3.3 recruited six promoters as design partners for Verified Resale, following Marty Cagan's customer discovery program, and gave Rowmate a separate, smaller partner program of its own. For an API, a partner's most useful work is to review the contract while it is still a draft. Rowmate and Tessera both reviewed it before it was built; Tessera had not yet committed to integrate, which made its review more candid.

What makes such a review last is the record it leaves. Every change a partner asked for was written into a decision log that lives beside the contract, with the request, the reason and the answer, much like the entries of an architecture decision record. Tessera asked for a reason code on every withdrawal, so that its sellers would know whether they or the organizer had taken a listing down, and the contract gained an open set of reasons. Rowmate asked for idempotency on listing creation, which the Architecture book's patterns already required, and the log notes that the request confirmed an existing rule.

The refusals matter as much. Rowmate asked to see how fast an event was selling, so it could advise sellers on pricing. The answer was no, because sales velocity is confidential at Encore, and partners never see it; the fifth fairness invariant says so. The log records the request, the refusal and the reason, so that when a different partner asks the same question a year later, a new product manager finds the answer and its reasoning already written down.

**Recap.** Designing from the outside in starts with the consumer's situation, written as job stories and turned into capabilities before any endpoint is named. Walking the failure paths, an old practice from use-case analysis, finds operations that the nominal path never shows, and grouping operations by bounded context avoids both the mega-API and the per-entity API. A contract with examples and a mock lets partners build before the code exists, provided the mock is generated from the contract and tested against the service, and design partners' requests, granted or refused, belong in a written log.

**Exercise 9.1.** Write three job stories for an API you own, each from a different consumer's situation. For each, find the existing operation that serves it. Where none does, or where the consumer would need three calls to do one thing, write down the operation the job story implies, and ask one real consumer whether you have their situation right.

### 9.2 Patterns That Last

#### A catalogue, adopted once {#c9-pattern-catalogue}

Every organization that builds APIs eventually holds the same arguments many times over. How does a client update two fields without sending the whole resource? What does an operation that takes four minutes return? Each question has several defensible answers, and in an organization of 40 teams each team will find a different one unless something stops it, so that a partner who learns how one team handles a long operation must learn again for the next.

Civil engineering solved a version of this problem long ago with standard details. A highway authority publishes standard drawings for a curb, a manhole, a guardrail end and a drainage inlet, and a designer on a new road uses them instead of drawing new ones. The designer's attention goes to what is particular to the site, its grades and soils and junctions, while the parts that should be the same everywhere are the same everywhere. The analogy holds well, with one difference worth naming. A badly drawn manhole is a problem in each place it is built, but each manhole stands alone. An API pattern is something consumers write code against, so a mistake in a standard pattern is copied into every API that adopts it, and consumers come to depend on the mistake. A pattern catalogue therefore needs the same versioning discipline as an API.

The best public model is Google's API Improvement Proposals (AIPs), published at google.aip.dev from 2019 onward. Each AIP describes one pattern, gives its reasons and examples, and is numbered so that a design review can say "follow AIP-134" and mean something precise. JJ Geewax, who worked on them, set out the same patterns in book form in *API Design Patterns* (2021). Microsoft and Zalando publish guidelines of their own, and Zalando marks every rule with its strength, MUST, SHOULD or MAY, and enforces many of them with its open-source linter, Zally. Each shows the same move: decide the pattern once, write it down with its reason, and stop deciding it again.

Encore's catalogue starts from what the Architecture book's Section 7.1 already fixed: problem-details errors under Request for Comments (RFC) 9457, idempotency keys on every operation that creates or moves money, and cursor pagination. It adds the patterns in Figure 9.2. One choice in it is a deliberate refusal. Google's AIP-160 defines a full filter grammar, with expressions such as `state = "LISTED" AND price < 60`, and it is real and well specified, but it is costly to implement in every service and most partners never need it. Encore's catalogue chose simple equality filters on named query parameters and recorded the reason, so that the question will not need to be asked again until a consumer's job story demands more.

| Problem | Pattern in Encore's catalogue | Example | Source |
|---|---|---|---|
| Errors a client can act on | Problem details with a stable code and "whose move it is" | `422` with code `cap_exceeded` | Architecture book, Section 7.1; RFC 9457 |
| Retrying without doing twice | `Idempotency-Key` on every create | Creating a listing | Architecture book, Section 7.1 |
| Lists that change while read | Opaque cursor, capped page size | Listing changes feed | Architecture book, Section 7.1 |
| Verbs on an existing resource | Custom method, `POST` with a colon | `POST /v2/listings/{id}:withdraw` | AIP-136 |
| Changing some fields | JSON Merge Patch; JSON Patch for arrays | Lowering a cap | RFC 7396; RFC 6902 |
| Work that takes minutes | Operation resource with progress and result | Reissue | AIP-151 |
| "Would this succeed?" | `validateOnly` on the real request | Pre-checking a listing | AIP-163 |
| Deletes a client may regret | Soft delete with expiry and undelete | Webhook endpoints | AIP-164 |
| Narrowing a list | Equality filters on named parameters | `?eventId=…&state=listed` | Encore's choice; AIP-160 considered |

*Figure 9.2 — Encore's API pattern catalogue, as of the Verified Resale build. The first three rows came from the Architecture book; the rest were added by the Public API team and the API guild.*

#### Standard methods and custom ones {#c9-custom-methods}

The core of a resource-oriented API is a small set of **standard methods**, the same five verbs applied to every resource: get one, list many, create, update and delete. Their value is predictability: a partner who has learned how Encore lists events can guess how it lists listings. Some actions do not fit the five verbs. Withdrawing a listing is neither an update, since the caller should not set the state field directly, nor a delete, since the record must remain. Google's convention, in AIP-136, is a **custom method**: a `POST` to the resource's address, followed by a colon and a verb, such as `POST /v2/listings/{id}:withdraw`. The colon marks the verb as something other than a sub-resource, and the convention keeps the five standard verbs pure.

The Architecture book's Section 7.1 gave a different answer to a similar problem. There a seat hold became a workflow resource, `POST /holds`, with its own identity and lifetime, and the catalogue has to say when each form applies. Encore's rule is short. A custom method is right for a single step that changes the state of an existing resource and finishes at once: a listing is withdrawn, and that is the whole of it. A workflow resource is right when the process itself has an identity and a lifetime that a consumer may want to read, cancel or audit: a hold that expires in five minutes, an order that passes through payment, a reissue that may take minutes to finish. The test is whether anyone will ever want to ask about the process after it has started. If so, the process deserves a name of its own.

The fragment below shows the two forms side by side in the partner contract. Creating a listing is a standard method that also accepts `validateOnly`, which the next subsection but one explains, and withdrawing a listing is a custom method.

```yaml
paths:
  /v2/listings:
    post:
      operationId: createListing
      parameters:
        - {name: validateOnly, in: query, schema: {type: boolean, default: false}}
        - {name: Idempotency-Key, in: header, required: true, schema: {type: string}}
      responses:
        "201": {description: Listing created}
        "200": {description: "validateOnly: would be accepted; nothing created"}
        "422": {description: Breaks an organizer rule; the problem names the rule}
  /v2/listings/{id}:withdraw:
    post:
      operationId: withdrawListing
      responses:
        "200": {description: Listing is now withdrawn, with reason seller_request}
```

#### Partial updates {#c9-partial-updates}

The simplest update is a full replacement: the client sends the whole resource and the server stores it. Suppose an organizer's system, written last year, updates resale rules by sending the cap and window it knows about. This year the rule set gained a per-fan listing limit. The old client's full replacement omits it, and the server, doing exactly what it was asked, erases the limit the organizer set last week, with no error and no warning. The principle that prevents this fits in one sentence: an update changes only the fields the client names, so that an old client can never erase a field it does not know.

There are three established ways to name the fields. Google's APIs use a **field mask**, an `update_mask` listing the paths to change, described in AIP-134; it is precise and works best with protocol buffers and gRPC, where a message cannot tell an absent field from an empty one. For HTTP and JSON, the widely used alternative is **JSON Merge Patch** (RFC 7396, 2014): the client sends a JSON (JavaScript Object Notation) document holding only the fields it wants to change, and the server merges it in. Merge Patch has two known limits, both written into Encore's catalogue: a `null` value means "remove this field", so a field cannot be set to null on purpose, and an array can only be replaced whole. Where a client must change one element of an array, the catalogue points to **JSON Patch** (RFC 6902, 2013), which sends a list of operations instead of a document.

Encore's catalogue chose Merge Patch as the default for its HTTP APIs. A large promoter's system lowering the cap for one event sends `PATCH /v2/events/{id}/resale-rules` with `{"cap": {"amount": 5000, "currency": "EUR"}}`, and the window and the per-fan limit are untouched whatever that system knows about them.

#### Long-running operations {#c9-long-running}

The Architecture book's Section 7.1 introduced the minimal answer to work that outlasts a request: respond `202 Accepted` and return a status resource the client can poll. For a partner integrating against real work, that minimum leaves several questions open. How far along is it? Can I cancel it? If it failed, why, and should I retry? How long can I come back and ask? Google's AIP-151 answers them with a single resource type, the **operation**, used across Google Cloud: a resource that represents work in progress, carrying its progress as metadata, a `done` flag, and either a result or an error once it finishes. Geewax gives the pattern a chapter, and Lauret treats long operations in his.

Reissue is Encore's clearest case. When a listing sells, the order's response names an operation, and the operation passes through three stages: the seller's barcode is revoked and added to the revocation lists that venue scanners hold for offline validation, a new ticket identity is issued to the buyer, and the new ticket is delivered to the buyer's app, with any wallet pass updated. Most reissues complete in under 30 seconds, and 99% within four minutes; Encore's listings close two hours before doors precisely so that the slowest of them still finish long before anyone reaches a turnstile. The operation reports its current stage, so a partner can tell its buyer "your ticket is being issued" honestly, and any failed stage with Encore's retry, so the partner can tell "delayed" from "lost". Operations are kept for 30 days, for partners reconciling disputes.

Cancellation deserves a precise answer, since AIP-151 allows it but does not require it. A reissue can be cancelled only before its first stage completes. Once the seller's barcode has been revoked, reversing the reissue needs two people's approval at Encore, as the Software book's Section 7.4 describes, so the operation carries a `cancellable` flag that turns false after the first stage. Offering partners a cancel button that really meant a support case would be a promise Encore could not keep.

#### Validation-only requests and undoable deletes {#c9-validate-only}

Rowmate's first job story asked to know at once whether a listing would be accepted. The pattern that answers it is the **validation-only request**: the client sends the real request with a flag, `validateOnly`, and the server runs every check it would run for real, then returns the verdict without changing anything. AIP-163 describes it, and Geewax gives it a chapter. Partners call it while a fan fills in the listing form, so the fan learns before pressing the final button that the event's cap is €50, or that resale for this show closes tomorrow evening.

The pattern has one hard requirement: the validation must run the same code as the real request. A separate, simplified copy of the rules will one day say "accepted" to something the real request rejects. Encore implements `validateOnly` as a flag that stops the Resale service's create path just before it writes, so every new organizer rule is honored by validation the day it ships. The verdict is true only of its moment, since the organizer may tighten the rules a minute later, and the partner must still handle a `422` on the real request.

Soft delete is the companion pattern for actions a client may regret. In AIP-164 a deleted resource is marked deleted, hidden from ordinary lists and restorable with an `:undelete` method for a stated period. Encore applies it to webhook endpoint registrations, where partners asked for it: an endpoint deleted by mistake on a Friday evening can be restored, with its delivery history and signing secret, for seven days. Listings do not need the pattern, because they are never deleted; a withdrawn listing remains a record, readable for reconciliation.

#### Deciding what compatible means {#c9-defining-compatibility}

In April 1964 IBM announced System/360, a family of computers of very different sizes and prices that shared one architecture, so that a program written for one model would run on the others. Compatibility was the product: a customer could outgrow a small machine and move to a larger one without rewriting their programs. Every API provider makes a promise of this kind, written down or not, and Geewax's chapter on versioning makes the point that compatibility is a choice. A provider can promise perpetual stability, it can promise very little and change freely, or it can version semantically and promise stability within a major version. Each choice suits a different audience, and AIP-180 records Google's.

Facebook offers a clear public example of the choice written down. At its f8 conference in April 2014 it introduced versioning for its Graph API, with a guarantee that core APIs would remain stable for two years and a 90-day migration window for the "extended" ones. A later changelog clarified that a version lives for two years after the next version is released, a number a partner could plan by.

Encore's choice is the Architecture book's Section 7.2: additive change forever, never repurpose a field, tolerant readers on both sides, and a new version only as a last resort. This section adds how the choice is written down. Encore's partner documentation carries a compatibility page. Removing a field, adding a required input, tightening validation, changing a default and changing the meaning of an event are breaking, and come with 12 months' notice. Adding a field, an endpoint, an event type or a value to an open enumeration is not, and partners are told in writing that their code must tolerate these.

The resale API forced one subtle entry onto that page. Every change to an organizer's rules makes some listings invalid that were valid a minute before. Is a lower cap a breaking change? The page answers no, because the contract states that listings are always subject to the organizer's current rules and defines the `rules.changed` event and the `rule_change` withdrawal as the way partners learn of changes. A new kind of rule, which a partner's code must understand to stay correct, is breaking, and is announced like any other breaking change.

**Recap.** A pattern catalogue settles recurring design questions once, with reasons, so that 40 teams stop answering them differently. Custom methods carry single-step verbs and workflow resources carry processes with a lifetime. Partial updates change only named fields, so old clients cannot erase new ones. Long-running work becomes an operation with progress, a result and honest cancellation. Validation-only requests run the real code, and the meaning of "compatible" is a written choice, most useful where it settles the hard cases.

**Exercise 9.2.** List the patterns your APIs use for partial update, long-running work and "would this succeed?" checks. Count how many variants of each exist across your teams, and for one pattern, write the catalogue entry that would end the variation: the problem, the chosen pattern, its reason, an example and the source you took it from.

### 9.3 Consistency Across 40 Teams

#### A style guide people read {#c9-style-guide}

In April 1893 Horace Hart, the Controller of the Oxford University Press, had a small booklet of *Rules for Compositors and Readers* printed and given to the press's own staff. Its purpose was that books set by many hands, for many authors, should read as though one house had made them, and it grew edition by edition, as the press wrote down its decisions, into the guide still known as *Hart's Rules*. An API style guide is the same instrument for the same purpose: many teams, one surface, and a written record of how things are done here. The analogy breaks at the moment of application. A copy editor applies house style after the author has finished, and a mistake can be corrected in the next printing. An API's names are published the day it ships, so its style guide has to be applied before release, by tools as far as possible.

Higginbotham gives a chapter to establishing an API style guide, and Lauret's second edition gives a part of the book to design guidelines. They agree on what makes a guide read. It is short enough to read in an hour. Every rule carries its reason, because a rule without one is broken at the first inconvenience, and an example, good and bad. The guide is versioned, and owned by a small group with the authority to change it. Zalando, Microsoft, Google and PayPal publish theirs openly, and reading two or three is the fastest way to see what a good one looks like. The Architecture book's Section 7.5 told of one such guide, 89 rules written RFC-style; this section is about keeping one alive.

Encore's guide is owned by the Public API team, with an API guild drawn from the dozen or so teams that publish partner or public surfaces, and has 71 rules at its current version. It opens with a glossary, because vocabulary is where inconsistency starts and where the Architecture book's bounded contexts reach the API. Eric Evans called it ubiquitous language in *Domain-Driven Design* (2003): a context's words, used the same way in conversation, code and interface. The glossary defines once the terms partners meet: a **listing** is an offer to resell one ticket; a **reissue** is the replacement of a sold ticket with a new identity and barcode for its buyer; **face value** is the price at the primary sale. It also records words that change meaning across contexts. Inside Support a "ticket" is a case; in every partner-facing API a ticket is the right to enter a venue. Google keeps a glossary of the same kind as AIP-9.

#### Lint rules and their lifecycle {#c9-rule-lifecycle}

The Architecture book's Section 7.5 made the case that governance should ship as linting, with Spectral-style rules running in continuous integration (CI) against every contract change, and its Section 7.2 added the breaking-change differ. This subsection takes that as settled and turns to something those sections left out: rules have lives of their own. They are proposed, tried, enforced, excepted and eventually retired, and a guide that has no process for each of those stages grows rigid in some places and ignored in others.

Encore's guild runs the lifecycle in the open. Anyone may propose a rule, in a pull request to the guide, with the problem it solves, a reason, an example and either a lint implementation or, where a linter cannot check it, an item for the review checklist. "Paths name resources as nouns" can be linted. "Names use the consumer's words" cannot, and becomes a question the reviewer asks. Of Encore's 71 rules, 58 are linted and 13 are checklist items. A new linted rule runs as a warning for a month, so the guild can count how many existing contracts it would fail and read why, before it becomes an error that fails builds.

Exceptions are declared in the contract itself and approved in the pull request, never granted in a side conversation, and the guild counts them every month by rule. The record is small:

```yaml
# In the contract: one entry per exception, read by Encore's lint step
x-encore-lint-exceptions:
  - rule: list-pagination-cursor          # guide rule P-3
    path: /v2/events/{id}/price-levels
    reason: "Fixed list of at most 12 items; a cursor adds work and no value."
    approved-in: "Partner APIs PR, reviewed by the API guild"
    expires: "next major version of the guide"
```

Counting exceptions turns them into evidence about the rules. Last quarter the guild recorded 37 exceptions, 21 of them against the cursor-pagination rule, nearly all for short, fixed lists like price levels. That was the guide being wrong, and the rule was amended to exempt lists with a documented maximum of 50 items. Rules also retire: a rule that has prevented nothing for a year, and whose reason no longer applies, is removed the way it was adopted, by pull request with a reason.

#### Review where it matters {#c9-review-not-gate}

The Architecture book's Section 7.5 rejected design review boards, for good reason: a board that reads every design in a meeting is slow, depends on who attends and turns its members into gatekeepers, and the DORA research cited in the Resilience book's Section 1.3 found that approval by bodies outside the team slows delivery without making it safer. But linting cannot ask whether an API's words are the consumer's words, whether an operation belongs in this boundary or the next, or what happens on the failure path. Some human review is worth having. The question is how to have it without rebuilding the board.

The evidence here is practitioner experience and published company practice. Zalando's guidelines describe API review by a guild, and Mehdi Medjaoui and his co-authors, in *Continuous API Management* (second edition, 2021), argue for deciding explicitly which decisions are centralized. Encore reviews only new partner or public surfaces and breaking changes in them; everything internal and every additive change passes on lint alone. Two guild members on a rota review asynchronously in the pull request, against a turnaround target of two working days; last quarter they reviewed 23 changes with a median of a day and a half. They may block only for a broken rule, and anything else is advice the team may decline in writing.

#### Seeing the landscape {#c9-landscape}

Past a certain size, an organization stops having APIs and starts having an API landscape, with properties no single API has. Medjaoui and his co-authors give a chapter to landscapes and offer eight aspects to watch, all beginning with V: variety, vocabulary, volume, velocity, vulnerability, visibility, versioning and volatility. The eight V's are one book's framework, not an industry standard, and Encore uses them only as a checklist of questions to ask each quarter.

The proven part of landscape governance is plainer: a catalogue that lists every API with its owner, tier and lifecycle stage. Backstage's software catalog has an API entity kind for exactly this, and many organizations keep the same records in other tools. The Architecture book's Section 7.5 required every endpoint to be born with an owner, tier, objective and deprecation policy, and the Software book's Section 6.3 makes each service's manifest the source of the catalogue. This section adds the landscape view: looking at the catalogue as a whole to see what no single entry shows.

| Aspect | The question Encore asks | Encore at month 9 |
|---|---|---|
| Volume | How many APIs, and of which exposure? | 268 in the catalogue: 214 internal, 31 partner, 23 public |
| Variety | How many ways do we solve the same problem? | Long-running work: one pattern in new APIs, three in older ones |
| Vocabulary | Do teams use the glossary's words? | Four partner APIs still say `ticket` for a support case |
| Versioning | How many versions are live, and how old is the oldest? | Two major versions; the oldest partner version is four years old |
| Visibility | Can a partner or a team find what exists? | Partner and public APIs in the portal; 9 internal APIs missing from the catalogue |
| Volatility | Which APIs change most, and do their consumers know? | The Resale API, by design, during the build; announced in the changelog |
| Vulnerability | Which APIs expose personal data or money? | 11 partner APIs touch payments, orders or fan data |
| Velocity | How long from design to a published contract? | Median 19 days for partner APIs, including review |

*Figure 9.3 — Encore's API landscape as the guild reviewed it at month 9 of Verified Resale. The numbers matter less than the habit of asking each question every quarter.*

The landscape view is where orphans show up. Four internal APIs in the catalogue had owners who had moved teams, and nobody had noticed, because the APIs still worked. An orphaned API is harmless until the day it needs to change, and the catalogue's job is to make sure that day does not also start the search for whoever owns it.

**Recap.** A style guide is read when it is short, gives a reason and an example for every rule, carries a glossary of the domain's words and is owned by a small group that can change it. Lint rules have a lifecycle, from proposal through a trial as warnings to enforcement, counted exceptions and retirement, and counted exceptions are evidence about the rules. Human review is kept for new partner and public surfaces, with a turnaround target, and a catalogue seen as a landscape shows the drift and the orphans that no single API reveals.

**Exercise 9.3.** Run your linter over every API contract in your organization and rank the five most violated rules. For each, decide whether the contracts are wrong or the rule is, and write down the evidence. Then find one API in your catalogue whose owner has left, and see how long it takes to find who owns it now.

### 9.4 Partner and Public APIs

#### The API as a product {#c9-api-product}

The Architecture book's Section 7.5 observed that an API with outside users has become a product, and the Software book's Section 8.3 builds the partner program around it. *Continuous API Management* sets out the product view in detail, with ten pillars of an API product and a lifecycle of five stages: create, publish, realize, maintain and retire. "Realize", the period in which a published API starts producing the value it was built for, is the stage teams most often forget.

What this chapter adds is the team. Section 1.3 argued that a product is best led by a trio, a product manager, a designer and a tech lead who share responsibility for value, usability and feasibility. The partner API has its own trio inside the Partner APIs team. Its product manager owns the value proposition for partners: sell resale tickets that are guaranteed to be valid at the door, and earn 4 points of the 10% fee on each. Its designer works on what partners touch: the portal, the documentation, the error messages and the sandbox. Its tech lead owns the contract and its evolution.

The trio's measures follow the partner's journey after the first call. They track the days from sandbox credentials to a first sandbox listing, the share of partners who pass certification at the first attempt, the hours of integration work partners report, and the share of listings that fail after a partner showed them to a fan as accepted. That last number is the one Rowmate's first job story was about, and the trio holds it near zero.

#### The first month {#c9-first-month}

The Architecture book measured developer experience in minutes to the first successful call, with a target under 10. That number is right for the first afternoon. A partner integration is judged on its first month, when the partner's engineers move from calling the API to building a product on it, and every gap in the sandbox becomes a question sent to Encore and a day lost waiting.

A sandbox is only useful when its data is realistic. Encore's resale sandbox holds events with every kind of organizer rule, a sold-out on-sale in progress, and tickets in every state of the listing lifecycle. It also borrows an idea from Stripe, whose testing documentation lists card numbers that always produce a given outcome, such as a decline. Encore's sandbox has test tickets of the same kind: one whose buyer always fails Bot Screening, one whose organizer tightens the cap 30 seconds after it is listed, and one whose reissue fails at delivery and succeeds on retry. A partner engineer can make each failure happen on demand.

Three artifacts carry the rest of the first month. **Software development kits (SDKs)** are generated from the contract with OpenAPI Generator, as Higginbotham advises, and carry their own semantic version, because the SDK version is what partners actually pin. A dated **changelog** records every change to the contract, including the additive ones. And a **status page** reports the partner API's health separately from the fan storefront's. Higginbotham's chapter on the minimum viable portal describes this set well.

Behind them sits an input partners never see: usage per partner, meaning calls per endpoint, error rates, SDK versions in the field and the last time each partner touched each deprecated field. Medjaoui and his co-authors treat this as the basis of continuous improvement, and it decides when a field can be removed and which partner needs help.

#### Go-live: what the contract asks a partner to prove {#c9-go-live}

An airline does not let a newly qualified pilot carry passengers on the strength of a licence alone. First comes a check ride, much of it spent on procedures that should never be needed: an engine failure at takeoff, a rejected landing. Partner certification has the same shape. A partner that can create a listing has shown very little; what matters is what its integration does when the rules change, when a webhook arrives twice or when a reissue is late. The analogy breaks on decay. A pilot's skills fade, so pilots are rechecked on a calendar; a partner's integration breaks when either side changes, so recertification follows major versions and production signals.

Certification before production access has well-known precedents. Salesforce's AppExchange security review and Shopify's app review both stand between a partner and the provider's customers, and Twitter's 2012 rules, as we saw at the start of the chapter, required certification for client apps pre-installed on devices. The Software book's Section 8.3 owns Encore's certification program and its suite of scenarios: a simulated on-sale, a reissue, a listing that breaks a cap, a webhook outage and a revoked grant. That suite fails a candidate partner that caches prices past an organizer's cap change. This section owns the other half: the list of behaviors the contract requires, from which the suite's scenarios are drawn. Partners receive sandbox credentials at once and production credentials only after certification.

```text
Verified Resale partner API: what certification checks (contract v2.4)
[ ] Acts on rules.changed within 5 min; never shows a listing that breaks current rules
[ ] Calls validateOnly before showing a listing as accepted; still handles 422 on create
[ ] Sends an Idempotency-Key on every create; reuses it on retry
[ ] Verifies webhook signatures; rejects timestamps older than 5 min
[ ] Deduplicates events by webhook-id; tolerates events arriving out of order
[ ] Honors 429 and Retry-After; never retries a 422
[ ] Treats unknown enum values (new withdrawal reasons, event types) as non-fatal
[ ] Shows the all-in price, including the 10% fee, before the buyer commits
[ ] Reconciles its listing copy from the changes feed, and on cursor expiry from a full read
[ ] Uses certificate-bound 15-min tokens; holds no long-lived key in any repository
```

Every line traces to a clause of the contract or the terms, and that is the test of a good checklist: a partner that fails an item can be shown the sentence it broke. The last line exists because of the Rowmate key leak told in the Resilience book's Section 7.2, which is why partners now authenticate with 15-minute tokens bound to a client certificate.

#### Deprecation as a campaign {#c9-deprecation-program}

The Architecture book's Section 7.2 gave the mechanics of retirement: `Deprecation` and `Sunset` headers, a migration funnel, and a person on the phone for the last three partners. The Software book's Section 6.4 shows scheduled brownouts flushing out hidden dependents. This subsection is about the campaign around those mechanics, which is where retirements succeed or fail. Having spent a decade maintaining a widely used open-source library, I have come to believe that a deprecation notice is the least-read document in software, and a retirement that relies on people reading it will not finish.

Twitter's own retirement of version 1.0 is instructive precisely because it slipped. Version 1.1 shipped on 5 September 2012 with a promise of six months to migrate. In March 2013 Twitter moved the date to 7 May, with blackout tests before it, short planned outages to show developers what would break, and version 1.0 finally returned `410 Gone` on 11 June 2013. Salesforce offers a calmer example. Its policy promises at least a year's notice before retiring an API version, and when it scheduled versions 21.0 to 30.0 for retirement in Summer '23, it postponed the date to Summer '25 and gave customers a switch to test against the retirement first. Dates slip. A slip announced in advance, with a reason and a new date, costs a provider far less of its partners' trust than a retirement that takes them by surprise.

Encore's first campaign of this kind retires the Partner Listings endpoint for link-out resale offers, since keeping it would leave an unverified path beside the verified one. Notice goes out on Verified Resale's launch day, through the changelog, email to every partner's technical contacts and a `Deprecation` header, with a `Sunset` date 12 months later, as the partner terms require. A weekly dashboard shows each caller's remaining traffic, a Partner APIs engineer offers each caller help with the migration, two brownouts are scheduled for the last quarter, and the trio's product manager makes the last calls by phone. At the month-18 review Rowmate has moved entirely. The remaining callers are a handful of small sites that have not applied for Verified Resale, and for them the campaign ends in a clear, early, courteous goodbye.

#### Terms are part of the contract {#c9-terms}

We can now return to Twitter's lesson and apply it. A partner's contract with Encore has two documents. The OpenAPI document says what may be called and what comes back. The partner terms say how often it may be called, what the partner may do with what it receives, how it must be shown to fans, and how and when any of this may change. Conduct terms, such as no buying of primary inventory, no scraping and the enforcement ladder from warning to termination, are the business of the Software book's Section 8.3. This subsection covers the terms that shape the API.

Rate limits come first, because limits are where Twitter's 2012 changes began, and because a limit changes what a partner can build. The Architecture book's Section 7.3 owns the mechanics: a contractual quota, a token-bucket burst allowance, `429` with a `Retry-After` header under RFC 9110, and the IETF draft `RateLimit` and `RateLimit-Policy` headers, which are still drafts and labelled as such in Encore's documentation. The terms add the numbers. Each resale partner's steady quota is set by tier, and during a major on-sale an event-scoped limit applies on top: 20 availability reads a second per event, with a burst of 100, for every partner alike. The figure is published, so a partner can design its product around it before its first on-sale.

Display and data-use rules shape a partner's product more than its code, as Tweetbot's $19.99 price showed. Encore's terms require partners to show the all-in price, including the 10% fee, before a buyer commits, and they limit what a partner may do with a buyer's personal data.

Change notice is the clause on which everything else rests. Encore's terms promise 12 months' notice of any breaking change and name the dated changelog as the channel for notice, on the model of Stripe's dated versions, which the Architecture book's Section 7.2 cited. The terms also govern their own amendment. A change that takes something away from partners, such as a lower quota, a narrower data-use clause or a change to the 4-point share, carries the same 12 months' notice; a change that adds something carries 30 days. One exception covers an active security threat: Encore may act at once and must explain in writing within five working days. Facebook's two-year guarantee of 2014 was such a promise written down in public; in January 2023 Twitter's written rule followed its action by a week. Partners can plan around strict terms. They cannot plan around terms that move without warning.

#### Agents as consumers {#c9-agents}

AI agents increasingly call APIs as tools, and since Anthropic introduced the Model Context Protocol (MCP) on 25 November 2024 they have had a common protocol for it; OpenAI announced support on 26 March 2025, and in December 2025 the protocol was donated to the Agentic AI Foundation under the Linux Foundation. The practice is young, and its best lesson is the one the Architecture book's Section 7.5 drew: an agent inherits the contracts, scopes and quotas of any other client. Encore publishes no MCP server for partners. An agent acting for Rowmate uses Rowmate's certified credentials and limits.

**Recap.** The partner API is a product with its own trio, judged on the partner's whole journey rather than its first call. The first month depends on a realistic sandbox with test fixtures that produce failures on demand, generated SDKs versioned apart from the API, a dated changelog, a status page and usage data per partner. Certification checks the behaviors the contract requires, above all on the failure paths, and deprecation is a campaign that plans for its dates to slip. The terms are part of the contract, and the clause that matters most is the one that governs notice, including notice of changes to the terms themselves.

**Exercise 9.4.** Ask a developer from outside your team to build a working integration in your sandbox in one afternoon, using only your public documentation. Write down every question they had to ask and every failure they could not make happen on demand. Then read your partner terms and find the clause that says how much notice you give before changing them. If there is none, draft it.

### 9.5 Webhooks and Integrations

#### What the contract already says {#c9-webhook-contract}

The webhook contract is settled. The Architecture book's Section 7.1 gave it: signed payloads, at-least-once delivery with backoff, an ID on every event for deduplication, and a replay endpoint. The delivery machinery is a shared platform capability, as the Software book's Sections 6.3 and 6.4 tell, and the isolation of webhook workers belongs to the Resilience book's Chapter 5. This section is about what remains: what a partner receives, what it can see, and how it keeps its copy of the world correct.

#### Thin events or full payloads {#c9-thin-events}

A **full event**, which Stripe calls a snapshot event, carries the state of the resource as it was when the event was emitted. A **thin event** carries little more than the event's type and the identifiers of the resources involved, and the receiver fetches the current state when it needs it. Full events save a call. Thin events are current when acted on, hardly ever change shape, and carry less personal data across the internet, since buyer details are fetched under the partner's scopes.

Stripe now offers both, and its reasoning is public. Thin events arrived with its Meters API in the 2024-09-30 release. For snapshot events, Stripe's documentation warns that the object "can be stale by the time you process it" and recommends fetching the latest state. That warning is Encore's reason for choosing thin events. Between the moment a listing sells and the moment a partner processes the event, the reissue may have completed or failed and the organizer may have tightened the rules. Encore's events, `listing.sold`, `listing.withdrawn`, `listing.expired`, `rules.changed`, `reissue.completed` and `reissue.failed`, are all thin. Their envelope follows the Standard Webhooks format of the next subsection; CloudEvents 1.0, a Cloud Native Computing Foundation (CNCF) specification, suits events that also travel over streams.

A thin `listing.sold` delivery looks like this. The headers carry the event's ID, its time and its signature, and the body names the listing and the order and nothing more.

```http
POST /hooks/encore HTTP/1.1
Host: partner.rowmate.example
Content-Type: application/json
webhook-id: evt_01J9ZK6Q4X2M8T
webhook-timestamp: 1767225600
webhook-signature: v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pX4=

{"type": "listing.sold",
 "data": {"listing": "listings/lst_7Hq2", "order": "orders/ord_93Ka",
          "reissueOperation": "operations/rei_51Vd"}}
```

A courier who finds nobody at home leaves a card saying a parcel is waiting at the depot, and the recipient collects it there. A thin event is that card. The analogy is exact up to the depot. A depot holds the parcel unchanged until someone collects it, while Encore's "depot" returns whatever is true at the moment of fetching, which may differ from what prompted the card: a partner that fetches the listing after `listing.sold` may find it already `reissued`. That is the point of the design, and the partner's code must expect state to have moved on. The cost is an extra call for every event, which matters at an on-sale, when hundreds of listings may sell in a minute. Encore sizes those reads as part of the partner API's capacity and does not count them against the event-scoped availability limit, since a partner fetching an order it was told about is doing exactly what it was asked to do.

#### Delivery the partner can see {#c9-delivery-visible}

Webhook delivery fails in ways the receiver cannot see: a partner whose endpoint has been returning errors since Tuesday's deploy knows only that its sales seem quiet. So delivery has to be visible to the partner, in the portal, without a support case. Encore's partner portal shows, for each endpoint, a delivery log of every attempt with its status code and latency, the retry schedule each failing event is on, the endpoint's health over the past week, and any events waiting for replay. A partner engineer can resend any event from the log.

A partner should also be able to read the retry schedule before it needs it. Providers publish theirs. Stripe's documentation says it retries live-mode deliveries "for up to 3 days with an exponential back off". Shopify's current documentation describes up to eight retries over four hours, after which the subscription is removed. Encore's default is in Figure 9.4. Partners may shorten the total window, down to 24 hours, or choose different intervals within bounds, because the shared delivery service made retries configurable per partner, a story the Software book's Section 6.4 tells.

| Attempt | Time after the event | What the partner sees |
|---|---|---|
| 1 | Immediately | Delivery logged with status and latency |
| 2–4 | 30 s, 2 min, 10 min | Event marked "retrying" with its next attempt time |
| 5–7 | 30 min, 1 h, 3 h | Endpoint health turns amber in the portal |
| 8 onward | Every 6 h | After 24 h of continuous failure: email and portal banner to technical contacts |
| — | 72 h | Endpoint disabled with notice; events kept for replay for 14 days |

*Figure 9.4 — Encore's default webhook retry schedule and what the partner sees at each step. A disabled endpoint loses nothing that the replay window still holds.*

Two further practices complete the picture. When a partner registers an endpoint, Encore sends a verification event and activates the endpoint only when it answers correctly, as Slack's URL verification challenge and Microsoft Graph's validation token do, so a mistyped URL cannot silently swallow a partner's events. And Encore formats and signs its deliveries according to the **Standard Webhooks** specification, version 1.0.0, published in December 2023 by an effort that Svix started with a steering committee from Kong, Zapier, Twilio, Lob, Mux, ngrok and Supabase. It is young and its adoption is still growing, but it standardizes what every provider used to invent separately, the `webhook-id`, `webhook-timestamp` and `webhook-signature` headers and how the signature is computed, so a partner can verify several providers with one library.

#### Testing integrations {#c9-testing-integrations}

The webhook path is the hardest part of an integration to test, because the partner is the receiver and cannot easily make the sender misbehave. Stripe's tooling shows what good support looks like. Its command-line tool can forward events to a developer's laptop with `stripe listen` and fire specific events with `stripe trigger`, and its dashboard can send a test event to any registered endpoint. Higginbotham's chapter on testing places these tools in a broader strategy.

Encore's sandbox goes one step further, because resale has sequences that single test events cannot reproduce. One scenario, `on-sale-rush`, sells 2,000 listings in ten minutes, with 1% of events delivered twice and a few out of order. Another tightens an organizer's cap in the middle of a sale; a third makes a reissue fail at delivery and then succeed. Each is also a recorded fixture, a file of signed events a partner can replay in its own test suite, and certification draws on the same scenarios. A sandbox of this standard is really a simulator, and simulators as products are the subject of the Software book's Section 3.3.

#### Inventory feeds and reconciliation {#c9-inventory-feeds}

Webhooks tell a partner what changed, quickly and usually reliably. "Usually" is the difficulty. An endpoint is disabled for a weekend, a worker drops an event because of a bug, and the partner's copy of Encore's listings drifts without anything in a push-only design noticing. Encore already had inventory feeds for partners, listed in Section 1.2 among the things Verified Resale could reuse. For resale they were upgraded on a proven pattern: an incremental feed of changes read by cursor, backed by a periodic full reconciliation.

The pattern has well-known public examples. Google Calendar's API gives each client a `syncToken` with which to fetch only what changed since its last read; when the token is too old, the API answers `410 Gone` and the client performs a full sync. Kubernetes controllers list the objects they manage and then watch for changes from that list's `resourceVersion`, starting over when the watch falls too far behind. Encore's `GET /v2/listing-changes?cursor=…` returns every change since the cursor, in order, and the cursor expires after seven days, after which the partner reads its full set of listings and starts afresh.

Rowmate reconciles hourly and after every `rules.changed` event, because a rule change can withdraw many listings at once, and those are the moments when a missed event would leave a fan looking at a listing that can no longer be bought. Webhooks are fast and can miss; the feed is slower and does not, so the feed corrects whatever the webhooks missed.

**Recap.** The webhook contract is settled elsewhere, and so is the shared delivery service; what remains is the partner's experience of it. Thin events let partners act on current state at the price of one more call. Delivery becomes visible through a per-partner log, a published retry schedule, endpoint verification and notice before disabling, and the young Standard Webhooks format saves partners from verifying each provider differently. Sandboxes that emit realistic failure sequences and recorded fixtures make the receiving side testable, and a cursor-based feed with periodic full reconciliation corrects the drift that webhooks alone cannot detect.

**Exercise 9.5.** In a sandbox, disable your own webhook endpoint for an hour while events are flowing. Then answer three questions without asking the provider for help. Can you see which events you missed? Can you recover them, by replay or from a feed? And would your system have noticed the gap if you had not caused it yourself?

### Kata: Sign Here

> **Your brief: "Tallyhouse."** Tallyhouse sells electronic signature and contract workflow as a service to about 7,000 businesses in four EU countries, and has 95 engineers in 12 teams. A customer drafts a contract from a template, routes it for internal approval, sends it as an envelope to its signers in order and files the signed copy. Law firms and practice-management systems integrate today by dropping documents into an SFTP folder, SFTP being a file-transfer protocol, and waiting for an email saying whether the envelope went out. Tallyhouse wants to open a partner API to about 300 law firms and practice-management vendors, so that a partner can send and track a client's contracts from its own system. Three teams already expose five internal APIs with three pagination styles and two incompatible ways of updating a signer's details. One large practice-management vendor scrapes the web interface because nothing else does what it needs. An envelope takes from a few minutes to several weeks to complete, often must be signed before a deadline such as an offer's expiry or a filing date, and may stall on data a paralegal can fix, such as a mistyped signer email or a missing signature field. The commercial team has promised partners "the same terms as the big platforms", which nobody has written down, and some 40 firms still use the SFTP folder every week.

**Deliverables:**

1. **Capability canvas** — Job stories from two kinds of partner, a law firm and a practice-management vendor, for "send a contract for signature from a partner system". Walk the nominal path and at least three failure paths, including a signer corrected after the envelope has gone out, and list the operations they yield.
2. **Pattern choices** — Catalogue entries for the three patterns the API needs most: the envelope as a long-running operation (with its stages, progress and voiding rule), validation-only submission of an envelope before it is sent, and partial update of signer records. Give each a reason and a public source.
3. **Lint rules and their lifecycle** — Ten rules for the new API style guide, marking which can be linted and which become review questions, and a one-page process for proposing, trying, excepting and retiring rules across the 12 teams.
4. **Certification checklist** — The behaviors a partner must show in the sandbox before receiving production credentials, each traced to a clause of the contract or the terms, and the sandbox fixtures that make each failure happen on demand.
5. **Webhook delivery view** — A design for what a partner sees in the portal about its `envelope.completed` and `envelope.declined` events: the delivery log, the retry schedule, endpoint health and the notice before disabling. Say whether the events are thin or full, and why.
6. **Terms and retirement** — The API terms that the commercial team's promise should have been: rate limits, notice periods for breaking changes and for changes to the terms themselves, and data-use rules. Then plan the SFTP retirement campaign for the 40 firms, with dated milestones.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Outside-in design | Could each operation be traced back to a job story a real partner would recognize, including the failure paths? |
| Patterns decided once | Would a partner who learned one Tallyhouse team's API find the next team's familiar? |
| Governance without a gate | Do the lint rules and review process keep 12 teams consistent without anyone waiting a week for approval? |
| Certification on failure paths | Does certification test what partners do when things go wrong, and can every item be shown to rest on a written clause? |
| Visible delivery | Could a partner whose endpoint failed overnight find out what it missed and recover it without contacting Tallyhouse? |
| Terms partners can plan around | Would the practice-management vendor that scrapes the interface today be able to plan a year of work on the terms you wrote? |

#### Where you now stand

You can now design an API from its consumers' situations outward, settle recurring design questions once in a catalogue, keep many teams consistent with a style guide, a living rule set and review kept for the surfaces that need it, and run a partner API as a product, with a sandbox, certification, deprecation campaigns and terms written to be planned around. You can also run the webhooks and feeds that keep a partner's copy of the world honest. Each chapter so far has taken one part of Verified Resale on its own: strategy, discovery, measures, price, design, frontend, phones and now interfaces. Chapter 10 puts them back together. It follows the Verified Resale bet memo from the morning it was written to a staged launch with three organizers, Rowmate and one market, and to the review that asks whether the bet paid. It begins with another launch that let people in a few at a time.

### References

- Michael Sippey — [*Changes coming in Version 1.1 of the Twitter API*](https://web.archive.org/web/20140115133550/https://dev.twitter.com/blog/changes-coming-to-twitter-api). Twitter Developers blog, 16 August 2012 — free online.
- James Higginbotham — [*Principles of Web API Design: Delivering Value with APIs and Microservices*](https://www.informit.com/store/principles-of-web-api-design-modernizing-apis-for-9780137355631). Addison-Wesley, 2021.
- Arnaud Lauret — [*The Design of Web APIs*, 2nd ed.](https://www.manning.com/books/the-design-of-web-apis-second-edition). Manning, 2025.
- JJ Geewax — [*API Design Patterns*](https://www.manning.com/books/api-design-patterns). Manning, 2021.
- Mehdi Medjaoui, Erik Wilde, Ronnie Mitra, Mike Amundsen — [*Continuous API Management*, 2nd ed.](https://www.oreilly.com/library/view/continuous-api-management/9781098103514/). O'Reilly, 2021.
- Google — [*API Improvement Proposals*](https://google.aip.dev/). google.aip.dev, 2019 onward — free online.
- Standard Webhooks — [*Standard Webhooks Specification*, v1.0.0](https://github.com/standard-webhooks/standard-webhooks). December 2023 — free online.
- Stripe — [*Event destinations*](https://docs.stripe.com/event-destinations). Stripe documentation — free online.
- Zalando — [*RESTful API and Event Guidelines*](https://opensource.zalando.com/restful-api-guidelines/). Zalando SE — free online.
- OpenAPI Initiative — [*OpenAPI Specification*, v3.1.0](https://spec.openapis.org/oas/v3.1.0). 2021 — free online.
- Iconfactory — [*Twitterrific: End of an Era*](https://blog.iconfactory.com/2023/01/twitterrific-end-of-an-era/). The Breakroom, 19 January 2023 — free online.
- Twitter Developers — [*API v1 Retirement: Final Dates*](https://blog.x.com/developer/en_us/a/2013/api-v1-retirement-final-dates). 29 March 2013 — free online.
- M. Nottingham, E. Wilde — [RFC 8594: *The Sunset HTTP Header Field*](https://www.rfc-editor.org/rfc/rfc8594). IETF, 2019 — free online.
- S. Dalal, E. Wilde — [RFC 9745: *The Deprecation HTTP Response Header Field*](https://www.rfc-editor.org/rfc/rfc9745). IETF, 2025 — free online.
- Salesforce — [*REST API Developer Guide: API End-of-Life Policy*](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_eol.htm). Salesforce developer documentation — free online.
- Anthropic — [*Introducing the Model Context Protocol*](https://www.anthropic.com/news/model-context-protocol). 25 November 2024 — free online.

---

## Chapter 10: Capstone — Verified Resale from Idea to Launch {#ch10}

> A bet written down before we knew how it would end is the only kind we can learn from.

On 1 April 2004 Google issued a press release headed "Google Gets the Message, Launches Gmail." It offered free web mail with "1,000 megabytes (1 gigabyte) of free storage", at a time when Hotmail's free accounts held 2 MB and Yahoo Mail's 4 MB, so that Gmail's gigabyte was about 500 times Hotmail's free allowance. Given the date and the size of the offer, many readers took it for an April Fools' joke, and the same day Google did announce a real hoax, a research center on the Moon. Brian Rakowski, Gmail's first product manager, later told Harry McCracken of *TIME* that "the ultimate April Fools' joke was to launch something kind of crazy on April 1st and have it still exist on April 2nd." The service behind the joke had been nearly three years in the making. Paul Buchheit, Google's 23rd employee, began it in August 2001 under the code name Caribou, and built a first searchable mail prototype in about a day by adapting the search code of Google Groups. About a dozen people were working on it by launch. They ran it on about 300 old Pentium III machines that nobody else at Google wanted, and Buchheit described the trap they were in with some precision: "We couldn't get many machines because people thought we couldn't launch."

What Google did with those machines is the part that concerns us. It did not open Gmail to everyone. It gave accounts to about 1,000 people outside the company, let each of them invite a couple of friends, and widened slowly from there. McCracken is careful about the motive: "The limited rollout had been born of necessity, but 'it had a side effect,' says Harik", meaning Georges Harik, who oversaw most of Google's new products at the time. The side effect was demand. Invitations became a prized possession and sold on eBay for $150 and more. The gate turned out to do a third job as well, one nobody had designed it for. On 6 April, five days after launch, 31 organizations and advocates wrote to Larry Page and Sergey Brin asking Google to suspend Gmail, because it scanned the text of messages to place advertisements beside them, and California State Senator Liz Figueroa drafted a bill to require consent before mail could be scanned for ads. Google met that objection while its users numbered in thousands. The gate stayed in place for nearly three years, until sign-up opened to all on 14 February 2007, and the "beta" label stayed on the logo until 7 July 2009, when Google removed it from Gmail, Calendar, Docs and Talk together. By then the label carried a cost nobody had counted at the start: business customers did not want to adopt something that sounded unfinished, and Google said as much when it took the label down. Gmail grew all the same, to 425 million active users by 2012, although nothing in the record suggests that the long beta caused the growth, only that it did not prevent it.

I tell this story at the start of the last chapter because one launch shows, in small, what this book has argued in parts. A launch gated by who may enter is a product decision as much as a capacity one, and it does more jobs than its designers intend. Google meant to ration machines, and found that it had also manufactured demand, bought time to answer a public objection about privacy, and, years later, put off the customers who would pay the most. Some of that was luck, good and bad. The lesson I draw is modest and practical. Write down which jobs a launch is meant to do before it is done, so that afterward we can tell what we planned from what merely happened. That is also the method of this chapter. The Resilience book's capstone attended one review, and the Operations book's lived through one day. A product fits neither shape, because it is a bet that is made, tested, built, shipped and judged over many months. So this capstone follows one document, the bet memo for Verified Resale, through the five checkpoints at which Encore read it again.

Encore, at about 400 engineers, wrote that memo in the late winter of its ninth year. The Vesper Hale on-sale and the added stadium dates were behind it, and so was the Rowmate key leak, which had shown how little Encore controlled the resale that already ran through its partner application programming interface (API). Chapters 1 to 9 followed Verified Resale through one practice at a time: strategy, discovery, measurement, pricing, design, the design system, the phone and the partner API. Here we follow it through time, and Figure 10.1 lays out the route. Each section that follows is one checkpoint, and each names the chapters whose practices it draws together. The two capstones divide the work. This one asks why Encore made the bet and whether it paid, up to the review at month 18. The Software book's Chapter 11 asks how the code and the engineering system changed to deliver it, and reviews that change at month 24. When this chapter reaches engineering, it states the outcome and points there.

| Checkpoint | Month and season | State of the bet | This book | The Software book |
|---|---|---|---|---|
| 10.1 The bet | 0, late winter, year 9 | Memo written; first tranche funds discovery | Chapters 1–5 | Sections 10.4, 9.2–9.3 |
| 10.2 Designing it | 4, late spring | Discovery done; decision to build; Resale team formed; 23 dependencies | Chapters 6–9 | Sections 9.5, 7.3, 8.2–8.3 |
| 10.3 Building it | 9, autumn | Walking skeleton on the golden path; Rowmate certifying; 14 dependencies | Sections 2.5, 3.1, 3.4 | Sections 11.1–11.3 |
| 10.4 Launching it | 12, winter, year 10 | Three organizers, Rowmate, one market (France) | Section 4.5, Chapters 8–9 | Section 11.4 |
| 10.5 What Encore learned | 18, summer, year 10 | The memo's review; Rowmate and Tessera live | Sections 3.1, 5.5 | Section 11.5 |

*Figure 10.1 — One decision through 18 months. Each checkpoint rereads the same memo; the right-hand columns show where the practices it draws on are taught.*

### 10.1 The Bet

#### The diagnosis {#c10-diagnosis}

The memo's first page is a diagnosis, written in the shape Richard Rumelt gave good strategy and Section 2.1 taught: a diagnosis of the challenge, a guiding policy for meeting it, and coherent actions that carry the policy out. The challenge was not new, and that was part of the difficulty. Since its sixth year Encore had run Partner Listings, which let authorized partners read its event listings and post resale offers that appeared as "resale available at Rowmate" links on sold-out event pages. The ticket itself changed hands outside Encore. The seller forwarded the original pass, and Encore checked nothing beyond the partner's word. The memo named four consequences of that arrangement. The same barcode could be sold to several buyers, and only the first through the door got in. Organizers had no control over price or timing. Organizers took no share of the resale fee. And buyers were never screened, so the bots that Bot Screening turned away from the primary sale could buy freely on the secondary one. The Rowmate leak had made the last point concrete, because the leaked key, scoped only to `listings:read` and `resale:write`, was enough to create two fraudulent listings, removed before anyone bought them. The rest of the evidence was in Encore's own records. In the 12 months before the memo, Support had handled about 3,400 cases of dead or fake resold tickets, and within a day of the Vesper Hale on-sale more than 9,000 of its tickets were on unofficial sites.

A diagnosis has to say what the harm comes from, and Section 2.1 had already settled that: the harm comes from resale that nobody controls, and resale as such is something fans need. That sentence did a great deal of work. It turned the objection that had hung over the idea from the beginning ("we fight scalpers; now we host resale?") into a design constraint. Encore would not host resale on anyone's terms. It would host it on terms it could enforce at the barcode, and the guiding policy said so in one line: bring resale inside Encore, where every rule can be enforced on the ticket itself. The coherent actions followed from the policy. Every resold ticket would be reissued under a new barcode, every organizer's rules would be applied, only vetted partners would be admitted, and the same bot controls would guard the resale checkout as guarded the primary one. Partner Listings would be retired, with a year's notice to partners from the day Verified Resale launched (Section 9.4).

The jobs behind the diagnosis came from Section 2.2, and they explain why the product has three sides and four parties. The fan who cannot go wants the money back safely and quickly, and does not want to let down the friends in the seats beside them. The fan who wants in wants a real ticket at a price that does not feel like extortion, and fears being turned away at the door more than paying too much. The partner wants a legitimate market and inventory it can trust. The organizer wants control over price and timing, real fans in the seats, and a share of whatever the resale earns. These jobs partly conflict, and Section 2.3 showed why that conflict sits at the center of the product, and why a market with three sides needs its rules designed as carefully as its screens.

Encore was not alone in reaching this diagnosis, and the memo said so: Ticketmaster's closure of its European secondary sites in 2018, in favor of a face-value exchange, which Section 2.1 told, had followed scrutiny of the secondary market by the UK Competition and Markets Authority (CMA). A competitor's choice proves nothing about whether Encore's bet would pay. What it does show is that the harm in the diagnosis is real, that it has been acted on in Encore's own market, and that regulators have noticed it, which is the kind of evidence a diagnosis should rest on.

#### Where to play {#c10-where-to-play}

Section 2.4 drew the Wardley map that answered the next question: which parts of Verified Resale should Encore build, and which should it leave to others? Anchored on the need "a fan holds a guaranteed ticket", the map put reissue and revocation at the gate in the custom middle of the chain, possible for nobody else because only Encore issues the barcodes, and organizer rules near genesis. The memo recorded the map's output in two lines: build reissue and rule enforcement, and partner for listings. Rowmate already ran a marketplace with fans on it, and it would have been both expensive and hostile for Encore to build a rival storefront for resale when it could instead make every partner's storefront trustworthy. That Rowmate was a competitor as well as a partner did not change the choice; it changed the terms, which Section 2.4 worked through and the Software book's Section 8.3 turns into a partner program.

Wardley maps are a thinking tool, widely used by practitioners and thin in published outcome evidence, and the memo used the map only to make an argument visible, never as proof. The proof it would accept was the objectives that Section 2.5 drew from the strategy. The Resale trio would own one product outcome, "verified resales completed per eligible event", rather than a revenue figure it could only influence. The memo also named the one date that could become a high-integrity commitment, the kind Section 2.5 reserves for real deadlines: the resale clause had to be in the contracts organizers signed in the autumn contract season, because that season decided which tours of the following year could carry resale at all. As Section 2.5 recounts, Encore made that commitment only at month 4, once discovery had shown what it would be promising.

#### Discovery before code {#c10-discovery}

The memo did not fund a build. Its first tranche bought four months of discovery for the trio, a product manager, a designer and a tech lead, and within it an appetite of six weeks for two small teams, lent from Orders & Payments and Partner APIs, to run the prototypes (Section 3.4). The trio interviewed fans, organizers and Rowmate every week, in the manner of Section 3.1: 22 organizers, 31 fans and six people at Rowmate over the four months. It kept an opportunity solution tree whose single outcome was the north star described below. The design partners were the six Section 3.3 recruited, all mid-size festival and tour promoters: three in France, two in Belgium and one in the Netherlands. One of the French three, a promoter of arena tours, was openly hostile to resale. Rowmate took part in a separate, smaller partner program of its own.

Two assumptions in the memo were marked as riskiest, because the bet failed if either was false and the only evidence for either was what people had said in interviews. The first was that organizers would set rules and keep resale switched on. The second was that buyers would trust a ticket that had been reissued, believing both that the new one would scan and that the old one would not. Section 3.2 described how each was tested before any service existed. A Wizard-of-Oz pilot ran resale on four real shows, two in Lyon and two in Antwerp, about 11,200 tickets in all, with Support agents doing each reissue by hand through their old lost-ticket screen behind a real fan interface. It completed 191 resales from 268 listings, at a median of 14 Support minutes each, and no fan holding a reissued ticket was refused at the door. Four shows could not measure demand, and the pilot's pre-registration said so in advance: demand was read qualitatively. A clickable rules screen tested with all six promoters showed that organizers could express their rules. And when the trio asked what organizers wanted from resale, control came up in 19 of the 22 organizer interviews and the fee share in eight. By control they meant when resale opens, how many tickets one fan may list or buy, and whether it happens at all. Both riskiest assumptions came back supported. What discovery could not show was how organizers would actually behave once resale was live on their own events. We will see at month 18 what that left out.

#### Price before product {#c10-price}

Madhavan Ramanujam and Georg Tacke's argument, which Section 5.1 developed, is that willingness to pay should be tested while the product is still a concept, because the answer changes what is built. Encore held those conversations inside discovery, with the six design-partner promoters and with Rowmate, and set the price before the first screen was designed. The resale price is capped at face value, and organizers can only tighten the rules, never loosen them. The buyer pays a 10% service fee, included in the all-in price shown from the first screen. The fee is split 4 points to the partner through which the buyer purchases, 3 to the organizer and 3 to Encore, whose share carries the payment service provider (PSP) fees, fraud losses and support. When the buyer purchases in Encore's own app, Encore keeps the partner's 4 points as well. The seller receives the resale price in full, five days after the event, once the reissued ticket is beyond the reach of a dispute. A €60 ticket resold at €60 costs the buyer €66, of which the partner receives €2.40, the organizer €1.80 and Encore €1.80.

Section 5.2 compared the models Encore considered, among them a flat fee and a fee that fell as the price neared face value, and explained why a fixed percentage won. Two of the reasons matter here. The first is that the case was honest about its weakest term. Encore's variable cost of serving one more ticket is about €0.12 (the Resilience book, Section 2.5), but the pilot's hand-done reissues cost several times what Encore's 3 points could pay in Support time. So the memo recorded the business case as conditional: once reissue was automated, Support time per resale had to fall to a fraction of the pilot's figure, or Encore would lose money on every resale. That condition became one of the memo's guardrails. The second reason is that a split that organizers could see and predict was itself part of what Section 5.1 called communicating value: the organizer's message was control and a share, and a share that moved with the price would have been harder to explain than one that did not.

#### The memo {#c10-memo}

All of this lived in one document. The diagnosis, the map and the questions for discovery and pricing were in it at month 0, and the answers went into its later revisions. Its form deserves attention, because the form is what makes it possible to reread the document later. Writing a bet down before building it is an old discipline with a well-documented public variant. At Amazon the variant is the PR/FAQ (press release and frequently asked questions): a press release of about a page written as if the product had already launched, followed by the questions a skeptic would ask, with answers. Colin Bryar and Bill Carr, in *Working Backwards*, date the practice to Amazon's move into digital media in the early 2000s. Werner Vogels described the reasoning in 2006: "Writing a press release up front clarifies how the world will see the product — not just how we think about it internally." Encore's **bet memo** is an adaptation of that form, and the difference is worth stating. It is a document that states a product decision as a wager: what we believe, what we will spend, how we will know, and when we will stop. The press release opens it because writing from the customer's side first keeps the memo honest about value. The rest exists so that the bet can be judged later against what it said.

The FAQ is where the riskiest assumptions go, and it is the part most often written badly, because it is tempting to answer the questions we can answer well. Amazon's own history carries the warning. The Fire Phone launched in July 2014 at $199 on contract with AT&T, was cut to $0.99 on contract within weeks, and in October Amazon took a charge of $170 million, mostly for Fire Phone inventory and supplier commitments. A company that had made writing its bets down a habit for a decade still made this one. A memo guarantees nothing about the quality of the decision; it is only as good as the honesty with which its FAQ answers the questions nobody wants to ask.

Three further ideas gave the memo its teeth. The first is appetite, which Ryan Singer's *Shape Up* defines as "the amount of time we want to spend on a project, as opposed to an estimate." Encore's appetite was 12 months from the memo to the first resold ticket scanned at a gate, and it was a statement of what the bet was worth, set before anyone had forecast what it would cost. The second is the **kill criterion**: a condition, written in advance, under which we stop. Annie Duke, in *Quit*, recommends setting kill criteria in advance, best expressed as a state and a date, because a criterion set before the work begins is set by people who are not yet invested in continuing it. The third is the distinction Jeff Bezos drew in his 2015 letter to shareholders between decisions that are hard to reverse, one-way doors, and decisions that are easy to undo, two-way doors, which the Architecture book used for data migrations. The memo marked its doors. The fee split and the partner terms, which promise partners 12 months' notice of any breaking change, were close to one-way, and deserved the slow deliberation the memo gave them. How the fee was displayed, or the order in which listings appeared, were two-way doors, to be decided quickly and changed on evidence.

Here is the skeleton of revision 0, as the trio presented it:

```
VERIFIED RESALE: bet memo, revision 0 (month 0, late winter, year 9)
Press release  One page, dated launch day, written as if it had happened
Diagnosis      Uncontrolled resale harms fans and organizers (Section 2.1)
Policy         Bring resale inside Encore; enforce every rule at the barcode
FAQ            Riskiest first: organizers set rules and keep resale on;
               buyers trust a reissued ticket
Appetite       12 months to the first resold ticket scanned at a gate
North star     Verified resales completed per eligible event (scanned at the door)
Guardrails     Primary sell-through; bot rate on resale checkouts;
               organizer opt-out rate; Support minutes per resale
Kill K1        Month 4: fewer than 2 of the first 3 organizers we recruit commit
               a real event, or a voided pass still scans offline in the prototype
Kill K2        Month 18: below 10 completed resales per eligible event, or primary
               sell-through more than 2 points under its synthetic control
Doors          One-way: fee split, partner terms. Two-way: display, ordering
Tranche 1      Discovery, months 0–4: the trio; six weeks of two lent teams
Left open      Listing in Encore's app; seller payout timing; default window
```

Two things in that skeleton are easy to miss. The north star joined Section 2.5's outcome to Section 4.1's sharper version: a resale counts as completed only when the reissued ticket scans at the door, which keeps the number honest about the one thing the product promises. And the "left open" line is a strength of the memo. A memo that pretends to have settled everything invites people to believe it, and the open questions are where discovery's next weeks should go. All three were closed by month 4.

The memo ended with a pre-mortem. Gary Klein's method, published in the *Harvard Business Review* in 2007, asks a team to imagine that the project has already failed and to write down why. It works because it gives permission to say aloud what people otherwise keep to themselves. Encore's trio collected about 20 stories, and three recurred. In the most common, a stadium night arrives on which the old and new barcodes both admit someone, and the press reports that Encore's verified tickets are no safer than a screenshot. In the next, organizers refuse to enable resale because they see Encore taking a cut from their fans. In the third, Rowmate leaves, and the product has a pool of listings and no storefront that fans already use. Each of the three became a line in the FAQ, and the first became a test that would run on every build.

The memo works under four conditions, and Encore held to all of them. It was written before the build was funded. Its metrics and kill criteria were concrete enough to be checked by someone who had not written them. It was read and challenged in a meeting of the product, engineering and finance leads, which began with the strongest objection read aloud: that an anti-scalping company hosting resale would look, to fans and artists, like a company hosting touts. And it was reread at every checkpoint, which is the structure of this chapter. The mechanics of the tranches belong to the Software book (Section 10.4), and so do the formation of the Resale team by isolation (Section 9.2) and the trio's charter (Section 9.3). What belongs here is the decision those mechanics serve.

**Recap.** The bet began as a diagnosis: the harm lay in uncontrolled resale, and only Encore could control resale at the barcode. Discovery and pricing came before design, and the memo gathered their questions into one document with an appetite, a north star, guardrails, kill criteria written as a state and a date, and its doors marked. The form owes much to Amazon's PR/FAQ, and the Fire Phone is a reminder that the form guarantees nothing; what makes a memo useful is that it is honest about what is risky, and that it is read again.

**Exercise 10.1.** Write a one-page bet memo for an initiative of your own: a diagnosis in Rumelt's three parts, an appetite, a north star and two guardrails, and two kill criteria, each a state and a date. Mark every commitment as a one-way or a two-way door. Then hold a 30-minute pre-mortem with two colleagues and add the top three failure stories to the FAQ.

### 10.2 Designing It

At month 4 the trio reread the memo against what discovery had found and wrote revision 1. Both conditions in K1 had been tested and passed. The first three organizers recruited, who became the three French design partners, had all committed a real event for the launch, the hostile arena-tour promoter only one, and on the tightest rules the console allowed. The voided pass in the prototype did not scan offline, and in the pilot three revoked Apple Wallet passes, forwarded by sellers before the sale, were refused at the gate. The open questions had closed. Fans could list in Encore's own app as well as through partners, with Encore keeping the partner's 4 points; sellers would be paid five days after the event; and the default resale window would run from purchase until two hours before doors open, which organizers could shorten. Encore decided to build, and made the contract season its high-integrity commitment. The Resale team formed from people in Orders & Payments and Partner APIs, with the trio and a staff engineer, and the first quarterly plan showed 12 teams with work to do and 23 dependencies among them. How the team was formed and the plan drawn is the Software book's subject (Sections 9.2 and 10.2).

#### The experience {#c10-experience}

Verified Resale has three faces, and Section 6.2 gave each the posture it needs. The organizer's rules console is sovereign: it lives inside a console used for hours at a time, and it can be dense. The fan's purchase is transient, a few screens and one decision each. The wallet pass is nearly daemonic, consulted at the door and otherwise ignored. Because organizers set resale rules only a few times a year, the console opened on presets with an advanced path, as Section 6.2 prescribed for perpetual intermediates.

The monthly usability tests of Section 6.3 found the problem that most changed the design. Sellers saw "Sold" and did not believe their old ticket was void, so some of them kept the pass in their wallet "just in case", and a few forwarded it to a friend. Section 6.1 named it a gulf of evaluation: the system knew the ticket was dead, and nothing on the screen said so. The fix was to make the ticket itself change. On sale, the seller's ticket card turns to a cancelled state, its barcode greyed and struck through, with the line "Sold and reissued to the buyer. This ticket will not get you in." The next round of tests found that every participant now understood the old ticket was dead.

Accessibility was built in from the first component, as Section 6.4 requires under the European Accessibility Act, and one rule went beyond the screen. Accessible-seat tickets can be resold, but only to buyers who attest that they or someone in their party need the seat's features; Encore asks for no proof, because proof of disability is health data it has no lawful need to hold. The rule was drafted with disability organizations. The design system took two new patterns, `VerifiedBadge` and `ReissueStatus`, and extended a third, `PriceBreakdown`, to show the cap. Following the contribution path of Section 7.2, both new patterns began as candidates in the Resale team's code and were promoted to the core once Mobile App and Fan Messaging needed them.

#### The ticket in the phone {#c10-phone}

Section 8.3 described the ticket that makes reissue meaningful. Every mobile ticket at Encore has carried a rotating barcode since the eighth year, a time-based code generated on the device from a per-ticket secret, so a screenshot stops working within moments. (The barcode is the same entry credential the Architecture book called a QR code.) Reissue gives the buyer a new ticket identity with its own secret, voids the seller's pass, and adds the old barcode to the revocation lists that gate scanners hold for offline validation. Whether the old ticket is dead at a gate with no signal therefore depends on how fresh the scanner's list is, and Venue Entry's work was to make sure it was fresh before doors opened.

The release train set the schedule. Encore ships the fan app weekly, so a missed train costs a week, but the reissue-aware ticket view had to reach the phones of fans who might sell or buy, and old versions linger for years. Section 8.2 described the decision. The soft floor on app versions went up three months before launch, so that by launch day nearly every active phone could show a reissued ticket correctly, and an app below the reissue-aware version cannot list or buy at all. The hard floor did not move, because no fan who merely holds a ticket needed to be stranded for resale to be safe. Resale became the fan app's 15th feature module, owned by the Resale team. How revocation works in the code, and how it was made safe, is the Software book's Section 11.1.

#### The partner API {#c10-partner-api}

The partner API was designed from the outside in, as Section 9.1 taught, starting from Rowmate's job story: when a fan lists on our site, we want to know at once whether the organizer allows it, so that the listing never fails later. That story produced a `validateOnly` request that answers "would this listing be accepted?" before anything is created. Listing and purchase are idempotent. Withdrawal is a custom method, `POST /v2/listings/{id}:withdraw`, and reissue is a long-running operation with its own resource, because voiding a pass, issuing a barcode and delivering a wallet pass take longer than a request should wait. Partners learn that a listing sold through a thin, signed `listing.sold` webhook and fetch the details, because rules and prices may have changed since the listing was made, and they mirror the pool through an inventory feed that Rowmate reconciles hourly and on every rule change (Section 9.5). Rowmate built against the contract's mock server for three weeks before the service existed.

One engineering question had to be settled before the product could be built: which team owns reissue? The Software book tells the argument (Sections 9.5 and 11.1); its outcome was that the Inventory team, which owns the barcode core, owns issuance and revocation, and Resale calls it. For the product the verdict mattered for one reason. The question "is this barcode valid?" would have exactly one owner, the same team that answers it for every primary ticket, and the fan's guarantee would rest on it.

#### The price in the system {#c10-price-system}

A price lives in a system long after the meeting that set it, and Chapter 5 showed where. Organizer resale rules are typed configuration owned by the Resale service, and the controls available to each kind of organizer are entitlements held as versioned data (Section 5.3). The Software book's Section 7.3 builds that service. Every completed resale produces one `ResaleCompleted` event, emitted only after the reissue has succeeded, metered once, rated by the price book in force when it happened, and split into partner, organizer and Encore shares that the finance ledger reconciles daily (Section 5.4). The cap at face value is a product rule and also a compliance capability. Ireland's Sale of Tickets Act 2021 already forbids resale above face value for designated events, and rules of this kind arrive country by country, as Section 5.5 described.

Verified Resale's one artificial intelligence (AI) feature belongs here, because it sits on top of the rules. An organizer writes a request in plain language, such as "no resale until a week after the on-sale, two per fan", and the organizer rule assistant drafts the typed rule set and a plain summary, which the organizer confirms before anything applies. The assistant can express only rules the type system allows, so the rule that organizers can only tighten holds whatever the model says. Section 6.5 designed the assistant, and the Software book's Section 3.5 describes its evals.

#### The marketplace rules {#c10-marketplace-rules}

The last design artifact was the rulebook for the market itself. Partners are vetted before they receive sandbox credentials, certified in the sandbox before they receive production credentials, and bound by terms that say what they may and may not do; the Software book (Sections 8.2 and 8.3) treats those programs as a business. Some rules are as old as Partner Listings: partners have never been able to buy primary tickets, since the original key scopes. Others are new. Every resale buyer passes Bot Screening and the per-buyer limits, and Bot Screening's existing commitment, no more than one false block per 1,000 admitted sessions, covers the resale checkout as it covers the primary one. Partners read the same coarsened availability everyone gets and never see sales velocity, which Encore keeps confidential because scalpers would pay for it. And only fans resell: Encore admits no professional resellers, which also keeps it clear of the trader-traceability duties that the European Union's (EU) Digital Services Act places on marketplaces that host traders. Whether the market would reach enough listings and buyers to be worth visiting, the question of liquidity and ignition, is the Software book's Section 8.2.

**Recap.** At month 4 discovery had closed the memo's open questions and the decision to build was made. The design then spread across artifacts with different owners: flows for three postures, a wallet pass that visibly dies, a partner API built from partners' jobs, rules and fees as data, and a rulebook for the market. Each artifact traces back to a line in the memo, which is what kept 12 teams' work one product.

**Exercise 10.2.** For one feature you are building, list every artifact that defines it: flows, components, API operations, entitlements, configuration and policies. Name the owner of each, and mark the ones whose owner is not on the team that proposed the feature. Those are where the product's intent is most likely to be lost.

### 10.3 Building It

By month 9, in the autumn of the ninth year, the memo's second revision recorded a different kind of progress. The product side needed only the state of each promise, and the revision recorded it briefly. A walking skeleton ran from the partner API through Resale and Seat Inventory to a test wallet. The barcode core, written in Encore's first year and understood by one remaining author, was under tests that made it safe to change. The partner API was in the sandbox and Rowmate was certifying against it. Twenty-three dependencies had become 14. And in the autumn contract season, organizers signed contracts with the resale clause in them, which honored the memo's high-integrity commitment a season before any fan could resell a ticket.

#### What the product asked of engineering {#c10-asked}

The trio's job during delivery was to keep the product's intent intact while 12 teams built it, and the most effective tool they had was to write that intent in a form engineering could test. The memo's promises became four commitments: reissue under a new barcode, with the old one dead at every gate; organizer rules as typed configuration that can only tighten; a partner API with a sandbox and certification; and five fairness invariants, which Encore states in exactly these words:

1. Partners never buy primary tickets.
2. Only tickets bought through the Gate, within the per-fan limit, can be listed.
3. Organizer caps and rules can only tighten.
4. Every resale buyer passes Bot Screening and the per-buyer limits.
5. Partners never see sales-velocity data.

Each invariant is a sentence a fan or an organizer could understand, and each runs as a test on every build (the Software book, Section 11.3, tells how). That pairing is the point. A product promise that exists only in a memo can be eroded one reasonable change at a time, with no single change appearing to break it. An invariant under test fails the build instead, and someone has to decide in the open what to do about it. The first of the pre-mortem's failure stories, an old barcode and a new one both admitting someone on a stadium night, is now a test that runs thousands of times before any fan could meet it.

#### Scope held, scope cut {#c10-scope}

At month 4 the first forecast, a Monte Carlo simulation of the kind the Software book's Section 10.3 teaches, put the launch about two months beyond the appetite. The trio did what *Shape Up* recommends and treated the appetite as fixed and the scope as the variable. Singer calls the principle "fixed time, variable scope", and his circuit breaker states its consequence bluntly: "If they don't finish, by default the project doesn't get an extension." Encore did not adopt the whole method. It does not run six-week cycles across 40 teams, and Section 3.4 explained why it keeps its quarterly planning. It borrowed the two ideas that mattered, and they work under one condition, which Encore met: the people who set the appetite had the authority to cut scope, and the work had been shaped before it was forecast.

The cuts were chosen by one test: after the cut, could the bet still be judged? Tessera moved from launch to the months after it, because a second partner adds reach but changes nothing the north star or the guardrails needed to measure. Festival passes and other multi-day tickets were excluded from the first release, since they would have doubled the rules engine's cases for a small share of resales. The organizer's resale dashboard became a monthly statement, which told organizers what they had earned without the build of a new reporting surface. Rule templates that an organizer could apply across a whole tour were cut as well, on the forecast's evidence (the Software book, Section 10.3), so organizers would set rules event by event, with the console's bulk edits to help. What the trio held was everything the memo's kill criteria depended on: reissue, the invariants, organizer rules, and the measurement of completed resales at the door. A cut that removed any of those would have saved time only by leaving the bet with no way to be judged.

#### Discovery that continued during delivery {#c10-continued}

The weekly interviews did not stop when the build began, because, as Teresa Torres insists, discovery is a habit that continues through delivery. Two findings changed the build. The first came from fans: people who had bought a pair of seats wanted to sell them together, and buyers wanted to buy them together, because nobody wants to sit beside a stranger at a concert they planned with a friend. Listings of a pair became one listing by default, which the seller could split, and the cut of festival passes paid for the work. The second came from the organizers' box offices, which handle the fan whose phone has died at the door. They needed to see that a ticket had been resold, and to whom it now belonged, before they could help, so the box office's ticket lookup learned to show a reissued ticket's history. Neither finding was in the memo, and both would have reached Support as complaints in the first month had the trio stopped listening.

#### The engineering story is another book {#c10-another-book}

Everything else that happened between month 4 and month 12 is engineering, and the Software book's Chapter 11 tells it, from the first test written against the barcode core to the flags removed after launch. Two of its outcomes touched the product directly. Knowledge of the barcode core spread from one engineer to four, so the fan's guarantee no longer rested on one person. And the change to an opaque ticket identity, announced to partners at month 2, kept the promise of 12 months' notice: the old barcode format stays accepted on the partner API until month 14. What the product side needed from the rest was smaller: whether each commitment above was true, and on what date.

**Recap.** Building began with the product's promises turned into tests, so that intent survived 12 teams and many reasonable changes. When the forecast outran the appetite, the trio cut scope by asking whether the bet could still be judged after each cut, and kept listening to customers, which changed the build twice. The engineering itself belongs to the Software book; the product's part was to know which promises were true.

**Exercise 10.3.** For one initiative of yours, list the product commitments engineering must make true, and write each as a sentence a customer would understand. Mark which ones a test already protects. Then name the one you would cut first if the date held and the work grew, and say whether the bet could still be judged without it.

### 10.4 Launching It

Revision 3 of the memo, at month 12, was mostly a launch plan, and the launch is where Gmail's lesson applies most directly. Verified Resale opened in the winter of the tenth year to three organizers, one partner and one market.

#### The launch plan {#c10-launch-plan}

A launch staged by audience widens access by who may enter: a cohort of customers, then a market, then the next. Gmail did it with invitations, and Facebook did it in 2004 with college email addresses, opening at Harvard in February and at Columbia, Stanford and Yale in March, so that each new cohort arrived already dense with people who knew one another. It is easy to confuse this with progressive delivery, and the two should be kept apart. Progressive delivery releases code to a growing share of traffic so that a fault reaches few users, and it belongs to the Resilience book (Section 4.3); every Verified Resale change went through it. A launch staged by audience decides which customers the product serves, and in what order, and that is a product decision.

Encore's first cohort was the three design-partner organizers, chosen because they had shaped the product and would forgive its first mistakes. Each cohort had an entry criterion and an exit criterion written into the memo before launch, so that widening and retreating were both decisions made in advance. This is the product counterpart of the launch checklists in Google's *Site Reliability Engineering*, and Figure 10.2 shows Encore's version. The thresholds are Encore's own judgments, set by the trio from the pilot and the design partners' volumes; they come from no published standard.

| Cohort | Who may enter | Entry criterion | Exit (retreat) criterion |
|---|---|---|---|
| 1 (month 12) | Three design-partner organizers, Rowmate, France | Rowmate certified; invariants passing on every build; soft app floor reached by 95% of active phones | Any reissued ticket refused at a gate, or any old barcode admitted |
| 2 (about month 13) | All consenting organizers in France | 200 completed resales; no gate failures over 20 events; bot rate on resale checkouts no higher than on primary | Organizer opt-out rate above 15%, or Support minutes per resale above the business case's ceiling |
| 3 (about month 15) | Tessera, France | Tessera certified in the sandbox | As cohort 1, for Tessera's buyers |
| 4 (decided at month 18) | Further markets | The memo's review | Kill criterion K2 |

*Figure 10.2 — Verified Resale's launch cohorts, each with conditions to proceed and to retreat. Belgium joined at month 16 on cohort 2's criteria; the thresholds are Encore's.*

The plan also said who would be told before the first fan could resell. Gmail met its privacy objection five days after launch; Encore preferred to meet its own before launch. It briefed national consumer bodies and the organizers' associations in France on the product, the cap and the reissue guarantee, because the question "we fight scalpers; now we host resale?" would be asked in public, and it was better to answer it to people who had read the rules. And the plan avoided one of Gmail's costs deliberately. The product was never labelled a pilot or a beta to organizers. It was "Verified Resale in France", because organizers sign contracts a season ahead, and a cautious organizer, like Google's business customers, will not build next year's tour on something that sounds unfinished.

#### The experiment that could not be clean {#c10-experiment}

Section 4.5 promised that Encore would judge Verified Resale without a clean A/B test, and explained why it could not have one. Fans, sellers and organizers share one pool of seats, so a treatment that helps one fan can take a resold seat from another, and the comparison between arms measures transfers more than effects. Airbnb's fee meta-experiment, which Section 4.5 tells, put a size on that bias: at least 20% of the effect an individual-level test estimated for a fee increase was interference. What remained for the launch was to put Section 4.5's plan into use, and to keep to it once results began to arrive.

The plan used three designs, each answering a different question. For the question the memo cared about most, whether resale eats the primary sale, Encore used a **synthetic control**: an estimate of what a treated market would have done without the treatment, built as a weighted combination of untreated markets that tracked it closely beforehand. France had been chosen first for business reasons, its design partners and its contract season, so no randomized comparison of markets was available. Synthetic France was built from nine EU markets without resale, using 104 weeks of primary sell-through per eligible event. Alberto Abadie's conditions for trusting the method, a long pre-period, a pool of comparable donors, no spillover into them and no shock that strikes one market alone, were argued in the plan one by one, and Belgium was removed from the donors before the analysis began, because Belgian fans cross the border for French dates. When Belgium itself went live at month 16, the plan already said which estimator would handle a rollout that reaches countries in different months, because the ordinary regression gives biased answers there (Section 4.5).

For the narrower question of how to show the fee, Encore randomized by event. When the launch widened to all consenting French organizers, 38 of them let about 520 of their events be assigned at random to one of two presentations of the same all-in price: a single figure, or the figure with the split among partner, organizer and Encore itemized beneath it. Every fan of a given event saw one presentation, and every fan paid the same 10%, because Encore never varies the price a given fan pays (Section 5.5). Section 4.5 records why no switchback was used. The third design was a holdout: nine French organizers who agreed to go without resale for six months, were told what the holdout was for, and were free to leave it.

All of it was pre-registered before any fan had resold a ticket: the metrics, the donors, the checks and the decision rule. The overall evaluation criterion (OEC) of Section 4.1 was the memo's north star.

```
PRE-REGISTRATION VR-FR-01 (registered month 11)
Question     Does Verified Resale change primary sell-through in France?
Design       Synthetic control; unit: market-week; treated: France
Donors       Nine markets without resale; Belgium excluded (cross-border fans)
Pre-period   104 weeks of primary sell-through per eligible event
OEC          Completed verified resales per eligible event
Guardrails   Primary sell-through: no worse than −2.0 pts vs synthetic France
             Bot rate on resale checkouts: no higher than on primary
             Reissued tickets refused at gates: fewer than 1 in 10,000
Fit checks   Pre-period prediction error reported; placebo run on each donor
Decision     Widen beyond France only if all guardrails hold; review month 18
Not claimed  Displacement of grey-market resale: no data Encore controls
```

The last line matters as much as the rest. The diagnosis was about the grey market, and the grey market is the one thing Encore cannot observe, because it happens on sites and in messages Encore does not see. The closest measurement Encore owns is at its own doors: duplicate-ticket rejections at the gate, which on Partner Listings were mostly copied passes. The memo treated a fall in those rejections as supporting evidence, and any claim about displacement as qualitative. The placebo runs are the method's own honesty check: if a donor market, treated as if it had launched, showed an effect as large as France's, France's effect would mean little.

#### The first partners {#c10-first-partners}

Rowmate was the first partner, and the irony was not lost on anyone. It was Rowmate's 26-month-old key, committed to a public repository by a contractor, that Encore had revoked in 38 minutes in the eighth year, after it had been used to post two fraudulent listings. Encore kept Rowmate and changed the structure around it. Partners received sandbox credentials at once and production credentials only after certification, the checklist of Section 9.4: handling rule changes, verifying webhook signatures, retrying safely. In production they authenticate with 15-minute tokens bound to a client certificate, the arrangement the Resilience book (Section 7.2) put in place after the leak, so a key committed to a repository today would expire before anyone could use it. Rowmate passed certification at month 11.

Tessera followed at about month 15, after its own certification, and was live in 11 days, a speed the Software book's Section 8.3 credits to a partner program built with the second partner in mind from the start. Both partners hold terms that promise 12 months' notice of any breaking change to the API, the lesson Section 9.4 took from Twitter's treatment of its developers in 2012. At the month-18 review there were two partners, and no third had been signed.

#### The first resold ticket {#c10-first-ticket}

The first resold ticket belonged to a fan in Lyon who could not go to a sold-out Saturday concert there, promoted by one of the three French design partners. Its face value was €80. Figure 10.3 traces it through the product, step by step, with the team that owns each step and the section of this book that taught it. The Software book's Section 11.4 traces the same ticket through the code.

| Step | What happened | Owner | Where taught |
|---|---|---|---|
| 1 | On Tuesday evening the seller lists the ticket on Rowmate; Rowmate's `validateOnly` call confirms it was bought through the Gate, within the per-fan limit, inside the window | Partner APIs, Resale | Sections 9.1–9.2 |
| 2 | The organizer's rules apply: price at most €80, window open, one listing per fan | Resale | Sections 5.3, 6.5 |
| 3 | The listing enters the pool, visible on Rowmate and in Encore's app | Resale, Mobile App | Section 9.5 |
| 4 | On Thursday at lunchtime a second fan buys on Rowmate, passes Bot Screening and the per-buyer limit, and pays €88 | Bot Screening, Orders & Payments | Sections 2.3, 5.2 |
| 5 | The ticket is reissued under a new identity; the old barcode joins the gates' revocation lists | Inventory, Venue Entry | Section 8.3 |
| 6 | The seller's ticket turns to its cancelled state; the buyer's new pass arrives; "your ticket sold" goes by push, email and inbox | Fan Messaging, Mobile App | Sections 6.1, 8.3 |
| 7 | Rowmate receives a signed `listing.sold` webhook and fetches the result | Partner APIs | Section 9.5 |
| 8 | `ResaleCompleted` is metered: €3.20 to Rowmate, €2.40 to the organizer, €2.40 to Encore | Billing & Payouts | Section 5.4 |
| 9 | On Saturday evening the buyer's rotating barcode scans at the door | Venue Entry | Section 8.3 |
| 10 | Five days later the seller is paid €80 | Billing & Payouts | Sections 5.2, 5.4 |

*Figure 10.3 — The first resold ticket, through the product. Ten steps, nine teams, and the north star counts it only at step 9.*

Read the table's columns separately and two things appear. The "where taught" column covers nearly the whole of this book, which is the reason for tracing one ticket at all: a reader who has followed the chapters one at a time can see here that they describe one transaction. The "owner" column names nine teams for a single sale, and not one of them could have delivered the fan's guarantee alone. That is the plain meaning of the claim, made in Chapter 1, that a product at 400 engineers belongs to the whole organization, whatever team's name is on it. Notice too where the north star counts. Steps 1 to 8 are activity, and only step 9 is the outcome the memo promised.

#### Who decides on the day {#c10-who-decides}

The decision to open each cohort was a go or no-go call made by the Resale trio and its staff engineer, against the entry criteria in Figure 10.2 and nothing else. A decision against written criteria is long-standing practice; Google's launch coordination engineers, whose work the *Site Reliability Engineering* book describes, worked from checklists through as many as 70 launches a week. The condition that makes it work is the one Encore wrote down: the criteria come from the memo and the readiness evidence, and they are fixed weeks before launch morning, the moment when everyone is invested and nobody wants to be the one who says wait.

This meeting is easy to confuse with the readiness review the Resilience book describes, and they answer different questions. The readiness review, held on the Wednesday before a big on-sale, asks whether the system can carry a known peak. The launch decision asks whether a product should reach a new group of customers. Each of the four people in the decision could stop the launch alone, and so could the incident commander rotation if an incident was running. Running the day itself, from the first listing to the first scan, belongs to the Operations book (Chapters 5 and 7).

**Recap.** The launch was staged by who may enter, with each cohort's conditions to proceed and to retreat written before launch, and the public objection answered before the first fan could resell. Because a marketplace defeats a clean A/B test, Encore put Chapter 4's plan into use: a synthetic control, an event-level test of the fee's display and a consenting holdout, pre-registered and honest about what none of them could show. One ticket traced end to end showed that nine teams were needed to keep a single promise.

**Exercise 10.4.** Trace one transaction of your product end to end. For each step, name the team that owns it, the test that protects it, and the point at which your north star counts it. If the north star counts the transaction before the customer has received what was promised, rewrite the metric.

### 10.5 What Encore Learned

In the summer of the tenth year, about six months after launch, the trio, the staff engineer and the leads who had funded the bet met for the review the memo had promised at month 0. Verified Resale was live in France and Belgium, with Rowmate and Tessera. No kill criterion had triggered.

#### The review of the bet {#c10-review}

The review followed the shape of the after-action review that the Operations book (Section 6.4) borrowed from the US Army: what was supposed to happen, what happened, why the two differed, and what to keep or change. Its value depends on one condition above all, that the prediction was written down before the outcome was known. Baruch Fischhoff showed in 1975 that people who know an outcome judge it to have been more predictable than it was, a bias the Operations book (Section 6.2) meets in incident reviews. Without the memo, the review would have been a story told by people who already knew the ending. Figure 10.4 sets the memo's revisions side by side.

| Memo element | Month 0 | Month 4 | Month 9 | Month 12 | Month 18 |
|---|---|---|---|---|---|
| Riskiest assumption | Organizers set rules and keep resale on; buyers trust reissue | Both supported; control means timing and limits | Unchanged | Unchanged | Held; nearly all organizers delayed resale and set limits; caps hardly used |
| Scope | Rules, reissue, one partner | Plus own-app listing | Tessera, festival passes, dashboard and tour templates cut | Pairs listed together | Festival passes next |
| Date | First scan by month 12 | Forecast two months later | Back within appetite | First scan in Lyon | — |
| Kill criteria | K1, K2 defined | K1 passed | K2 unchanged | K2 unchanged | K2 not triggered |
| Open questions | Three | All closed | None | None | Widen; fee; team split |

*Figure 10.4 — The memo across five revisions. The cell that matters most is the riskiest assumption at month 18: it held, for a reason discovery had not seen.*

The numbers came first. The north star, measured across all eligible events in France, stood at an average of 34 completed resales per event against the memo's month-18 target of 30 (a different measure from the Resale team's first live-quarter key result of 40, which counted only the pilot organizers' events; Section 2.5), but the median was 11, because a handful of arena nights produced most of the resales; the trio recorded both, since an average alone would have flattered the product's reach. The synthetic control estimated the change in primary sell-through on resale-enabled events at a fall of 0.4 points, with an interval running from a fall of 1.3 points to a rise of 0.5. The guardrail held, and the review said plainly that the method could not rule out a small harm. The fee-display test found no detectable difference in completed purchases, and fewer support contacts asking where the money went when the split was shown, so the split stayed. Bot rates on resale checkouts stayed below those on primary checkouts. Scans refused at French doors because a barcode had already been used fell sharply on resale-enabled events, which supported the diagnosis without proving that the grey market had shrunk.

Then the harder part. Annie Duke, in *Thinking in Bets*, calls the habit of judging a decision by its outcome "resulting", and a review that only asks whether the kill criteria fired falls into it. Encore's review judged the decisions with the information available when each was made, and recorded the outcomes separately. It found one thing the team had got wrong, one that had gone well by luck, and one that had gone badly despite a good decision.

What the team got wrong was organizers, and the error was subtler than a failed assumption. The memo's riskiest assumption had held: organizers set rules and kept resale on. Discovery had also been right about what they meant by control, which was timing and limits far more than price. Where the trio went wrong was in how organizers would divide. Section 5.1 had found two groups, control-seeking promoters who wanted resale closed until well after the on-sale and revenue-seeking ones who wanted it as wide as possible, and the console's three presets served both: "Fan-first" for the first group, "Standard", open from purchase, for the second and shown first, and "Resale off", which Irish organizers are never offered. The trio expected the two groups to be of comparable size. In practice the revenue-seeking group barely appeared in behavior. Most organizers who enabled resale kept it closed for the first days after the on-sale, set per-fan limits below the event's own, and almost never lowered the cap. Several who had sounded revenue-seeking in interviews did the same. The follow-up interviews found the reason, and it was not money. Organizers feared resale that was visible in the first hours after an on-sale, because to their fans and their artists that looks like scalping whatever the price. The hostile arena-tour promoter had become the heaviest user of the rules, setting exactly that one on every date he put on resale: resale a week after the on-sale, one ticket per fan, close to the very request the rule assistant had been designed around. The interviews had recorded what organizers wanted to control. They had not shown how widely the fear behind it was shared, because people describe their interests more readily than their fears.

What went well by luck was the calendar. No stadium-sized on-sale fell in France during the first two cohorts, so the resale page never met the traffic that follows a large sell-out before the product widened. The guardrails held partly because they were never stressed, and the review wrote that down, because a guardrail that was never stressed has not yet been tested (Section 7.4 describes the review that peak pages need). What went badly despite a good decision was the holdout. Encore was right to require consent and to let organizers leave, and two of the nine did leave early, after their own fans asked why they could not resell. The holdout that remained was too small to say much about lasting effects on primary sales, and the next one will need more organizers to begin with.

#### The product at month 18 {#c10-product-later}

By month 18, 61% of eligible French organizers had enabled resale, and Belgium, which joined at month 16, was following the same curve more slowly. Tessera brought fans whom Rowmate did not reach, and the pool showed the effect Section 2.3 predicted: buyers came where the listings were, and listings came where the buyers were. Discovery continued at its weekly rhythm, and the finding about organizers had already changed the product. The console now shows the "Fan-first" preset first, the pitch to organizers leads with when resale opens instead of with the cap, and the lower cap stays on the advanced path for the few who want it. The platform's own default window, from purchase until two hours before doors, did not change, because the review wanted a season of evidence before changing what every organizer gets without asking.

#### Deciding again {#c10-deciding-again}

The review ended where the memo had begun, with a decision, and it had three options in front of it: widen, change the fee, or stop. Stopping was not supported by anything in the evidence, and the memo's own criteria said so. Changing the fee was a serious proposal. A buyer fee of 8% would have made the product easier to sell to fans, and several organizers asked for it. The review declined it for now, for reasons the memo had prepared. The split was a one-way door, partners held terms with 12 months' notice, and the fee test had varied only how the fee was shown, by design, so Encore had no evidence about price sensitivity and would not gather it by charging fans different prices. If the fee ever changes, it will change for everyone on an announced date, with existing organizer contracts protected by grandfathering and a sunset date, as Section 5.5 describes. Widening was the decision. The second part of the third tranche, held back until this review, funds further markets on cohort 2's criteria, with festival passes added to the rules engine, and with a larger holdout designed from the start.

#### The system and the organization {#c10-system-org}

The engineering has its own review, the Software book's Section 11.5, held at month 24, a year after launch, and the two reviews point at each other without repeating each other's lessons. What it found about the codebase, the platform and the barcode core belongs there. One of its outcomes matters to the product side: partner credentials and shared webhook delivery now belong to the platform group, so the next partner program will not have to build them again.

The organization is this review's business, because it decides who carries the bet forward. The trio stayed together through all five revisions of the memo, and the review judged that continuity to be one of the decisions that had gone well: the people who wrote the riskiest assumption were the people who read the evidence against it. The Resale team, grown well beyond a trio and a staff engineer, will split after the review, along the line between the fan and partner flows and the organizer's rules, so that the organizer side, where the review's main finding lies, has a trio of its own (the Software book, Section 9.2, covers how teams are split). The next tranche was released on the evidence in Figure 10.4 and on flow data from delivery (the Software book, Sections 10.4 and 10.5). And one change reached beyond Verified Resale. Encore's quarterly planning now asks that every bet above a set size arrive with a memo that has kill criteria and a review date, and the review is held whether or not the bet succeeds.

#### What did not change {#c10-unchanged}

Section 1.1 opened this book with Fred Brooks's sentence from "No Silver Bullet" (1986, published in *IEEE Computer* in 1987): "The hardest single part of building a software system is deciding precisely what to build." Eighteen months of Verified Resale confirm it from an unexpected direction. Almost everything that cost Encore effort in this chapter was hard in the way the Architecture book called accidental: dependencies, release trains, credentials, a barcode core that one person understood. The platform, the golden path and, in places, AI assistance made much of that cheaper, and the Software book's Chapter 11 measures how much. None of them touched the question the review found the team had answered imperfectly, which was what organizers feared when they asked for control. That question was essential in Brooks's sense. It came from the problem, from what organizers feared and how fans behave, and no tool could have removed it, because no tool knew it was there. Only weekly conversations, a written bet and an honest review found it, and only once organizers' choices on their own events could be counted.

So the book ends where it began, and I do not think that is a failure of progress. Construction will go on getting cheaper, and as it does, the share of our effort spent deciding what to build will grow, and so will the cost of deciding it badly, because a cheap wrong product still has to be owned, supported and eventually retired. At 400 engineers, as at nine, the essential difficulty lies in choosing what to build, writing the choice down, and having the discipline to read it again. The Software book takes up the building, the Resilience book what it takes to keep the result standing under load, and the Operations book what it takes to run it on the morning that matters.

**Recap.** The review read the memo against the outcome, judged the decisions separately from their results, and found that the riskiest assumption had held for a reason the team had not understood. Luck and good judgment were recorded apart, and the review ended in a new decision made by the memo's own criteria. What the platform and the tools removed was accidental difficulty; the essential one, knowing what customers mean, remained.

**Exercise 10.5.** Take a bet your organization made at least six months ago and find what was written before it was made. Judge the decision and the outcome separately: list one result that came from a good decision, one that came from luck, and one that went badly despite a sound decision. If nothing was written before the bet, record that as the first finding, and write the memo for your next bet before anyone funds it.

### Kata: The Second Night

> **Your brief: "Stayover."** Stayover is a hotel-booking software-as-a-service company with 300 engineers in 30 teams. About 6,000 independent hotels across eight EU countries run their reservations on it, and guests book either on the hotels' own sites or through 40 partner travel agencies that call Stayover's API. A third of all bookings are non-refundable, and each year guests who cannot travel write off about €90 million in rooms they paid for; many try to pass the booking to someone else by email, which hotels refuse because the name does not match the identity check at the desk. The board wants "verified transfer": a guest who cannot travel passes a non-refundable booking to another guest through a partner agency, and the hotel reissues it under the new guest's name. Hotels are split. Some want a share of a transfer fee, some want to forbid transfers on peak nights, and the largest chain says transfers will become a channel for touts who book cheap rooms in advance and resell them before trade fairs. The reservation core was written in the company's first year and has two engineers who understand it. Two partner agencies compete with Stayover's own booking site. The busiest week of the year, a trade fair in one city, is seven months away.

**Deliverables:**

1. **The bet memo** — One page: a press release written as if the product had launched, a diagnosis in Rumelt's three parts, the FAQ with the riskiest assumptions first, an appetite, a north star that counts only completed stays, three guardrails, two kill criteria each written as a state and a date, the one-way and two-way doors marked, and a "left open" list.
2. **The discovery plan** — Six weeks with six design-partner hotels from one segment, one of them owned by the hostile chain, and one partner agency in a program of its own: the weekly interview rhythm, the opportunity solution tree's outcome, and the cheapest test of each riskiest assumption, including one Wizard-of-Oz transfer.
3. **The price and the terms** — The transfer fee, its split among agency, hotel and Stayover, any cap, the rules hotels may tighten, and the partner terms with their notice period; show one worked example in euros.
4. **The partner API sketch** — Job stories for the agencies, the operations they imply (including a validation-only check and a long-running reissue), and the webhook that tells an agency a transfer completed.
5. **The launch plan and its evaluation** — Cohorts by who may enter, each with entry and exit criteria; who is briefed before the first transfer; and an evaluation that does not rely on a guest-level A/B test, pre-registered, with what it cannot show stated plainly.
6. **The review template** — The questions the month-18 review will ask, a table that sets the memo's revisions side by side, and the place where decision and outcome are judged separately.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Diagnosis | Does the memo say where the harm comes from, and does every action follow from that sentence? |
| Measurability | Could someone who did not write the kill criteria tell, on the date, whether they had fired? |
| Fairness | Would the tout scenario the chain fears be stopped by a rule the platform enforces, whatever a partner promises? |
| Honest evaluation | Does the evaluation name its own assumptions, such as donors that are truly untreated, and what it cannot measure? |
| Doors | Are the hard-to-reverse commitments, such as the fee split and the partner terms, given more deliberation than the easy ones? |
| Coherence | Do the memo, the price, the API, the launch and the review describe one bet, so that the review could be written from the memo alone? |

#### Where you now stand

You can now follow a product decision through its whole life: diagnose a problem, write the bet down with an appetite, metrics and kill criteria, test the riskiest assumptions and set the price before design, turn the bet's promises into commitments engineering can test, launch it to one audience at a time with the conditions written in advance, judge it without a clean experiment when the market will not allow one, and review it honestly against what was written before anyone knew the outcome. That is the product half of the work. The other half is the engineering system that turns such a decision into running software across 40 teams, and its capstone, the Software book's Chapter 11, follows the same 18 months and the same resold ticket from the first test written against the oldest code in Encore to the scan at the door in Lyon.

### References

- Harry McCracken — [*How Gmail Happened: The Inside Story of Its Launch 10 Years Ago*](https://time.com/43263/gmail-10th-anniversary/). *TIME*, 2014 — free online.
- Colin Bryar, Bill Carr — *Working Backwards: Insights, Stories, and Secrets from Inside Amazon*. St. Martin's Press, 2021.
- Werner Vogels — [*Working Backwards*](https://www.allthingsdistributed.com/2006/11/working_backwards.html). All Things Distributed, 2006 — free online.
- David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich, Sinan Aral — [*Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb*](https://doi.org/10.1287/mnsc.2020.01157). *Management Science* 71(1), 2025.
- Alberto Abadie — [*Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects*](https://www.aeaweb.org/articles?id=10.1257/jel.20191450). *Journal of Economic Literature* 59(2), 2021.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*, ch. 27, "Reliable Product Launches at Scale"](https://sre.google/sre-book/reliable-product-launches/). O'Reilly, 2016 — free online.
- Gary Klein — [*Performing a Project Premortem*](https://hbr.org/2007/09/performing-a-project-premortem). *Harvard Business Review* 85(9), 2007.
- Annie Duke — *Quit: The Power of Knowing When to Walk Away*. Portfolio, 2022.
- Ryan Singer — [*Shape Up: Stop Running in Circles and Ship Work that Matters*](https://basecamp.com/shapeup). Basecamp, 2019 — free online.
- Baruch Fischhoff — [*Hindsight ≠ Foresight: The Effect of Outcome Knowledge on Judgment Under Uncertainty*](https://doi.org/10.1037/0096-1523.1.3.288). *Journal of Experimental Psychology: Human Perception and Performance* 1(3), 1975.
- Annie Duke — *Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts*. Portfolio, 2018.
- Teresa Torres — *Continuous Discovery Habits*. Product Talk, 2021.
- Frederick P. Brooks Jr. — *No Silver Bullet: Essence and Accidents of Software Engineering*. *IEEE Computer* 20(4), 1987 (first presented at IFIP, 1986).

---

## Appendix: Encore at a Glance {#encore-glance}

Throughout this book, Encore has been introduced the way a touring crew learns a new venue: one part at a time, as each part becomes relevant. The organizer console appears when a chapter needs a customer who sets rules, the fan app when a chapter needs software that cannot be recalled, and Rowmate when a chapter needs someone outside our walls who builds on what we publish. That arrangement serves a reader who goes from front to back, because every part arrives with its reason for existing. It serves much less well the reader who opens the book at Chapter 7, or who returns months later to look up one practice and finds that the example assumes things they never read or have since forgotten.

This appendix is for that reader. It gathers onto a few tables the company, its products and customers, the teams this book names, the facts of Verified Resale, the people who appear in its story and the kata companies, so that a single glance can answer the question "what was that again?" Each row points to the chapter where the fact matters, and some point further: to the Architecture book, where Encore's systems were designed, and to the Software book, which follows the same 18 months from the engineering side. A row compresses a chapter's reasoning into a line, and the compression is useful only because the full explanation sits one pointer away.

### The company

| Term | What it is | Where to read more |
|---|---|---|
| **Encore** | A company selling concert tickets across the EU, priced in euros, which also sells its platform to venues as software as a service (SaaS). Three facts shape everything: traffic rises 500× within minutes when a tour goes on sale, every seat must be sold exactly once, and bots arrive before the fans | [Architecture book, 1.1](https://oleksiyp.github.io/arch-book/#encore-our-running-example); Chapter 1 |
| **Size and history** | Nine engineers in one team in its first year; 70 engineers in nine teams three years later; 400 engineers by its seventh year, and about 400 since | Chapter 1 |
| **The present of this book** | The winter of Encore's ninth year, a few months after the Vesper Hale on-sale that the Operations book followed, to the summer of its tenth | Chapters 1 and 10 |
| **Organization** | 40 stream-aligned teams of about nine engineers each, plus a platform group of nine teams and 40 people. The Resale team, formed at month 4, makes a 41st | Chapter 1; the Software book, Chapter 9 |
| **Organizers** | About 900 active organizers, the promoters and festival companies whose events Encore sells; about 120 have their own finance staff | Chapter 1 |
| **Sale Gate** | Encore's admission controller for on-sales. Only tickets bought through it can be resold | [Architecture book, 2.4](https://oleksiyp.github.io/arch-book/#24-choosing-a-style); Chapters 1 and 2 |
| **Partner Listings** | The year-six arrangement that Verified Resale replaces: partners posted resale offers as links on sold-out event pages, the ticket changed hands outside Encore, and Encore checked nothing beyond the partner's word | Chapters 1 and 2 |
| **The Rowmate key leak** | The incident that left every partner authenticating with 15-minute tokens bound to a client certificate | The Resilience book, Section 7.2; Chapters 1 and 10 |
| **Rotating barcode** | Since the eighth year, the barcode in Encore's app is generated on the phone from a secret held for each ticket, so a screenshot stops working. "Barcode" is the trade word for the Architecture book's entry QR code | Chapters 1 and 8 |
| **Setlist** | Encore's design system of tokens, tenant themes and accessible components, owned by the Design System team of six engineers and three designers | Chapter 7 |
| **Fan app** | Native on iOS and Android (ADR-031), shipped on a weekly release train, with 14 feature modules and a shell; Resale became the 15th | Chapter 8 |
| **Organizer console** | A shell with six remotes loaded at runtime since the eighth year; the resale rules console is the seventh. The fan storefront remains a modular monolith | Chapter 7 |
| **The evidence before the bet** | In the 12 months before the memo, Support handled about 3,400 cases of dead or fake resold tickets, and more than 9,000 Vesper Hale tickets were on unofficial sites within a day of the on-sale | Chapters 2 and 10 |

*Figure A.1 — Encore, the company, as this book finds it.*

### Products and customers

| Product | Its customers | What it does for them | Where to read more |
|---|---|---|---|
| **Fan storefront and app** | Fans | Find events, buy tickets, carry them to the door, and now resell them | Chapters 1, 7 and 8 |
| **Organizer console** | Organizers | Set up events, set prices, watch sales, and set resale rules | Chapters 1, 6 and 7 |
| **Partner and public APIs** | Partners: venues, a festival app, and the resale partners Rowmate and Tessera | Read listings and availability, list and sell resale tickets, receive webhooks, at `api.encore.com` | [Architecture book, 7.3](https://oleksiyp.github.io/arch-book/#the-gateway-earns-its-place-at-the-edge); Chapter 9 |
| **Encore SaaS for venues** | More than 500 venues, in three tiers | Run a venue's own box office on Encore's platform | Chapters 1 and 5 |
| **Internal platform** | Encore's own teams | The golden path on which teams build and deploy | Chapter 1; the Software book, Chapter 6 |

*Figure A.2 — Four kinds of customer, each served by a product of its own, and a fifth product that serves Encore itself.*

### The teams this book names

| Team | Its part in Verified Resale | Where to read more |
|---|---|---|
| **Resale** | Formed at month 4 from Orders & Payments and Partner APIs. Owns the Resale service, the fan app's Resale module, the rules engine and the organizer rule assistant | Chapters 2, 6 and 10 |
| **Inventory** | Owns Seat Inventory & Ticketing, including barcode issuance; issues and revokes tickets on reissue | Chapters 1, 3 and 10 |
| **Venue Entry** | Door-scanning apps and devices, and the revocation lists that gates hold for offline validation | Chapters 3, 8 and 10 |
| **Orders & Payments** | The resale purchase saga | Chapters 1 and 10 |
| **Billing & Payouts** | Meters the fee split and pays organizers, partners and sellers | Chapters 5 and 10 |
| **Partner APIs** | The partner endpoints, sandbox, certification and webhooks | Chapters 9 and 10 |
| **Bot Screening** | Screens every resale buyer as it screens a primary buyer | Chapters 2 and 10 |
| **Organizer Console** | The console shell and the resale rules console | Chapters 6 and 7 |
| **Mobile App** | The app shell, the release train, the version floor and the wallet ticket view | Chapter 8 |
| **Fan Messaging** | Pass replacement and the "your ticket sold" message | Chapters 6, 8 and 10 |
| **Design System** | `VerifiedBadge`, `ReissueStatus` and the cap line in `PriceBreakdown` | Chapters 6 and 7 |
| **Security Engineering** | Partner credentials, in one quarter of collaboration with Resale | The Software book |
| **Other teams named** | Fan storefront: Fan Discovery, Seat Map, Checkout, Web Storefront, Fan Growth. Organizer console: Organizer Onboarding, Event Setup, Pricing & Presales, Festivals, Organizer Insights, Forecasting. APIs: Public API, Embeds & Channels. SaaS: Tenant Onboarding, Tenant Configuration, Box Office. Shared domains: On-Sale, Trust & Safety, Catalog, Support Experience, Experimentation. Platform: Reliability, Runtime, Developer Portal, Web & API Paths, Event Backbone, AI Platform | Chapters 1, 4, 5 and 7 |

*Figure A.3 — The twelve teams Verified Resale touches, and the others this book names. Forty teams in all; the Software book reads the same roster as code ownership.*

### Verified Resale

| Term | What it is | Where to read more |
|---|---|---|
| **The product** | Fans list tickets they bought through the Sale Gate. Another screened fan buys, and Encore **reissues** the ticket under a new ticket identity, revoking the seller's old barcode at every gate. Organizers set the rules and share the fee | Chapters 1 and 2 |
| **Partners** | **Rowmate**, the launch partner, certified at month 11, and **Tessera**, the second, certified about month 15 and live 11 days later. Partners are marketplaces where fans list tickets; none owns inventory, and Encore admits no professional resellers. Every listing enters one pool, visible in Encore's app and on every partner | Chapters 1, 9 and 10 |
| **Price cap** | Face value, meaning what the seller originally paid, primary fees included. Organizers may set a lower cap, never a higher one | Chapters 1 and 5 |
| **Fee and split** | Buyers pay a 10% fee on top of the resale price: 4 points to the partner through which the ticket was bought, 3 to the organizer and 3 to Encore. Bought in Encore's own app, Encore keeps the partner's 4 as well. A €60 ticket resold at €60 costs the buyer €66; the partner gets €2.40, the organizer €1.80, Encore €1.80 and the seller €60. On a designated Irish event the buyer pays €60 and the fee comes out of the seller's proceeds | Chapters 1, 2 and 5 |
| **Payout** | The seller is paid five days after the event, once the reissued ticket is beyond the reach of a dispute | Chapters 5 and 10 |
| **Organizer rules** | Tighten only: disable resale, set a lower cap, shorten the resale window, lower the per-fan limits. The default window runs from purchase until two hours before doors. The console offers three presets, "Standard", "Fan-first" and "Resale off"; in Ireland it offers no "Resale off", because the Sale of Tickets Act 2021 voids terms that block resale at or below face value | Chapters 5 and 6 |
| **Five fairness invariants** | 1. Partners never buy primary tickets. 2. Only tickets bought through the Gate, within the per-fan limit, can be listed. 3. Organizer caps and rules can only tighten. 4. Every resale buyer passes Bot Screening and the per-buyer limits. 5. Partners never see sales-velocity data. All five are tested on every build | Chapters 2 and 10; the Software book, Chapter 1 |
| **Organizer rule assistant** | The product's one AI feature. An organizer writes rules in plain language; the assistant drafts the typed rule set and a summary rendered from templates, and nothing applies until the organizer confirms. It can express only rules the type system allows | Chapter 6; the Software book, Chapter 3 |
| **North star and guardrails** | Verified resales completed per eligible event, counted only when the reissued ticket scans at the door. Guardrails include primary sell-through and the bot rate | Chapters 2 and 4 |
| **Kill criteria** | K1 (month 4): fewer than two of the first three organizers recruited commit a real event, or a voided pass still scans offline. K2 (month 18): fewer than 10 resales per eligible event, or primary sell-through more than 2 points below its synthetic control | Chapters 4 and 10 |
| **Design partners and pilot** | Six mid-size festival and tour promoters: three in France, two in Belgium, one in the Netherlands, one of them hostile to resale. A hand-run pilot at four shows in Lyon and Antwerp, about 11,200 tickets, completed 191 resales from 268 listings with no fan refused at the door | Chapter 3 |

*Figure A.4 — Verified Resale: the rules, the money and the measures.*

| Month | Season | What happened | Where to read more |
|---|---|---|---|
| 0 | Late winter, year 9 | The bet memo, with diagnosis, appetite (12 months to the first scan at a gate), north star, guardrails and kill criteria; the first tranche funds discovery | Chapters 2 and 10 |
| 0–4 | Spring, year 9 | Discovery: weekly interviews, six design partners, the four-show pilot, the pitch and first release slice | Chapter 3 |
| 4 | Late spring, year 9 | Decision to build; K1 passed; the Resale team forms; the first quarterly plan shows 23 dependencies across 12 teams; the organizer contract season becomes the high-integrity commitment | Chapters 2 and 10 |
| 9 | Autumn, year 9 | A walking skeleton runs end to end; the partner API is in sandbox and Rowmate is certifying; dependencies are down to 14 | Chapter 10; the Software book, Chapter 11 |
| 11 | — | Rowmate certified; the evaluation pre-registered | Chapter 10 |
| 12 | Winter, year 10 | Staged launch: three French organizers, Rowmate, France. The first resold ticket, €80 face value, is bought for €88 and scans at a Saturday concert in Lyon | Chapter 10 |
| About 13 | — | All consenting organizers in France | Chapter 10 |
| About 15 | — | Tessera live | Chapters 9 and 10 |
| 16 | — | Belgium live | Chapter 10 |
| 18 | Summer, year 10 | The review of the bet: a mean of 34 resales per eligible event across France against a month-18 target of 30 (median 11); primary sell-through down 0.4 points, within an interval from −1.3 to +0.5; 61% of eligible French organizers had enabled resale; an 8% fee was considered and declined. No kill criterion triggered | Chapter 10 |

*Figure A.5 — The bet's 18 months. The Software book reviews the engineering at month 24.*

### People named in this book

| Who | Role | Where to read more |
|---|---|---|
| **Amira** | Product manager of the resale trio, from Partner APIs, where she had inherited Partner Listings and its complaints | Chapters 1, 3 and 10 |
| **Paolo** | Designer of the resale trio, from Organizer Console | Chapters 1, 3 and 10 |
| **Katrin** | Tech lead of the resale trio, from Orders & Payments. Her wallet prototype showed that phones cannot be trusted to kill an old ticket and gates can | Chapters 1 and 3 |
| **Lena** | The last remaining author of the barcode core, written in Encore's first year, and the only person who fully understands it | Chapter 3; the Software book, Chapters 2 and 11 |
| *The proposers* | Encore's chief product officer and head of partnerships, who proposed Verified Resale after the Vesper Hale on-sale | Chapter 1 |
| *The hostile promoter* | A French arena-tour promoter among the design partners, opposed to resale, who became the heaviest user of the rules | Chapters 3 and 10 |
| *The first seller* | A fan in Lyon who could not go to a sold-out Saturday concert | Chapter 10 |

*Figure A.6 — The people of Verified Resale. Names in italics are roles; the book does not name them.*

### The kata companies

| Chapter | Kata | Company | The brief in a line |
|---|---|---|---|
| 1 | The Policy Factory | Haverlock Insurance | A home and motor insurer that delivered 31 of 34 projects while its outcomes fell |
| 2 | The Empty Court | Courtside | A three-sided court-booking marketplace whose coaches want to resell slots |
| 3 | The Empty Chair | Clinicly | Clinic scheduling software, with no-shows and a loud largest customer |
| 4 | Two Baskets, One Courier | Pantry | A grocery-delivery marketplace evaluating courier batching |
| 5 | The Seat and the Meter | Sumwise | Small-shop bookkeeping moving from seats to usage-based pricing |
| 6 | The Replacement Bus | Ploverwick | Regional transport ticketing whose AI trip assistant meets a disrupted line |
| 7 | The Departures Board | Wayfare | A travel marketplace with a stalled design system in 32 locales |
| 8 | Unlocking Underground | Pedal | Bike sharing whose app must unlock bikes with no signal |
| 9 | Sign Here | Tallyhouse | E-signature SaaS opening a partner API to law firms |
| 10 | The Second Night | Stayover | Hotel-booking SaaS weighing verified transfer of non-refundable bookings |

*Figure A.7 — Ten practice briefs, each a different company with its own scale and trouble. All are fictional.*
