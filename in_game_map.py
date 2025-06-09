import pygame


class In_game_map():
    """This is a class for a in game map"""


    def __init__(self,rpg,width,height,background):
        """
        """
        
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.width =width
        self.height = height
        self.background = background

        self.map_surface = pygame.Surface((width,height))
        self.map_surface.fill(background)
        self.map_surface.set_colorkey((50,50,50))
        self.map_surface.set_alpha(200)

        self.map_surface_rect = self.map_surface.get_rect()
        self.map_surface_rect.bottomright = self.screen_rect.bottomright
        self.map_surface_rect.centerx -= 20
        self.map_surface_rect.centery -= 20

        self.scale_map = 200
        rpg.level_stuff.player_1.reset_player_map()

        

    def update_map(self,rpg):
        """This updates the map as needed"""
        rpg.level_stuff.physics_active.update_player_map(rpg)
        image_size = 4
        image_temp = pygame.Surface((image_size,image_size))
        locations_2 = 2
        pygame.draw.circle(image_temp,'red',(locations_2,locations_2),2,0)
        image_temp_boss = pygame.Surface((5,5))
        image_temp_boss.fill((50,50,50))
        pygame.draw.circle(image_temp_boss,'yellow',(locations_2,locations_2),2,0)
        image_temp_cross = pygame.Surface((5,5))
        image_temp_cross.fill((50,50,50))
        pygame.draw.circle(image_temp_cross,'yellow',(locations_2,locations_2),2,0)
        image_temp_pond = pygame.Surface((5,5))
        image_temp_pond.fill((50,50,50))
        pygame.draw.circle(image_temp_pond,'yellow',(locations_2,locations_2),2,0)
        image_temp_pillar = pygame.Surface((5,5))
        image_temp_pillar.fill((50,50,50))
        pygame.draw.circle(image_temp_pillar,'yellow',(locations_2,locations_2),2,0)
        image_temp_bowl = pygame.Surface((5,5))
        image_temp_bowl.fill((50,50,50))
        pygame.draw.circle(image_temp_bowl,'yellow',(locations_2,locations_2),2,0)
        image_temp_stone = pygame.Surface((5,5))
        image_temp_stone.fill((50,50,50))
        pygame.draw.circle(image_temp_stone,'yellow',(locations_2,locations_2),2,0)
        image_temp_plant = pygame.Surface((5,5))
        image_temp_plant.fill((50,50,50))
        pygame.draw.circle(image_temp_plant,'yellow',(locations_2,locations_2),2,0)
        self.map_surface.fill(self.background)
        self.map_surface.blit(image_temp,((self.width/2 )+(rpg.level_stuff.player_1.map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.player_1.map_y_location//self.scale_map)))
        self.map_surface.blit(image_temp_boss,((self.width/2 )+(rpg.level_stuff.level_1_boss.map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.level_1_boss.map_y_location//self.scale_map)))
        self.map_surface.blit(image_temp_cross,((self.width/2 )+(rpg.level_stuff.item_list[0].map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.item_list[0].map_y_location//self.scale_map)))
        self.map_surface.blit(image_temp_pond,((self.width/2 )+(rpg.level_stuff.item_list[1].map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.item_list[1].map_y_location//self.scale_map)))
        self.map_surface.blit(image_temp_pillar,((self.width/2 )+(rpg.level_stuff.item_list[2].map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.item_list[2].map_y_location//self.scale_map)))
        self.map_surface.blit(image_temp_bowl,((self.width/2 )+(rpg.level_stuff.item_list[3].map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.item_list[3].map_y_location//self.scale_map)))
        self.map_surface.blit(image_temp_stone,((self.width/2 )+(rpg.level_stuff.item_list[4].map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.item_list[4].map_y_location//self.scale_map)))
        self.map_surface.blit(image_temp_plant,((self.width/2 )+(rpg.level_stuff.item_list[5].map_x_location//self.scale_map),(self.height / 2)+(rpg.level_stuff.item_list[5].map_y_location//self.scale_map)))







    def draw_map(self):
        """This draws the map on the screen."""
        self.screen.blit(self.map_surface,self.map_surface_rect)




    