import os
from flask import Flask, redirect, Response
import yt_dlp

app = Flask(__name__)

def link_ayikla(video_url):
    # YouTube engelini aşmak için profesyonel ayarlar
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # YouTube'a "Ben iPhone kullanan bir insanım" diyoruz
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        # Sunucu IP'sini gizlemek için bazı gelişmiş yt-dlp hileleri
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'geo_bypass': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Video bilgilerini al
            info = ydl.extract_info(video_url, download=False)
            # Canlı yayın m3u8 linkini döndür
            return info.get('url')
        except Exception as e:
            return None

@app.route('/')
def ana_sayfa():
    return "YouTube Çözücü Aktif! /live.m3u8 adresine git."

@app.route('/live.m3u8')
def live():
    # beIN SPORTS HABER veya senin istediğin ID
    video_id = "i7UpPgxfZZ8"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    
    print(f"İşlem başlıyor: {youtube_url}")
    m3u8_link = link_ayikla(youtube_url)
    
    if m3u8_link:
        # redirect yerine bazen doğrudan linki yazdırmak Playerlar için daha iyidir
        # Ama kolaylık olsun diye şimdilik yönlendiriyoruz
        return redirect(m3u8_link)
    else:
        return "Hata: YouTube sunucu IP'sini engelledi veya link hatalı.", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
