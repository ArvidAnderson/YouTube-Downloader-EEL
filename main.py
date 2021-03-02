
#YouTube-DL-EEL
from pytube import YouTube
import eel
eel.init('web')

url = []

def get_youtube_video(text):
    try:
        yt = YouTube(text)
        print(YouTube(text).streams[1])
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
def redirect_to_download():
    eel.start('download.html', size=(500, 450), port = 8000)
    return None

@eel.expose
def setThumbnailandTitle():
    thumbnail_url = YouTube(url[0]).thumbnail_url
    title_text = YouTube(url[0]).title
    print(title_text)
    eel.setThumbnailandTitle(thumbnail_url, title_text)

@eel.expose
def debugger():
    print("DEBUGGER RAN")




eel.start('index.html', size=(500, 335))