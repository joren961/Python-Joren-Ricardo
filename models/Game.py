from models.BlockRow import BlockRow
from models.Computer import Computer
import datetime

class Game:
    def __init__(self, player, double_values, value_amount, position_amount, cheat, computer):
        self.startDatetime = datetime.datetime
        self.cheat = cheat
        self.finished = False
        self.round = 1
        self.player = player
        self.double_values = double_values
        self.value_amount = value_amount
        self.position_amount = position_amount
        self.computer = Computer(self.value_amount, self.position_amount)
        self.block_row_list = []
        for i in range(10):
            self.block_row_list.append(BlockRow(i, self.value_amount, self.position_amount))

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
