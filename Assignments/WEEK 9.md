1. How can we identify which book is written by which author?
   -  By matching handwriting.
   - By analyzing word length with previous books. ✓
   -   By analyzing the number of pages in a book.
   -  By analyzing the book’s preface.
   - 
2. How can a list L be transformed into a tuple?
   - tuple(L) ✓
   - tup(L)
   - L(tuple)
   - L(tup)

3. Will the following piece of code always return True?
   ![[Pasted image 20231029100808.jpg]]
   - True
   - False ✓

4. What is the output of the following code?
   ![[Pasted image 20231029100835.jpg]]
   - ![[Pasted image 20231029100842.jpg]]
   - ![[Pasted image 20231029100849.jpg]]
   - ![[Pasted image 20231029100859.jpg]]
   - ![[Pasted image 20231029100902.jpg]]✓ 
 

5. How many edges are there in the following graph?
   ![[Pasted image 20231029100936.jpg]]
   - 4 ✓
   - 5
   - 3
   - 2

6. How many neighbors does node 3 have?
   ![[Pasted image 20231029100942.jpg]]
   - 2
   - 4
   - 1
   - 3 ✓

7. In which of the following ways can we create a string in Python?
   - By using single quotes.
   - By using double quotes.
   - By using triple quotes.
   - All of the above. ✓

8. Which of the following is not true about Stylometry Analysis?
   - It is quantitative study of literature style
   - It is based on the observation that the authors tend to write in relatively consistent and recognizable ways
   - Any two people may have the same vocabulary ✓
   - It is a tool to study a variety of questions involving the style of writing

9. A complete graph will have __ degree of separation.
   - 1 ✓
   - 2
   - 3
   - Depends on the number of nodes.

10. Networkx in Python is used for
    - Making networks
    - Analyzing networks
    - Visualizing networks
    - All of the above ✓

---
## Programming Assignment 1

```python
def subStr(s1,s2):
  return(s2 in s1)  
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(subStr(s1, s2))
```
## Programming Assignment 2 
```python
def mergeDic(d1,d2):
  for kd in d2:
    if kd not in d1:
      d1[kd]=d2[kd]
  return(d1)

key = list(map(int, input().split()))
val = list(map(int, input().split()))

d1 = {}
for i in range(len(key)):
    d1[key[i]] = val[i]
    
d2 = {}
key = list(map(int, input().split()))
val = list(map(int, input().split()))
for i in range(len(key)):
    d2[key[i]] = val[i]

print(mergeDic(d1, d2))
```
## Programming Assignment 3
```python
n = int(input())
N=list(str(n))
P=[]
for isp in N:
  if isp not in P:
    P.append(isp)
ans=[]
for i in range(len(P)):
  a=[]
  for j in range(len(N)):
    if(P[i]==N[j]):
      a.append(j)
  ans.append(a)
#print(ans)

for i in range(len(P)):
  print(int(P[i]), "",end="")
  #print(len(ans[i]))
  for j in range(len(ans[i])):
               print(int(ans[i][j]),"",end="")
  print()
```