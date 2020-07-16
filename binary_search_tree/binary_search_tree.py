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
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.value = value
        if len(self.storage) == 0:
            self.size += 1
            self.storage.append(value)
        else:
            self.size += 1
            self.storage.append(self.value)
    
        return self.size

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.pop()
        else:
            return None
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.value = value
        if len(self.storage) == 0:
            self.size = self.size + 1
            self.storage.append(value)
        else:
            self.size += 1
            self.storage.append(self.value)
        
        return self.size

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #case1 value is less than self value
        if value < self.value:
            #If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                #repeat the process for left subtree
                self.left.insert(value)

        #case2 value is greater than self value
        elif value >= self.value:
            #if there is no right child inser value there
            if self.right is None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #case 1 if self.value equals target
        if self.value == target:
            return True
        #case2 if target is less than self.value
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        #case3 otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        maxvalue = self.value
        current = self
        if not self:
            return None
        while current is not None:
            if current.value > maxvalue:
                maxvalue = current.value
            current = current.right
        return maxvalue

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #if the current node is None
        #we know we ave reached the end of a recursion
        #(base case) we want to return
        if self is None:
            return

        #check if we can "move left"
        if self.left is not None:
            self.left.in_order_print(node)

        print(self.value)

        #visit the node by printing it's value
        #check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
         # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"               ​
        # start by placing the root in the queue
        queue = Queue()
        queue.enqueue(node)
        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        while queue.size > 0:

            # dequeue item from front of queue
            
            current= queue.dequeue()
            # print items value
            print(current.value)

            # place current item's left node in queue if not None
            if current.left is not None:
                queue.enqueue(current.left)
            # place current item's right node in queue if not None
            if current.right is not None:
                queue.enqueue(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        # initialize an empty stack
        # push the root node onto the stack
        # need a while loop to manager our iteration
        while stack.size > 0:
        # if stack is not empty enter the while loop
            current = stack.pop()
            # pop top item off the stack
            print(current.value)
            # print that item's value
            if current.right:
                stack.push(current.right)
            # if there is a right subtree
                # push right item onto the stack
            if current.left:
                stack.push(current.left)
            # if there is a left subtree
                # push left item onto the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass