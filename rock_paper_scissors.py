import random

play_again = "y"
count = 0
wins = 0
com_wins = 0

while play_again == "y":
    count = 0
    wins = 0
    com_wins = 0

    while count < 3:
        choices = ["rock", "paper", "scissors"]
        shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
        computer = random.choice(choices)
        player = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()
        # or use this: player = shortcuts.get(player, player)
        if player in shortcuts:
            player = shortcuts[player]
        if player not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors or (r/p/s)")
            continue
        else:
            print(f"computer: {computer}")
            if player == computer:
                print("This round is a tie!")
            elif (
                (player == "rock" and computer == "scissors")
                or (player == "paper" and computer == "rock")
                or (player == "scissors" and computer == "paper")
            ):
                print("You win this round!")
                wins += 1
            else:
                print("Computer wins this round!")
                com_wins += 1

            count += 1

    if wins > com_wins:
        print("You won the game!")
    elif com_wins > wins:
        print("Computer won the game!")
    else:
        print("The game is a tie!")

    while True:
        play_again = input("Play again? (y/n)").strip().lower()
        if play_again in ["y", "n"]:
            break
        else:
            print("Please enter 'y' or 'n'.")
