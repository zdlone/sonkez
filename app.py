import os
from flask import Flask, redirect, request
import requests
import re

app = Flask(__name__)

def youtube_m3u8_bul(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
    }
    try:
        # YouTube sayfasını iPhone gibi çekiyoruz (daha az korumalıdır)
        response = requests.get(url, headers=headers, timeout=15)
        # Sayfa içindeki m3u8 linkini arıyoruz
        match = re.search(r'hlsManifestUrl":"(https:[^"]+)"', response.text)
        if match:
            m3u8_url = match.group(1).replace(r'\/', '/')
            return m3u8_url
    except Exception as e:
        print(f"Hata: {e}")
    return None

@app.route('/live.m3u8')
def youtube_yayin():
    # TEST: Bu linkin canlı olduğundan emin ol (Kral FM Canlı Yayın örneği)
    hedef_yt_url = "https://www.youtube.com/watch?v=Jv8HS8gqV78" 
    
    # Eğer linki tarayıcıdan göndermek istersen: /live.m3u8?url=YOUTUBE_LINKI
    user_url = request.args.get('url')
    final_url = user_url if user_url else hedef_yt_url
    
    link = youtube_m3u8_bul(final_url)
    
    if link:
        return redirect(link)
    
    return "YouTube hala engel koyuyor. Başka bir kanal linki deneyin veya 5 dk bekleyin.", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
