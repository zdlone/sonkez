import os
from flask import Flask, redirect
import yt_dlp

app = Flask(__name__)

def youtube_link_coz(video_url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return info.get('url')
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

@app.route('/live.m3u8')
def youtube_yayin():
    # Buradaki linkin canlı ve doğru olduğundan emin ol!
    hedef_yt_url = "https://www.youtube.com/watch?v=Jv8HS8gqV78" 
    
    guncel_link = youtube_link_coz(hedef_yt_url)
    
    if guncel_link:
        return redirect(guncel_link)
    return "Yayin su an aktif degil veya link hatali. Kod yt-dlp ile cozulemedi.", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
