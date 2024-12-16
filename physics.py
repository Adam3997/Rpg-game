
import pygame





class Physics():
    """"""


    def __init__(self,rpg):
        """"""

        self.screen_rect = rpg.screen.get_rect()


    

    def update_speed(self,rpg):
        """"""
        rpg.movement_speed += rpg.accelleration 
        if rpg.movement_speed > rpg.speed_limit:
            rpg.movement_speed = rpg.speed_limit
    


    
    def update_enemy(self,rpg,left,right,up,down):
        """"""
        n = 0
        m = len(rpg.enemy_list)
        while n < m:
            if up:
                rpg.enemy_list[n].rect.y += rpg.movement_speed * rpg.dt
            if down:
                rpg.enemy_list[n].rect.y -= rpg.movement_speed * rpg.dt
            if left:
                rpg.enemy_list[n].rect.x += rpg.movement_speed * rpg.dt
            if right:
                rpg.enemy_list[n].rect.x -= rpg.movement_speed * rpg.dt
        
            n += 1
        collisions = pygame.sprite.spritecollide(rpg.player1,rpg.enemy_list,False)
        #print(len(collisions), ' on map')
        if collisions:
            collisions[0].delete_me()
            """then a fight will happen. """
            #print('here')
            rpg.campagne_fight = True
            
            
            #print('the player hit a monster!s')   # this is where i was working on the campagne fight interactions. 


    def update_trees(self,rpg,left,right,up,down):
        """"""
        n = 0
        m = len(rpg.world1.flowers)

        while n < m:
            if up:
                rpg.world1.rect_list[n].y += rpg.movement_speed * rpg.dt
                
                
            if down:
                rpg.world1.rect_list[n].y -= rpg.movement_speed * rpg.dt
                
                
            if left:
                rpg.world1.rect_list[n].x += rpg.movement_speed * rpg.dt
                
                
            if right:
                rpg.world1.rect_list[n].x -= rpg.movement_speed * rpg.dt
                
                
            
            n += 1
        
    def update_grass(self,rpg,left,right,up,down):
        """"""
        n = 0
        m = len(rpg.world1.grass)

        while n < m:
            if up:
                rpg.world1.rect_list2[n].y += rpg.movement_speed * rpg.dt
            if down:
                rpg.world1.rect_list2[n].y -= rpg.movement_speed * rpg.dt 
            if left:
                rpg.world1.rect_list2[n].x += rpg.movement_speed * rpg.dt   
            if right:
                rpg.world1.rect_list2[n].x -= rpg.movement_speed * rpg.dt
         
            n += 1
        n = 0
        m = len(rpg.world2.grass)

        while n < m:
            if up:
                rpg.world2.rect_list2[n].y += rpg.movement_speed * rpg.dt
            if down:
                rpg.world2.rect_list2[n].y -= rpg.movement_speed * rpg.dt 
            if left:
                rpg.world2.rect_list2[n].x += rpg.movement_speed * rpg.dt   
            if right:
                rpg.world2.rect_list2[n].x -= rpg.movement_speed * rpg.dt
         
            n += 1
        
        n = 0
        m = len(rpg.world3.grass)

        while n < m:
            if up:
                rpg.world3.rect_list2[n].y += rpg.movement_speed * rpg.dt
            if down:
                rpg.world3.rect_list2[n].y -= rpg.movement_speed * rpg.dt 
            if left:
                rpg.world3.rect_list2[n].x += rpg.movement_speed * rpg.dt   
            if right:
                rpg.world3.rect_list2[n].x -= rpg.movement_speed * rpg.dt
         
            n += 1
        
        n = 0
        m = len(rpg.world4.grass)

        while n < m:
            if up:
                rpg.world4.rect_list2[n].y += rpg.movement_speed * rpg.dt
            if down:
                rpg.world4.rect_list2[n].y -= rpg.movement_speed * rpg.dt 
            if left:
                rpg.world4.rect_list2[n].x += rpg.movement_speed * rpg.dt   
            if right:
                rpg.world4.rect_list2[n].x -= rpg.movement_speed * rpg.dt
         
            n += 1
    

    def movement(self,rpg):
        """"""
        self.momentum(rpg)
        keys = pygame.key.get_pressed()


        if keys[pygame.K_w]:
            #polygon = self.world1.rect
            #if not self.collideRectPolygon(self.try1.rect,(polygon)):
            if rpg.world1.rect.y < self.screen_rect.centery:
                rpg.world1.rect.y += rpg.movement_speed * rpg.dt
                rpg.try1.rect.y += rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left = False,right=False,up=True,down=False)
                self.update_trees(rpg,left = False,right=False,up=True,down=False)
                self.update_grass(rpg,left = False,right=False,up=True,down=False)
                rpg.particle_list_1[1].player_movement_particle(rpg,left = False,right=False,up=True,down=False)
                self.update_speed(rpg)
                if rpg.moving_up < rpg.speed_limit:
                    rpg.moving_up += rpg.accelleration
        if keys[pygame.K_s]:
            if rpg.world1.rect.bottom > self.screen_rect.centery : # this must be fixex. i am trying to make it so that the player cannot move off the map world1. this works for a and w. not for s and d. 
                rpg.world1.rect.y -= rpg.movement_speed * rpg.dt
                rpg.try1.rect.y -= rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left = False,right=False,up=False,down=True)
                self.update_trees(rpg,left = False,right=False,up=False,down=True)
                self.update_grass(rpg,left = False,right=False,up=False,down=True)
                rpg.particle_list_1[1].player_movement_particle(rpg,left = False,right=False,up=False,down=True)
                self.update_speed(rpg)
                if rpg.moving_down < rpg.speed_limit:
                    rpg.moving_down += rpg.accelleration
        if keys[pygame.K_a]:
            if rpg.world1.rect.x < self.screen_rect.centerx:
                rpg.world1.rect.x += rpg.movement_speed * rpg.dt
                rpg.try1.rect.x += rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left=True,right=False,up=False,down=False)
                self.update_trees(rpg,left=True,right=False,up=False,down=False)
                self.update_grass(rpg,left=True,right=False,up=False,down=False)
                rpg.particle_list_1[1].player_movement_particle(rpg,left = True,right=False,up=False,down=False)
                self.update_speed(rpg)
                if rpg.moving_left < rpg.speed_limit:
                    rpg.moving_left += rpg.accelleration
        if keys[pygame.K_d]:
            if rpg.world1.rect.right > rpg.screen_rect.centerx:
                rpg.world1.rect.x -= rpg.movement_speed * rpg.dt
                rpg.try1.rect.x -= rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left = False,right=True,up=False,down=False)
                self.update_trees(rpg,left = False,right=True,up=False,down=False)
                self.update_grass(rpg,left = False,right=True,up=False,down=False)
                rpg.particle_list_1[1].player_movement_particle(rpg,left = False,right=True,up=False,down=False)
                self.update_speed(rpg)
                if rpg.moving_right < rpg.speed_limit:
                    rpg.moving_right += rpg.accelleration
        if keys[pygame.K_w] == False and keys[pygame.K_s] == False and keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            """"""
            #self.movement_speed = self.default_speed
            rpg.movement_speed -= rpg.accelleration / 4
            if rpg.movement_speed < 0:
                rpg.movement_speed = 0 # movement being negative was causing a issue if you did not click to move for some time.
        
        rpg.dt = rpg.clock.tick(60) / 1000





    def momentum(self,rpg):
        """"""
        if rpg.moving_right < 0:
            rpg.moving_right = 0
        if rpg.moving_left < 0:
            rpg.moving_left = 0
        if rpg.moving_up < 0:
            rpg.moving_up = 0
        if rpg.moving_down < 0:
            rpg.moving_down = 0
        #print(self.particle_list_1[1].nested_polygon_list[1])
        total = rpg.moving_right + rpg.moving_left + rpg.moving_down + rpg.moving_up
        if total > 0:
            """"""
            if rpg.moving_right > 0:
                rpg.world1.rect.x -= rpg.movement_speed * rpg.dt
                rpg.try1.rect.x -= rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left = False,right=True,up=False,down=False)
                self.update_trees(rpg,left = False,right=True,up=False,down=False)
                self.update_grass(rpg,left = False,right=True,up=False,down=False)
                #self.particle_list_1[1].player_movement_particle(self,left = False,right=True,up=False,down=False)
                rpg.moving_right -=  rpg.deccelleration
                if rpg.moving_right < 0:
                    rpg.moving_right = 0
            
            if rpg.moving_left > 0:
                rpg.world1.rect.x += rpg.movement_speed * rpg.dt
                rpg.try1.rect.x += rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left = True,right=False,up=False,down=False)
                self.update_trees(rpg,left = True,right=False,up=False,down=False)
                self.update_grass(rpg,left = True,right=False,up=False,down=False)
                #self.particle_list_1[1].player_movement_particle(self,left = True,right=False,up=False,down=False)
                rpg.moving_left -= rpg.deccelleration
                if rpg.moving_left < 0:
                    rpg.moving_left = 0  
            if rpg.moving_up > 0:
                rpg.world1.rect.y += rpg.movement_speed * rpg.dt
                rpg.try1.rect.y += rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left = False,right=False,up=True,down=False)
                self.update_trees(rpg,left = False,right=False,up=True,down=False)
                self.update_grass(rpg,left = False,right=False,up=True,down=False)
                #self.particle_list_1[1].player_movement_particle(self,left =False,right=False,up=True,down=False)
                rpg.moving_up -= rpg.deccelleration
                if rpg.moving_up < 0:
                    rpg.moving_up = 0 
            if rpg.moving_down > 0:
                rpg.world1.rect.y -= rpg.movement_speed * rpg.dt
                rpg.try1.rect.y -= rpg.movement_speed * rpg.dt
                self.update_enemy(rpg,left = False,right=False,up=False,down=True)
                self.update_trees(rpg,left = False,right=False,up=False,down=True)
                self.update_grass(rpg,left = False,right=False,up=False,down=True)
                #self.particle_list_1[1].player_movement_particle(self,left = False,right=False,up=False,down=True)
                rpg.moving_down -= rpg.deccelleration
                if rpg.moving_down < 0:
                    rpg.moving_down = 0

    



