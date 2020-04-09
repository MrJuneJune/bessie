import pyttsx3
import speech_recognition as sr
import youtube_play


def listen(func_or_class, *args, **kwargs):
    return func_or_class(*args, **kwargs)


def say(voice):
    engine.say(voice.split('say')[1])


def print_say(voice):
    print(voice)


commands = {
    'play': youtube_play.YoutubePlayer,
    'say': say,
    'write': print_say,
#    'pause': VLC_PLAYER.do,
#    'stop': VLC_PLAYER.do,
}


engine = pyttsx3.init()
r = sr.Recognizer()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # here
    while True:
        audio=r.listen(source)
        response=r.recognize_google(audio)
        writeresponse)
        for command in commands.keys():
            if command in response:
#                listen(commands[command], response, command=command)
                listen(commands[command], response)
                engine.runAndWait() 
        if response=='Stop':
            break
