import sys

import numpy as np
import requests
import pickle

import time
start = time.time()
data = np.ones((10, 1))
print("SEND: ", sys.getsizeof(data), "MB")
res = requests.post('http://127.0.0.1:8080', data=pickle.dumps(data.copy()))
array = pickle.loads(res.content)
print(data)
print(array)
print(array.nbytes / 1024 / 1024)
print(sys.getsizeof(array))
print("time:", time.time() - start)
