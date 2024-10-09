import random
possible_actions = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(possible_actions)
    print(f"\nYou chose {user_choice}, computer chosen {computer_choice}.\n")
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers the rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Invalid input, Please enter rock, paper or scissors.")
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

