# game.py

print("Rock, Paper, Scissors, Shoot!")

player_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("The player chose:", player_choice)

#validate the input such that only if it is one of the expected values
#...will we continue with the rest of the program
#...otherwise we will stop the program before it tries to do anything else
#...and we'll ask the user to run the program again

if (player_choice =="rock") or (player_choice =="paper") or (player_choice =="scissors"):
    print("Valid. Keep Going")
else: 
    print("OOPS, Invalid input. Please try again.")
    exit()

print("This is the end of our game. Please play again.")