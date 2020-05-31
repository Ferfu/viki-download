from __future__ import unicode_literals
import youtube_dl
import threading
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os

langDict = {'aa': 'Afar', 'ab': 'Abkhazian', 'ae': 'Avestan', 'af': 'Afrikaans', 'ak': 'Akan', 'am': 'Amharic', 'an': 'Aragonese', 'ar': 'Arabic', 'as': 'Assamese', 'av': 'Avaric', 'ay': 'Aymara', 'az': 'Azerbaijani', 'ba': 'Bashkir', 'be': 'Belarusian', 'bg': 'Bulgarian', 'bh': 'Bihari', 'bm': 'Bambara', 'bi': 'Bislama', 'bn': 'Bengali', 'bo': 'Tibetan', 'br': 'Breton', 'bs': 'Bosnian', 'ca': 'Catalan', 'ce': 'Chechen', 'ch': 'Chamorro', 'co': 'Corsican', 'cr': 'Cree', 'cs': 'Czech', 'cu': 'Church', 'cv': 'Chuvash', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'dv': 'Divehi', 'dz': 'Dzongkha', 'ee': 'Ewe', 'el': 'Greek', 'en': 'English', 'eo': 'Esperanto', 'es': 'Spanish', 'et': 'Estonian', 'eu': 'Basque', 'fa': 'Persian', 'ff': 'Fulah', 'fi': 'Finnish', 'fj': 'Fijian', 'fo': 'Faroese', 'fr': 'French', 'fy': 'Western', 'ga': 'Irish', 'gd': 'Gaelic', 'gl': 'Galician', 'gn': 'Guarani', 'gu': 'Gujarati', 'gv': 'Manx', 'ha': 'Hausa', 'he': 'Hebrew', 'hi': 'Hindi', 'ho': 'Hiri', 'hr': 'Croatian', 'ht': 'Haitian', 'hu': 'Hungarian', 'hy': 'Armenian', 'hz': 'Herero', 'ia': 'Interlingua', 'id': 'Indonesian', 'ie': 'Interlingue', 'ig': 'Igbo', 'ii': 'Sichuan', 'ik': 'Inupiaq', 'io': 'Ido', 'is': 'Icelandic', 'it': 'Italian', 'iu': 'Inuktitut', 'ja': 'Japanese', 'jv': 'Javanese', 'ka': 'Georgian', 'kg': 'Kongo', 'ki': 'Kikuyu', 'kj': 'Kuanyama', 'kk': 'Kazakh', 'kl': 'Kalaallisut', 'km': 'Central', 'kn': 'Kannada', 'ko': 'Korean', 'kr': 'Kanuri', 'ks': 'Kashmiri', 'ku': 'Kurdish', 'kv': 'Komi', 'kw': 'Cornish', 'ky': 'Kirghiz', 'la': 'Latin', 'lb': 'Luxembourgish', 'lg': 'Ganda', 'li': 'Limburgan', 'ln': 'Lingala', 'lo': 'Lao', 'lt': 'Lithuanian', 'lu': 'Luba-Katanga', 'lv': 'Latvian', 'mg': 'Malagasy', 'mh': 'Marshallese', 'mi': 'Maori', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mn': 'Mongolian', 'mne': 'Montenegrin ', 'mo': 'Moldavian', 'mr': 'Marathi', 'ms': 'Malay', 'mt': 'Maltese', 'my': 'Burmese', 'na': 'Nauru', 'nb': 'Bokmål,', 'nd': 'Ndebele,', 'ne': 'Nepali', 'ng': 'Ndonga', 'nl': 'Dutch', 'nn': 'Norwegian', 'no': 'Norwegian', 'nr': 'Ndebele,', 'nv': 'Navajo', 'ny': 'Chichewa', 'oc': 'Occitan', 'oj': 'Ojibwa', 'om': 'Oromo', 'or': 'Oriya', 'os': 'Ossetian', 'pa': 'Panjabi', 'pi': 'Pali', 'pl': 'Polish', 'ps': 'Pushto', 'pt': 'Portuguese', 'qu': 'Quechua', 'rm': 'Romansh', 'rn': 'Rundi', 'ro': 'Romanian', 'ru': 'Russian', 'rw': 'Kinyarwanda', 'sa': 'Sanskrit', 'sc': 'Sardinian', 'sd': 'Sindhi', 'se': 'Northern', 'sg': 'Sango', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'sm': 'Samoan', 'sn': 'Shona', 'so': 'Somali', 'sq': 'Albanian', 'sr': 'Serbian', 'ss': 'Swati', 'sh': 'Serbo-Croatian', 'st': 'Sotho,', 'su': 'Sundanese', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'tg': 'Tajik', 'th': 'Thai', 'ti': 'Tigrinya', 'tk': 'Turkmen', 'tl': 'Tagalog', 'tn': 'Tswana', 'to': 'Tonga', 'tr': 'Turkish', 'ts': 'Tsonga', 'tt': 'Tatar', 'tw': 'Twi', 'ty': 'Tahitian', 'ug': 'Uighur', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 've': 'Venda', 'vi': 'Vietnamese', 'vo': 'Volapük', 'wa': 'Walloon', 'wo': 'Wolof', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'za': 'Zhuang', 'zh': 'Chinese Simplified', 'zt': 'Chinese Traditional', 'zu': 'Zulu'}

def toggleEntry():
    if login.get():
        usernameEntry.config(state = "normal")
        passwordEntry.config(state = "normal")
    else:
        usernameEntry.config(state = "disabled")
        passwordEntry.config(state = "disabled")
def askDirectory():
    location = tk.filedialog.askdirectory()
    locationLabel.config(text = location)

def selectAll():
    for video in videoList:
        videoList[video[1]].set(True)
def deselectAll():
    for video in videoList:
        videoList[video[1]].set(False)
def download():
    if urlEntry.get():
        videoSelected = ""
        for video in videoList:
            if videoList[video][1].get():
                videoSelected += str(videoList[video][0]) + ","
        videoSelected = videoSelected[:-1]
        if subtitleSelected.get() == "No subtitle":
            subtitleSelected.set("")
        else:
            subtitleSelected.set(list(langDict.keys())[list(langDict.values()).index(subtitleSelected.get())])
        downloadButton.config(text = "Downloading. Check terminal for progerss", state = "disabled")
        ydl_options = {
            "playlist_items": videoSelected,
            "subtitleslangs": [subtitleSelected],
        }
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            ydl.download([urlEntry.get()])
        restoreButtons()
    else:
        tk.messagebox.showerror("Error", "No URL given")



videoList = {}
subtitleList = []
location = os.getcwd()



# ------------------------------------------------------- UI -------------------------------------------------------

m = tk.Tk()
m.geometry()
m.title("viki-download-gui")




# login

'''
loginFrame = tk.Frame(m)
login = tk.BooleanVar()
loginCheck = tk.Checkbutton(m, text = "Login to Viki account", var = login, command = toggleEntry).grid(row = 0, column = 0)
usernameLabel = tk.Label(loginFrame, text = "Username").grid(row = 0, column = 0)
usernameEntry = tk.Entry(loginFrame, state = "disabled")
usernameEntry.grid(row = 0, column = 1)
passwordLabel = tk.Label(loginFrame, text = "Password").grid(row = 1, column = 0)
passwordEntry = tk.Entry(loginFrame, state = "disabled")
passwordEntry.grid(row = 1, column = 1)
loginFrame.grid(row = 0, column = 1)
'''


# url entry and video info extraction

def getVideoInfo():
    try: # for when the URL is valid
        urlButton.config(text = "Extracting video info", state = "disabled")
        with youtube_dl.YoutubeDL() as ydl:
            playlistInfo = ydl.extract_info(urlEntry.get(), download=False)
        for i, video in enumerate(playlistInfo['entries']):
            videoList[video.get('title')] = [i, tk.BooleanVar()] # adding entry to dictionary, with title as key and index + False as value
            for subtitle in video.get('subtitles').keys(): # adding subtitle language to list if it isn't already present
                if langDict[subtitle] not in subtitleList:
                    subtitleList.append(langDict[subtitle])
        subtitleList.sort() # sorting list of languages alphabetically
        for video in videoList: # creating a checkbox for every video in playlist
            tk.Checkbutton(videoListFrame, text = video, var = videoList[video][1]).pack(anchor = "w")
        subtitleList.insert(0, "No subtitle") # allow selecting no subtitle as an option
        subtitleSelected.set(subtitleList[0]) # set default option to no subtitle
        subtitleMenu = tk.OptionMenu(subtitleFrame, subtitleSelected, *subtitleList).pack() # creating dropdown menu to select subtitle
        restoreButtons()
    except: # for when the URL is invalid
        restoreButtons()
        tk.messagebox.showerror(title="Error", message="Invalid URL")
        urlEntry.delete(0, tk.END)
        urlEntry.insert(0, "")
def restoreButtons():
    urlButton.config(text = "Extract video info", state = "normal")
    downloadButton.config(text = "Download", state = "normal")

urlFrame = tk.Frame(m)
urlLabel = tk.Label(m, text = "Drama homepage URL").grid(row = 1, column = 0)
urlEntry = tk.Entry(urlFrame, width = 50)
urlEntry.pack(side = tk.LEFT)
videoList = {}
subtitleList = []
urlButton = tk.Button(urlFrame, text = "Extract video info", command = lambda: threading.Thread(target = getVideoInfo, args = ()).start())
urlButton.pack(side = tk.LEFT)
urlFrame.grid(row = 1, column = 1)

# video selection

videoFrame = tk.Frame(m)
videoLabel = tk.Label(videoFrame, text = "Select videos").pack()
selectAll = tk.Button(videoFrame, text = "Select all", command = selectAll).pack()
deselectAll = tk.Button(videoFrame, text = "Deselect all", command = deselectAll).pack()
videoListFrame = tk.Frame(m, height=300, width=300)
videoFrame.grid(row = 2, column = 0)
videoListFrame.grid(row = 2, column = 1)

# subtitle selection

subtitleFrame = tk.Frame(m)
subtitleLabel = tk.Label(m, text = "Select subtitle").grid(row = 3, column = 0)
subtitleSelected = tk.StringVar()
subtitleFrame.grid(row = 3, column = 1)


# file location selection

locationFrame = tk.Frame(m)
locationLabel = tk.Label(locationFrame, text = location)
locationLabel.pack()
locationButton = tk.Button(m, text = "Select download location", command = askDirectory).grid(row = 4, column = 0)
locationFrame.grid(row = 4, column = 1)

# download

downloadButton = tk.Button(m, text = "Start Download", command = lambda: threading.Thread(target = download).start())
downloadButton.grid(row = 5, columnspan = 2)

m.mainloop()
