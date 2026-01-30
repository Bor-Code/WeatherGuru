🌤️ WeatherGuru - Akıllı Hava Durumu Paneli
WeatherGuru, Python ve Streamlit kullanılarak geliştirilmiş, modern ve kullanıcı dostu bir hava durumu takip uygulamasıdır. OpenWeatherMap API entegrasyonu sayesinde dünyanın her yerinden şehirler için sıcaklık, nem, rüzgar hızı ve hissedilen sıcaklık gibi detaylı atmosferik verileri anlık olarak sunar.

🚀 Canlı Demo
Uygulamayı tarayıcınızda hemen test edin:
👉 WeatherGuru Uygulamasını Başlat

✨ Özellikler
Anlık Veri Akışı: Dünyanın dört bir yanındaki şehirler için gerçek zamanlı hava durumu bilgisi
Kapsamlı Metrikler: Sıcaklık, hissedilen sıcaklık, nem oranı ve rüzgar hızı gibi detaylı bilgiler
Modern Tasarım: Streamlit ile tasarlanmış, hem masaüstü hem de mobil cihazlarda mükemmel çalışan şık arayüz
Akıllı Hata Yönetimi: Geçersiz şehir adları veya bağlantı sorunları için anlaşılır ve yardımcı geri bildirimler
Hızlı ve Güvenilir: Minimum gecikme ile verimli veri çekme

🛠️ Teknoloji Yığını
Programlama Dili: Python 3.10+
Framework: Streamlit
Hava Durumu API: OpenWeatherMap
Bağımlılıklar: requests, python-dotenv

💻 Yerel Kurulum
WeatherGuru'yu kendi bilgisayarınızda birkaç basit adımda çalıştırın:
1. Depoyu Klonlayın
bashgit clone https://github.com/Bor-Code/WeatherGuru.git
cd WeatherGuru
2. Bağımlılıkları Yükleyin
bashpip install -r requirements.txt
### 3. API Anahtarını Yapılandırın
Proje kök dizininde bir `.env` dosyası oluşturun ve OpenWeatherMap API anahtarınızı ekleyin:
OPENWEATHER_API_KEY=buraya_api_anahtariniz
Not: Ücretsiz API anahtarınızı OpenWeatherMap adresinden alabilirsiniz
4. Uygulamayı Başlatın
bashstreamlit run app.py
Uygulama otomatik olarak varsayılan tarayıcınızda http://localhost:8501 adresinde açılacaktır

Hazır olarak bakmak isterseniz linke tıklamanız yeterlidir: https://weatherguru-bor-code.streamlit.app/

🤝 Katkıda Bulunma
Katkılarınızı bekliyoruz! Şunları yapabilirsiniz:
Hata bildirimi yapma
Yeni özellikler önerme
Pull request gönderme

👤 Geliştirici
Bor-Code
GitHub: @Bor-Code
E-Mail: non.mrbora@gmail.com

------------------------------------------------------------------------------------------------------------------------------

🌤️ WeatherGuru - Smart Weather Dashboard
WeatherGuru is a modern and user-friendly weather tracking application developed using Python and Streamlit. Thanks to its OpenWeatherMap API integration, it provides real-time detailed atmospheric data such as temperature, humidity, wind speed, and perceived temperature for cities around the world.

🚀 Live Demo
Test the application in your browser right now:
👉 Launch WeatherGuru Application

✨ Features
Real-Time Data Stream: Real-time weather information for cities around the world
Comprehensive Metrics: Detailed information such as temperature, feels-like temperature, humidity, and wind speed
Modern Design: A sleek interface designed with Streamlit that works perfectly on both desktop and mobile devices
Smart Error Handling: Clear and helpful feedback for invalid city names or connection issues
Fast and Reliable: Efficient data retrieval with minimal latency

🛠️ Tech Stack
Programming Language: Python 3.10+
Framework: Streamlit
Weather API: OpenWeatherMap
Dependencies: requests, python-dotenv

💻 Local Setup
Run WeatherGuru on your own computer in a few simple steps:
1. Clone the Repository
bashgit clone https://github.com/Bor-Code/WeatherGuru.git
cd WeatherGuru
2. Install Dependencies
bashpip install -r requirements.txt
### 3. Configure the API Key
Create a `.env` file in the project root directory and add your OpenWeatherMap API key:
OPENWEATHER_API_KEY=your_api_key
Note: You can get your free API key from OpenWeatherMap
4. Run the Application
bashstreamlit run app.py
The application will automatically open in your default browser at http://localhost:8501

If you want to see it ready to go, just click the link: https://weatherguru-bor-code.streamlit.app/

🤝 Contribute
We welcome your contributions! You can:
Report bugs
Suggest new features
Submit pull requests

👤 Developer
Bor-Code
GitHub: @Bor-Code
Email: non.mrbora@gmail.com