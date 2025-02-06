class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None

    def size(self,root):
        if root is None:
            return 0
        
        return 1+self.size(root.left)+self.size(root.right)
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print(root.size(root))