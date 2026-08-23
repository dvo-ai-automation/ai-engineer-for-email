import requests
import json

r = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=knmi_seamless&forecast_days=3"
)

data = r.json()
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