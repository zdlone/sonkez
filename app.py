import os
from flask import Flask, redirect
import requests
import re

app = Flask(__name__)

def link_yakala():
    # YouTube yerine koruması daha zayıf olan alternatif bir yayın sitesi
    # Bu site genellikle m3u8 linklerini açık bırakır
    url = "https://yayin.canlitv.center/cartoon-network" 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        # Sayfa içindeki gizli .m3u8 linkini bulur
        match = re.search(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', r.text)
        if match:
            return match.group(0)
    except:
        return None
    return None

@app.route('/')
def home():
    return "Sunucu Aktif! Yayini izlemek icin /live.m3u8 ekleyin."

@app.route('/live.m3u8')
def youtube_yayin():
    guncel_link = link_yakala()
    if guncel_link:
        return redirect(guncel_link)
    
    # Eğer yukarıdaki patlarsa yedek bir sabit m3u8 (Test amaçlı)
    return redirect("https://canlitv.center/cartoon-network/live.m3u8")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
