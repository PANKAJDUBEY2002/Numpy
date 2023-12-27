#import numpy module
import numpy as np

#create 1-d array which contains zeroes
a=np.zeros(3)
print(a)
print(a.dtype)




#create 2-darrat which contains zeroes
a=np.zeros((3,4))
print(a)
print(a.dtype)




#create 1-d array which contains ones
a=np.ones(3)
print(a)
print(a.dtype)




#create 2-d array which containd ones
a=np.ones((3,4))
print(a)
print(a.dtype)



#create 1-d array which contain specific value
a=np.full(3,11)
print(a)
print(a.dtype)




#create 2-d array which contain specific value
a=np.full((2,3),11)
print(a)
print(a.dtype)






#create identity matrix
a=np.identity(3)
print(a)
print(a.dtype)





#create random matrix
a=np.random.rand(3,5)
print(a)
print(a.dtype)







#cretae random matrix which contain values b/w upper limit and lower limit which exclude upper limit
a=np.random.randint(3,12,size=(2,3))
print(a)
print(a.dtype)
