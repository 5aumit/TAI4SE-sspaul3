import random

computer_wins = 0
player_wins = 0

while True:
    print("")

    user_choice = input("Choose Rock, Paper or Scissors : ")
    user_choice = user_choice.lower()

    moves = ["rock","paper","scissors"]
    comp_choice = random.choice(moves)
    

    print("")

    if user_choice == "rock":
        if comp_choice == "rock":
            print("You chose rock. The computer chose rock. You tied.")

        elif comp_choice == "paper":
            print("You chose rock. The computer chose paper. You lose.")
            computer_wins = computer_wins + 1

        elif comp_choice == "scissors":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins = player_wins + 1

    elif user_choice == "paper":
        if comp_choice == "rock":
            print("You chose paper. The computer chose rock. You win.")
            player_wins = player_wins + 1

        elif comp_choice == "paper":
            print("You chose paper. The computer chose paper. You tied.")


        elif comp_choice == "scissors":
            print("You chose paper. The computer chose scissors. You lose.")
            computer_wins = computer_wins + 1

    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("You chose scissors. The computer chose rock. You lose.")
            computer_wins = computer_wins + 1

        elif comp_choice == "paper":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins = player_wins + 1

        elif comp_choice == "scissors":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(computer_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n) : ")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
