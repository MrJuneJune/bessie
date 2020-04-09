from time import sleep
import pafy
import vlc


# Get url with best video quality
class YoutubePlayer:
    def __init__(self, voice):
        ''' Initiate vlc and play youtube video init by using playurl created from pafy'''
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.play(voice)

    def play(self, voice):
        '''
        Play a song
        '''
        song_name = voice.split('play')[1]
        url = self.get_url(song_name)
        media = self.instance.media_new(self.get_play_url(url))
        media.get_mrl()
        self.player.set_media(media)
        self.player.play()

    def get_url(self, song_name):
        '''
        Convert string to query param. Then look for youtube links
        '''
        import urllib.request
        from bs4 import BeautifulSoup
        print(song_name)
        query = urllib.parse.quote(song_name)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.findAll(attrs={'class':'yt-uix-tile-link'})[0])
        url = 'https://www.youtube.com' + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']
        return url

    def get_play_url(self, url):
        best_video = pafy.new(url).getbest()
        return best_video.url

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def resume(self):
        self.player.resume()

    def do(self, *arg, **kwargs): 
        if hasattr(self, kwargs[command]):
            getattr(self, *arg, **kwargs)
            return True
        return False
