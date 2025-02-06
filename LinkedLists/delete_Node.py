class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__ (self):
        self.head = None


    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    

    
    def delete_Node(self,pos):
        if self.head is None:
            return
        
        temp = self.head

        for i in range(pos-1):
            temp = temp.next
            if temp is None:
                return
            next_ptr = temp.next.next

            temp.next = None

            temp.next = next_ptr


    def delete_by_value(self,key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        
        prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ",end=" ")
            temp=temp.next

lst=LinkedList()
lst.insert(12)
lst.insert(8)
lst.insert(10)
lst.delete_by_value(8)



lst.display()



        