import streamlit as st
import random

def fetch_weather_data(city):
    # Simulate weather data
    weather_conditions = [
        {"description": "clear sky"},
        {"description": "few clouds"},
        {"description": "scattered clouds"},
        {"description": "rain"},
        {"description": "thunderstorm"},
        {"description": "snow"},
    ]
    return {
        "main": {
            "temp": round(random.uniform(15, 35), 1),
            "humidity": random.randint(30, 90)
        },
        "weather": [random.choice(weather_conditions)],
        "wind": {
            "speed": round(random.uniform(1, 10), 1)
        }
    }

def main():
    st.title("Weather Updates App")
    
    city = st.text_input("Enter city name:")
    
    if st.button("Get Weather"):
        if city:
            weather_data = fetch_weather_data(city)
            if weather_data:
                st.subheader(f"Weather in {city}")
                st.write(f"Temperature: {weather_data['main']['temp']}°C")
                st.write(f"Weather: {weather_data['weather'][0]['description']}")
                st.write(f"Humidity: {weather_data['main']['humidity']}%")
                st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
            else:
                st.error("Could not fetch weather data. Please try again.")
        else:
            st.warning("Please enter a city name.")

if __name__ == "__main__":
    main()