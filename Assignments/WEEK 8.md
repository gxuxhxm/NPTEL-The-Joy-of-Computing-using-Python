
1. What is the correct initialization of tuples?
   - Dates = [12, 23, 3, 4]
   - Dates = (12, 23, 3, 4) ✓
   - Dates = {12, 23, 3, 4}
   - Both B and C

2. What operations can be done on tuples?
   - Tuples are appendable.
   - We can delete a value from tuples.
   - Both A and B.
   - We can count the number of instances of an element. ✓

3. What will be the output of the following code?
   ![[Pasted image 20231029100417.jpg]]
   - 1,2,3,4,5
   - 5,4,3,2,1
   - 5,4,3,2 ✓
   - 1,2,3,4

4. What will be the output of the following code?
   ![[Pasted image 20231029100422.jpg]]
   - facebook ✓
   - gbdfcppl
   - ezbdannj
   - ytvxuhhd

5. When the following program will clap?
   ![[Pasted image 20231029100428.jpg]]
   - When both players will enter the same letters.
   - When player 2 will enter the next letter with respect to player 1. ✓
   - When player 1 will enter the next letter with respect to player 2.
   - It will never clap.

6. Which statement is correct about the following program?
   ![[Pasted image 20231029100436.jpg]]
   - The graph will go up when guess and pick are the same.
   - The graph will go down when guess and pick are the same.
   - The graph will go up when guess and pick are not the same. ✓
   - Both B and C

7. What does NLTK do?
   - Helps to work with human language data. ✓
   - Helps to convert machine data into human language.
   - Helps to work on gibberish language.
   - Helps to translate dog language into human language.

8. What is the output of the following code?
   ![[Pasted image 20231029100442.jpg]]
   - ['!', 'e', 'e', 'e', 'h', 'h', 'r', 't', 'y']
   - ['h', 'e', 'y', '!', 't', 'h', 'e', 'r', 'e']
   - ['y', 't', 'r', 'h', 'h', 'e', 'e', 'e', '!'] ✓
   - None of the above

9. While converting an image into black and white during enhancement, you cannot convert it back into a colored image.
   - True
   - False ✓

10. How does VADER help in sentiment analysis?
    - It calculates whether the statement is negative, positive, or neutral. ✓
    - It takes care of the intensity of a statement. ✓
    - Both A and B
    - None of the above
---

```python
def squareT(T):
  return(T+tuple([i*i  for i in T]))
                  
if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    T = tuple(L)
    ans = squareT(T)
    if type(ans) == type(T):
        print(ans)
```

```python
vo = list('aeiou')+list('AEIOU')
def replaceV(s):
    ans = ""
    a = 0 
    while a < len(s) - 2: 
        if s[a] in vo and s[a + 1] in vo and s[a + 2] in vo:
            a = a + 2  
            ans+="_"
        else:
            ans += s[a]
        a += 1  
    ans += s[a:] 
    return(ans)			
			

                  
                
S = input()
print(replaceV(S))
```

## Programming Assignment 3
```python
n = 10
L = list(map(int, input().split()))
G=list()
for i in L:
  if i!=0:
    G.append(i)
G+=[0]*(len(L)-len(G))
print(G,end="")
```