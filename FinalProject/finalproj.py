#!/bin/usr/python3

import crayons

def title():
   print(crayons.red('''
       ----HOUSE OF HORROR----
      =========================
'''))

title()            # displays our 'TITLE'

input()            # requires user to press 'enter'

health = 200.0     # Current Health (this is a float so division doesn't make an int)
maxHealth = 200    # Max Health
healthDashes = 20  # Max Displayed dashes

def danger_meter():
  dashConvert = int(maxHealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
  currentDashes = int(health/dashConvert)              # Convert health to dash count: 80/10 => 8 dashes
  remainingHealth = healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces

  healthDisplay = '-' * currentDashes                  # Convert dashes as a string:   "--------"
  remainingDisplay = ' ' * remainingHealth             # Convert spaces as a string: "            "
  percent = str(int((health/maxHealth)*100)) + "%"     # Get the percent as a whole number: 40%
  

  if percent > "79%" or percent == "100%":
      print(crayons.green("       |" + healthDisplay + remainingDisplay + "|"))     # Print out textbased healthbar to display depending on percentage (80 and up 'GREEN')
  elif percent > "39%":
      print(crayons.yellow("       |" + healthDisplay + remainingDisplay + "|"))    # Print out textbased healthbar to display depending on percentage (40 and up 'YELLOW')
  else:
      print(crayons.red("       |" + healthDisplay + remainingDisplay + "|"))       # Print out textbased healthbar to display (39 and below 'RED')

  print("                " + percent)                                               # Print the percent to display


danger_meter()      # displays our 'DANGER METER' aka Health

def instructions(): # intro with basic instructions!
    print('''
    You are an inspiring detective and psychic investigator.                        
    For weeks, you have experienced reoccurring nightmares that you sense might be important. 
    Your mission is to get to the bottom these visions. 
    You will decide how to move through the story. 
    The story is divided into 5 sections. 
    When presented with the two options you are to choose either ‘top’ or ‘bottom’. 
    Items that can be picked up by using ‘get {item name}' and will be highlighted the color 'CYAN'.
    Your health meter represents your precarious state, if it reaches ‘0’ game over.
    ''')
instructions()

def sec_1():
    input()
    print('''
    It's a Tuesday morning in late June and you wake up in a cold sweat. The nightmares came again last night. 
    Even though you are aspiring detective and psychic investigator, you haven't been able to make sense of the haunting dreams you've had these past few weeks. 
    In your dreams, you keep seeing the same spooky house. 
    You're still shivering under the covers when you hear the phone ring downstairs in your basement. 
    Where you have your combination office and research laboratory. You dash down to the lab to answer it. \" I need…. I need….\" 
    A weak voice says when you pick up the receiver.\" I need your hel-l-l-lp.\" You hear a loud click, and the phone goes dead. 
    But you were prepared: while the caller was talking, you activated your high-speed telephone tracing device. 
    It instantly displays the caller’s number: 555-7259. You call back the number right away, but there's no answer. 
    After consulting the tall stack of reverse phone books behind your desk. You are disappointed to learn the number is unlisted. 
    You sense that phone call is somehow related to your nightmares. Later, while at the Hedge Brook Police Station you returned a night scope you borrowed for a recent stakeout.
    You described the mysterious phone call and your recurring dreams to your friend, Sergeant Morrison. 
    \"That call does sound strange\", he says. \"We'll look into it.\"  
    \"And what about that house in your dreams?\" a voice says from the hallway. \"I wonder if you're dreaming about the Marsden house out in Hedge Brook Rd.\" 
    Detective Murphy sticks his mustache face into the room. 
    \"Modern house, ornate gate… That sounds like the Marsden place. Alright,\" says sergeant Morrison. 
    \"Strange things are reported to happen out there.\" Detective Murphy takes a puff on his pipe. \"That place is haunted,\" he says. 
    \"I know it sounds unprofessional, but I've had a file on the Marsden house for years, and I’m sure of it.\" 
    He waves a folder in front of your eyes, and a phone number written on the front jumps out at you. 
    It matches the one from your mysterious phone call. So, the call is related to your nightmares, Your psychic senses were right.
    ''')
    input()
    print(crayons.red('''    

                                                   ==CLUE 1==
                                          Get inside the Marsden house.'''))
    print('''
    

    Back at home, you grab a bottle of water. And you're Trusty Pocketknife preparing for a new investigation. 
    Half an hour later, you stand before the Marsden Residence, which appears exactly as it did in your nightmares. 
    The house’s futuristic look is a strange contrast to the antiquated appearance of the Stone wall and the wrought iron gate, 
    which is locked shut and wrapped in steel chains. Even though the air is balmy, 
    a chill travels down your spine, the gathering clouds on the horizon hint at the brewing summer thunderstorm.
    ''')

    answer1= input(crayons.magenta('''
    Do you want to search the wall for a way in?
    
    or 
    
    Do you climb the gate?
    
    '''))

sec_1()
