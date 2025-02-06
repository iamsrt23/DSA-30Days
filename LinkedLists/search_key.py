class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__ (self):
        self.head = None


    def insert_at_end(self,data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def search_value(self,value):
        temp = self.head

        while temp:
            if temp.data == value:
                return True
            temp= temp.next
        return False
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp= temp.next

lst = LinkedList()
lst.insert_at_end(20)
lst.insert_at_end(10)
lst.insert_at_end(30)
value=30
if(lst.search_value(value)):
    print(str(value)+" is found")
else:
    print(str(value)+" is not found")

lst.display()
