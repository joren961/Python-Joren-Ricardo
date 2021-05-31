from models.Pin import Pin

class PinRow:
    def __init__(self):
         self.pin_row = []
         for _ in range(4):
             self.pin_row.append(Pin())
      
    # getter method
    def get_pin_row(self):
        return self.pin_row