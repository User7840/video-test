import os
import random
import vlc
import signal
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

playing = False
instance = vlc.Instance()

def getVideos():
    videos = []
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))
    return videos

def play_video(video):
    
    if not instance:
        print('failed to get vlc instance')
        return
    else:
        player = instance.media_player_new()
        media = instance.media_new(video)
        player.set_media(media)
        player.play()
        print(player.get_state())

def playVideos(videos):
    if len(videos) > 0:
        random.shuffle(videos)
        for video in videos:
            play_video(video)
    else:
        print('No videos found')
        exit()

def signal_handler(signal, frame):
    print("Keyboard interrupt, exiting")
    instance.release()
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

playVideos(getVideos())
while True:
    pass