import os
from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return "GitHub Hybrid Sistem Aktif! Yayini izlemek icin /live.m3u8 ekleyin."

@app.route('/live.m3u8')
def live():
    # Senin bilgilerine göre doldurulmuş bağlantı
    GITHUB_RAW_URL = "https://raw.githubusercontent.com/zdlone/sonkez/main/link.txt"
    
    try:
        # GitHub Actions tarafından oluşturulan link.txt dosyasını okuyoruz
        r = requests.get(GITHUB_RAW_URL, timeout=5)
        if r.status_code == 200:
            m3u8_link = r.text.strip()
            # GitHub'dan gelen gerçek YouTube m3u8 linkine yönlendiriyoruz
            return redirect(m3u8_link)
    except Exception as e:
        print(f"Hata oluştu: {e}")
    
    return "Link henüz hazır değil veya yenileniyor. Lütfen 30 saniye sonra tekrar dene.", 503

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
