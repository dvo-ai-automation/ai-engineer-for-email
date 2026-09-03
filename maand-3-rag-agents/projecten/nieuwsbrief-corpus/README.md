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

**Let op wat je hier eigenlijk aan het doen bent.** Eén webshop mailt vanaf drie verschillende
afzenderadressen en telt dan als drie merken. Dezelfde mail komt twee keer binnen. `type` moet
consistent toegekend worden of je telling klopt niet. Dat normaliseren, dedupliceren en
classificeren is datamodellering — dezelfde vaardigheid als het opschonen van een
contactendatabase, alleen op een schaal die in één maand past. Het is het enige stuk van dat
onderwerp dat in dit traject zit; de rest staat in "Na dit traject" in
[ROADMAP.md](../../../ROADMAP.md).

## De drie analyses

Zodra de mails erin zitten, zijn dit geen nieuwe builds maar queries over metadata die je toch
al opslaat. Ze dekken drie onderwerpen die in mijn vak zwaar wegen en die de generieke roadmap
niet kent.

- [ ] **E-maildruk.** Groeperen op `merk` en `datum` en tellen: hoe vaak mailt elk merk je, over
      welke periode. Echte verzendfrequentie van de ontvangende kant, zonder klantdata. Geen
      model nodig. Dit is de opening van de post van week 10–11: een getal dat iedereen voelt,
      vóór de clustering die eerst uitleg nodig heeft.
- [ ] **Lifecycle, voor zover waarneembaar.** Elke aanmelding triggert een welkomstflow, dus je
      hebt gratis wat 50 webshops sturen in de eerste dertig dagen: hoeveel mails, in welke
      volgorde, welk `type`. Cart, post-purchase en winback zou je moeten uitlokken bij vijftig
      shops; dat past niet in deze maand. Blijf bij het moment dat je toch al observeert.
- [ ] **Clustering.** Waar de embeddings voor waren: welke groepen vallen er vanzelf uit, en
      welke had je niet verwacht. De clusters die niets bleken te betekenen horen er ook in.

## De vraag-antwoordlaag

Klein, binnen deze build, en het is de plek waar grounding en citaties landen — zonder deze
laag is die mijlpaal van maand 3 niet verdiend.

- [ ] Een vraag als "welke merken stuurden in november gratis-verzending-mails" geeft een
      antwoord **met de mails eronder waar het uit blijkt**
- [ ] Metadata-filtering en reranking zitten hierin: breed ophalen, terugscoren naar de mails
      die de bewering echt staven
- [ ] Elke bewering uit de post van week 10–11 gaat hier eerst doorheen. Kan de laag hem niet
      staven met echte mails, dan gaat de bewering eruit

Dat laatste punt is de reden dat deze laag bestaat. Het is mijn eigen regel — geen getal dat ik
niet gemeten heb — afgedwongen in code in plaats van in goede bedoelingen.

## Wat het oplevert

De labelset voor de evals (build B) komt hieruit, en de checker uit maand 2 draait erop.

## Wat er nog niet goed aan is

*Nog niets gebouwd. Dit kopje vullen zodra er iets draait.*
