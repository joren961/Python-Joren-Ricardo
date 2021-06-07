from models.BlockRow import BlockRow
import datetime


class Game:
    def __init__(self, player, double_number, number_amount, position_amount, cheat):
        self.startDatetime = datetime.datetime
        self.cheat = int(cheat)
        self.finished = False
        self.turn = 1
        self.player = player
        self.double_number = double_number
        self.number_amount = number_amount
        self.position_amount = position_amount
        self.block_row_list = []
        
        for i in range(10):
            self.block_row_list.append(BlockRow(i, position_amount))

        self.computer_code = self.randomize_code()

    def randomize_code(self):
        random_block_row = BlockRow(0, self.position_amount)
        random_block_row = random_block_row.randomize_block_row(self.number_amount)
        return random_block_row

    # getter method
    def get_player(self):
        return self.player
      
    # getter method
    def get_cheat(self):
        return self.cheat

    # getter method
    def get_number_amount(self):
        return self.number_amount

    # getter method
    def get_position_amount(self):
        return self.position_amount

    # getter method
    def get_computer_code(self):
        return self.computer_code

    # getter method
    def get_block_row_list(self):
        return self.block_row_list

    # getter method
    def set_block_row_list(self, value):
        self.block_row_list = value

    # getter method
    def get_double_number(self):
        return self.double_number

    # getter method
    def get_turn(self):
        return self.turn
    
    # setter method
    def set_turn(self, value):
        self.turn = value


