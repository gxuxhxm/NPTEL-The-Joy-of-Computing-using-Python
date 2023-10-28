import random

# Function to choose a random word from a list
def choose_word():
    word_list = ["rainbow", "computer", "science", "programming", "mathematics", "player", "condition", "reverse", "water", "boat"]
    return random.choice(word_list)

# Function to jumble the letters of a word
def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

# Function to play the game
def play_game():
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    player1_score = 0
    player2_score = 0

    while True:
        picked_word = choose_word()
        jumbled = jumble_word(picked_word)
        print(f"Jumbled word: {jumbled}")

        if random.randint(0, 1) == 0:
            current_player = player1_name
        else:
            current_player = player2_name

        guess = input(f"{current_player}, what's the original word? ").lower()

        if guess == picked_word:
            print("Correct!")
            if current_player == player1_name:
                player1_score += 1
            else:
                player2_score += 1
        else:
            print(f"Wrong! The correct word is: {picked_word}")

        play_again = input("Do you want to continue (yes/no)? ").lower()
        if play_again != "yes":
            break

    print(f"Final Scores:\n{player1_name}: {player1_score}\n{player2_name}: {player2_score}")
    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()