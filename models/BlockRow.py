from models.Block import Block
from models.PinRow import PinRow
import random

class BlockRow:
    def __init__(self, row_number):
         self.block_row = []
         for _ in range(4):
             self.block_row.append(Block())
         
         self.row_number = row_number
         self.pin_row = PinRow()
     
    # getter method
    def get_block_row(self):
        return self.block_row

    # getter method
    def get_pin_row(self):
        return self.pin_row

    def ramdomize_block_row(self):
        for block in self.block_row:
            block.set_number(random.randint(1, 4))
