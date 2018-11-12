# Python program to find n'th node from end using slow
# and fast pointer
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printNthFromList(self, n):
        main_p = self.head
        ref_p = self.head
        count = 0
        if self.head is not None:
            while count < n:
                if ref_p is None:
                    print("%d is greater than the number of nodes in list" % (n))
                    return
                ref_p = ref_p.next
                count += 1
        while ref_p is not None:
            main_p = main_p.next
            ref_p = ref_p.next
        print("Node number %d from list is: %d" % (n, main_p.data))


# Driver program to test above function
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)

llist.printNthFromList(3)
