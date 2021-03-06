# Week 6 - 12) Implement TREE_SORT algorithm in a language of your choice, but
#              make sure that the INORDER function is implemented iteratively.

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
def tree_insert(tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def post_order(tree):
    if(tree.left!=None):
        post_order(tree.left)
    if(tree.right!=None):
        post_order(tree.right)
    print(tree.value)

'''
RECURSIVE IN_ORDER
------------------
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)
'''

########################
## Iterative In Order ##
########################
def in_order(tree):
    '''Sorts a Binary Tree Structure so that it is designed in to be in
accending order.'''                                                       # Example: n=2
    # Assigns an empty array as a stack.
    stack = []                                                            # O(1) --> O(1)

    while True:                                                           # O(n) --> O(2)

        if tree != None:                                                  # O(n) --> O(2)
            # Append the value of the tree to the stack.
            stack.append(tree)                                            # O(n) --> O(2)

            # Set the value of the tree to the left node.
            tree = tree.left                                              # O(n) --> O(2)
        else:                                                             # O(n) --> O(2)
            if tree == None and len(stack) > 0:                           # O(n) --> O(2)
                # Set the tree to the popped item.
                tree = stack.pop()                                        # O(n) --> O(2)

                # Print the current value of the tree.
                print(tree.value)# O(n) --> O(2)

                # Set the tree to the right node.
                tree = tree.right                                         # O(n) --> O(2)

                # Return to the start of the loop.
                continue                                                  # O(n) --> O(2)
            
            if tree == None and len(stack) == 0:                          # O(n) --> O(2)
                # Break out of the loop as sort is complete.
                break                                                     # O(n) --> O(2)

def tree_sort(array):
    tree = None
    for number in array:
        tree = tree_insert(tree, number)

    print("IN-ORDER")
    in_order(tree)
    
    print("\nPOST-ORDER")
    post_order(tree)

if __name__ == '__main__':
    while True:
        try:
            # Create an integer array and store in a tree.           
            array = input("Enter an array of integers (seperated by ','): ").split(",")
            array = [int(n) for n in array]
            # Sort the tree and get the results from this.
            tree_sort(array)
        except:
            break

