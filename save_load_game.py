import json
from pathlib import Path

class Save_and_load_game():
    """This is the save and load logic."""


    def __init__(self,rpg,save_number):
        """Whatever must be initialized"""
        words = 'save_game_'
        save_number = str(save_number)
        words += save_number
        words += '_save.json'
        self.path = Path(words)
        self.save_numer = save_number
        self.words = words

        self.save_game_text_up_timer = 200
        self.save_game_text_up_timer_old = self.save_game_text_up_timer
        
    

    def save_game(self,rpg):
        """This is the save game logic"""

        # add in things that are saved
        # they will be saved in a dict

        player_score = []
        player_health = []
        #player_location = []
        level_current = []
        boss_health = [] # i will save only after a level is beaten so i do not need this.
        magic_active = []
        n = 0
        m = 1 # this will be chnaged to be dynamic later.

        
        player_score.append(rpg.level_stuff.player_1.score)
        level_current.append(rpg.level_stuff.current_level_tracker)
        player_health.append(rpg.level_stuff.player_1.health)
            
        

        save_dict = {'score':[player_score],'level':[level_current],'health':[player_health]} # thats enough for now. will be improved as needed.
        contents = json.dumps(save_dict)
        self.path.write_text(contents)


    
    def load_game(self,rpg):
        """This will load the data to restart the game"""
        #path = Path('save_game_1_full_save.json')
        #contents = path.read_text()
        #information_roster = json.loads(contents
        try:
            path = Path(self.words)
            contents = path.read_text()
            information_loaded = json.loads(contents)
            
            
            rpg.level_stuff.player_1.score = information_loaded['score'][0][0]
            rpg.level_stuff.current_level_tracker = information_loaded['level'][0][0]
            rpg.level_stuff.player_1.health = information_loaded['health'][0][0]
        except:
            pass # i will add something that displays text to screen to tell the player this happened.
        #print('data is loaded')
        #print(rpg.level_stuff.player_1.score,rpg.level_stuff.current_level_tracker )
        