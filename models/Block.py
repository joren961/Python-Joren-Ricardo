class Block:
    def __init__(self, number = 0):
         self.set_number(self, number)
      
    # getter method
    def get_number(self):
        return self.number
      
    # setter method
    def set_number(self, x):
        self.number = x
