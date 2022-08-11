#!/usr/bin/python3

import requests

AOIF_CHAR = "https://swapi.dev/api/people/"
def main():
    choice= input("Choose between 1 and 88 to select a starwars character!\n>" )
 
    resp = requests.get(AOIF_CHAR + choice).json()
   
    print("CHARACTER:", end= " ")
    print(f"{resp['name']}\n" if resp['name'] else f"{resp['aliases'][0]}\n")

if __name__ == "__main__":
    main()
  
