import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/live.m3u8')
def youtube_yayin():
    # Video ID: Jv8HS8gqV78
    video_id = "Jv8HS8gqV78"
    
    # YouTube doğrudan m3u8 API linki
    manifest_url = f"https://www.youtube.com/api/manifest/hls_variant/id/{video_id}/source/yt_live_broadcast/master.m3u8"
    
    return redirect(manifest_url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
