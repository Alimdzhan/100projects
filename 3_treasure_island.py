print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("You are at a cross road. Where do you want to go?\n Type 'left or 'right'\n")
if left_right == "left":
    swim_wait = input("You've come to a lake. There is an island in the middle of the lake\n Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if swim_wait == "wait":
        door = input("Which door do you want to choose?\n Type 'blue', 'red' or 'yellow'\n")
        if door == "red":
            print("You are a winner!!! Congratulations!")
        elif door == "blue":
            print("You were eaten by beasts! Game over!")
        elif door == "yellow":
            print("You were eaten by beasts! Game over!")
        else:
            print("You've write wrong word")
    else:
        print("You were attacked by trout! Game over!")
else:
    print("Game over!")