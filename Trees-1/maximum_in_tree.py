class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None
    def maximum(self,root):
        if root is None:
            return float('-inf')
        
        left_max = self.maximum(root.left)
        right_max = self.maximum(root.right)

        return max(root.data,left_max,right_max)


# Example Tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)


print(root.maximum(root))