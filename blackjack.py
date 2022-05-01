logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

print(logo)
deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

while play == 'y':
    user_hand = [random.choice(deck), random.choice(deck)]
    computer_hand = [random.choice(deck), random.choice(deck)]
    user_scores = []
    computer_scores = []
    for card in user_hand:
        if card == 'J' or card == 'Q' or card == 'K':
            user_scores.append(10)
        elif card == 'A':
            user_scores.append(11)
        else:
            user_scores.append(card)

    for card in computer_hand:
        if card == 'J' or card == 'Q' or card == 'K':
            computer_scores.append(10)
        elif card == 'A':
            computer_scores.append(11)
        else:
            computer_scores.append(card)

    user_score = sum(user_scores)
    computer_score = sum(computer_scores)

    print(
        f"Your Hand: {user_hand[0]} , {user_hand[1]} Score: {user_score}\nOpponent's Hand: {computer_hand[0]} , {computer_hand[1]} Score: {computer_score}")

    if user_score == 21:
        print("You have a blackjack! You win!")
        play = input("Do you want to play again? Type 'y' or 'n': ")
        if play == 'y':
            continue
        else:
            break
    elif computer_score == 21:
        print("Your opponent has a blackjack! You lose!")
        play = input("Do you want to play again? Type 'y' or 'n': ")
        if play == 'y':
            continue
        else:
            break
    another_card = input("Would you like another card? Type 'y' or 'n': ")


    def convert(s):
        new = ""
        for element in s:
            new += str(element)
        return new


    while another_card == 'y':
        user_new_card = random.choice(deck)
        user_hand.append(user_new_card)
        if user_new_card == 'J' or user_new_card == 'Q' or user_new_card == 'K':
            user_scores.append(10)
        elif user_new_card == 'A':
            if sum(user_scores) + 11 > 21:
                user_scores.append(1)
            else:
                user_scores.append(11)
        else:
            user_scores.append(user_new_card)
        user_score = sum(user_scores)
        print(
            f"Your Hand: {user_hand} Score: {user_score}\nOpponent's Hand: {computer_hand} Score: {computer_score}")
        if user_score > 21:
            print("Bust!! You lose!")
            break
        another_card = input("Do you want another card? Type 'y' or 'n'")

    while computer_score < 17:
        computer_new_card = random.choice(deck)
        computer_hand.append(computer_new_card)
        if computer_new_card == 'J' or computer_new_card == 'Q' or computer_new_card == 'K':
            computer_scores.append(10)
        elif computer_new_card == 'A':
            if sum(computer_scores) + 11 > 21:
                computer_scores.append(1)
            else:
                computer_scores.append(11)
        else:
            computer_scores.append(computer_new_card)
        computer_score = sum(computer_scores)

    if user_score <= 21:
        print(
            f"Your Hand: {user_hand} Score: {user_score}\nOpponent's Hand: {computer_hand} Score: {computer_score}")
        if computer_score <= 21:
            if user_score > computer_score:
                print("You win!")
            elif computer_score > user_score:
                print("You lose!")
            elif computer_score == user_score:
                print("Tie!")
        else:
            print("Computer busts! You win!")
    play = input("Do you want to play again? Type 'y' or 'n': ")

print("Thanks for playing!")
