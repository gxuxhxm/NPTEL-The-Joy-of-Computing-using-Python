def play_game():
    while True:
        # Assign choices for players
        choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

        # Input choices and secret bit positions for Player One and Player Two
        num_one = int(input("Player One, enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))
        num_two = int(input("Player Two, enter your choice (0 for Paper, 1 for Rock, 2 for Scissors): "))
        bit_one = int(input("Player One, enter the secret bit position (0, 1, or 2): "))
        bit_two = int(input("Player Two, enter the secret bit position (0, 1, or 2): "))

        # Calculate P1 and P2 based on the secret bit positions
        p1 = (num_one >> bit_one) & 1
        p2 = (num_two >> bit_two) & 1

        # Compare choices to determine the winner
        if p1 == p2:
            print("It's a draw!")
        elif p1 == 0 and p2 == 2:
            print("Player One wins!")
        elif p1 == 2 and p2 == 0:
            print("Player Two wins!")
        elif p1 < p2:
            print("Player Two wins!")
        else:
            print("Player One wins!")

        play_again = input("Do you want to continue? (Enter 'y' for yes, 'n' for no): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()