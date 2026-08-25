# De programmeerkant onder mijn AI-werk

Ik bouw al twee jaar AI- en automationoplossingen voor e-mailmarketing. Sinds 30 juli 2026 haal ik
de programmeerkant eronder op: Python, API's, structured outputs, RAG, agents en evals — zelf
kunnen bouwen, repareren en meten wat ik nu samenstel. Alles wat ik onderweg bouw staat in deze
repo, de werkende dingen en de lelijke, op de dag dat ze af zijn.

Geen cursus die ik verkoop, geen samenvatting achteraf. Een logboek dat meeloopt.

### ▶ [Bekijk het interactieve dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/)

Voortgang per skill, de bouwopdrachten, de valkuilen en de mijlpalen van alle vier de maanden.

---

## Wat je hier aan hebt

**Haal je de programmeerkant onder je eigen werk op?** Dan is dit een uitgeschreven plan met de
resources er al bij uitgekozen, plus een eerlijk beeld van hoe lang dingen echt duren. Het
[dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/) is te kopiëren en de
[ROADMAP](ROADMAP.md) vertelt je welke vier fouten dit soort trajecten meestal beëindigen.
In [`prompts/`](prompts/) staan de prompts waarmee ik mezelf laat begeleiden in plaats van
antwoorden te laten voorzeggen.

**Wil je zien of ik kan bouwen?** Begin bij de tabel hieronder. Elk project draait, heeft een
eigen README met een demo, en vertelt aan het eind zelf wat er nog niet aan deugt.

**Beoordeel je code?** Bij elk project staan de tussenversies (`V1` t/m `V4`). Daaraan zie je
niet alleen wat ik kan, maar hoe snel het gaat.

---

## Wat er nu werkt

| Project | Wat het doet | Bewijs |
|---|---|---|
| [**Expense tracker**](maand-1-fundament/projecten/expense-tracker/) | CLI-tool die uitgaven valideert, wegschrijft naar JSON en dag- en maandtotalen teruggeeft. Vangt vijf soorten kapotte input op zonder te crashen. | 62 regels · 5 unit tests · stdlib only |
| [**Bitcoin Price Index**](maand-1-fundament/cs50/Libraries/bitcoin/) | Haalt de live BTC-koers op via een externe API, met de key uit een environment variable in plaats van uit de code. | `requests` · JSON · `.env` |
| [`maand-1-fundament/cs50/`](maand-1-fundament/cs50/) | 33 opgeloste CS50P-opdrachten, college 0 t/m 6. | incl. 4 eigen testsuites |

---

## Waar ik nu sta

**Maand 1: Python en de plumbing** · week 4 van 4 · *bijgewerkt 21 aug 2026*

| | |
|---|---|
| **Af** | CS50P college 0 t/m 6 · de expense tracker, inclusief tests · Git met branches en merges |
| **Nu bezig** | De weather CLI: een script dat de Open-Meteo API aanroept en het antwoord schoon print |
| **Daarna** | Wat een HTTP-request fysiek ís · statuscodes · SQL-basis · dan maand 2 |

De vier maanden lopen van 30 juli t/m 18 november 2026, bij 15–25 uur per week.

---

## Waar wat staat

| Pad | Inhoud |
|---|---|
| [maand-1-fundament/](maand-1-fundament/) | Python, Git, terminal, API's, SQL · **nu bezig** |
| [maand-2-llm-apis/](maand-2-llm-apis/) | Prompting, structured outputs, tool calling, streaming · *subject line-evaluator · briefing naar campagnedocument* |
| [maand-3-rag-agents/](maand-3-rag-agents/) | RAG, vector-DB's, agents, evals · *RAG over ESP-docs · evals op de evaluator · monitoring-agent* |
| [maand-4-ship-it/](maand-4-ship-it/) | De twee beste builds deployen, met README en demo |
| [ROADMAP.md](ROADMAP.md) | Het plan: doel, de twee regels, de vier valkuilen |
| [prompts/](prompts/) | De prompts waarmee ik mezelf laat begeleiden |
| [docs/](docs/) | Het dashboard hierboven, één self-contained HTML-bestand |
| [notities/](notities/) | Losse aantekeningen en dingen om uit te zoeken |

Elke `projecten/`-map bevat de builds van die maand, elk project met een eigen README.

---

## De twee regels waar alles op rust

1. **De 30-minutenregel**: per uur kijken of lezen minstens 30 minuten bouwen zónder tutorial open.
2. **Alles gaat publiek**: elk project op GitHub op de dag dat het af is, ook de lelijke.

De tweede is de moeilijkste en de belangrijkste. Daarom staat in elke project-README een kopje
"wat er nog niet goed aan is", door mij geschreven en niet weggepoetst.

---

## Bron

De structuur (de skills per maand, de twee regels, de vier valkuilen) komt uit een artikel van
@free_ai_guides, 7 juli 2026 · https://x.com/i/article/2074513567701680128. De bouwopdrachten van
maand 2 t/m 4 zijn van mezelf en komen uit mijn eigen vak; zie [ROADMAP.md](ROADMAP.md#over-de-bron).

Vragen, of ben je met hetzelfde bezig? Open gerust een [issue](https://github.com/dvo-ai-automation/ai-engineer-4-months/issues).

## Licentie

[MIT](LICENSE). Pak eruit wat je kunt gebruiken. Kopieer de roadmap, fork het dashboard,
leen de projectopzet. Naamsvermelding wordt gewaardeerd, maar hoeft niet.
