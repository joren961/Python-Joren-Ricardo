from models.BlockRow import BlockRow


class Computer:
    def __init__(self):
        self.block_row = BlockRow()
        self.block_row.ramdomize_block_row()

        # getter method

    def get_block_row(self):
        return self.block_row
