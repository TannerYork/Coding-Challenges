# Find Middle Node In Limked List Problem from Ryan Hopkins #

# Given the first node in a linked list, find the middle node of the list.
# if the list is even, return the first node of the two middle nodes.


### SETUP ###
import math

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

### SOLUTION ###
# The below solution words in O(n) time complexity, however, the space compexity is also O(N)
# This can be improved by making the two functions work iteratively instead of recurcively
def total_nodes(node, total=1):
    '''Recurcively add the total nodes in the linked list'''
    print(node.val, node.next)
    if node.next is None:
        print(total)
        return total
    total_nodes(node.next, total+1)

def middle_node(node, total, index=1):
    '''Recurcively traverse the linked list to find the middle node'''
    if node.next is None and index is 1:
        return node
    elif total % 2 == 0 and index == total/2:
        return node
    elif total % 2 != 0 and index == math.ceil(total/2):
        return node
    middle_node(node.next, index+1, total)