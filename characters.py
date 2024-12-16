import pygame
from pygame.sprite import Sprite
from cards import Card
import random


class Character(Sprite):
    """"""

    def __init__(self,rpg,*stats):
        """"""
        super().__init__()
        self.screen_rect = rpg.screen.get_rect()
        self.screen = rpg.screen
        self.attack = stats[0]
        self.armor = stats[1]
        self.agility = stats[2]
        self.intelligence = stats[3]
        self.health = stats[4]

        self.card_1a = Card('mech',0,2,0,0,0,0,'shield')
        self.card_2a = Card('mech',2,0,0,0,0,0,'sword')
        self.card_3a = Card('mech',30,0,0,0,0,0,'missile')
        self.card_4a = Card('mech',0,4,0,0,0,0,'armor')
        self.card_5a = Card('mech',8,0,0,0,0,0,'rifle')
        self.card_6a = Card('animal',4,0,0,0,0,0,'bite')
        self.card_7a = Card('animal',2,0,0,0,0,0,'claw')
        self.card_8a = Card('animal',0,0,2,0,0,0,'run')
        self.card_9a = Card('magic',0,0,10,0,0,0,'heal')
        self.card_10a = Card('magic',2,0,0,0,0,0,'start fire')
        self.card_11a = Card('magic',0,0,0,0,0,0,'flooding')
        self.card_12a = Card('magic',0,0,0,0,0,0,'black-magic')
        self.card_13a = Card('magic',0,0,0,0,0,0,'hang from well')
        self.card_14a = Card('nature',0,0,0,0,0,0,'flock')
        self.card_15a = Card('nature',0,0,0,0,0,0,'egg')
        self.card_16a = Card('nature',0,0,0,0,0,0,'jack')

        self.card_list = [self.card_1a,self.card_2a,self.card_3a,self.card_4a,self.card_5a,self.card_6a,self.card_7a,self.card_8a,self.card_9a,self.card_10a,self.card_11a,self.card_12a,self.card_13a,self.card_14a,self.card_15a,self.card_16a]
        #self.deck_list2 = self.deck_list
        deck_size = 0
        self.deck_list = random.sample(self.card_list,k=8)
        self.deck_list2 = []

        while deck_size < 40:
            n = random.choice(self.card_list)
            if n.name == self.card_3a.name:
                self.card_list.remove(self.card_3a)
                
                

            self.deck_list2.append(n)
            deck_size += 1
        deck_size = 0
        

        self.image = pygame.image.load('images1\cat_1_1.bmp')
        self.rect = self.image.get_rect()

        #self.screen_rect.midleft = self.screen_rect.midleft
        self.rect.y += rpg.screen_height / 4

        self.attack_sprites = [pygame.image.load('images1\cattack_1.bmp'),pygame.image.load('images1\cattack_2.bmp'),pygame.image.load('images1\cattack_3.bmp'),pygame.image.load('images1\cattack_4.bmp'),pygame.image.load('images1\cattack_5.bmp')]
        self.attack_rect1 = [self.attack_sprites[0].get_rect(),self.attack_sprites[1].get_rect,self.attack_sprites[2].get_rect,self.attack_sprites[3].get_rect,self.attack_sprites[4].get_rect]
        
        self.attack_sprites_r = [pygame.image.load('images1\cattack_1r.bmp'),pygame.image.load('images1\cattack_2r.bmp'),pygame.image.load('images1\cattack_3r.bmp'),pygame.image.load('images1\cattack_4r.bmp'),pygame.image.load('images1\cattack_5r.bmp')]
        self.attack_rect1_r = [self.attack_sprites_r[0].get_rect(),self.attack_sprites_r[1].get_rect,self.attack_sprites_r[2].get_rect,self.attack_sprites_r[3].get_rect,self.attack_sprites_r[4].get_rect]
        self.fire_sprites = [pygame.image.load('images1\spark\spark1.bmp'),pygame.image.load('images1\spark\spark2.bmp'),pygame.image.load('images1\spark\spark3.bmp')
                             ,pygame.image.load('images1\spark\spark4.bmp'),pygame.image.load('images1\spark\spark5.bmp'),pygame.image.load('images1\spark\spark6.bmp')
                             ,pygame.image.load('images1\spark\spark7.bmp'),pygame.image.load('images1\spark\spark8.bmp'),pygame.image.load('images1\spark\spark9.bmp')
                             ]
        self.animation_tracker = 0
        self.animation_tracker_r = 0
        self.animation_spark_track = 0
        self.animation_countdown = 200
        self.animation_length = 200
        #locations
        self.x = self.rect.x
        self.y = self.rect.y
        self.animation_sound = pygame.mixer.Sound('try3.mp3')
        self.animation_sound.set_volume(0.5)
    def attack_animation(self):
        """"""
        self.screen.blit(self.attack_sprites[self.animation_tracker],(350,225))
    def attack_animation_r(self):
        self.screen.blit(self.attack_sprites_r[self.animation_tracker_r],(650,225))
    def fire_attack(self,rpg):
        """"""
        rpg.fire_attack = self.animation_length
        self.animation_spark_track = 0
    def draw_fire(self,rpg):
        
        self.screen.blit(self.fire_sprites[self.animation_spark_track],(500,0))
        #print(location[0],location[1])
    def draw_me(self,rpg):
        """"""
        self.screen.blit(self.image,self.rect) 
       
    def attack_sound(self):
        """"""
        pygame.mixer.Sound.play(self.animation_sound)
    

    def create_deck(self):
    
        """"""
        self.card_list = [self.card_1a,self.card_2a,self.card_3a,self.card_4a,self.card_5a,self.card_6a,self.card_7a,self.card_8a,self.card_9a,self.card_10a,self.card_11a,self.card_12a,self.card_13a,self.card_14a,self.card_15a,self.card_16a]
        #self.deck_list2 = self.deck_list
        deck_size = 0
        self.deck_list = random.sample(self.card_list,k=8)
        self.deck_list2 = []
        while deck_size < 40:
            n = random.choice(self.card_list)
            if n.name == self.card_3a.name:
                self.card_list.remove(self.card_3a)
            self.deck_list2.append(n)
            deck_size += 1


    def update_deck(self,rpg):
        #print(len(self.deck_list2))
        #self.health_check()
        if len(self.deck_list2) < 1:
            self.start_menu = False
        rpg.fight_demo.attack_1_button.prep_msg(self.deck_list2[0].name)
        if len(self.deck_list2) == 1:
            return
        rpg.fight_demo.attack_2_button.prep_msg(self.deck_list2[1].name)
        if len(self.deck_list2) == 2:
            return
        rpg.fight_demo.attack_3_button.prep_msg(self.deck_list2[2].name)
        if len(self.deck_list2) == 3:
            return
        rpg.fight_demo.attack_4_button.prep_msg(self.deck_list2[3].name)
         
        
