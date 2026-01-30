import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("⚠️ HATA: API anahtarı bulunamadı! .env dosyanızı kontrol edin.")
    exit()

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    try:
        response = requests.get(base_url, params=params, timeout=5)
        data = response.json()
        # Şehri bulursa
        if response.status_code == 200:
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            wind_speed = data['wind']['speed']
            desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            return (f"🌤️ {city_name.capitalize()} için hava: {desc}\n"
                    f"🌡️ Sıcaklık: {temp}°C (Hissedilen: {feels_like}°C)\n"
                    f"💧 Nem: %{humidity}\n"
                    f"💨 Rüzgar: {wind_speed} m/s") 
        # Bulamazsa
        elif response.status_code == 404:
            return "❌ Şehir bulunamadı, lütfen ismini kontrol et."  
        # Geçersiz API
        elif response.status_code == 401:
            return "🔑 API anahtarı geçersiz!"   
        # Hata Kodu
        else:
            return f"❌ Hata kodu: {response.status_code}"
    except requests.Timeout:
        return "⏱️ İstek zaman aşımına uğradı, tekrar deneyin."
    except Exception as e:
        return f"⚠️ Bir hata oluştu: {e}"

def start_bot():
    print("--- WeatherGuru Botuna Hoş Geldin! 🌍 ---")
    print("Çıkmak için 'E' tuşuna basabilirsin.\n")
    
    while True:
        city = input("Hava durumunu öğrenmek istediğiniz şehri girin: ").strip()        
        if city.upper() == 'E':
            print("Görüşmek üzere!! 👋\n")
            break     
        if not city:
            print("⚠️ Lütfen bir şehir adı girin!\n")
            continue      
        print("🔄 Veri çekiliyor...")
        result = get_weather(city)
        print("-" * 50)
        print(result)
        print("-" * 50 + "\n")

if __name__ == "__main__":
    start_bot()