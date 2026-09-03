# Werkbank

Een werkomgeving waarin ik tools bouw voor e-mailmarketing en CRM-automatisering: Python,
LLM-API's, structured outputs, retrieval en evals. Elk project staat in een eigen map, draait,
en heeft een eigen README.

---

## Wat hier draait

| Project | Wat het doet | Technische kern |
|---|---|---|
| [**Expense tracker**](maand-1-fundament/projecten/expense-tracker/) | CLI-tool die uitgaven valideert, wegschrijft naar JSON en dag- en maandtotalen teruggeeft. Vangt vijf soorten kapotte input op zonder te crashen. | 62 regels · 5 unit tests · stdlib only |
| [**Bitcoin Price Index**](maand-1-fundament/cs50/Libraries/bitcoin/) | Haalt de live BTC-koers op via een externe API, met de key uit een environment variable in plaats van uit de code. | `requests` · JSON · `.env` |
| [**CS50P-opdrachten**](maand-1-fundament/cs50/) | 33 opgeloste opdrachten, college 0 t/m 6. | incl. 4 eigen testsuites |

---

## Waar wat staat

| Pad | Inhoud |
|---|---|
| [maand-1-fundament/](maand-1-fundament/) | Python, Git, terminal, API's, SQL |
| [maand-2-llm-apis/](maand-2-llm-apis/) | Prompting, structured outputs, tool calling, streaming · *subject line-checker · briefing naar campagnedocument* |
| [maand-3-rag-agents/](maand-3-rag-agents/) | RAG, vector-DB's, agents, evals · *nieuwsbrief-corpus · evals · signaalsplitser* |
| [maand-4-ship-it/](maand-4-ship-it/) | Builds draaibaar maken voor iemand anders: deployment, README, demo |
| [publiek/](publiek/) | README-templates voor de builds die als losse repo uitgerold worden |
| [ROADMAP.md](ROADMAP.md) | Het plan: doel, de twee regels, de vier valkuilen |
| [prompts/](prompts/) | De prompts waarmee ik mezelf laat begeleiden |
| [docs/](docs/) | Het werkoverzicht, één self-contained HTML-bestand |
| [notities/](notities/) | Losse aantekeningen en dingen om uit te zoeken |

Elke `projecten/`-map bevat de builds van die maand, elk project met een eigen README. Daarin
staat altijd een kopje "wat er nog niet goed aan is", door mij geschreven en niet weggepoetst.

---

## Licentie

[MIT](LICENSE). Pak eruit wat je kunt gebruiken. Naamsvermelding wordt gewaardeerd, maar hoeft niet.
