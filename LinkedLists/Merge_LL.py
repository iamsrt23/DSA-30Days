class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def merge_ll(self,lst1,lst2):
        dummy_node = Node(-1)
        temp = dummy_node

        while lst1 is not None and lst2 is not None:

            if lst1.data <= lst2.data:
                temp.next = lst1
                lst1 = lst1.next

            else:
                temp.next = lst2
                lst2 = lst2.next
        
        
            temp= temp.next
        if lst1 is not None:
            temp.next = lst1

        else:
            temp.next = lst2

        return dummy_node.next
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next



# Create two linked lists
lst1 = LinkedList()
lst2 = LinkedList()

# Insert nodes into lst1 and lst2
lst1.insert(20)
lst1.insert(30)
lst1.insert(40)

lst2.insert(10)
lst2.insert(15)
lst2.insert(45)

# Display lst1 and lst2 before merging
print("List 1 before merging:")
lst1.display()

print("List 2 before merging:")
lst2.display()

# Merge the lists and set the result to lst1
lst1.head = lst1.merge_ll(lst1.head, lst2.head)

# Display the merged list
print("Merged List:")
lst1.display()



