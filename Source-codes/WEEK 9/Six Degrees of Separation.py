import networkx as nx

# Step 1: Import Network Data
G = nx.read_edgelist("facebook_combined.txt")

# Step 2: Extract Nodes
N = list(G.nodes)

# Step 3: Calculate Shortest Paths
shortest_path_length_list = []
for u in N:
    for v in N:
        if u != v:
            l = nx.shortest_path_length(G, source=u, target=v)
            print(f"Shortest path between {u} and {v} is of length {l}")
            shortest_path_length_list.append(l)

# Step 4: Calculate Minimum, Maximum, and Average Shortest Path Lengths
minimum_shortest_path_length = min(shortest_path_length_list)
maximum_shortest_path_length = max(shortest_path_length_list)
average_shortest_path_length = sum(shortest_path_length_list) / len(shortest_path_length_list)

# Step 5: Analyze Six Degrees of Separation
print("Minimum Shortest Path Length:", minimum_shortest_path_length)
print("Maximum Shortest Path Length:", maximum_shortest_path_length)
print("Average Shortest Path Length:", average_shortest_path_length)

# Step 6: Explain Six Degrees of Separation
print("Six Degrees of Separation: The idea that you can connect with anyone in the world through a network of acquaintances within an average of six connections.")

# Step 7: Explain Exponential Growth in Connections
print("Exponential Growth in Connections: This concept works because of the exponential growth in the number of friends' friends within a social network.")

# Step 8: Encourage Exploration of NetworkX
print("Encouragement to Explore NetworkX: You can explore the NetworkX library further and make use of its various functionalities for graph analysis.")
