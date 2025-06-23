import pygame

class Sound_logic():
    """This is the class for sound in the game"""


    def __init__(self,rpg):
        try:

            # boss stuff
            self.fire_sound_1 = pygame.mixer.Sound('_internal\\fire_blaze_3.mp3')
            self.fire_sound_1_natural_level = 0.6
            self.fire_sound_2 = pygame.mixer.Sound('_internal\\fire_blaze_4.mp3')
            self.fire_sound_2_natural_level = 0.6
            self.bang_sound_1 = pygame.mixer.Sound('_internal\\loud_bang.mp3')
            self.bang_sound_1_natural_level = 0.8
            
            
            # other sounds
            # these are overall sound settings
            self.bite_sound = pygame.mixer.Sound('_internal\\bite.mp3')
            self.bite_sound_natural_level = 1.0
            
            
            self.click_1_sound = pygame.mixer.Sound('_internal\\click_sound_2.mp3')
            self.click_1_sound_natural_level = 1.0
            self.fire_crackle_sound = pygame.mixer.Sound('_internal\\fire_crackle.mp3')
            self.fire_crackle_sound_natural_level = 1.0
            self.screach_sound = pygame.mixer.Sound('_internal\\screach.mp3')
            self.screach_sound_natural_level = 1.0
            

            # this will be backgrounds sounds.
            self.owl_background_noise = pygame.mixer.Sound('_internal\\owl_fake.mp3')
            self.owl_background_noise_natural_level = 1.0
            self.cracking_noise = pygame.mixer.Sound('_internal\\cracking.mp3')
            self.cracking_noise_natural_level = 1.0
            self.stab_sound = pygame.mixer.Sound('_internal\\stab_2.mp3')
            self.stab_sound_natural_level = 1.0
            self.footstep_sound = pygame.mixer.Sound("_internal\\footstep.mp3")
            self.footstep_sound_natural_level = 0.2
            self.footstep_sound_2 = pygame.mixer.Sound('_internal\\footstep_2.mp3')
            self.footstep_sound_2_natural_level = 0.1
            self.grunt_sound = pygame.mixer.Sound('_internal\\grunt.mp3')
            self.grunt_sound_natural_level = 1.0
            self.spooky_sound = pygame.mixer.Sound('_internal\\spooky_noise.mp3')
            self.spooky_sound_natural_level = 1.0
            self.spooky_sound_2 = pygame.mixer.Sound('_internal\\spooky_noise_2.mp3')
            self.spooky_sound_2_natural_level = 1.0
            self.wind_1_sound = pygame.mixer.Sound('_internal\\wind_1.mp3')
            self.wind_1_sound_natural_level = 1.0
            self.wind_2_sound = pygame.mixer.Sound('_internal\\wind_2.mp3')
            self.wind_2_sound_natural_level = 1.0
            self.splat_rev_sound = pygame.mixer.Sound('_internal\\hit_rev.mp3')
            self.splat_rev_sound_natural_level = 1.0
            self.cat_rev_sound = pygame.mixer.Sound('_internal\\cat_rev.mp3')
            self.cat_rev_sound_natural_level = 1.0
            self.whistle_sound = pygame.mixer.Sound('_internal\\whistle_1.mp3')
            self.whistle_sound_natural_level = 1.0
            self.whistle2_sound = pygame.mixer.Sound('_internal\\whistle_rev.mp3')
            self.whistle2_sound_natural_level = 1.0
            
            
            # this is general volume
            self.bite_attack_sound = pygame.mixer.Sound('_internal\\bite_filtered.mp3')
            self.bite_attack_sound_natural_level = 1.0
            self.player_hit_sound = pygame.mixer.Sound('_internal\\yell.mp3')
            self.player_hit_sound_natural_level = 1.0
            self.player_interact_sound = pygame.mixer.Sound('_internal\\tapping_rain.mp3')
            self.particle_hit_sound_natural_level = 1.0
            self.particle_hit_sound = pygame.mixer.Sound('_internal\\hit_particle_2.mp3')
            self.player_interact_sound_natural_level = 1.0 # this is switched with the one above
            self.enemy_move_sound = pygame.mixer.Sound('_internal\\rain_abrupt.mp3')
            self.enemy_move_sound_natural_level = 1.0
            
            
            # this is dialogue
            self.before_boss_1_dialogue = pygame.mixer.Sound('_internal\\before_boss_dialogue_fixed.mp3')
            self.before_boss_1_dialogue_natural_level = 1.0
            self.dialogue_1 = pygame.mixer.Sound('_internal\\dialogue_1_fixed.mp3')
            self.dialogue_1_natural_level = 1.0
            # this is dialogue volume
            self.dialogue_1.set_volume(self.dialogue_1_natural_level)
            self.before_boss_1_dialogue.set_volume(self.before_boss_1_dialogue_natural_level)

            # this is the background.
            self.footstep_sound_2.set_volume(self.footstep_sound_2_natural_level)
            self.footstep_sound.set_volume(self.footstep_sound_natural_level)
            self.stab_sound_limit = 1
            pygame.mixer.music.load('_internal\\rocks.mp3')
            self.music_natural_level = 0.12 # 0.2 is too loud.
            pygame.mixer.music.set_volume(self.music_natural_level * rpg.settings_hold.max_volume)
        except:
            print('Missing sound File')
            rpg.game = False
    
    

    def update_sound_levels(self,rpg):
        """"""

            #overall volume here
        self.fire_sound_1.set_volume(self.fire_sound_1_natural_level * rpg.settings_hold.max_volume)
        self.fire_sound_2.set_volume(self.fire_sound_2_natural_level * rpg.settings_hold.max_volume)
        self.fire_crackle_sound.set_volume(self.fire_crackle_sound_natural_level * rpg.settings_hold.max_volume)
        self.bang_sound_1.set_volume(self.bang_sound_1_natural_level * rpg.settings_hold.max_volume)
        self.bite_attack_sound.set_volume(self.bite_attack_sound_natural_level * rpg.settings_hold.max_volume)
        self.click_1_sound.set_volume(self.click_1_sound_natural_level * rpg.settings_hold.max_volume)
        self.screach_sound.set_volume(self.screach_sound_natural_level * rpg.settings_hold.max_volume)
        self.cracking_noise.set_volume(self.cracking_noise_natural_level * rpg.settings_hold.max_volume)
        self.stab_sound.set_volume(self.stab_sound_natural_level * rpg.settings_hold.max_volume)
        self.grunt_sound.set_volume(self.grunt_sound_natural_level * rpg.settings_hold.max_volume)
        self.splat_rev_sound.set_volume(self.splat_rev_sound_natural_level * rpg.settings_hold.max_volume)
        self.bite_attack_sound.set_volume(self.bite_attack_sound_natural_level * rpg.settings_hold.max_volume)
        self.player_hit_sound.set_volume(self.player_hit_sound_natural_level * rpg.settings_hold.max_volume)
        self.player_interact_sound.set_volume(self.player_interact_sound_natural_level * rpg.settings_hold.max_volume)
        self.particle_hit_sound.set_volume(self.particle_hit_sound_natural_level * rpg.settings_hold.max_volume)
        self.enemy_move_sound.set_volume(self.enemy_move_sound_natural_level * rpg.settings_hold.max_volume)



        # dialogue volume here
        self.before_boss_1_dialogue.set_volume(self.before_boss_1_dialogue_natural_level * rpg.settings_hold.dialogue_volume * rpg.settings_hold.max_volume)
        self.dialogue_1.set_volume(self.dialogue_1_natural_level * rpg.settings_hold.dialogue_volume * rpg.settings_hold.max_volume)


        #background volume here
        self.owl_background_noise.set_volume(self.owl_background_noise_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        self.footstep_sound.set_volume(self.footstep_sound_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        self.spooky_sound.set_volume(self.spooky_sound_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        self.wind_1_sound.set_volume(self.wind_1_sound_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        self.wind_2_sound.set_volume(self.wind_2_sound_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        self.whistle_sound.set_volume(self.whistle_sound_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        self.whistle2_sound.set_volume(self.whistle2_sound_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        self.cat_rev_sound.set_volume(self.cat_rev_sound_natural_level * rpg.settings_hold.background_volume * rpg.settings_hold.max_volume)
        




    def update_current_volume(self,rpg):
        """"""
            