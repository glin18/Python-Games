from game_data import data
import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(logo)
current_score = 0
play = True
while play:
    A = random.choice(data)
    B = random.choice(data)
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if A['follower_count'] > B['follower_count']:
        answer = 'A'
    else:
        answer = 'B'
    if choice == answer:
        print(f"Correct! The answer was {answer}")
        current_score += 1
        print(f"Current Score: {current_score}")
    else:
        print("Sorry, that is wrong")
        print(f"Final Score: {current_score}")
        play = False
print("Thanks for playing!")