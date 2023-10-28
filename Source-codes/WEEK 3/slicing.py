# Sample list of students
students = ["akanksha", "arun", "Harish", "lakshmi", "rajesh", "varsha"]

# Basic list slicing: students[1:4]
subset = students[1:4]
print(subset)  # Output: ['arun', 'Harish', 'lakshmi']

# Slicing with a start index only: students[:4]
subset = students[:4]
print(subset)  # Output: ['akanksha', 'arun', 'Harish', 'lakshmi']

# Slicing with an end index only: students[2:]
subset = students[2:]
print(subset)  # Output: ['Harish', 'lakshmi', 'rajesh', 'varsha']


#removing items
my_list = [10, 20, 30, 40, 50]

# Remove the value 30 from the list
my_list.remove(30)
print(my_list)  # Output: [10, 20, 40, 50]

# Remove the item at index 2 (value 40) and store it in a variable
removed_item = my_list.pop(2)
print(removed_item)  # Output: 40


#List Comprehensions
original_list = [1, 2, 3, 4, 5]

# Create a new list by squaring each element from the original list
squared_list = [x**2 for x in original_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25]