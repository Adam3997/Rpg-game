#import pygame
#from pygame.sprite import _Group, Sprite
# i should refacter this to be more readable.
import pygame
from pygame.sprite import Sprite
from sprite_sheet_animater import Sprite_loader
from physics_stats import Physics_stats

# i must fix things: make it so when player has 1 or less velocity they become 0 velocity.
class Player(Sprite,Physics_stats):
    """This is the player in the game. You have a sprite and a location on screen. No animations yet. """
    def __init__(self,rpg):
        """initialize the player."""
        Physics_stats.__init__(self,rpg)
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()
        self.stab_damage = 10
        self.stab_damage_old = self.stab_damage
        self.score = 0
        self.health = 100    #100 
        self.movement_delay = 200
        self.mass = 2 # this represents 84 kilograms
        self.min_acc = 30
        self.max_acc = 250
        # 10 low 90 high is slow
        # 30 and 90 might be faster
        # 30 and 150 is fast

        self.throw_timer_delay = 120
        self.throw_timer_delay_old = self.throw_timer_delay


        self.block_active = False
        self.block_active_timer = 60
        self.block_active_timer_old = self.block_active_timer

        self.magic_animation_active = False
        self.magic_animation_delay = 10
        self.magic_animation_delay_old = self.magic_animation_delay
        
        # ritual life added +1
        self.extra_life_invoked = False


        self.armor = 1

        self.cut_scene_animation_counter = 81
        self.impact_delay = 40
        self.impact_delay_old = self.impact_delay
        ## # this stuff will be used for attack logic
        self.attack_direct_1_counter = 6
        self.attack_direct_1_counter_old = self.attack_direct_1_counter
        self.attack_active = False
        self.attack_length = 5
        self.footstep_sound_countdown = 12
        self.footstep_sound_countdown_old = self.footstep_sound_countdown
        self.footstep_next = 'right'
        self.previous_direction = 'right'
        self.highest = 'right'
        self.animation_last = 'right'
        n = 0
        m = 8
        self.image_list_right = []
        self.image_list_left = []

        self.sprite_sheet_player_1 = Sprite_loader('_internal\\img\\player_image.png',3)
        
        self.image_resized = pygame.transform.scale2x(self.sprite_sheet_player_1.surface_list[0])
        self.rect_2 = self.image_resized.get_rect()
        self.rect = pygame.Rect(0,0,50,50)
        self.rect_2.center = self.screen_rect.center
        self.rect.center = self.screen_rect.center
        self.rect.x += -60
        self.rect.y += -60
        self.x = self.rect.x
        self.y = self.rect.y
        self.last_attack = False
        self.animation_counter = 0
        self.animation_delay = 2
        self.animation_delay_start = self.animation_delay
        self.animation_length_walk = 7
        


        self.cut_scene_animation_delay = 10
        self.cut_scene_animation_delay_old = self.cut_scene_animation_delay

        #self.shadow_rect = pygame.Rect(0,0,50,80)
        #self.shadow_rect.center = self.rect.center
        #self.shadow_rect.centery += 10

        self.death_animation_timer = 500
        self.death_animation_timer_old = self.death_animation_timer

        self.death_animation_active = False

        self.death_animation_start = 180
        self.death_animation_end = 185

        self.death_animation_delay = 10
        self.death_animation_delay_old = self.death_animation_delay

        


        self.shadow_surface = pygame.Surface((50,80), pygame.SRCALPHA)
        self.shadow_rect = self.shadow_surface.get_rect()
        #self.shadow_rect.centery += 10
        self.shadow_surface.fill((10,10,10))
        self.shadow_surface.set_colorkey((10,10,10))
        pygame.draw.ellipse(self.shadow_surface,(2, 48, 32,150),self.shadow_rect)
        

        #self.shadow_of_player 

        self.map_x_location = self.rect.centerx
        self.map_y_location = self.rect.centery
        self.map_x_location_old = self.rect.centerx
        self.map_y_location_old = self.rect.centery

        self.prep_game_over(rpg)

    def reset_player_map(self):
        """This resets the player on the map"""
        self.map_x_location = self.map_x_location_old
        self.map_y_location = self.map_y_location_old
    
    def movement_test(self,rpg):
        """This is a test"""
        self.movement_delay -= 1
        if self.movement_delay <= 0:
            self.change_accelleration()
            #print('acc changed')
            self.movement_delay = 200
        #self.update_speed(rpg)

        self.rect.x += self.velocity[0] * rpg.dt
        self.rect.y += self.velocity[1] * rpg.dt
    
    def draw_death_stuff(self):
        """"""
        if self.death_animation_active:
            self.screen.blit(self.game_over,self.game_over_rect)
            self.screen.blit(self.sprite_sheet_player_1.surface_list[self.death_animation_start],self.rect_2)
            self.death_animation_delay -= 1
            if self.death_animation_delay <= 0:
                self.death_animation_delay = self.death_animation_delay_old
                #self.death_animation_start += 1
                if self.death_animation_start < self.death_animation_end:
                    self.death_animation_start += 1
                    #print(self.death_animation_start)

    def death_animation_logic(self,rpg):
        """This holds logic for playing dying. """
        if self.death_animation_active:
            self.death_animation_timer -= 1
            #self.draw_death_stuff()
            
            if self.death_animation_timer <= 0:
                self.death_animation_active = False
                rpg.campagne_mode = False
                rpg.game_over_screen = True

    # i need to add one for checking if particle hits a tree.
    def check_particle_hit(self,rpg):
        """this checks if the particle hits an enemy or boss"""
        rect_particle = pygame.Rect(0,0,70,70)
        rect_particle.centerx = rpg.level_stuff.particle_list_1[1].particle_x_location + 45
        rect_particle.centery = rpg.level_stuff.particle_list_1[1].particle_y_location + 40
        if rpg.level_stuff.boss_type == 'spider':
            collisions_test_boss = pygame.Rect.colliderect(rect_particle,rpg.level_stuff.level_1_boss.rect_2)
            if collisions_test_boss:
                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.particle_hit_sound)
                if rpg.level_stuff.boss_type == 'spider':
                    if rpg.level_stuff.particle_list_1[1].damage > rpg.level_stuff.level_1_boss.armor:
                        rpg.level_stuff.level_1_boss.health -= rpg.level_stuff.particle_list_1[1].damage
                        rpg.overlay.create_damage_for_overlay(rpg.level_stuff.particle_list_1[1].damage,rect_particle.center,'cyan')
                        rpg.level_stuff.particle_list_1[1].damage -= rpg.level_stuff.particle_list_1[1].damage
                        if rpg.level_stuff.particle_list_1[1].damage < 0:
                            rpg.level_stuff.particle_list_1[1].damage = 0
                    if rpg.level_stuff.particle_list_1[1].post_hit_particle_active == False:
                            rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                    rpg.level_stuff.particle_list_1[1].post_hit_particle_active = True
                    #rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                    rpg.level_stuff.particle_list_1[1].reset_particle(rpg) # collision for boss here
            collisions_test_boss = pygame.Rect.colliderect(rect_particle,rpg.level_stuff.level_1_boss.weakness_rect) # this will do double damage.
            if collisions_test_boss:
                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.particle_hit_sound)
                if rpg.level_stuff.boss_type == 'spider':
                    if (rpg.level_stuff.particle_list_1[1].damage * 2) > rpg.level_stuff.level_1_boss.armor:
                        rpg.level_stuff.level_1_boss.health -= (rpg.level_stuff.particle_list_1[1].damage * 2)
                        rpg.overlay.create_damage_for_overlay((rpg.level_stuff.particle_list_1[1].damage * 2),rect_particle.center,'blue')
                        rpg.level_stuff.particle_list_1[1].damage -= rpg.level_stuff.particle_list_1[1].damage
                        if rpg.level_stuff.particle_list_1[1].damage < 0:
                            rpg.level_stuff.particle_list_1[1].damage = 0
                    if rpg.level_stuff.particle_list_1[1].post_hit_particle_active == False:
                            rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                    rpg.level_stuff.particle_list_1[1].post_hit_particle_active = True
                    #rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                    rpg.level_stuff.particle_list_1[1].reset_particle(rpg) # collision for boss here
            
            #print(rpg.level_1_boss.health )
        if rpg.level_stuff.boss_type == 'wolf':
            n = 0 # this will be the wolves
            m = len(rpg.level_stuff.level_1_boss.wolf_list) - 1
            while n <= m:
                collisions_test  = pygame.Rect.colliderect(rect_particle,rpg.level_stuff.level_1_boss.wolf_list[n])
                if collisions_test:
                    #print('hit with particle')
                    pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.particle_hit_sound)
                    rpg.level_stuff.level_1_boss.wolf_list[n].health -= rpg.level_stuff.particle_list_1[1].damage
                    rpg.overlay.create_damage_for_overlay(rpg.level_stuff.particle_list_1[1].damage,rect_particle.center,'cyan')
                    rpg.level_stuff.particle_list_1[1].damage -= rpg.level_stuff.particle_list_1[1].damage
                    
                    if rpg.level_stuff.particle_list_1[1].damage < 0:
                        rpg.level_stuff.particle_list_1[1].damage = 0
                    if rpg.level_stuff.particle_list_1[1].post_hit_particle_active == False:
                        rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                    rpg.level_stuff.particle_list_1[1].post_hit_particle_active = True
                    #rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                    rpg.level_stuff.particle_list_1[1].reset_particle(rpg) # collision and reset here
                    
                n += 1
        
        
        n = 0
        m = len(rpg.level_stuff.enemy_list) - 1
        while n <= m:
            collisions_test  = pygame.Rect.colliderect(rect_particle,rpg.level_stuff.enemy_list[n])
            if collisions_test:
                #print('hit with particle')
                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.particle_hit_sound)
                rpg.level_stuff.enemy_list[n].health -= rpg.level_stuff.particle_list_1[1].damage
                rpg.overlay.create_damage_for_overlay(rpg.level_stuff.particle_list_1[1].damage,rect_particle.center,'cyan')
                rpg.level_stuff.particle_list_1[1].damage -= rpg.level_stuff.particle_list_1[1].damage
                
                if rpg.level_stuff.particle_list_1[1].damage < 0:
                    rpg.level_stuff.particle_list_1[1].damage = 0
                if rpg.level_stuff.particle_list_1[1].post_hit_particle_active == False:
                    rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                rpg.level_stuff.particle_list_1[1].post_hit_particle_active = True
                #rpg.level_stuff.particle_list_1[1].accellerate_post_hit_particles(rpg)
                rpg.level_stuff.particle_list_1[1].reset_particle(rpg) # collision and reset here
                
            n += 1
    
    def attack_sword_1(self,rpg):
        """ this is the direct attack in front of the character.""" # my plan is to create a new  rect in front of the character, and if its touching the monster
        # then 
        self.rect_attack_right = pygame.Rect.copy(self.rect)
        self.rect_attack_left = pygame.Rect.copy(self.rect)
        self.rect_attack_up = pygame.Rect.copy(self.rect)
        self.rect_attack_down = pygame.Rect.copy(self.rect)
        self.rect_attack_right.centerx += 90
        self.rect_attack_right.centery += 10
        self.rect_attack_left.centerx -= 80
        self.rect_attack_down.centery += 90
        self.rect_attack_up.centery -= 90
        self.rect_attack_up.centerx += 10
        match self.highest:
            case 'right':
                n = 0
                m = len(rpg.level_stuff.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_right.colliderect(rpg.level_stuff.enemy_list[n])
                    if collisions_test:
                        #print('hit right')
                        rpg.level_stuff.enemy_list[n].health -= self.stab_damage
                        
                        if rpg.stab_sound_limit > 0:   
                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                            rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_right.center,'cyan')
                            self.stab_damage -= self.stab_damage
                            rpg.stab_sound_limit -= 1
                    n += 1
                if rpg.level_stuff.boss_type == 'spider':
                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_right,rpg.level_stuff.level_1_boss.rect_2)
                    if collisions_test_boss:
                        if self.stab_damage > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= self.stab_damage
                            rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_right.center,'cyan')
                            self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:   
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                self.stab_damage -= self.stab_damage
                                rpg.stab_sound_limit -= 1
                    
                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_right,rpg.level_stuff.level_1_boss.weakness_rect)
                    if collisions_test_boss:
                        if (self.stab_damage*2) > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= (self.stab_damage * 2)
                            rpg.overlay.create_damage_for_overlay((self.stab_damage * 2),self.rect_attack_right.center,'blue')
                            self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:   
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                self.stab_damage -= self.stab_damage
                                rpg.stab_sound_limit -= 1
                    #print('hit with attack')
                if rpg.level_stuff.boss_type == 'wolf':
                    n = 0
                    m = len(rpg.level_stuff.level_1_boss.wolf_list) - 1
                    while n <= m:
                        collisions_test = self.rect_attack_right.colliderect(rpg.level_stuff.level_1_boss.wolf_list[n])
                        if collisions_test:
                            #print('hit right')
                            rpg.level_stuff.level_1_boss.wolf_list[n].health -= self.stab_damage
                            
                            if rpg.stab_sound_limit > 0:   
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_right.center,'cyan')
                                self.stab_damage -= self.stab_damage
                                rpg.stab_sound_limit -= 1
                        n += 1
            case 'left':
                n = 0
                m = len(rpg.level_stuff.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_left.colliderect(rpg.level_stuff.enemy_list[n])
                    if collisions_test:
                        #print('hit left')
                        rpg.level_stuff.enemy_list[n].health -= self.stab_damage
                        
                        if rpg.stab_sound_limit > 0:
                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                            rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_left.center,'cyan')
                            rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                    n += 1
                if rpg.level_stuff.boss_type == 'spider':
                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_left,rpg.level_stuff.level_1_boss.rect_2)
                    if collisions_test_boss:
                        if self.stab_damage > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= self.stab_damage
                            #rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_left.center,'cyan')
                            #self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_left.center,'cyan')

                                rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                    
                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_left,rpg.level_stuff.level_1_boss.weakness_rect)
                    if collisions_test_boss:
                        if (self.stab_damage*2) > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= (self.stab_damage * 2)
                            #rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_left.center,'cyan')
                            #self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage*2,self.rect_attack_left.center,'purple')

                                rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                
                if rpg.level_stuff.boss_type == 'wolf':
                    n = 0
                    m = len(rpg.level_stuff.level_1_boss.wolf_list) - 1
                    while n <= m:
                        collisions_test = self.rect_attack_left.colliderect(rpg.level_stuff.level_1_boss.wolf_list[n])
                        if collisions_test:
                            #print('hit right')
                            rpg.level_stuff.level_1_boss.wolf_list[n].health -= self.stab_damage
                            
                            if rpg.stab_sound_limit > 0:   
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_left.center,'cyan')
                                self.stab_damage -= self.stab_damage
                                rpg.stab_sound_limit -= 1
                        n += 1
            case 'up':
                n = 0
                m = len(rpg.level_stuff.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_up.colliderect(rpg.level_stuff.enemy_list[n])
                    if collisions_test:
                        #print('hit up')
                        rpg.level_stuff.enemy_list[n].health -= self.stab_damage
                        
                        if rpg.stab_sound_limit > 0:
                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                            rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_up.center,'cyan')
                            rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                    n += 1
                if rpg.level_stuff.boss_type == 'spider':
                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_up,rpg.level_stuff.level_1_boss.rect_2)
                    if collisions_test_boss:
                        if self.stab_damage > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= self.stab_damage
                            #rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_up.center,'cyan')
                            #self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_up.center,'cyan')
                                rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                        #print('hit with attack')
                    
                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_up,rpg.level_stuff.level_1_boss.weakness_rect)
                    if collisions_test_boss:
                        if (self.stab_damage*2) > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= self.stab_damage*2
                            #rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_up.center,'cyan')
                            #self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage*2,self.rect_attack_up.center,'purple')
                                rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                        #print('hit with attack')
                if rpg.level_stuff.boss_type == 'wolf':
                    n = 0
                    m = len(rpg.level_stuff.level_1_boss.wolf_list) - 1
                    while n <= m:
                        collisions_test = self.rect_attack_up.colliderect(rpg.level_stuff.level_1_boss.wolf_list[n])
                        if collisions_test:
                            #print('hit right')
                            rpg.level_stuff.level_1_boss.wolf_list[n].health -= self.stab_damage
                            
                            if rpg.stab_sound_limit > 0:   
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_up.center,'cyan')
                                self.stab_damage -= self.stab_damage
                                rpg.stab_sound_limit -= 1
                        n += 1
            case 'down':
                n = 0
                m = len(rpg.level_stuff.enemy_list) - 1
                while n <= m:
                    collisions_test = self.rect_attack_down.colliderect(rpg.level_stuff.enemy_list[n])
                    if collisions_test:
                        #print('hit down')
                        rpg.level_stuff.enemy_list[n].health -= self.stab_damage
                        
                        if rpg.stab_sound_limit > 0:
                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                            rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_down.center,'cyan')
                            rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                        #print('direct hit below')
                    n += 1
                if rpg.level_stuff.boss_type == 'spider':
                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_down,rpg.level_stuff.level_1_boss.rect_2)
                    if collisions_test_boss:
                        if self.stab_damage > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= self.stab_damage
                            
                            #self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_down.center,'cyan')
                                rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                    #print('hit with attack')

                    collisions_test_boss = pygame.Rect.colliderect(self.rect_attack_down,rpg.level_stuff.level_1_boss.weakness_rect)
                    if collisions_test_boss:
                        if self.stab_damage*2 > rpg.level_stuff.level_1_boss.armor:
                            rpg.level_stuff.level_1_boss.health -= self.stab_damage*2
                            
                            #self.stab_damage -= self.stab_damage
                        if rpg.stab_sound_limit > 0:
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage*2,self.rect_attack_down.center,'purple')
                                rpg.stab_sound_limit -= 1
                        self.stab_damage -= self.stab_damage
                    #print('hit with attack')

                if rpg.level_stuff.boss_type == 'wolf':
                    n = 0
                    m = len(rpg.level_stuff.level_1_boss.wolf_list) - 1
                    while n <= m:
                        collisions_test = self.rect_attack_down.colliderect(rpg.level_stuff.level_1_boss.wolf_list[n])
                        if collisions_test:
                            #print('hit right')
                            rpg.level_stuff.level_1_boss.wolf_list[n].health -= self.stab_damage
                            
                            if rpg.stab_sound_limit > 0:   
                                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.stab_sound)
                                rpg.overlay.create_damage_for_overlay(self.stab_damage,self.rect_attack_down.center,'cyan')
                                self.stab_damage -= self.stab_damage
                                rpg.stab_sound_limit -= 1
                        n += 1


    def check_throw_timer(self):
        """"""
        if self.throw_timer_delay != self.throw_timer_delay_old:
            self.throw_timer_delay -= 1
            if self.throw_timer_delay <= 0:
                self.throw_timer_delay = self.throw_timer_delay_old

    def attack_cycle(self,rpg):
        """This will be the loops for the attack animation and damage"""
        self.check_health(rpg)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]: # J
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
            #rpg.overlay.create_damage_for_overlay(rpg.level_stuff.particle_list_1[1].damage,rect_particle.center,'cyan')
        if keys[pygame.K_k]: # K
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_h]: # H
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_b]: # B
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_l]: # L
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_q]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_e]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_z]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_x]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_c]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_f]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_CAPSLOCK]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_CAPSLOCK]:
            self.health -= 1
            rpg.overlay.create_damage_for_overlay(1,self.rect_2.center,'red')
        if keys[pygame.K_o]:
            #print('You pressed o')
            self.prep_mis_click_o_exit(rpg)
            self.draw_misclick_message()
            pygame.display.update()
            pygame.time.delay(5000)
            rpg.game = False

        if keys[pygame.K_n]:
            """n will be for attack direct 1 for now."""
            if self.attack_active == False and self.block_active == False:
                self.attack_animation(rpg)
                if self.animation_last == 'right':
                    self.animation_counter = 63
                if self.animation_last == 'left':
                    self.animation_counter = 45
                if self.animation_last == 'down':
                    self.animation_counter = 54
                if self.animation_last == 'up':
                    self.animation_counter = 36
                if self.attack_direct_1_counter == self.attack_direct_1_counter_old:
                    self.attack_direct_1_counter -= 1
        if self.attack_direct_1_counter < self.attack_direct_1_counter_old:
            if self.attack_direct_1_counter < self.attack_direct_1_counter_old - 3:
                self.attack_sword_1(rpg)
            if self.animation_delay <=0:
                self.attack_direct_1_counter -= 1
            if self.attack_direct_1_counter <= 0:
                self.attack_direct_1_counter = self.attack_direct_1_counter_old
    
    def prep_mis_click_o_exit(self,rpg):
        """When the player pressed o this will display a message explaining what happened."""
        self.misclick_message = rpg.font.render("You pressed 'o', you lose, exiting now.",True,rpg.text_color,'White')
        self.misclick_message_rect = self.misclick_message.get_rect()
        self.misclick_message_rect.center = rpg.screen_rect.center
        
    def draw_misclick_message(self):
        """This displays the message."""
        self.screen.blit(self.misclick_message,self.misclick_message_rect)

    def prep_game_over(self,rpg):
        game_over_words = 'Game Over!'
        self.game_over = rpg.font.render(game_over_words,True,rpg.text_color,'red')
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = rpg.screen_rect.center
        self.game_over_rect.centery -= 200
    
    def block_cycle(self):
        """This holds the block logic."""
        if self.block_active:
            self.block_active_timer -= 1
            self.armor = 200
            self.friction_slowdown = 0.5
            if self.block_active_timer <= 0:
                self.block_active_timer = self.block_active_timer_old
                self.block_active = False
                self.armor = 1
                self.friction_slowdown = 0.9
            
    def check_health(self,rpg):
        """This checks the player health to see if the player loses"""
        if self.health <= 0 and self.extra_life_invoked == False:

            rpg.high_score_stuff.add_score(rpg.level_stuff.player_1.score) # this adds the score.
            rpg.high_score_stuff.update_top_scores()
            rpg.high_score_stuff.save_top_scores(rpg)
            
            #self.screen.blit(self.game_over,self.game_over_rect)
            #rpg.campagne_mode = False
            #rpg.game_over_screen = True
            pygame.mouse.set_visible(True)
            self.death_animation_active = True
        if self.health <= 0 and self.extra_life_invoked:
            self.health = 100
            self.extra_life_invoked = False
    
    def draw_for_credits(self,x,y):
        """This draws the player on screen for a cut scene"""
        self.screen.blit(self.sprite_sheet_player_1.surface_list[self.cut_scene_animation_counter],(x,y))

    def draw_for_cut_scene(self):
        """This draws the player on screen for a cut scene"""
        self.screen.blit(self.sprite_sheet_player_1.surface_list[self.cut_scene_animation_counter],self.rect_2)

    def draw_me(self,rpg):
        hypotenuse = ((self.velocity[0]**2) + (self.velocity[1]**2))**0.5
        a = self.velocity[0]**2
        b = self.velocity[1]**2
        highest = max(a,b)
        speed_trigger = 50
        if highest == a:
            if self.velocity[0] > 0:
                self.highest = 'right'
                self.previous_direction = self.highest
            if self.velocity[0] < 0:
                self.highest = 'left'
                self.previous_direction = self.highest
        if highest == b:
            if self.velocity[1] > 0:
                self.highest = 'down'
                self.previous_direction = self.highest
            if self.velocity[1] < 0:
                self.highest = 'up'
                self.previous_direction = self.highest
                # dop this
        if self.velocity[0] == 0 and self.velocity[1] == 0:
            self.highest = self.previous_direction
        right_start = 99
        left_start = 81
        up_start = 72
        down_start = 90
        if self.attack_active == False:
            match self.highest:
                case 'right':
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'right':
                            if self.animation_counter  < (right_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.footstep_sound_countdown -= 1
                                    if self.footstep_sound_countdown <= 0:
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left' # more birds nests
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (right_start + self.animation_length_walk):
                                self.animation_counter = right_start
                        if self.animation_last != 'right':
                            self.animation_counter = right_start
                            self.animation_last = 'right'
                case 'left':
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'left':
                            if self.animation_counter  < (left_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.footstep_sound_countdown -= 1
                                    if self.footstep_sound_countdown <= 0:
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left' # eagles nest
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (left_start + self.animation_length_walk):
                                self.animation_counter = left_start
                        if self.animation_last != 'left':
                            self.animation_counter = left_start
                            self.animation_last = 'left'
            # right is 27, left is 9, down is 18, up is 0
                case 'down':
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'down':
                            if self.animation_counter  < (down_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.footstep_sound_countdown -= 1
                                    if self.footstep_sound_countdown <= 0: # nested list
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left'
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (down_start + self.animation_length_walk):
                                self.animation_counter = down_start
                        if self.animation_last != 'down':
                            self.animation_counter = down_start
                            self.animation_last = 'down'
                case 'up':
                    if hypotenuse >= speed_trigger:
                        if self.animation_last == 'up':
                            if self.animation_counter  < (up_start + self.animation_length_walk):
                                if self.animation_delay <=0:
                                    self.animation_counter += 1
                                    self.footstep_sound_countdown -= 1
                                    if self.footstep_sound_countdown <= 0:
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left' # embarrassing
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                    self.animation_delay = self.animation_delay_start
                                if self.animation_delay > 0:
                                    self.animation_delay -= 1
                            if self.animation_counter >= (up_start + self.animation_length_walk):
                                self.animation_counter = up_start
                        if self.animation_last != 'up':
                            self.animation_counter = up_start
                            self.animation_last = 'up'
        right_start = 63
        left_start = 45
        up_start = 36
        down_start = 54
        if self.attack_active == True:
            match self.highest:
                case 'right':
                    if self.animation_last == 'right':
                        if self.animation_counter  < (right_start + self.attack_length):
                            if self.animation_delay <=0:
                                self.animation_counter += 1
                                self.footstep_sound_countdown -= 1
                                if self.footstep_sound_countdown <= 0:
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left'# nest goes here
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                self.animation_delay = self.animation_delay_start
                            if self.animation_delay > 0:
                                self.animation_delay -= 1
                        if self.animation_counter >= (right_start + self.attack_length):
                            self.animation_counter = right_start + 36
                            self.attack_active = False
                            rpg.overlay.display_attack_1 = True
                    if self.animation_last != 'right':
                        self.animation_counter = right_start 
                        self.animation_last = 'right'
                case 'left':
                    #if hypotenuse >= speed_trigger:
                    if self.animation_last == 'left':
                        if self.animation_counter  < (left_start +self.attack_length):
                            if self.animation_delay <=0:
                                self.animation_counter += 1
                                self.footstep_sound_countdown -= 1
                                if self.footstep_sound_countdown <= 0:
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left' # jokes getting old
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                self.animation_delay = self.animation_delay_start
                            if self.animation_delay > 0:
                                self.animation_delay -= 1
                        if self.animation_counter >= (left_start + self.attack_length):
                            self.animation_counter = left_start + 36
                                #print('attack ends', self.animation_counter, left_start, self.attack_length)
                            self.attack_active = False
                            rpg.overlay.display_attack_1 = True
                    if self.animation_last != 'left':
                        self.animation_counter = left_start
                        self.animation_last = 'left'
            # right is 27, left is 9, down is 18, up is 0
                case 'down':
                    #if hypotenuse >= speed_trigger:
                    if self.animation_last == 'down':
                        if self.animation_counter  < (down_start + self.attack_length):
                            if self.animation_delay <=0:
                                self.animation_counter += 1
                                self.footstep_sound_countdown -= 1
                                if self.footstep_sound_countdown <= 0:
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left' # overpopulation of birds
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                self.animation_delay = self.animation_delay_start
                            if self.animation_delay > 0:
                                self.animation_delay -= 1
                        if self.animation_counter >= (down_start + self.attack_length):
                            self.animation_counter = down_start + 36
                            self.attack_active = False
                            rpg.overlay.display_attack_1 = True
                                #print('attack ends', self.animation_counter, left_start, self.attack_length)
                    if self.animation_last != 'down':
                        self.animation_counter = down_start
                        self.animation_last = 'down'
                case 'up':
                    #if hypotenuse >= speed_trigger:
                    if self.animation_last == 'up':
                        if self.animation_counter  < (up_start + self.attack_length):
                            if self.animation_delay <=0:
                                self.animation_counter += 1
                                self.footstep_sound_countdown -= 1
                                if self.footstep_sound_countdown <= 0:
                                        if self.footstep_next == 'right':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound)
                                            self.footstep_next = 'left'
                                        if self.footstep_next == 'left':
                                            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.footstep_sound_2)
                                            self.footstep_next = 'right'
                                        self.footstep_sound_countdown = self.footstep_sound_countdown_old
                                self.animation_delay = self.animation_delay_start
                            if self.animation_delay > 0:
                                self.animation_delay -= 1
                        if self.animation_counter >= (up_start + self.attack_length):
                            self.animation_counter = up_start + 36
                            self.attack_active = False
                            rpg.overlay.display_attack_1 = True
                    if self.animation_last != 'up':
                        self.animation_counter = up_start
                        self.animation_last = 'up'
        #pygame.draw.ellipse(self.screen,(2,48,32),self.rect)
        #self.screen.blit(self.shadow_surface,self.rect)
        self.screen.blit(self.sprite_sheet_player_1.surface_list[self.animation_counter],self.rect_2)
        #x_distance =  rpg.level_stuff.level_1_boss.rect_2.centerx - self.rect.centerx 
        #y_distance =  rpg.level_stuff.level_1_boss.rect_2.centery - self.rect.centery 
        #pygame.draw.line(self.screen,'white',self.rect.center,(self.rect.centerx + (x_distance / 100),self.rect.centery + (y_distance / 100)))
        #pygame.draw.rect(self.screen,(0,0,200),self.rect_2)
        #pygame.draw.rect(self.screen,(0,200,200),self.rect)

    def attack_animation(self,rpg):
        """this will be the logic for the attack animation"""
        if self.attack_direct_1_counter < self.attack_direct_1_counter_old:
            self.attack_active = True
            rpg.overlay.display_attack_1 = False
            self.stab_damage = 10
            rpg.stab_sound_limit = 1
            if rpg.level_stuff.sound_logic.grunt_sound.get_volume() > rpg.settings_hold.max_volume:
                rpg.level_stuff.sound_logic.grunt_sound.set_volume(rpg.settings_hold.max_volume)
            pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.grunt_sound)



class NPC_character(Sprite,Physics_stats):
    """This is the class for NPc's. i put it in with the player class."""

    def __init__(self,rpg,text_temp,location_temp):
        Physics_stats.__init__(self,rpg)
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        super().__init__()

        # the above should work.
        # text_temp will most likely be a list.
        self.text = text_temp
        self.location = location_temp
        self.map_x_location = location_temp[0] # this is for the map. 
        self.map_y_location = location_temp[1]

        # font and other stuff
        #self.text_color =  (82, 54, 31)
        #self.bg_color = (31, 59, 82)
        #self.font = pygame.font.SysFont('vinerhanditc',48)
        self.font_character = pygame.font.SysFont('candara',25) # candara works.
        self.text_color_character = (255,255,255)
        self.bg_color_character = (0,0,0)

    def prepare_text(self,rpg,index_to_prep):
        """this prepares the text for display."""
        length_text = len(self.text[index_to_prep])
        distance_to_render = 100
        m = length_text/distance_to_render
        m = int(m)
        n = 0
        self.rendered_text = [] # list for storing finished text.
        self.rendered_text_rect = []
        self.length_text_rows = 0

        while n < (m + 1):
            """This loops through text to render it line by line."""
            a = self.font_character.render(self.text[index_to_prep][(length_text * n):(length_text * n + 1)],False,self.text_color_character,self.bg_color_character)
            self.rendered_text.append(a)
            b = a.get_rect()
            self.rendered_text_rect.append(b)
            self.length_text_rows += 1
            n += 1

        

    def create_background_for_text(self,rpg):
        """This is the background underneath the text."""

        self.rect_for_background = pygame.Rect(width=200, height=(self.length_text_rows * 30) )
        self.rect_for_background.midbottom = self.screen_rect.midbottom
        self.rect_for_background.centery -= 50


    def display_text(self,rpg):
        """This displays the characters text on screen."""
        # i will test having the text in a box at the bottom of the screen
        # and i will test having the text at the location of the character.
        # the game will pause while you read/talk to the character.


