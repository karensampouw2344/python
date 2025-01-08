import requests

# Function to fetch weather data
def get_weather(city, api_key):
    # OpenWeatherMap API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    # Make a GET request to fetch weather data
    response = requests.get(base_url, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()

        # Extract weather details
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Print the weather details
        print(f"\nWeather in {city_name}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found. Please check the city name and try again.")

# Main function to run the app
def weather_app():
    print("Welcome to the Weather App!")
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

    while True:
        city = input("\nEnter the city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye! Stay safe.")
            break
        get_weather(city, api_key)

# Run the app
if __name__ == "__main__":
    weather_app()
