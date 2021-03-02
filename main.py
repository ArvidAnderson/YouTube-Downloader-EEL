
# YouTube-DL-EEL
from pytube import YouTube
from tkinter import Tk
import tkinter.filedialog
import eel
eel.init('web')

url = []
file_path = []


def get_youtube_video(text):
    try:
        yt = YouTube(text)
        url.append(text)
        video_exists_passthrough(True)
    except:
        video_exists_passthrough(False)
    return None


@eel.expose
def get_youtube_video_passthrough(text):
    get_youtube_video(text)
    return None


@eel.expose
def video_exists_passthrough(yesno):
    eel.video_exists(yesno)
    return None

@eel.expose
def setThumbnailandTitle():
    thumbnail_url = YouTube(url[0]).thumbnail_url
    title_text = YouTube(url[0]).title
    eel.setThumbnailandTitle(thumbnail_url, title_text)
    return None

@eel.expose
def get_file_path():
    if not file_path:
        pass
    else:
        file_path.pop(0)
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder = tkinter.filedialog.askdirectory()
    file_path.append(folder)
    eel.setFilePath(folder)
    return None

@eel.expose
def download_video():
    print("Downloading best")
    YouTube(url[0]).streams.first().download(file_path[0])

@eel.expose
def download_audio():
    print("Downloading best")
    YouTube(url[0]).streams.get_audio_only().download(file_path[0])


@eel.expose
def get_streams():
    stream = YouTube(url[0]).streams.all()
    for i in stream:
        print(i)



if __name__ == "__main__":
    eel.start('index.html', size=(500, 470))
