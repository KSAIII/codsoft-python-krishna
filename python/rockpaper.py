import random


user_score = 0
computer_score = 0


choices = ["rock", "paper", "scissors"]


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


while True:
    print("\nRock, Paper, Scissors Game")
    print("Choose one: rock, paper, scissors")
    user_choice = input("Your choice: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    
    if "win" in result:
        user_score += 1
    elif "win" in result:
        computer_score += 1
    
    print(f"User Score: {user_score}, Computer Score: {computer_score}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Final scores:")
        print(f"User Score: {user_score}, Computer Score: {computer_score}")
        break
