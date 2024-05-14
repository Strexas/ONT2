from minknow_api import Connection
from minknow_api.manager import Manager

manager = Manager()
# manager.add_simulated_device("MS00001", minknow_api.manager_pb2.SimulatedDeviceType.SIMULATED_MINION)
devices = [i for i in manager.flow_cell_positions()]

connection = Connection(8000, "127.0.0.1")
connection.protocol.stop_protocol(connection.protocol._pb.StopProtocolRequest(data_action_on_stop=connection.acquisition._pb.StopRequest.DataAction.STOP_KEEP_ALL_DATA))

print(devices)
