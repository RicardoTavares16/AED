from Vertex import Vertex

# Adaptado das aulas de AED

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def calcDist(self,n):
        distance = 0
        for i in range (len(n)-1):
            distance = distance + self.getVertex(n[i]).getWeight(self.getVertex(n[i+1]))
        distance = distance + self.getVertex(n[len(n)-1]).getWeight(self.getVertex(n[0]))
        return distance

    def __contains__(self,n):
         return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def addEdge2(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def getNumVertices(self):
        return self.numVertices

    def __iter__(self):
        return iter(self.vertList.values())

def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph.getVertices() - set(path):

            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
