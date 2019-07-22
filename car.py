class Car():
    
    def __init__(self, model, year):
        '''initialization'''
        self.model = model
        self.year = year
        
    def move(self):
        print(self.model + " moves")

