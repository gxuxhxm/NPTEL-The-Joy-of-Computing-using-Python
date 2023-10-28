import random
import matplotlib.pyplot as plt

# User input
bet = int(input("Enter your bet from 1 to 10: "))

# Account initialization
account = 0

# Simulation loop for one week (30 days)
x = []  # Days
y = []  # Account balances

for day in range(30):
    # Simulate a game round
    lucky_draw = random.randint(1, 10)

    if bet == lucky_draw:
        account += 900  # You win 900 rupees
    else:
        account -= 100  # You lose 100 rupees

    x.append(day + 1)
    y.append(account)

# Data collection

# Visualization
plt.plot(x, y)
plt.xlabel("Days")
plt.ylabel("Account Balance")
plt.title("Lottery Simulation - Profit or Loss")
plt.show()