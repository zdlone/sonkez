import os
from flask import Flask, redirect
import yt_dlp

app = Flask(__name__)

def link_bul(video_url):
    # YouTube'un engellememesi için gelişmiş ayarlar
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # YouTube'un botları anlamaması için rastgele tarayıcı bilgisi
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Senin attığın linki burada işliyoruz
            info = ydl.extract_info(video_url, download=False)
            if 'url' in info:
                return info['url']
    except Exception as e:
        print(f"Hata: {e}")
        return None

@app.route('/live.m3u8')
def youtube_yayin():
    # BURAYA SANA AİT YOUTUBE LİNKİNİ YAPIŞTIR
    senin_linkin = "https://www.youtube.com/watch?v=Jv8HS8gqV78" 
    
    taze_link = link_bul(senin_linkin)
    
    if taze_link:
        # Sunucu taze linki buldu, şimdi kullanıcıyı oraya gönderiyor
        return redirect(taze_link)
    
    return "Link su an yakalanamadi, YouTube engeli olabilir.", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
