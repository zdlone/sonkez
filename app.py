import os
from flask import Flask, redirect
import subprocess

app = Flask(__name__)

def youtube_link_coz(video_url):
    try:
        # yt-dlp ile YouTube'un ham m3u8 linkini çekiyoruz
        komut = ["yt-dlp", "-g", "-f", "best", video_url]
        guncel_link = subprocess.check_output(komut).decode("utf-8").strip()
        return guncel_link
    except Exception as e:
        print(f"Hata: {e}")
        return None

@app.route('/live.m3u8')
def youtube_yayin():
    # İZLEMEK İSTEDİĞİN YOUTUBE LİNKİNİ BURAYA YAPIŞTIR
    hedef_yt_url = "https://www.youtube.com/watch?v=Jv8HS8gqV78" 
    
    guncel_link = youtube_link_coz(hedef_yt_url)
    
    if guncel_link:
        # Seni YouTube'un o anki taze linkine fırlatır
        return redirect(guncel_link)
    return "Yayin su an aktif degil veya link hatali", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
