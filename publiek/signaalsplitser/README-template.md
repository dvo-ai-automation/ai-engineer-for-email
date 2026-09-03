# Signaalsplitser

Detecteert twee soorten problemen in een tijdreeks van campagnecijfers en houdt ze strikt
gescheiden: "stuk" is deterministisch (er is niets verstuurd, de aantallen staan op nul, de feed
is leeg), "minder" is statistisch (een daling boven een drempel, met een minimumvolume en een
voortschrijdend gemiddelde eronder). Die twee door één drempel halen is de gangbare fout in
alerting: je mist storingen, of je leert mensen je meldingen weg te klikken.

## Hoe je het draait

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Op een eigen reeks:

```bash
python splits.py --reeks <pad naar csv> --config drempels.yaml
```

Op gegenereerde testdata:

```bash
python maak_reeks.py --weken <n> --storing week:<n> --daling week:<n>,pct:<n> > test.csv
python splits.py --reeks test.csv --config drempels.yaml
```

Er zit geen ESP-koppeling in. De input is een CSV met per periode een volume en een uitkomst;
wat je daarin stopt bepaal je zelf.

## Wat de output is

Per periode nul of meer signalen, met het type erbij:

```
<periode>  STUK    <reden: geen verzending | volume nul | lege feed>
<periode>  MINDER  daling <p>% t.o.v. voortschrijdend gemiddelde over <n> perioden
                   volume <n> (minimum <n>) · drempel <p>%
<periode>  —       geen signaal
```

Een STUK-signaal heeft geen drempel en geen marge: de voorwaarde geldt of hij geldt niet. Een
MINDER-signaal noemt altijd het volume waarop hij gebaseerd is, zodat je kunt zien of het om
ruis gaat.

## Beperkingen

- **Synthetische data.** Wat hier in de repo zit is gegenereerd, geen echte campagnedata. De
  drempels zijn daarop afgestemd en zeggen niets over jouw reeksen tot je ze zelf hebt geijkt.
- **Geen ESP-adapters.** De tool leest een CSV. Het ophalen bij een ESP, en het overzicht van
  journeys daarboven, zit hier niet in en is geen omissie maar een grens.
- **Een voortschrijdend gemiddelde gaat mee met een langzame daling.** Zakt iets over vele
  perioden geleidelijk weg, dan schuift de referentie mee en meldt de tool niets. Dat is een
  bekende eigenschap van deze methode, geen bug.
- **Seizoen zit er niet in.** Een reeks met een sterk seizoenspatroon geeft signalen op
  momenten waarop de daling verwacht was.
- **Eén reeks tegelijk.** Geen correlatie tussen reeksen, dus een storing die tien campagnes
  raakt geeft tien losse meldingen.

## Wat er nog niet goed aan is

- <wat er kapotgaat, welke vals-positieven je overhoudt, wat je zou overdoen>
