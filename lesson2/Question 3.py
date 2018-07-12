# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:11:46 2018

@author: Thinkpad
"""

#----------------------------------------#
#Question 3
#Level 2
#
#Question:
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

#----------------------------------------#
def detec_ul():
    s = input ("give me a sentence: ")
    ans = {'up':0, 'down':0}
    for i in s:
        if i.isupper():
            ans['up'] += 1
        if i.islower():
            ans['down'] += 1
    return ans

a = detec_ul()
print ('UPPER CASE '+str(a['up']))            
print ('LOWER CASE '+str(a['down']))