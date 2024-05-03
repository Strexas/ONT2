from minknow_api.manager import Manager
import os
os.environ["MINKNOW_TRUSTED_CA"] = "/home/dainius/PycharmProjects/ONT/Icarust/static/tls_certs/ca.crt"
from minknow_api.manager import Manager
m = Manager()
pos = list(m.flow_cell_positions())
# print(pos)
# con = pos[0].connect()
# print(con)
# con.instance.get_version_info()
