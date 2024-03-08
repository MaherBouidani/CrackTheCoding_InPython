class Node: 
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value



# count = 0

def minimal_tree(array, start, end):
        # global count

        if  start > end:
            return None

        mid = (start + end) // 2

        print(mid)

        node = Node(array[mid])
        # if count == 0: 
        #     print("root node:", node)

        # count += 1

        node.left = minimal_tree(array, start, mid - 1)
        node.right = minimal_tree(array, mid+1, end)

        return node

    # def print_tree()



# class Tree(Node):
#     def __init__(self, root=None):
#         self.root = root

#     def print_node(self):
#         return self.root.value, self.root.left.value, self.root.right.value


array = [1,2,3,4,5,6,7,8]

root = minimal_tree(array,0,len(array)-1)

hash_table = {}
hash_table[1] = []
def traverse(root_node):
    global hash_table

    

    #termination condition
    if root_node is None: 
        return None


    #recursive call
    print(root_node.value)
    hash_table[1].append(root_node.value)
    print(hash_table)
    root_node_left = traverse(root_node.left)
    root_node_right = traverse(root_node.right)

    return root_node_left, root_node_right


traverse(root)



    
        




