# Subject line- en preheader-checker

Classificeert een subject line plus preheader: wat voor belofte er gedaan wordt, hoe de
preheader zich tot de subject line verhoudt, en of die belofte in de body terugkomt. Claude API
met een JSON-schema als output, zodat elke uitkomst per veld te toetsen is in plaats van een
oordeel in proza.

Bewust géén weergave-check (afkappunt per client, emoji-rendering): dat doet elke ESP-preview
al. Dit is een meetinstrument om over een grote hoeveelheid nieuwsbrieven te halen.

## Hoe je het draait

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # zet je ANTHROPIC_API_KEY erin
```

```bash
python check.py --subject "<subject line>" --preheader "<preheader>"
```

Met de body erbij, zodat `belofte_ingelost` ingevuld kan worden:

```bash
python check.py --subject "<subject line>" --preheader "<preheader>" --body <bestand.txt>
```

Met een merkstem als context:

```bash
python check.py --subject "<subject line>" --preheader "<preheader>" --merkstem merkstem.md
```

De merkstem gaat er als parameter in en beïnvloedt de toelichting. Er komt geen cijfer op stijl
uit; zie Beperkingen.

## Wat de output is

JSON, één object per gecontroleerde regel:

```json
{
  "subject": "<de ingevoerde subject line>",
  "preheader": "<de ingevoerde preheader>",
  "belofte": "<korting|nieuw_assortiment|urgentie|redactioneel|service>",
  "preheader_relatie": "<herhaalt|vult_aan|staat_los>",
  "belofte_ingelost": "<ja|nee|niet_vast_te_stellen>",
  "toelichting": "<waarom, in één zin per veld>"
}
```

Elk veld is zo gekozen dat een mens er onafhankelijk een label bij kan zetten. Dat is de
voorwaarde om er een eval tegenaan te kunnen leggen; zie `evals/`.

## Beperkingen

- **Geen spamwoordscore.** Spamwoordenlijsten zijn achterhaald: moderne filters kijken naar
  reputatie, engagement en authenticatie, niet naar losse woorden. Voor dat laatste is er een
  aparte tool.
- **Geen score op merkstem.** Een cijfer op stijl is niet toetsbaar en er kan dus geen eval
  tegenaan. De merkstem is er alleen als context voor de toelichting.
- **`belofte_ingelost` kan alleen mét body.** Zonder `--body` staat dat veld altijd op
  `niet_vast_te_stellen`, en dat is geen bevinding.
- **De categorieën zijn een keuze, geen natuurwet.** Ze komen uit `<hoe je ze bepaald hebt>`.
  Een regel die in twee categorieën past, krijgt er één.
- **Geen voorspelling van open rate.** De tool zegt wat er beloofd wordt, niet hoe het presteert.
- **Gemeten kwaliteit: `<score per veld>`, op `<n>` gelabelde regels uit `<m>` merken.**
  Staat hier nog een punthaak, dan is dit getal niet gemeten en mag je het niet claimen.

## Wat er nog niet goed aan is

- <wat er kapotgaat, wat je nog niet afgevangen hebt, wat je zou overdoen>
