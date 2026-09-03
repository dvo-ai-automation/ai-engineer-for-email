# Evals voor de subject line-checker

Houdt de checker tegen een set gelabelde subject lines en meet per veld uit het schema hoe vaak
hij het goed heeft. Draait meerdere promptversies tegen dezelfde set, zodat je kunt zien welke
versie wint en met hoeveel in plaats van dat je het aanneemt.

## Hoe je het draait

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Eén versie meten:

```bash
python eval.py --set testset.jsonl --prompt prompts/<versie>.md
```

Alle versies naast elkaar:

```bash
python eval.py --set testset.jsonl --prompt-dir prompts/ --vergelijk
```

De testset is een JSONL met per regel de input en het handmatig toegekende label. Labelen gaat
vóór draaien: label je nadat je de output hebt gezien, dan meet je je eigen bevestiging.

## Wat de output is

Per promptversie een score per veld, plus het totaal:

```
Promptversie: <naam>          n = <aantal gelabelde regels>

  veld                     goed      score
  weergave.afkap_tekens    <n>/<n>   <p>%
  preheader.body_eet       <n>/<n>   <p>%
  emoji.fallback           <n>/<n>   <p>%
  ----------------------------------------
  totaal                   <n>/<n>   <p>%
```

Met `--vergelijk` komt daar een tabel bij met alle versies onder elkaar en het verschil ten
opzichte van de basisversie. `--fouten` schrijft de gevallen weg die misgingen, met input,
verwacht label en wat het model teruggaf.

## Beperkingen

- **De score geldt tegen deze set, niet in het algemeen.** Hij zegt hoe vaak de prompt het eens
  is met hoe ik heb gelabeld op deze regels. Waar de labels vandaan komen en hoe ze getrokken
  zijn, staat in `testset.md`.
- **Eén labeler.** Er is geen tweede persoon die onafhankelijk gelabeld heeft, dus er is geen
  maat voor hoe eenduidig de labels zijn. Bij twijfelgevallen telt mijn interpretatie.
- **Alleen velden met een eenduidig goed antwoord.** Wat niet objectief te labelen is, zit niet
  in de set en wordt dus ook niet gemeten.
- **De set is klein.** Bij dit aantal regels zijn kleine verschillen tussen promptversies niet
  te onderscheiden van toeval. Het verschil dat je nodig hebt voor een uitspraak staat in
  `testset.md`.

## Wat er nog niet goed aan is

- <wat er kapotgaat, waar de labels wringen, wat je zou overdoen>
