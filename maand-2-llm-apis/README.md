# Maand 2: Bouwen met LLM-API's

**27 augustus – 23 september 2026**

**Doel:** echte AI-features bouwen met model-API's. Dit is de kern van het vak. Diepte hier
betaalt zich meer terug dan diepte waar dan ook in het traject.

Volledige uitwerking: [tabblad Roadmap in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/) · [ROADMAP.md](../ROADMAP.md)

## Skills

Prompting · structured outputs · tool calling · streaming.

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

**A · Subject line- en preheader-checker** — [`projecten/subject-checker/`](projecten/subject-checker/)

De structured-outputs-opdracht, maar dan in mijn eigen vak. Claude API met een JSON-schema als
output, gericht op wat objectief te controleren is. Per subject line + preheader terug:

- [ ] `weergave` — hoe de regel eruitkomt per client (Gmail, Outlook, Apple Mail, mobiel), met het afkappunt in tekens én pixels
- [ ] `preheader` — lengte, en of de eerste regel body de preheader opeet
- [ ] `emoji` — rendering en fallback per platform
- [ ] `merkstem` — blijft een **parameter** voor context, geen score. Een cijfer op stijl is niet toetsbaar, dus er kan later geen eval tegenaan

Geen spamwoordscore: spamwoordenlijsten zijn achterhaald, moderne filters kijken naar reputatie,
engagement en authenticatie. Elke uitspraak van deze tool moet in maand 3 tegen een gelabelde set
te houden zijn.

Draait op publieke nieuwsbrieven en regels die ik zelf verzin. **Geen klantdata.**

**B · Briefing naar campagnedocument** — [`projecten/briefing-naar-campagnedocument/`](projecten/)

De tool-calling-opdracht. Een input-briefing eruit, mijn vaste documentstructuur erin. Dit raakt
werk dat ik nu handmatig doe, dus de kwaliteitslat is die van mijn eigen output.

- [ ] Tools die de briefing uitlezen en per sectie van de documentstructuur invullen
- [ ] Ontbrekende velden worden benoemd, niet verzonnen
- [ ] Het model besluit; mijn code voert uit

**Blijft intern.** Deze build verschijnt niet als publieke repo: de documentstructuur is
werkgevers-IP.

## De skills zonder eigen project

Deze twee builds dragen álle skills van deze maand. Wat vroeger een los oefenprojectje was,
zit nu erin:

- **Prompting** → vijf promptversies van de checker, alle vijf gedraaid, outputs naast elkaar. Bewaren: dit is de nulmeting voor de evals in maand 3.
- **Streaming** → de checker streamt zijn oordeel terwijl het binnenkomt.
- **Conversation state** → de briefing-tool vraagt door bij een onvolledige briefing en houdt de history zelf bij.
- **Failure handling** → Tenacity op beide, en een onverwacht antwoord sloopt nooit de run.

## Posts deze maand

Volledige kalender met voorwaarden en bewijs: [tabblad Posts in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/#posts).

**Week 5 (27 aug – 2 sep) · "Waarom het omzetgetal in je journey-dashboard te laag staat"**
Consent Mode, thresholding en het attributievenster. **Voorwaarde: geen.** Deze vraagt geen build
en geen afgeronde maand, dus hij kan als eerste. Bewijs is het mechanisme, niet een n.

*Regel deze week de toestemming aan die je later nodig hebt: de klant, voor de post in week 9.
Vraag hem nu, niet in de week van publicatie. Ook deze week starten: het [nieuwsbrief-corpus](../maand-3-rag-agents/projecten/nieuwsbrief-corpus/)
— aanmelden bij 40 tot 60 webshops, anders is er in maand 3 te weinig volume.*

**Week 8 (17 – 23 sep) · "Honderd subject lines, en waar mijn checker structureel faalt"**
Niet de demo, de faalgevallen. **Voorwaarde: build A af én honderd echte subject lines uit het
corpus erdoorheen.** Zonder die honderd heb je een mening in plaats van een bevinding. Bewijs:
het aantal doorgemeten regels en uit hoeveel merken ze komen, het schema, de promptversie en de
faalcategorieën met aantallen.

## Milestone

- [ ] Prompts die betrouwbare output geven voor een gegeven taak
- [ ] Gestructureerde JSON uit een model met Pydantic en Instructor
- [ ] Tool calling waarmee een model jouw Python-functies draait
- [ ] Een antwoord realtime streamen
- [ ] Multi-turn gespreksgeschiedenis beheren
- [ ] Tokenkosten inschatten vóór verzending
- [ ] API-fouten en slechte output afhandelen zonder crash
- [ ] Uitleggen wat prompt injection is
