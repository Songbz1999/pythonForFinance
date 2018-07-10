# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 01:40:24 2018

@author: Thinkpad
"""

#----------------------------------------#
#Question 3
#Level 1
#
#Question:
#With a given integral number n, write a program to generate a dictionary that 
#contains (i, i*i) such that is an integral number between 1 and n (both included). 
#and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
#----------------------------------------#
def func_1_3 ():
    n = int (input ( "give me a number: ") )
    d = {}
    for i in range(n):
        d[i+1] = ( i + 1 ) ** 2
    return d

print(func_1_3())