class Player:
    def __init__(self, nickname):
        self.set_nickname(self, nickname)
    
    # getter method
    def get_nickname(self):
        return self.nickname
      
    # setter method
    def set_nickname(self, x):
        self.nickname = x