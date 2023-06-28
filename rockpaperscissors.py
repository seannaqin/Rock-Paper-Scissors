import random

choices = ["rock", "paper", "scissors"]

while True:
    comp = random.choice(choices)

    player = ""
    while player not in choices:
        print()
        player = input("rock, paper, or scissors? ").lower()

    print()
    print("Player: " + player)
    print("Computer: " + comp)

    if player == comp:
        print("It's a tie!")
    elif (player == "rock" and comp == "paper") \
        or (player == "paper" and comp == "scissors") \
        or (player == "scissors" and comp == "rock"):
            print("You lose!")
    else:
        print("You win!")
    print()

    if input("Would you like to play again? (y/n) ").lower() != "y":
        break
    