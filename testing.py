import random
import time

from BaseNode import BaseNode


class Randomizer(BaseNode):
    def __init__(self):
        super().__init__([], ["out"])

    def process(self):
        value = random.randint(1, 100)
        print(value, "INSIDE RANDOM")
        self.send_output("out", value)


class Printer(BaseNode):
    def __init__(self):
        super().__init__(["in"], [])

    def process(self):
        print(self.input_values["in"], "INSIDE PRINTER")


r = Randomizer()
p = Printer()


r.bind_o2i("out", p, "in")
r.start()
p.start()
