import networkx as nx

# Create an empty graph
g = nx.Graph()

# Add nodes
g.add_node(1)
g.add_node(2)
g.add_node(3)

# Add edges
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)

# Print nodes and edges
print("Nodes:", g.nodes)
print("Edges:", g.edges)

# Visualize the graph
import matplotlib.pyplot as plt
nx.draw(g)
plt.show()