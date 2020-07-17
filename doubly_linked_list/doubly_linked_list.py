"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #crete instance of ListNode with value
        new_node = ListNode(value)
        #increment the DLL length attribute
        self.length += 1

        #if DLL is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        #set head and tail to the new node instance

        #if DLL is not empty
        else:
        #set new nodes next to current head
            new_node.next = self.head
        #set heads prev to new node
            self.head.prev = new_node
        #set head to the new node
            self.head = new_node
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #store the value of the head
        thevalue = self.head.value
        #decrement the length of the DLL
        self.length -= 1
        #delete the head
        #if head.next is not None
        if self.head.next is not None:
            self.head.next.prev = None
            self.head = self.head.next
        #set head.nexts prev to NOne
        #set head to head.next
        else:
            self.head = None
            self.tail = None
        #else if head.next is none
        #set head to none
        #set tail to None
        return thevalue
        #retur the value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #crete instance of ListNode with value
        new_node = ListNode(value)
        #increment the DLL length attribute
        self.length += 1

        #if DLL is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        #set head and tail to the new node instance

        #if DLL is not empty
        else:
        #set new nodes prev to current tail
            new_node.prev = self.tail
        #set tails prev to new node
            self.tail.next = new_node
        #set tails to the new node
            self.tail = new_node
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
             #store the value of the tail
        tailvalue = self.tail.value
        #decrement the length of the DLL
        self.length -= 1
        #delete the head
        #if head.next is not None
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        #set head.nexts prev to NOne
        #set head to head.next
        else:
            self.head = None
            self.tail = None
        #else if head.next is none
        #set head to none
        #set tail to None
        return tailvalue
        #retur the value
            
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value1 = node.value
        self.delete(node)
        self.add_to_head(value1)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value2 = node.value
        self.delete(node)
        self.add_to_tail(value2)
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # empty list
        if not self.head:
            print("nothing to delete") 
            return
        #one item in list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        #node is self head
        if node == self.head:
            self.head = node.next
            self.length -= 1
            return
        # node is self.tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
            return
        #other cases
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev     

                self.length -=1       

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        maxvalue = self.head.value
        current = self.head

        while current is not None:
            if current.value > maxvalue:
                maxvalue = current.value
            current = current.next
        return maxvalue