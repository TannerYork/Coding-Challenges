# Evaluate if a binary tree is a binary search tree Problem from Ryan Hopkins #

# Given the root node of a binary three, check if the binary tree is a binary 
# search tree.


### SOLUTION ###
# The solution below uses in-order traversal to loop through all the nodes in the tree (as
# if looping through an ordered list) and makes sure the previous node is not greater than 
# the current. If it is, then return false because that makes the tree not a binary search
# tree.
def is_bst(root, prev_node=None):
    if root is None:
        return True
    left = is_bst(root.left, prev_node)
    if prev_node is not None:
        if prev_node.value > root.value:
            return False
    prev_node = root
    right = is_bst(root.right, prev_node)
    return left and right


### TESTING ###
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
node8 = Node(8)
node12 = Node(12)
root.left = node8
root.right = node12

# Left side of tree
node11 = Node(11)
node13 = Node(13)
node12.left = node11
node12.right = node13

# Right side of tree
node7 = Node(7)
node9 = Node(9)
node8.left = node7
node8.right = node9

if __name__ == '__main__':
    print(is_bst(root)) # True