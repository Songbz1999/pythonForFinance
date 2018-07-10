# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 01:49:08 2018

@author: Thinkpad
"""

#----------------------------------------#
#Question 4
#Level 1
#
#Question:
#Write a program which accepts a sequence of comma-separated numbers from console 
#and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

#----------------------------------------#
#dir (l)
#help (l.split)
def txt_list ():
    l = input ("give me a sequence of comma-separated numbers: ")
    ans=  l.split (',')
    return ans

ans = txt_list()
print (ans)
print (tuple (ans))