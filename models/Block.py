class Block:
    def __init__(self, number):
        self.number = number
        self.value = ""

    # getter method
    def get_number(self):
        return self.number

    # getter method
    def get_value(self):
        return self.value

    # setter method
    def set_value(self, value):
        self.value = value
