import random

options = ["r", "p", "s"]
player = "Player"
cpu = "CPU"
r = "r"
p = "p"
s = "s"

print("Welcome to game")


def answers(player, cpu):
    if player == "r" and cpu == "s":
        print('Player Wins, Rock beats Scisscors')
    elif player == "s" and cpu == "p":
        print("Player Wins, Scissors cut Paper")
    elif player == "p" and cpu == "r":
        print("Player Wins, Paper covers Rock")
    elif cpu == "r" and player == "s":
        print("CPU Wins, Rock beats Sissors")
    elif cpu == "s" and player == "p":
        print("CPU Wins, Scissorc cut Paper")
    elif cpu == "p" and player == "r":
        print("CPU Wins, Paper covers Rock")
    else:
        print("It's a Tie!")

while True:
    cpu_choice = random.choice(options)
    cwins = 0
    pwins = 0
    answer = input("Choose 'r', 'p', or 's': ")
    if answer in options:
        answers(answer, cpu_choice)
    break






