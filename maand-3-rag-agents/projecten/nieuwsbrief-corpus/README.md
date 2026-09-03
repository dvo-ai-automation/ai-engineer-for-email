# Nieuwsbrief-corpus

Een doorzoekbaar corpus van Nederlandse B2C-nieuwsbrieven, opgebouwd uit een eigen inbox op een
apart e-mailadres dat alleen daarvoor bestaat.

## Dit is geen importscript

Belangrijkste ontwerpbeslissing, en de reden dat deze zin bovenaan staat: dit ding haalt
periodiek mail op, mag dezelfde mail nooit twee keer inladen, en moet het overleven als IMAP er
een dag uit ligt. Daarmee is het het enige onderdeel van het traject dat draait zonder dat
iemand kijkt.

Bouw hem dus vanaf dag één zo, niet als script dat je af en toe start:

- **Idempotent.** Elke mail heeft een `Message-ID`. Sla op welke je al hebt en sla die over.
  Twee keer draaien op één dag mag niets veranderen aan wat erin zit.
- **Hervatbaar.** Breekt de run halverwege af, dan gaat de volgende run verder in plaats van
  opnieuw te beginnen.
- **Het zegt het als hij niets deed.** Nul nieuwe mails op een dinsdag is normaal. Nul nieuwe
  mails op zeven dagen achter elkaar betekent dat er iets stuk is, en dat moet je merken zonder
  ernaar te kijken.

Dat is een vak op zich, en het is het enige stuk daarvan dat in dit traject past zonder extra
build. Zie de sectie "Na dit traject" in [ROADMAP.md](../../../ROADMAP.md).

## Opzet

1. **Verzamelen.** Eén e-mailadres, aangemeld bij 40 tot 60 Nederlandse webshops. Het corpus
   groeit vanaf het moment van aanmelden en niet eerder; dit is het enige onderdeel dat je niet
   kunt inhalen door harder te werken.
2. **Binnenhalen.** Ophalen via IMAP, met de drie eigenschappen hierboven.
3. **Parsen.** HTML naar platte tekst, met subject en preheader apart bewaard.
4. **Embedden.** Chunken, embeddings, wegschrijven naar een lokale vector-DB.
5. **Gebruiken.** Clusteren en doorzoeken, met filtering op de metadata hieronder.

Publieke bron, eigen data. Geen klantdata en geen toestemming nodig.

**De domeinen van deze webshops zijn tegelijk de input voor de
[authenticatie-scan](../../../maand-2-llm-apis/projecten/authenticatie-scan/).** Schrijf ze
tijdens het aanmelden weg in `domeinen.txt`; achteraf reconstrueren is dubbel werk.

## Geplande metadata per mail

| Veld | Inhoud |
|---|---|
| `message_id` | Sleutel voor de dubbelcheck bij het binnenhalen |
| `merk` | Afzender, genormaliseerd naar één naam per webshop |
| `datum` | Verzenddatum |
| `type` | `promo`, `transactioneel` of `redactioneel` |
| `sector` | Branche van de webshop |
| `subject` | De subject line, los van de body |
| `preheader` | De preheader, los van de body |

Deze indeling ligt nog niet vast: `type` en `sector` zijn de twee die waarschijnlijk schuiven
zodra er echte mails in zitten.

## Wat het oplevert

De labelset voor de evals (build B) komt hieruit, en de checker uit maand 2 draait erop.

## Wat er nog niet goed aan is

*Nog niets gebouwd. Dit kopje vullen zodra er iets draait.*
