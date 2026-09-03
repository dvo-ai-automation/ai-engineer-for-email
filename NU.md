# Nu

**Week 6 · do 3 sep – wo 9 sep 2026 · Maand 2**

Dit bestand bevat alleen de week waar je in zit. Niet de maand, niet het traject. Als je
's ochtends één ding opent, is het dit. Aan het eind van de week gooi je hem leeg en zet je
de volgende week erin.

Regels voor dit bestand:

- **Eén bouwstap en één klusje per dag.** Meer plan je niet in, ook niet als het goed gaat.
  Gaat het goed, dan pak je de volgende dag naar voren; je vult de dag niet bij.
- **Elke bouwstap heeft een "klaar als".** Dat is een ding dat je op je scherm kunt zien.
  Staat het er, dan ben je klaar voor vandaag, ook als het half voelt.
- **Loopt een dag uit, dan schuift de rest op.** Je haalt niets in door twee dagen in één te doen.
  De zaterdag staat er expres voor.

---

## Deze week in één zin

Het corpus moet gaan verzamelen (dat kan niet ingehaald worden), en dezelfde lijst webshops
levert meteen de data voor je eerste post met een echt getal erin.

---

## Do 3 sep

**Bouwen · verbinding met de mailbox**
Maak een apart e-mailadres aan dat alleen voor het corpus bestaat, zet IMAP aan, en schrijf
een script van vijftien regels dat verbindt en het aantal mails in de inbox print.

> **Klaar als:** er een getal in je terminal staat en geen foutmelding. Welk getal maakt niet
> uit — heb je al aangemeld, dan staan de eerste welkomstmails er misschien al in. Het punt is
> dat de verbinding staat: dat is de moeilijkste stap van maand 3, en die werkt dan nu al.

> ⚠️ **Waar je een halve dag aan kunt verliezen:** de meeste providers laten je niet met je
> gewone wachtwoord via IMAP naar binnen. Je hebt een app-wachtwoord nodig (bij Gmail: eerst
> tweestapsverificatie aan, dan een app-wachtwoord aanmaken). Loopt het vast op inloggen en niet
> op je code, zoek dan daar. En dat wachtwoord gaat in `.env`, nooit in je script.

**Klusje · aanmelden, ronde 1**
Meld je aan bij 10 Nederlandse webshops. Noteer per aanmelding **twee** dingen in
`domeinen.txt`, gescheiden door een puntkomma: de merknaam zoals jij hem zou noemen, en het
kale domein — `Voorbeeld;voorbeeld.nl`, niet `https://www.voorbeeld.nl/`.

De merknaam lijkt overbodig omdat hij in het domein zit. Dat is hij niet: straks mailt dezelfde
webshop je vanaf drie verschillende afzenderadressen, en dan telt hij als drie merken in je
druk-analyse. Nu opschrijven kost je vijf seconden per shop; later uitzoeken kost je een dag.

---

## Vr 4 sep

**Bouwen · niets nieuws**
Draai het script van gisteren nog een keer. Er staat nu een hoger getal. Kijk hoe één zo'n mail
eruitziet als je hem uitprint. Niet parsen, alleen kijken.

Zoek in die uitdraai twee dingen op: de `Message-ID`-header, en de `From`-header. De eerste is
straks je sleutel om te voorkomen dat dezelfde mail twee keer in je corpus komt. De tweede is
waarom je gisteren die merknaam apart opschreef — kijk of het afzenderadres eruitziet als iets
waar je automatisch het merk uit kunt afleiden.

> **Klaar als:** je één ruwe mail hebt gezien, je de `Message-ID` eruit kunt aanwijzen, en je
> weet hoe onleesbaar HTML-mail is. Dat laatste is precies waarom stap 3 van het corpus bestaat.

**Klusje · aanmelden, ronde 2**
15 webshops erbij, in dezelfde `merk;domein`-notatie. `domeinen.txt` staat nu op 25 regels.

---

## Za 5 sep

Inhaaldag. Staat er iets van do of vr open, dan doe je dat. Staat er niets open, dan is dit
een vrije dag. Je begint hier niet aan iets nieuws.

---

## Ma 7 sep

**Bouwen · één DNS-lookup**
Vraag van één domein uit je lijst het SPF-record op en print het. Gebruik `dnspython`.
Dit is dezelfde vorm als de weather CLI: ophalen, uitpakken, printen.

> **Klaar als:** er een regel met `v=spf1` in je terminal staat.

**Klusje · aanmelden, ronde 3**
15 webshops erbij. `domeinen.txt` staat nu op 40 regels. Hiermee is de aanmeldklus klaar.

---

## Di 8 sep

**Bouwen · de hele lijst langs**
Lees `domeinen.txt` in (splits elke regel op de puntkomma), vraag per domein SPF én DMARC op,
schrijf het resultaat naar `records.json`. Vang af: domein bestaat niet, geen record aanwezig,
time-out.

> **Klaar als:** `records.json` net zo veel regels heeft als je domeinlijst, en er geen
> traceback op je scherm staat. Domeinen zonder record horen erin te staan als leeg,
> niet te ontbreken.

**Klusje · geen**
Deze dag is de zwaarste van de week. Hou hem leeg.

---

## Wo 9 sep

**Bouwen · het getal**
Parse uit elk DMARC-record de policy: `p=none`, `p=quarantine` of `p=reject`. Tel hoeveel
er in elke categorie vallen, plus hoeveel domeinen helemaal geen DMARC hebben.

> **Klaar als:** je vier getallen hebt die optellen tot het aantal domeinen in je lijst.
> **Dit zijn de getallen uit je post van week 8.** Schrijf ze op met de datum erbij — DNS
> verandert, dus zonder meetdatum is een uitkomst niet te citeren.

Let op hoe je dit straks opschrijft: je hebt **authenticatie** gemeten, niet deliverability.
Reputatie, engagement, bounces en lijsthygiëne zitten hier niet in. Claim wat je gemeten hebt,
anders is dat het eerste waar iemand uit het vak je op pakt.

**Klusje · LinkedIn**
Twee dingen, allebei vijf minuten. Zet het concept uit `notities/linkedin-posts.md` in de
LinkedIn-editor en laat hem daar staan; publiceren doe je volgende week. En pas in je oude
expense-tracker-post de zin "drie weken geleden schreef ik mijn eerste regel Python" aan naar
de framing die verderop in diezelfde post al staat. Editen, niet verwijderen.

---

## Waar dit heen gaat

Zodat je weet waarom je dit doet, in één regel per week. Verder vooruit kijk je niet.

| Week | Wat |
|---|---|
| **7** (10–16 sep) | Je records door een model halen met een Pydantic-schema erop: het structured-outputs-blok, geoefend op data die je al hebt. Post 1 gaat live. |
| **8** (17–23 sep) | De subject-checker met hetzelfde schemapatroon, plus de vijf promptversies v1 t/m v5 over twintig regels uit je corpus. Post 2 gaat live met de getallen van 9 september. |

Alles daarna: [ROADMAP.md](ROADMAP.md) en het [dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/). Niet vandaag.
