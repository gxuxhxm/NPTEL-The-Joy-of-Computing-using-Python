def binary_search(a, x):
    first_pos = 0
    last_pos = len(a) - 1
    flag = 0
    count = 0

    while first_pos <= last_pos and flag == 0:
        count += 1
        mid = (first_pos + last_pos) // 2

        if x == a[mid]:
            flag = 1
            print(f"Element found at position {mid}.")
            return count
        elif x < a[mid]:
            last_pos = mid - 1
        else:
            first_pos = mid + 1

    print("Number is not present.")
    return count

# Sample Usage:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7
iterations = binary_search(a, x)
print(f"Number of iterations: {iterations}")