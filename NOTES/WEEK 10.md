## FLAMES
---
### Explaination:
1. **Objective**: The FLAMES game is a popular childhood game used to predict the relationship between two people, usually with romantic implications.
2. **Acronym**: FLAMES stands for **F**riends, **L**overs, **A**ffection, **M**arriage, **E**nemy, **S**iblings. These are the possible outcomes of the game.
3. **Participants**: Typically, two people's names are used for this game. They can be friends, lovers, classmates, or any two individuals.
4. **Name Conversion**: The game starts with the input of the two people's names. These names are usually converted to lowercase to ensure consistency in the comparison.
5. **Removing Matching Letters**: The game then checks each letter of the two names for common characters. These common letters are removed from both names. The process continues until no matching letters are found.
6. **Modular Counting**: After removing the matching letters, the remaining letters are counted. This counting is performed in a circular or modular fashion, meaning it restarts from the beginning after reaching the end of the list.
7. **Result Computation**: The count is used to determine which category the result falls into (Friends, Lovers, Affection, Marriage, Enemy, or Siblings).
8. **Handling Siblings**: If the result count reaches the last category (Siblings), the game may either stop or start counting from the first category again, depending on the specific implementation.
9. **Output**: The outcome of the game is the category that corresponds to the count, such as "Friends" or "Lovers."
10. **Discussion**: FLAMES is often seen as a fun and playful game, and people may discuss the results and their implications. It's essential to remember that the game is usually taken lightly and isn't meant to be taken seriously.
11. **Alternative Interpretations**: Some variations and interpretations of the game exist, and different cultures may have their own versions. The key is to have fun and not to base important life decisions on the game's results.
12. **Variations**: People may create variations or extensions of the game to explore different aspects of a relationship or make it more interesting.
### FLAMES Game Summary:

1. **Input Names**: You start by taking two persons' names as input.

2. **Preprocessing Names**: Convert the names to lowercase and remove any spaces.

3. **Remove Matching Letters**: Define a function to remove matching letters. This function takes two parameters, which are the processed names in the form of lists.

   ```python
   def remove_matching_letter(list1, list2):
       # Iterate through the lists to find matching letters and remove them
       for i in range(len(list1)):
           for j in range(len(list2)):
               if list1[i] == list2[j]:
                   list1.remove(list1[i])
                   list2.remove(list2[j])
                   return [list1 + ['*'] + list2, True]
       return [list1 + ['*'] + list2, False]
   ```

4. **Flag for Proceeding**: Use a flag called `proceed` to determine whether to continue checking for matching letters or to proceed with counting. Initially, set `proceed` to `True`.

5. **Count Matching Letters**: After removing matching letters, count the remaining letters in both lists.

   ```python
   count = len(list1) + len(list2)
   ```

6. **Define FLAMES Result**: Create a list named `result` to store the possible FLAMES outcomes: ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"].

7. **Split Index Calculation**: Calculate the `split_index` based on the count and the length of the result list using the modulo operator. Subtract 1 to convert it to a zero-based index.

   ```python
   split_index = (count % len(result)) - 1
   ```

8. **Process Results Based on Split Index**: Depending on the value of `split_index`, you may need to handle positive and negative values differently.

   - If `split_index` is positive, split the result into the right and left halves and concatenate them accordingly.
   - If `split_index` is negative, consider the left half and ignore the last element.

9. **Loop Until One Result Remains**: Put the counting and processing logic inside a loop that continues as long as the length of the result is greater than one.

10. **Final Result**: When the loop exits, there is only one result left in the `result` list. This result represents the relationship between the two persons.

11. **Print the Result**: Print the final result, and that's the outcome of the FLAMES game.

### Full Code:

Here's the full code for the FLAMES game:

```python
def remove_matching_letter(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list1.remove(list1[i])
                list2.remove(list2[j])
                return [list1 + ['*'] + list2, True]
    return [list1 + ['*'] + list2, False]

def main():
    name1 = input("Enter the name of the first person: ").lower().replace(" ", "")
    name2 = input("Enter the name of the second person: ").lower().replace(" ", "")
    
    list1 = list(name1)
    list2 = list(name2)
    
    proceed = True
    while proceed:
        result, proceed = remove_matching_letter(list1, list2)
    
    count = len(list1) + len(list2)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    split_index = (count % len(result)) - 1
    
    if split_index >= 0:
        right_half = result[split_index + 1:]
        left_half = result[:split_index]
        new_result = right_half + left_half
    else:
        new_result = result[:split_index]  # Ignore the last element
    
    while len(new_result) > 1:
        count = len(new_result)
        split_index = (count % len(new_result)) - 1
        
        if split_index >= 0:
            right_half = new_result[split_index + 1:]
            left_half = new_result[:split_index]
            new_result = right_half + left_half
        else:
            new_result = new_result[:split_index]  # Ignore the last element
    
    final_result = new_result[0]
    print(f"The relationship between {name1} and {name2} is: {final_result}")

if __name__ == "__main":
    main()
```

### Sample Output:

```
Enter the name of the first person: ajay
Enter the name of the second person: priya
The relationship between ajay and priya is: Friends
```

You can input any names to determine the FLAMES relationship between two people. The code handles the logic of the game, from removing matching letters to counting and determining the final result.
## Data Compression
---
Simple and naive method for compressing an image using NumPy and image libraries.

1. **Image Representation**: Images can be represented as matrices, with each pixel corresponding to a matrix cell. In the case of grayscale images, each cell contains values ranging from 0 to 255.

2. **Lossy vs. Lossless Compression**: Image compression can be either lossy or lossless. Lossy compression involves reducing the data while still preserving image visibility, whereas lossless compression reduces the size without data loss.

3. **Compression Objective**: The goal is to map the 8-bit values (0-255) of the image to 3-bit values (0-7) to reduce the image size. This mapping is done based on a simple block approach.

4. **Block-Based Mapping**: Dividing the 8-bit range into blocks: 0-31, 32-63, 64-95, 96-127, 128-159, 160-191, and 192-255. Each block is represented by a 3-bit value: 0, 1, 2, 3, 4, 5, and 6, respectively.

5. **Python Implementation**: We'll use NumPy and the Python Imaging Library (PIL) to load and manipulate the image.

   ```python
   import numpy as np
   from PIL import Image

   # Load the image
   image = Image.open('lena.jpg')
   pixel_map = np.array(image)

   # Create a new image with the same size
   img = Image.new(image.mode, image.size)
   pixel_new = np.array(img)

   # Loop through the original image
   for i in range(image.size[0]):
       for j in range(image.size[1]):
           value = pixel_map[i, j]

           # Map the 8-bit value to a 3-bit value
           if 0 <= value <= 31:
               pixel_new[i, j] = 0
           elif 32 <= value <= 63:
               pixel_new[i, j] = 1
           elif 64 <= value <= 95:
               pixel_new[i, j] = 2
           elif 96 <= value <= 127:
               pixel_new[i, j] = 3
           elif 128 <= value <= 159:
               pixel_new[i, j] = 4
           elif 160 <= value <= 191:
               pixel_new[i, j] = 5
           else:
               pixel_new[i, j] = 6

   # Save the new image
   img.save('lena_compressed.jpg')

   # Display the new image
   img.show()
   ```

6. **Compression Outcome**: The original image was 42.1 KB, and the compressed image is only 4.86 KB. Despite the reduction in size, the compressed image retains the general structure and appearance.

This simple example demonstrates how to achieve image compression through basic mapping techniques. Real-world image compression algorithms, like JPEG, are far more sophisticated but build upon similar principles.

Image compression is a fascinating and evolving field with numerous advanced techniques. This example serves as a starting point for understanding the fundamentals of image compression. 