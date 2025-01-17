import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("array a:", a)
print("array b:", b)

c = np.concatenate((a, b))
print("array c:", c)

d = np.array([[1, 2], [3, 4]])
e = np.array([[5, 6], [7, 8]])
print("array d:", d)
print("array e:", e)

f = np.concatenate((d, e), axis=0)
print("array f:", f)
g = np.concatenate((d, e), axis=1)
print("array g:", g)

h = np.vstack((d, e))
print("array h:", h)

i = np.hstack((d, e))
print("array i:", i)
'''
array a: [1 2 3]
array b: [4 5 6]
array c: [1 2 3 4 5 6]
array d: [[1 2]
 [3 4]]
array e: [[5 6]
 [7 8]]
array f: [[1 2]
 [3 4]
 [5 6]
 [7 8]]
array g: [[1 2 5 6]
 [3 4 7 8]]
array h: [[1 2]
 [3 4]
 [5 6]
 [7 8]]
array i: [[1 2 5 6]
 [3 4 7 8]]
'''