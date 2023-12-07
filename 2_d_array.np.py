import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
# when size of two list are unequal then python treat as a 1-d array
b=np.array([[1,2,3],[1,2]])
print(b)
# when datatype of element is differ then python convert all element present in array into same data-type
c=np.array([[1.0,2,3],[6,7,8]])
print(c)
# object datatpe in python
d=np.array([[1,2,3],"hello"])
print(d)
