import random

# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Number%20Guessing
# ASCII Text
print('''

███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████  ██    ██ ███████ ███████ ███████ ██ ███    ██  ██████  
████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██       ██    ██ ██      ██      ██      ██ ████   ██ ██       
██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██   ███ ██    ██ █████   ███████ ███████ ██ ██ ██  ██ ██   ███ 
██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██    ██ ██    ██ ██           ██      ██ ██ ██  ██ ██ ██    ██ 
██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████   ██████  ███████ ███████ ███████ ██ ██   ████  ██████  
                                                                                                                          
''')
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts_remaining = 10
if difficulty == 'hard':
    attempts_remaining = 5
while attempts_remaining > 0:
    print(f"You have {attempts_remaining} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"Correct! You win! The answer was {number}")
        break
    if guess > number:
        print("Too high")
    if guess < number:
        print("Too low")
    attempts_remaining -= 1
    if attempts_remaining == 0:
        print(f"No attempts remaining. The answer was {number}")
    else:
        print("Guess Again")
print("Thanks for playing!")