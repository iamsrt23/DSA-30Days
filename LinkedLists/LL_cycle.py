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

    def ll_cycle(self):
        slow,fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next



# Create a linked list and perform operations
lst = LinkedList()
lst.insert_at_end(20)
lst.insert_at_end(10)
lst.insert_at_end(30)
lst.insert_at_end(25)
lst.insert_at_end(20)
lst.insert_at_end(54)
lst.insert_at_end(10)

# Create a cycle for testing
# Uncomment the next two lines to introduce a cycle
# temp = lst.head
# while temp.next: temp = temp.next
# temp.next = lst.head.next  # Creating a cycle

print("Cycle Detected:", lst.ll_cycle())

# Display the linked list (works only if no cycle exists)
lst.display()
