## **Substitution Cipher**
---
### **Concept: Substitution Cipher**
- A substitution cipher is a basic encryption method that replaces each letter in the plaintext with another letter or symbol.
- It relies on a fixed replacement rule and a secret key for encryption and decryption.
- The key idea is to map each character in the plaintext to a corresponding character in the ciphertext.

### **Key Points from the Discussion:**
- Romeo and Juliet illustrate the substitution cipher concept as a way to keep messages secret.
- In this method, letters are shifted by a fixed number of positions in the alphabet.
- The secret key is the number of positions to shift the letters.
- The transcript highlights that shifting can be easily broken if someone knows the technique.
- A middleman can decrypt the message by systematically trying all possible shifts.
- Substitution ciphers are vulnerable to attack, often referred to as the Caesar cipher.
- The transcript introduces the idea that English text has distinct statistical properties, allowing even complex substitution ciphers to be recognized through frequency analysis.
- The conclusion is that modern encryption techniques are needed for secure communication, as substitution ciphers are not suitable for safeguarding sensitive information.
- The discussion emphasizes that cryptography is about creating and breaking codes and securing information from unauthorized access.

### Code

```python
#week 6  
def substitution_cipher(text, shift):
    encrypted_text = ""
    for c in text:
        if c.isalpha():
            offset = ord('A') if c.isupper() else ord('a')
            new_letter = chr(((ord(c) - offset + shift) % 26) + offset)
            encrypted_text += new_letter
        else:
            encrypted_text += c
    return encrypted_text

text = "Hello, World!"
shift = 3  # Define the shift value
encrypted_text = substitution_cipher(text, shift)

print("Original Text:", text)
print("Encrypted Text:", encrypted_text)

```

Sample Output:
```
Original Text: Hello, World! 123
Encrypted Text: Khoor, Zruog! 123
```

This code defines a `substitution_cipher` function that takes an input text and a shift value. It then shifts each alphabetic character by the specified amount and leaves non-alphabetic characters unchanged. The sample output demonstrates the encryption of the input text using a shift of 3.

## Tic Tac Toe
---
**Problem Statement:**
Create a Tic Tac Toe game in Python where two players take turns marking a 3x3 grid, aiming to get three of their symbols in a row, column, or diagonal. The game should handle turns, validate input, and identify a win or a draw.

**Code:**
1. **Initialize the Game:**
   - Create a 3x3 board to represent the Tic Tac Toe grid.
   - Define player symbols as 'X' and 'O'.
   - Initialize a variable to keep track of the current player.


```python
# Initialize the Tic Tac Toe board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the current state of the board
def display_board():
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("---------")

# Function to check if a player has won
def check_won(symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

# Main game loop
current_player = "X"
turns = 0

while turns < 9:
    display_board()
    move = input(f"Player {current_player}, enter your move (row and column): ").split(',')
    
    if len(move) != 2:
        print("Invalid input. Please enter row and column (e.g., '1,2').")
        continue
    
    row, col = map(int, move)
    
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid input. Row and column values must be between 1 and 3.")
        continue
    
    if board[row - 1][col - 1] != " ":
        print("Invalid move. The cell is already occupied.")
        continue
    
    board[row - 1][col - 1] = current_player
    turns += 1
    
    if check_won(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break
    
    current_player = "X" if current_player == "O" else "O"
else:
    display_board()
    print("It's a draw!")

```

This code initializes the game, displays the board, allows two players to take turns, and checks for a win or a draw. You can run this code in a Python environment to play the game.

2. **Display the Board:**
   - Create a function to display the current state of the board.

3. **Play the Game:**
   - Implement a loop to continue the game until a player wins or the game ends in a draw.
   - Inside the loop, display the current state of the board.
   - Prompt the current player to enter their move (row and column).
   - Check if the move is valid (within the grid and the cell is empty).
   - Update the board with the player's symbol.
   - Check if the current player has won:
     - Check rows, columns, and diagonals for three of the same symbols.
     - If a win is detected, declare the current player as the winner and end the game.
   - If there are no valid moves left (the board is full), declare the game as a draw and end it.

4. **Player Switching:**
   - Implement a mechanism to switch players' turns (from 'X' to 'O' and vice versa).

5. **Sample Output:**
   - Start with an empty board like this:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```
   - Players take turns entering their moves (e.g., "1" for the top-left cell).
   - The game continues until a player wins or it's a draw.
   - If a win occurs, display a message declaring the winner (e.g., "Player X wins!").
   - If the game ends in a draw, display a message stating it's a draw.

## Recursion
---
### Introduction to Recursion**
- Recursion is a programming technique where a function calls itself to solve a problem.
- It involves breaking a problem into smaller, similar subproblems.
- Base case(s) are the conditions that determine when the recursion should stop.
- Recursive case(s) are the conditions that allow the function to call itself.
- Recursion requires careful handling of base cases to avoid infinite loops.

### Factorial Using Recursion**
- Factorial is the product of all positive integers from 1 to n.
- The base case for the factorial is when n is 0, in which case the result is 1.
- In the recursive case, the factorial of n is calculated by multiplying n with the factorial of (n-1).
```python
# Recursive factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
- Output examples:
  - `factorial(5)` returns 120.
  - `factorial(0)` returns 1.

### Fibonacci Sequence Using Recursion**
- The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.
- The base cases for the Fibonacci sequence are the 0th and 1st Fibonacci numbers, which are 0 and 1, respectively.
- In the recursive case, the nth Fibonacci number is calculated by summing the (n-1)th 
  and (n-2)nd Fibonacci numbers.
```python
# Recursive Fibonacci function
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
- Output examples:
  - `fibonacci(4)` returns 3.
  - `fibonacci(10)` returns 55.
### Binary Search Using Recursion
- Binary search is a search algorithm used to find an element in a sorted list.
- The base case for binary search is when there's only one element left in the list.
- In binary search, you compare the middle element of the list with the target element.
- If the middle element is the target, you're done. Otherwise, you search in the left or right half of the list.
```python
# Recursive binary search function
def binary_search(arr, x, start, end):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, x, mid + 1, end)
        else:
            return binary_search(arr, x, start, mid - 1)
    else:
        return -1
```
- Output examples:
  - `binary_search([20, 40, 45, 60, 70, 90], 80, 0, 5)` returns "80 not found."
  - `binary_search([20, 40, 45, 60, 70, 90], 90, 0, 5)` returns "90 is found at position 5."

### Overview of Binary Search (No specific code)**
- Provides an overview of binary search, which is used to find an element in a sorted list.
- Explains that binary search is based on comparing the target element with the middle element of the list.

### Fibonacci Sequence Using Recursion**
- Reiterates the concept of the Fibonacci sequence and explains how to calculate the nth Fibonacci number using recursion.
```python
# Recursive Fibonacci function
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
- Output example:
  - `fibonacci(10)` returns 55.

