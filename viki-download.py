from __future__ import unicode_literals
import youtube_dl


while True:
    ep1 = input('Copy + paste the URL of the FIRST episode of the series:\n')
    try:
        epUrl = ep1[ep1.index('videos/') + 7:]
        break
    except:
        print('Not a valid URL. The URL should be in the following format:\nhttps://www.viki.com/videos/XXXXXXXv-name-of-drama-episode-XX')

epTag = int(epUrl[:epUrl.index('v-')])
epName = epUrl[epUrl.index('v-') + 2 : epUrl.index('episode-') - 1]

epList = []
while True:
    epNumber = input("List the episode(s) you wish to download in one of the following formats:\n1. Separated by commas, e.g. 1,2,3\n2. Give a range of episodes separated by a dash, e.g 1-3\n")
    try:
        if '-' in epNumber:
            start = int(epNumber[:epNumber.index('-')])
            end = int(epNumber[epNumber.index('-') + 1:])
            for i in range(start, end + 1):
                epList.append('https://www.viki.com/videos/' + str(epTag - 1 + i) + 'v-' + epName + '-episode-' + str(i))
        elif ',' in epNumber:
            epNumber = list(epNumber)
            epNumberList = []
            for x in epNumber:
                if x != ' ' and x != ',':
                    epNumberList.append(int(x))
            for x in epNumberList:
                epList.append('https://www.viki.com/videos/' + str(epTag - 1 + x) + 'v-' + epName + '-episode-' + str(x))
        else:
            epList.append('https://www.viki.com/videos/' + str(epTag - 1 + int(epNumber)) + 'v-' + epName + '-episode-' + epNumber)
        break
    except:
        print('Not a valid list of episodes')

sub = False
subLang = 'en'
while True:
    subIn = input('Download subtitles? [y/n]\n')
    if subIn == 'y':
        sub = True
        while True:
            subLangIn = input('English, Simplified Chinese, or Indonesian? [e/c/i]\n')
            if subLangIn == 'e':
                break
            elif subLangIn == 'c':
                subLang = 'zh'
                break
            elif subLangIn == 'i':
                subLang = 'id'
                break
            else:
                print('Invalid input\n')
        break
    elif subIn == 'n':
        break
    else:
        print('Invalid input')




ydl_opts = {"writesubtitles": sub, "subtitleslangs": [subLang]}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(epList)
