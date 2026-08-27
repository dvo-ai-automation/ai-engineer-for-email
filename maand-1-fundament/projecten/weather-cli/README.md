# Weather CLI

> **Status: af.** Het script draait, vangt zijn eigen fouten af en schrijft naar een bestand.
> Onderaan staat een eerlijk kopje over wat er nog niet aan deugt.

Het tweede en laatste project van maand 1. Je geeft een plaatsnaam mee, het script haalt de
temperatuur op via de [Open-Meteo API](https://open-meteo.com/en/docs), print drie dagen in de
terminal en bewaart ze in `weer.json`.

## Waarom deze build

De [expense tracker](../expense-tracker/) leest en schrijft bestanden en handelt zijn eigen
errors af. [`bitcoin.py`](../../cs50/libraries/bitcoin/) roept een externe API aan. Wat ik nog
niet had gedaan is die twee in één programma combineren, en dat is precies de mijlpaal van
maand 1:

> Een Python-programma dat bestanden leest/schrijft, een API aanroept en zijn eigen errors
> afhandelt zonder te crashen.

Open-Meteo vraagt geen API-key. Dat was bewust: het haalt één obstakel weg, zodat de aandacht
naar het request en het uitpakken van het JSON-antwoord gaat in plaats van naar authenticatie.

## Gebruiken

```bash
cd maand-1-fundament/projecten/weather-cli
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python weatherV4.py "Amsterdam"
```

De plaatsnaam moet tussen aanhalingstekens, anders ziet Python `Den` en `Haag` als twee losse
argumenten en stopt het script.

```
$ python weatherV4.py "Amsterdam"
De temperatuur was vandaag 27.2°C. Morgen wordt het 19.8°C en overmorgen 18.1°C
```

En in `weer.json` komt erbij:

```json
[
  { "tijd": "2026-08-27", "temperatuur": 27.2 },
  { "tijd": "2026-08-28", "temperatuur": 19.8 },
  { "tijd": "2026-08-29", "temperatuur": 18.1 }
]
```

## Hoe het werkt

Het script doet **twee** API-calls, en dat is de kern van de opdracht:

1. **Geocoding** — `geocoding-api.open-meteo.com` zet `"Amsterdam"` om naar coördinaten
   (`52.37`, `4.89`). Zonder deze stap kun je alleen hardgecodeerde plekken opvragen.
2. **Forecast** — `api.open-meteo.com` geeft met die coördinaten 72 uurwaarden terug, drie
   dagen à 24 uur.

Uit die 72 waarden pakt het script de indexen `17`, `41` en `65`: 17:00 uur op dag 1, 2 en 3.
De timestamp `2026-08-27T17:00` wordt met `.split("T")` in stukken gehakt zodat alleen de datum
overblijft.

## Van V1 naar V4

Elke versie loste één probleem op dat de vorige nog had. Alle vier staan nog in de map, zodat je
ze naast elkaar kunt lezen:

| versie | wat erbij kwam | commit |
|---|---|---|
| **V1** | 12 regels: één GET, één temperatuur, printen. Coördinaten hardgecodeerd. | [`f3f9fff`](https://github.com/dvo-ai-automation/ai-engineer-4-months/commit/f3f9fff) |
| **V2** | Drie dagen in plaats van één, timestamp opsplitsen, wegschrijven naar `weer.json`. | [`d823212`](https://github.com/dvo-ai-automation/ai-engineer-4-months/commit/d823212) |
| **V3** | Plaatsnaam als argument, geocoding-call erbij, `try`/`except` op timeouts, statuscodes. | [`3a7aff9`](https://github.com/dvo-ai-automation/ai-engineer-4-months/commit/3a7aff9) |
| **V4** | Statuscode-checks die daadwerkelijk werken. Zie hieronder. | [`9ca012e`](https://github.com/dvo-ai-automation/ai-engineer-4-months/commit/9ca012e) |

De les van V4 zat in één teken. V3 had dit:

```python
if w.status_code == [500, 503]:
```

Een `int` vergelijken met een `list` is altijd `False`. Die check ging dus nooit af: bij een
serverfout viel het script stilletjes door en probeerde het verder te rekenen met een kapotte
response. `in` is wat ik bedoelde, `==` is wat ik schreef, en Python klaagt daar niet over.
Dat is precies het soort fout dat je niet ziet zolang alles goed gaat.

Dezelfde ronde: de check op de opgehaalde data keek naar `plaats` (de geocoding-response) in
plaats van naar `data` (het weerbericht), en de melding bij een 400 zei "Check je API-key"
terwijl deze API helemaal geen key gebruikt.

## Wat het afvangt

| situatie | wat er gebeurt |
|---|---|
| geen argument meegegeven | `Geef een plaatsnaam op tussen aanhalingstekens` |
| geen internet of API te traag (>5s) | `API-call timed out` |
| plaatsnaam bestaat niet | `plaatsnaam bestaat niet` |
| status 500 of 503 | `Wacht even en probeer het nogmaals` |
| status 400, 401 of 404 | `Ongeldige coördinaten` |
| status 403 | `Je hebt geen toegang` |
| data opgehaald maar `hourly` ontbreekt | `Data wel opgehaald, maar er zit niet in wat je zocht` |
| `weer.json` bestaat niet | `Maak weer.json aan` |

Alles gaat via `sys.exit()` met een leesbare melding, dus geen traceback in het gezicht van de
gebruiker en een exit code van 1 voor de shell.

## Wat er nog niet aan deugt

Dit is de lijst die ik bewust laat staan. Ze horen bij een volgende versie, niet bij deze.

- **"Vandaag" klopt niet buiten Engeland.** Ik geef geen `timezone` mee, dus Open-Meteo
  antwoordt in GMT. Index 17 is dus 17:00 GMT, wat in Nederland 19:00 is en in Tokio 02:00 de
  volgende ochtend. Het getal is echt, het label "vandaag" is voor plaatsen ver van GMT
  misleidend. Op te lossen met `&timezone=auto` in de URL.
- **De indexen 17, 41 en 65 zijn hardgecodeerd.** Ze werken alleen omdat ik precies 72
  uurwaarden opvraag die om middernacht beginnen. Zodra ik `forecast_days` verander, klopt het
  niet meer. Zoeken op de datum in `time` zou robuuster zijn dan tellen.
- **Het weermodel staat vast op `knmi_seamless`.** Prima voor Nederland, maar ik vraag het ook
  voor Tokio op zonder te controleren of dat model daar iets zinnigs zegt.
- **Ambigue plaatsnamen gaan stil fout.** Ik vraag `count=10` resultaten op en pak er
  altijd blind de eerste van. Bij "London" krijg je er één, zonder te vragen welke.
- **`weer.json` groeit met dubbelingen.** Twee keer draaien op dezelfde dag zet dezelfde datum
  er twee keer in. Er is geen check of een datum al bestaat.
- **Het script maakt `weer.json` niet zelf aan**, het zegt alleen dat jij dat moet doen. Met
  `'a'` of een `try`/`except` eromheen kan dat netter.
- **`data` wordt hergebruikt voor twee dingen**: eerst het weerbericht, daarna de inhoud van
  het JSON-bestand. Het werkt, maar het is verwarrend om te lezen.
- **Een lege `results`-lijst geeft een `IndexError`**, en die vang ik niet af. Ik vang alleen
  `KeyError`.

## Wat ik hier geleerd heb

Niet het script zelf, dat is een middel. Het ging om de vraag die de roadmap oversloeg:
**wat is een HTTP-request fysiek?** De statuscodes (200 ok, 401 verkeerde key, 429 rate limit,
500 serverfout) zijn pas te onthouden als het model eronder klopt.

Wat er bij deze build echt is blijven hangen:

- Een API-antwoord is gewoon een dict met lijsten erin. Het uitpakken is hetzelfde werk als
  bij een zelfgemaakt bestand, alleen bepaal jij de vorm niet.
- Een `try`/`except` om een request heen vangt netwerkproblemen af; een statuscode-check vangt
  af dat de server je verzoek weigert. Dat zijn twee verschillende dingen en je hebt ze allebei
  nodig.
- Een check die er goed uitziet, kan stilletjes nooit afgaan. `== [500, 503]` crasht niet, hij
  doet gewoon niks. Testen of je error-afhandeling écht triggert hoort erbij.

Elke LLM-aanroep die ik vanaf maand 2 doe is in de kern ditzelfde request, dus deze laag moest
zitten.

---

*Gebouwd in maand 1, week 4. Volgende stop: [maand 2](../../../maand-2-llm-apis/).*
