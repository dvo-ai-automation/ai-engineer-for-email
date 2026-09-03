# Authenticatie-scan

Vraagt van een lijst domeinen de SPF-, DKIM- en DMARC-records op, parseert ze, en telt hoeveel
er daadwerkelijk beschermd zijn. Publieke DNS-data, geen klantdata, geen toestemming nodig.

## Waarom deze build hier staat

Twee redenen, en de tweede is de belangrijkste.

**Hij levert een post met een gemeten getal.** De domeinlijst is dezelfde lijst webshops
waar het [nieuwsbrief-corpus](../../../maand-3-rag-agents/projecten/nieuwsbrief-corpus/) zich
bij aanmeldt, dus het verzamelwerk gebeurt toch al. Wat eruit komt — hoeveel van die merken op
`p=none` staan, dus wel meten maar niets tegenhouden — is iets wat de lezer binnen tien minuten
op zijn eigen domein kan nadoen.

**Hij is de oefenbuild voor structured outputs.** De DNS-kant is deterministisch: een record
zegt wat het zegt, daar hoort geen model bij. Het model komt pas in beeld bij het omzetten van
veertig gepareseerde records naar veertig leesbare risico-oordelen met dezelfde vorm. Dat is
precies de skill van maand 2, geoefend op data die je al hebt, vóór je hem toepast op de
[subject-checker](../subject-checker/).

En daarmee levert hij en passant de makkelijkste eval-set die er is: een DMARC-verdict heeft
een objectief goed antwoord. Als je in maand 3 je eerste eval bouwt, wil je beginnen op een set
waar vaststaat wat goed is, vóór je aan subject lines begint waar het label discutabel is.

## Opzet

| Stap | Wat | Model nodig? |
|---|---|---|
| 1 | Domeinen inlezen uit `domeinen.txt` | nee |
| 2 | SPF-, DKIM- en DMARC-records opvragen via DNS | nee |
| 3 | Policy eruit parsen (`p=none` / `quarantine` / `reject`) | nee |
| 4 | Tellen per categorie | nee |
| 5 | Per domein een risico-oordeel in vaste vorm | ja, met schema |

De grens tussen stap 4 en 5 is het hele punt van deze build. Alles boven die lijn is een
opzoeking en hoort nooit door een model te gaan.

## Draaien

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scan.py
```

`ANTHROPIC_API_KEY` komt uit `.env` en staat niet in de repo.

## Wat er nog niet goed aan is

*Nog niets gebouwd. Dit kopje vullen zodra er iets draait.*
