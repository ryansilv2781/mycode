#!/usr/bin/python3


def showInstructions():
   print('''
RPG Game
========
Commands:
  go [north,east,south,west]
  get [item name]
  find the amazing items and escape the hotel... 
  beware of the monster...
''')

def showStatus():
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Lobby' : {
                  'north' : 'Hallway',
                  'south' : 'Courtyard',
                  'east'  : 'Garage',
                  'west'  : 'Fountain',
                  'item'  : 'key',
                },

            'Vents' : {
                  'west'  : 'Boiler Room',
                  'south' : 'Libray',
                  'item'  : 'monster',
                },
            'Courtyard' : {
                  'north' : 'Lobby',
                  'east'  : 'Alley',
               },
            'Alley' : {                                                 
                  'north' : 'Garage',                                       
                  'west'  : 'Courtyard',
                  'item'  : 'cookie crumbs',                              
               },
            'Garage' : { 
                  'west'  : 'Lobby',
                  'south' : 'Alley', 
               },
            'Fountain' : {
                  'north' : 'Garden',
                  'east'  : 'Lobby',
               },
            'Garden' : {
                  'north' : 'Dinning hall',
                  'south' : 'Fountain',
                  'east'  : 'Hallway',
                  'item'  : 'cookie crumbs',
               },
            'Hallway' : { 
                  'north' : 'Boiler Room',
                  'south' : 'Lobby',
                  'east'  : 'Library',
                  'west'  : 'Garden',
                  'item'  : 'cookie crumbs',
               },   
            'Boiler Room' : {
                  'south' : 'Hallway',
                  'east'  : 'Vents',
                  'item'  : 'cookie crumbs',
               },    
            'Library' : {
                  'north' : 'Vents',
                  'west'  : 'Hallway',
                  'item'  : 'potion',
               },
            'Dinning hall' : {
                  'south' : 'Garden',
                  'item'  : 'cookie',
            }
         }

#start the player in the Lobby
currentRoom = 'Lobby'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Courtyard' and 'key' in inventory and 'cookie' in inventory and 'potion' in inventory:
    print('You escaped the hotel with the ultra rare key and magic potion... YOU WIN! enjoy that cookie!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('you never EVER go into the vents.... the monster got you... GAME OVER!')
    break
