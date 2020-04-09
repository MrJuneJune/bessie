import pafy
import vlc
from time import sleep

url = "https://www.youtube.com/watch?v=SZkkZLSCv44"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
sleep(10)
