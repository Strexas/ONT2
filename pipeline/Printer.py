from .BaseNode import BaseNode


class Printer(BaseNode):
    def __init__(self):
        super().__init__(["value"], [])

    def process(self):
        print("Printer: ", self.input_values["value"])
