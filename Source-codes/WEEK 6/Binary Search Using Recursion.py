# Recursive binary search function
def binary_search(arr, x, start, end):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, x, mid + 1, end)
        else:
            return binary_search(arr, x, start, mid - 1)
    else:
        return -1