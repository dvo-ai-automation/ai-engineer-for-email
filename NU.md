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

> **Klaar als:** er `0` in je terminal staat. Dat is de bedoeling — de inbox is leeg.
> Je hebt dan bewezen dat de moeilijkste stap van maand 3 nu al werkt.

**Klusje · aanmelden, ronde 1**
Meld je aan bij 10 Nederlandse webshops. Noteer per aanmelding het domein in `domeinen.txt`,
één per regel, kaal (`voorbeeld.nl`, niet `https://www.voorbeeld.nl/`).

---

## Vr 4 sep

**Bouwen · niets nieuws**
Draai het script van gisteren nog een keer. Er staat nu waarschijnlijk geen `0` meer.
Kijk hoe één zo'n mail eruitziet als je hem uitprint. Niet parsen, alleen kijken.

> **Klaar als:** je één ruwe mail in je terminal hebt gezien en je weet hoe onleesbaar
> HTML-mail is. Dat is precies waarom stap 3 van het corpus bestaat.

**Klusje · aanmelden, ronde 2**
15 webshops erbij. `domeinen.txt` staat nu op 25 regels.

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
Lees `domeinen.txt` in, vraag per domein SPF én DMARC op, schrijf het resultaat naar
`records.json`. Vang af: domein bestaat niet, geen record aanwezig, time-out.

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
> **Dit zijn de getallen uit je post van week 8.** Schrijf ze op met de datum erbij.

**Klusje · post 1**
Zet het concept uit `notities/linkedin-posts.md` in de LinkedIn-editor en laat hem daar staan.
Publiceren doe je volgende week.

---

## Waar dit heen gaat

Zodat je weet waarom je dit doet, in één regel per week. Verder vooruit kijk je niet.

| Week | Wat |
|---|---|
| **7** (10–16 sep) | Je records door een model halen met een Pydantic-schema erop: het structured-outputs-blok, geoefend op data die je al hebt. Post 1 gaat live. |
| **8** (17–23 sep) | De subject-checker, met hetzelfde schemapatroon dat je in week 7 al een keer hebt gebouwd. Post 2 gaat live, met de getallen van 9 september erin. |

Alles daarna: [ROADMAP.md](ROADMAP.md) en het [dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/). Niet vandaag.
