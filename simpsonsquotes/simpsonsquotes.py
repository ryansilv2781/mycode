#!/usr/bin/env python3
"""Quotes from The Simpsons!"""

import urllib.request
import json
import requests

# defining the url
SIM= "https://thesimpsonsquoteapi.glitch.me/quotes"
SIMCH= "https://thesimpsonsquoteapi.glitch.me/quotes?character="
def main():
    simpsonquote = urllib.request.urlopen(SIM)
    simpson = simpsonquote.read()
    simquote = json.loads(simpson.decode('utf-8'))
    
    # showed index (this was '0')
    # for idx, word in enumerate(simquote):
    #    print(idx, word)

    # getting random quote or by character        
    # print(simquote)
    print('-------------------------')
    print("THE SIMPSONS QUOTE: \n")
    print('\"'+simquote[0]['quote']+'\"')
    print('         -',simquote[0]['character']) 
    print('-------------------------')
    
    input() # user can press 'enter'
    choice= input("Do want a \'random\' qoute or would you rather search for one \'by name\'?\n").lower().title()
    print('-------------------------') 
    while choice == 'Random':
        main()

    if choice == 'By Name':             # .lower().title() converts 'bY nAmE' >> 'By Name' 
        usrsel= input("Who would you like to hear a quote from?\n").lower().title()
        print('-------------------------')
        selquote = requests.get(SIMCH + usrsel).json()
        # print(f"{resp}")                                  testing..................
        # sim1 = urllib.request.urlopen(SIMCH + usr_select) testing..................
        # simselect = sim1.read()                           testing..................
        # selquote = json.loads(simselect.decode('utf-8'))  testing..................
        print("HERE'S THE THE QUOTE YOU ASKED FOR: \n")
        print('\"'+selquote[0]['quote']+'\"')
        print('         -',selquote[0]['character'])
        print('-------------------------')
        input("Hope it was a funny quote... try this one...")
        main()
    else:
        answer= input("Did you mean \'random\'?\n")

        while answer == 'y':
            main()
        else:
            print("ADIOS!")
            print('------------------------')
            exit() 

if __name__ == "__main__":
    main()   
