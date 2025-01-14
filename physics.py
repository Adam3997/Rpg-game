
import pygame
import random




class Physics():
    """"""


    def __init__(self,rpg):
        """"""

        self.screen_rect = rpg.screen.get_rect()

        self.physics_delay = 5
        self.physics_delay_old = self.physics_delay

        self.tree_collision_delay = 10
        self.tree_collision_delay_old = self.tree_collision_delay


    

    def update_speed(self,rpg):
        """"""
        rpg.player_1.velocity += rpg.player_1.dv_dt 
        vector = (rpg.player_1.velocity[0]**2) + (rpg.player_1.velocity[1]**2)
        if vector > rpg.player_1.max_speed:
            rpg.player_1.velocity[0] = rpg.player_1.max_speed * 0.9 
            rpg.player_1.velocity[1] = rpg.player_1.max_speed * 0.9
    


    
   
              
                

     
    def detect_collisions_bounce_trees(self,rpg):
        
        collisions_test = pygame.sprite.spritecollide(rpg.player_1,rpg.tree_set.tree_list,False)
        
        if collisions_test:
            if self.tree_collision_delay == self.tree_collision_delay_old:
                rpg.player_1.impact_delay -=1
                
                v_1_f_x = (((rpg.player_1.mass - collisions_test[0].mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[0]) + (((2 * collisions_test[0].mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
                v_1_f_y = (((rpg.player_1.mass - collisions_test[0].mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[1]) + (((2 * collisions_test[0].mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])
                v_2_f_x = (((2 * rpg.player_1.mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[0]) + (((collisions_test[0].mass - rpg.player_1.mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
                v_2_f_y = (((2 * rpg.player_1.mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[1]) + (((collisions_test[0].mass - rpg.player_1.mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])

               
            
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
                
                rpg.player_1.velocity[0] = v_1_f_x
                    
                rpg.player_1.velocity[1] = v_1_f_y

                self.tree_collision_delay -= 1
        if self.tree_collision_delay < self.tree_collision_delay_old:
            self.tree_collision_delay -= 1
        if self.tree_collision_delay <= 0:
            self.tree_collision_delay = self.tree_collision_delay_old
                
              



    def detect_collisions_bounce(self,rpg):

        collisions_test = pygame.sprite.spritecollide(rpg.player_1,rpg.enemy_list,False)
        if collisions_test:
            rpg.player_1.impact_delay -=1
            
            v_1_f_x = (((rpg.player_1.mass - collisions_test[0].mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[0]) + (((2 * collisions_test[0].mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
            v_1_f_y = (((rpg.player_1.mass - collisions_test[0].mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[1]) + (((2 * collisions_test[0].mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])
            v_2_f_x = (((2 * rpg.player_1.mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[0]) + (((collisions_test[0].mass - rpg.player_1.mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[0])
            v_2_f_y = (((2 * rpg.player_1.mass ) / (rpg.player_1.mass + collisions_test[0].mass)) * rpg.player_1.velocity[1]) + (((collisions_test[0].mass - rpg.player_1.mass)/(rpg.player_1.mass + collisions_test[0].mass))*collisions_test[0].velocity[1])

            
           
                
            rpg.player_1.velocity[0] = v_1_f_x
                
            rpg.player_1.velocity[1] = v_1_f_y

            n = 0
            m = len(rpg.enemy_list) - 1
            while n <= m:
                if rpg.enemy_list[n].id_number == collisions_test[0].id_number:
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
                    rpg.enemy_list[n].velocity[0] =  v_2_f_x
                    rpg.enemy_list[n].velocity[1] =  v_2_f_y

                        #print(rpg.enemy_list[n].velocity[0],'after')
                n += 1
               


        

        

    def update_enemy_test2(self,rpg):
        """This moves the enemy when the player moves. This simulates player movement."""
        #self.enemy_loop(rpg)
        n = 0
        m = len(rpg.enemy_list)
        #print(n,m)
       
        while n < m:
            
            rpg.enemy_list[n].rect.y -= (rpg.player_1.velocity[1] * rpg.dt)  
            
            rpg.enemy_list[n].rect.x -= (rpg.player_1.velocity[0]* rpg.dt)
            
        
            n += 1     
                

        #collisions2 = pygame.Rect.colliderect(rpg.particle_list_1[1].particle_1.rect,rpg.enemy_list[1])
        #if collisions2:
           # """"""


    def update_trees_2(self,rpg):
        """"""
        n = 0
        m = len(rpg.tree_set.tree_list) - 1
        while n <= m:
            rpg.tree_set.tree_list[n].rect_image.y -= (rpg.player_1.velocity[1] * rpg.dt)
            rpg.tree_set.tree_list[n].rect_image.x -= (rpg.player_1.velocity[0] * rpg.dt)
            rpg.tree_set.tree_list[n].rect.y -= (rpg.player_1.velocity[1] * rpg.dt)
            rpg.tree_set.tree_list[n].rect.x -= (rpg.player_1.velocity[0] * rpg.dt)

            n += 1
    
    
    def update_boss(self,rpg):
        """"""

        rpg.level_1_boss.rect.x -= (rpg.player_1.velocity[0] * rpg.dt)
        rpg.level_1_boss.rect.y -= (rpg.player_1.velocity[1] * rpg.dt)
        rpg.level_1_boss.rect_2.x -= (rpg.player_1.velocity[0] * rpg.dt)
        rpg.level_1_boss.rect_2.y -= (rpg.player_1.velocity[1] * rpg.dt)
        rpg.level_1_boss.rect_attack_right.x -= (rpg.player_1.velocity[0] * rpg.dt)
        rpg.level_1_boss.rect_attack_right.y -= (rpg.player_1.velocity[1] * rpg.dt)
        rpg.level_1_boss.rect_attack_left.x -= (rpg.player_1.velocity[0] * rpg.dt)
        rpg.level_1_boss.rect_attack_left.y -= (rpg.player_1.velocity[1] * rpg.dt)
        rpg.level_1_boss.rect_attack_up.x -= (rpg.player_1.velocity[0] * rpg.dt)
        rpg.level_1_boss.rect_attack_up.y -= (rpg.player_1.velocity[1] * rpg.dt)
        rpg.level_1_boss.rect_attack_down.x -= (rpg.player_1.velocity[0] * rpg.dt)
        rpg.level_1_boss.rect_attack_down.y -= (rpg.player_1.velocity[1] * rpg.dt)


    def enemy_loop(self,rpg):
        """This is the loop for enemy movement. If they have velocity, this velocity will change their location. This will also apply a random acelleration after some random interval. """
        n = 0
        m = len(rpg.enemy_list)
        while n < m :
            rpg.enemy_list[n].update_speed(rpg)
            if rpg.enemy_list[n].velocity[0] > 0:
                """move here"""
                self.enemy_movement_action(rpg,up=False,down=False,right=True,left=False,number=n)
            if rpg.enemy_list[n].velocity[0]< 0:
                """move here"""
                self.enemy_movement_action(rpg,up=False,down=False,right=False,left=True,number=n)
            if rpg.enemy_list[n].velocity[1] > 0:
                """move here"""
                self.enemy_movement_action(rpg,up=False,down=True,right=False,left=False,number=n)
            if rpg.enemy_list[n].velocity[1] < 0:
                """move here"""
                self.enemy_movement_action(rpg,up=True,down=False,right=False,left=False,number=n)
            rpg.enemy_list[n].accelleration_timer -= 1
            if rpg.enemy_list[n].accelleration_timer <= 0:
                self.accellerate_enemy(rpg)
                rpg.enemy_list[n].accelleration_timer = 100

            n += 1
        #self.enemy_movement_action(rpg)
        self.enemy_movement_slowdown(rpg)

    

    def accellerate_enemy(self,rpg):
        """This changes the velocity of the enemies on the map"""
        n = 0
        m = len(rpg.enemy_list)
        while n < m:
            """"""
            o = random.choice(['up','down','left','right'])
            #rpg.enemy_list[n].change_accelleration()
            rpg.enemy_list[n].set_animation_direction()
            match o:
                case 'up':
                    """"""
                    rpg.enemy_list[n].accellerate_up(rpg)
                case 'down':
                    """"""
                    rpg.enemy_list[n].accellerate_down(rpg)
                case 'right':
                    """"""
                    rpg.enemy_list[n].accellerate_right(rpg)
                case 'left':
                    """"""
                    rpg.enemy_list[n].accellerate_left(rpg)
            n +=1
            #rpg.enemy_list[n].V_x += rpg.enemy_list[n].dxdt

    def enemy_movement_action(Self,rpg,up,left,right,down,number):
        """This updates the location based upon the velocity"""
        #rpg.enemy_list[number].set_animation_direction()
        if up:
            """"""
            rpg.enemy_list[number].rect.y += rpg.enemy_list[number].velocity[1] *rpg.dt
        if down:
            """"""
            rpg.enemy_list[number].rect.y += rpg.enemy_list[number].velocity[1] *rpg.dt
        if left:
            """"""
            rpg.enemy_list[number].rect.x += rpg.enemy_list[number].velocity[0] *rpg.dt
        if right:
            """"""
            rpg.enemy_list[number].rect.x += rpg.enemy_list[number].velocity[0] *rpg.dt
        
    def enemy_movement_slowdown(self,rpg):
        """This is a combination of drag and friction. This is combined for one slowdown variable. Will also stop them if they slow down enough. The velocity is framerate
         releative. """
        n = 0
        m = len(rpg.enemy_list)
        slowdown = 0.9 
        while n < m:
            rpg.enemy_list[n].V_x *= (slowdown)
            rpg.enemy_list[n].V_y *= (slowdown)
            if -1 <= rpg.enemy_list[n].V_x <= 1:
                rpg.enemy_list[n].V_x = 0
                rpg.enemy_list[n].V_y= 0

            n += 1

    



    def update_grass(self,rpg):
        """moves the grass when player moves""" # needs to be refactored
        # the map can also move in here
        rpg.world1.rect.x -= (rpg.player_1.velocity[0] * rpg.dt)
        rpg.world1.rect.y -= (rpg.player_1.velocity[1] * rpg.dt)
        
        n = 0
        m = len(rpg.world1.grass)

        while n < m:
            rpg.world1.rect_list2[n].y -= (rpg.player_1.velocity[1] * rpg.dt)
            rpg.world1.rect_list2[n].x -= (rpg.player_1.velocity[0] * rpg.dt)
                
         
            n += 1
       
    
    
    def momentum_3(self,rpg):
        """"""
        """if -1 < rpg.player_1_test.velocity[0] < 1:
                rpg.player_1_test.velocity[0] = 0
        if -1 < rpg.player_1_test.velocity[1] < 1:
                rpg.player_1_test.velocity[1] = 0"""
        #print('here')
        #rpg.player_1_test.update_speed(rpg)
        rpg.player_1.update_speed(rpg)
        self.update_enemy_test2(rpg)
        self.update_trees_2(rpg)
        self.update_grass(rpg)  
    
    
    def movement_2(self,rpg):
        """The full movement loop. Moves everything when you press w, a, s, d, to simulate the player moving with the 'camera' centered
         on the player. """
        #self.enemy_loop(rpg)
        
        self.momentum_3(rpg)
        if rpg.player_1.impact_delay >= rpg.player_1.impact_delay_old:
            
            keys = pygame.key.get_pressed()


            if keys[pygame.K_w]:
                #print('pressing up')
                rpg.player_1.accellerate_up(rpg)
                rpg.player_1.acc_timer += 1 
                
                #self.update_enemy_test(rpg,left = False,right=False,up=True,down=False)
                    
                #self.update_speed(rpg)
            if keys[pygame.K_s]:
                rpg.player_1.accellerate_down(rpg)
                rpg.player_1.acc_timer += 1 
                
                #self.update_enemy_test(rpg,left = False,right=False,up=False,down=True)
                    
                #self.update_speed(rpg
            if keys[pygame.K_a]:
                rpg.player_1.accellerate_left(rpg)
                rpg.player_1.acc_timer += 1 
                
                #self.update_enemy_test(rpg,left=True,right=False,up=False,down=False)
                
                #self.update_speed(rpg)
            if keys[pygame.K_d]:
                
                rpg.player_1.accellerate_right(rpg)
                rpg.player_1.acc_timer += 1 
                
                #print(rpg.player_1_test.velocity[0],rpg.player_1_test.velocity[1])
                #self.update_enemy_test(rpg,left = False,right=True,up=False,down=False)

                #self.update_speed(rpg)
            if keys[pygame.K_a]==False and keys[pygame.K_d] == False and keys[pygame.K_s]==False and keys[pygame.K_w]==False:
                rpg.player_1.acc_timer = 1
        if rpg.player_1.impact_delay < rpg.player_1.impact_delay_old:
            rpg.player_1.impact_delay -= 1
            if rpg.player_1.impact_delay <= 0:
                rpg.player_1.impact_delay = rpg.player_1.impact_delay_old
        
        rpg.dt = rpg.clock.tick(rpg.target_framerate) / 1000

    



    




