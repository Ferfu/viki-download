from __future__ import unicode_literals
import youtube_dl
from threading import Thread
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

langDict = {'aa': 'Afar', 'ab': 'Abkhazian', 'ae': 'Avestan', 'af': 'Afrikaans', 'ak': 'Akan', 'am': 'Amharic', 'an': 'Aragonese', 'ar': 'Arabic', 'as': 'Assamese', 'av': 'Avaric', 'ay': 'Aymara', 'az': 'Azerbaijani', 'ba': 'Bashkir', 'be': 'Belarusian', 'bg': 'Bulgarian', 'bh': 'Bihari', 'bm': 'Bambara', 'bi': 'Bislama', 'bn': 'Bengali', 'bo': 'Tibetan', 'br': 'Breton', 'bs': 'Bosnian', 'ca': 'Catalan', 'ce': 'Chechen', 'ch': 'Chamorro', 'co': 'Corsican', 'cr': 'Cree', 'cs': 'Czech', 'cu': 'Church', 'cv': 'Chuvash', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'dv': 'Divehi', 'dz': 'Dzongkha', 'ee': 'Ewe', 'el': 'Greek', 'en': 'English', 'eo': 'Esperanto', 'es': 'Spanish', 'et': 'Estonian', 'eu': 'Basque', 'fa': 'Persian', 'ff': 'Fulah', 'fi': 'Finnish', 'fj': 'Fijian', 'fo': 'Faroese', 'fr': 'French', 'fy': 'Western', 'ga': 'Irish', 'gd': 'Gaelic', 'gl': 'Galician', 'gn': 'Guarani', 'gu': 'Gujarati', 'gv': 'Manx', 'ha': 'Hausa', 'he': 'Hebrew', 'hi': 'Hindi', 'ho': 'Hiri', 'hr': 'Croatian', 'ht': 'Haitian', 'hu': 'Hungarian', 'hy': 'Armenian', 'hz': 'Herero', 'ia': 'Interlingua', 'id': 'Indonesian', 'ie': 'Interlingue', 'ig': 'Igbo', 'ii': 'Sichuan', 'ik': 'Inupiaq', 'io': 'Ido', 'is': 'Icelandic', 'it': 'Italian', 'iu': 'Inuktitut', 'ja': 'Japanese', 'jv': 'Javanese', 'ka': 'Georgian', 'kg': 'Kongo', 'ki': 'Kikuyu', 'kj': 'Kuanyama', 'kk': 'Kazakh', 'kl': 'Kalaallisut', 'km': 'Central', 'kn': 'Kannada', 'ko': 'Korean', 'kr': 'Kanuri', 'ks': 'Kashmiri', 'ku': 'Kurdish', 'kv': 'Komi', 'kw': 'Cornish', 'ky': 'Kirghiz', 'la': 'Latin', 'lb': 'Luxembourgish', 'lg': 'Ganda', 'li': 'Limburgan', 'ln': 'Lingala', 'lo': 'Lao', 'lt': 'Lithuanian', 'lu': 'Luba-Katanga', 'lv': 'Latvian', 'mg': 'Malagasy', 'mh': 'Marshallese', 'mi': 'Maori', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mn': 'Mongolian', 'mne': 'Montenegrin ', 'mo': 'Moldavian', 'mr': 'Marathi', 'ms': 'Malay', 'mt': 'Maltese', 'my': 'Burmese', 'na': 'Nauru', 'nb': 'Bokmål,', 'nd': 'Ndebele,', 'ne': 'Nepali', 'ng': 'Ndonga', 'nl': 'Dutch', 'nn': 'Norwegian', 'no': 'Norwegian', 'nr': 'Ndebele,', 'nv': 'Navajo', 'ny': 'Chichewa', 'oc': 'Occitan', 'oj': 'Ojibwa', 'om': 'Oromo', 'or': 'Oriya', 'os': 'Ossetian', 'pa': 'Panjabi', 'pi': 'Pali', 'pl': 'Polish', 'ps': 'Pushto', 'pt': 'Portuguese', 'qu': 'Quechua', 'rm': 'Romansh', 'rn': 'Rundi', 'ro': 'Romanian', 'ru': 'Russian', 'rw': 'Kinyarwanda', 'sa': 'Sanskrit', 'sc': 'Sardinian', 'sd': 'Sindhi', 'se': 'Northern', 'sg': 'Sango', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'sm': 'Samoan', 'sn': 'Shona', 'so': 'Somali', 'sq': 'Albanian', 'sr': 'Serbian', 'ss': 'Swati', 'sh': 'Serbo-Croatian', 'st': 'Sotho,', 'su': 'Sundanese', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'tg': 'Tajik', 'th': 'Thai', 'ti': 'Tigrinya', 'tk': 'Turkmen', 'tl': 'Tagalog', 'tn': 'Tswana', 'to': 'Tonga', 'tr': 'Turkish', 'ts': 'Tsonga', 'tt': 'Tatar', 'tw': 'Twi', 'ty': 'Tahitian', 'ug': 'Uighur', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 've': 'Venda', 'vi': 'Vietnamese', 'vo': 'Volapük', 'wa': 'Walloon', 'wo': 'Wolof', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'za': 'Zhuang', 'zh': 'Chinese Simplified', 'zt': 'Chinese Traditional', 'zu': 'Zulu'}



m = tk.Tk()
m.geometry()
m.title("viki-download-gui")


# login

'''

def toggleEntry():
    if login.get():
        usernameEntry.config(state = "normal")
        passwordEntry.config(state = "normal")
    else:
        usernameEntry.config(state = "disabled")
        passwordEntry.config(state = "disabled")

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

videoList = {}
subtitleList = []
subtitleSelected = tk.StringVar()
def clearList():
    global videoList
    global subtitleList
    videoList = {}
    subtitleList = []
    for widget in videoListFrame.winfo_children():
        widget.destroy()
    for widget in subtitleFrame.winfo_children():
        widget.destroy()
def getVideoInfo():
    try: # for when the URL is valid
        clearList()
        global videoList
        global subtitleList
        global subtitleSelected
        global urlEntry
        inactiveButtons()
        with youtube_dl.YoutubeDL() as ydl:
            playlistInfo = ydl.extract_info(urlEntry.get(), download=False)
        for i, video in enumerate(playlistInfo['entries'], 1):
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
        activeButtons()
    except: # for when the URL is invalid
        activeButtons()
        tk.messagebox.showerror(title="Error", message="Invalid URL")
        urlEntry.delete(0, tk.END)
        urlEntry.insert(0, "")
        return ({}, [])
def activeButtons():
    global urlButton
    global downloadButton
    global selectAllButton
    global deselectAllButton
    global locationButton
    global downloadButton
    urlButton.config(text = "Extract video info", state = "normal")
    downloadButton.config(text = "Download", state = "normal")
    selectAllButton.config(state = "normal")
    deselectAllButton.config(state = "normal")
    locationButton.config(state = "normal")
def inactiveButtons():
    global urlButton
    global downloadButton
    global selectAllButton
    global deselectAllButton
    global locationButton
    global downloadButton
    urlButton.config(text = "Extracting video info", state = "disabled")
    downloadButton.config(text = "Downloading. Check terminal for progress", state = "disabled")
    selectAllButton.config(state = "disabled")
    deselectAllButton.config(state = "disabled")
    locationButton.config(state = "disabled")

urlFrame = tk.Frame(m)
urlLabel = tk.Label(m, text = "Drama homepage URL").grid(row = 1, column = 0)
urlEntry = tk.Entry(urlFrame, width = 50)
urlEntry.pack(side = tk.LEFT)
urlButton = tk.Button(urlFrame, text = "Extract video info", command = lambda: Thread(target = getVideoInfo).start())
urlButton.pack(side = tk.LEFT)
urlFrame.grid(row = 1, column = 1)

# video selection

def selectAll():
    global videoList
    for video in videoList:
        videoList[video[1]].set(True)
def deselectAll():
    global videoList
    for video in videoList:
        videoList[video[1]].set(False)

videoFrame = tk.Frame(m)
videoLabel = tk.Label(videoFrame, text = "Select videos").pack()
selectAllButton = tk.Button(videoFrame, text = "Select all", command = selectAll)
selectAllButton.pack()
deselectAllButton = tk.Button(videoFrame, text = "Deselect all", command = deselectAll)
deselectAllButton.pack()
videoListFrame = tk.Frame(m, height=300, width=300)
videoFrame.grid(row = 2, column = 0)
videoListFrame.grid(row = 2, column = 1)

# subtitle selection

subtitleFrame = tk.Frame(m)
subtitleLabel = tk.Label(m, text = "Select subtitle\n\nNote: some languages are not\navailable for every episode\n").grid(row = 3, column = 0)
subtitleFrame.grid(row = 3, column = 1)


# file location selection

location = ""
locationSelected = False
def askDirectory():
    global location
    global locationSelected
    location = tk.filedialog.askdirectory()
    locationLabel.config(text = location)
    locationSelected = True

locationFrame = tk.Frame(m)
locationLabel = tk.Label(locationFrame, text = location)
locationLabel.pack()
locationButton = tk.Button(m, text = "Select download location", command = askDirectory)
locationButton.grid(row = 4, column = 0)
locationFrame.grid(row = 4, column = 1)

# download

def download():
    global urlEntry
    global locationSelected
    if urlEntry.get() and locationSelected:
        global videoList
        global location
        global subtitleSelected
        print("tetestset", location)
        print(videoList)
        videoSelected = ""
        for video in videoList:
            if videoList[video][1].get():
                videoSelected += str(videoList[video][0]) + ","
        videoSelected = videoSelected[:-1]
        downloadSubtitles = True
        if subtitleSelected.get() == "No subtitle":
            downloadSubtitles = False
        else:
            subtitleSelected.set(list(langDict.keys())[list(langDict.values()).index(subtitleSelected.get())])
        print(subtitleSelected.get())
        inactiveButtons()
        ydl_options = {
            "outtmpl": location + '/%(title)s.%(ext)s',
            "playlist_items": videoSelected,
            "writesubtitles": downloadSubtitles,
            "subtitleslangs": [subtitleSelected.get()],
        }
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            ydl.download([urlEntry.get()])
        activeButtons()
        clearList()
    elif not locationSelected:
        tk.messagebox.showerror("Error", "Download location not selected")
    else:
        tk.messagebox.showerror("Error", "No URL given")

downloadButton = tk.Button(m, text = "Start Download", command = lambda: Thread(target = download).start())
downloadButton.grid(row = 5, columnspan = 2)

m.mainloop()
