# import streamlit as st
# import requests

# st.set_page_config(page_title="Weather App", page_icon="⛅")
# st.title("🌤️ Simple Weather App")

# # Input from user
# city = st.text_input("City ka naam likhiye:")

# # Replace with your own OpenWeatherMap API key
# API_KEY = "375e97fab7dfa1ebf77ebda920e6fa6c"

# def get_weather(city_name):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "City": data["name"],
#             "Temperature (°C)": data["main"]["temp"],
#             "Weather": data["weather"][0]["description"].title(),
#             "Humidity (%)": data["main"]["humidity"],
#             "Wind Speed (km/h)": round(data["wind"]["speed"] * 3.6, 2)
#         }
#     else:
#         return None

# if city:
#     weather = get_weather(city)
#     if weather:
#         st.success(f"Weather in {weather['City']}:")
#         st.metric("🌡️ Temperature", f"{weather['Temperature (°C)']} °C")
#         st.write(f"☁️ Condition: {weather['Weather']}")
#         st.write(f"💧 Humidity: {weather['Humidity (%)']}%")
#         st.write(f"🌬️ Wind: {weather['Wind Speed (km/h)']} km/h")
#     else:
#         st.error("City naam sahi se likhiye ya network check kariye.")

##

import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="⛅")

# Set background image using custom HTML & CSS
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://cdn.pixabay.com/photo/2021/01/11/08/53/sky-5907605_1280.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🌤️ Simple Weather App")

city = st.text_input("Enter the city name:")

# Use your OpenWeatherMap API key
API_KEY = "375e97fab7dfa1ebf77ebda920e6fa6c"

def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": data["name"],
            "Temperature": data["main"]["temp"],
            "Weather": data["weather"][0]["description"].title(),
            "Icon": data["weather"][0]["icon"],
            "Humidity": data["main"]["humidity"],
            "Wind Speed": round(data["wind"]["speed"] * 3.6, 2)
        }
    else:
        return None

if city:
    weather = get_weather(city)
    if weather:
        st.success(f"Weather in {weather['City']}")
        
        icon_url = f"http://openweathermap.org/img/wn/{weather['Icon']}@2x.png"
        st.image(icon_url, width=100)

        st.metric("🌡️ Temperature", f"{weather['Temperature']} °C")
        st.write(f"☁️ Condition: {weather['Weather']}")
        st.write(f"💧 Humidity: {weather['Humidity']}%")
        st.write(f"🌬️ Wind Speed: {weather['Wind Speed']} km/h")
    else:
        st.error("City not found. Please check the name or try again.")
