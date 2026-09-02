import requests
import json
import os
import datetime

def extract_air_quality() -> dict:
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": 40.4165,
        "longitude": -3.7026,
        "hourly": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone",
        "current": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone",
        "timezone": "auto"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    data["_metadata"] = {
        "extracted_at": datetime.datetime.now().isoformat(),
        "source": "open-meteo-air-quality",
    }

    return data

def save_raw_data(data: dict, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Datos de calidad del aire guardados en {output_path}")

def main() -> None:
    output_file = "data/raw/air_quality_raw.json"

    try:
        raw_data = extract_air_quality()
        save_raw_data(raw_data, output_file)
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

    