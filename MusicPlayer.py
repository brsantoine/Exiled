import pygame as pg

class MusicPlayer:

    def playMenuMusic(self):
        pg.mixer.music.load("music/aerocity_stranger.mp3")
        pg.mixer.music.play()

    def playExpeditionMusic(self):
        pg.mixer.music.load("music/cloudkicker_night.mp3")
        pg.mixer.music.play()

    def fadeOut(self):
        pg.mixer.music.fadeout(10000)