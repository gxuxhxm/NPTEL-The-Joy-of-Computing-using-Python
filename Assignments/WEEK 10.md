1. What is the output of the following code?
   ![[Pasted image 20231029101354.jpg]]
   - hello everyone 
   - Hello Everyone
   - helloeveryone
   - hello everyone✓

2. In flames game, when will we stop the iteration over FLAMES?
   - When only one letter is left in flames. ✓
   - Only once.
   - Only the letter remaining times.
   - None of the above.

3. Output of the following code will be?
   ![[Pasted image 20231029101406.jpg]]
   - hello
   - h.e.l.l.o
   - .h.e.l..l.o ✓
   - .h.e.l.l.o

4. Which code snippet represents replacing all vowels with ‘ _’ in a string? 
- ![[Pasted image 20231029101447.jpg]]
  - ![[Pasted image 20231029101454.jpg]]
  - ![[Pasted image 20231029101459.jpg]]
  - ![[Pasted image 20231029101503.jpg]] ✓

5. What will be the output of the following list slicing.
   ![[Pasted image 20231029101523.jpg]]
   - ' Joy of C' ✓
   - 'Joy of C'
   - 'Joy of Co'
   - ' Joy of Co'

6. What does the following code represent?
   ![[Pasted image 20231029101527.jpg]]
   - Replacing all vowels at even index with ‘ _’ . 
   - Replacing all letters at even index with ‘ _ ’.
   - Replacing all vowels at odd index with ‘ _’ .✓
   - Replacing all letters at odd index with ‘ _’ .

7. What will be the output of the following code?
   ![[Pasted image 20231029101558.jpg]]
   - [3 7] ✓
   - [4 6]
   - [3 4]
   - None of the above

8. What is the correct way to display the transpose of a matrix?
   - ![[Pasted image 20231029101615.jpg]]
   - ![[Pasted image 20231029101642.jpg]] ✓
   - ![[Pasted image 20231029101649.jpg]]✓ 
   - ![[Pasted image 20231029101654.jpg]]
   
9. Are Lossy and Lossless compressions the same?
   - Yes, they are identical.
   - No, they are different. ✓
   - It depends on the context.
   - Not enough information provided.

10. What is the shape of the following numpy array?
    numpy.array([ [1,2,3], [4,5,6] ])
    - (2,3) ✓
    - (3,2)
    - (3,3)
    - (2,2)

11. What will be the output of the following code?
    ![[Pasted image 20231029101743.jpg]]
    - [[ 7 7 17] [ 6 26 16]] ✓
    - [[ -7 -7 -17] [ -6 -26 -16]]
    - [[ 7 7 17] [ 6 26 16]]
    - [[ 9 11 23] [14 36 28]]
---
## Programming Assignment 1
```python
L = list(map(int, input().split()))
K=[0]*(max(L)+1)
for i in range(len(K)):
  if i in L:
    K[i]=i
print(*K,end="") 

```
## Programming Assignment 2
```python
def closestSchool(x, y, L):
  min=9999999
  distance=list()
  for ij in L: 
    dis=((x-ij[0])**2+(y-ij[1])**2)**0.5
    distance.append(dis)
    if dis<min:
      min=dis  
  for ij in range(len(distance)):
    if distance[ij]==min:
        print(L[ij]) 		

x, y = map(int, input().split())

n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)
closestSchool(x, y, L)
```
## Programming Assignment 3
```python
print(input().swapcase(),end='')
```