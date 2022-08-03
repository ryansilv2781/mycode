#!/usr/bin/env python3

# request number (1-50) from user
ranking = int(input("Please pick a number 1-50 to select a movie!"))

message = "the movie you have selected is ranked number "+str(ranking)+" out of 50!"

# have to subtract 1 so it matches up with the list that was made
ranking = ranking - 1

# Top 50 movie lists 
movienamelist = ["Avatar","Avengers: Endgame","Titanic","Star Wars: The Force Awakens","Avengers: Infinity War","Spider-Man: No Way Home","Jurassic World","The Lion King","The Avengers","Furious 7","Frozen II","Avengers: Age of Ultron","Black Panther","Harry Potter and the Deathly Hallows – Part 2","Star Wars: The Last Jedi","Top Gun: Maverick film currently playing","Jurassic World: Fallen Kingdom","Frozen","Beauty and the Beast","Incredibles 2","The Fate of the Furious","Iron Man 3","Minions","Captain America: Civil War","Aquaman","The Lord of the Rings: The Return of the King","Spider-Man: Far From Home","Captain Marvel","Transformers: Dark of the Moon","Skyfall","Transformers: Age of Extinction","The Dark Knight Rises","Joker","Star Wars: The Rise of Skywalker","Toy Story 4","Toy Story 3","Pirates of the Caribbean: Dead Man's Chest","Rogue One: A Star Wars Story","Aladdin","Pirates of the Caribbean: On Stranger Tides","Despicable Me 3","Jurassic Park","Finding Dory","Star Wars: Episode I – The Phantom Menace","Alice in Wonderland","Zootopia","The Hobbit: An Unexpected Journey","Harry Potter and the Philosopher's Stone","The Dark Knight","Harry Potter and the Deathly Hallows – Part 1"]

# titanic
if(int(ranking) == 2):
    print("the movie's name is "+movienamelist[ranking]+" grab some tissues, this is a sad one!")
# frozen
elif(int(ranking) == 17):
    print("Kids will love this one! "+movienamelist[ranking]+", grab some snacks!")
# every other movie
else:        
    print("the movie name is "+movienamelist[ranking]+" garb your popcorn and enjoy!")

