from __future__ import unicode_literals
import youtube_dl

# login
while True:
    login = input('\nLogin? [y/n]\n')
    if login == 'y':
        login = True
        break
    elif login == 'n':
        login = False
        break
    else:
        print('\nInvalid input\n')

if login:
    username = input('\nUsername: ')
    password = input('\Password: ')

# playlist url
while True:
    url = input('\nEnter the URL of the HOME PAGE of the series (e.g. https://www.viki.com/tv/36667c-hotel-del-luna):\n')
    try:
        with youtube_dl.YoutubeDL({"playliststart": 0, "playlistend": 0, "quiet": True}) as ydl:
            ydl.extract_info(url, download=False)
        break
    except:
        print("\nInvalid URL\n")

# episodes
while True:
    ep = input("\nEnter the first and last episodes to download separated by a space (e.g. 1 16)\n")
    try:
        start, end = [int(x) for x in ep.split()]
        break
    except:
        print('\nInvalid input\n')

# subtitles
while True:
    downloadSubs = input("\nDownload subtitles? [y/n]\n")
    if downloadSubs == "y":
        downloadSubs = True
        break
    elif downloadSubs == "n":
        downloadSubs = False
        break
    else:
        print("\nInvalid input\n")
if downloadSubs == True:
    with youtube_dl.YoutubeDL({"playliststart": end, "playlistend": end, "listsubtitles": True}) as ydl:
        ydl.extract_info(url, download=False)
    subLang = input("\nEnter subtitle language. Note some subtitle langauges are not available for all episodes.\n")

options = {
    "username": username,
    "password": password,
    "writesubtitles": downloadSubs,
    "subtitleslangs": [subLang],
    "playliststart": start,
    "playlistend": end
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])
