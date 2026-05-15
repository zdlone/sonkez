// Not: Sketchware Java 1.7 isteğini unutmuyorum ama bu kod Render (Python) için.
import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/live.m3u8')
def youtube_yayin():
    # Sadece Video ID'sini kullanıyoruz (watch?v= kısmından sonraki 11 hane)
    # Senin attığın linkin ID'si: Jv8HS8gqV78
    video_id = "Jv8HS8gqV78"
    
    # YouTube'un engellemediği doğrudan API yönlendirmesi
    # Bu link sunucu üzerinden değil, YouTube'un kendi CDN'i üzerinden çalışır
    manifest_url = f"https://www.youtube.com/api/manifest/hls_variant/id/{video_id}/source/yt_live_broadcast/master.m3u8"
    
    # Bu linki doğrudan yönlendiriyoruz
    return redirect(manifest_url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
