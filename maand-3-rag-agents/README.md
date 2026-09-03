# Maand 3: RAG en agents

**24 september – 21 oktober 2026**

**Doel:** één solide retrieval-systeem en één solide agent bouwen, begrijpen waarom elk
onderdeel er zit, en ze kunnen debuggen als ze breken. Dat is de lat.

Volledige uitwerking: [tabblad Roadmap in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/) · [ROADMAP.md](../ROADMAP.md)

## Skills

RAG · vector-DB's · agents · evals.

## Resources

- Embeddings: Stack Overflow "intuitive introduction to text embeddings" + OpenAI embeddings guide
- Chunking: LangChain `RecursiveCharacterTextSplitter` (size ~500, overlap ~50)
- Vector-DB: **Chroma**, lokaal · https://docs.trychroma.com
- Reranking: Cohere reranking-docs
- RAG-framework: **LlamaIndex**
- Agents: Anthropic **"Building Effective Agents"**, lezen vóór je één regel agent-code schrijft, daarna LangGraph
- Evals: **DeepEval** algemeen, **Ragas** voor RAG

## Gereedschap

[Prompt 3: Grounded RAG Answering](../prompts/03-grounded-rag-answering.md)

## Twee dingen om te onthouden

- **De meeste RAG-fouten zijn retrieval-fouten, geen modelfouten.** Kijk altijd eerst wat er opgehaald werd voordat je het model de schuld geeft.
- **Een agent is een while-loop met een model dat de vertakkingen kiest.** Eén call als het in één prompt past · een vaste workflow als de stappen voorspelbaar zijn · een agent alleen als het aantal stappen echt onvoorspelbaar is.

## Builds

**A · Corpus van Nederlandse B2C-nieuwsbrieven** — [`projecten/nieuwsbrief-corpus/`](projecten/nieuwsbrief-corpus/)

Eén apart e-mailadres, 40 tot 60 Nederlandse webshops, vanaf week 5 verzamelen. Levert dezelfde
skills als een RAG over documentatie (chunken, embedden, metadata-filtering, retrieval,
reranking), maar produceert een bevinding in plaats van een vraagbaak. Publieke bron, eigen data,
geen klantdata, geen toestemming nodig.

- [ ] Warming-up: 20 zinnen embedden en de drie meest vergelijkbare teruggeven, zodat de mechaniek klopt voordat de echte mails erin gaan
- [ ] Binnenhalen via IMAP; HTML parsen naar platte tekst, met subject en preheader apart
- [ ] Chunken (~500 / overlap ~50), opslaan in Chroma met metadata per merk, datum, type (promo, transactioneel, redactioneel) en sector
- [ ] Metadata-filtering: op merk, op periode, op type
- [ ] Reranking: breed ophalen, terugscoren naar de beste paar
- [ ] Clusteren en doorzoeken

**De val zit in de doorlooptijd, niet in de techniek.** Het corpus moet in week 5 gaan
verzamelen. Zonder aanmelden geen build.

**B · Evals op de checker uit maand 2** — [`projecten/evaluator-evals/`](projecten/)

**De belangrijkste build van het hele traject**, en degene die vrijwel niemand in
e-mailmarketing doet. Dit is het verschil tussen een claim en een getal.

- [ ] Testset van vijftig gelabelde subject lines, getrokken uit het corpus uit build A in plaats van zelf verzonnen. Eerst labelen, dan pas draaien
- [ ] Meet hoe vaak de prompt het goed heeft, per veld uit het schema
- [ ] Draai de vijf promptversies uit maand 2 tegen dezelfde set; nu weet je welke wint en met hoeveel
- [ ] Elke promptwijziging vanaf hier gaat langs deze set

**C · Signaalsplitser** — [`projecten/signaalsplitser/`](projecten/)

Een detector die twee soorten signalen strikt gescheiden houdt, op synthetische tijdreeksen
**zonder ESP-koppeling**. Landt hier en niet eerder: pas met retrieval en evals eronder is het
meer dan een while-loop met goede bedoelingen.

- [ ] Detector 1 — **stuk**: deterministisch. Geen verzending uitgevoerd, aantallen op nul, lege feed. Hier hoort geen drempel bij, alleen een controle
- [ ] Detector 2 — **minder**: statistisch. Daling boven een drempel, met een minimumvolume en een voortschrijdend gemiddelde over vier weken. Zonder die twee meld je ruis
- [ ] Die twee niet door elkaar halen. Het is de klassieke fout in alerting: één drempel over beide, waarna je óf storingen mist óf stakeholders leert je meldingen te negeren
- [ ] From scratch, geen framework, eigen loop. **Doe dit vóór je LangGraph aanraakt**
- [ ] Een falende tool-call laat de loop niet hangen en niet stil crashen

De ESP-adapters en het journey-overzicht horen hier niet in: Funnelboost bouwt zelf alerting, dus
die kant blijft intern.

## Posts deze maand

Volledige kalender met voorwaarden en bewijs: [tabblad Posts in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/#posts).

**Week 9 (24 – 30 sep) · "Er staan journeys live die niemand meer kan benoemen"**
Het patroon, niet de klant. **Voorwaarde: de nulmeting vastgelegd én het publicatiegesprek gevoerd**
(aangevraagd in week 5). Bewijs: het aantal live journeys dat niemand kon benoemen, relatief
gebracht. Geen omzet, geen merknaam, geen sector — sector plus aantal merken maakt de klant in
Nederland herkenbaar, ook zonder naam.

**Week 10–11 · "Wat duizend Nederlandse nieuwsbrieven laten zien als je ze door embeddings haalt"**
De clustering, welke patronen eruit vallen en wat dat zegt over hoe Nederlandse webshops hun
e-mail inrichten. **Voorwaarde: build A af én het corpus groot genoeg.** Geen post zonder n.
Bewijs: het werkelijke aantal mails en merken, de clusterverdeling en de periode waarover
verzameld is.

**Week 12 (15 – 21 okt) · "Tegen vijftig gelabelde voorbeelden bleek het iets anders"**
Het verschil tussen een claim en een getal. **Voorwaarde: build B af.** De sterkste post van het
traject en de enige die niemand kan verzinnen, dus wachten tot het getal er echt is. Bewijs:
vijftig gelabelde regels uit het corpus, score per veld, plus het verschil tussen de vijf
promptversies uit maand 2. Het percentage in de titel vul je pas in als je het gemeten hebt.

## Milestone

- [ ] Uitleggen wat een embedding is en waarom vergelijkbare tekst vergelijkbare vectoren geeft
- [ ] Een document zinnig chunken
- [ ] Embeddings opslaan en queryen met metadata-filtering
- [ ] Reranking toevoegen
- [ ] Een retrieval-fout debuggen
- [ ] Complete RAG-pipeline met gegronde, geciteerde antwoorden
- [ ] Agent-loop from scratch
- [ ] Correct kiezen tussen call, workflow en agent
- [ ] Een eval-set draaien en er een getal uit halen
