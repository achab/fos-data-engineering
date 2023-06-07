import json
import time

import requests


def get_list_of_cities():
    # read the file cities.json and returns its content.
    # Example: this function should return ["Algiers", "Batna", "Tamanrasset"]
    with open("cities.json", "r") as f:
        cities = json.load(f)
    return cities

def get_lat_lon(city):
    # get latitude and longitude data of cities in Algeria 
    # using the API documented here: https://nominatim.org/release-docs/latest/api/Search/
    # Example: this function should return 36.6875, 3.125
    url = f"https://nominatim.openstreetmap.org/search?city={city}&country=Algeria&format=json"
    res = requests.get(url).json()
    lat = res[0]["lat"]
    lon = res[0]["lon"]
    return lat, lon

def get_current_weather(lat, lon):
    # get current weather data at (latitude, longitude)
    # using the API documented here: https://open-meteo.com/
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    resp = requests.get(url).json()
    return resp

def get_weather_all_cities(cities):
    data = dict()
    for city in cities:
        lat, lon = get_lat_lon(city)
        res = get_current_weather(lat, lon)
        data[city] = res
    return data

def save_output_data(data_):
    unix_timestamp = int(time.time())
    output_filename = f"raw_data_{unix_timestamp}.json"
    with open(output_filename, "w") as f:
        json.dump(data_, f)

def main():
    cities = get_list_of_cities()
    weather_data = get_weather_all_cities(cities)
    save_output_data(weather_data)


if __name__ == "__main__":
    main()
