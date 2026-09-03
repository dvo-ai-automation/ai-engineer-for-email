# Roadmap: vier maanden de programmeerkant eronder

Ik bouw al twee jaar AI- en automationoplossingen voor e-mailmarketing. Deze roadmap gaat over
de laag daaronder: zelf kunnen bouwen, repareren en meten wat ik nu samenstel.

- **Start:** donderdag 30 juli 2026
- **Einde:** woensdag 18 november 2026 (16 weken)
- **Tempo:** 15–25 uur per week.

| Maand | Periode | Thema |
|---|---|---|
| 1 | 30 jul – 26 aug | Python en de plumbing |
| 2 | 27 aug – 23 sep | Bouwen met LLM-API's |
| 3 | 24 sep – 21 okt | RAG en agents |
| 4 | 22 okt – 18 nov | Shippen |

> ### 📊 [De volledige uitwerking staat in het dashboard →](https://dvo-ai-automation.github.io/ai-engineer-for-email/)
>
> Per maand: alle skills met hun gekozen resource, de bouwopdrachten, de valkuilen, de
> mijlpalen en de actuele voortgang. Dit bestand houdt alleen nog vast wat vaststaat;
> het dashboard houdt bij waar je staat.

---

## De doelstelling in één zin

> Als je een LLM betrouwbaar een specifieke taak kunt laten doen binnen een app, én je begrijpt genoeg om het te repareren als het stukgaat, dan ben je een AI engineer.

Je bouwt producten bovenop bestaande modellen. Geen calculus, geen backpropagation, geen
transformer-internals. Dat is een ander vak (research scientist).

Wat dit traject mij oplevert is diepte, geen inzetbaarheid: die is er al. Het verschil dat ik
zoek is dat ik straks een getal kan laten zien waar ik nu een claim heb.

---

## De twee regels waar alles op rust

1. **De 30-minutenregel**: per uur kijken of lezen minstens 30 minuten bouwen zónder tutorial
   open. Typ de voorbeelden zelf. Maak ze kapot. De errors zijn het leren.
2. **Alles gaat publiek**: elk project op GitHub op de dag dat je het af hebt, ook de lelijke.

---

## De 4 fouten (lees dit elke maandag opnieuw)

Deze fouten beëindigen dit soort trajecten in week 2, niet in maand 3.

**1. Beginnen met theorie en wiskunde.**
Fix: overslaan. Je pikt de concepten op als je ze in een echt project tegenkomt, en dán blijven ze hangen.

**2. Tutorials kijken in plaats van bouwen.**
Fix: de 30-minutenregel hierboven.

**3. Tools leren in plaats van skills.**
Fix: leer de skill ónder de tool. Een betrouwbare prompt schrijven verloopt niet als een framework update. Deze roadmap is daarom per skill georganiseerd, niet per tool.

**4. Wachten tot je je klaar voelt om in het openbaar te bouwen.**
Fix: begin in maand 1. Niemand kijkt zo aandachtig mee dat je vroege werk je in verlegenheid brengt.

**Wat je al meebrengt:** in AI-werk telt oordeelsvermogen, communicatie en het kunnen
bezitten van een uitkomst zwaarder dan het aantal frameworks dat je kent. Dat is precies wat
je uit je huidige werk meeneemt en niet opnieuw hoeft te leren. Houd dit vier maanden lang in
je achterzak.

---

## Wat ik in maand 2 t/m 4 bouw

*Eigen invulling, geen onderdeel van het bronartikel. De volledige postkalender met voorwaarden,
benodigd bewijs en toestemmingen staat in het [tabblad Posts](https://dvo-ai-automation.github.io/ai-engineer-for-email/#posts). De structuur van de roadmap (de skills per
maand, de twee regels, de vier valkuilen) blijft staan; de projecten zijn vervangen door builds
uit mijn eigen vak, zodat elke build ook zonder deze roadmap nut houdt.*

**Maand 2 · LLM-API's** — [details](maand-2-llm-apis/README.md)

- **A. Subject line- en preheader-checker.** Claude API met een JSON-schema als output, gericht op wat objectief te controleren is: weergave per client met het afkappunt, preheader-lengte, en emoji-rendering per platform. Merkstem is een parameter voor context, geen score. Publieke nieuwsbrieven en zelfverzonnen regels, geen klantdata.
- **B. Briefing naar campagnedocument.** Tool calling: een input-briefing eruit, mijn vaste documentstructuur erin. Blijft intern; de documentstructuur is werkgevers-IP.
- **Post:** subject lines uit het corpus door de checker, en waar hij er structureel naast zit. De faalgevallen, niet de demo.

**Maand 3 · RAG en agents** — [details](maand-3-rag-agents/README.md)

- **A. Corpus van Nederlandse B2C-nieuwsbrieven.** Eén apart e-mailadres, 40 tot 60 webshops, vanaf week 5 verzamelen. IMAP binnenhalen, HTML naar platte tekst, embeddings, vector-DB met metadata per merk, datum, type en sector. Dezelfde skills als een docs-RAG, maar het levert een bevinding op in plaats van een vraagbaak.
- **B. Evals op de checker uit maand 2.** Vijftig gelabelde subject lines, getrokken uit het corpus, en meten hoe vaak de prompt het goed heeft. De belangrijkste build.
- **C. Signaalsplitser.** Een detector die twee soorten signalen strikt gescheiden houdt op synthetische tijdreeksen: stuk is deterministisch, minder is statistisch met drempel, minimumvolume en een voortschrijdend gemiddelde. From scratch, zonder ESP-koppeling.
- **Posts:** week 9 het journey-patroon (na de nulmeting en het publicatiegesprek) · week 10–11 wat het corpus laat zien · week 12 de evals, met het getal erbij.

**Maand 4 · Shippen** — [details](maand-4-ship-it/README.md)

- De twee beste builds draaibaar maken voor iemand anders: deployment, README, demo.
- **Post:** week 13–14 het alerting-ontwerp, "stuk" versus "minder".

---

## Verdiepen: begrippen die deze roadmap niet uitlegt

*Bijgehouden sinds 14 aug 2026, laatst bijgewerkt 3 sep 2026, op basis van de vragen die tijdens het bouwen opkwamen. De
roadmap noemt deze termen als bullet point alsof je ze al kent; voor een beginner zijn het
gaten. Deze lijst staat bewust hier en niet in het dashboard: het zijn jouw open vragen,
geen onderdeel van het oorspronkelijke plan.*

- [x] **Environment variable**: uitgelegd 14 aug, in de praktijk gebruikt 16 aug. Een waarde
      die búiten je programma leeft en die je code opvraagt in plaats van bevat. Bestaat zodat
      je API-keys niet in je repo belanden. `export` geldt alleen in het venster waarin je het
      typt. Daarom `.env` + `python-dotenv`, en `.env` altijd in `.gitignore`. Toepassing:
      [`bitcoin.py`](maand-1-fundament/cs50/libraries/bitcoin/bitcoin.py) haalt zijn
      CoinCap-key uit `COINCAP_API_KEY` in plaats van uit de code.
- [x] **Branching en merging**: geleerd 16 aug op deze repo: het dashboard en deze herschrijving
      zijn op een aparte branch gebouwd en pas daarna samengevoegd. Een merge-conflict veroorzaken
      en oplossen staat nog open; dat komt vanzelf.
- [x] **Virtual environment (venv)**: zelfde familie als de env var: iets buiten je code dat
      bepaalt hoe hij draait. In de praktijk gebruikt vanaf week 3; per project een eigen
      `.venv` met een `requirements.txt` ernaast. Bij het hernoemen van een projectmap breekt
      hij, want in `.venv/bin/` staan absolute paden: weggooien en opnieuw aanmaken.
- [x] **`async`/`await`**: afgevinkt als onderdeel van maand 1 (blok API's/HTTP, "weet dat het
      bestaat"). Dieper dan één alinea is het niet gegaan en dat hoeft ook niet.
- [x] **Wat een HTTP-request/response fysiek ís**: gedaan in week 4, vóór de statuscodes
      (200/401/429/500). Toepassing: de weather CLI, die de Open-Meteo API aanroept en op
      statuscodes controleert.

---

## Waar de rest gebleven is

De volledige uitgeschreven roadmap (alle skills per maand, de picks, de "hoeveel is genoeg"-
grenzen per resource, de CS50P-volgorde en de mijlpalen) staat nu in het
[dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/), en de tekstversie
blijft opvraagbaar in de git-history:

```bash
git show aee8ab0:ROADMAP.md
```

---

**Bron:** de structuur (skills per maand, de twee regels, de vier valkuilen) komt uit een artikel van @free_ai_guides, 7 juli 2026 · https://x.com/i/article/2074513567701680128. De builds van maand 2 t/m 4 zijn van mezelf.
