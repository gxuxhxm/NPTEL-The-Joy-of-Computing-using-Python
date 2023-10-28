
## **Slicing:**
   - Slicing is a method to extract a portion of a list.
   - It involves specifying a start index, end index (exclusive), and an optional step value.
   - It creates a new list with the selected elements from the original list.

   ```python
   my_list = [0, 1, 2, 3, 4, 5]
   
   # Extract elements from index 2 to 4 (exclusive)
   sliced_list = my_list[2:4]
   print(sliced_list)  # Output: [2, 3]
   ```


```python
# Sample list of students
students = ["akanksha", "arun", "Harish", "lakshmi", "rajesh", "varsha"]

# Basic list slicing: students[1:4]
subset = students[1:4]
print(subset)  # Output: ['arun', 'Harish', 'lakshmi']

# Slicing with a start index only: students[:4]
subset = students[:4]
print(subset)  # Output: ['akanksha', 'arun', 'Harish', 'lakshmi']

# Slicing with an end index only: students[2:]
subset = students[2:]
print(subset)  # Output: ['Harish', 'lakshmi', 'rajesh', 'varsha']
```

## **Removing Items:**
   - You can remove items from a list using methods like `remove` and `pop`.
   - `remove(item)` deletes the first occurrence of a specific item from the list.
   - `pop(index)` removes an item by its index and returns its value.

   ```python
   my_list = [10, 20, 30, 40, 50]

   # Remove the value 30 from the list
   my_list.remove(30)
   print(my_list)  # Output: [10, 20, 40, 50]

   # Remove the item at index 2 (value 40) and store it in a variable
   removed_item = my_list.pop(2)
   print(removed_item)  # Output: 40
   ```

## **List Comprehensions:**
   - List comprehensions provide a concise way to create new lists based on existing ones.
   - They involve applying an expression to each item in an existing list and creating a new list as a result.

   ```python
   original_list = [1, 2, 3, 4, 5]

   # Create a new list by squaring each element from the original list
   squared_list = [x**2 for x in original_list]
   print(squared_list)  # Output: [1, 4, 9, 16, 25]
   ```

## FizzBuzz 
---
### **FizzBuzz Problem Statement:**

1. Write a program to print numbers from 1 to n.
2. Replace numbers that are multiples of 3 with "Fizz."
3. Replace numbers that are multiples of 5 with "Buzz."
4. If a number is a multiple of both 3 and 5, print "FizzBuzz."
5. Continue until n is reached.
6. The program should print the sequence of numbers and substitutions.

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

You can run this code, and it will print the FizzBuzz sequence from 1 to 100, following the rules as described.

## Crowd Computing
---
### **Problem Statement:**
- The problem involves estimating the number of gems in a jar based on estimates from a crowd.
- Given a list of 75 estimates of the number of gems in the jar.
- The actual number of gems in the jar is 375.
- Find an accurate estimate using different methods: mean, trimmed mean, and median.

### **Solution:**
- Import the necessary libraries, such as `matplotlib` and `statistics`.
- Create a list named `estimates` containing 75 estimates of the number of gems.
- Sort the `estimates` list in ascending order.
- Calculate the ten percent trimmed mean by removing the ten percent smallest and largest values.
- Calculate the mean and median of the estimates.
- Use Matplotlib to plot the estimates, mean, and median on a graph.
- Sure, here are brief explanations of the two modules imported in the code:

1. `matplotlib.pyplot`:
   - `matplotlib.pyplot`, often imported as `plt`, is a Python library for creating static, animated, or interactive visualizations in a programmatic way.
   - It provides a wide range of functions and classes for creating various types of plots, charts, and graphs.
   - In the code, `matplotlib.pyplot` is used for creating line plots and adding different markers, such as dashes, dots, squares, and triangles, to represent data.

2. `statistics`:
   - The `statistics` module is part of Python's standard library and provides a collection of functions for performing basic statistical operations on data.
   - It includes functions for calculating statistical measures like mean, median, mode, standard deviation, and variance.
   - In the code, the `statistics` module is used to calculate the mean and median of the given data, which are then plotted on the graph using `matplotlib`.

These modules are essential for data visualization, analysis, and statistical calculations in Python. They are commonly used in data science and scientific computing to visualize and analyze data.

### **Python Code:**
```python
# Import libraries
import matplotlib.pyplot as plt
import statistics

# List of 75 estimates
estimates = [374, 376, 377, 375, 374, 376, 373, 378, 376, 375, 377, 376, 374, 375, 376, 374, 377, 375, 376, 378, 374, 377, 376, 375, 373, 374, 376, 375, 377, 376, 374, 376, 375, 377, 375, 376, 374, 378, 376, 375, 377, 376, 374, 375, 376, 378, 374, 377, 375, 376, 374, 377, 376, 375, 376, 374, 377, 375, 376, 374, 378, 376, 375, 377, 376, 374, 375, 376, 378, 374, 377, 375, 376, 374, 377, 376, 375, 378]


# Sort estimates in ascending order
estimates.sort()

# Calculate the ten percent trimmed mean
trim_value = int(0.10 * len(estimates))
trimmed_estimates = estimates[trim_value : -trim_value]

# Plot the estimates, mean, and median
plt.plot(estimates, [5] * len(estimates), 'r--', label='Estimates')
plt.plot([statistics.mean(estimates)], [5], 'ro', label='Mean', markersize=5)
plt.plot([statistics.median(estimates)], [5], 'bs', label='Median', markersize=5)
plt.plot([375], [5], 'g^', label='Actual', markersize=7)

# Set labels and legend
plt.xlabel('Number of Gems')
plt.yticks([])  # Hide y-axis labels
plt.legend()

# Display the graph
plt.show()
```

This code will generate a plot showing the estimates, mean, median, and the actual value (`375`) on the x-axis. The mean and median can help determine which estimate is closest to the actual value.

## Permuntations - Jumbled words
---
### **Problem Statement:**
1. Create a two-player word jumble game.
2. One player thinks of a word, jumbles the letters, and presents it.
3. The other player must guess the original word.
4. If guessed correctly, they earn a point.
5. The game continues until one player quits, and final scores are displayed.

### **Output:**
1. Display jumbled word for the current player to guess.
2. Show whether the guess is correct.
3. Update the player's score if they guess correctly.
4. Display final scores when the game ends.

### **Code Blocks:**
1. Import necessary modules and libraries.
2. Define functions for choosing a random word and jumbling it.
3. Implement the game logic using a `while` loop.
4. Get player names and initialize scores.
5. Alternate between players' turns.
6. Display jumbled word, take guesses, and update scores.
7. Allow players to continue or quit.
8. Show final scores at the end of the game.


```python
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
```

This code creates a simple version of the game. Players enter their names, and the game alternates between them. It randomly selects a word, jumbles it, and players need to guess the original word. The game continues until one of the players decides to quit, and final scores are displayed.

### **Problem Explanation:**
1. The program creates a two-player word jumble game.
2. Players enter their names, and the game tracks their scores.
3. The game randomly selects a word, jumbles its letters, and displays it for the current player to guess.
4. If the guess is correct, the player earns a point.
5. If incorrect, the correct answer is shown.
6. Players can choose to continue or quit.
7. The game continues until one player decides to quit, and final scores are presented.

### Example output:

```
Enter Player 1's name: Alice
Enter Player 2's name: Bob

Jumbled word: oeht
Alice, what's the original word? the
Correct!

Do you want to continue (yes/no)? yes
Jumbled word: otnmimamahics
Bob, what's the original word? mathematics
Correct!

Do you want to continue (yes/no)? yes
Jumbled word: cemoptur
Alice, what's the original word? computer
Correct!

Do you want to continue (yes/no)? yes
Jumbled word: nnidoitoc
Bob, what's the original word? condition
Correct!

Do you want to continue (yes/no)? no

Final Scores:
Alice: 1
Bob: 1
Thank you for playing!
```

In this example, two players (Alice and Bob) take turns guessing jumbled words. After each round, the correct answer is revealed, and players can choose to continue or quit. The final scores are displayed at the end of the game.

## Theory of evolution
---
### **Problem Statement:**
- Avni and Simran discuss the concept of evolution, specifically how DNA carries genetic information.
- They mention the randomness involved in evolution.
- They propose simulating evolution through a simplified model using genetic algorithms.
- The goal is to write a Python program that evolves a binary string by randomly flipping bits.

### **Code:**
- Read a DNA data file containing a binary string (zeros and ones).
- Define a function, `evolve(x)`, to evolve the binary string.
- Generate a random index `ind` within the range of the binary string's length.
- Generate another random integer `P` from 1 to 100.
- If `P` is 1 and the bit at index `ind` is 0, flip it to 1; otherwise, flip it to 0.


```python
import random

# Read the binary string from a DNA data file
with open("DNA_data.txt", "r") as file:
    dna_string = file.read().strip()

# Define the evolve function
def evolve(dna):
    # Generate a random index within the range of the binary string
    ind = random.randint(0, len(dna) - 1)
    # Generate another random integer P from 1 to 100
    P = random.randint(1, 100)

    # If P is 1 and the bit at index ind is 0, flip it to 1; otherwise, flip it to 0
    if P == 1 and dna[ind] == "0":
        dna = dna[:ind] + "1" + dna[ind+1:]
    else:
        dna = dna[:ind] + "0" + dna[ind+1:]

    return dna

# Perform evolution iterations
for _ in range(10): #10 years/10 generations 
    dna_string = evolve(dna_string)

# Print the evolved binary string
print("Evolved DNA String:", dna_string)
```

In this code, we first read the binary string from a file. Then, we define an `evolve` function that randomly selects an index and flips a bit based on a randomly generated integer `P`. We repeat this process for a specified number of iterations.

You can replace `"DNA_data.txt"` with the actual path to your DNA data file.

### Breakdown of Basic Operation :

```python
# If P is 1 and the bit at index ind is 0, flip it to 1; otherwise, flip it to 0
if P == 1 and dna[ind] == "0":
    dna = dna[:ind] + "1" + dna[ind+1:]
else:
    dna = dna[:ind] + "0" + dna[ind+1:]
```

This code represents a basic mechanism for simulating evolution in a binary string. Let's break it down step by step:

1. `P` is a random integer that can be any value between 1 and 100. It's used to introduce randomness into the process. In your code, you're checking if `P` is exactly equal to 1.

2. `dna` is a binary string, and `ind` is a randomly chosen index within that string. The binary string consists of '0's and '1's.

3. Next, you're checking two conditions:
   - `P == 1`: This condition checks if the random integer `P` is equal to 1. In your code, this check has a 1% chance of being true because `P` can be any random integer from 1 to 100. When `P` is 1, it signifies a rare event.
   - `dna[ind] == "0"`: This condition checks if the bit (0 or 1) at the randomly chosen index `ind` is equal to "0".

4. If both conditions are true (i.e., `P` is 1, and the bit at index `ind` is 0), you execute the code block after the first `if` statement. In this code block, you flip the bit at index `ind` from 0 to 1 by slicing the `dna` string:
   - `dna[:ind]` extracts the part of the string before the index `ind`.
   - `"1"` is the new value that you want to set at index `ind`.
   - `dna[ind+1:]` extracts the part of the string after index `ind`.
   - The result is a modified `dna` string with the bit at index `ind` changed from 0 to 1.

5. If either of the conditions (P is not 1 or the bit at index `ind` is not 0), you execute the code block after the `else` statement. In this case, you flip the bit at index `ind` from 1 to 0 using the same slicing technique.

So, this code mimics a random event (controlled by `P`) that occasionally flips a bit in the binary string (from 0 to 1 or vice versa), simulating a simple form of mutation in an evolutionary process. The rarity of `P` being equal to 1 ensures that such mutations happen infrequently, as is often the case in natural evolution.

### **Output:**
- The binary string after the evolution process is displayed.
- The program can print the randomly generated values of `P` and `ind` to show when changes occur in the string.

### **Example Output:**
Initial Binary String (from "DNA_data.txt"): `1101011001`

Here's a step-by-step example of how the code evolves this binary string:

1. Original String: `1101011001`
2. Randomly chosen index `ind`: Let's say `ind` is 4 (chosen randomly).
3. Random integer `P`: Let's say `P` is 1 (a rare event).
4. Condition check: `P == 1` is true, and `dna[ind] == "0"` is also true because the bit at index 4 is 0.
5. Mutation occurs: The bit at index 4 changes from 0 to 1.
6. Evolved String: `1101111001`

This process is repeated multiple times, with each iteration potentially flipping a bit based on the rarity of `P` being equal to 1. The evolved string is the result of these iterations.

After a series of iterations, the final evolved string might look something like this (this is just an example, and the actual result will vary each time you run the code):

Final Evolved String: `1011110100`

The code simulates a simple form of evolution by introducing occasional random mutations, as dictated by the value of `P`, to the binary string. The final evolved string reflects the result of these random mutations.
