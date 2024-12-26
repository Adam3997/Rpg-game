import pygame
from button import Button
import random


class Fighting_logcic():
    """This is the class that holds the fight logic and interactions"""

    def __init__(self,rpg,fighter_1,fighter_2):
        """Initialize the class"""
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.screen_rect = rpg.screen.get_rect()
        self.screen = rpg.screen

        n = 60
        x_change = 150
        self.attack_1_button = Button(self,rpg.starter_character.deck_list2[0].name,2)
        self.attack_1_button.rect.y += 100
        self.attack_1_button.rect.x += x_change
        self.attack_1_button.prep_msg(rpg.starter_character.deck_list2[0].name)

        self.attack_2_button = Button(self,rpg.starter_character.deck_list2[ 1].name,2)
        
        self.attack_2_button.rect.y += 100 + n
        self.attack_2_button.rect.x += x_change
        self.attack_2_button.prep_msg(rpg.starter_character.deck_list2[ 1].name)

        self.attack_3_button = Button(self,rpg.starter_character.deck_list2[ 2].name,2)
        self.attack_3_button.rect.y += 100 +  n*2
        self.attack_3_button.rect.x += x_change
        self.attack_3_button.prep_msg(rpg.starter_character.deck_list2[ 2].name)

        self.attack_4_button = Button(self,rpg.starter_character.deck_list2[3].name,2)
        self.attack_4_button.rect.y += 100 +  n*3
        self.attack_4_button.rect.x += x_change
        self.attack_4_button.prep_msg(rpg.starter_character.deck_list2[3].name)



    
    def reset_stats(self,rpg):
        rpg.starter_character.health = 30
        rpg.enemy1.health = 30

    def health_check(self,rpg): # replace the selfs with rpg 
        """"""
        if rpg.starter_character.health <= 0:
            #rpg.start_menu = False
            #rpg.opening_menu = True
            self.reset_stats(rpg)
            rpg.enemy1.create_deck()
            rpg.starter_character.create_deck()
            self.update_infoboard(rpg)
            rpg.campagne_fight= False
            return
        if rpg.enemy1.health <= 0:
            #rpg.start_menu = False
            #rpg.opening_menu = True
            #print('Computer loses')
            rpg.enemy1.create_deck()
            rpg.starter_character.create_deck()
            self.reset_stats(rpg)
            self.update_infoboard(rpg)
            #collissions = pygame.sprite.groupcollide(rpg.player1,rpg.enemy_list,False,True)
            #print(len(collissions), ' is the len of collission in health check')
            #print(collissions[0])

            #del collissions[0]
            #print(len(collissions))
            #collissions[0].delete_me()
            rpg.campagne_fight = False

            return
        
    def update_infoboard(self,rpg):
        """"""
        words2 = 'Health: '
        words2 += str(rpg.starter_character.health)
        info_color = 'yellow'

        #self.game_over = self.font.render(words1,True,self.text_color,'gray')
        #self.game_over_rect = self.game_over.get_rect()
        self.health_1 = rpg.font.render(words2,True,rpg.text_color,info_color)
        self.health_1_rect = self.health_1.get_rect()
        #self.health_1_rect.topleft = self.screen_rect.topleft
        self.health_1_rect.midbottom = rpg.starter_character.rect.midtop


        words3 = 'Health: '
        words3 += str(rpg.enemy1.health)
        self.health_2 = rpg.font.render(words3,True,rpg.text_color,info_color)
        self.health_2_rect = self.health_2.get_rect()
        #self.health_2_rect.topright = self.screen_rect.topright
        self.health_2_rect.midbottom = rpg.enemy1.rect.midtop

    def draw_infoboard(self,rpg):
        """"""
        rpg.screen.blit(self.health_1,self.health_1_rect)
        rpg.screen.blit(self.health_2,self.health_2_rect)
        
    def play_attack(self,rpg):
        """"""
        rpg.animation_timer = 0
    

    
    def _check_attack_1_button(self,rpg,mouse_pos):
        """"""
        button_clicked = self.attack_1_button.rect.collidepoint(mouse_pos)
        #print('button 1 check')
        if len(rpg.starter_character.deck_list2) < 1:
            print(len(rpg.starter_character.deck_list1))
            return

        if button_clicked and rpg.campagne_fight:
            """""" 
             
            #attack happens
            rpg.enemy1.health -= rpg.starter_character.deck_list2[0].attack
            rpg.starter_character.health += rpg.starter_character.deck_list2[0].health
            if rpg.starter_character.deck_list2[0].attack > 0:
                """"""
                #self.play_attack()
                #self.starter_character.attack_sound()
            if rpg.starter_character.deck_list2[0].name == 'start fire':
                """"""
                rpg.starter_character.fire_attack(rpg)
            del rpg.starter_character.deck_list2[0]
            self.enemy_attack(rpg)
            self.update_infoboard(rpg)
             
            

            rpg.turn += 1
    def _check_attack_2_button(self,rpg,mouse_pos):
        """"""
        button_clicked = self.attack_2_button.rect.collidepoint(mouse_pos)
        if len(rpg.starter_character.deck_list2) <= 2:
            return

        if button_clicked and rpg.campagne_fight:
            """""" 
            #attack happens
            rpg.enemy1.health -= rpg.starter_character.deck_list2[1].attack
            rpg.starter_character.health += rpg.starter_character.deck_list2[1].health
            if rpg.starter_character.deck_list2[1].attack > 0:
                """"""
                #self.play_attack()
                #self.starter_character.attack_sound()
            if rpg.starter_character.deck_list2[1].name == 'start fire':
                """"""
                rpg.starter_character.fire_attack(rpg)
            del rpg.starter_character.deck_list2[1]
            self.enemy_attack(rpg)
            self.update_infoboard(rpg)
            #self.starter_character.attack_sound()
            
            

            rpg.turn += 1
    def _check_attack_3_button(self,rpg,mouse_pos):
        """"""
        button_clicked = self.attack_3_button.rect.collidepoint(mouse_pos)
        if len(rpg.starter_character.deck_list2) <= 3:
            return

        if button_clicked and rpg.campagne_fight:
            """""" 
            #attack happens
            rpg.enemy1.health -= rpg.starter_character.deck_list2[2].attack
            rpg.starter_character.health += rpg.starter_character.deck_list2[2].health
            if rpg.starter_character.deck_list2[2].attack > 0:
                """"""
                #self.play_attack()
                #self.starter_character.attack_sound()

            if rpg.starter_character.deck_list2[2].name == 'start fire':
                """"""
                rpg.starter_character.fire_attack(rpg)
            del rpg.starter_character.deck_list2[2]
            self.enemy_attack(rpg)
            self.update_infoboard(rpg)
            
            

            rpg.turn += 1
    def _check_attack_4_button(self,rpg,mouse_pos):
        """"""
        button_clicked = self.attack_4_button.rect.collidepoint(mouse_pos)
        if len(rpg.starter_character.deck_list2) <= 4:
            return

        if button_clicked and rpg.campagne_fight:
            """""" 
            #attack happens
            rpg.enemy1.health -= rpg.starter_character.deck_list2[3].attack
            rpg.starter_character.health += rpg.starter_character.deck_list2[3].health
            if rpg.starter_character.deck_list2[3].attack > 0:
                """"""
                #self.play_attack()
                #self.starter_character.attack_sound()

            if rpg.starter_character.deck_list2[3].name == 'start fire':
                """"""
                rpg.starter_character.fire_attack(rpg)
            del rpg.starter_character.deck_list2[3]

            self.enemy_attack(rpg)

            self.update_infoboard(rpg)
            
            

            rpg.turn += 1

    def enemy_attack(self,rpg):
        """"""
        n = random.choice([0,1,2,3])
        rpg.starter_character.health -= rpg.enemy1.deck_list2[n].attack
        if rpg.enemy1.deck_list2[n].attack > 0:
                """""" 
                #self.play_attack2()
                #self.enemy1.attack_sound()
        del rpg.enemy1.deck_list2[n]
        
    def play_attack2(self,rpg):
        """"""
        rpg.animation_timer2 = 0

    def check_events_fight(self,rpg):
        """"""
        for event in pygame.event.get():
            #print('events checked')
            if event.type == pygame.QUIT:
                rpg.game = False    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #print('mouse checked')
                mouse_pos = pygame.mouse.get_pos()
                rpg.fight_demo._check_attack_1_button(rpg,mouse_pos)
                rpg.fight_demo._check_attack_2_button(rpg,mouse_pos)
                rpg.fight_demo._check_attack_3_button(rpg,mouse_pos)
                rpg.fight_demo._check_attack_4_button(rpg,mouse_pos)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    rpg.game = False
    
    
    def draw_fight_screen(self,rpg):
        #print('draw_fight_screen')
        rpg.screen.fill(rpg.screen_color)
        rpg.fight_demo.health_check(rpg)
        rpg.starter_character.draw_me(rpg)
        rpg.starter_character.update_deck(rpg)
        rpg.fight_demo.attack_1_button.draw_button()
        rpg.fight_demo.attack_2_button.draw_button()
        rpg.fight_demo.attack_3_button.draw_button()
        rpg.fight_demo.attack_4_button.draw_button()
        rpg.enemy1.draw_me(rpg)
        rpg.fight_demo.draw_infoboard(rpg)

        if rpg.animation_timer <= rpg.animation_length:
            rpg.starter_character.attack_animation()
            rpg.animation_timer += 1
            if rpg.animation_timer % rpg.interval == 0:
                rpg.starter_character.animation_tracker += 1
                if rpg.starter_character.animation_tracker >= 5:
                    rpg.starter_character.animation_tracker = 0
        if rpg.animation_timer2 <= rpg.animation_length:
            rpg.enemy1.attack_animation_r()
            rpg.animation_timer2 += 1
            if rpg.animation_timer2 % rpg.interval == 0:
                rpg.enemy1.animation_tracker_r += 1
                if rpg.enemy1.animation_tracker_r >= 5:
                    rpg.enemy1.animation_tracker_r = 0
        if rpg.fire_attack > 0:
            rpg.starter_character.animation_countdown -= 1
            if rpg.starter_character.animation_countdown % 20 == 0:
                rpg.starter_character.animation_spark_track += 1
                if rpg.starter_character.animation_spark_track >= len(rpg.starter_character.fire_sprites):
                    rpg.starter_character.animation_spark_track = len(rpg.starter_character.fire_sprites) - 1
            rpg.starter_character.draw_fire(rpg)
                        #print('here')
            rpg.fire_attack -= 1


