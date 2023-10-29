I'm glad to convert the questions and answers into multiple-choice questions (MCQs) for you. Here are the questions with the correct answers indicated:

1. What is a sink?
   - A) A node with no incoming edges.
   - B) A node with maximum incoming edges.
   - C) A node with maximum outgoing edges.
   - D) A node with no outgoing edges.
     
     **Correct Answer: D) A node with no outgoing edges.***

2. What should we do when encountering a sink in the case of the PageRank algorithm?
   - A) Stop the algorithm.
   - B) Start with the last node.
   - C) Randomly choose a node from all nodes.
   - D) Randomly choose a node from neighbor nodes.

     **Correct Answer:C) Randomly choose a node from all nodes.**

3. In the PageRank algorithm:
   - A) We randomly travel from node to node without any relationship.
   - B) We randomly travel from node to neighbor node.
   - C) The maximum visited node will be the leader.
   - D) B and C.
  
   **Correct Answer: D) B and C.**

4. If we perform the PageRank algorithm on the web as a graph, which of the following is true?
   - A) Websites are nodes and hyperlinks in websites are edges.
   - B) Hyperlinks in websites are nodes and websites are edges.
   - C) Websites will work as nodes and edges.
   - D) Hyperlinks will work as nodes and edges.
   
   **Correct Answer: A) Websites are nodes and hyperlinks in websites are edges.**

5. Identify the type of graph:
   ![[Pasted image 20231029102545.jpg]]
   - A) Triangle Graph
   - B) Directed Graph
   - C) Barbell Graph
   - D) Wheel graph
     
    **Correct Answer: C) Barbell Graph**

6. Which of the following Python functions will return a random floating-point number between 0 and 1?
   - A) random.float()
   - B) random.randomfloat()
   - C) random.frandom()
   - D) random.random()
   
   **Correct Answer: D) random.random()**

7. What will be the `G.out_degree(3)` for the following graph (`G`)?
   ![[Pasted image 20231029102555.jpg]]
   - A) 4
   - B) 5
   - C) 3
   - D) 6
   
    **Correct Answer: B) 5**

8. In the PageRank algorithm, the leader is decided by:
   - A) A node (person) with the maximum number of outgoing edges.
   - B) A node (person) with the maximum number of incoming edges.
   - C) A node (person) which is visited the maximum times.
   - D) Can not decide.
   
   **Correct Answer: C) A node (person) which is visited the maximum times.**

9. Which of the following is true about directed graphs?
   - A) One can come back and forth from one node to another using a single edge.
   - B) One can only go forward from one node to another using a single edge.
   - C) One can go to any node from one node using one edge.
   - D) None of the above.

   **Correct Answer: B) One can only go forward from one node to another using a single edge.**
11. What will be the output of the following code?
- A) ['Hey', 'there', '!']
- B) ['Hey', 'there', ' ', '!']
- C) ['H', 'e', 'y', ' ', 't', 'h', 'e', 'r', 'e', '!']
- D) ['H', 'e', 'y', 't', 'h', 'e', 'r', 'e', '!']

**Correct Answer: C) ['H', 'e', 'y', ' ', 't', 'h', 'e', 'r', 'e', '!']**

---
## Programming Assignment 1
```python
print(int("".join(list(input())[::-1])),end="")
pass      
                
```

## Programming Assignment 2
```python
Ll=input().split()
M=list()
for i in Ll:
  M.append("".join(list(i)[::-1]))
ans=[]
for i in sorted(M):
  ans.append("".join(list(i)[::-1]))
print(ans,end="")	  
```

## Programming Assignment 3
```python
roll146=input()
print(roll146.split('@')[0],roll146.split('@')[1].split(".")[0],end="")
```
