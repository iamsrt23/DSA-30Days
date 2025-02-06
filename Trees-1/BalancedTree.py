class Node:
    def __init__ (self,data):
        self.data=data
        self.right = None
        self.left = None

    
    def is_balanced(self,root):
        if root is None:
            return 0
        
        left_height = self.is_balanced(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.is_balanced(root.right)
        if right_height ==-1:
            return -1
        
        if abs(left_height-right_height) >1:
            return -1
        else:
            return max(left_height,right_height)+1
    


# Example Tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.right.right.right = Node(70)



print(root.is_balanced(root))