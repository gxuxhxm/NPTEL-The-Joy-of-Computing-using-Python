def magic_square(n):
    magic_square = [[0 for _ in range(n)] for _ in range(n)]
    i = n // 2
    j = n - 1
    num = n * n
    count = 1

    while count <= num:
        if i == -1 and j == n:
            j = n - 2
            i = 0
        if j == n:
            j = 0
        if i < 0:
            i = n - 1
        if magic_square[i][j] != 0:
            j -= 2
            i += 1
            continue
        else:
            magic_square[i][j] = count
            count += 1
        j += 1
        i -= 1

    return magic_square

# Example usage:
n = 3  # You can change n to any odd number
result = magic_square(n)
for row in result:
    print(row)
