import time
import numpy as np
t0 = time.perf_counter()
i = int()
j = int()
c = 0
max = 100000000
data = np.ones((max),dtype=np.int16)
#data = {x:0 for x in range(2,  max + 1)}
for i in range(2, max):
    if(data[i] == 1):
        for j in range(2 * i, max , i):
                        data[j] = 0
#for i in data:
#    print(i)
print(time.perf_counter() - t0)
