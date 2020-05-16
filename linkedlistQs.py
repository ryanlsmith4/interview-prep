# Copied from the LL from another class but rotate method is on 31


class Node():

    def __init__(self, data):
        self.next = None
        self.data = data

    def update(self, newData):
        self.data = newData

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

        newNode = Node(data)

        if(self.size == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

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
        currHead = self.head.next
        previous = self.head
        for i in range(k - 1):
            previous = currHead
            currHead = currHead.next
        self.tail.next = self.head
        self.head = currHead
        self.tail = previous
        self.tail.next = None

    def findIndexOfNode(self, find):
            if(find > self.size-1):
                print("Doesn't exist in LinkedList")
                return None

            index = self.head
            for _ in range(find):
                index = index.next

            return index

    def findMiddle(self):
            if self.size % 2 == 0:
                raise ValueError('List size not odd')
            return self.findIndexOfNode(self.size//2)



if __name__ == '__main__':
    ll = LinkedList([11,22,33,44,55,66,77])
    print(ll)
    ll.rotate(16)
    print(ll)
    print(ll.findMiddle())
