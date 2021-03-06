from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #get current value of node
        current_value = self.value
        #compare to value to be inserted

        # if new value is less than current value
        if value < current_value:
            #if left side is taken
            if self.left is not None:
                #make that node call insert
                self.left.insert(value)    
            #if left side is not taken insert new node with value in left side
            else:
                self.left = BSTNode(value)
        #if new value is greater or equal to current value
        elif value >= current_value:
            #if right side is taken
            if self.right is not None: 
                #make that node call insert
                self.right.insert(value)
            #if right side is not taken insert new node with value in right side
            else:
                self.right = BSTNode(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        found = False
        if self.value > target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value >= target
        if self.value <= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        #follow tree down entire right side until we find node with no right side
        #if self.right is None
        if self.right is None:
            #return self.value
            max_num = self.value
        #else call get_max function on self.right
        else:
            max_num = self.right.get_max()
        return max_num
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #run function on current nodes value
        fn(self.value)
        #check if there is a right node if so call for_each on that node
        if self.right is not None:
            self.right.for_each(fn)
         #check if there is a left value if so run for_each on that node
        if self.left is not None:
            self.left.for_each(fn)
       
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #check if there is a left node if so call in_order_print with self.left as param
        if node.left is not None:
            value = node.left.in_order_print(node.left)
        #print self.value  
        value = print(node.value)
        #check if there is a right node if so call in_order_print with self.right as param
        if node.right is not None:
            value = node.right.in_order_print(node.right)
        return value

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
    # create a queue for nodes
        queue = Queue()
    # add the first node to the queue
        queue.enqueue(node)
    # while queue is not empty
        while queue.__len__() != 0:
        # remove the first node from the queue
            removed = queue.dequeue()
        # print the removed node 
            print(removed.value)
        # add all children into the queue
            if removed.right is not None:
                queue.enqueue(removed.right)
            if removed.left is not None:
                queue.enqueue(removed.left)
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = Stack()
        # add the first node to the stack
        stack.push(node)
        # while the stack is not empty
        while stack.__len__() != 0:
            # get the current node from the top of the stack
            removed = stack.pop()
            # print that node
            print(removed.value)
            # add all children to the stack
            if removed.right is not None:
                stack.push(removed.right)
            if removed.left is not None:
                stack.push(removed.left)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        #visit node and print out value
        value = print(node.value)
        #if there is a left node call pre_order_dft on that node
        if node.left is not None:
            node.left.pre_order_dft(node.left)
        #if there is a right node call pre_order_dft on that node
        if node.right is not None:
            node.right.pre_order_dft(node.right)
        return value
        

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        #if there is a left node call post_order_dft on that node
        if node.left is not None:
            node.left.post_order_dft(node.left)
        #if there is a right node call post_order_dft on that node
        if node.right is not None:
            node.right.post_order_dft(node.right)
        #print out value of node
        return print(node.value)
