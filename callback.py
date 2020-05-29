import youtube_dl

with youtube_dl.YoutubeDL() as ydl:
    ydl.extract_info("https://www.viki.com/videos/1154058v-hotel-del-luna-episode-1", download=False)
