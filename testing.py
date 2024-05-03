import random
import time

from Node import BaseNode


class Randomizer(BaseNode):
    def __init__(self):
        super().__init__([], ["out"])

    def process(self):
        value = random.randint(1, 100)
        print(value, "INSIDE RANDOM")
        self.send_output("out", value)


class Printer(BaseNode):
    def __init__(self):
        super().__init__(["value"], [])

    def process(self):
        print(self.input_values["value"], "INSIDE PRINTER")