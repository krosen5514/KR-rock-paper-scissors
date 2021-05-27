# game.py

import random
import os
import dotenv

dotenv.load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME")

#trying to use .env on name:
#import os
#from .env import load_dotenv
#PLAYER_NAME = os.getenv("USER_NAME", default="Player One")

print("-------------------")
print("Welcome,", PLAYER_NAME, ", to my Rock-Paper-Scissors game!")
print("-------------------")

player_choice = input("Please choose either: 'rock', 'paper', 'scissors': ")

print("You chose:", player_choice)

#validate the input such that only if it is one of the expected values
#...will we continue with the rest of the program
#...otherwise we will stop the program before it tries to do anything else
#...and we'll ask the user to run the program again

if (player_choice =="rock") or (player_choice =="paper") or (player_choice =="scissors"):
    print("Valid. Keep Going!")
else: 
    print("OOPS, Invalid input. Please try again.")
    exit()
print("-------------------")

valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("The computer chose:", computer_choice)

#Rock beats Scissors
#Paper beats Rock
#Scissors beats Paper
#Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"
print("-------------------")
if player_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE")
    elif computer_choice == "paper":
        print("Sorry, you lost this round...")
    elif computer_choice == "scissors":
        print("YOU WON, nice job!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON, nice job! CONGRATS!")
    elif computer_choice == "paper":
        print("IT'S A TIE")
    elif computer_choice == "scissors":
        print("Sorry, you lost this round...")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("Sorry, you lost this round...")
    elif computer_choice == "paper":
        print("YOU WON, nice job!")
    elif computer_choice == "scissors":
        print("IT'S A TIE")

print("-------------------")

print("Thanks for playing! Please play again.")