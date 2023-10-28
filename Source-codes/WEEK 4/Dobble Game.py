import string
import random

# Step 1: Set up Symbols
symbols = list(string.ascii_letters)

# Step 2: Create Cards
pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)

# Step 3: Choose a Common Symbol
same_symbol = random.choice(symbols)
symbols.remove(same_symbol)

# Step 4: Assign Symbols to the Cards
card1 = [None] * 5
card2 = [None] * 5

if pos1 == pos2:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol

    alphabet1 = random.choice(symbols)
    symbols.remove(alphabet1)
    alphabet2 = random.choice(symbols)
    symbols.remove(alphabet2)

    card1[pos2] = alphabet1
    card2[pos1] = alphabet2

# Step 5: Check for Remaining Positions
i = 0
while i < 5:
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)

        card1[i] = alphabet1
        card2[i] = alphabet2
    i += 1

# Step 6: Player Input
ch = input("Spot the common symbol: ")

# Step 7: Check for Correct Answer
if ch == same_symbol:
    print("Right!")
else:
    print("Wrong!")

# Example Output:
# (Assuming the common symbol is 'A' and player inputs 'A')
# Output: Spot the common symbol: A
#         Right!