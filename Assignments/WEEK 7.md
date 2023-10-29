
1. Values of CSV files are separated by?
   - Comma ✓
   - Colons
   - Semi-colons
   - Slash

2. What is the output of the following code?
   ![[Pasted image 20231029095827.jpg]]
   - 1, 2, 3, 7, 11, 10, 9, 5, 6
   - 1, 2, 3, 5, 6, 7, 9, 10, 11 
   - 1, 5, 9, 10, 11, 7, 3, 2, 6✓
   - 1, 5, 9, 2, 6, 10, 3, 7, 11

3. What will be the output of the following code?
   ![[Pasted image 20231029095847.jpg]]
   - Scalar triangle
   - Right angle triangle
   - Equilateral triangle ✓
   - Isosceles triangle

4. Which of the following program will draw a hexagon?
   - Program A 
     ![[Pasted image 20231029095903.jpg]]
   - Program B✓
     ![[Pasted image 20231029095922.jpg]]
   - Program C
     ![[Pasted image 20231029095928.jpg]]
   - Program D 
     ![[Pasted image 20231029095932.jpg]]

5. Which library is used to render data on Google Maps?
   - gplot
   - googlemaps
   - gmplot ✓
   - gmeplot

6. What is the output of the following code?
   ![[Pasted image 20231029095941.jpg]]
   - Output A
     ![[Pasted image 20231029095951.jpg]]
   - Output B
     ![[Pasted image 20231029095954.jpg]]
   - Output C✓
     ![[Pasted image 20231029100005.jpg]]
   - Output D 
     ![[Pasted image 20231029100010.jpg]]

7. Which turtle command is equivalent to lifting up a pen?
   - penlift()
   - penup() ✓
   - uppen()
   - penremove()

8. Why do we use functions?
   - To improve readability.
   - To reuse code blocks.
   - For the ease of code debugging.
   - All of the above ✓

9. Which library is used to import images?
   - PIL ✓
   - Imageview
   - IMG
   - image

10. In snakes and ladders, what can be the ways to track ladders and snakes?
    - Maintain a dictionary with snakes or ladder number blocks as keys. ✓
    - Using the if condition to check on every number.
    - Both A and B. ✓
    - None of the above

## Programming Assignment 1
```python
def DiagCalc(M):
    countL = 0
    countR = 0
    for i in range(len(M)):
        countL += M[i][i]
        countR += M[i][-1 - i]

    print(countL)
    print(countR)
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

DiagCalc(M)
```

## Programming Assignment 2
```python
def Transpose(M):
    rowlen = len(M)
    collen = len(M[0])
    ans  = [[] for i in range(collen)]
    for i in range(collen):
        for j in range(rowlen):
            ans[i].append(M[j][i])
    return ans
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)
print(Transpose(M))
```

## Programming Assignment 3
```python
def snake(M):
    rowlen = len(M)
    collen = len(M[0])
    ans  = []

    for i in range(rowlen):
        if i%2 == 0:
            for j in M[i]:
                ans.append(j)
        else:
            l = M[i]

            for j in range(-1, -collen-1, -1):
                ans.append(l[j])
    return ans
n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

print(snake(M))
```