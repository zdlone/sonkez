import os
from flask import Flask, redirect, request
import requests
import re

app = Flask(__name__)

def link_kaziyici(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # YouTube'un yeni m3u8 formatını yakalar
        match = re.search(r'hlsManifestUrl":"([^"]+)"', response.text)
        if match:
            return match.group(1).replace(r'\/', '/')
    except:
        return None
    return None

@app.route('/live.m3u8')
def youtube_yayin():
    # TEST İÇİN DEĞİŞTİRDİM: TRT HABER CANLI (YouTube'un en stabil yayınıdır)
    # Eğer bu çalışırsa, kendi linkinle değiştirirsin.
    varsayilan_url = "https://www.youtube.com/watch?v=9uVpT7NidS0"
    
    link = link_kaziyici(varsayilan_url)
    
    if link:
        return redirect(link)
    
    return "Sistem Calisiyor Ama YouTube Linki Vermiyor. Lutfen Farkli Bir Kanal Deneyin.", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
