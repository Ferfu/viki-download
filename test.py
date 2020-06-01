import youtube_dl

url = "viki.com/tv/36424c-my-id-is-gangnam-beauty"

ydl_options = {
    "playlist_items": "1, 3, 3",
    "writesubtitles": True,
    "subtitleslangs": ['en'],
}
with youtube_dl.YoutubeDL(ydl_options) as ydl:
    ydl.download([url])
