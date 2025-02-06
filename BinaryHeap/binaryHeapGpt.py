class BinaryHeap:
    def __init__(self, capacity, is_min_heap=True):
        """Initialize a binary heap with a fixed size."""
        self.capacity = capacity
        self.size = 0  # Current number of elements
        self.heap = [None] * capacity  # Fixed-size list
        self.is_min_heap = is_min_heap  # True for Min Heap, False for Max Heap

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def compare(self, child, parent):
        """Comparison logic for Min or Max Heap."""
        if self.is_min_heap:
            return self.heap[child] < self.heap[parent]  # Min Heap: child should be smaller
        else:
            return self.heap[child] > self.heap[parent]  # Max Heap: child should be greater

    # -------------- Peek (Get Top Element) --------------
    def peek(self):
        """Return the top element of the heap."""
        if self.size == 0:
            return None
        return self.heap[0]

    # -------------- Insert Value in Binary Heap --------------
    def insert(self, key):
        """Insert a new key into the heap."""
        if self.size == self.capacity:
            print("Heap is full! Cannot insert.")
            return

        self.heap[self.size] = key  # Insert at the end
        self._heapify_up(self.size)  # Restore heap property
        self.size += 1

    def _heapify_up(self, i):
        """Move the element up to restore heap order."""
        while i > 0 and self.compare(i, self.parent(i)):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)  # Move up

    # -------------- Extract Min (For Min Heap) or Extract Max (For Max Heap) --------------
    def extract_top(self):
        """Remove and return the top element (Min for Min Heap, Max for Max Heap)."""
        if self.size == 0:
            return None
        if self.size == 1:
            self.size -= 1
            return self.heap.pop(0)

        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]  # Move last element to root
        self.size -= 1
        self._heapify_down(0)  # Restore heap order
        return root

    def _heapify_down(self, i):
        """Move the element down to restore heap order."""
        smallest_largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < self.size and self.compare(left, smallest_largest):
            smallest_largest = left
        if right < self.size and self.compare(right, smallest_largest):
            smallest_largest = right
        if smallest_largest != i:
            self.heap[i], self.heap[smallest_largest] = self.heap[smallest_largest], self.heap[i]
            self._heapify_down(smallest_largest)  # Recursively heapify down

    # -------------- Traversal of Binary Heap --------------
    def traverse(self):
        """Print all elements in level order."""
        print("Heap:", self.heap[:self.size])

    # -------------- Delete Entire Heap --------------
    def delete_heap(self):
        """Delete the entire heap."""
        self.heap = [None] * self.capacity
        self.size = 0
        print("Heap deleted successfully.")

# ---------------- Example Usage ----------------
print("Creating a Min Heap of size 10...")
heap = BinaryHeap(10, is_min_heap=True)  # Change is_min_heap=False for Max Heap

heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(3)

print("Heap after inserts:")
heap.traverse()

print("Top element:", heap.peek())

print("Extracted top element:", heap.extract_top())
print("Heap after extraction:")
heap.traverse()

heap.delete_heap()