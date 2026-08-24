import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Geef een plaatsnaam op tussen aanhalingstekens")

plaatsnaam = sys.argv[1]
try:
    r = requests.get(
    f"https://geocoding-api.open-meteo.com/v1/search?name={plaatsnaam}&count=10&language=en&format=json", timeout=5   
    )
except (requests.exceptions.Timeout, requests.ConnectionError):
    sys.exit("API-call timed out")
if r.status_code != 200:
    sys.exit("API werkt niet")

plaats = r.json()

try:
    latitude = plaats["results"][0]["latitude"]
    longitude = plaats["results"][0]["longitude"]
except KeyError:
    sys.exit("plaatsnaam bestaat niet")
    
try:
    w = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&models=knmi_seamless&forecast_days=3", timeout=5
    )
except (requests.exceptions.Timeout, requests.ConnectionError):
    sys.exit("API-call timed out")
if w.status_code != 200:
    sys.exit("API werkt niet")

data = w.json()


vandaag = data["hourly"]["time"][17]
datum_vandaag = vandaag.split("T")
temp = data["hourly"]["temperature_2m"][17]
morgen = data["hourly"]["time"][41]
datum_morgen = morgen.split("T")
temp_morgen = data["hourly"]["temperature_2m"][41]
overmorgen = data["hourly"]["time"][65]
datum_overmorgen = overmorgen.split("T")
temp_overmorgen = data["hourly"]["temperature_2m"][65]

celsius = data["hourly_units"]["temperature_2m"]

weer = [
    {"tijd": datum_vandaag[0], "temperatuur": temp},
    {"tijd": datum_morgen[0], "temperatuur": temp_morgen},
    {"tijd": datum_overmorgen[0], "temperatuur": temp_overmorgen},
]
with open('weer.json', 'r') as lezen:
    data = json.load(lezen)
    data.extend(weer)
with open('weer.json', 'w') as schrijven:
    json.dump(data, schrijven, indent=2)

print(f"De temperatuur was vandaag {temp}{celsius}. Morgen wordt het {temp_morgen}{celsius} en overmorgen {temp_overmorgen}{celsius}")