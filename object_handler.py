from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc'
        self.static_sprite_path = 'resources/sprites/static_sprites'
        self.animated_sprite_path = 'resources/sprites/animated_sprites'
        add_npc = self.add_npc
        add_sprite = self.add_sprite
        self.npc_positions = {}
    
        # sprite map 
        add_sprite(SpriteObject(game))
        add_sprite(SpriteObject(game, pos = (8.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos = (1.25, 1.25)))
        add_sprite(AnimatedSprite(game, pos = (11.85, 1.25)))
        add_sprite(AnimatedSprite(game, path = self.animated_sprite_path + '/red_torch/1.png',pos = (6.8, 3.85), scale = 1.0, shift = 0.1))
        add_sprite(AnimatedSprite(game, path = self.animated_sprite_path + '/red_torch/1.png' ,pos = (8.2, 3.85), scale = 1.0, shift = 0.1))
        add_sprite(AnimatedSprite(game, path = self.animated_sprite_path + '/heart_foun/1.png' ,pos = (7.5, 5.85), scale = 0.5, shift = 0.6))
        add_sprite(AnimatedSprite(game, path = self.animated_sprite_path + '/eye/1.png' ,pos = (1.5, 7.7), scale = 0.5, shift = 0.0))
        add_sprite(AnimatedSprite(game, path = self.animated_sprite_path + '/skull_altar/1.png' ,pos = (5.75, 5.25), scale = 0.5, shift = 0.6))

        #npc map
        add_npc(NPC(game))
        add_npc(NPC(game, pos = (9.5, 7.5)))
        add_npc(CacoDemonNPC(game))
        add_npc(CacoDemonNPC(game, pos = (12.5, 5)))
        add_npc(CyberDemonNPC(game))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update( )for npc in self.npc_list]


    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)





