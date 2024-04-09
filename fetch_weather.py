import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_weather():
    api_key = '8817bc03068298401e5b13fd86c78801'
    lat = '47.60'
    lon = '122.33'
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'imperial'
    }
    try:
        response = requests.get(base_url, params=parameters, timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info(data)
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        logging.error(f'Error occurred: {err}')

if __name__ == "__main__":
    while True:
        fetch_weather()
        time.sleep(3600)  # Fetch weather data every hour

