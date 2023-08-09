# class Graph:
#     def __init__(self) -> None:
#         self.vertices = {}

#     def add_vertices(self, vertix):
#         if vertix not in self.vertices:
#             self.vertices[vertix] = set()

#     def add_edges(self, vertix, edge):
#         if vertix in self.vertices and edge in self.vertices:
#             self.vertices[vertix].add(edge)

#     def remove_vertix(self, vertix):
#         if vertix in self.vertices:
#             del self.vertices[vertix]
        
#             for value in self.vertices.values():
#                 if vertix in value:
#                     value.remove(vertix)
    
#     def dfs_helper(self, vertix, visited):
#         print(".............................")
#         print("visited BEFORE ADD", visited)
#         if vertix not in visited:
#             visited.add(vertix)
        
#         print("visited AFTER ADD", visited)
#         print(".............................")
        
#         for neighbour in self.vertices[vertix]:
#             if neighbour not in visited:
#                 self.dfs_helper(neighbour, visited)



#     def dfs_traversal(self, vertix):
#         visited = set()

#         self.dfs_helper(vertix, visited)

#         print(visited)










# graph = Graph()

# graph.add_vertices('A')
# graph.add_vertices('B')
# graph.add_vertices('C')
# graph.add_vertices('D')

# graph.add_edges('A', 'B')
# graph.add_edges('A', 'C')

# graph.add_edges('B', 'D')
# graph.add_edges('B', 'C')

# graph.add_edges('C', 'D')

# graph.add_edges('D', 'A')

# graph.dfs_traversal('A')


# print(graph.vertices)

# def make_list(num): 
#     if num == 1:        
#         return 1    
#     return [num].append(make_list(num - 1))
	    
        
            
    # print(make_list(5))

# s = [1]
# s.append(3)

# print(s)
# s = [[1,0], [2,3], [4,5]]

# for row, item in s:
#     print("row:", row, "....", "item:", item)

# from collections import defaultdict


# dictionary = defaultdict(list)

# dictionary[0].append(1)

# for item in dictionary[2]:
#     print("I am here")

# print(dictionary)

list_test = [1,2,3,4]

print(list_test[len(list_test) - 1])






