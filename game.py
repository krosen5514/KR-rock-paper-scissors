# game.py

import random

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

player_choice = input("Please choose eith: 'rock', 'paper', 'scissors': ")

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
if (player_choice =="rock") and (computer_choice == "scissors"):
    print("Computer Wins")
if (player_choice =="scissors") and (computer_choice == "rock"):
    print("Computer Wins")
if (player_choice =="rock") and (computer_choice == "paper"):
    print("Computer Wins")

if (computer_choice =="rock") and (player_choice == "scissors"):
    print("You Win!")
if (computer_choice =="scissors") and (player_choice == "rock"):
    print("You Win!")
if (computer_choice =="rock") and (player_choice == "paper"):
    print("You Win!")

if (computer_choice =="rock") and (player_choice == "rock"):
    print("It's a tie")
if (computer_choice =="scissors") and (player_choice == "scissors"):
    print("It's a tie")
if (computer_choice =="paper") and (player_choice == "paper"):
    print("It's a tie")

print("-------------------")

print("Thanks for playing. Please play again.")