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