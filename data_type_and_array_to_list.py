import numpy as np
a=np.array([1,2,3])

# print data type of an array

print(a.dtype)



#set data type of an array during creating array and then print data type

b=np.array([1,2,3],dtype='int16')
print(b.dtype)







#set data type of an array through astype() function call
b=a.astype('int8')
print(b.dtype)





#convert array to list
l1=a.tolist()
print(l1)

