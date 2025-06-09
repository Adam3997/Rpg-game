
import pygame
import random




class Physics():
    """This handles the physics interactions. the physics stats holds the stats needed for these calculations.
    Accelleration changes velocity, then velocity changes location. Collisions are elastic collisions with no angle of impact."""


    def __init__(self,rpg):
        self.screen_rect = rpg.screen.get_rect()
        self.physics_delay = 5
        self.physics_delay_old = self.physics_delay
        self.tree_collision_delay = 10
        self.tree_collision_delay_old = self.tree_collision_delay
        self.boss_collision_delay = 10
        self.boss_collision_delay_old = self.boss_collision_delay

    """def update_speed(self,rpg):
        
        rpg.level_stuff.player_1.velocity += rpg.level_stuff.player_1.dv_dt 
        vector = (rpg.level_stuff.player_1.velocity[0]**2) + (rpg.level_stuff.player_1.velocity[1]**2)
        if vector > rpg.level_stuff.player_1.max_speed:
            rpg.level_stuff.player_1.velocity[0] = rpg.level_stuff.player_1.max_speed * 0.9 
            rpg.level_stuff.player_1.velocity[1] = rpg.level_stuff.player_1.max_speed * 0.9"""
    
    
    
    def detect_collisions_bounce_wolf(self,rpg):
        """This detects collisions between the boss and player."""
        n = 0
        m = len(rpg.level_stuff.level_1_boss.wolf_list) - 1
        while n <= m:
            collisions_test = pygame.Rect.colliderect(rpg.level_stuff.player_1.rect,rpg.level_stuff.level_1_boss.wolf_list[n])
            
            if collisions_test:
                if self.boss_collision_delay == self.boss_collision_delay_old:
                    rpg.level_stuff.player_1.impact_delay -=1
                    
                    v_1_f_x = (((rpg.level_stuff.player_1.mass - rpg.level_stuff.level_1_boss.wolf_list[n].mass ) / (rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass)) * rpg.level_stuff.player_1.velocity[0]) + (((2 * rpg.level_stuff.level_1_boss.wolf_list[n].mass)/(rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass))*rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0])
                    v_1_f_y = (((rpg.level_stuff.player_1.mass - rpg.level_stuff.level_1_boss.wolf_list[n].mass ) / (rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass)) * rpg.level_stuff.player_1.velocity[1]) + (((2 * rpg.level_stuff.level_1_boss.wolf_list[n].mass)/(rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass))*rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1])
                    v_2_f_x = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass)) * rpg.level_stuff.player_1.velocity[0]) + (((rpg.level_stuff.level_1_boss.wolf_list[n].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass))*rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0])
                    v_2_f_y = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass)) * rpg.level_stuff.player_1.velocity[1]) + (((rpg.level_stuff.level_1_boss.wolf_list[n].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.wolf_list[n].mass))*rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1])
                    # this is a recoil force for person 2
                    if -10 <= v_2_f_x <= 10:
                        if v_2_f_x > 0:
                            v_2_f_x += 250
                        else:
                            v_2_f_x -= 250
                    if -10 <= v_2_f_y <= 10:
                        if v_2_f_y > 0:
                            v_2_f_y += 250
                        else:
                            v_2_f_y -= 250
                    # below is the for player _1 
                    if -10 <= v_1_f_x <= 10:
                        if v_1_f_x > 0:
                            v_1_f_x += 250
                        else:
                            v_1_f_x -= 250
                    if -10 <= v_1_f_y <= 10:
                        if v_1_f_y > 0:
                            v_1_f_y += 250
                        else:
                            v_1_f_y -= 250
                    
                    rpg.level_stuff.player_1.velocity[0] = v_1_f_x
                        
                    rpg.level_stuff.player_1.velocity[1] = v_1_f_y

                    rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0] = v_2_f_x

                    rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1] = v_2_f_y

                    

                    self.boss_collision_delay -= 1
            if self.boss_collision_delay < self.boss_collision_delay_old:
                self.boss_collision_delay -= 1
            if self.boss_collision_delay <= 0:
                self.boss_collision_delay = self.boss_collision_delay_old
            n += 1


    def detect_collisions_bounce_boss(self,rpg):
        """This detects collisions between the boss and player."""
        collisions_test = pygame.Rect.colliderect(rpg.level_stuff.player_1.rect,rpg.level_stuff.level_1_boss.rect_2)
        
        if collisions_test:
            if self.boss_collision_delay == self.boss_collision_delay_old:
                rpg.level_stuff.player_1.impact_delay -=1
                
                v_1_f_x = (((rpg.level_stuff.player_1.mass - rpg.level_stuff.level_1_boss.mass ) / (rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.mass)) * rpg.level_stuff.player_1.velocity[0]) + (((2 * rpg.level_stuff.level_1_boss.mass)/(rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.mass))*rpg.level_stuff.level_1_boss.velocity[0])
                v_1_f_y = (((rpg.level_stuff.player_1.mass - rpg.level_stuff.level_1_boss.mass ) / (rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.mass)) * rpg.level_stuff.player_1.velocity[1]) + (((2 * rpg.level_stuff.level_1_boss.mass)/(rpg.level_stuff.player_1.mass + rpg.level_stuff.level_1_boss.mass))*rpg.level_stuff.level_1_boss.velocity[1])
                #v_2_f_x = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[0]) + (((collisions_test[0].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
                #v_2_f_y = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[1]) + (((collisions_test[0].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])

               
            
                if -10 <= v_1_f_x <= 10:
                    if v_1_f_x > 0:
                        v_1_f_x += 250
                    else:
                        v_1_f_x -= 250
                if -10 <= v_1_f_y <= 10:
                    if v_1_f_y > 0:
                        v_1_f_y += 250
                    else:
                        v_1_f_y -= 250
                
                rpg.level_stuff.player_1.velocity[0] = v_1_f_x
                    
                rpg.level_stuff.player_1.velocity[1] = v_1_f_y

                self.boss_collision_delay -= 1
        if self.boss_collision_delay < self.boss_collision_delay_old:
            self.boss_collision_delay -= 1
        if self.boss_collision_delay <= 0:
            self.boss_collision_delay = self.boss_collision_delay_old
              
                

     
    def detect_collisions_bounce_trees(self,rpg):
        """This detects collissions between trees and the player."""
        collisions_test = pygame.sprite.spritecollide(rpg.level_stuff.player_1,rpg.level_stuff.tree_set.tree_list,False)
        
        if collisions_test:
            if self.tree_collision_delay == self.tree_collision_delay_old:
                rpg.level_stuff.player_1.impact_delay -=1
                
                v_1_f_x = (((rpg.level_stuff.player_1.mass - collisions_test[0].mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[0]) + (((2 * collisions_test[0].mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
                v_1_f_y = (((rpg.level_stuff.player_1.mass - collisions_test[0].mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[1]) + (((2 * collisions_test[0].mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])
                #v_2_f_x = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[0]) + (((collisions_test[0].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
                #v_2_f_y = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[1]) + (((collisions_test[0].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])

               
            
                if -10 <= v_1_f_x <= 10:
                    if v_1_f_x > 0:
                        v_1_f_x += 250
                    else:
                        v_1_f_x -= 250
                if -10 <= v_1_f_y <= 10:
                    if v_1_f_y > 0:
                        v_1_f_y += 250
                    else:
                        v_1_f_y -= 250
                
                rpg.level_stuff.player_1.velocity[0] = v_1_f_x
                    
                rpg.level_stuff.player_1.velocity[1] = v_1_f_y

                self.tree_collision_delay -= 1
        if self.tree_collision_delay < self.tree_collision_delay_old:
            self.tree_collision_delay -= 1
        if self.tree_collision_delay <= 0:
            self.tree_collision_delay = self.tree_collision_delay_old
                
              



    def detect_collisions_bounce(self,rpg):
        """This detecs for collisions between the player and the enemies on the map"""
        collisions_test = pygame.sprite.spritecollide(rpg.level_stuff.player_1,rpg.level_stuff.enemy_list,False)
        if collisions_test:
            rpg.level_stuff.player_1.impact_delay -=1
            
            rpg.level_stuff.player_1.health -= 1
            rpg.overlay.create_damage_for_overlay(1,rpg.level_stuff.player_1.rect.center,'red')
            v_1_f_x = (((rpg.level_stuff.player_1.mass - collisions_test[0].mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[0]) + (((2 * collisions_test[0].mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
            v_1_f_y = (((rpg.level_stuff.player_1.mass - collisions_test[0].mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[1]) + (((2 * collisions_test[0].mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])
            v_2_f_x = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[0]) + (((collisions_test[0].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
            v_2_f_y = (((2 * rpg.level_stuff.player_1.mass ) / (rpg.level_stuff.player_1.mass + collisions_test[0].mass)) * rpg.level_stuff.player_1.velocity[1]) + (((collisions_test[0].mass - rpg.level_stuff.player_1.mass)/(rpg.level_stuff.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])

            
           
                
            rpg.level_stuff.player_1.velocity[0] = v_1_f_x
                
            rpg.level_stuff.player_1.velocity[1] = v_1_f_y

            n = 0
            m = len(rpg.level_stuff.enemy_list) - 1
            while n <= m:
                if rpg.level_stuff.enemy_list[n].id_number == collisions_test[0].id_number:
                    """"""
                        #print(rpg.enemy_list[n].velocity[0],'before')
                    margin = 5
                    if -margin <= v_2_f_x  <= margin:
                        if v_2_f_x > 0:
                            v_2_f_x += 150
                        if v_2_f_x <= 0:
                            v_2_f_x -= 150
                    if -margin <= v_2_f_y  <= margin:
                        if v_2_f_y > 0:
                            v_2_f_y += 150
                        if v_2_f_y <= 0:
                            v_2_f_y -= 150
                    rpg.level_stuff.enemy_list[n].velocity[0] =  v_2_f_x
                    rpg.level_stuff.enemy_list[n].velocity[1] =  v_2_f_y
                    rpg.level_stuff.enemy_list[n].health -= 5
                    
                    rpg.overlay.create_damage_for_overlay(1,rpg.level_stuff.enemy_list[n].rect.center,'cyan')

                        #print(rpg.enemy_list[n].velocity[0],'after')
                n += 1
               

    def update_town(self,rpg):
        """This updates the town on the map"""

        if rpg.level_stuff.town_exists:
            """"""
            n = 0
            m = len(rpg.level_stuff.town_1.house_list) - 1

            while n <= m:
                rpg.level_stuff.town_1.house_list[n].rect.centerx -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
                rpg.level_stuff.town_1.house_list[n].rect.centery -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
                n += 1
        
    def update_player_map(self,rpg):
        """This updates the player movements on the map"""

        rpg.level_stuff.player_1.map_x_location += (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
        rpg.level_stuff.player_1.map_y_location += (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
        

    def update_enemy_test2(self,rpg):
        """This moves the enemy when the player moves. This simulates player movement."""
        #self.enemy_loop(rpg)
        n = 0
        m = len(rpg.level_stuff.enemy_list)
        #print(n,m)
       
        while n < m:
            
            rpg.level_stuff.enemy_list[n].rect.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)  
            rpg.level_stuff.enemy_list[n].rect.x -= (rpg.level_stuff.player_1.velocity[0]* rpg.dt)
            rpg.level_stuff.enemy_list[n].rect_picture.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)  
            rpg.level_stuff.enemy_list[n].rect_picture.x -= (rpg.level_stuff.player_1.velocity[0]* rpg.dt)
            
            rpg.level_stuff.enemy_list[n].rect_attack_right.y -= rpg.level_stuff.player_1.velocity[1]* rpg.dt
            rpg.level_stuff.enemy_list[n].rect_attack_right.x -= rpg.level_stuff.player_1.velocity[0]* rpg.dt

            rpg.level_stuff.enemy_list[n].rect_attack_left.y -= rpg.level_stuff.player_1.velocity[1]* rpg.dt
            rpg.level_stuff.enemy_list[n].rect_attack_left.x -= rpg.level_stuff.player_1.velocity[0]* rpg.dt

            rpg.level_stuff.enemy_list[n].rect_attack_down.y -= rpg.level_stuff.player_1.velocity[1]* rpg.dt
            rpg.level_stuff.enemy_list[n].rect_attack_down.x -= rpg.level_stuff.player_1.velocity[0]* rpg.dt

            rpg.level_stuff.enemy_list[n].rect_attack_up.y -= rpg.level_stuff.player_1.velocity[1]* rpg.dt
            rpg.level_stuff.enemy_list[n].rect_attack_up.x -= rpg.level_stuff.player_1.velocity[0]* rpg.dt

            
        
            n += 1     
                

    def update_trees_2(self,rpg):
        """this updates the trees location when the player moves."""
        n = 0
        m = len(rpg.level_stuff.tree_set.tree_list) - 1
        while n <= m:
            rpg.level_stuff.tree_set.tree_list[n].rect_image.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            rpg.level_stuff.tree_set.tree_list[n].rect_image.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.tree_set.tree_list[n].rect.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            rpg.level_stuff.tree_set.tree_list[n].rect.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)

            n += 1
    
 
    def update_items(self,rpg):
        """Updates the list of items on screen"""
        u = 0
        v = len(rpg.level_stuff.item_list) - 1
        while u <= v:
            rpg.level_stuff.item_list[u].rect.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.item_list[u].rect.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            
            u += 1
        u = 0
        v = len(rpg.level_stuff.generic_items.item_list_generic) - 1
        while u <= v:
            rpg.level_stuff.generic_items.item_list_generic[u].rect.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.generic_items.item_list_generic[u].rect.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            u += 1


    def update_boss(self,rpg):
        """this moves the boss and its components when player moves"""

        rpg.level_stuff.level_1_boss.rect.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_2.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_2.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_right.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_right.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_left.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_left.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_up.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_up.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_down.x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
        rpg.level_stuff.level_1_boss.rect_attack_down.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
        i = 0
        j = len(rpg.level_stuff.level_1_boss.fireball_list_x)
        while i < j:
            rpg.level_stuff.level_1_boss.fireball_list_x[i].fire_ball_rect.x -=  (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.level_1_boss.fireball_list_x[i].fire_ball_rect.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            i += 1
        i = 0
        j = len(rpg.level_stuff.level_1_boss.fireball_list)
        while i < j:
            rpg.level_stuff.level_1_boss.fireball_list[i].fire_ball_rect.x -=  (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.level_1_boss.fireball_list[i].fire_ball_rect.y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            i += 1
        i = 0
        j = len(rpg.level_stuff.level_1_boss.fire_circle_level_1.rect_circle_spell_list) - 1
        while i <= j:
            rpg.level_stuff.level_1_boss.fire_circle_level_1.rect_circle_spell_list[i].centerx -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.level_1_boss.fire_circle_level_1.rect_circle_spell_list[i].centery -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            i += 1
        i = 0
        j = len(rpg.level_stuff.level_1_boss.fireball_list_war_invoke) - 1
        while i <= j:
            rpg.level_stuff.level_1_boss.fireball_list_war_invoke[i].fire_ball_rect.centerx -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.level_1_boss.fireball_list_war_invoke[i].fire_ball_rect.centery -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            i += 1
        i = 0
        j = len(rpg.level_stuff.level_1_boss.fireball_list_war_invoke_2) - 1
        while i <= j:
            rpg.level_stuff.level_1_boss.fireball_list_war_invoke_2[i].fire_ball_rect.centerx -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            rpg.level_stuff.level_1_boss.fireball_list_war_invoke_2[i].fire_ball_rect.centery -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            i += 1



    def enemy_loop(self,rpg):
        """This is the loop for enemy movement. If they have velocity, this velocity will change their location. This will also apply a random acelleration after some random interval. """
        n = 0
        m = len(rpg.level_stuff.enemy_list)
        while n < m :
            x_distance = rpg.level_stuff.player_1.rect.centerx - rpg.level_stuff.enemy_list[n].rect.centerx
            y_distance = rpg.level_stuff.player_1.rect.centery - rpg.level_stuff.enemy_list[n].rect.centery
            hypotenuse_enemy_player_1 = ((x_distance**2) +(y_distance**2))**0.5
            if hypotenuse_enemy_player_1 <= 2000:
                rpg.level_stuff.enemy_list[n].update_speed_stats(rpg)

                if rpg.level_stuff.enemy_list[n].velocity[0] > 0:
                    """move here"""
                    self.enemy_movement_action(rpg,up=False,down=False,right=True,left=False,number=n)
                if rpg.level_stuff.enemy_list[n].velocity[0]< 0:
                    """move here"""
                    self.enemy_movement_action(rpg,up=False,down=False,right=False,left=True,number=n)
                if rpg.level_stuff.enemy_list[n].velocity[1] > 0:
                    """move here"""
                    self.enemy_movement_action(rpg,up=False,down=True,right=False,left=False,number=n)
                if rpg.level_stuff.enemy_list[n].velocity[1] < 0:
                    """move here"""
                    self.enemy_movement_action(rpg,up=True,down=False,right=False,left=False,number=n)
                rpg.level_stuff.enemy_list[n].accelleration_timer -= 1
                rpg.level_stuff.enemy_list[n].update_info(rpg)
                if rpg.level_stuff.enemy_list[n].accelleration_timer <= 0:
                    #self.accellerate_enemy(rpg)
                    #rpg.level_stuff.enemy_list[n].update_info(rpg)
                    rpg.level_stuff.enemy_list[n].decide_L_or_l_movement(rpg) # this used to be make decision
                    
                    rpg.level_stuff.enemy_list[n].accelleration_timer = rpg.level_stuff.enemy_list[n].acc_timer_old

            n += 1
        #self.enemy_movement_action(rpg)
        #self.enemy_movement_slowdown(rpg)

    

    def accellerate_enemy(self,rpg):
        """This changes the velocity of the enemies on the map"""
        n = 0
        m = len(rpg.level_stuff.enemy_list)
        while n < m:
            """"""
            o = random.choice(['up','down','left','right'])
            #rpg.enemy_list[n].change_accelleration()
            rpg.level_stuff.enemy_list[n].set_animation_direction(rpg)
            match o:
                case 'up':
                    """"""
                    rpg.level_stuff.enemy_list[n].accellerate_up(rpg)
                case 'down':
                    """"""
                    rpg.level_stuff.enemy_list[n].accellerate_down(rpg)
                case 'right':
                    """"""
                    rpg.level_stuff.enemy_list[n].accellerate_right(rpg)
                case 'left':
                    """"""
                    rpg.level_stuff.enemy_list[n].accellerate_left(rpg)
            n +=1
            #rpg.enemy_list[n].V_x += rpg.enemy_list[n].dxdt

    def update_enemy_map(self,rpg):
        """this moves the enemy along the map."""



    def enemy_movement_action(Self,rpg,up,left,right,down,number):
        """This updates the location based upon the velocity"""
        #rpg.enemy_list[number].set_animation_direction()
        if up:
            """"""
            rpg.level_stuff.enemy_list[number].rect_picture.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_right.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_down.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_left.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_up.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_x_location += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_y_location += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
        if down:
            """"""
            rpg.level_stuff.enemy_list[number].rect_picture.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_right.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_down.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_left.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_up.y += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_x_location += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_y_location += rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
        if left:
            """"""
            rpg.level_stuff.enemy_list[number].rect_picture.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_right.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_down.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_left.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_up.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_x_location -= rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_y_location -= rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
        if right:
            """"""
            rpg.level_stuff.enemy_list[number].rect_picture.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_right.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_down.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_left.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].rect_attack_up.x += rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_x_location -= rpg.level_stuff.enemy_list[number].velocity[0] *rpg.dt
            rpg.level_stuff.enemy_list[number].map_y_location -= rpg.level_stuff.enemy_list[number].velocity[1] *rpg.dt
        
    
    

    def update_grass(self,rpg):
        """moves the grass when player moves""" # needs to be refactored
        # the map can also move in here

        rpg.level_stuff.grass_decorations.update_location(rpg)
        n = 0
        m = len(rpg.world1.grass)
        while n < m:
            rpg.world1.rect_list2[n].y -= (rpg.level_stuff.player_1.velocity[1] * rpg.dt)
            rpg.world1.rect_list2[n].x -= (rpg.level_stuff.player_1.velocity[0] * rpg.dt)
            n += 1
       
    def momentum_3(self,rpg):
        """This holds the final momentum logic"""
        rpg.level_stuff.player_1.update_speed_stats(rpg)
        self.update_enemy_test2(rpg)
        self.update_trees_2(rpg)
        self.update_grass(rpg) 
        self.update_items(rpg)
        rpg.level_stuff.cloud_stuff.move_clouds_for_player(rpg)
        rpg.overlay.update_damage(rpg) 
        if rpg.level_stuff.boss_type == 'wolf':
            self.update_wolf_boss(rpg)
    
    def update_wolf_boss(self,rpg):
        """This handles physics for the wolf boss.
        This will be the movement of the wolves."""

        n = 0
        m = len(rpg.level_stuff.level_1_boss.wolf_list) - 1
        while n <= m:
            
            rpg.level_stuff.level_1_boss.wolf_list[n].update_info(rpg)

            rpg.level_stuff.level_1_boss.wolf_list[n].rect.x -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect.x += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect.y += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1] * rpg.dt


            rpg.level_stuff.level_1_boss.wolf_list[n].rect_picture.x += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_picture.y += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_picture.x -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_picture.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_left.x -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_left.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_left.x += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_left.y += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1] * rpg.dt

            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_right.x -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_right.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_right.x += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_right.y += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1] * rpg.dt

            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_up.x -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_up.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_up.x += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_up.y += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1] * rpg.dt

            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_down.x -= rpg.level_stuff.player_1.velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_down.y -= rpg.level_stuff.player_1.velocity[1] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_down.x += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[0] * rpg.dt
            rpg.level_stuff.level_1_boss.wolf_list[n].rect_attack_down.y += rpg.level_stuff.level_1_boss.wolf_list[n].velocity[1] * rpg.dt


            rpg.level_stuff.level_1_boss.wolf_list[n].accelleration_timer -= 1
            if rpg.level_stuff.level_1_boss.wolf_list[n].accelleration_timer <= 0:
                #self.accellerate_enemy(rpg)
                #rpg.level_stuff.level_1_boss.wolf_list[n].update_info(rpg)
                rpg.level_stuff.level_1_boss.wolf_list[n].decide_L_or_l_movement(rpg) # this used to be make decision
                    
                rpg.level_stuff.level_1_boss.wolf_list[n].accelleration_timer = rpg.level_stuff.level_1_boss.wolf_list[n].acc_timer_old
            n += 1

    
    def movement_2(self,rpg):
        """The full movement loop. Moves everything when you press w, a, s, d, to simulate the player moving with the 'camera' centered
         on the player."""
        #self.momentum_3(rpg)
        if rpg.level_stuff.player_1.impact_delay >= rpg.level_stuff.player_1.impact_delay_old:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                rpg.level_stuff.player_1.accellerate_up(rpg)
                rpg.level_stuff.player_1.acc_timer += 1 
            if keys[pygame.K_s]:
                rpg.level_stuff.player_1.accellerate_down(rpg)
                rpg.level_stuff.player_1.acc_timer += 1 
            if keys[pygame.K_a]:
                rpg.level_stuff.player_1.accellerate_left(rpg)
                rpg.level_stuff.player_1.acc_timer += 1 
            if keys[pygame.K_d]:
                rpg.level_stuff.player_1.accellerate_right(rpg)
                rpg.level_stuff.player_1.acc_timer += 1 
            if keys[pygame.K_a]==False and keys[pygame.K_d] == False and keys[pygame.K_s]==False and keys[pygame.K_w]==False:
                rpg.level_stuff.player_1.acc_timer = 1
        if rpg.level_stuff.player_1.impact_delay < rpg.level_stuff.player_1.impact_delay_old:
            rpg.level_stuff.player_1.impact_delay -= 1
            if rpg.level_stuff.player_1.impact_delay <= 0:
                rpg.level_stuff.player_1.impact_delay = rpg.level_stuff.player_1.impact_delay_old
        
        rpg.dt = rpg.clock.tick(rpg.target_framerate) / 1000

    



    




