import random

print("Rules are: \n "
      "Rock vs Paper --> Paper wins \n"
      "Rock vs Scissor --> Rock wins \n"
      "Paper vs Scissor --> Scissor wins \n")


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
            else:
                print("Rock wins ...")

        elif choice == "Paper":
            if comp_choice == "Scissor":
                print("Scissor wins ...")
            else:
                print("Paper wins ...")

        elif choice == "Scissor":
            if comp_choice == "Rock":
                print("Rock wins ...")
            else:
                print("Scissor wins ...")   

             
    
    # Asking if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
    
print("Thanks for playing")