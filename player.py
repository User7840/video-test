import os
import random
import vlc
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

global playing

def getVideos():
    videos = []
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))

    print(videos)
    return videos

def play_video(video):
    instance = vlc.Instance()
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

playVideos(getVideos())
while True:
    pass