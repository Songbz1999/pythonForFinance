# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 02:14:23 2018

@author: Thinkpad
"""

#----------------------------------------#
#Question 5
#Level 1
#
#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

#----------------------------------------#

class func_string():
    def _init_(self):
        self.ans = ''
    def getString(self):
        self.ans = input ('give me a string: ')
    def printString(self):
        print (self.ans.upper())
        
a = func_string()
a.getString()
a.printString()
        