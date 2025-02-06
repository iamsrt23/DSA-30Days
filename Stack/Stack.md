# Stack

It is a Data Structure that stores items in a Last-in/First-out Manner.(LIFO)

ex: Pile of plates, books and Bangles

**Why Stack?**

- Back Button in Browser

**Stack Operations:**

- Create Stack —> customStack = []
- Push —>  customStack.push(1)
- Pop —>  customStack.pop() → remove top element
- Peek—>  customStack.peek() —>shows  top element
- isEmpty →  customStack.isEmpty() —> True or False
- isFull →  customStack.isFull() —> True or False(if size limit)
- deleteStack → customStack .delete()

**Stack Creation:**

Stack using List:

- Easy to implement
- Speed problem when it grows

Stack using LinkedList:

- Fast Performance
- Implementation is not easy

```python
# Create Stack using Python Lists

class Stack:
    def __init__(self): # time:O(1) and space:O(1)
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    

```

**Stack Methods:**

```python
# Create Stack using Python Lists

class Stack:
    def __init__(self): # time:O(1) and space:O(1)
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    

    # isEmpty

    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
        
    # Push

    def push(self,value):# time:O(1) and space:O(1)
        self.list.append(value)
        return "The element is added successfully"
        

    # pop

    def pop(self):# time:O(1) and space:O(1)
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        
    # peek

    def peek(self):# time:O(1) and space:O(1)
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]
    # delete
    def delete(self):# time:O(1) and space:O(1)
        self.list = None
        
    

customStack= Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)

print("The pop value is ")
print(customStack.pop())
print("The peek value is ")
print(customStack.peek())

```

**Stack With Limited Size:**

```python
class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list=[]

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # isFull

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #push

    def push(self,value):
        if self.isFull():
            return "The stack is Full"
        
        else:
            self.list.append(value)
            return "The element is Added Succesfully"
        
    
    # pop()
    def pop(self):
        if self.isEmpty():
            return "There is no Element in the stack"
        else:
            return self.list.pop()
        
    # peek()

    def peek(self):
        if self.isEmpty():
            return "There is no Element in the stack"
        else:
            return self.list(len(self.list)-1)
        
    # delete

    def delete(self):
        self.list = None
        
         
        

customStack = Stack(5)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

    

```

![Screenshot 2025-01-22 at 5.33.26 PM.png](Stack%2018363324436c805a81fadae1ea827205/Screenshot_2025-01-22_at_5.33.26_PM.png)

**Stack Using Linked List:**

- Create a Stack
- Create an Object of Linked List Class  [head|null]
    - push(head will be updated)
    - pop(head will be updated)
    - peek(returns the Head value)
    - isEmpty(Head is None)
    - delete(head=None)
    
    ```python
    class Node:
        def __init__(self,value=None):
            self.value = value
            self.next = next
    
    class LinkedList:
        def __init__(self):
            self.head = None
    
        def __iter__(self):
            curNode = self.head
            while curNode:
                yield curNode
                curNode = curNode.next
    
    class Stack:
        def __init__(self):
            self.LinkedList = LinkedList()
    
        def __str__(self):
            values = [str(x.value) for x in self.LinkedList]
            return "\n".join(values)
    
        # isEmpty
        def isEmpty(self):
            if self.LinkedList.head == None:
                return True
            else:
                return False
            
    
        # push
        def push(self,value):
            node = Node(value)
            node.next = self.LinkedList.head
            self.LinkedList.head = node
    
        # pop
        def pop(self):
            if self.isEmpty():
                return "There is No element in the stack"
            
            else:
                nodeValue = self.LinkedList.head.value
                self.LinkedList.head = self.LinkedList.head.next
                return nodeValue
        # peek
        def peek(self):
            if self.isEmpty():
                return "There is No element in the stack"
            else:
                nodeValue = self.LinkedList.head.value
                return nodeValue
        # delete
        def delete(self):
            self.LinkedList.head = None
    
            
        
    
    customStack=Stack()
    print(customStack.isEmpty())
    customStack.push(1)
    customStack.push(2)
    customStack.push(3)
    print(customStack)
    print("---------------")
    customStack.pop()
    print(customStack)
    print("---------------")
    print(customStack.peek())
    ```
    

![Screenshot 2025-01-22 at 6.07.53 PM.png](Stack%2018363324436c805a81fadae1ea827205/Screenshot_2025-01-22_at_6.07.53_PM.png)

**When To use /Avoid Stack:**

**Use:**

- LIFO functionality
- The Chance of data corruption is Minimum

**Avoid:**

- Random Access is not possible (data size increase becomes problem)