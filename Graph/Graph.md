# Graph

A Graph is a non-linear DataStructure consists of a finite set of Vertices or Nodes  and a set of Edges which connect pair of nodes.

![Screenshot 2025-01-29 at 10.18.35 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.18.35_AM.png)

**Graph Terminology:**

- **Vertices (Vertex):** Vertices are the nodes of the graph
- **Edge:** The edge is the line that connects pairs of vertices
- **Un weighted Graph:** A graph which does not have a weight associated with any edge
- **Weighted Graph:** A graph which has a weight associated with any edge
- **Un Directed Graph:** In case the edges of the graph do not have a direction associated with them
- **Directed Graph:** if the edges in a graph have a direction associated with them
- **Cyclic Graph:**  A graph which has at least one loop
- **A Cyclic Graph:** A graph with no loop
- **Tree:**  It is a special case of directed acyclic graphs

**Graph Types:**

![Screenshot 2025-01-29 at 10.41.03 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.41.03_AM.png)

- **Unweighted - undirected**

![Screenshot 2025-01-29 at 10.41.53 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.41.53_AM.png)

- **Unweighted - Directed**

![Screenshot 2025-01-29 at 10.42.43 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.42.43_AM.png)

- **Positive - weighted - undirected**

![Screenshot 2025-01-29 at 10.43.40 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.43.40_AM.png)

- **Positive - weighted - directed**

![Screenshot 2025-01-29 at 10.45.05 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.45.05_AM.png)

- **Negative - weighted - undirected**

![Screenshot 2025-01-29 at 10.45.39 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.45.39_AM.png)

- **Negative - weighted -Directed**

![Screenshot 2025-01-29 at 10.46.22 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.46.22_AM.png)

**Graph representation:**

**Adjacency Matrix:** An Adjacency matrix is a square matrix or you can say it is a 2D array, And the elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph

![Screenshot 2025-01-29 at 10.51.53 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.51.53_AM.png)

**Adjacency List:**  An Adjacency list is a collection of unordered list used to represent a graph. Each list describes the set of neighbors of a vertex in the graph.

![Screenshot 2025-01-29 at 10.55.03 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_10.55.03_AM.png)

- If a graph is complete or almost complete we should use Adjacency matrix
- if the number of edges are few then we should use Adjacency List

**Python Dictionary Implementation:**

{ A: [B,C,D],

B: [A,E],

C:[A,D],

D:[A,C,E],

E:[B,D] }

**Create a Grpah and Add Edge and Vertex:**

```python
# Graph 

class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

customDict = {"a":["b","c"],
              "b":["a","d","e"],
              "c":["a","e"],
              "d":["b","e","f"],
              "e":["d","f"],
              "f":["d","e"]
              }

graph = Graph(customDict)
graph.addEdge("e","c")
print(graph.gdict)
```

**Graph Traversal:**

- BFS
    - It is an Algorithm for traversing Graph Data structure . It starts at some arbitary node of a graph and explores the neighbor nodes (which are at current level) first, before moving to the next level neighbors.
        
        ![Screenshot 2025-01-29 at 11.11.13 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_11.11.13_AM.png)
        

```python
# Graph 

class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

# BFS
    def bfs(self,vertex): #time:O(v + E) and space(v+E) v:vertices
        visited = [vertex]
        queue = [vertex]
        while queue:
            dvertex = queue.pop(0)
            print(dvertex)

            for adjacentVertex in self.gdict[dvertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

customDict = {"a":["b","c"],
              "b":["a","d","e"],
              "c":["a","e"],
              "d":["b","e","f"],
              "e":["d","f"],
              "f":["d","e"]
              }

graph = Graph(customDict)
graph.bfs("a")
graph.addEdge("e","c")
print(graph.gdict)
```

- DFS
- It is an Algorithm for traversing a graph data structure which starts selecting some arbitrary node and explores as far as possible along each edge before backtracking.
    
    
    ```python
    # Graph 
    
    class Graph:
        def __init__(self,gdict=None):
            if gdict is None:
                gdict={}
            self.gdict = gdict
    
        def addEdge(self,vertex,edge):
            self.gdict[vertex].append(edge)
            
    		
    # DFS
        def dfs(self,vertex): #time:O(v + E) and space(v+E) v:vertices
            visited = [vertex]
    # stack
            stack = [vertex]
    
            while stack:
                # Last element
                popVertex = stack.pop()
                print(popVertex)
    
                for adjacentVertex in self.gdict[popVertex]:
                    if adjacentVertex not in visited:
                        visited.append(adjacentVertex)
                        stack.append(adjacentVertex)
    
    customDict = {"a":["b","c"],
                  "b":["a","d","e"],
                  "c":["a","e"],
                  "d":["b","e","f"],
                  "e":["d","f"],
                  "f":["d","e"]
                  }
    graph = Graph(customDict)
    graph.addEdge("e","c")
    print("---------DFS----------------")
    graph.dfs("b")
    ```
    

**BFS vs DFS:**

![Screenshot 2025-01-29 at 11.47.22 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_11.47.22_AM.png)

![Screenshot 2025-01-29 at 11.47.32 AM.png](Graph%2018a63324436c80daa127f9d622ae4f98/Screenshot_2025-01-29_at_11.47.32_AM.png)

Graph.py

```python
# Graph 

class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

# BFS
    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            # first element
            dvertex = queue.pop(0)
            print(dvertex)

            for adjacentVertex in self.gdict[dvertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

# DFS
    def dfs(self,vertex):
        visited = [vertex]
# stack
        stack = [vertex]

        while stack:
            # Last element
            popVertex = stack.pop()
            print(popVertex)

            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

customDict = {"a":["b","c"],
              "b":["a","d","e"],
              "c":["a","e"],
              "d":["b","e","f"],
              "e":["d","f"],
              "f":["d","e"]
              }

graph = Graph(customDict)
graph.bfs("a")
graph.addEdge("e","c")
print(graph.gdict)
print("---------DFS----------------")
graph.dfs("b")
```

Graph DFS.py

```python
def dfs(graph,node,visited=set()):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)

dfs(graph,0)
```

Graph_BFS.py

```python
from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            queue.extend(graph[node])
```