import random
choices = ["rock"," paper", "scissors"]

computer = random.choice(choices)
player= None

while player not in choices:
    player = input("rock,paper or scissors?:").lower()

if computer == player:
    print("computer:", computer)
    print("player", player)
    print("Tie")

elif player == "rock"
    if computer == "paper":
       print("computer:", computer)
       print("player", player)
       print("You lose!")
