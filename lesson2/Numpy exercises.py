# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 19:45:31 2018

@author: Thinkpad
"""
'''
Numpy exercises:
1. Create a null vector of size 10 but the fifth value which is 1
2. Create a vector with values ranging from 10 to 49 
3. Reverse a vector (first element becomes last) 
4. Create a 3x3 matrix with values ranging from 0 to 8 
5. Find indices of non-zero elements from [1,2,0,0,4,0] 
6. Create a 3x3 identity matrix 
7. Create a 3x3x3 array with random values 
8. Create a 10x10 array with random values and find the minimum and maximum values 
9. Create a random vector of size 30 and find the mean value 
10. Create a 2d array with 1 on the border and 0 inside 
'''
import numpy as np
#1. Create a null vector of size 10 but the fifth value which is 1
a1 = np.zeros([1, 10])
a1[(0,4)] = 1#it is parentheses () inside, not bracket []
#2. Create a vector with values ranging from 10 to 49 
a2 = np.arange(10,50)
#3. Reverse a vector (first element becomes last) 
a3 = a2[::-1]#is there any other way to complete this?
#4. Create a 3x3 matrix with values ranging from 0 to 8 
a4 = np.arange(9).reshape((3,3))
#5. Find indices of non-zero elements from [1,2,0,0,4,0] 
a5 = []
l5 = [1,2,0,0,4,0]
for i in range(len(l5)):
    if l5[i] != 0:
        a5.append(i)
#6. Create a 3x3 identity matrix 
a6 = np.eye(3)
#7. Create a 3x3x3 array with random values 
a7 = np.random.rand(3,3,3)
#8. Create a 10x10 array with random values and find the minimum and maximum values 
a8 = np.random.rand(10,10)
a8_min = a8.min()
a8_max = a8.max()
#9. Create a random vector of size 30 and find the mean value 
a9 = np.random.rand(30)
a9_mean = a9.mean()
#10. Create a 2d array with 1 on the border and 0 inside 
a10 = np.ones((5,5))
a10[1:-1, 1:-1] = 0



