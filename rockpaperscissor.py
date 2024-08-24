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

player_choice = input("Rock,Paper,Scissor(0/1/2) Choose!\n")
choices = [rock,paper,scissors]
print(f"You have picked {choices[int(player_choice)]}")#ubah int karena keluarny string
compu_choice = random.randint(0,2)
print(f"The Computer chose {choices[int(compu_choice)]}")
print(compu_choice)

if int(player_choice) == 0:
    if compu_choice == 0:
        print("Tie")
    elif compu_choice ==1:
        print("You Lose")
    elif compu_choice ==2:
        print("You Won")


if int(player_choice) == 1:
    if compu_choice == 0:
        print("You won")
    elif compu_choice ==1:
        print("Tie")
    elif compu_choice ==2:
        print("You Lose")

if int(player_choice) == 2:
    if compu_choice == 0:
        print("You Lose")
    elif compu_choice ==1:
        print("You Won")
    elif compu_choice ==2:
        print("Tie")