# Tutorial on How to make a LinkedList in python. We are not using the module LinkedList, rather creating class definition from scratch

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
  def string(self):
    return str(self)


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)

print(first_node.data, first_node.next)