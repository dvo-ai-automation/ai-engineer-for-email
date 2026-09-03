# Subject line- en preheader-checker

Controleert een subject line plus preheader op wat objectief te controleren is: hoe de regel
eruitkomt per client, of de preheader past, en hoe emoji renderen. Claude API met een JSON-schema
als output.

## Wat het teruggeeft

- `weergave` — per client (Gmail, Outlook, Apple Mail, mobiel), met het afkappunt in tekens en pixels
- `preheader` — lengte, en of de eerste regel body de preheader opeet
- `emoji` — rendering en fallback per platform

De merkstem gaat er als parameter in, voor context. Er komt geen cijfer op stijl uit: een score
op merkstem is niet toetsbaar, dus er kan later geen eval tegenaan.

Er zit ook geen spamwoordscore in. Spamwoordenlijsten zijn achterhaald; moderne filters kijken
naar reputatie, engagement en authenticatie.

## Draaien

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`ANTHROPIC_API_KEY` komt uit `.env` en staat niet in de repo.

## Status

`hello.py` is de eerste werkende API-call, nog geen checker. Hij vraagt om spamwoorden en is
daarmee achterhaald door de opzet hierboven; hij blijft staan als eerste call en gaat eruit
zodra de echte checker draait.

## Wat er nog niet goed aan is

*Nog niets gebouwd behalve die eerste call. Dit kopje vullen zodra er iets draait.*
