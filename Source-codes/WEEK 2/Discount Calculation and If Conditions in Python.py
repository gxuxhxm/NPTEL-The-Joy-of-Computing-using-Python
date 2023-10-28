# Input the cost of the item
cost = input("What is the cost? ")

# Convert the input (which is a string) to an integer
d = int(cost)

# Calculate the discounted price (10% discount)
discounted_price = 0.9 * d

# Print the discounted price
print("The cost after a 10% discount is:", discounted_price)


# Input the user's choice
choice = input("Please enter your choice: ")

# Convert the input (which is a string) to an integer
d = int(choice)

# Use an if statement to check the value of the choice
if d == 1:
    print("You entered the number one.")
elif d == 2:
    print("You entered the number two.")
elif d == 3:
    print("You entered the number three.")
else:
    print("You entered an unrecognized number.")