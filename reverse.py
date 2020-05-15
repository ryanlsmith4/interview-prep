

# Copied from the LL from another class but rotate method is on 31


class Node():

    def __init__(self, data):
        self.next = None
        self.data = data

    def update(self, new_data):
        self.data = new_data

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList():

    def __init__(self, items = None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.iter = None
        self.size = 0
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        return 'LinkedList({!r})'.format(self.items())

    def append(self, data):

        new_node = Node(data)

        if(self.size == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def items(self):
        items = []  
        node = self.head 
        while node is not None: 
            items.append(node.data)  
            node = node.next  
        return items 

    def rotate(self, k):
        k %= self.size
        if k == 0:
            return
        curr_head = self.head.next
        previous = self.head
        for i in range(k - 1):
            previous = curr_head
            curr_head = curr_head.next
        self.tail.next = self.head
        self.head = curr_head
        self.tail = previous
        self.tail.next = None


if __name__ == '__main__':
    ll = LinkedList([11,22,33,44,55,66,77])
    print(ll)
    ll.rotate(16)
    print(ll)