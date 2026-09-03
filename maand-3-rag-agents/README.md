# Maand 3: RAG en agents

**24 september – 21 oktober 2026**

**Doel:** één solide retrieval-systeem en één solide agent bouwen, begrijpen waarom elk
onderdeel er zit, en ze kunnen debuggen als ze breken. Dat is de lat.

Volledige uitwerking: [tabblad Roadmap in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/) · [ROADMAP.md](../ROADMAP.md)

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
- [ ] **Bouw het binnenhalen als iets dat draait zonder dat jij kijkt**: idempotent op `Message-ID`, hervatbaar na een afgebroken run, en het meldt het als er zeven dagen niets binnenkwam. Dit is het enige stuk "onbewaakt draaien" dat in dit traject past zonder extra build
- [ ] Binnenhalen via IMAP; HTML parsen naar platte tekst, met subject en preheader apart
- [ ] Chunken (~500 / overlap ~50), opslaan in Chroma met metadata per merk, datum, type (promo, transactioneel, redactioneel) en sector
- [ ] Metadata-filtering: op merk, op periode, op type
- [ ] Reranking: breed ophalen, terugscoren naar de beste paar
- [ ] **Analyse 1 · e-maildruk**: groeperen op merk en datum en tellen. Geen model nodig, en het is de opening van de post van week 10–11
- [ ] **Analyse 2 · lifecycle**: wat 50 webshops sturen in je eerste dertig dagen. Alleen het moment dat je toch al observeert
- [ ] **Analyse 3 · clustering**: welke groepen vallen er vanzelf uit, en welke had je niet verwacht
- [ ] **Vraag-antwoordlaag met citaties**: een antwoord mét de mails eronder waar het uit blijkt. Hier landen grounding en reranking, en hier haal je elke bewering uit je post doorheen vóór je hem plaatst
- [ ] Merken normaliseren vóór je gaat tellen: één webshop mailt vanaf drie afzenderadressen. Dit is je eerste echte stukje datamodellering

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

Twee, allebei met een gemeten getal eronder. Volledige kalender:
[tabblad Posts in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/#posts).

**Week 10–11 · "Wat duizend Nederlandse nieuwsbrieven laten zien als je ze door embeddings haalt"**
De clustering, welke patronen eruit vallen en wat dat zegt over hoe Nederlandse webshops hun
e-mail inrichten. Ook de clusters die je niet had verwacht en de clusters die niets bleken te
betekenen. **Voorwaarde: build A af én het corpus groot genoeg.** Geen post zonder n; is er te
weinig volume, dan schuift de post op in plaats van dat je de conclusie oprekt. Bewijs: het
werkelijke aantal mails en merken, de clusterverdeling en de periode waarover verzameld is.

**Week 12 (15 – 21 okt) · "Hoe weet je of de AI die je subject lines schrijft het goed heeft?"**
Zelfde build als altijd, andere ingang. De oude titel ("mijn prompt had het naar eigen zeggen
altijd goed") praat tegen engineers; deze praat tegen iemand die net zijn copy door een model is
gaan halen en niemand heeft die kan zeggen hoe vaak dat ding ernaast zit. **Voorwaarde: build B
af.** Bewijs: vijftig gelabelde regels uit het corpus, hoe je ze getrokken hebt en uit hoeveel
merken, de score per veld, en het verschil tussen de vijf promptversies uit maand 2. Hier landen
ook de faalgevallen van de checker, die eerder een eigen post in week 8 waren.

*De signaalsplitser levert deze maand geen post op. Op synthetische data is het een
ontwerpverhaal, en de eerste reactie is "op welke data dan?". Bouwen wel — hij leert je de
agent-loop from scratch — publiceren pas als hij ooit op echt volume draait.*

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
