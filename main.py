import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

print("player: ", player)
print("computer: ", computer)

if player == computer:
    print("Game Tied!!")
elif player == "rock":
    if computer == "scissors":
        print("You win!!")
    elif computer == "paper":
        print("You lose and computer wins!! Better luck next time")
elif player == "paper":
    if computer == "rock":
        print("You win!!")
    elif computer == "scissors":
        print("You lose and computer wins!! Better luck next time")
elif player == "scissors":
    if computer == "paper":
        print("You win!!")
    elif computer == "rock":
        print("You lose and computer wins!! Better luck next time")
