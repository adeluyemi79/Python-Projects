print ("welcome to Treasure Island,")
print("your mission is to find the treasure,")
choice1 = input("you\'re at a cossroad, whre do you want to go?\n Type 'left' or' right'. "). lower ()
if choice1 == "left":
    choice2 = input ("you\'ve come to a lake. There ia an island in the middle of thr lake. Type 'wait' to wait for a boat. Type 'swim' to swim accross.\n "). lower ()
    if choice2 == "wait":
        choice3 = input (" you arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. which color do you choose?\n"). lower ()
    if choice3 == "red":
        print ("it's a room full of fire . Game over.") 
    elif choice3 == "yellow":
        print ("you found the treasure! you win! ")
    elif choice3 == "blue":
        print ("you enter a room of beasts. Game over.")
    else:
        print ("you choose a door that doesn't exist. Game over.")
    
        

