import requests

END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
weather_api = 
parameters = {
        "lat": 51.51,
        "lon": 19.00,
        "appid": weather_api,
        "exclude": "current, minutely, daily",
}
#weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid={weather_api}")
weather_response = requests.get(END_POINT, params=parameters)

weather_response.raise_for_status()

print(weather_response.json())

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#Doc making a call
#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
