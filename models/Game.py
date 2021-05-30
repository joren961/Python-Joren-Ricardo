import datetime


class Game:
    def __init__(self, player, double_colors, color_amount, position_amount, cheat):
        self.startDatetime = datetime.datetime
        self.cheat = cheat
        self.finished = False
        self.round = 1
        self.player = player
        self.doubleColors = double_colors
        self.colorAmount = color_amount
        self.positionAmount = position_amount

    # def generate_code(self):
    #
    #
    # # def play(self):
    # #
    # #
    # # def toggle_cheat(self):
    # #     if self.cheat:
    # #         self.cheat = False
    # #     else:
    # #         self.cheat = True
