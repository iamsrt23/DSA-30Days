class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__ (self):
        self.top = None
        self.size = 0

    
    def is_empty(self):
        return  self.top is None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size +=1

    def pop(self):
        if self.is_empty():
            return None
        
        else:
            poped_data = self.top.data
            self.top = self.top.next
            self.size -=1

            return poped_data
    
    def peek(self):

        if self.is_empty():
            return None
        
        else:
            return self.top.data
        
    
    def get_size(self):
        return self.size
    
    def display(self):
        if self.is_empty():
            return None
        else:
            current = self.top
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            return elements


if __name__ == "__main__":
    stack = Stack()  # Create a new stack

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    print(f"Top element: {stack.peek()}")
    print(f"Popped element: {stack.pop()}")
    stack.display()

    print(f"Stack size: {stack.get_size()}")
    stack.push(40)
    stack.push(50)
    stack.display()
