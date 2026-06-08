import requests
from datetime import datetime

api_key = "f4afa78cdd3a2c8b380d2359cbd9bedc"
stadt = input("Für welche Stadt willst du das Wetter wissen? ")

# 5-Tage-Forecast (alle 3 Stunden)
url = f"http://api.openweathermap.org/data/2.5/forecast?q={stadt}&units=metric&appid={api_key}&lang=de"
response = requests.get(url)
daten = response.json()

if daten["cod"] != "200":
    print("Stadt nicht gefunden. Bitte überprüfe die Schreibweise.")
    exit()

# Wir gruppieren die Daten nach Datum
forecast = {}
for eintrag in daten["list"]:
    datum = datetime.fromtimestamp(eintrag["dt"]).strftime("%Y-%m-%d")
    temp = eintrag["main"]["temp"]
    wetter = eintrag["weather"][0]["description"]
    
    if datum not in forecast:
        forecast[datum] = {"temps": [], "wetter": []}
    forecast[datum]["temps"].append(temp)
    forecast[datum]["wetter"].append(wetter)

# Ausgabe: min/max Temperatur pro Tag
for datum, info in forecast.items():
    temp_min = min(info["temps"])
    temp_max = max(info["temps"])
    wetter_haeufig = max(set(info["wetter"]), key=info["wetter"].count)
    print(f"{datum}: {temp_min:.1f}°C - {temp_max:.1f}°C, Wetter: {wetter_haeufig}")
    