#import numpy module

import numpy as np




#make 2 dimensional array of float32 data type

a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='float32')
print(a)




#insert not a number value at first row first column

a[1][1]=np.nan
print(a)
