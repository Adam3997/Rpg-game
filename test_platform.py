import pygame

from physics_stats import Physics_stats
from player import Player
from physics import Physics
from enemy_logic import Overworld_person

class test_platform():
    """this will be used for testing new code without having
    to use the full game code. """


    def test_code(self):
        """initializes"""

        pygame.init()

        # sets up the screen.
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        # clock for framerate.
        self.clock = pygame.time.Clock()
        #font in case its needed
        self.font = pygame.font.SysFont(None,48)
        self.text_color = (30,30,30)
        self.bg_color = (250,250,250)
        
        # this says the test is true and thus the code will run. 
        self.test = True

        self.player_1_test = Player(self)
        self.physics_test = Physics(self)

        self.dt = 0
        # test code can go here and then be deleted when done

        self.test_physics = Physics_stats()

        n = 0
        m = 100
        self.enemy_list = []
        while n <= m:
            j = Overworld_person(self)
            j.id_number = n
            #print(j.id_number)
            self.enemy_list.append(j)


            n += 1


        # test code above. and below as needed to blit to screen. 
        while self.test:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.test = False
            self.clock.tick(60)
            self.dt = self.clock.tick(60) / 1000
            self.screen.fill(self.bg_color)
            #self.player_1_test.movement_test(self)
            self.physics_test.movement_2(self)
            self.player_1_test.draw_me(self)
            self.physics_test.detect_collisions_bounce(self)
            n = 0
            m = len(self.enemy_list) - 1
            while n <= m:
                self.enemy_list[n].draw_me()
                n += 1
            self.physics_test.enemy_loop(self)
            self.player_1_test.attack_cycle(self)

            
            
            
          
          
            
                
            pygame.display.flip()




if __name__ == '__main__':
    testing = test_platform()
    testing.test_code()