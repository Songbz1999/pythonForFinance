# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:06:30 2018

@author: Thinkpad
"""

#----------------------------------------#
#Question 1
#
#Question:
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world

#----------------------------------------#
def txt_list():
    t = input ("give me a sequence of whitespace separated words: ")
    ans = t.split()
    return ans
def rem_du(l):
    ans = []
    for i in l:
        if i not in ans:
            ans.append(i)
    return ans
a = txt_list()
b = rem_du(a)
c = sorted(b)
print(' '.join(c))