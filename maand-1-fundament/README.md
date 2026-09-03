# Maand 1: Python en de plumbing

**30 juli – 26 augustus 2026**

**Doel:** een functionele Python-developer worden die een API kan aanroepen, een klein project
kan beheren en niet meer hoeft te googelen op basissyntax. Niet expert. Functioneel.

> AI engineering is éérst software engineering. Als deze laag wankelt, wordt de AI-laag nooit betrouwbaar.

Volledige uitwerking: [tabblad Roadmap in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/) · [ROADMAP.md](../ROADMAP.md)

## Resources (één pick per skill, niet gaan shoppen)

- Python: **CS50P** · https://cs50.harvard.edu/python
- Git & GitHub: **GitHub Skills** · https://skills.github.com
- Terminal: korte beginnerscursus, daarna erin leven (MIT "Missing Semester" als je dieper wilt: https://missing.csail.mit.edu)
- API's/HTTP: **MDN HTTP overview** · https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview + **Python `requests` docs** · https://requests.readthedocs.io/en/latest/
- SQL: **SQLBolt** · https://sqlbolt.com

## Dagelijks gereedschap

[Prompt 1: Python Learning Partner](../prompts/01-python-learning-partner.md).
Laat het uitleggen, jíj typt.

## Weekplanning

*Maand 1 is afgerond op 26 augustus 2026. Voor waaróm dit niet gelijkloopt met de
CS50P-colleges, en hoe diep je per college moet gaan: [CS50P: volgorde en diepte](https://dvo-ai-automation.github.io/ai-engineer-4-months/).*

- [x] **Week 1 (30 jul – 5 aug)**: setup afronden · CS50P: variabelen, condities, loops, functies
- [x] **Week 2 (6 – 12 aug)**: CS50P: collections, file handling, JSON · een week lang alles via de terminal
  - Gedaan: Exceptions (4/4) · start Libraries
- [x] **Week 3 (13 – 19 aug)**: CS50P: exceptions, venv/pip · build de CLI-tool
  - Gedaan: Libraries (6/6) · Unit Tests (4/4) · File I/O (4/4) · CS50P t/m college 6 af
  - Gedaan: **de expense tracker** werkt, mét 5 unit tests · venv en pip in de praktijk gebruikt
- [x] **Week 4 (20 – 26 aug)**: HTTP/API's/`requests` · build het API-script · SQLBolt
  - Gedaan: **de weather CLI**, V1 t/m V4 met een eigen README · wat een HTTP-request is en de statuscodes · SQLBolt · GitHub Skills

## Builds

- [x] [`projecten/expense-tracker/`](projecten/expense-tracker/): CLI-tool die naar JSON leest en schrijft. **Af op 20 aug**: 62 regels code, 5 unit tests, vangt vijf soorten kapotte input op. [Lees de README →](projecten/expense-tracker/README.md)
- [x] [`projecten/weather-cli/`](projecten/weather-cli/): script dat de Open-Meteo API (geen key nodig, https://open-meteo.com/en/docs) aanroept en schoon print. Vier versies bewaard, van hardgecodeerde coördinaten tot statuscode-checks. [Lees de README →](projecten/weather-cli/README.md)

## Milestone

- [x] Python-programma dat bestanden leest/schrijft, een API aanroept en zijn eigen errors afhandelt zonder crash
- [x] Code geversioneerd met Git en live in een GitHub-repo, inclusief branches en een merge
- [x] Zonder aarzelen door de terminal bewegen
- [x] Uitleggen wat een HTTP-request is en er één maken in Python
- [x] Een basis-SQL-query draaien
