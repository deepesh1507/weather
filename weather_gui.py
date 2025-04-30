import tkinter as tk
from tkinter import ttk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # OpenWeatherMap API key (replace with your own)
        self.api_key = "9223d19a9a11570febce512f9d40e296"  # Get from openweathermap.org

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # City input
        self.city_label = ttk.Label(self.main_frame, text="Enter City:")
        self.city_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.city_entry = ttk.Entry(self.main_frame, width=30)
        self.city_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Search button
        self.search_button = ttk.Button(self.main_frame, text="Get Weather", command=self.display_weather)
        self.search_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Weather display labels
        self.city_display = ttk.Label(self.main_frame, text="City: ", font=("Arial", 14))
        self.city_display.grid(row=2, column=0, columnspan=2, pady=5)

        self.temp_display = ttk.Label(self.main_frame, text="Temperature: ", font=("Arial", 12))
        self.temp_display.grid(row=3, column=0, columnspan=2, pady=5)

        self.condition_display = ttk.Label(self.main_frame, text="Condition: ", font=("Arial", 12))
        self.condition_display.grid(row=4, column=0, columnspan=2, pady=5)

        self.humidity_display = ttk.Label(self.main_frame, text="Humidity: ", font=("Arial", 12))
        self.humidity_display.grid(row=5, column=0, columnspan=2, pady=5)

        self.wind_display = ttk.Label(self.main_frame, text="Wind: ", font=("Arial", 12))
        self.wind_display.grid(row=6, column=0, columnspan=2, pady=5)

    def display_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            self.city_display.config(text="City: Please enter a city")
            return

        # Construct API URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        
        try:
            # Make API request
            response = requests.get(url)
            data = response.json()

            # Check if request was successful
            if data["cod"] != 200:
                self.city_display.config(text=f"City: {data['message'].capitalize()}")
                return

            # Extract weather data
            city_name = data["name"]
            temperature = f"{round(data['main']['temp'])}°C"
            condition = data["weather"][0]["description"].capitalize()
            humidity = f"{data['main']['humidity']}%"
            wind = f"{round(data['wind']['speed'] * 3.6)} km/h"  # Convert m/s to km/h

            # Update GUI labels
            self.city_display.config(text=f"City: {city_name}")
            self.temp_display.config(text=f"Temperature: {temperature}")
            self.condition_display.config(text=f"Condition: {condition}")
            self.humidity_display.config(text=f"Humidity: {humidity}")
            self.wind_display.config(text=f"Wind: {wind}")

        except requests.RequestException:
            self.city_display.config(text="City: Network error, try again")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()