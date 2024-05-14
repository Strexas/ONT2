from pipeline.Reader import Reader
from pipeline.Printer import Printer


reader = Reader()
printer = Printer()


reader.bind_o2i("raw_data", printer, "value")

reader.start()
printer.start()

