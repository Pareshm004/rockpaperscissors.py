import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None
while player not in choices:
    player = input("rock, paper or scissors?:")
if player == computer:
    print("player: ", player)
    print("computer: ", computer)
    print("Game Tied!!")
elif player == "rock":
    if computer == "scissor":
        print("player: ", player)
        print("computer: ", computer)
        print("You win!!")
    if computer == "paper":
        print("player: ", player)
        print("computer: ", computer)
        print("You lose and computer wins!!Better luck next time")
elif player == "paper":
    if computer == "rock":
        print("player: ", player)
        print("computer: ", computer)
        print("You win!!")
    if computer == "scissor":
        print("player: ", player)
        print("computer: ", computer)
        print("You lose and computer wins!!Better luck next time")
elif player == "scissor":
    if computer == "paper":
        print("player: ", player)
        print("computer: ", computer)
        print("You win!!")
    if computer == "rock":
        print("player: ", player)
        print("computer: ", computer)
        print("You lose and computer wins!!Better luck next time")
