import random

# Function to check ladders and adjust the player's score
def check_ladder(points):
    ladder = {8: 26, 21: 82, 43: 77, 50: 91, 54: 93, 62: 96, 66: 87, 80: 100}
    if points in ladder:
        print("You found a ladder!")
        return ladder[points]
    return points

# Function to check snakes and adjust the player's score
def check_snake(points):
    snake = {44: 22, 46: 5, 48: 9, 52: 11, 55: 7, 59: 17, 64: 36, 69: 33, 73: 1, 83: 19, 92: 51, 95: 24, 98: 28}
    if points in snake:
        print("Oops! You encountered a snake!")
        return snake[points]
    return points

# Function to check if the player has reached the endpoint
def reached_end(points, end_point):
    if points == end_point:
        return True
    return False

# Main part of the code
end_point = 100

# Input player names
player_one_name = input("Enter Player 1's name: ")
player_two_name = input("Enter Player 2's name: ")

# Initialize player points
player_one_score = 0
player_two_score = 0

# Initialize the turn
turn = 0

# Game loop to play the Snake and Ladder game
while True:
    if turn % 2 == 0:
        current_player_name = player_one_name
        current_player_score = player_one_score
    else:
        current_player_name = player_two_name
        current_player_score = player_two_score

    choice = input(f"{current_player_name}, do you want to continue (yes/no)? ")

    if choice.lower() == "no":
        print("Game Over! Final Scores:")
        print(f"{player_one_name}: {player_one_score}")
        print(f"{player_two_name}: {player_two_score}")
        break

    dice = random.randint(1, 6)
    current_player_score += dice
    print(f"{current_player_name} rolled a {dice}. {current_player_name}'s score is now {current_player_score}.")

    current_player_score = check_ladder(current_player_score)
    current_player_score = check_snake(current_player_score)

    if current_player_score > end_point:
        current_player_score = end_point

    if reached_end(current_player_score, end_point):
        print(f"{current_player_name} has reached the endpoint and won the game!")
        break

    print("----------------------------------------------------")

print("Thank you for playing! Have a great day.")