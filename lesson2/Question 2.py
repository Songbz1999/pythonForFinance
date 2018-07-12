# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:55:57 2018

@author: Thinkpad
"""


#----------------------------------------#
#Question 2
#
#Question:
#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010
#Notes: Assume the data is input by console.

#----------------------------------------#

def bin_div5():
    l = input("give me a sequence of comma separated 4 digit binary numbers: ")
    raw = l.split(',')
    ans = []
    for i in raw:
        if int(i,2) % 5 == 0:
            ans.append(i)
    return ans
print(' '.join(bin_div5()))
            