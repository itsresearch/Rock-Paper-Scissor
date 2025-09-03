import random

print("Rules are: \n "
      "Rock vs Paper --> Paper wins \n"
      "Rock vs Scissor --> Rock wins \n"
      "Paper vs Scissor --> Scissor wins \n")

player_score = 0
computer_score = 0

while True:
    print("Enter your choice: Rock, Paper, or Scissor:")
    choice = input("Enter your choice: ").capitalize()
    
    while choice not in ("Rock", "Paper", "Scissor"):
        print("Invalid choice. Please choose Rock, Paper, or Scissor.")
        choice = input("Enter your choice: ").capitalize()
    
    print("You choose:", choice)
    print("Now it's the computer's turn...")
    
    comp_choice_num = random.randint(1, 3)
    if comp_choice_num == 1:
        comp_choice = "Rock"
    elif comp_choice_num == 2:
        comp_choice = "Paper"
    elif comp_choice_num == 3:
        comp_choice = "Scissor"

    print("Computer choose:", comp_choice)

    # Checking draw
    if choice == comp_choice:
        print("It's a draw ...")
    else:
        # Determining the winner
        if choice == "Rock":
            if comp_choice == "Paper":
                print("Paper wins ...")
                computer_score += 1
            else:
                print("Rock wins ...")
                player_score += 1

        elif choice == "Paper":
            if comp_choice == "Scissor":
                print("Scissor wins ...")
                computer_score += 1
            else:
                print("Paper wins ...")
                player_score += 1

        elif choice == "Scissor":
            if comp_choice == "Rock":
                print("Rock wins ...")
                computer_score += 1
            else:
                print("Scissor wins ...")   
                player_score += 1

    print(f"\nScore -> You: {player_score} | Computer: {computer_score}")
    
    # Asking if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("\nFinal Score: ")
print(f"\nYou: {player_score} | Computer: {computer_score}")
if player_score > computer_score:
    print("Congratulatons you are the overall winner")
elif player_score < computer_score:
    print("Computer wins")
else:
    print("It's a draw.")

print("Thanks for playing")