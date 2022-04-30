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
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
rock_paper_scissors = ["rock", "paper", "scissors"]
computer_choice = rock_paper_scissors[random.randint(0, 2)]
your_choice = rock_paper_scissors[choice]
print(f"You chose {your_choice} and the computer chose {computer_choice}")

if your_choice == "rock":
    print(rock)
    if computer_choice == "paper":
        print(paper)
        print("You lose")
    if computer_choice == "scissors":
        print(scissors)
        print("You win")
    if computer_choice == "rock":
        print(rock)
        print("It is a draw")
elif your_choice == "paper":
    print(paper)
    if computer_choice == "paper":
        print(paper)
        print("It is a draw")
    if computer_choice == "scissors":
        print(scissors)
        print("You lose")
    if computer_choice == "rock":
        print(rock)
        print("You win")
elif your_choice == "scissors":
    print(scissors)
    if computer_choice == "paper":
        print(paper)
        print("You win")
    if computer_choice == "scissors":
        print(scissors)
        print("It is a draw")
    if computer_choice == "rock":
        print(rock)
        print("You lose")

print("Thanks for playing!")


