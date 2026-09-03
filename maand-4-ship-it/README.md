# Maand 4 — Shippen

**22 oktober – 18 november 2026**

**Doel:** de twee beste builds uit maand 2 en 3 draaibaar maken voor iemand anders.
Weinig nieuwe concepten, veel doen.

Volledige uitwerking: [tabblad Roadmap in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/) · [ROADMAP.md](../ROADMAP.md)

## Resources

- **Docker** getting-started guide (packaging)
- **Langfuse** (tracing: prompt, response, tokenkosten, latency)
- Kostenbeheersing: harde spending limits · caching · rate limiting · goedkopere modellen waar die volstaan

## De opdracht

**Zet een voordeur op het corpus.** Iemand plakt een subject line of stuurt zijn eigen
nieuwsbrief door, en krijgt terug hoe die zich verhoudt tot wat de Nederlandse webshops in het
corpus doen. Dat is de milestone van deze maand letterlijk — draaibaar voor iemand anders, een
demo zonder installatie — en het hergebruikt alles wat er in maand 2 en 3 al staat: de
IMAP-inname, de checker, de corpusbenchmark.

Dit is ook het enige artefact van het hele traject dat een e-commerce owner zelf opent. Alle
andere builds zijn voor de uitvoerder of voor jezelf.

- [ ] Gedeployed, met harde spending limits, caching en rate limiting
- [ ] Basis-tracing met Langfuse
- [ ] Een README waarmee iemand anders het aan de praat krijgt zonder mij
- [ ] Een demo die het laat zien zonder dat iemand het hoeft te installeren

**Wordt de mail-inname te veel, dan wordt het een plakveld.** Lager dan dat ga je niet: er moet
iets zijn dat een ander kan openen. Naast deze build maak je de authenticatie-scan uit maand 2
publiek draaibaar; die is klein en af te maken naast het bovenstaande.

## README-structuur voor elk portfolioproject

1. Welk probleem het project oplost
2. Wie het zou gebruiken
3. Welke aanpak je koos en waarom
4. **Wat er misging en wat je leerde** ← de sectie die bijna niemand schrijft
5. Hoe je het draait

## Posts deze maand

Eén, volledige kalender in het [tabblad Posts](https://dvo-ai-automation.github.io/ai-engineer-for-email/#posts).

**Week 15–16 · "Ik heb er een voordeur op gezet, en dit ging er stuk"**
De tool live, plus wat er misging toen er iemand anders dan ik op klikte. **Voorwaarde: het
ding draait publiek en er is minstens één keer iets stukgegaan dat je kunt beschrijven.** Bewijs:
de link, en de faalgevallen met wat je eraan veranderd hebt. Geen lanceerpost zonder die tweede
helft — dat is precies de sectie die bijna niemand schrijft.

## Richting kiezen (één)

- [ ] **AI product engineer** — direct waarde leveren bij een klant
- [ ] **Applied ML** — fine-tuning, Ollama, inference-optimalisatie
- [ ] **AI automation** — n8n + LangGraph, bedrijfsworkflows zoals lead-qualification

## Milestone

- [ ] Twee gedeployde projecten met echte kostenbeheersing, elk met een eerlijke README
- [ ] Een demo per project
- [ ] Een heldere one-liner over wat je bouwt
- [ ] Een zichtbaar spoor van werk in het openbaar
- [ ] Een gekozen richting
