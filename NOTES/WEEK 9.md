## **Natural Language Processing (NLP)**
###
What is NLP (Natural Language Processing)?

Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction between computers and human language. It involves the development of algorithms and models that enable computers to understand, interpret, and generate human language. NLP techniques are used for a wide range of applications, including sentiment analysis, language translation, chatbots, speech recognition, and more.

*Overview*
The discussion revolves around stylometry, which is the quantitative study of literary style. It explores how authors have distinctive and recognizable writing styles and discusses the application of NLP techniques to analyze and distinguish authorship based on writing style. It also demonstrates a basic example of author stylometry by analyzing word length distributions of different authors. Let's combine this knowledge with sentiment analysis.

### *Code Blocks*

Below are the code blocks for combining NLP with sentiment analysis:

```python
# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from textblob import TextBlob

# Define the authors and their documents
authors = ["Hamilton", "Madison", "Disputed", "Jay", "Shared"]
federalist_by_author = {  # Replace with your actual data
    "Hamilton": "Text data for Hamilton...",
    "Madison": "Text data for Madison...",
    "Disputed": "Text data for Disputed...",
    "Jay": "Text data for Jay...",
    "Shared": "Text data for Shared..."
}

# Preprocess and analyze the text
author_tokens = {}
for author, text_data in federalist_by_author.items():
    # Tokenize the text and remove stopwords
    tokens = [word for word in word_tokenize(text_data) if word.isalpha() and word not in stopwords.words("english")]
    author_tokens[author] = tokens

# Calculate the word length distribution for each author
author_word_lengths = {}
for author, tokens in author_tokens.items():
    word_lengths = [len(word) for word in tokens]
    author_word_lengths[author] = word_lengths

# Perform sentiment analysis using TextBlob
sentiment_scores = {}
for author, text_data in federalist_by_author.items():
    blob = TextBlob(text_data)
    sentiment_scores[author] = blob.sentiment.polarity

# Plot the word length distributions
plt.figure(figsize=(12, 6))
for author in authors:
    fdist = FreqDist(author_word_lengths[author])
    fdist.plot(15, title=f"Word Length Distribution for {author}", cumulative=False)
plt.legend(authors)
plt.show()

# Display sentiment analysis results
for author, sentiment in sentiment_scores.items():
    print(f"Sentiment analysis for {author}: Sentiment Score = {sentiment}")
```


The code will generate word length distribution plots for authors and display sentiment analysis results for each author, showing their sentiment scores.

Please note that the provided code is a simplified example, and you should replace the sample text data with your actual data. The sentiment analysis scores provided by TextBlob will be numerical values indicating the sentiment polarity for each author's text, where positive values indicate positive sentiment, and negative values indicate negative sentiment.

## NetworkX
---
### Introduction to NetworkX 01
The presenter introduces NetworkX, a Python library for network analysis. They demonstrate how to create and visualize a simple graph using NetworkX.

**Summary:**
- NetworkX is used for analyzing, visualizing, and generating networks.
- The example graph contains three nodes and three edges, representing a social network.
- The code demonstrates how to create a graph with three nodes, add nodes and edges, and visualize the graph.

**Code:**
```python
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
```

**Sample Output:**
```
Nodes: [1, 2, 3]
Edges: [(1, 2), (1, 3), (2, 3)]
```

### Introduction to NetworkX 02
The presenter continues the NetworkX tutorial by showing how to generate a scale-free graph using NetworkX. They also save the graph in GEXF format for visualization in Gephi.

**Summary:**
- The presenter generates a scale-free graph using NetworkX, which follows a preferential attachment model.
- The generated graph is saved in GEXF format, a standard format for graph data exchange.
- The video introduces Gephi, a tool for graph visualization and analysis.
- Gephi is used to open and visualize the saved GEXF graph, allowing for node coloring and sizing based on node degrees.

**Code (NetworkX to Create Scale-Free Graph and Save in GEXF Format):**
```python
import networkx as nx

# Create a scale-free graph
g = nx.barabasi_albert_graph(50, 2)

# Save the graph in GEXF format
nx.write_gexf(g, "analysis1.gexf")
```

**Sample Output (Gephi Visualization):**
- After opening the saved GEXF file in Gephi, you can visualize the graph and apply visualizations like node coloring and sizing based on node degrees.

## Six Degrees of Separation
---

### **Key Points:**

1. **Introduction to Graph Theory:**
   - The video discusses concepts related to graph theory, specifically focusing on networks and their applications.

2. **Importing NetworkX:**
   - The NetworkX library in Python is introduced as a powerful tool for analyzing graph data.

3. **Reading Graph Data:**
   - The video demonstrates how to read graph data stored in edge list format from a file named "facebook_combined.txt."

   ```python
   import networkx as nx
   G = nx.read_edgelist("facebook_combined.txt")
   ```

4. **Capturing Nodes:**
   - The list of nodes (individuals in the network) is extracted from the graph data and stored in a variable.

   ```python
   N = list(G.nodes)
   ```

5. **Finding Shortest Paths:**
   - The video illustrates how to compute the shortest path length between all possible pairs of nodes in the graph.

   ```python
   shortest_path_length_list = []
   for u in N:
       for v in N:
           if u != v:
               l = nx.shortest_path_length(G, source=u, target=v)
               print(f"Shortest path between {u} and {v} is of length {l}")
               shortest_path_length_list.append(l)
   ```

6. **Minimum, Maximum, and Average Shortest Path Lengths:**
   - The video highlights the computation of the minimum, maximum, and average shortest path lengths.

   ```python
   minimum_shortest_path_length = min(shortest_path_length_list)
   maximum_shortest_path_length = max(shortest_path_length_list)
   average_shortest_path_length = sum(shortest_path_length_list) / len(shortest_path_length_list)
   ```

7. **Understanding Six Degrees of Separation:**
   - The concept of "six degrees of separation" is explained, suggesting that you can connect with anyone in the world through a network of acquaintances within an average of six connections.

8. **Exponential Growth in Connections:**
   - The video provides an intuitive explanation of why this concept works, emphasizing the exponential growth in the number of friends' friends within a social network.

9. **Encouragement to Explore NetworkX:**
   - The video encourages viewers to explore the NetworkX library further and make use of its various functionalities for graph analysis.

### **Sample Output (Partial):**

```
Shortest path between 0 and 1 is of length 1
Shortest path between 0 and 2 is of length 2
Shortest path between 0 and 3 is of length 3
...
Minimum Shortest Path Length: 1
Maximum Shortest Path Length: 3
Average Shortest Path Length: 1.694
```

The sample output is a partial representation of the shortest path calculations between nodes and the computed minimum, maximum, and average shortest path lengths.


**NOTE : In a complete graph, every pair of vertices is directly connected by an edge. This means that the distance, or "degree of separation," between any two vertices in a complete graph is indeed 1. In other words, any two vertices in a complete graph are adjacent to each other, and you can reach one from the other in a single step, making the degree of separation 1.**
## Area Calculation - Dont measure
---
**Part 1: Introduction**
- **Key Points**:
  - Introduction to the topic of calculating the area of Punjab concerning India.
  - The methodology involves utilizing RGB values of specific regions in an image.

**Part 2: Calculating RGB Values of an Image**
- **Key Points**:
  - Demonstrates how to compute the RGB values of an image using Python.
  - PIL (Pillow) is the Python library used for image processing.
  - The image (test1.png) is opened and converted to an RGB matrix.
  - RGB values of two regions within the image are determined using the `getpixel()` method.
- **Code Block**:
  ```python
  from PIL import Image

  # Open the image
  im = Image.open('test1.png')

  # Convert the image to an RGB matrix
  RGB_im = im.convert('RGB')

  # Get RGB values at specific coordinates
  r, g, b = RGB_im.getpixel((x, y))
  ```

**Part 3: Calculating Area Using RGB Values - Randomized Method**
- **Key Points**:
  - Introduces a randomized method to estimate the area of Punjab relative to India using Python.
  - Requires known RGB values for specific regions in an image.
  - Import libraries like Pillow, numpy, and random.
  - A loop iterates a large number of times (e.g., 100,000 iterations).
  - Random x and y coordinates are selected within the image's dimensions.
  - The RGB value at the chosen coordinates is examined, and counts for India and Punjab are incremented accordingly.
  - Punjab's area is calculated based on the counts and the known area of India.
- **Code Block with Sample Output**:
  ```python
  from PIL import Image
  import numpy as np
  import random

  im = Image.open('map01.png')
  RGB_im = im.convert('RGB')
  
  count_Punjab = 0
  count_India = 0
  count = 0
  
  while count <= 100000:
      x = random.randint(0, 2480)
      y = random.randint(0, 2735)
      z = 0
      
      r, g, b = RGB_im.getpixel((x, y))
      
      if r == 60:
          count_India += 1
      elif r == 80:
          count_Punjab += 1
      count += 1
  
  area_Punjab = (count_Punjab / count_India) * 3287263
  print("Area of Punjab:", area_Punjab)
  ```

**Part 4: Calculating Area Using RGB Values - Pythonic Method**
- **Key Points**:
  - Focuses on computing the RGB values of an image in an automated way without using a color picker.
  - Similar to the previous method but avoids manual identification of RGB values.
  - Presents a Pythonic approach for calculating RGB values.
- **Code Block**:
  ```python
  from PIL import Image
  import numpy as np
  import random

  im = Image.open('map01.png')
  RGB_im = im.convert('RGB')
  
  count_Punjab = 0
  count_India = 0
  count = 0
  
  while count <= 100000:
      x = random.randint(0, 2480)
      y = random.randint(0, 2735)
      z = 0
      
      r, g, b = RGB_im.getpixel((x, y))
      
      if r == 60:
          count_India += 1
      elif r == 80:
          count_Punjab += 1
      count += 1
  
  area_Punjab = (count_Punjab / count_India) * 3287263
  print("Area of Punjab:", area_Punjab)
  ```


Please note that the sample outputs in the code blocks will vary with each run due to the randomized nature of the methods. The provided code is meant to give you a sense of the process for calculating the area of Punjab based on RGB values.

