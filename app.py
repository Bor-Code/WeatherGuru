import streamlit as st
import requests
import os
from dotenv import load_dotenv
st.set_page_config(page_title="WeatherGuru", page_icon="🌤️", layout="centered")

# API Anahtarını Getir
try:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except:
    load_dotenv()
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    response = requests.get(base_url, params=params)
    return response

#Arayüz
st.title("🌤️ WeatherGuru")
st.write("Şehir ismini gir, anlık hava durumunu görün.")

# Arama
city_input = st.text_input("Şehir Adı:", placeholder="Örn: Istanbul, Konya, London")
if st.button("Hava Durumunu Getir") and city_input:
    with st.spinner('Veriler çekiliyor...'):
        response = get_weather_data(city_input)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            st.success(f"{city_input.capitalize()} için hava durumu başarıyla alındı!")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Sıcaklık", value=f"{main['temp']} °C", delta=f"Hissedilen: {main['feels_like']} °C")           
            with col2:
                st.metric(label="Nem", value=f"%{main['humidity']}")         
            with col3:
                st.metric(label="Rüzgar", value=f"{wind['speed']} m/s")
            st.info(f"Genel Durum: **{weather['description'].upper()}**")          
        else:
            st.error("❌ Şehir bulunamadı! Lütfen ismi kontrol et.")

# Alt bilgi
st.markdown("---")
st.caption("WeatherGuru | Python & Streamlit ile geliştirildi.")
st.caption("Developed by [Bor-Code]")