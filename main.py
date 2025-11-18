import sys
import platform
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını proje kökünden yükler

def main():
    print("Hello from sipgiris !")
    print("Python sürümü:", platform.python_version())
    print("Detaylı sürüm (sys.version):", sys.version)

    # .env'den değişkenleri oku (varsayılanlar belirtildi)
    app_name = os.getenv("APP_NAME", "sipgiris")
    app_version = os.getenv("APP_VERSION", "1.0.0")
    debug = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes", "on")
    print(f"Uygulama Adı: {app_name}")
    print(f"Uygulama Sürümü: {app_version}")
    print(f"Hata Ayıklama Modu: {debug}")

   

if __name__ == "__main__":
    main()
