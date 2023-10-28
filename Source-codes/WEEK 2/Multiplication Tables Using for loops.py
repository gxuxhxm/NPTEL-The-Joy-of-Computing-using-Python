# Displaying multiplication tables using "for" loops
t = int(input("Enter the table number: "))

for i in range(1, 11):  # Loop through numbers from 1 to 10
    result = t * i
    print(f"{t} x {i} = {result}")