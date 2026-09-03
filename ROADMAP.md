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

**De regel waar deze builds op geselecteerd zijn:** de post is het product, de build is hoe ik
het recht verdien om hem te schrijven. Elke post hieronder heeft een getal dat ik zelf gemeten
heb, een mechanisme dat ik alleen ken omdat ik het gebouwd heb, en een zin die de lezer maandag
kan gebruiken. Haalt een build die drie niet, dan is het een oefening en geen post.

**Maand 2 · LLM-API's** — [details](maand-2-llm-apis/README.md)

- **C. Authenticatie-scan.** SPF, DKIM en DMARC van de webshops uit de corpuslijst opvragen, parsen en tellen. De DNS-kant is deterministisch; het model komt pas in beeld bij het omzetten naar oordelen in vaste vorm. Dit is de oefenbuild voor structured outputs én de makkelijkste eval-set van het traject, want een DMARC-verdict heeft een objectief goed antwoord.
- **A. Subject line- en preheader-checker.** Van weergave-check naar classificatie: wat voor belofte wordt er gedaan, hoe verhoudt de preheader zich tot de subject line, en wordt de belofte in de body waargemaakt. De weergave-check is eruit — dat doet elke ESP-preview al. Merkstem blijft een parameter, geen score.
- **B. Briefing naar campagnedocument.** Tool calling. Blijft intern; de documentstructuur is werkgevers-IP, dus deze telt niet mee als extern bewijs.
- **Posts:** week 7 wat een journey oplevert (de drie oude journey-posts samengevoegd tot één) · week 8 de DMARC-verdeling over de gemeten domeinen.

**Maand 3 · RAG en agents** — [details](maand-3-rag-agents/README.md)

- **A. Corpus van Nederlandse B2C-nieuwsbrieven.** IMAP, HTML naar platte tekst, embeddings, vector-DB met metadata. **Gebouwd als iets dat draait zonder dat ik kijk:** idempotent, hervatbaar, en het meldt zijn eigen stilte. Dezelfde skills als een docs-RAG, maar het levert een bevinding op in plaats van een vraagbaak.
- **B. Evals op de checker uit maand 2.** Vijftig gelabelde subject lines uit het corpus, en meten hoe vaak de prompt het goed heeft. De belangrijkste build.
- **C. Signaalsplitser.** Stuk is deterministisch, minder is statistisch. From scratch, op synthetische tijdreeksen, zonder ESP-koppeling. **Bouwen wel, posten niet** — op synthetische data is het een ontwerpverhaal.
- **Posts:** week 10–11 wat het corpus laat zien · week 12 hoe je weet of de AI die je subject lines schrijft het goed heeft.

**Maand 4 · Shippen** — [details](maand-4-ship-it/README.md)

- Een voordeur op het corpus: iemand plakt een subject line of stuurt een nieuwsbrief door en krijgt terug hoe die zich verhoudt tot de merken in het corpus. Het enige artefact van het traject dat een e-commerce owner zelf opent.
- Daarnaast de authenticatie-scan publiek draaibaar maken.
- **Post:** week 15–16 de tool live, plus wat er stukging toen er iemand anders op klikte.

---

## Na dit traject

*Toegevoegd 3 sep 2026. Twee dingen die waardevol zijn voor waar ik naartoe wil, maar die niet
in de resterende weken passen. Ze staan hier zodat ze niet verdwijnen, niet omdat ze nu aan de
beurt zijn.*

**1. De datalaag.** Deze roadmap maakt me expert in AI over tékst — subject lines, preheaders,
copy, briefings. Geen enkele build raakt een contact, een event, een aankoop of een segment.
Maar de vraag waar mijn doelgroep op vastloopt is niet "schrijf een betere onderwerpregel"
(dat doen ze zelf met ChatGPT), het is "wie krijgt wat, en wanneer". Dat is een datavraagstuk:
ESP-events, shopdata en analytics aan elkaar knopen op contactniveau, met identiteiten die niet
matchen. SQL staat in maand 1 genoemd en is stilzwijgend nooit gebeurd.

Het is te groot voor elf weken naast RAG, evals en shippen. Het is wel het onderwerp van het
volgende traject. Het kan zonder klantdata: er bestaan publieke transactiedatasets van echte
webshops — echte aankopen, alleen niet uit mijn markt, dus het mechanisme is overdraagbaar en
het getal niet. Dat is wat je erbij zegt.

**2. Onbewaakt draaien.** Elke build hier is een script dat ik start. Wat mijn doelgroep koopt
is het tegenovergestelde: iets dat maandagochtend gedraaid heeft zonder dat iemand keek.
Scheduling, state, idempotentie, herstel na een afgebroken run. Docker en Langfuse in maand 4
zijn verpakking, geen bedrijfsvoering. Het enige stuk dat nu al meegaat is het corpus, dat als
onbewaakt systeem gebouwd wordt in plaats van als importscript.

**3. Wat je wel en niet door een model mag halen.** Deze repo zit vol met "geen klantdata",
"publieke bron", "toestemming aanvragen in week 5". Dat oordeelsvermogen is zichtbaar in de
bestandsstructuur en onzichtbaar voor de doelgroep, terwijl het precies de vraag is die bij
Nederlandse B2C-webshops elk AI-project blokkeert. Hoort erbij: een laag die namen, adressen en
ordernummers eruit haalt vóór de API-call en ze er daarna weer in zet. Een dag werk, en het
interessante zit in wat de regex mist. **Dit is de goedkoopste van de drie — als maand 3 op
schema ligt, kan deze er wél bij.**

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
