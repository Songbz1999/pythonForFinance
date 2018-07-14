# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 16:48:04 2018

@author: Thinkpad
"""
import numpy as np
#Numpy:
#
#1. How to add a border (filled with 0's) around an existing array?
a1 = np.pad(np.ones((2,2)),1,'constant')
#2. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal  
a2 = np.diag(np.arange(4) + 1, -1)
#3. Create a 8x8 matrix and fill it with a checkerboard pattern 
a3 = np.zeros((8,8))
a3[::2,::2] = 1
a3[1::2,1::2] = 1
#4. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element 
a4 = np.unravel_index(100, (6,7,8))
#>>> np.unravel_index([22, 41, 37], (7,6))
#(array([3, 6, 6]), array([4, 5, 1]))
#>>> np.unravel_index([31, 41, 13], (7,6), order='F')
#(array([3, 6, 6]), array([4, 5, 1]))

#5. Create a checkerboard 8x8 matrix using the tile function
a5 = np.tile(a3, (2,2))
#6. How to add a border (filled with 0's) around an existing array? 
a6 = a1
#7. What is the result of the following expression? 
''' ? '''
#8. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal 
a8 = a2
#9. Create a 8x8 matrix and fill it with a checkerboard pattern 
a9 = a3
#10. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
a10 = a4
#11. Create a checkerboard 8x8 matrix using the tile function 
a11 = a5
#12. Normalize a 5x5 random matrix 
a12 = np.random.randint(2,10,(3,3))
a12 = (a12-a12.min())/(a12.max()-a12.min())
#13. Create a custom dtype that describes a color as four unsigned bytes (RGBA) 
a13 = np.dtype(('R',int, 1),('G',int, 1),('B',int, 1),('A',int, 1))
#14. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) 
a14 = np.dot(np.ones((5,3)),np.ones((3,2)))
#15. Given a 1D array, negate all elements which are between 3 and 8, in place.
a15 = np.random.randint(1,10,8)
a15[(a15 < 8) & (a15 > 3)] *= -1
#16. How to get all the dates corresponding to the month of July 2016?
'''?'''
#17. Consider two random array A and B, check if they are equal
a17 = np.allclose(np.random.randint(1,3,3), np.random.randint(1,3,3))
#18. How to convert a float (32 bits) array into an integer (32 bits) in place?
a18 = np.ones((2,2),dtype=np.float32)
a18 = a18.astpye(np.int32, copy = False) '''?'''
#19. Compute a matrix rank?
a19 = np.linalg.matrix_rank(a1)
#20. How to get the n largest values of an array?
a20 = a15[np.argsort(a15)[-3]]