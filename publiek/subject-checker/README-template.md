# Subject line- en preheader-checker

Controleert een subject line en preheader op wat objectief te controleren is: waar de regel
afkapt per mailclient, of de preheader past en niet wordt opgegeten door de eerste regel body,
en hoe emoji renderen per platform. Claude API met een JSON-schema als output, zodat de
uitkomst per veld te toetsen is in plaats van een oordeel in proza.

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
  "weergave": {
    "<client>": { "afkap_tekens": <n>, "afkap_pixels": <n>, "zichtbaar": "<het deel dat overblijft>" }
  },
  "preheader_check": {
    "lengte_tekens": <n>,
    "body_eet_preheader": <true|false>,
    "toelichting": "<waarom wel of niet>"
  },
  "emoji": [
    { "teken": "<emoji>", "rendert_op": ["<platform>"], "fallback": "<wat er staat als het niet rendert>" }
  ]
}
```

De clients en platforms die daadwerkelijk gecontroleerd worden, staan in `clients.json`.

## Beperkingen

- **Geen spamwoordscore.** Spamwoordenlijsten zijn achterhaald: moderne filters kijken naar
  reputatie, engagement en authenticatie, niet naar losse woorden. Een lijst zou een getal
  opleveren dat nergens mee correleert.
- **Geen score op merkstem.** Een cijfer op stijl is niet toetsbaar en er kan dus geen eval
  tegenaan. De merkstem is er alleen als context voor de toelichting.
- **Afkappunten zijn een benadering.** Ze komen uit `clients.json`, niet uit een render-engine.
  Clients wijzigen hun weergave zonder aankondiging; de waarden zijn voor het laatst
  gecontroleerd op `<datum>`.
- **Geen voorspelling van open rate.** De tool zegt hoe een regel eruitkomt, niet hoe hij
  presteert.

## Wat er nog niet goed aan is

- <wat er kapotgaat, wat je nog niet afgevangen hebt, wat je zou overdoen>
