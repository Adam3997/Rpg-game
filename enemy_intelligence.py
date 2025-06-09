import math
import pygame
import random

class Enemy_intelligence():
    """This will hold the intelligence of the enemies on the map."""
    def __init__(self,type_of_character):
        """"""

        self.history = []
        self.history.append((0,0,0,0,(0,0),0,0))
        self.time_to_action = 100
        self.time_to_action_old = self.time_to_action

        self.hypotenuse = 0.0
        self.x_dist = 0.0
        self.y_list = 0.0
        self.angle_to_player = 0.0

        self.x_diff = 0.0
        self.y_diff = 0.0

        self.decision = ''  
        self.time_of_day = 'Day'

        self.last_damage = 0

        self.L_delay_timer = 30
        self.L_delay_timer_old = self.L_delay_timer
        self.first_movement = ''
        self.movement_happened = False

        self.L_shape = False
        self.shape_1 = False

        self.type_of_character = str(type_of_character)

        self.L_scale = 10
        self.reg_scale = 6

        self.history_limit = 5000

        self.record_history = True


    def check_history_limit(self,rpg):
        """This checks to see if the size limit of the history list is  reached. """
        history_length = len(self.history)
        if history_length >= self.history_limit:
            self.record_history = False
            rpg.level_stuff.history_log.history.append(self.history)
    
    def update_info(self,rpg):
        """This updates the info the enemy "knows"""
        self.x_dist = rpg.level_stuff.player_1.rect.centerx - self.rect_picture.centerx
        self.y_dist = rpg.level_stuff.player_1.rect.centery - self.rect_picture.centery

        self.hypotenuse = ((self.x_dist**2) +(self.y_dist**2))**0.5
        if self.hypotenuse != 0:
            angle_temp = (self.y_dist / self.hypotenuse)
            self.angle_to_player = math.degrees(math.asin(angle_temp))


        

    def decide_L_or_l_movement(self,rpg): # this should work.
        """This is where the npc decides to make an 
        L manuever or move in a stright line towards player."""
        scale = self.L_scale
        
        if self.first_movement == ('left' or 'right'):
            if self.first_movement == 'left':
                self.dv_dt[0] += (self.x_dist * scale)
                #self.first_movement = ''
            if self.first_movement == 'right':
                self.dv_dt[1] += (self.y_dist * scale)
                #self.first_movement = ''
            self.first_movement = ''
            return
        choice_to_move = random.choice(['L','1','targeting'])
        
        match choice_to_move:
            case 'L':
                """"""
                choice_left_or_right = random.choice(['right','left'])
                if choice_left_or_right == 'right':
                    self.dv_dt[0] += (self.x_dist * scale)
                    self.first_movement = 'right'
                if choice_left_or_right == 'left':
                    self.dv_dt[1] += (self.y_dist * scale)
                    self.first_movement = 'left'
            case '1':
                """"""
                self.make_decision(rpg)
            case 'targeting':
                """This targets the player.
                This means it adds the distance vector to the players velocity vector.
                Multiply the number of seconds it takes to arrive by the vector to
                make it arrive in 1 second. """
                movement_x = self.x_dist + rpg.level_stuff.player_1.velocity[0]
                movement_y = self.y_dist + rpg.level_stuff.player_1.velocity[1]

                self.dv_dt[0] += movement_x
                self.dv_dt[1] += movement_y
                

    


    def make_decision(self,rpg,level_logic): # this is actually direct movement. will change name later.
        """This makes the deciison on what the enemy does"""

        if self.hypotenuse <= 1000:
            # then it will do something
            scale = self.reg_scale
            length = len(self.history)
            self.x_diff = self.x_dist - level_logic.history[length - 1][0]
            self.y_diff = self.x_dist - level_logic.history[length - 1][1]
            
            self.dv_dt[0] += (self.x_dist * scale)
            self.dv_dt[1] += (self.y_dist * scale)

            
            a = self.x_dist
            b = self.y_dist
            c = self.hypotenuse
            d = self.angle_to_player
            #e = (self.x_dist)#,self.y_dist)
            f = self.x_diff
            g = self.y_diff
            h = self.last_damage
            #self.last_damage = 0
            i = self.y_dist
            j = self.type_of_character
            if self.record_history:
                self.history.append((a,b,c,d,f,g,h,i,j))
            if self.type_of_character == 'spider':
                pygame.mixer.Sound.play(rpg.level_stuff.sound_logic.enemy_move_sound)

class History_for_AI():
    """This will hold the AI data for machine learning to improve AI difficulty. """

    def __init__(self,level_logic):
        """"""
        self.history = []
        #self.history.append((0,0,0,0,(0,0),0,0))
        #self.record_history = True
        #self.history_length_limit = 35000


    








