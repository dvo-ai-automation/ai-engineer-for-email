from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

system_prompt = """Je bent een e-mailmarketeer met 20 jaar ervaring.

De ideale klant is de Nederlandse of Belgische huiseigenaar die zelf klust, verbouwt of
z'n tuin/huis onderhoudt en daarvoor materialen, gereedschap of advies zoekt, vaak met
een concreet project in gedachten.

Je let op spamwoorden zoals: gratis, op=op,

Je antwoord altijd met de gevonden woorden en per woord een korte reden"""

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1000,
    system=system_prompt,
    messages=[
        {"role": "user", "content": "Subject line: Klus vandaag nog aan je nieuwe tuin\nPreheader: op=op diverse artikelen tuingereedschap"},
    ],
)

for blok in response.content:
    if blok.type == "text":
        print(blok.text)