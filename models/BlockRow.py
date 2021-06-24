from re import S
from models.Block import Block
from models.PinRow import PinRow
import random


class BlockRow:
    def __init__(self, row_number, position_amount):
        self.block_row = []

        for i in range(position_amount):
            self.block_row.append(Block(i))

        self.row_number = row_number
        self.pin_row = PinRow(position_amount)

    # getter method
    def get_block_row(self):
        return self.block_row

    # getter method
    def get_pin_row(self):
        return self.pin_row

    # getter method
    def get_string_code(self, block_row):
        code_string = ""
        for block in block_row.get_block_row():
            s = str(block.get_value())
            code_string += s + " "

        return code_string

    def randomize_block_row(self, number_amount, double_number):
        if int(double_number) == 1:
            for block in self.block_row:
                block.set_value(random.randint(1, number_amount))
        else:
            random_list = random.sample(range(1, number_amount + 1), len(self.block_row))
            for i in range(len(self.block_row)):
                self.block_row[i].set_value(random_list[i])

        return self
