# Topological Sort

Sorts given actions in such a way that if there is a dependency of one action on another, then the dependent action always comes later than its parent action.

![Screenshot 2025-01-30 at 10.26.36 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_10.26.36_AM.png)

![Screenshot 2025-01-30 at 10.33.34 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_10.33.34_AM.png)

```python
# Topological Sort

from collections import defaultdict
class Graph:
    def __init__(self,numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    # Topolgocal Sort

    def topologicalSortUtil(self,v,visited,stack): #time:O(V+E) and space:O(V+E)
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)
        print(stack)

customGraph = Graph(8)
customGraph.addEdge("A","C")
customGraph.addEdge("C","E")
customGraph.addEdge("E","H")
customGraph.addEdge("E","F")
customGraph.addEdge("F","G")
customGraph.addEdge("B","C")
customGraph.addEdge("B","D")
customGraph.addEdge("D","F")
 
customGraph.topologicalSort()
```

# Single Source Shortest Path Problem

A single source problem is about finding a path between a given vertex (called source) to all other vertices in a graph such that the total distance between them (source and destination) is minimum.

The Problem:

- Five offices in different cities.
- Travel costs between these cities are known.
- Find the cheapest way from head office to branches in different cities

![Screenshot 2025-01-30 at 10.54.13 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_10.54.13_AM.png)

solution

![Screenshot 2025-01-30 at 10.54.53 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_10.54.53_AM.png)

- BFS {Level Order Traversal}

![Screenshot 2025-01-30 at 10.56.54 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_10.56.54_AM.png)

![Screenshot 2025-01-30 at 11.01.45 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_11.01.45_AM.png)

```python
# Single Source Shortest Path Problem

class Graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

# BFS   
    def bfs(self,start,end):#time:O(E) and space:O(E)
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path
            for adjacent in self.gdict.get(node,[]):
                newPath = list(path)
                newPath.append(adjacent)
                queue.append(newPath)

customDict = {"a":["b","c"],
              "b":["d","g"], 
              "c":["e","d"],
              "d":["f"],
              "e":["f"],
              "g":["f"]

}

g = Graph(customDict)
print(g.bfs("a","f"))
```

![Screenshot 2025-01-30 at 11.13.53 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_11.13.53_AM.png)

![Screenshot 2025-01-30 at 11.15.34 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_11.15.34_AM.png)

- DFS has a tendency to go “as far as possible” from source , hence it can never find “Shortest Path” so SSSP does not work with DFS.

- Dijkstra’s Algorithm
    
    ![Screenshot 2025-01-30 at 11.38.50 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_11.38.50_AM.png)
    

![Screenshot 2025-01-30 at 11.39.48 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_11.39.48_AM.png)

![Screenshot 2025-01-30 at 11.42.02 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_11.42.02_AM.png)

![Screenshot 2025-01-30 at 11.44.53 AM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_11.44.53_AM.png)

```python
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances = {}

    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode,toNode)] = distance

def dijkstra(graph,initial):
    visited = {initial :0}
    path = defaultdict(list)

    nodes=set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode,edge)]
            if edge not in visited or weight<visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

        return visited, path
    
customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A","B",2)
customGraph.addEdge("A","C",5)
customGraph.addEdge("B","D",1)
customGraph.addEdge("B","C",6)
customGraph.addEdge("B","E",3)
customGraph.addEdge("C","F",8)
customGraph.addEdge("D","E",4)
customGraph.addEdge("E","G",9)
customGraph.addEdge("F","G",7)

print(dijkstra(customGraph,"A"))
```

- Bellman Ford

![Screenshot 2025-01-30 at 12.27.06 PM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_12.27.06_PM.png)

Bellman Ford Algorithm is used to find single source shortest path problem. if there is a negative cycle it catches it and report its existence.

positive cycle

![Screenshot 2025-01-30 at 12.29.43 PM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_12.29.43_PM.png)

![Screenshot 2025-01-30 at 12.30.30 PM.png](Topological%20Sort%2018b63324436c8068bfbac4eb10b224dd/Screenshot_2025-01-30_at_12.30.30_PM.png)

Negative Cycle: