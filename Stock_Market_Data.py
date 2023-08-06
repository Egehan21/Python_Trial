import numpy as np

x=np.array([1,2,3], ndmin=8)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7,8,9], [10,11,12]]])

print(d[1,0,0]+d[1,1,2])

arr1 = np.array([1, 2, 3, 4, 5, 6, 7])

result = d[:, 0, :2][:, 0]
print(result)

arr = np.array([1.1, 2.1, 3.1],dtype='i4')
print(arr.dtype)
#print(d[0,0, 1:2 , 1,0,:2])


'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:6:3])
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:])

print(c[1, 1:])
print(d[1, 0, 1:])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(x)
print(x.ndim)



example_array=np.array=([1,2,3,4,5,[2,3,4]])

print(example_array.ndim)

#ab = np.array([42])
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(ab.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) '''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr[0] = 31

print(arr)
