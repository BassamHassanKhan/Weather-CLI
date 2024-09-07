import requests
import sys

# API Key for OpenWeatherMap (replace with your own)
API_KEY = 'your_openweather_api_key'

# Base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(city_name):
    """
    Fetches weather data for a given city from the OpenWeatherMap API.
    
    Args:
        city_name (str): The name of the city for which to fetch the weather.
    
    Returns:
        None: Prints the weather information to the console.
    """
    # Complete API URL with the city name and API key
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name

    # Send a GET request to the API
    response = requests.get(complete_url)

    # Parse the JSON response
    data = response.json()

    # If the response code is 404, the city was not found
    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather_description = data["weather"][0]["description"]

        # Print the weather details
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main['temp']} K")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
        print(f"Description: {weather_description}")
    else:
        # If the city is not found, print a message
        print("City not found!")


if __name__ == "__main__":
    """
    Main function that runs when the script is executed.
    
    - Expects a city name as a command-line argument.
    - If no city name is provided, prompts the user to enter one.
    """
    if len(sys.argv) > 1:
        city_name = sys.argv[1]
        get_weather(city_name)
    else:
        print("Please provide a city name.")
