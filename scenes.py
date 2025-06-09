import pygame
from cut_scene import Cut_scene
import random

class Scenes():
    """This is the class for holding a specific cut scene.
    With alll the stuff needed for a scene."""

    def __init__(self,rpg):
        """This initializes the scene"""
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (128,70,27)
        self.bg_color = (79,121,66)
        # this says the test is true and thus the code will run. 
        self.test = False
        
        self.dt = 0

        #test code for cut scenes
        self.cut_scene_test = Cut_scene(self,movements=((-50,0),(50,0)),timing=(5,10),text=('''The beast’s roar cut through the woods, sending birds flying; their shapes as fleeting as\n shooting stars in the night, however Ragnar gazed upon the beast; unperturbed.\n
“The sound of animals haunts my dreams.” Ragnar readies himself for battle. “Calling me\n to battle, a great challenge has arrived.”\n
The beast bares its fangs; dripping venom as if flowing from a river. Suddenly a hiss from\n the belly of the cornered animal signals the start of the fight. \n
… boss fight begins. 
''','second text'),directions=('left','right'))

        




    def perform_cut_scene_1(self,rpg):
        """This is the first cut scene"""

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rpg.game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            rpg.game = False
        """if keys[pygame.K_SPACE]:
            #self.cut_scene_test.particle_for_cut_scene.set_particle_active_cut_scene(100,50)
            w = 0
            x = len(self.cut_scene_test.particle_cut_scene_list) - 1
            while w <= x:
                y = random.randrange(-200,200)
                z = random.randrange(1000,1200)
                self.cut_scene_test.particle_cut_scene_list[w].set_particle_active_cut_scene(y,z)
                w += 1"""
        self.clock.tick(60)
        self.dt = self.clock.tick(60) / 1000
        self.screen.fill(self.bg_color)
        self.cut_scene_test.cut_scene_boss.draw_me_for_cut_scene_1(self)
        self.cut_scene_test.cycle_cut_scene(rpg)
        #self.cut_scene_test.check_camera_change_ends()

        #del self.mouse_pos
            
            
            
        #pygame.display.flip()