#We use this to let the computer make random choices
import random 

#RockPaperScissors Class
#Principle Single Responsibility Principle and this class only handles the game
class RockPaperScissors:
    def __init__(self):
        #List of possible choices
        #Simple list of strings for game options
        self.choices = ["rock", "paper", "scissors"]
    # Principle SoC in which it Handles user input, computer choice, and result logic
    def play(self):
        #Ask the user for their choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        # Randomly let the computer pick a choice
        computer_choice = random.choice(self.choices)
        #Show both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        #Game Logi
        #Principl DRY in whihch use one set of conditions to check who wins
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")

#Main Code to Start the Game
# here is used the principle keep it simple stupid
 #Create a game object
game = RockPaperScissors() 
game.play()  