Sure, here are the questions converted into multiple-choice questions with the correct answers checked:

1. Which is the fastest sorting algorithm?
   - A) Bubble Sort
   - B) Bucket Sort
   - C) Quick Sort ✓
   - D) Insertion Sort

2. How can you remove all items from a dictionary?
   - A) dict.clear() ✓
   - B) del dict
   - C) dict.remove_all()
   - D) dict.pop()

3. What happens if you try to add a new key to a dictionary that already exists?
   - A) The key and its associated value will be updated. ✓
   - B) The key and its associated value will be added.
   - C) The key will be added, but the associated value will remain unchanged.
   - D) An error will occur.

4. Which of the following is true about dictionaries?
   - A) There can be multiple same keys.
   - B) Every value must be unique.
   - C) Every key must be unique. ✓
   - D) We can’t get every key from the dictionary.

5. What is the syntax to create a dictionary?
   - A) D = []
   - B) D = {}✓
   - C) D = ()
   - D) D = dictionary() 

6. What will be the output of the following code?
   ![[Pasted image 20231029093946.jpg]]
   - A) 'a' 'b' 'c'
   - B) 20 30 50
   - C) ('a', 20), ('b', 30), ('c', 50) ✓
   - D) ('a', 'b', 'c') (20, 30, 50)

7. In the Monte Hall Problem, what is the probability of winning if you switch doors after the host reveals a goat behind one of the other doors?
   - A) 1/3
   - B) 1/2
   - C) 2/3 ✓
   - D) 3/4

8. In the Monte Hall Problem, what is the probability of winning if you do not switch doors after the host reveals a goat behind one of the other doors?
   - A) 1/3 ✓
   - B) 1/2
   - C) 2/3
   - D) 3/4

9. What is the name of the game show that the Monte Hall Problem was based on?
   - A) Jeopardy
   - B) Wheel of Fortune
   - C) The Price is Right
   - D) Let's Make a Deal ✓

10. Which module in Python can be used for Speech to Text conversion?
    - A) SpeechRecognition ✓
    - B) PyAudio
    - C) Wave
    - D) all of the above do the same for these

---
## Programming Assignment 1
You are given a string S. Write a function count_letters which will return a dictionary containing letters (including special character) in string S as keys and their count in string S as values.  
(input and output will be handled by us you just need to write the function and return the dictionary)  

- Input  
The Joy of computing  
  
- Output  
{'T': 1, 'h': 1, 'e': 1, ' ': 3, 'j': 1, 'o': 3, 'y': 1, 'f': 1, 'c': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1}  
  
- Explanation: T is appeared once in the string, similarly o is appeared 3 times in the string and so on. (You do not have to worry about the order of arrangement in your dictionary)

```python
def count_letters(S):
    output_dict = {}
    for char in S:
        if char in output_dict:
            output_dict[char] += 1
        else:
            output_dict[char] = 1
    return output_dict

S = input()
d = count_letters(S)
d1 = {}
for i in S:
    try:
        d1[i]+=1
    except KeyError:
        d1[i]=1
if d1 == d:
    print('yes')
else:
    print('no')
```

## ## Programming Assignment 2
You are given a list L. Write a function uniqueE which will return a list of unique elements is the list L in sorted order. (Unique element means it should appear in list L only once.)  
Input will be handled by us  
- Input  
[1,2,3,3,4,4,2,5,6,7]  
  
- Output  
[1,5,6,7]  
  
- Explanation  
Elements 1,5,6,7 appears in the input list only once.

```python
def uniqueE(L):
  ans=list()
  for a in L:
    if L.count(a)==1:
      ans.append(a)
  return(sorted(ans))   
  
L = [int(i) for i in input().split()]
print(uniqueE(L))
```

## Programming Assignment 3
You are given a list L. Write a program to print first prime number encountered in the list L.(Treat numbers below and equal to 1 as non prime)  
Input will be handled by us.  
  
- Input  
[1,2,3,4,5,6,7,8,9]  
  
- output  
2  
  
- Explanation  
Since 2 is the first prime number is list L, therefor it is printed.

```python
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_first_prime(L):
    for num in L:
        if is_prime(num):
            return num
    return None

L = [int(i) for i in input().split()]
first_prime = find_first_prime(L)
if first_prime is not None:
    print(first_prime)

```