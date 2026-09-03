# Authenticatie-scan

Vraagt van een lijst domeinen de SPF-, DKIM- en DMARC-records op, leest de DMARC-policy eruit
en telt hoeveel domeinen daadwerkelijk iets tegenhouden. Alleen publieke DNS-data: er gaat
niets naartoe dat niet al openbaar opvraagbaar is.

## Hoe je het draait

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # zet je ANTHROPIC_API_KEY erin, alleen nodig voor --oordeel
```

```bash
python scan.py domeinen.txt
```

Eén domein per regel, kaal (`voorbeeld.nl`, niet `https://www.voorbeeld.nl/`).

Met een geschreven risico-oordeel per domein erbij:

```bash
python scan.py domeinen.txt --oordeel
```

Zonder `--oordeel` komt er geen model aan te pas: het opvragen, parsen en tellen is een
opzoeking, geen oordeel. Zie Beperkingen.

## Wat de output is

JSON, één object per domein:

```json
{
  "domein": "<domein>",
  "spf": "<het ruwe SPF-record, of null>",
  "dmarc": "<het ruwe DMARC-record, of null>",
  "policy": "<none|quarantine|reject|geen>",
  "gemeten_op": "<yyyy-mm-dd>"
}
```

Plus een telling over de hele lijst:

```json
{
  "domeinen": <n>,
  "geen_dmarc": <n>,
  "none": <n>,
  "quarantine": <n>,
  "reject": <n>
}
```

Die vier categorieën tellen op tot `domeinen`. Doen ze dat niet, dan is er een lookup stilletjes
mislukt en klopt het resultaat niet.

## Beperkingen

- **DKIM is niet volledig te controleren zonder de selector.** Zonder de selector die de
  verzender gebruikt, kun je het record niet opvragen. Een leeg DKIM-veld betekent dus
  "niet gevonden", niet "niet aanwezig".
- **Een record zegt niets over of het klopt.** Een SPF-record kan bestaan en tegelijk de
  verkeerde verzendende partijen bevatten. Deze tool leest wat er staat; hij verifieert geen
  verzendstromen.
- **`p=none` is geen fout.** Het is een geldige tussenstap bij het uitrollen van DMARC. Wat het
  wél betekent is dat er op dat moment niets wordt tegengehouden.
- **Een momentopname.** DNS verandert. Elk resultaat heeft daarom `gemeten_op` erbij staan, en
  zonder die datum is een uitkomst niet te citeren.
- **Het model oordeelt alleen, het meet niet.** `--oordeel` zet een schema op de al gemeten
  records. Als het oordeel afwijkt van het record, is het record leidend.

## Wat er nog niet goed aan is

- <wat er kapotgaat, wat je nog niet afgevangen hebt, wat je zou overdoen>
