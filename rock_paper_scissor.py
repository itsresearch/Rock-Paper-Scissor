# rock paper scissor game.

import random

print("========= Rock Paper Scissors Game ==========")

choices = ["rock", "paper", "scissors"]
while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer = random.choice(choices)
    print("Computer chose: ", computer)

    # logic of the game.
    if user == computer:
        print("Its a tie.")
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win.")
    else:
        print("You loose.")

    # play again.
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing.")
        break


# AND = Both/All condition True =====> True. else false.
# True and False ======> False.
# True and True=======> True
# False and False=====> False
# True and(False and True)========> False

# OR = Any condition True======> True.
# True or False =====> True
# False or True ======> True
# False or (true or false) =====> True
# false and (true or False)=====> false

