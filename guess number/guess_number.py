import random

def user_number_guess(computer_num):
    prompt = "enter your guess (1 - 99):"
    num_guesses = 0
    number = 0
    #use while loop here
    
    while number != computer_num:
        number = int(input(prompt))
        num_guesses += 1
        
        # if...
        if number < computer_num:
            print("too low")
        elif number > computer_num:
                print("too high")
        else:
            print(f"correct! number of guess:(num_guessess)")
        
def main():
    user_number_guess(random.randrange(1,100))
    
main()