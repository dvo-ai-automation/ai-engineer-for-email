# Nu

**Week 6 · do 3 sep – wo 9 sep 2026 · Maand 2 · Bouwen met LLM-API's**

Dit bestand bevat alleen de week waar je in zit. Als je 's ochtends één ding opent, is het dit.
Aan het eind van de week gooi je hem leeg en zet je de volgende week erin.

- **Eén bouwstap en één klusje per dag.** Gaat het goed, dan pak je de volgende dag naar voren;
  je vult de dag niet bij.
- **Elke bouwstap heeft een "klaar als".** Iets dat je op je scherm kunt zien. Staat het er, dan
  ben je klaar voor vandaag, ook als het half voelt.
- **Loopt een dag uit, dan schuift de rest op.** Zaterdag staat er expres voor.

---

## Het doel van deze week

Twee dingen, en aan allebei is aan het eind van de week te zien of het gelukt is:

1. **Het corpus verzamelt.** Een eigen mailbox, aangemeld bij 40+ webshops, en Python komt
   erbij. Vanaf dat moment groeit het vanzelf en hoef je er niets meer aan te doen.
2. **Je hebt vier getallen.** Hoeveel van die webshops staan op `p=none`, `quarantine`,
   `reject`, of hebben helemaal geen DMARC. Dat zijn de getallen waar je post van week 8 op rust.

Deze week komt er geen model aan te pas. Dat is opzet: dit is de deterministische helft van
build C, en het punt ervan is dat je zes dagen iets nuttigs bouwt zonder één API-call.

## Wat je deze week afvinkt

In het [dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/), tabblad Roadmap,
Maand 2:

- [ ] Blok **"Deterministisch of model"** — alle drie de taken *(het blok met het label Week 6)*
- [ ] **BUILD C · Authenticatie-scan**, de deterministische helft: opvragen, parsen, tellen

Verder niets. De blokken Prompting en Structured outputs staan gelabeld als Week 7 en Week 8;
daar begin je deze week niet aan.

## De post deze week

**Er gaat niets live.** Wel twee dingen van vijf minuten die woensdag klaarstaan:

- Post 1 (*wat levert een journey eigenlijk op*) als concept in de LinkedIn-editor → gaat live in **week 7**
- De oude expense-tracker-post editen → één zin, zie woensdag

De getallen die je dinsdag meet, worden **post 2 in week 8**. Je schrijft hem deze week nog niet.

---

## Do 3 sep

**Bouwen · verbinding met de mailbox**
Maak een apart e-mailadres aan dat alleen voor het corpus bestaat, zet IMAP aan, en schrijf een
script van vijftien regels dat verbindt en het aantal mails in de inbox print.

> **Klaar als:** er een getal in je terminal staat en geen foutmelding. Welk getal maakt niet uit.
> Het punt is dat de verbinding staat — dat is de moeilijkste stap van maand 3, en die werkt dan nu al.

> ⚠️ **Waar je een halve dag aan kunt verliezen:** de meeste providers laten je niet met je gewone
> wachtwoord via IMAP naar binnen. Je hebt een app-wachtwoord nodig (bij Gmail: eerst
> tweestapsverificatie aan, dan een app-wachtwoord aanmaken). Loopt het vast op inloggen en niet
> op je code, zoek dan daar. Dat wachtwoord gaat in `.env`, nooit in je script.

**Klusje · aanmelden, ronde 1**
10 Nederlandse webshops. Noteer per aanmelding **twee** dingen in `domeinen.txt`, gescheiden door
een puntkomma: de merknaam zoals jij hem zou noemen, en het kale domein —
`Voorbeeld;voorbeeld.nl`, niet `https://www.voorbeeld.nl/`.

Die merknaam lijkt overbodig omdat hij in het domein zit. Straks mailt dezelfde webshop je vanaf
drie afzenderadressen en telt hij als drie merken in je druk-analyse. Vijf seconden nu, een dag
uitzoekwerk later.

*Leert je: niets uit de roadmap — dit is de voorbereiding waar maand 3 volledig op rust.*

## Vr 4 sep

**Bouwen · kijken wat je binnenhaalt**
Draai het script van gisteren nog een keer; er staat nu een hoger getal. Print één mail
ongefilterd uit en zoek er twee dingen in op: de `Message-ID`-header en de `From`-header.

> **Klaar als:** je de `Message-ID` kunt aanwijzen en je hebt gezien hoe onleesbaar HTML-mail is.
> Die eerste is straks je sleutel om te voorkomen dat dezelfde mail twee keer in je corpus komt.
> Dat tweede is precies waarom stap 3 van het corpus bestaat.

**Klusje · aanmelden, ronde 2**
15 webshops erbij, zelfde notatie. `domeinen.txt` staat op 25 regels.

*Leert je: de metadata-eisen uit het corpus-README — `message_id` als dubbelcheck, `merk` uit de afzender.*

## Za 5 sep

Inhaaldag. Staat er iets open van do of vr, dan doe je dat. Staat er niets open, dan is dit een
vrije dag. Je begint hier niet aan iets nieuws.

## Zo 6 sep

**Bouwen · één DNS-lookup**
Vraag van één domein uit je lijst het SPF-record op en print het. `dnspython`. Dit is dezelfde
vorm als de weather CLI: ophalen, uitpakken, printen — alleen is de bron nu DNS in plaats van HTTP.

> **Klaar als:** er een regel met `v=spf1` in je terminal staat.

**Klusje · aanmelden, ronde 3**
10 webshops erbij. `domeinen.txt` staat op 35 regels.

*Leert je: roadmap-taak "Herken wat een opzoeking is en wat een oordeel is" — een DNS-record zegt
wat het zegt, daar hoort geen model bij.*

## Ma 7 sep

**Bouwen · de hele lijst langs**
Lees `domeinen.txt` in (splits elke regel op de puntkomma), vraag per domein SPF én DMARC op,
schrijf het resultaat naar `records.json`. Vang af: domein bestaat niet, geen record aanwezig,
time-out.

> **Klaar als:** `records.json` net zoveel regels heeft als je domeinlijst en er geen traceback op
> je scherm staat. Domeinen zonder record horen erin te staan als leeg, niet te ontbreken.

**Klusje · aanmelden afmaken**
De laatste 5 tot 10. Je zit dan op 40+ en de aanmeldklus is klaar voor de rest van het traject.

*Leert je: roadmap-taak "Vang de faalgevallen van een lookup af".*

## Di 8 sep

**Bouwen · het getal**
Parse uit elk DMARC-record de policy: `p=none`, `p=quarantine` of `p=reject`. Tel hoeveel er in
elke categorie vallen, plus hoeveel domeinen helemaal geen DMARC hebben.

> **Klaar als:** je vier getallen hebt die optellen tot het aantal domeinen in je lijst. Doen ze
> dat niet, dan is er een lookup stilletjes mislukt.

**Klusje · geen.** Dit is de zwaarste dag van de week. Hou hem leeg.

*Leert je: roadmap-taak "Ken de drie DMARC-policies". Hiermee is het blok Week 6 af.*

## Wo 9 sep

**Bouwen · vastleggen**
Geen nieuwe code. Schrijf de vier getallen op mét de meetdatum, en vul het kopje "wat er nog niet
goed aan is" in `projecten/authenticatie-scan/README.md` in.

> **Klaar als:** iemand anders je README kan lezen en weet wat je gemeten hebt en wanneer.

Let op hoe je het opschrijft: je hebt **authenticatie** gemeten, geen deliverability. Reputatie,
engagement, bounces en lijsthygiëne zitten er niet in. Claim wat je gemeten hebt — dat is het
eerste waar iemand uit het vak je anders op pakt. En zonder meetdatum is een DNS-uitkomst niet te
citeren, want DNS verandert.

**Klusje · LinkedIn, twee keer vijf minuten**
Zet post 1 als concept in de editor (publiceren volgende week). En pas in je oude
expense-tracker-post de zin *"drie weken geleden schreef ik mijn eerste regel Python"* aan naar de
framing die verderop in diezelfde post al staat: je bouwt al langer automatiseringen, alleen niet
met eigen code. Editen, niet verwijderen.

*Leert je: je eigen repo-regel — elk project heeft een eerlijk kopje over wat er nog niet aan deugt.*

---

## Waar je hierna staat

Eén regel per week. Verder vooruit kijk je niet.

| Week | Waar je aan werkt | Wat er live gaat |
|---|---|---|
| **7** · 10–16 sep | Structured outputs: een Pydantic-schema op je records, zodat er per domein een risico-oordeel in vaste vorm uitkomt. Plus je eerste promptronde (v1 kaal tegen v2 specifiek) — juist hier, want een DMARC-record heeft een objectief goed antwoord, dus je ziet meteen of je prompt beter werd. | **Post 1** |
| **8** · 17–23 sep | De subject-checker, met hetzelfde schemapatroon. Promptronde 2: v1 t/m v5 over twintig regels uit je corpus. Dat zijn je vijf bewaarde versies, de nulmeting voor maand 3. | **Post 2**, met de getallen van 8 september |
| **9** · vanaf 24 sep | Maand 3 opent: embeddings en de vector-DB op het corpus dat dan drie weken heeft staan verzamelen. | — |

Alles daarna: [ROADMAP.md](ROADMAP.md) en het [dashboard](https://dvo-ai-automation.github.io/ai-engineer-for-email/). Niet vandaag.
