## How does google work
---
**Part 1: Introduction**
- Introduction to PageRank and how it works.
- Mention of creating a directed graph using NetworkX.
- Setting up Python libraries.

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
```

**Part 2: Directed Graph and Edge Data**
- Explanation of the edge list data.
- Using `nx.read_edge_list` to read the data.
- Displaying the directed graph.

```python
G = nx.read_edgelist("page_rank.txt", create_using=nx.DiGraph(), nodetype=int)
nx.draw(G, with_labels=True)
plt.show()
```

**Part 3: Points Distribution Method**
- Introduction to the concept of distributing points based on edges.
- Explaining how nodes distribute points to their neighbors.
- Describing the iterative process.

**Part 4: Simulating Points Distribution in Excel**
- Demonstrating the points distribution in an Excel sheet.
- Showing how to manually distribute points based on the edges.

**Part 5: Programming a Complex Network**
- Starting with a more complex network with many nodes and edges.
- Creating a random network for demonstration.

```python
import random

G = nx.gnp_random_graph(25, 0.2, directed=True)
```

**Part 6: Visualizing the Complex Network**
- Visualizing the complex network using NetworkX.
- Showing how to plot the directed graph.

```python
nx.draw(G, with_labels=True)
plt.show()
```

**Part 7: Equal Points to All Nodes**
- Initializing equal points to all nodes in the network.
- Starting the points distribution game.

**Part 8: Points Distribution Based on Outgoing Edges**
- Describing how nodes distribute points based on their outgoing edges.
- Simulating the distribution process.

**Part 9: User-Controlled Stopping of Points Distribution**
- Allowing the user to control when the points distribution process stops.

**Part 10: Converting Point List to Dictionary**
- Explaining the need to convert the list of points to a dictionary to preserve node information.

```python
points_dict = {}
for i in range(len(points)):
    points_dict[i] = points[i]
```

**Part 11: Ranking Nodes by Points**
- Describing the process of ranking nodes based on their points.
- Using `sorted` to sort the dictionary by point values.

```python
sorted_points = sorted(points_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_points)
```

**Part 12: Comparing with NetworkX PageRank**
- Using NetworkX's `nx.pagerank` to compute PageRank values for the graph.
- Comparing the results with the manually calculated PageRank.

```python
networkx_pagerank = nx.pagerank(G)
sorted_networkx_pagerank = sorted(networkx_pagerank.items(), key=lambda x: x[1], reverse=True)
print(sorted_networkx_pagerank)
```

**Part 13: Proving PageRank Convergence**
- Mentioning the mathematical proof of PageRank convergence.
- Explaining the convergence state of PageRank.
- Emphasizing that even if different methods or seeds are used, the distribution is the same.

**Part 14: Creating a Directed Graph from Edge Data**
- Using NetworkX to create a directed graph from edge data.
- Reading data from a file using `nx.read_edgelist`.

```python
G = nx.read_edgelist("page_rank.txt", create_using=nx.DiGraph(), nodetype=int)
```

**Part 15: Visualizing the Directed Graph**
- Visualizing the directed graph created from edge data.
- Showing how to draw the graph with labels.

```python
nx.draw(G, with_labels=True)
plt.show()
```

**Part 16: Task for the Audience**
- Assigning a task to the audience: Running PageRank on the graph created in Part 15 to determine the leader of the group.
## **Collatz Conjecture**
---
**Collatz Conjecture: Part 1**
- Introduction to the Collatz Conjecture.
- Explaining the simplicity and complexity of the conjecture.
- The conjecture states that for any given positive integer n:
  - If n is even, divide it by 2.
  - If n is odd, multiply it by 3 and add 1.
- Demonstrating the application of the conjecture with examples.

```python
def collatz(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    print(f'Number 1 achieved after {iterations} iterations.')

# Example usage:
collatz(12)
```

**Collatz Conjecture: Part 2**
- Revisiting the Collatz Conjecture.
- A reminder of the operations to apply to n.
- The Collatz Conjecture is tested using a Python function.

```python
def check_collatz(number):
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        iterations += 1
    print(f'Number 1 achieved after {iterations} iterations.')

# Example usage:
check_collatz(12)
check_collatz(20)
```

**Collatz Conjecture: Part 3**
- Introducing a Python function to check the Collatz Conjecture for any given number.
- Demonstrating how different numbers reach 1 in varying numbers of iterations.

```python
def check_collatz(number):
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        iterations += 1
    print(f'Number 1 achieved after {iterations} iterations.')

# Example usage:
check_collatz(12)
check_collatz(20)
check_collatz(64)
```

---
thank you
 ~created by [Goutham](https://www.github.com/gxuxhxm)

