#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
# need to inport!!!!!!!!!!!!
import random

def main():
    num= random.randint(1,100)
    
    rounds= 0
    guess=""
    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100:\n>")
        # input returns userinput as 'strings'
        # guess= "60"

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit(): # checks to see if user typed a number
            guess= int(guess)
        else:
            continue # error prevention

        if guess > num:
            print("Too high!")
            # 'rounds + 1' wrong way due to 'rounds' not saving new value
            rounds= rounds + 1

        # only use one 'if'
        elif guess < num:
            print("Too low!")
            # rounds + 1
            rounds += 1 # short hand!

        else:
            print("Correct!")
        
        if rounds == 5:
            print("that was five guesses! better luck next time! the correct number was", num)


main()

