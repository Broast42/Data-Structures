"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # add 1 to length
        #if head and tail is none create new node and set to both head and tail
        #else self.head = self.head.insert_before(value)
        pass

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #if no head or tail return none
        #otherwise subtract 1 from length
        #create a var to link to current self.head node
        #then change head pointer self.head = self.head.next
        #then delete the node that is linked to var by using the var
        pass

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # add 1 to length
        #if head and tail is none create new node and set to both head and tail
        #else self.tail = self.tail.insert_after(value)
        pass

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #if no head or tail return none
        #otherwise subtract 1 from length
        #create a var to link to current self.tail node
        #then change tail pointer self.tail = self.tail.prev
        #then delete the node that is linked to the var
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #create var to link to current head var_node = self.head
        #create a second var to link to incoming node new_node
        #delete node node.delete
        #set head pointer to new node self.head = new_node
        #set new_node.prev to none and new_node.next to var_node
        #set var_node.prev to new_node
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        #create var to link to tail node var_node = self.tail
        #create a second var to link to incoming node new_node
        #delete node node.delete
        #set tail pointer to new node self.tail = new_node
        #set new_node.next to none and new_node.prev to var_node
        #set var_node.next to new_node
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        #subtract 1 from length
        #if self.head = node 
            # self.head = self.head.next
            # self.head.prev = None
            #node.next = None
        #else if self.tail = Node
            #self.tail = self.tail.prev
            #self.tail.next = None
            #node.prev = None
        #else node.delete
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        #if self.head is None return 0
        #create curent value var
        #creat max num var
        #while current_var is not None
            #if current_var.value is greater than max_num
                #max_num = curent_var.value
            #current_var = current_var.next
        #return max_num
        pass
