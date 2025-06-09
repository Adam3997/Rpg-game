import json
from pathlib import Path
from button import Button
import pygame

class Settings():
    """This will hold the settings for the game
    This includes the screen size, and any other settings."""

    def __init__(self,rpg):
        """This initializes the settings for the game"""

        self.load_settings(rpg)
        self.cofee_brown = (111,78,55)
        self.fallow_brown = (193,154,107)
        self.text_color = self.fallow_brown
        self.text_background_color = self.cofee_brown

        self.button_click_delay = 10
        self.button_click_delay_old = self.button_click_delay
        

    def create_setting_screen(self,rpg):
        """"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        quarter = self.screen.get_rect().height
        quarter /= 4

        sixth = self.screen.get_rect().height
        sixth /= 6

        tenth = self.screen.get_rect().height
        tenth /= 10

        tenth_width = self.screen.get_rect().width
        tenth_width /= 20

        eighth_width = self.screen.get_rect().width
        eighth_width /= 8

        sixth_width = self.screen.get_rect().width
        sixth_width /= 6

        self.button_1080 = Button(rpg,'1080p',1)
        self.button_1080.msg_image_rect.x += tenth_width
        self.button_1080.msg_image_rect.y = sixth
        self.button_720 = Button(rpg,'720p',1)
        self.button_720.msg_image_rect.x -= tenth_width
        self.button_720.msg_image_rect.y = sixth
        
        
        self.button_volume_plus_1 = Button(rpg,'+ 1',1)
        self.button_volume_plus_1.msg_image_rect.y = sixth + tenth
        self.button_volume_plus_1.msg_image_rect.x += tenth_width
        self.button_volume_minus_1 = Button(rpg,'- 1',1)
        self.button_volume_minus_1.msg_image_rect.y = sixth + tenth
        self.button_volume_minus_1.msg_image_rect.x -= tenth_width
        self.button_volume_plus_10 = Button(rpg,'+ 10',1)
        self.button_volume_plus_10.msg_image_rect.y = sixth + tenth
        self.button_volume_plus_10.msg_image_rect.x += 2 * tenth_width
        self.button_volume_minus_10 = Button(rpg,'- 10',1)
        self.button_volume_minus_10.msg_image_rect.y = sixth + tenth
        self.button_volume_minus_10.msg_image_rect.x -= 2 * tenth_width

        self.button_voice_plus_1 = Button(rpg,'+ 1',1)
        self.button_voice_plus_1.msg_image_rect.y = sixth + (2* tenth)
        self.button_voice_plus_1.msg_image_rect.x += tenth_width
        self.button_voice_minus_1 = Button(rpg,'- 1',1)
        self.button_voice_minus_1.msg_image_rect.y = sixth + (2* tenth)
        self.button_voice_minus_1.msg_image_rect.x -= tenth_width
        self.button_voice_plus_10 = Button(rpg,'+ 10',1)
        self.button_voice_plus_10.msg_image_rect.y = sixth + (2* tenth)
        self.button_voice_plus_10.msg_image_rect.x += 2 * tenth_width
        self.button_voice_minus_10 = Button(rpg,'- 10',1)
        self.button_voice_minus_10.msg_image_rect.y = sixth + (2* tenth)
        self.button_voice_minus_10.msg_image_rect.x -= 2 * tenth_width

        self.button_background_plus_1 = Button(rpg,'+ 1',1)
        self.button_background_plus_1.msg_image_rect.y =  sixth + (3*tenth)
        self.button_background_plus_1.msg_image_rect.x += tenth_width
        self.button_background_minus_1 = Button(rpg,'- 1',1)
        self.button_background_minus_1.msg_image_rect.y =  sixth + (3*tenth)
        self.button_background_minus_1.msg_image_rect.x -= tenth_width
        self.button_background_plus_10 = Button(rpg,'+ 10',1)
        self.button_background_plus_10.msg_image_rect.y =  sixth + (3*tenth)
        self.button_background_plus_10.msg_image_rect.x += 2 * tenth_width
        self.button_background_minus_10 = Button(rpg,'- 10',1)
        self.button_background_minus_10.msg_image_rect.y =  sixth + (3*tenth)
        self.button_background_minus_10.msg_image_rect.x -= 2 * tenth_width
        
        self.font_settings = pygame.font.SysFont('vinerhanditc',28)
        self.current_volume = self.font_settings.render(str(self.max_volume*100),True,self.text_color,self.text_background_color)
        self.current_volume_rect = self.current_volume.get_rect()
        self.current_volume_rect.center = self.screen_rect.center
        self.current_volume_rect.y = sixth + tenth

        self.current_volume_voice = self.font_settings.render(str(self.dialogue_volume*100),True,self.text_color,self.text_background_color)
        self.current_volume_rect_voice = self.current_volume_voice.get_rect()
        self.current_volume_rect_voice.center = self.screen_rect.center
        self.current_volume_rect_voice.y = sixth + 2*tenth

        self.current_volume_background = self.font_settings.render(str(self.background_volume*100),True,self.text_color,self.text_background_color)
        self.current_volume_rect_background = self.current_volume_background.get_rect()
        self.current_volume_rect_background.center = self.screen_rect.center
        self.current_volume_rect_background.y = sixth + 3 * tenth

        self.change_difficulty_button = Button(rpg,'Change Difficulty',1)
        if self.difficulty == 1.0:
            self.difficulty_display = self.font_settings.render('Normal',True,self.text_color,self.text_background_color)
        elif self.difficulty == 2.0:
            self.difficulty_display = self.font_settings.render('Hard',True,self.text_color,self.text_background_color)
        elif self.difficulty == 0.5:
            self.difficulty_display = self.font_settings.render('Easy',True,self.text_color,self.text_background_color)

    def update_volume_text(self):
        """"""
        a = self.max_volume * 100
        a = round(a,0)
        b = self.dialogue_volume * 100
        b = round(b,0)
        c = self.background_volume * 100
        c = round(c,0)
        self.current_volume = self.font_settings.render(str(a),True,self.text_color,self.text_background_color)
        self.current_volume_voice = self.font_settings.render(str(b),True,self.text_color,self.text_background_color)
        self.current_volume_background = self.font_settings.render(str(c),True,self.text_color,self.text_background_color)
        #self.current_volume_rect = self.current_volume.get_rect()
        #self.current_volume_rect.center = self.screen_rect.center

    def save_settings(self,rpg):
        """path = Path('high_scores_save.json')
        contents = json.dumps(self.top_score_list)
        path.write_text(contents)"""
        path = Path('Settings_file.json')
        
        contents = json.dumps((self.full_screen,self.resolution_1080p,self.resolution_720p,self.max_volume,self.dialogue_volume,self.background_volume,self.difficulty))
        path.write_text(contents)
        

    def load_settings(self,rpg):
        """"""
        path = Path('Settings_file.json')
        try:
            contents = path.read_text()
            information_loaded = json.loads(contents)
            self.full_screen = information_loaded[0]
            self.resolution_1080p = information_loaded[1]
            self.resolution_720p = information_loaded[2]
            self.max_volume = information_loaded[3]
            self.dialogue_volume = information_loaded[4]
            self.background_volume = information_loaded[5]
            self.difficulty = information_loaded[6]


        except:
            self.full_screen = True
            self.resolution_1080p = True
            self.resolution_720p = False
            self.max_volume = 1.0
            self.dialogue_volume = 1.0
            self.background_volume = 1.0
            self.difficulty = 1.0  # 1.0 is normal, 2.0 is hard, 0.5 is easy. 
            self.save_settings(rpg)


    def draw_settings_screen(self,rpg):
        """"""
        self.update_volume_text()
        if self.button_click_delay != self.button_click_delay_old:
            self.button_click_delay -= 1
        if self.button_click_delay <= 0:
            self.button_click_delay = self.button_click_delay_old


        self.button_1080.draw_button()
        self.button_720.draw_button()
        self.button_background_minus_1.draw_button()
        self.button_background_minus_10.draw_button()
        self.button_background_plus_1.draw_button()
        self.button_voice_minus_1.draw_button()
        self.button_background_plus_10.draw_button()
        self.button_voice_plus_1.draw_button()
        self.button_voice_plus_10.draw_button()
        self.button_voice_minus_10.draw_button()
        self.button_volume_minus_1.draw_button()
        self.button_volume_minus_10.draw_button()
        self.button_volume_plus_1.draw_button()
        self.button_volume_plus_10.draw_button()
        self.screen.blit(self.current_volume,self.current_volume_rect)
        self.screen.blit(self.current_volume_voice,self.current_volume_rect_voice)
        self.screen.blit(self.current_volume_background,self.current_volume_rect_background)

        #self.main_menu_stuff.return_main_menu_button.draw_button()



    def _check_button_background_minus_1(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_background_minus_1.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.background_volume -= 0.01
            if self.background_volume < 0:
                self.background_volume = 0
            
            self.button_click_delay -= 1

    def _check_button_background_minus_10(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_background_minus_10.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.background_volume -= 0.1
            if self.background_volume < 0:
                self.background_volume = 0
            
            self.button_click_delay -= 1


    def _check_button_background_plus_1(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_background_plus_1.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.background_volume += 0.01
            if self.background_volume > 1:
                self.background_volume = 1
            
            self.button_click_delay -= 1
    
    def _check_button_background_plus_10(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_background_plus_10.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.background_volume += 0.1
            if self.background_volume > 1:
                self.background_volume = 1
            
            self.button_click_delay -= 1

    

    def _check_button_volume_plus_1(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_volume_plus_1.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.max_volume += 0.01
            if self.max_volume > 1:
                self.max_volume = 1
            
            self.button_click_delay -= 1

    def _check_button_volume_plus_10(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_volume_plus_10.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.max_volume += 0.1
            if self.max_volume > 1:
                self.max_volume = 1
            
            self.button_click_delay -= 1
            

    def _check_button_volume_minus_1(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_volume_minus_1.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.max_volume -= 0.01
            if self.max_volume < 0:
                self.max_volume = 0
            
            self.button_click_delay -= 1

    def _check_button_volume_minus_10(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_volume_minus_10.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.max_volume -= 0.1
            if self.max_volume < 0:
                self.max_volume = 0
            
            self.button_click_delay -= 1

    def _check_button_dialogue_minus_1(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_voice_minus_1.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.dialogue_volume -= 0.01
            if self.dialogue_volume < 0:
                self.dialogue_volume = 0
            
            self.button_click_delay -= 1
    
    def _check_button_dialogue_minus_10(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_voice_minus_10.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.dialogue_volume -= 0.1
            if self.dialogue_volume < 0:
                self.dialogue_volume = 0
            
            self.button_click_delay -= 1

    def _check_button_dialogue_plus_1(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_voice_plus_1.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.dialogue_volume += 0.01
            if self.dialogue_volume > 1:
                self.dialogue_volume = 1
            
            self.button_click_delay -= 1

    def _check_button_dialogue_plus_10(self,rpg,mouse_pos):
        """this checks if yuou hit the button """
        button_clicked = self.button_voice_plus_10.msg_image_rect.collidepoint(mouse_pos)
        if button_clicked and rpg.main_menu_stuff.settings_menu and self.button_click_delay == self.button_click_delay_old:
            self.dialogue_volume += 0.1
            if self.dialogue_volume > 1:
                self.dialogue_volume = 1
            
            self.button_click_delay -= 1







            
