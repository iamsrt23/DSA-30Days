class stack:
    def __init__ (self,capacity):
        self.stack=[]
        self.capacity = capacity
    

    def is_empty(self):
        return len(self.stack) == 0


    def is_full(self):
        return len(self.stack) == self.capacity
    
    def push(self,item):
        
        if self.is_full():
            print("stack is full")

        else:
            return self.stack.append(item)
            
    

    def pop(self):

        if self.is_empty():
            print("Stack is empty")
            
            return None

        else:

            return self.stack.pop()
        
    
    def peek(self):

        if self.is_empty():
            print("Stack is empty")
            
            return None
        else:
            return self.stack[-1]
        
    
    def size(self):
        return len(self.stack)
    
    def display(self):

        if self.is_empty():
            print("Stack is empty")

        else:
            return self.stack[::-1]
        

if __name__ == "__main__":
    stack = stack(5)  # Create a stack with a capacity of 5

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    print(f"Top element: {stack.peek()}")
    print(f"Popped element: {stack.pop()}")
    stack.display()

    print(f"Stack size: {stack.size()}")
    stack.push(40)
    stack.push(50)
    stack.push(60)
    stack.push(70)  # This should trigger a Stack Overflow
    stack.display()

         