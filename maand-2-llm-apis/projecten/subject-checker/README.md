# Subject line- en preheader-checker

Classificeert een subject line plus preheader: wat voor belofte wordt er gedaan, hoe verhoudt
de preheader zich tot de subject line, en wordt die belofte in de body waargemaakt. Claude API
met een JSON-schema als output.

## Waarom niet de weergave-check

De eerste opzet controleerde het afkappunt per client, de preheaderlengte en emoji-rendering.
Dat is eruit gegaan: dat doet elke ESP-preview en elke previewtool al. De lezer denkt dan
"dat heb ik al", en terecht.

Wat niemand heeft is de laag eronder — een instrument dat je over duizend nieuwsbrieven kunt
halen om te zien wát Nederlandse webshops hun lezers beloven. Daarmee is dit geen los tooltje
meer maar het meetinstrument voor
[het corpus](../../../maand-3-rag-agents/projecten/nieuwsbrief-corpus/) in maand 3.

## Wat het teruggeeft

- `belofte` — het type belofte: korting, nieuw assortiment, urgentie, redactioneel, service
- `preheader_relatie` — herhaalt de preheader de subject line, vult hij hem aan, of staat hij los
- `belofte_ingelost` — komt de belofte terug in de body, ja/nee/niet vast te stellen
- `merkstem` — gaat er als parameter in, voor context. Er komt geen cijfer op stijl uit: een
  score op stijl is niet toetsbaar, dus er kan later geen eval tegenaan

Elk veld hierboven is zo gekozen dat een mens er onafhankelijk een label bij kan zetten. Dat is
de voorwaarde om er in maand 3 een eval tegenaan te kunnen leggen.

Geen spamwoordscore. Spamwoordenlijsten zijn achterhaald; moderne filters kijken naar reputatie,
engagement en authenticatie — dat laatste meet de
[authenticatie-scan](../authenticatie-scan/).

## De vijf promptversies

Dit is waar het promptingblok van maand 2 landt. Geen los promptproject: vijf versies van
dezelfde checker, in `prompts/`, alle vijf gedraaid over dezelfde twintig regels uit het corpus.

| Versie | Wat erin zit | Welke roadmap-stap dit is |
|---|---|---|
| `prompts/v1.txt` | Kale instructie: "beoordeel deze subject line". | De nulmeting. Zonder v1 weet je niet of de rest iets oplevert |
| `prompts/v2.txt` | De vijf beloftecategorieën expliciet gedefinieerd, elk in één zin, met de grensgevallen erbij. | *Specificiteit verslaat beleefdheid* |
| `prompts/v3.txt` | Het model benoemt eerst in één zin wát er beloofd wordt, kiest daarna pas de categorie. | *Chain-of-thought* |
| `prompts/v4.txt` | Vijf handgelabelde subject lines uit het corpus als voorbeeld. | *Few-shot* |
| `prompts/v5.txt` | Wat er in v2 t/m v4 werkte, gecombineerd. | *Gevoel voor woordkeuzes* |

- [ ] v1 t/m v5 geschreven en opgeslagen
- [ ] Alle vijf gedraaid over dezelfde twintig regels, outputs naast elkaar in `vergelijking.md`
- [ ] De vijf few-shot-voorbeelden apart in `few-shot.jsonl`

**Die laatste stap is niet optioneel.** De voorbeelden uit v4 mogen nooit in de eval-set van
maand 3 terechtkomen: dan meet je of het model zijn eigen voorbeelden herkent in plaats van of
het de taak kan. Zet ze apart op het moment dat je ze kiest, niet achteraf.

De vijf versies plus de vergelijkingstabel zijn de nulmeting waar
[build B in maand 3](../../../maand-3-rag-agents/README.md) tegen meet. Achteraf reconstrueren
lukt niet — je weet dan niet meer welke versie welke output gaf.

## Draaien

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`ANTHROPIC_API_KEY` komt uit `.env` en staat niet in de repo.

## Status

`hello.py` is de eerste werkende API-call, nog geen checker. Hij vraagt om spamwoorden en is
daarmee dubbel achterhaald; hij blijft staan als eerste call en gaat eruit zodra de echte
checker draait.

Het schemapatroon dat deze build gebruikt, wordt eerst een week eerder geoefend op de
[authenticatie-scan](../authenticatie-scan/). Dezelfde skill, twee keer toegepast.

## Wat er nog niet goed aan is

*Nog niets gebouwd behalve die eerste call. Dit kopje vullen zodra er iets draait.*
