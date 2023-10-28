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