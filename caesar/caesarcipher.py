#!/bin/usr/python3

"""
This Caesar cipher is a shift cipher that uses addition ('e') and subtraction ('d')
to encrypt and decrypt letters.
RYAN SILVA | RS.RYAN2781@GMAIL.COM
"""
                                                                # every symbol that can be encrypted/decrypted
                                                                # we can add numbers and punctuation marks to encrypt those
                                                                # symbols as well.
SYMBOLS = '$A:BC?D<E;F,G>H%IJ -KL^M|90&8N.O*P\Q!R7S=T/56U4V+W@X3Y_Z#12'

print('''
This Caesar cipher encrypts letters by shifting them over by a 
key number. For example, a key of 2 means the letter A is encrypted into C, 
the letter B encrypted into D, and so on.
''')
print()

def cipher():                                                   # user will enter if they are encrypting 'e' or decrypting 'd'
    while True:                                                 # keep asking until the user enters 'e' or 'd'.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()                          # the '.lower()' ensures it will be lowercase regardless of user input
        if response.startswith('e'):                            # the '.startswith makes it so the user can input the word 'encrypt'
            mode = 'encrypt'                                    # downside: they can use any word that stats with 'e' to encrypt
            break                                               # same goes for decrypt.
        elif response.startswith('d'):
            mode = 'decrypt'
            break                                               # 'break' allows you top leave the 'while' loop 
        print('Please enter the letter e or d.')                # '- 1' because SYMBOLS start at the position '0'    
                                                                # let the user enter the key to use:
    while True:                                                 # will keep asking for user to enter a valid 'key'
        maxKey = len(SYMBOLS) - 1                               # the {} is part of '.format()' this allows me to add/remove more symbols
        print('Please enter the key (1 to {}) to use.'.format(maxKey))
        response = input('> ')
        if 0 < int(response) and int(response) < len(SYMBOLS):  # this is saying: 0<{input} and {input}<25 ('25' here can change if we add more symbols)
            key = int(response)                                 # if the above is true then user input will become the key
            break                                               # break out of the while loop
                                                                # let the user enter the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(mode))              # the symbols are all uppercase, 'a' is different from 'A'
    message= input('> ')                                        # cipher only works on uppercase letters.
    message= message.upper()
    newString= ""                                               # newString is the displayed new message after encryption/decryption
    for char in message:                                        # char stands for 'character' in ASCII
        result= SYMBOLS.index(char.upper())                     # .upper() makes everything uppercase| index shows position
                                                                                     
        if mode == 'encrypt':                                   # this is what happens if selected encryption
            result= result + key                                # adding to move right iot to land on our new character we want displayed
            if 0 <= result and result < len(SYMBOLS):           # if when adding the 'positional value' of a character with the 'key' given by the user is less than  
                newString += SYMBOLS[result]                    # the total length of SYMBOLS then no further action required.
            elif 0 <= result and result >= len(SYMBOLS):        # if when adding the 'positional value' of a character with the 'key' given by the user is greater than or equal
                result= result - len(SYMBOLS)                   # to the total length of SYMBOLS, then we must subtract the length of SYMBOLS from the result.
                newString += SYMBOLS[result]                    # giving us the appearance of looping
                                                                # newString is a new variable| Symbols[results] is 
        elif mode == 'decrypt':                                 # this is what happens if selected decryption
            result= result - key                                # subtracting to move left iot to land on our new character we want displayed
            if 0 <= result:                                     # if when subtracting the 'key' from the 'positional value' of a character (result) given from the user
                newString += SYMBOLS[result]                    # is greater than or equal to '0' then no further action required.
            elif 0 > result:                                    # if when subtracting the 'key' from the 'positional value' of a character (result) given from the user
                result= len(SYMBOLS) + result                   # is less than '0' then we must add the length of SYMBOLS to the result, giving us the appearance of looping 
                newString += SYMBOLS[result]                    
                                                                # prints newString
                                                                # displaying the encrypted/decrypted string to the screen
    print(newString)                                            # user can now copy it. 

if __name__ == "__main__":
    cipher()
