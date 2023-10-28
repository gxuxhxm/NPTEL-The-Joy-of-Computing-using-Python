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