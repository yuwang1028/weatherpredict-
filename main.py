import requests


def fetch_weather(city):
    api_key = "068442a68d0a03dc0db6ce5e94e6d46e"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


def display_weather(weather_data):
    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Temperature: {temperature}°C")
        print(f"Climatic Conditions: {description}")
    else:
        print("City not found. Please enter a valid city name.")


def main():
    city = input("Enter the city name: ")
    weather_data = fetch_weather(city)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
