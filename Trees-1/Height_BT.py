class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def height(self,root):
        if root is None:
            return -1
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1+ max(left_height,right_height)
    


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)  

print(root.height(root))