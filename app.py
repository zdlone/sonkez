import os
from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route('/live.m3u8')
def youtube_yayin():
    # TRT HABER Video ID: 9uVpT7NidS0
    # Bu yöntem, YouTube'un video ID'sini kullanarak doğrudan API üzerinden link oluşturur
    video_id = "9uVpT7NidS0" 
    
    # YouTube linklerini çözen ücretsiz ve sağlam bir dış servis (API) kullanıyoruz
    # Bu sayede Render'ın IP engeline takılmayız.
    api_url = f"https://youtube-hls-service.vercel.app/api/get-hls?id={video_id}"
    
    try:
        # Dış servisten m3u8 linkini çekiyoruz
        r = requests.get(api_url, timeout=10)
        if r.status_code == 200:
            m3u8_link = r.json().get('url')
            if m3u8_link:
                return redirect(m3u8_link)
    except:
        pass
    
    # Alternatif 2: Eğer API çalışmazsa doğrudan yönlendirme dene
    return redirect(f"https://www.youtube.com/watch?v={video_id}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
