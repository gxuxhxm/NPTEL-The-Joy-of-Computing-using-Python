import networkx as nx
import matplotlib.pyplot as plt

# Part 1: Introduction
print("Part 1: Introduction")
print("Introduction to PageRank and how it works.")
print("Mention of creating a directed graph using NetworkX.")
print("Setting up Python libraries.")
G = nx.DiGraph()

# Part 2: Directed Graph and Edge Data
print("\nPart 2: Directed Graph and Edge Data")
print("Explanation of the edge list data.")
print("Using nx.read_edge_list to read the data.")
print("Displaying the directed graph.")
G = nx.read_edgelist("page_rank.txt", create_using=nx.DiGraph(), nodetype=int)
nx.draw(G, with_labels=True)
plt.show()

# Part 3: Points Distribution Method
print("\nPart 3: Points Distribution Method")
print("Introduction to the concept of distributing points based on edges.")
print("Explaining how nodes distribute points to their neighbors.")
print("Describing the iterative process.")

# Part 4: Simulating Points Distribution in Excel
print("\nPart 4: Simulating Points Distribution in Excel")
print("Demonstrating the points distribution in an Excel sheet.")
print("Showing how to manually distribute points based on the edges.")

# Part 5: Programming a Complex Network
print("\nPart 5: Programming a Complex Network")
print("Starting with a more complex network with many nodes and edges.")
print("Creating a random network for demonstration.")
G = nx.gnp_random_graph(25, 0.2, directed=True)

# Part 6: Visualizing the Complex Network
print("\nPart 6: Visualizing the Complex Network")
print("Visualizing the complex network using NetworkX.")
print("Showing how to plot the directed graph.")
nx.draw(G, with_labels=True)
plt.show()

# Part 7: Equal Points to All Nodes
print("\nPart 7: Equal Points to All Nodes")
print("Initializing equal points to all nodes in the network.")
print("Starting the points distribution game.")

# Part 8: Points Distribution Based on Outgoing Edges
print("\nPart 8: Points Distribution Based on Outgoing Edges")
print("Describing how nodes distribute points based on their outgoing edges.")
print("Simulating the distribution process.")

# Part 9: User-Controlled Stopping of Points Distribution
print("\nPart 9: User-Controlled Stopping of Points Distribution")
print("Allowing the user to control when the points distribution process stops.")

# Part 10: Converting Point List to Dictionary
print("\nPart 10: Converting Point List to Dictionary")
print("Explaining the need to convert the list of points to a dictionary to preserve node information.")
points_dict = {}
for i in range(len(points)):
    points_dict[i] = points[i]

# Part 11: Ranking Nodes by Points
print("\nPart 11: Ranking Nodes by Points")
print("Describing the process of ranking nodes based on their points.")
print("Using sorted to sort the dictionary by point values.")
sorted_points = sorted(points_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_points)

# Part 12: Comparing with NetworkX PageRank
print("\nPart 12: Comparing with NetworkX PageRank")
print("Using NetworkX's nx.pagerank to compute PageRank values for the graph.")
print("Comparing the results with the manually calculated PageRank.")
networkx_pagerank = nx.pagerank(G)
sorted_networkx_pagerank = sorted(networkx_pagerank.items(), key=lambda x: x[1], reverse=True)
print(sorted_networkx_pagerank)

# Part 13: Proving PageRank Convergence
print("\nPart 13: Proving PageRank Convergence")
print("Mentioning the mathematical proof of PageRank convergence.")
print("Explaining the convergence state of PageRank.")
print("Emphasizing that even if different methods or seeds are used, the distribution is the same.")

# Part 14: Creating a Directed Graph from Edge Data
print("\nPart 14: Creating a Directed Graph from Edge Data")
print("Using NetworkX to create a directed graph from edge data.")
print("Reading data from a file using nx.read_edgelist.")
G = nx.read_edgelist("page_rank.txt", create_using=nx.DiGraph(), nodetype=int)

# Part 15: Visualizing the Directed Graph
print("\nPart 15: Visualizing the Directed Graph")
print("Visualizing the directed graph created from edge data.")
print("Showing how to draw the graph with labels.")
nx.draw(G, with_labels=True)
plt.show()

# Part 16: Task for the Audience
print("\nPart 16: Task for the Audience")
print("Assigning a task to the audience: Running PageRank on the graph created in Part 15 to determine the leader of the group.")
