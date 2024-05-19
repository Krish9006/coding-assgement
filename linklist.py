class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if self.head is None:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current.next is None:
            raise IndexError("Index out of bounds")
        current.next = current.next.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def rotate_right(self, k):
        if not self.head or k <= 0:
            return
        size = self.size()
        k = k % size
        if k == 0:
            return
        
        old_tail = self.head
        for _ in range(size - 1):
            old_tail = old_tail.next
        old_tail.next = self.head  # Make it circular
        
        new_tail = self.head
        for _ in range(size - k - 1):
            new_tail = new_tail.next
        self.head = new_tail.next
        new_tail.next = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge(self, other):
        if not self.head:
            self.head = other.head
            return
        if not other.head:
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other.head

    def interleave(self, other):
        dummy = Node()
        tail = dummy
        current1, current2 = self.head, other.head
        while current1 or current2:
            if current1:
                tail.next = current1
                current1 = current1.next
                tail = tail.next
            if current2:
                tail.next = current2
                current2 = current2.next
                tail = tail.next
        self.head = dummy.next

    def find_middle(self):
        if not self.head:
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def index_of(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def split_at_index(self, index):
        if index <= 0 or not self.head:
            return LinkedList(), self
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                break
            current = current.next
        second_half = LinkedList()
        second_half.head = current.next
        current.next = None
        return self, second_half

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)

# Example usage
if __name__ == "__main__":
    # Create a new linked list and test the functions
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("Original list:", ll)

    # Insert at index
    ll.insert_at_index(1, 4)
    print("After insert:", ll)

    # Delete at index
    ll.delete_at_index(2)
    print("After delete:", ll)

    # Size of the list
    print("Size:", ll.size())

    # Check if the list is empty
    print("Is empty:", ll.is_empty())

    # Rotate the list to the right by 2 positions
    ll.rotate_right(2)
    print("After rotate:", ll)

    # Reverse the list
    ll.reverse()
    print("After reverse:", ll)

    # Append and prepend
    ll.append(5)
    ll.prepend(0)
    print("After append and prepend:", ll)

    # Merge two lists
    ll2 = LinkedList()
    ll2.append(6)
    ll2.append(7)
    ll.merge(ll2)
    print("After merge:", ll)

    # Interleave two lists
    ll3 = LinkedList()
    ll3.append(8)
    ll3.append(9)
    ll.interleave(ll3)
    print("After interleave:", ll)

    # Find the middle element
    print("Middle element:", ll.find_middle())

    # Find the index of an element
    print("Index of 4:", ll.index_of(4))

    # Split the list at index
    first_half, second_half = ll.split_at_index(3)
    print("First half:", first_half)
    print("Second half:", second_half)
