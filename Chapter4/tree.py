class TreeNode: 
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class Tree:

    def __init__(self, root=None):
        self.root = root
    
    def creat_tree(self, value):

        if self.root is None:
            if self.root.left is None:
                self.root.left = TreeNode(value)
            elif self.root.right is None:
                self.root.right = TreeNode(value)
        
        self.root.left = self.creat_tree()
        




values = [1,2,3,4,5,6,7,8]

for value in values:
    node = TreeNode()



# node = TreeNode(1)
# node.left = TreeNode(2)
# node.right = TreeNode(3)

    