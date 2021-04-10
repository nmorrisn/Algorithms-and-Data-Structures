class Graph:
    def __init__(self):
        self.nodecount = 0
        self.adjacentlist = {}

    def add_vertex(self, node):
        if node not in self.adjacentlist:
            self.adjacentlist[node] = []
            self.nodecount += 1

    def add_edge(self, node1, node2):
        # not checking if someone already added this but with node2 as node1
        # not checking if node2 already exists in the adjacent list
        if node1 not in self.adjacentlist:
            self.add_vertex(node1)  

        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)

    def __str__(self):
        return str(self.__dict__)


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(3)

graph.add_edge(0,1)
graph.add_edge(0,2)
print(graph)