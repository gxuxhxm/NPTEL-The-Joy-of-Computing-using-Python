def check_collatz(number):
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        iterations += 1
    print(f'Number 1 achieved after {iterations} iterations.')

# Example usage:
check_collatz(12)
check_collatz(20)
check_collatz(64)
