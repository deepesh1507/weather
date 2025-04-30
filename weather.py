import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        print(f"\n🌤️ Weather in {city.capitalize()}:")
        print(f"🌡️ Temperature: {main['temp']}°C")
        print(f"💧 Humidity: {main['humidity']}%")
        print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
        print(f"📝 Description: {weather['description'].capitalize()}")
    else:
        print("❌ City not found or error fetching data.")

if __name__ == "__main__":
    api_key = "****************************"  # Replace with your actual API key
    city = input("🌆 Enter city name: ")
    get_weather(city, api_key)
