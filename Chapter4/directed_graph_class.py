class Graph:
    def __init__(self) -> None:
        self.vertices = {}

    def add_vertices(self, vertix):
        if vertix not in self.vertices:
            self.vertices[vertix] = []

    def add_edges(self, vertix, edge):
        if vertix in self.vertices and edge in self.vertices:
            self.vertices[vertix].append(edge)

    def remove_vertix(self, vertix):
        if vertix in self.vertices:
            del self.vertices[vertix]
        
            for value in self.vertices.values():
                if vertix in value:
                    value.remove(vertix)

    def get_edges(self):

        edges = []
        for value in self.vertices.values():
            edges.append(for val in value)

        return edges









graph = Graph()

graph.add_vertices('A')
graph.add_vertices('B')
graph.add_vertices('C')
graph.add_vertices('D')

graph.add_edges('A', 'B')
graph.add_edges('A', 'C')

graph.add_edges('B', 'D')
graph.add_edges('B', 'C')

graph.add_edges('C', 'D')

graph.add_edges('D', 'A')

graph.remove_vertix('C')

edges_list = graph.get_edges()
print("edge list:", edges_list)



