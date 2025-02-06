# Single Source Shortest Path Problem

class Graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


# BFS   
    def bfs(self,start,end):
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