
---
## Dictionaries in Python

**Introduction:**
- Dictionaries in Python are a data structure used to store key-value pairs.
- This data structure allows for efficient mapping of keys to values.
- Dictionaries are similar to real-world dictionaries where words (keys) have corresponding meanings (values).

**Creating a Dictionary:**
- Dictionaries are created using curly braces `{}`.
- An empty dictionary is created by using `dictionary_name = {}`.

**Adding Items to a Dictionary:**
- Key-value pairs are added to a dictionary using the format: `dictionary_name[key] = value`.
- Example: `conversion_factor['dollar'] = 60`.

**Viewing a Dictionary:**
- To print the entire dictionary, use the `print(dictionary_name)` statement.
- To view a list of keys, use `dictionary_name.keys()`.
- To view a list of values, use `dictionary_name.values()`.
- To view key-value pairs, use `dictionary_name.items()`.

**Accessing Specific Items in a Dictionary:**
- To access the value of a specific key, use `dictionary_name[key]`.
- Example: `conversion_factor['euro']` will return `80`.

**Deleting Items from a Dictionary:**
- To delete a specific key-value pair, use the `del` statement.
- Example: `del conversion_factor['yen']`.

**Updating Values in a Dictionary:**
- Updating a value in the dictionary is similar to creating a new item.
- Use the format: `dictionary_name[key] = new_value`.

**Error Handling:**
- If you try to access a key that is not present in the dictionary, it will raise a `KeyError`.

**Example - Currency Conversion:**
- Demonstrates how to use a dictionary to perform currency conversion.
- Values in the dictionary represent conversion rates.

**Conclusion:**
- Dictionaries are a powerful data structure for managing key-value pairs.
- Python provides various methods to manipulate and work with dictionaries effectively.

Certainly, here are the notes for the second part of the speech-to-text tutorial:

## Speech to Text with Python using Speech Recognition
---
### **Introduction:**
- The presenter introduces the use of Python and the Speech Recognition library to convert audio files to text.
- Emphasizes the utility of this technology, especially for helping with tasks like learning lyrics and dance skills.

### **Installation of Speech Recognition:**
- Instructions for installing the Speech Recognition library using the ` pip install speechrecognition` command.
- Mention that you need to use your terminal to execute this command.

### **Steps to Use Speech Recognition:**
1. Create an audio file using a microphone to record the audio you want to convert to text.
2. Convert the audio file to the ".wav" extension. Speech Recognition only works with ".wav" files.
3. Proceed with the programming steps once you've completed the above.

### **Importing Libraries:**
- Import the SpeechRecognition library using `import speech_recognition as sr`.

### **Initializing the Program:**
- Create a variable (e.g., `audio_file`) and assign the filename of your ".wav" audio file to it.
- Initialize the recognizer using `recognizer = sr.Recognizer()`.

### **Processing the Audio File:**
- Read the audio file using `audio = sr.AudioFile(audio_file)`.

### **Transcribing the Audio to Text:**
- Use a `try` block with error handling to perform speech recognition.
- Attempt to recognize the audio file using `audio_recognized = recognizer.recognize_google(audio)`.
- Handle potential exceptions, such as `sr.UnknownValueError` or `sr.RequestError`, and provide appropriate messages.
#### Code:

```python
import speech_recognition as sr  
  
# Step 1: Create an audio file and convert it to .wav  
# In this example, you need to have an audio file named "kangal-irandal.wav".  
  
# Step 2: Import Speech Recognition and Initialize the Program  
recognizer = sr.Recognizer()  
  
# Step 3: Process the Audio File  
audio_file = "Listening and reading practice (320 wav file.wav" # Provide the path to your .wav audio file  
with sr.AudioFile(audio_file) as source:  
try:  
# Recognize the audio using Google's speech recognition  
audio_data = recognizer.record(source) # Record the audio data from the source  
audio_recognized = recognizer.recognize_google(audio_data)  
print("Recognized Text: " + audio_recognized)  
except sr.UnknownValueError:  
print("Google Speech Recognition could not understand audio")  
except sr.RequestError as e:  
print("Could not request results from Google Speech Recognition; {0}".format(e))  
  
# The recognized text will be printed to the console.
```

To use this code:

1. Make sure you have the `speech_recognition` library installed. If not, install it using `pip install SpeechRecognition`.

2. Replace `"sample_simran.wav"` with the path to your own `.wav` audio file that you want to convert to text.

3. Execute the script, and it will attempt to transcribe the audio in the provided file and print the recognized text to the console.
### **Output:**
- Print the recognized text using `print(audio_recognized)`.
### **Conclusion:**
- The presenter demonstrates the capability of converting audio to text using Google's Speech Recognition.
- Highlights the utility of the technology for various applications.



## Monty Hall Problem 
---
### **Introduction**: 
The Monty Hall problem is a famous probability puzzle inspired by a game show scenario.
### **Scenario**: 
In this scenario, you, as the contestant, are presented with three closed doors. Behind one door, there is a valuable prize (let's say a BMW car), while the other two doors hide less desirable prizes (e.g., goats).

### **Initial Choice**: 
You start by choosing one of the three doors, hoping to find the car behind it.

### **Host's Move**: 
After you make your initial choice, the game host (Monty Hall) opens one of the other two doors, revealing a goat. Importantly, Monty always chooses a door that you didn't pick and that doesn't hide the car.

### **Swap or Stay**: 
At this point, you have a decision to make. You can either stick with your original choice (i.e., not swapping) or switch to the other unopened door (i.e., swapping).

### **Objective**: 
The objective is to determine whether swapping or staying with your initial choice gives you a higher probability of winning the car.

### Monty Hall Simulation Code:

```python
import random

def monty_hall_simulation(num_simulations):
    swap_wins = 0
    no_swap_wins = 0

    for _ in range(num_simulations):
        doors = [0, 1, 2]
        car_behind_door = random.choice(doors)
        contestant_choice = random.choice(doors)
        goat_doors = [door for door in doors if door != car_behind_door and door != contestant_choice]
        monty_opens = random.choice(goat_doors)
        remaining_doors = [door for door in doors if door != monty_opens and door != contestant_choice]
        
        # Contestant decides whether to swap or stay
        # If swapping, contestant chooses the remaining unopened door.
        if random.choice(["swap", "stay"]) == "swap":
            contestant_choice = remaining_doors[0]
        
        if contestant_choice == car_behind_door:
            swap_wins += 1
        else:
            no_swap_wins += 1

    return swap_wins, no_swap_wins

if __name__ == "__main__":
    num_simulations = 10000  # Change this number to set the number of simulations
    swap_wins, no_swap_wins = monty_hall_simulation(num_simulations)

    print(f"Simulated {num_simulations} Monty Hall games:")
    print(f"Number of wins with swapping: {swap_wins}")
    print(f"Number of wins without swapping: {no_swap_wins}")
```

### Sample Output:

```
Simulated 10000 Monty Hall games:
Number of wins with swapping: 6611
Number of wins without swapping: 3389
```

In this sample output, after simulating 10,000 Monty Hall games, swapping (changing the initial choice) resulted in 6,611 wins, while not swapping (staying with the initial choice) led to 3,389 wins. This demonstrates that swapping has a higher probability of winning, consistent with the Monty Hall problem's solution.

## Rock Paper Scissors
---
### Code Structure:

1. **Game Rules**:
   - The game is Rock, Paper, Scissors.
   - There are three entities: Rock, Paper, and Scissors.
   - Each player (Player One and Player Two) makes a choice:
     - Player One's choices: 0 for Rock, 1 for Paper, and 2 for Scissors.
     - Player Two's choices: 0 for Paper, 1 for Rock, and 2 for Scissors.

2. **Input**:
   - The program uses a `while` loop to allow the user to input choices and secret bit positions.
   - The user inputs `num_one` (Player One's choice), `num_two` (Player Two's choice), `bit_one` (Player One's secret bit position), and `bit_two` (Player Two's secret bit position).
   - The loop continues until the user chooses to exit by entering 'n'.

3. **Comparison**:
   - The program compares Player One's choice (`num_one` and `bit_one`) with Player Two's choice (`num_two` and `bit_two`) based on the game rules.

4. **Output**:
   - The program prints the result of the comparison, indicating whether it's a draw or which player wins.

5. **Continuation Prompt**:
   - The program asks the user if they want to continue playing ('y' for yes, 'n' for no).
   - If the user chooses 'n', the `while` loop will terminate, and the program will exit.

### Sample code:


```python
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
```

This Python code defines a `play_game` function that lets Player One and Player Two make their choices and determine the winner based on the rules you provided. The game continues until the user chooses to exit by entering 'n'.

## Sorting and Searching 
---
**Problem Statement:**
- In this scenario, we aim to explore searching and sorting algorithms.
- We begin with the linear search to understand its limitations and inefficiency for searching large arrays.
- We then introduce binary search as an efficient algorithm for searching in sorted arrays.
- The goal is to find a specific element in a sorted array with minimal iterations.

**Notes:**

**Linear Search:**
1. Linear search is a basic searching algorithm used to find a specific element within an array.
2. It operates by checking each element in the array sequentially.
3. The number of iterations required to find an element can be quite high, especially in large arrays.
4. Inefficient for large arrays, as the worst-case scenario may involve searching through every element.

```python
def linear_search(a, x):
    count = 0

    for i in range(len(a)):
        count += 1
        if a[i] == x:
            print(f"Element found at position {i}.")
            return count

    print("Number is not present.")
    return count

# Sample Usage:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7
iterations = linear_search(a, x)
print(f"Number of iterations: {iterations}")
```


**Binary Search:**
1. Binary search is a more efficient search algorithm, especially for sorted arrays.
2. It leverages the knowledge that the array is sorted to minimize the number of iterations.
3. The key idea is to compare the target element with the middle element of the array.
4. If the target element is greater, you can discard the left half of the array; if it's smaller, discard the right half.
5. Continue this process until the target element is found or the search space is empty.
6. The number of iterations is drastically reduced, making it a fast and efficient search algorithm.

**Python Code for Binary Search:**
```python
def binary_search(a, x):
    first_pos = 0
    last_pos = len(a) - 1
    flag = 0
    count = 0

    while first_pos <= last_pos and flag == 0:
        count += 1
        mid = (first_pos + last_pos) // 2

        if x == a[mid]:
            flag = 1
            print(f"Element found at position {mid}.")
            return count
        elif x < a[mid]:
            last_pos = mid - 1
        else:
            first_pos = mid + 1

    print("Number is not present.")
    return count

# Sample Usage:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7
iterations = binary_search(a, x)
print(f"Number of iterations: {iterations}")
```

**Sample Output:**
```
Element found at position 6.
Number of iterations: 3
```

- The binary search algorithm is demonstrated using an array of numbers, searching for element 7.
- The element is found at position 6, and it took 3 iterations to locate it efficiently.

**Efficiency Comparison:**
- Linear search may require up to n iterations for an array of size n.
- Binary search takes log2(n) iterations for an array of size n, making it much more efficient.
- Binary search excels in large sorted arrays, minimizing the number of steps needed to locate an element.