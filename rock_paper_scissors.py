import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    my_move = input("What is your move? To make a move, enter rock, paper, or scissors. To quit the game, enter quit. ")

    if my_move == "quit":
        break

    if my_move != "rock" and my_move != "paper" and my_move != "scissors":
        print("Your move isn't valid!")
    else:
        rand = random.randint(0, 2)

        opponent_move = ""
        if rand == 0:
            opponent_move = "rock"
        elif rand == 1:
            opponent_move = "paper"
        else:
            opponent_move = "scissors"
        print("Opponent move: " + str(opponent_move))

        if my_move == opponent_move:
            print("It's a tie!")
        elif (my_move == "rock" and opponent_move == "scissors") or (my_move == "scissors" and opponent_move == "paper") or (my_move == "paper" and opponent_move == "rock"):
            print("You won!")
        else:
            print("You lost!")
print("Thanks for playing Rock, Paper, Scissors!")