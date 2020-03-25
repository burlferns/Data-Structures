# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Base cases
        if value >= self.value and self.right == None: # Handles > & =
            self.right = BinarySearchTree(value)
            return
        if value < self.value and self.left == None:
            self.left = BinarySearchTree(value)
            return
    
        # Recursion calls
        if value >= self.value and self.right != None: # Handles > & =
            self.right.insert(value)
        elif value < self.value and self.left != None:
            self.left.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if target == self.value:
            return True
        if target > self.value and self.right == None:
            return False
        if target < self.value and self.left == None:
            return False

        #Recursion calls
        if target > self.value and self.right != None:
            return self.right.contains(target)
        if target < self.value and self.left != None:
            return self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # Base case
        if self.right == None:
            return self.value

        #Recursion calls
        if self.right != None:
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Always Do
        cb(self.value)

        # Base case
        if self.left == None and self.right == None:
            return

        # Recursion calls
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
