#!/bin/usr/python3

"""
The Caesar cipher is a shift cipher that uses addition(e) and subtraction(d)
to encrypt and decrypt letters.
"""
                                                            # every possible symbol that can be encrypted/decrypted:
                                                            # we can add numbers and punctuation marks to encrypt those
                                                            # symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
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
    print('Please enter the letter e or d.')
                                                            # let the user enter the key to use:
while True:                                                 # will keep asking for user to enter a valid 'key'
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
                                                            # Let the user enter the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('> ')                                       # Caesar cipher only works on uppercase letters:
message = message.upper()                                   # Stores the encrypted/decrypted form of the message:
translated = ''
                                                            # Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
                                                            # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)                          # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key                                 # Handle the wrap-around if num is larger than the length of
                                                            # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)                        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:                                                   # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol
                                                            # Display the encrypted/decrypted string to the screen:
print(translated)


