import numpy as np
import pickle
import pandas as pd
import sys

a = pd.DataFrame(np.ones((1000000, 2)), columns=['a', 'b'])
print(sys.getsizeof(a) / 1024 / 1024)
with open("array.pickle", "wb") as f:
    pickle.dumps(a)

with open('array.pickle', 'rb') as f:
    array = pickle.loads(f.read())
    print(sys.getsizeof(array) / 1024 / 1024)
