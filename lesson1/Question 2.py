# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 20:57:08 2018

@author: Thinkpad
"""

#----------------------------------------#
#Question 2
#Level 1
#
#Question:
#Write a program which can compute the factorial of a given numbers.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#----------------------------------------#
def fac():
    n=8
    ans=1
    for i in range(n):
        ans=ans*(i+1)
    print(ans)
fac()    
