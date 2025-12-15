import numpy as np
a = np.array(['10', '11','12','34'] , dtype=int)
b = np.array(['57', '874','74','73'] , dtype=int)
c = a ** b 
d= np.random.randint(0,3,(2,3))
print (d)
print(d.ndim)
print(d.size)
print(d.data)
e = np.mean(a)
print(e)