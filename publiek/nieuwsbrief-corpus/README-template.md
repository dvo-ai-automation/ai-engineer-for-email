# Nieuwsbrief-corpus

Bouwt een doorzoekbaar corpus van Nederlandse B2C-nieuwsbrieven op uit één e-mailadres dat
alleen daarvoor bestaat: binnenhalen via IMAP, HTML naar platte tekst, subject en preheader
apart, embeddings in een lokale vector-DB. Daarmee kun je filteren op merk, periode en type, en
clusteren om te zien hoe webshops hun e-mail inrichten.

## Hoe je het draait

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # IMAP-gegevens en je embedding-key
```

Ophalen en indexeren:

```bash
python ingest.py --since <datum>
```

Zoeken:

```bash
python zoek.py "<vraag of zin>" --merk "<merk>" --type promo --vanaf <datum>
```

Clusteren:

```bash
python cluster.py --k <aantal clusters>
```

Het corpus groeit alleen als het e-mailadres aangemeld staat. Aanmelden is handwerk en het duurt
weken voordat er volume is; zonder aanmelden levert dit script niets op.

## Wat de output is

`ingest.py` schrijft per mail één record weg:

```json
{
  "merk": "<afzender, genormaliseerd>",
  "datum": "<verzenddatum>",
  "type": "<promo|transactioneel|redactioneel>",
  "sector": "<branche>",
  "subject": "<de subject line>",
  "preheader": "<de preheader>",
  "tekst": "<body als platte tekst>"
}
```

`zoek.py` geeft de best scorende mails terug met hun metadata. `cluster.py` geeft per cluster
het aantal mails, de merken die erin zitten en de termen die het cluster onderscheiden:

```
Cluster <n> · <aantal> mails · <aantal> merken
  kenmerkende termen: <termen>
  merken: <merken>
```

## Beperkingen

- **Eén inbox, niet de markt.** Het corpus bevat wat er naar dat ene adres verstuurd is. Merken
  die niet zijn aangemeld ontbreken, en segmentatie aan de kant van de afzender bepaalt mee wat
  je krijgt. Het is geen aselecte steekproef en de uitkomsten zijn niet naar "de Nederlandse
  e-mailmarkt" te generaliseren.
- **Nederlandse B2C-webshops.** B2B, non-profit en buitenlandse afzenders zitten er niet in.
- **HTML-parsing verliest opmaak.** Alles wat betekenis droeg via beeld, kleur of positie is weg.
- **`type` en `sector` zijn toegekend, niet gemeten.** Hoe dat gebeurt staat in `labels.md`, met
  de gevallen waarin het misgaat.
- **Geen persoonsgegevens.** Ontvangergegevens, tracking-parameters en unsubscribe-links worden
  bij het parsen verwijderd. Het corpus zelf staat niet in deze repo.

## Wat er nog niet goed aan is

- <wat er kapotgaat, welke merken je niet binnenkrijgt, wat je zou overdoen>
