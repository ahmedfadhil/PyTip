from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:
    # Graph constructor
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # DFS function
    def DFS(self, v):
        # Mark all vertices as not visited
        visited = [False] * (len(self.graph))
        # Call the recursive helper
        self.DFSUtil(v, visited)


gr = Graph()
gr.addEdge(0, 1)
gr.addEdge(0, 2)
gr.addEdge(1, 2)
gr.addEdge(2, 3)
gr.addEdge(3, 3)

gr.DFS(0)
