class GameStats():
    
    def __init__(self, ai_settings):
        '''intialization'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
        
        self.game_active = False
        
        self.score = 0
        
        self.high_score = 0
        
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        
        