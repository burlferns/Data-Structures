import sys
# sys.path.append('../queue_and_stack')
sys.path.append('/Volumes/ST5/DB/OL/CI-LambdaSchool/myGitPrj/unit06/3-DataStructures/Data-Structures/queue_and_stack')
# from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self

        while (value >= current_node.value and current_node.right != None) or \
            (value < current_node.value and current_node.left != None):
            if value >= current_node.value: # Handles > & =
                current_node = current_node.right
            else:
                current_node = current_node.left
        
        if value >= current_node.value: # Handles > & =
            current_node.right = BinarySearchTree(value)
            return
        if value < current_node.value:
            current_node.left = BinarySearchTree(value)
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self

        while (target > current_node.value and current_node.right != None) or \
            (target < current_node.value and current_node.left != None):
            if target > current_node.value: 
                current_node = current_node.right
            else:
                current_node = current_node.left

        if target == current_node.value:
            return True
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self

        while current_node.right != None:
            current_node = current_node.right
            
        return current_node.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current_node = stack.pop()
            cb(current_node.value)
            if current_node.right != None:
                stack.push(current_node.right)
            if current_node.left != None:
                stack.push(current_node.left)
     

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
