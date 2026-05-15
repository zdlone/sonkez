import os
from flask import Flask, redirect, Response
import yt_dlp

app = Flask(__name__)

def get_yt_link(video_url):
    # YouTube'un "Sen sunucusun" demesini engellemek için mobil taklidi yapıyoruz
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'quiet': True,
        'no_warnings': True,
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=False)
            # Eğer canlı yayınsa m3u8 linkini çek
            return info.get('url')
        except Exception as e:
            print(f"Hata: {e}")
            return None

@app.route('/')
def index():
    return "YouTube Streamer Aktif!"

@app.route('/live.m3u8')
def live():
    # Senin istediğin YouTube linki
    target_url = "https://www.youtube.com/watch?v=Jv8HS8gqV78"
    
    stream_url = get_yt_link(target_url)
    
    if stream_url:
        # 403 hatasını yememek için linke doğrudan yönlendirme yapıyoruz
        return redirect(stream_url)
    else:
        return "Yayin linki su an alınamıyor, YouTube engeli aktif.", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
