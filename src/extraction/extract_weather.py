import datetime
import json
import os
import pathlib

import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 40.4165,
    "longitude": -3.7026,
    "hourly": "temperature_2m,precipitation_probability,wind_speed_10m",
    "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
    "timezone": "auto"
}

def extract_weather() -> dict:
    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    data["_metadata"] = {
        "extracted_at": datetime.datetime.now().isoformat(),
        "source": "open-meteo",
    }

    return data

def save_raw_data(data: dict, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main() -> None:
    output_file = "data/raw/weather_raw.json"

    try:
        raw_data = extract_weather()
        save_raw_data(raw_data, output_file)
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
