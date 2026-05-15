import os
from flask import Flask, redirect
import yt_dlp

app = Flask(__name__)

def youtube_link_coz(video_url):
    # YouTube'un bot olduğumuzu anlamaması için ek ayarlar
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'source_address': '0.0.0.0', # IPv4 zorlaması
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Sadece linki al, tüm veriyi indirmeye çalışma (hızlıdır)
            info = ydl.extract_info(video_url, download=False)
            if 'url' in info:
                return info['url']
            elif 'formats' in info:
                # Canlı yayınlarda m3u8 formatını bul
                for f in info['formats']:
                    if f.get('protocol') == 'm3u8_native' or '.m3u8' in f.get('url', ''):
                        return f['url']
        return None
    except Exception as e:
        print(f"Hata: {e}")
        return None

@app.route('/live.m3u8')
def youtube_yayin():
    # TEST İÇİN: Buradaki linki kopyalayıp tarayıcıda açtığından emin ol!
    hedef_yt_url = "https://www.youtube.com/watch?v=Jv8HS8gqV78" 
    
    guncel_link = youtube_link_coz(hedef_yt_url)
    
    if guncel_link:
        print("Link basariyla cozuldu!")
        return redirect(guncel_link)
    
    return "YouTube engeline takildik veya yayin kapali. Lutfen 1 dakika sonra tekrar dene.", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
