# A basic "for" loop to print a statement multiple times
for i in range(10):
    print("Hi, how are you?")

# The "range" function generates numbers from 0 to 9 (10 times).

# Using a "for" loop with a variable to print numbers and their multiples
answer = 0
for i in range(5):
    answer += i
    print("For I in range 5: answer =", answer)

# The loop adds numbers from 0 to 4 to the "answer" variable.

# Using a "for" loop with a variable to print numbers and their multiples
answer = 0
for i in range(5):
    answer += i
    print("For I in range 5: answer =", answer)

# The loop adds numbers from 0 to 4 to the "answer" variable.

# Simulating a doctor's clinic using a while loop
n = 1  # Initialize token number
c = 1  # Initialize a control variable

print("Hello everyone, we are starting.")

while c == 1:
    print(f"Token number {n} may please come in.")
    c = int(input("Continue? (0 to stop, 1 to continue): "))  # Convert to integer

    if c == 1:
        n += 1

print("Thank you, this is the end of our day.")