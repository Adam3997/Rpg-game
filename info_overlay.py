import pygame
from sprite_sheet_animater import Sprite_loader

class Info_overlay():
    """This is the overlay of information for the player. Like health"""

    def __init__(self,rpg):
        """initialize the variable"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.overlay_color = (74,4,4)
        self.red_text = (226,223,210)
        self.font_overlay = pygame.font.SysFont(None,32)
        self.icons = Sprite_loader('_internal\\sheet_white1x.png',4)
        self.rect_1 = self.icons.surface_list[1].get_rect()
        self.rect_2 = self.icons.surface_list[1].get_rect()
        self.rect_3 = self.icons.surface_list[1].get_rect()
        size = self.screen.get_width()
        size = size/2
        self.rect_1.bottom = rpg.screen_rect.bottom
        self.rect_1.x += (size - 80)
        self.rect_2.bottom = rpg.screen_rect.bottom
        self.rect_2.x += size
        self.rect_3.bottom = rpg.screen_rect.bottom
        self.rect_3.x += (size + 80)
        self.display_attack_1 = True
        self.display_attack_2 = True
        self.display_attack_3 = True

        self.damage_list = []
        self.damage_list_timer = []
        #self.damage_list_color = []
        self.damage_list_rects = []

        #self.font_damage = pygame.font.SysFont('frenchscript',30)
        self.font_damage = pygame.font.SysFont('arialblack',30)
        # create the stuff
        self.update_overlay(rpg=rpg)



    def update_overlay(self,rpg):
        """This updates the info in the overlay"""
        player_health = 'Player Health: '
        score = 'Score: '
        #print(rpg.player_1.score)
        time_info = 'Time: '
        # add information to string
        player_health += str(int(rpg.level_stuff.player_1.health))
        #score += str(int(rpg.level_stuff.player_1.score))   #  f"{num:,}"
        score += f"{int(rpg.level_stuff.player_1.score):,}"
        time_info += str(round(rpg.time_tracker,1))
        #create overlay here
        self.player_health = self.font_overlay.render(player_health,True,self.red_text,self.overlay_color)
        self.score = self.font_overlay.render(score,True,self.red_text,self.overlay_color)
        self.time_info = self.font_overlay.render(time_info,True,self.red_text,self.overlay_color)
        # create rect
        self.player_health_rect = self.player_health.get_rect()
        self.score_rect = self.score.get_rect()
        self.time_info_rect = self.time_info.get_rect()
        # set rect location
        self.player_health_rect.topright = rpg.screen_rect.topright
        self.score_rect.topright = self.player_health_rect.bottomright
        self.time_info_rect.topright = self.player_health_rect.bottomright

        n = 0
        m = len(self.damage_list_timer) - 1
        while n <= m:
            self.damage_list_timer[n] -= 1
            if self.damage_list_timer[n] <= 0:
                self.damage_list.remove(self.damage_list[n])
                self.damage_list_timer.remove(self.damage_list_timer[n])
                self.damage_list_rects.remove(self.damage_list_rects[n])
                m -= 1
            n += 1

    def create_damage_for_overlay(self,damage,location,color):
        """This is for damage to prepare to show on screen"""

        #surface_hold = pygame.Surface()
        text_hold = str(damage)
        #text_hold_rect = text_hold.get_rect()

        text_hold = self.font_damage.render(text_hold,True,color,(0,0,0))
        text_hold_rect = text_hold.get_rect()
        surface_hold = pygame.Surface((text_hold_rect.width,text_hold_rect.height))
        surface_hold.blit(text_hold,(0,0))
        surface_hold.set_colorkey((0,0,0))
        text_hold_rect.center = location
        self.damage_list.append(surface_hold)
        self.damage_list_rects.append(text_hold_rect)
        self.damage_list_timer.append(100)


    def update_damage(self,rpg):
        """This updates the damage list which holds all the damage info that is put on screen."""

        n = 0
        m = len(self.damage_list_rects)- 1
        while (n <= m) and m >= 0:
            self.damage_list_rects[n].centerx -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            self.damage_list_rects[n].centery -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            n += 1

    def draw_overlay(self,rpg):
        rpg.screen.blit(self.player_health,self.player_health_rect)
        rpg.screen.blit(self.score,self.score_rect)
        if self.display_attack_1:
            rpg.screen.blit(self.icons.surface_list[11],self.rect_1)
        if self.display_attack_2:
            rpg.screen.blit(self.icons.surface_list[0],self.rect_2)
        if self.display_attack_3:
            rpg.screen.blit(self.icons.surface_list[27],self.rect_3)
        n = 0
        m = len(self.damage_list) - 1
        while (n <= m) and m >= 0:
            rpg.screen.blit(self.damage_list[n],self.damage_list_rects[n])
            n += 1