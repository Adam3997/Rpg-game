from physics_stats import Physics_stats
from sprite_sheet_animater import Sprite_loader
import pygame
import random



class Projectile_class(Physics_stats):
    """This will hold a projectile class that can impact things and do damage."""


    def __init__(self,rpg,type,knockback):
        """initiialize stuff"""


        Physics_stats.__init__(self,rpg)
        super().__init__(rpg)
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        if type != 'smoke':
        
            information = '_internal\\explosion\expl_0'
            information += str(type)
            information += '_000'
            self.fire_ball = Sprite_loader(information,-2) # default is 3 # 8 will be for the extra attack
            self.fire_ball_knockback = 20
            self.fire_damage = 5
            self.fire_damage_old = self.fire_damage
        if type == 'smoke':
            """"""
            information = '_internal\\explosion\puff_smoke_01_000'
            #information += str(type)
            #information += '_000'
            self.fire_ball = Sprite_loader(information,-10)
            self.friction_slowdown -= 0.02
            self.fire_ball_knockback = 0
            self.fire_damage = 0
            self.fire_damage_old = self.fire_damage
        #self.new_smoke_3 = Sprite_loader('explosion\expl_03_000',-2)
        self.fire_ball_rect = pygame.Rect(0,0,50,50)

        self.fire_ball_countdown = 150
        self.fire_ball_countdown_old = self.fire_ball_countdown

        self.fire_ball_lifespan = 75
        self.fire_ball_lifespan_old = self.fire_ball_lifespan


        self.fire_ball_active = False
        self.fire_ball_animation_counter = 0
        self.fire_ball_animation_delay = 5
        self.fire_ball_animation_delay_old = self.fire_ball_animation_delay
        self.animation_limit = 10
        #self.attack_speed_scale = random.randint(1,6)
        
        self.x_offset = 230
        self.y_offset = 150
        #self.fire_ball_rect.center = boss.rect.center
        self.fire_ball_rect.x += self.x_offset
        self.fire_ball_rect.y += self.y_offset

        self.counter_for_animation = 0
        self.hit_limit = 1
        
        #print(self.fire_ball_rect)

        self.knockback = knockback   # bigger number is 

    def check_fire_hit(self,rpg):
        """checks if fire hits players"""

        collisions_test  = pygame.Rect.colliderect(self.fire_ball_rect,rpg.level_stuff.player_1.rect)
        if collisions_test:        
            if self.hit_limit > 0:
                #print('boss hits player')
                rpg.level_stuff.player_1.velocity[1] += self.velocity[1] / self.knockback   #4
                rpg.level_stuff.player_1.velocity[0] += self.velocity[0] / self.knockback   #4
                if self.fire_damage > rpg.level_stuff.player_1.armor:
                    rpg.level_stuff.player_1.health -= self.fire_damage
                    rpg.overlay.create_damage_for_overlay(self.fire_damage,rpg.level_stuff.player_1.rect.center,'red')
                    self.fire_damage -= self.fire_damage
                    if self.fire_damage < 0:
                        self.fire_damage = 0
                    self.hit_limit -=1
                    if self.hit_limit < 0:
                        self.hit_limit = 0
                self.fire_ball_active = False
                