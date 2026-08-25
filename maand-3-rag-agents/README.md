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

**A · RAG over ESP-documentatie** — [`projecten/esp-docs-rag/`](projecten/)

De Copernica- en Klaviyo-docs in een vector-DB, plus een vraag-antwoordlaag. Publieke bron,
direct nuttig, en hij draagt over klanten heen — precies het portabiliteitscriterium.

- [ ] Warming-up: 20 zinnen embedden en de drie meest vergelijkbare teruggeven, zodat de mechaniek klopt voordat de echte docs erin gaan
- [ ] Docs ingesten, chunken (~500 / overlap ~50), opslaan in Chroma met metadata (bron, ESP, sectie)
- [ ] Metadata-filtering: alleen Copernica, alleen Klaviyo, of allebei
- [ ] Reranking: breed ophalen, terugscoren naar de beste paar
- [ ] Antwoorden mét citaat naar de bronpagina. Zonder bron geen antwoord

**B · Evals op de evaluator uit maand 2** — [`projecten/evaluator-evals/`](projecten/)

**De belangrijkste build van het hele traject**, en degene die vrijwel niemand in
e-mailmarketing doet. Dit is het verschil tussen een claim en een getal.

- [ ] Testset van vijftig gelabelde subject lines. Eerst labelen, dan pas draaien
- [ ] Meet hoe vaak de prompt het goed heeft, per veld uit het schema
- [ ] Draai de vijf promptversies uit maand 2 tegen dezelfde set; nu weet je welke wint en met hoeveel
- [ ] Elke promptwijziging vanaf hier gaat langs deze set

**C · Journey-monitor** — [`projecten/journey-monitor/`](projecten/)

De generieke versie van het journey-overzicht dat ik nu wekelijks met de hand bijhoud. Landt hier
en niet eerder: pas met retrieval en evals eronder is het meer dan een while-loop met goede
bedoelingen. **Draait op dummy-data — geen klantdata in deze repo.**

- [ ] Een adapter per ESP met één vaste output: journey-ID, naam, status, doelgroep, laatst verzonden, prestatie week-op-week. Een tweede ESP erbij is dan een adapter, geen fork
- [ ] Detector 1 — **stuk**: deterministisch. Verzending niet uitgevoerd, journey vuurt niet meer, aantallen op nul, lege feed. Hier hoort geen drempel bij, alleen een controle
- [ ] Detector 2 — **minder**: statistisch. Daling boven een drempel, met een minimumvolume en een voortschrijdend gemiddelde over vier weken. Zonder die twee meld je ruis
- [ ] Die twee niet door elkaar halen. Het is de klassieke fout in alerting: één drempel over beide, waarna je óf storingen mist óf stakeholders leert je meldingen te negeren
- [ ] From scratch, geen framework, eigen loop. **Doe dit vóór je LangGraph aanraakt**
- [ ] Een falende tool-call laat de loop niet hangen en niet stil crashen

## Posts deze maand

Volledige kalender met voorwaarden en bewijs: [tabblad Posts in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/#posts).

**Week 9 (24 – 30 sep) · "Er staan journeys live die niemand meer kan benoemen"**
Het patroon, niet de klant. **Voorwaarde: de nulmeting vastgelegd én het publicatiegesprek gevoerd**
(aangevraagd in week 5). Bewijs: het aantal live journeys dat niemand kon benoemen, relatief
gebracht. Geen omzet, geen merknaam, geen sector — sector plus aantal merken maakt de klant in
Nederland herkenbaar, ook zonder naam.

**Week 12 (15 – 21 okt) · "Tegen vijftig gelabelde voorbeelden was het 68 procent"**
Het verschil tussen een claim en een getal. **Voorwaarde: build B af.** De sterkste post van het
traject en de enige die niemand kan verzinnen, dus wachten tot het getal er echt is. Bewijs: n=50,
score per veld, plus het verschil tussen de vijf promptversies uit maand 2. Volledig eigen data.

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
