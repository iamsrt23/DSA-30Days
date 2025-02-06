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