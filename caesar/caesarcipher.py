#!/bin/usr/python3


"""
The Caesar cipher is a shift cipher that uses addition ('e') and subtraction ('d')
to encrypt and decrypt letters.
"""
                                                            # every symbol that can be encrypted/decrypted
                                                            # we can add numbers and punctuation marks to encrypt those
                                                            # symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('''The Caesar cipher encrypts letters by shifting them over by a 
key number. For example, a key of 2 means the letter A is
encrypted into C, the letter B encrypted into D, and so on.''')
print()
                                                            # user will enter if they are encrypting 'e' or decrypting 'd'
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
    maxKey = len(SYMBOLS) - 1                               # the {} is part of '.format()' this allows me to add more symbols
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ')
    if 0 <= int(response) and int(response) < len(SYMBOLS): # this is saying: 0<{input} and {input}<25 ('25' here can change if we add more symbols)
        key = int(response)                                 # if the above is true then user input will become the key
        break   
                                                            # let the user enter the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))              # the symbols are all uppercase, 'a' is different from 'A'
message= input('> ')                                        # cipher only works on uppercase letters.
message= message.upper()
newString= ""
for char in message:
    result= SYMBOLS.index(char.upper())
                                                            # encrypt/decrypt each symbol in the message                      
    if mode == 'encrypt':
        result= result + key
        if 0 <= result and result < len(SYMBOLS):
            newString += SYMBOLS[result]
        elif 0 <= result and result >= len(SYMBOLS):
            result= result - len(SYMBOLS)
            newString += SYMBOLS[result]
        
    elif mode == 'decrypt':
        result= result - key                                
        if 0 > result: 
            result= len(SYMBOLS) + result       
            newString += SYMBOLS[result]
            
                                                           # display the encrypted/decrypted string to the screen
print(newString)                                           # user can now copy it. 


