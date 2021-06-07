from models.Pin import Pin


class PinRow:
    def __init__(self, position_amount):
        self.pins = []
        for _ in range(position_amount):
            self.pins.append(Pin())

    # getter method
    def get_pins(self):
        return self.pins
