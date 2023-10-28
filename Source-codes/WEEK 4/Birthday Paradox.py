import random

def is_shared_birthday(num_people):
    birthdays = [random.randint(1, 365) for _ in range(num_people)]
    return len(birthdays) != len(set(birthdays))

def birthday_paradox_simulation(num_simulations, num_people):
    shared_count = 0
    for _ in range(num_simulations):
        if is_shared_birthday(num_people):
            shared_count += 1
    return shared_count / num_simulations

num_simulations = 10000
num_people = 23  # You can change the group size

probability = birthday_paradox_simulation(num_simulations, num_people)
print(f"Probability of shared birthdays in a group of {num_people} people: {probability:.2f}")

