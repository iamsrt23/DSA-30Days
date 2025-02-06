class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None


    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

root.postorder(root)