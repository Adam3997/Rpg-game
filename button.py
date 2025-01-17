import pygame.font

class Button:
    """A class to build buttons for a game."""

    def __init__(self,gaming, msg,location):
        """Initialize button atributes."""
        self.screen = gaming.screen
        self.screen_rect  = self.screen.get_rect()

        # set the dimensions and properties of the button.
        self.width, self.height = 200,50
        self.width_2, self.height_2 = 100,60
        self.button_color = (0, 135, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        

        
        if location == 1:
            # set the dimensions and properties of the button.
            #self.width, self.height = 200,50
            #self.button_color = (0, 135, 0)
            #self.text_color = (255,255,255)
            #self.font = pygame.font.SysFont(None,48)
            
            # build the button's rect object and center it.
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
        elif location == 2:
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.midleft = self.screen_rect.midleft
            #self.font = pygame.font.SysFont(None,28)
            # set the dimensions and properties of the button.
            #self.width, self.height = 200,50
            #self.button_color = (0, 135, 0)
            #self.text_color = (255,255,255)
            #self.font = pygame.font.SysFont(None,48)
        elif location  == 3:
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.topleft = self.screen_rect.topleft
        elif location == 4: # this goes to midtop and is smaller button. for price pick page. 
            self.rect = pygame.Rect(0, 0, self.width_2, self.height_2)
            self.rect.midtop = self.screen_rect.midtop
            self.rect.centery +=  300
        elif location == 5:
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.midbottom = self.screen_rect.midbottom

        # the button message needs to be prepped only once
        self.prep_msg(msg)
    
    def prep_msg(self,msg):
        """turn msg into a rendered image and center the text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
