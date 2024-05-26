  # Rock, Paper, Scissors game :D !! WARNING its syntax sensitive and im to lazy to fix rn/sleep deprived :p 

 # Importing the neccessary packages 
import random;
 
 # makes the game replayable :)
while True:
 # User input.
 user_action = input("Enter a choice (Rock, paper, Scissors): ")
 # Computer input.
 possible_actions = ["rock", "paper", "Scissors"]
 computer_action = random.choice(possible_actions)
 # Displays user & computer choice 
 print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
 # Determines a winner 
 if user_action == computer_action:
    print(f"Both players selected {user_action} its a tie!")
 elif user_action == "rock":
    if computer_action == "Scissors":
        print("Rock smashes scissors! You Win!")
    else:
        print("Paper Covers rock, you lose :(")
 elif user_action == "paper":
    if computer_action == "rock": 
        print("Paper covers rock! You win!")
    else: 
        print("Scissors cuts paper! you lose :(")
 elif user_action == "Scissors":
    if computer_action == "paper":
        print("scissors cuts paper! You win!")
    else:
        print("Rock smashes Scissors! You lose :(")

 # Prompts the user to decide if they want to play again. 
 play_again = input("play again? (y,n): ")
 if play_again.lower() != "y":
    break  