# Nieuwsbrief-corpus

Een doorzoekbaar corpus van Nederlandse B2C-nieuwsbrieven, opgebouwd uit mijn eigen inbox op een
apart e-mailadres dat alleen daarvoor bestaat.

## Opzet

1. **Verzamelen.** Eén e-mailadres, aangemeld bij 40 tot 60 Nederlandse webshops. Aanmelden
   gebeurt in week 5; het corpus groeit vanaf dat moment vanzelf.
2. **Binnenhalen.** Ophalen via IMAP.
3. **Parsen.** HTML naar platte tekst, met subject en preheader apart bewaard.
4. **Embedden.** Chunken, embeddings, wegschrijven naar een lokale vector-DB.
5. **Gebruiken.** Clusteren en doorzoeken, met filtering op de metadata hieronder.

Publieke bron, eigen data. Geen klantdata en geen toestemming nodig.

## Geplande metadata per mail

| Veld | Inhoud |
|---|---|
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
