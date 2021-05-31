from enum import Enum

enum_color = Enum('Color', 'None White Black')

class Pin:
    # def __init__(self, color = enum_color.None):
    #      self.set_color(self, color)

    # getter method
    def get_color(self):
        return self.color
      
    # setter method
    def set_color(self, color):
        self.color = color
