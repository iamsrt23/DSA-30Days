class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__ (self):
        self.head=None

    

    def insert_at_end(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def lengthofll(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next


lst = LinkedList()
lst.insert_at_end(20)
lst.insert_at_end(10)
lst.insert_at_end(30)

# Calculate and display the length of the linked list
print("Length of Linked List:", lst.lengthofll())

# Display the linked list
print("Elements in Linked List:")
lst.display()