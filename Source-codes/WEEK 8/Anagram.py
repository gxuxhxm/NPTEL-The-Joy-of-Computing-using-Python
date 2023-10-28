# Input two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if the sorted version of the strings is the same
if sorted(str1) == sorted(str2):
    print("These are anagrams.")
else:
    print("These are not anagrams.")

# Print the sorted versions of the strings for verification
print("Sorted str1:", sorted(str1))
print("Sorted str2:", sorted(str2))