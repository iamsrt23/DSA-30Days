class Node:
    def __init__ (self,data):
        self.data=data
        self.right = None
        self.left = None


class BinaryTreeToDLL:
    def __init__ (self):
        self.prev = None
        self.next = None

    def binary_Dll(self,root):
        if root is None:
            return
        
        self.binary_Dll(root.left)

        if self.prev is None:
            self.head = root

        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root

        self.binary_Dll(root.right)

    def print_dll(self,head):
        current = head
        while current:
            print(current.data,end="<->")
            current = current.right
        print("None")














root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left=Node(30)
root.right.right = Node(35)

converter = BinaryTreeToDLL()
converter.binary_Dll(root)

# Print the DLL
converter.print_dll(converter.head)