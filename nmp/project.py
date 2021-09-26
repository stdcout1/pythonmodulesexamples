import numpy as np
s1 = np.arange(2,10)
s2 = np.arange(22,100,10)
s3 = np.arange(202,910,100)
stacked = np.vstack((s1,s2,s3))
n = np.multiply.outer(s1,s2).ravel()
n = np.multiply.outer(n,s3).ravel()
results = np.unique(n)
print (results)