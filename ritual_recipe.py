

class Ritual_recipe():
    """This is the recipe for the ritual
    This keeps track of which is done first and handles
    the logic for the ritual and how it affects gameworld."""

    def __init__(self,rpg):
        
        self.screen = rpg.screen
        self.screen_rect = rpg.screen.get_rect()

        self.need_to_check = True
        self.need_to_perform = False

        self.invoke_glory = False #invoke = bring in
        self.evoke_glory = False # evoke bring out or surround.

        self.invoke_war = False
        self.evoke_war = False

        self.invoke_life = False
        self.evoke_life = False

        self.invoke_knowledge = False
        self.evoke_knowledge = False

        self.alternate_ending = False


        
        self.first = ''
        self.second = ''
        self.third = ''
        self.fourth = ''
        self.current_spot_in_ritual_code = 0

        #self.ritual_count = 0
        self.first_ritual = False
        self.second_ritual = False
        self.third_ritual = False
        self.fourth_ritual = False

    def check_for_finished_ritual(self):
        """this checks if the invoke/evoke should
        become active."""
        if self.need_to_check:
            #print('checking')
            #self.check_glory()
            #self.check_knowledge()
            #self.check_life()
            self.check_war()
        """if self.need_to_perform:
            self.perform_war(rpg)"""
            

    def perform_glory(self,rpg):
        """Sets the spell to affect game""" # meaning this is what changes the stats or whatever as nessecary.
        if self.need_to_perform:
            if self.evoke_glory:
                rpg.level_stuff.player_1.score += 5000
                #self.ritual_count += 1
                rpg.level_stuff.level_1_boss.health += 100
                self.need_to_perform = False
            if self.invoke_glory:
                rpg.level_stuff.player_1.score **= 2
                rpg.level_stuff.player_1.health /= 2
                self.need_to_perform = False

    def perform_war(self,rpg):
        """This sets the stat changes for war ritual"""
        if self.need_to_perform:
            #print('need to perform is true')
            if self.evoke_war:
                """"""
                #print('war changed')
                self.need_to_perform = False
                n = 0
                m = len(rpg.level_stuff.enemy_list)
                while n < m:
                    rpg.level_stuff.enemy_list[n].damage *= 2
                    rpg.level_stuff.enemy_list[n].damage_old *= 2
                    n += 1
            if self.invoke_war:
                """"""
                #print('war invoked')
                rpg.level_stuff.level_1_boss.invoke_war_attack = True
                rpg.level_stuff.level_1_boss.health += 50
                self.need_to_perform = False
    
    def perform_life(self,rpg):
        """This sets the stat changes for life ritual"""
        if self.need_to_perform:
            if self.evoke_life:
                """"""
                rpg.level_stuff.player_1.health += 100
                rpg.level_stuff.level_1_boss.health += 100
                self.need_to_perform = False
            if self.invoke_life:
                """"""
                rpg.level_stuff.player_1.extra_life_invoked = True
                rpg.level_stuff.player_1.health += 20
                self.need_to_perform = False
                # this will give a backup life
    def perform_knowledge(self,rpg):
        """This sets the stat changes for knowledge ritual"""
        if self.need_to_perform:
            if self.evoke_knowledge:
                """"""
                self.alternate_ending = True
                self.need_to_perform = False
            if self.invoke_knowledge:
                """"""
                rpg.level_stuff.level_1_boss.alternate_death_method = True
                self.need_to_perform = False
        

    def check_glory(self):
        """This checks for glory spell/code"""
        if self.first == 'cross' and self.second =='bowl' and self.third =='pond' and self.fourth =='plant':
            self.evoke_glory = True
            self.need_to_check = False
            self.need_to_perform = True
        if self.first == 'cross' and self.second =='pond' and self.third =='pillar' and self.fourth =='plant':
            self.invoke_glory = True
            self.need_to_check = False
            self.need_to_perform = True

    def check_war(self):
        """This checks for glory spell/code"""
        if self.first == 'stone' and self.second =='bowl' and self.third =='pillar' and self.fourth =='plant':
            self.evoke_war = True
            self.need_to_check = False
            self.need_to_perform = True
        if self.first == 'pillar' and self.second =='pond' and self.third =='stone' and self.fourth =='plant':
            self.invoke_war = True
            self.need_to_check = False
            self.need_to_perform = True
            #print('ritual done')
    
    def check_life(self):
        """This checks for glory spell/code"""
        if self.first == 'plant' and self.second =='bowl' and self.third =='pond' and self.fourth =='stone':
            self.evoke_glory = True
            self.need_to_check = False
            self.need_to_perform = True
        if self.first == 'plant' and self.second =='pond' and self.third =='bowl' and self.fourth =='stone':
            self.invoke_glory = True
            self.need_to_check = False
            self.need_to_perform = True
    
    def check_knowledge(self):
        """This checks for glory spell/code"""
        if self.first == 'pond' and self.second =='bowl' and self.third =='stone' and self.fourth =='plant':
            self.evoke_glory = True
            self.need_to_check = False
            self.need_to_perform = True
        if self.first == 'pond' and self.second =='bowl' and self.third =='plant' and self.fourth =='stone':
            self.invoke_glory = True
            self.need_to_check = False
            self.need_to_perform = True