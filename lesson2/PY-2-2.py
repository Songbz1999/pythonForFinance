# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:37:10 2018

@author: Thinkpad
"""

'''
2. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random

def game():
    time = 0 
    ans = random.randint(1, 9)
    while True:
        time += 1
        cmd = input ('Guess a number between 1 and 9, type exit to quit: ')
        if cmd == 'quit':
            break
        elif int(cmd) == ans:
            print('congratulations！')
            break
        elif int(cmd) < ans:
            print('Too small! ')
        else :
            print('Too big! ')
    print('the answer is ' + str(ans) + ', you have use ' + str(time) + ' times')
    return

game()
