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
left_right = input("You are at a crossroad. Which way do you want to go?\nType left or right: ").lower()

if left_right == "left":
    swim_wait = input("You reach a river where trout are swimming by.\nDo you swim or wait?:").lower()
    if swim_wait == "wait":
        door = input("You reach 3 different colored doors.\nDo you choose red, yellow, or blue?:").lower()
        if door == "yellow":
            print("You found the treasure! YOU WIN!")
        elif door == "red":
            print("You were burned by a fire. Game over :(")
        elif door == "blue":
            print("You were eaten by a beast. Game over :(")
        else:
            print("Game over :(")
    else:
        print("You were attacked by the trout. Game over :(")
else:
    print("You fell into a hole. Game over :(")
