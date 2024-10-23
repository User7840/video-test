import os
import random
import time
import mpv
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
    player = mpv.MPV(ytdl=True)
    player.play(video)
    player.wait_for_playback()

def playVideos(videos):
    if len(videos) > 0:
        random.shuffle(videos)
        for video in videos:
            play_video(video)

playVideos(getVideos())
while True:
    pass
