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

**1. De datalaag: RFM, retentie-analyses en het datamodel eronder.** Deze roadmap maakt me
expert in AI over tékst — subject lines, preheaders, copy, briefings. Geen enkele build raakt
een contact, een event, een aankoop of een segment. Daarmee vallen drie onderwerpen die in mijn
vak zwaar wegen volledig buiten dit traject: **RFM-modellen**, **retentie- en cohortanalyses**,
en **het datamodel** waar die twee op rusten (contacten, events, sends en orders koppelen met
identiteiten die niet matchen). Ze hebben alle drie gedragsdata op contactniveau nodig, en die
heb ik niet zonder klant.
Maar de vraag waar mijn doelgroep op vastloopt is niet "schrijf een betere onderwerpregel"
(dat doen ze zelf met ChatGPT), het is "wie krijgt wat, en wanneer". Dat is een datavraagstuk:
ESP-events, shopdata en analytics aan elkaar knopen op contactniveau, met identiteiten die niet
matchen. SQL staat in maand 1 genoemd en is stilzwijgend nooit gebeurd.

Wat er wél van in dit traject zit: het normaliseren, dedupliceren en classificeren van de
merken in het corpus. Datzelfde werk, op een schaal die in één maand past.

De rest is te groot voor elf weken naast RAG, evals en shippen. Het is wel het onderwerp van het
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

## Waar ik het dan voor inzet

*Toegevoegd 3 sep 2026, omdat dit het stuk was dat ontbrak: de builds hierboven zijn geen
producten, en dat kan verwarrend zijn als je er middenin zit.*

Geen van de zes builds is iets waar een CRM-manager voor betaalt. Een DMARC-check doet mxtoolbox
gratis, een subject line-classifier wil niemand dagelijks draaien, en een corpus van
nieuwsbrieven is onderzoek. Dat is opzet, geen fout: **deze roadmap traint capaciteiten op
publiceerbare proxies.** De echte toepassingen in mijn vak hebben allemaal klantdata of
ESP-toegang nodig en mogen dus niet naar buiten. De builds zijn het bewijs dat ik het kan; het
product is iets anders.

Wat ik na dit traject kan bouwen, valt in vier vormen: rommelige input betrouwbaar omzetten in
gestructureerde data mét een gemeten foutmarge · een berg documenten doorzoekbaar maken met
antwoorden die naar hun bron wijzen · iets in de gaten houden en melden als het verandert · dat
alles onbewaakt laten draaien tegen voorspelbare kosten.

Vertaald naar wat een klant daar aan heeft, drie dingen. Geen ervan staat in de roadmap hierboven,
omdat ze alle drie klanttoegang vragen — maar de vaardigheden ervoor zitten er in november wel.

**1. Journey-inventarisatie.** De ESP-API uitlezen en teruggeven: elke live flow, wanneer hij voor
het laatst verstuurde, hoeveel mensen erin kwamen, wat hij opleverde, en welke flows niemand meer
kan benoemen. Saai, onsexy, en enorm waardevol, want vrijwel elke partij waar ik binnenkom heeft
dit niet. Ik heb het handmatig al een keer gedaan; wat ik miste is de code eromheen.

**2. Alerting op kapotte flows.** Een welkomstflow staat drie weken stil en niemand merkt het.
Direct geldverlies, en precies wat de signaalsplitser doet — alleen zonder ESP-koppeling. Dit is
de meest gevraagde van de drie.

**3. Rapportage die klopt en uitlegbaar is.** Per journey, per week, met erbij waarom het getal
niet optelt tot wat de ESP claimt. Dat is de post van week 7, maar dan als draaiend systeem in
plaats van een verhaal.

Wat deze drie gemeen hebben: **het is geen AI-magie, het is plumbing met oordeelsvermogen erin.**
Dat is wat ik na vier maanden kan en nu niet.

**Nog steeds buiten bereik:** segmentatie, RFM, churn-scoring, next-best-offer — alles wat gedrag
op contactniveau nodig heeft, wacht op de datalaag hierboven. Net als alles dat op echt volume
moet draaien of een serieuze gebruikersinterface heeft.

**Eén open vraag.** De signaalsplitser is één stap verwijderd van een demo die een CRM-manager
binnen tien seconden begrijpt: een ESP-adapter, gekoppeld aan een eigen gratis testaccount in
plaats van aan synthetische reeksen. Maar ik heb zelf vastgelegd dat de ESP-kant intern blijft
omdat Funnelboost zelf alerting bouwt. Dat is een gesprek met mijn werkgever, geen technische
beslissing: vraag of een publieke demonstrator op een eigen testaccount botst met wat zij bouwen.
Het antwoord kan prima ja zijn.

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

## Waar dit eindigt

*Geschreven 3 sep 2026, halverwege maand 2. Bedoeld om terug te lezen in week 11, als het
bouwen tegenzit en de vraag opkomt waar dit ook alweer voor was. Eerlijk opgeschreven, niet
motiverend.*

**Wat ik op 18 november kan** — niet begrijp, maar kan, met iets dat draait als bewijs:

- Een model een afgebakende taak laten doen binnen een programma, met een schema eromheen zodat mijn code op de uitkomst kan vertrouwen
- Meten of dat model het goed doet: een gelabelde set bouwen, er een getal uit halen, twee promptversies tegen elkaar zetten
- Retrieval over eigen data: embedden, opslaan met metadata, filteren, reranken, antwoorden mét bron
- Beoordelen wanneer er géén model in moet
- Iets deployen dat draait zonder mij, met kostenplafonds en tracing
- Een fout in dat alles opsporen zonder te gokken

Niet indrukwekkend voor een engineer met vijf jaar ervaring. Wel ongebruikelijk voor iemand in
e-mailmarketing.

**Wat ik dan nog niet kan:** werken op datavolume (geen SQL, geen joins over systemen — zie "Na
dit traject"), productie-engineering (queues, concurrency, CI), werken in andermans code — alles
wat ik bouw is greenfield en solo, ik heb nooit een review gehad — en iets draaien dat echt
gebruikt wordt.

**Het gat:** ik heb dan bewijs dat ik kan bouwen, en geen bewijs van effect. Elk getal dat ik
publiceer gaat over de markt of over mijn eigen gereedschap, niet over "ik deed X bij een bedrijf
en toen gebeurde Y". Dat effect is er wel, in mijn dagelijkse werk, maar het mag niet naar buiten.
Dat is geen fout in het plan; het is de prijs van netjes omgaan met klantdata.

**Wat de posts doen.** Niet: een publiek opbouwen. Vijf posts in drie maanden is geen bereik en
levert geen inbound op. Wel: wie mij opzoekt vindt binnen anderhalve minuut een samenhangend spoor
van werk dat niemand anders in dit vakgebied heeft. Ik word verifieerbaar, en ik krijg vijf
aanleidingen om zelf een gesprek te openen.

**Wat het oplevert, en niet meer dan dit:**

1. **Ik kan afmaken wat ik begin.** Nu stel ik samen, straks bouw ik. Dat verandert welke opdrachten ik aandurf.
2. **Ik meet.** Iedereen in e-mailmarketing laat inmiddels AI teksten schrijven; vrijwel niemand kan zeggen hoe vaak dat ding ernaast zit.
3. **Ik heb iets dat van mij is.** Het corpus vooral: een dataset over de Nederlandse markt die niemand anders heeft en die vanzelf blijft groeien. **Zet hem niet stil op 18 november.**

Wat het níét oplevert: een andere functietitel, een publiek, of autoriteit. Die komen van
herhaling ná november.

**Over dat ik de helft nog niet snap.** Dat is de volgorde, niet een probleem. Embeddings snap je
niet vóór je er iets mee bouwt. In november zal een deel nog steeds niet diep zitten, en dat hoeft
ook niet — de doelstelling bovenaan dit bestand zegt *repareren*, niet doorgronden. Die lat haal
ik als ik dit afmaak.

**De twee dingen die het meest zouden toevoegen, en die nu nergens gepland staan:** één echte
gebruiker van de voordeur die ik zelf niet ben, en één keer dat mijn eigen meting een beslissing
op mijn werk heeft veranderd — dat laatste mag ik beschrijven als mechanisme, zonder klant en
zonder cijfer.

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
