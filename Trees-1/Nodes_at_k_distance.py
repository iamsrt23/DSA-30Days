class Node:
    def __init__ (self,data):
        self.data= data
        self.right = None
        self.left = None

    def node_at_k(self,root,k):
        if root is None:
            return 
        if k == 0 :
            print(root.data,end=" ")
        else:
            self.node_at_k(root.left,k-1)
            self.node_at_k(root.right,k-1)

    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

root.node_at_k(root,1)