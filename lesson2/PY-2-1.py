# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:29:27 2018

@author: Thinkpad
"""

'''
1. Write a program that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:

My name is Steven

Then I would see the string:

Steven is name My

shown back to me.
'''
def get_sent():
    l = input("give me a long string containing multiple words:")
    word = l.split()
    ans = word[::-1]
    return ans

a = get_sent()
print(' '.join(a))