import numpy as np
'''this is numpy library oractice file'''

# print(np.__version__)
# arr = np.array([1, 2, 3, 4, 5])
# bigArr = np.array((1, 2, 3, 4, 5)) # 1- d array
# arr2 = np.array(42) # 0- d array
# arr3 =  np.array([[1, 2, 3], [4, 5, 6]]) # 2- d array
# arr4 = np.array([[[1, 2, 3], [4, 5, 6],[4, 5, 6]]])  # 3- d array
# print("---------------------")
# print("\n",arr2)
# print(arr,"\n")
# print(bigArr,"\n")
# print(arr2,"\n")
# print(arr3,"\n")
# print(arr4,"\n","\n")


# print(arr.ndim)
# print(arr2.ndim)
# print(arr3.ndim)
# print(arr4.ndim)
# arr5 = np.array([1, 2, 3, 4], ndmin=5)
# print(arr5 ," \n" ,arr5.ndim)
# print(type(arr))

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

arr3 = np.array([[[1, 2, 3,4], [4, 5, 6, 5]], [[7, 8, 9, 8], [10, 11, 12,9]]])

print(arr3[0, 1, 2])
print(arr3.dtype)



#We can also define the step, like this: [start:end:step].
newarr = np.array([1, 2, 3, 4], dtype='i4')


print(newarr.dtype)
print(newarr)
newarr1 = arr.astype('i')
arr5 = np.array([1, 0, 3])

newarr = arr5.astype(bool)
print(arr5, " " , arr5.dtype)
print(newarr, " " , newarr.dtype)
print(arr3[0,1,2:4])
x = newarr.view()
# print(newarr.view())
print(x.base)
latestarr = newarr.copy() # ----------change the original array 
print(latestarr)
print(latestarr.base)