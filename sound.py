import pygame as pg
from pygame import mixer

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound'
        self.shotgun = pg.mixer.Sound(self.path + '/shotgun_sound.mp3')
        self.shotgun.set_volume(0.15)
        self.npc_pain = pg.mixer.Sound(self.path + '/soldier_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + '/death_soldier.wav')
        self.npc_shot = pg.mixer.Sound(self.path + '/enemy_shot.wav')
        self.npc_shot.set_volume(0.15)
        self.player_pain = pg.mixer.Sound(self.path + '/player_pain.wav')
        self.player_pain.set_volume(0.3)

