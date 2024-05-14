from read_until import ReadUntilClient
import numpy
from .BaseNode import BaseNode


class Reader(BaseNode):
    def __init__(self):
        super().__init__([], ['raw_data'])

        self.ont_data_reader = ReadUntilClient()
        self.ont_data_reader.run()

    def process(self):
        read_batch = self.ont_data_reader.get_read_chunks()
        for channel, read in read_batch:
            raw_data = numpy.fromstring(read.raw_data, self.ont_data_reader.signal_dtype)
            self.send_output("raw_data", raw_data)
