1. Which library is used for browser automation?
   - selenium ✓

2. What the given statement will return?
   - Time in seconds. ✓
   - Current date and time.
   - Time in minutes.
   - The current date, time, and year.

3. Identify the library that can be used to get all time zones:
   - pytz ✓
   - selenium
   - calendar
   - nltk

4. The output of the following code will be?
   ![[Pasted image 20231029102100.jpg]]
   - Date and time in yy-mm-dd hh:MM:ss:ms respectively. ✓
   - Time and date in hh:MM:ss:ms dd-mm-yy respectively.
   - Date and time in mm-dd-yy hh:MM:ss:ms respectively.
   - Date and time in dd-mm-yy hh:MM:ss:ms respectively.

5. We can use the selenium web driver for different browsers.
   - True ✓
   - False

6. What will be the output of the following code?
   ![[Pasted image 20231029102107.jpg]]
   - Print the current date and time of all time zones. ✓
   - Print the current date and time of specific time zones.
   - Print the current date of all time zones.
   - Print the current date of some specific time zones.

7. What will be the output if the system date is 10 December 2021(Friday)?
   ![[Pasted image 20231029102111.jpg]]
   - 4 ✓
   - 3
   - 5
   - error

8. Which statement will return the calendar for a whole year?
   - calendar.prcal(year) ✓
   - calendar.month(year)
   - calendar(year)
   - calendar.year(year)

9. By which statement can we come out of the loop?
   - break ✓
   - continue
   - leave
   - catch

10. How to check for the leap year?
    - calendar.isleap(year) ✓
    - calendar.leap(year)
    - calendar.is_leap(year)
    - calendar.checkleap(year)

---
##  Programming Assignment 1
```python
a1=int(input())
b3=int(input())
c=int(input())
L=[a1,b3,c]
h=max(L)
L.remove(h)
if h**2==L[0]**2+L[1]**2:
  print("YES",end="")
else:
  print("NO",end="")
                  
                
```
## Programming Assignment 2
```python
LGF=sorted(input().split("#"),reverse=True)
print("#".join(LGF),end="")            
```

## Programming Assignment  3
```python
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))

for i in range(a, b + 1):
    if not is_prime(i):
        print(i)

```