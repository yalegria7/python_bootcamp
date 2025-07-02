import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]

player_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

print("Rock, Paper, Scissors... Shoot!!")
if player_choice >= 0 and player_choice <=2:
    print(game_options[player_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_options[computer_choice])

if player_choice == 0 and computer_choice == 2:
    print("You win :D")
elif player_choice == 2 and computer_choice == 0:
    print("You lose :(")
elif player_choice < computer_choice:
    print("You lose :(")
elif player_choice > computer_choice:
    print("You win :D")
elif player_choice == computer_choice:
    print("Draw! Try again!")
