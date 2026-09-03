# Maand 2: Bouwen met LLM-API's

**27 augustus – 23 september 2026**

**Doel:** echte AI-features bouwen met model-API's. Dit is de kern van het vak. Diepte hier
betaalt zich meer terug dan diepte waar dan ook in het traject.

Volledige uitwerking: [tabblad Roadmap in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/) · [ROADMAP.md](../ROADMAP.md)

## Skills

Prompting · structured outputs · tool calling · streaming.

**In welke week wat.** De skills staan in het dashboard op uitvoeringsvolgorde, niet op
leerboekvolgorde, met per blok een weeklabel:

| Week | Blok | Build |
|---|---|---|
| 6 | Deterministisch of model | BUILD C, deterministische helft |
| 7 | Structured outputs · Prompting ronde 1 · Kosten en tokens | BUILD C, de oordeelstap |
| 8 | Prompting ronde 2 · Failure handling · Prompt injection | BUILD A, de checker |

**Tool calling en conversation state halen deze maand niet**, en dat is een keuze en geen
vergissing: er zijn nog drie weken en er staat nog geen regel code van deze maand. Ze zijn niet
geschrapt maar verplaatst — tool calling landt in maand 3 op de vraag-antwoordlaag van het
corpus, conversation state in maand 4 op de voordeur. Streaming leer je hier en pas je daar toe.
Dat betekent dat BUILD B (briefing naar campagnedocument) deze maand niet gebouwd wordt.

## Resources

- Prompting: `anthropics/prompt-eng-interactive-tutorial` (GitHub), daarna de officiële prompt-docs van Anthropic en OpenAI
- Structured outputs: **Instructor** + Pydantic, met de officiële structured-output docs
- Tool calling: OpenAI function calling guide + Anthropic tool use docs, náást elkaar
- Streaming: officiële streaming-docs + Simon Willison's uitleg
- Retries: **Tenacity**
- Security: OWASP-guide over prompt injection

## Gereedschap

[Prompt 2: Structured Data Extraction](../prompts/02-structured-data-extraction.md)

## Builds

Drie builds, in deze volgorde. C staat voor A omdat het schemapatroon dat je in C één keer
bouwt, in A opnieuw gebruikt wordt: één skill, twee toepassingen.

**C · Authenticatie-scan** — [`projecten/authenticatie-scan/`](projecten/authenticatie-scan/)

SPF-, DKIM- en DMARC-records van de webshops uit de corpuslijst opvragen, parsen en tellen.
Publieke DNS-data, geen klantdata, geen toestemming nodig.

- [ ] Domeinen inlezen, records opvragen, fouten afvangen (geen domein, geen record, time-out)
- [ ] Policy parsen en tellen per categorie — **deterministisch, hier hoort geen model bij**
- [ ] Pas daarna: per domein een risico-oordeel in vaste vorm, mét schema. Dít is het structured-outputs-blok
- [ ] De domeinlijst is dezelfde lijst als bij het corpus. Schrijf hem weg tijdens het aanmelden

De grens tussen tellen en oordelen is het punt van deze build, en het is dezelfde les die
de signaalsplitser in maand 3 nog een keer geeft.

**A · Subject line- en preheader-checker** — [`projecten/subject-checker/`](projecten/subject-checker/)

Van weergave-check naar classificatie. Niet hoe de regel eruitkomt in Gmail (dat doet elke
ESP-preview al), maar wát er beloofd wordt:

- [ ] `belofte` — korting, nieuw assortiment, urgentie, redactioneel, service
- [ ] `preheader_relatie` — herhaalt, vult aan, of staat los
- [ ] `belofte_ingelost` — komt de belofte terug in de body
- [ ] `merkstem` — blijft een **parameter** voor context, geen score. Een cijfer op stijl is niet toetsbaar, dus er kan later geen eval tegenaan

Elk veld is zo gekozen dat een mens er onafhankelijk een label bij kan zetten. Dat is de
voorwaarde voor de evals in maand 3. Geen spamwoordscore: die lijsten zijn achterhaald, en het
stuk dat moderne filters wél bekijken meet build C.

Draait op publieke nieuwsbrieven en regels die ik zelf verzin. **Geen klantdata.**

**B · Briefing naar campagnedocument** — [`projecten/briefing-naar-campagnedocument/`](projecten/)

De tool-calling-opdracht. Een input-briefing eruit, mijn vaste documentstructuur erin.

- [ ] Tools die de briefing uitlezen en per sectie van de documentstructuur invullen
- [ ] Ontbrekende velden worden benoemd, niet verzonnen
- [ ] Het model besluit; mijn code voert uit

**Blijft intern.** Deze build verschijnt niet als publieke repo: de documentstructuur is
werkgevers-IP. Daarmee telt hij niet mee als extern bewijs — als er één build moet schuiven
omdat de maand te vol wordt, is het deze.

## De skills zonder eigen project

Deze drie builds dragen álle skills van deze maand:

- **Prompting** → vijf genummerde promptversies van de checker: v1 kaal, v2 specifiek, v3 chain-of-thought, v4 few-shot, v5 de combinatie. Ze staan als aanvinkbare stappen in [`projecten/subject-checker/`](projecten/subject-checker/) en de bestanden horen in `prompts/v1.txt` t/m `v5.txt`. De vijf few-shot-voorbeelden gaan apart in `few-shot.jsonl` en mogen nooit in de eval-set van maand 3.
- **Structured outputs** → eerst op de records uit build C, daarna op de subject lines in build A.
- **Streaming** → skill hier, toepassing in maand 4. De checker streamt níét: hij geeft een klein object terug en draait als batch over het corpus. Streamen is pas zinnig bij de voordeur, waar een mens zit te wachten.
- **Conversation state** → de briefing-tool vraagt door bij een onvolledige briefing en houdt de history zelf bij.
- **Failure handling** → Tenacity op alle drie. Concreet: de batchrun over duizend mails mag niet stoppen bij mail 400, en een mail die drie keer faalt wordt overgeslagen én gelogd, niet stilgeslikt.
- **Kosten** → reken uit wat de hele batchrun kost vóór je op enter drukt, schrijf het getal op, en vergelijk met de rekening.
- **Prompt injection** → geen theorie hier: je voert marketingmails van derden aan een model. Zet in een testmail een regel die de checker opdraagt alles 'redactioneel' te noemen en kijk of je schema hem tegenhoudt.

## Posts deze maand

Twee, allebei met een build of een eigen waarneming eronder. Volledige kalender:
[tabblad Posts in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/#posts).

**Week 7 (10 – 16 sep) · "Wat levert een journey eigenlijk op?"**
De drie losse journey-posts uit de oude kalender zijn hier één post geworden: ze putten alle
drie uit hetzelfde klantproject en samen tonen ze geen regel code. Neem het GA4-sampling-verhaal
als kern — acht maanden opgevraagd, 4% teruggekregen, geen foutmelding — plus de naamgeving die
nergens uit af te leiden is. **Voorwaarde: geen.** Bewijs: eigen waarneming, geen klantcijfer.
Geen merknaam, geen sector, geen aantallen over de klant. Sluit af met wat je nu bouwt, dan doet
hij ook positioneringswerk.

**Week 8 (17 – 23 sep) · "Ik heb de DMARC-records van N Nederlandse webshops opgevraagd"**
**Voorwaarde: build C draait en de lijst is geteld.** Bewijs: het werkelijke aantal domeinen, de
verdeling over `geen` / `p=none` / `quarantine` / `reject`, en de datum van meten. De `N` in de
titel vul je pas in als je hem gemeten hebt. Publieke DNS-data, dus geen toestemming.

*De post "honderd subject lines en waar de checker faalt" is vervallen als losse post: het
corpus begon later dan gepland en heeft in week 8 nog te weinig volume voor die claim. De
faalgevallen komen terug in de eval-post van week 12, waar ze sterker staan omdat er dan
labels tegenover staan.*

## Milestone

- [ ] Prompts die betrouwbare output geven voor een gegeven taak
- [ ] Gestructureerde JSON uit een model met Pydantic en Instructor
- [ ] Tool calling waarmee een model jouw Python-functies draait
- [ ] Een antwoord realtime streamen
- [ ] Multi-turn gespreksgeschiedenis beheren
- [ ] Tokenkosten inschatten vóór verzending
- [ ] API-fouten en slechte output afhandelen zonder crash
- [ ] Uitleggen wat prompt injection is
