from models.Game import Game
from models.Player import Player

class GameController:

    def create_game(self, player, double_values, value_amount, position_amount, cheat):
        self.game = Game(Player(player), double_values, value_amount, position_amount, cheat)

    def get_game(self):
        return self.game

    def next_turn(self, turn, input_list):
        turn = int(turn)

        self.update_blocks(turn, input_list)
        self.update_pins(turn, input_list)
        self.check_if_won(turn, input_list)

        if(turn == 10):
            self.game_over()

        turn += 1
        self.game.set_turn(turn)

    def update_blocks(self, turn, input_list):
        block_row_list = self.game.get_block_row_list()
        
        for i in range(len(input_list)):
            block_row_list[turn-1].get_block_row()[i].set_value(int(input_list[i]))

        self.game.set_block_row_list(block_row_list)

    def update_pins(self, turn, input_list):
        block_row_list = self.game.get_block_row_list()
        
        for i in range(len(input_list)):
            self.game.get_computer_code().get_block_row()[i].set_is_used(False)

        for i in range(len(input_list)):
            if block_row_list[turn-1].get_block_row()[i].get_value() == self.game.get_computer_code().get_block_row()[i].get_value():
                for j in range(len(block_row_list[turn-1].get_pin_row().get_pins())):
                    if block_row_list[turn-1].get_pin_row().get_pins()[j].get_value() == "":
                        block_row_list[turn-1].get_pin_row().get_pins()[j].set_value(1)
                        block_row_list[turn-1].get_block_row()[i].set_is_used(True)
                        self.game.get_computer_code().get_block_row()[i].set_is_used(True)
                        break

        for i in range(len(input_list)):
            for j in range(len(self.game.get_computer_code().get_block_row())):
                if self.game.get_computer_code().get_block_row()[j].get_is_used() == False:
                    if block_row_list[turn-1].get_block_row()[i].get_value() == self.game.get_computer_code().get_block_row()[j].get_value():
                        for k in range(len(block_row_list[turn-1].get_pin_row().get_pins())):
                            if block_row_list[turn-1].get_pin_row().get_pins()[k].get_value() == "":
                                block_row_list[turn-1].get_pin_row().get_pins()[k].set_value(2)
                                self.game.get_computer_code().get_block_row()[j].set_is_used(True)
                                break  

        self.game.set_block_row_list(block_row_list)
 
    def check_if_won(self, turn, input_list):
        block_row_list = self.game.get_block_row_list()

        count = 0 
        for i in range(len(input_list)):
            if block_row_list[turn-1].get_pin_row().get_pins()[i].get_value() == 1:            
                count += 1
        
        if(count == len(input_list)):
            self.won_game()

    def won_game(self):
        print("You won")

    def game_over(self):
        print("You lost")
