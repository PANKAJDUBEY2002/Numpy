#import numpy module
import numpy as np


# make array by read data from text file
a=np.genfromtxt('data.txt',delimiter=',')
print(a)




# change data type of created nupy array from float to int32
a=a.astype('int32')
print(a)
