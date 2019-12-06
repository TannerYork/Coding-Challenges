# Reverse Linked List from Ryan Hopkins #

# Given a linked list, reverse the list inplace.

### SOLUTION ###
# The solution below is O(n) time complexity and O(1) space complexity

def reverse_linked_list(linked_list):
    prev_node = None
    node = linked_list.head
    next_node = node.next
    while node is not linked_list.tail:
        node.next = prev_node
        prev_node = node
        node = next_node
        next_node = node.next
    node.next = prev_node
    linked_list.head, linked_list.tail = linked_list.tail, linked_list.head


### TESTING ###

class Node():
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = Node(item)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

reverse_linked_list(linked_list)
node = linked_list.head
while node is not None:
    print(node.data)
    node = node.next