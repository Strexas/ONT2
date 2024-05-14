import random
import time

from BaseNode import BaseNode
from testing import Printer

from minknow_api.manager import Manager
from minknow_api.data import get_signal
import minknow_api
from minknow_api.data_service import DataService
from minknow_api import Connection
from minknow_api.acquisition_service import AcquisitionService
from minknow_api.device_service import DeviceService


class MinONEmulator(BaseNode):
    def __init__(self, device_name):
        super().__init__([], ["raw_data"])
        self.device_name = device_name

        manager = Manager()
        # manager.remove_simulated_device(device_name)
        #
        # time.sleep(10)  # Wait while device is deleting
        # manager.add_simulated_device(device_name, minknow_api.manager_pb2.SimulatedDeviceType.SIMULATED_MINION)
        print([i.device_type for i in manager.flow_cell_positions()])

    def process(self):
        time.sleep(5)
        self.send_output("raw_data", random.randint(0, 1))


# emulator = MinONEmulator("MS00000")
# printer = Printer()
#
# emulator.bind_o2i("raw_data", printer, "value")
# emulator.start()
# printer.start()

from minknow_api.tools import protocols

manager = Manager()
manager.add_simulated_device("MS00002", minknow_api.manager_pb2.SimulatedDeviceType.SIMULATED_MINION)
devices = [i for i in manager.flow_cell_positions()]
print(devices)
# stop_condition = protocols.CriteriaValues(runtime=72 * 60 * 60)
# outputargs = protocols.OutputArgs(reads_per_file="fast5s_reads_per_file")
# run_id = protocols.start_protocol(connection,
#                                   identifier="1",
#                                   sample_id="test_sample1",
#                                   experiment_group="test_experiment1",
#                                   barcode_info=[],
#                                   stop_criteria=stop_condition,
#                                   fast5_arguments=outputargs)

# ds = DeviceService()
# ds.set_user_specified_flow_cell_id(1)

# print(get_signal(connection))
