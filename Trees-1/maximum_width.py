from collections import deque
class Node:
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None

    def width_of_tree(self,root):
        if root is None:
            return
        
        queue = deque([root])
        max_width =0

        while queue:
            size = len(queue)
            max_width=max(max_width,size)
            
            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return max_width
            
        

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.right.right.right = Node(70)

print(root.width_of_tree(root))