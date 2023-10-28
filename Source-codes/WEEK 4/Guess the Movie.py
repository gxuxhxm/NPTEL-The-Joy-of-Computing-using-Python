import random

def create_question(movie_name):
    question = ""
    for char in movie_name:
        if char == ' ':
            question += ' '
        else:
            question += '*'
    return question

def unlock_letter(movie_name, question, letter):
    output = ""
    for i in range(len(movie_name)):
        if movie_name[i] == letter:
            output += letter
        else:
            output += question[i]
    return output

def play_game():
    players = [input("Player one, enter your name: "), input("Player two, enter your name: ")]
    scores = [0, 0]
    movies = ["movie1", "movie2", "movie3", "movie4", "movie5", "movie6", "movie7", "movie8", "movie9", "movie10"] #add your own example movie names

    while True:
        for i in range(2):
            print(f"{players[i]}'s turn:")
            movie = random.choice(movies)
            question = create_question(movie)
            print(question)

            while '*' in question:
                letter = input("Guess a letter: ")
                if letter in movie:
                    print("Correct!")
                    question = unlock_letter(movie, question, letter)
                else:
                    print("Letter not found.")
                print(question)

            scores[i] += 1
            print(f"{players[i]} guessed the movie: {movie}")
            print(f"{players[i]}'s score is {scores[i]}")

        choice = input("Continue the game (1) or quit (0)? ")
        if choice == '0':
            break

    print(f"Game Over!\n{players[0]}'s score: {scores[0]}\n{players[1]}'s score: {scores[1]}")

play_game()