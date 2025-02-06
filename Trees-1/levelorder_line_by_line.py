from collections import deque
class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None

    def level_order_line(self,root):
        if root is None:
            return
        
        queue=deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                current_node = queue.popleft()
                print(current_node.data,end=" ")

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            print()


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50) 

root.level_order_line(root)