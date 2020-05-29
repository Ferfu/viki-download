from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import time

requiredFields = {"url": False, "location": False}

def debugging():
    with youtube_dl.YoutubeDL() as ydl:
        ydl.extract_info(urlEntry.get(), download=False)
def toggleEntry():
    if login.get():
        usernameEntry.config(state = "normal")
        passwordEntry.config(state = "normal")
    else:
        usernameEntry.config(state = "disabled")
        passwordEntry.config(state = "disabled")
def askDirectory():
    location = tk.filedialog.askdirectory()
    locationButton.config(text = location)
def checkUrl():
    urlButton.config(text = "Extracting video information\nThis may take 1 min")
    time.sleep(10)
    try:
        with youtube_dl.YoutubeDL({"playliststart": 0, "playlistend": 0, "quiet": True}) as ydl:
            ydl.extract_info(urlEntry.get(), download=False)
        requiredFields["url"] = True
        getVideoInfo()
    except:
        urlButton.config(text = "Check URL")
        tk.messagebox.showerror(title="Error", message="Invalid URL")
def getVideoInfo():
    with youtube_dl.YoutubeDL() as ydl:
        ydl.extract_info(urlEntry.get(), download=False)

m = tk.Tk()
m.geometry()

m.title("viki-download-gui")

login = tk.BooleanVar()
loginCheck = tk.Checkbutton(m, text = "Login to Viki account", var = login, command = toggleEntry)

usernameLabel = tk.Label(text = "Username")
usernameEntry = tk.Entry(state = "disabled")

passwordLabel = tk.Label(text = "Password")
passwordEntry = tk.Entry(state = "disabled")

urlLabel = tk.Label(text = "URL of HOME PAGE of drama\ne.g. https://www.viki.com/tv/36667c-hotel-del-luna")
urlEntry = tk.Entry()
urlButton = tk.Button(text = "Check URL", command = checkUrl)

videoLabel = tk.Label(text = "Select videos")
subtitleLabel = tk.Label(text = "Select subtitles")
locationLabel = tk.Label(text = "Select download location")
location = "Select download location"
locationButton = tk.Button(text = location, command = askDirectory)

downloadButton = tk.Button(text = "Start Download")






loginCheck.grid(row = 0, column = 0)

usernameLabel.grid(row = 1, column = 0)
usernameEntry.grid(row = 1, column = 1)

passwordLabel.grid(row = 2, column = 0)
passwordEntry.grid(row = 2, column = 1)

urlLabel.grid(row = 3, column = 0)
urlEntry.grid(row = 3, column = 1)
urlButton.grid(row = 4, column = 1)

videoLabel.grid(row = 5)
subtitleLabel.grid(row = 6, column = 0)
locationLabel.grid(row = 7, column = 0)
locationButton.grid(row = 7, column = 1)

downloadButton.grid(row = 9)



m.mainloop()
