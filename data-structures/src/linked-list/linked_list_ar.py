class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None
    
    

class LinedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def get_node(self, index):
        if index < 0 :
            raise ValueError('node indices cannot be 0.')
        else:
            current_node = self.head
            i = 0
            while current_node:
                if i == index:
                    return current_node
                current_node = current_node.next 
                i += 1

            raise IndexError(f"index {index} exceeds the length of linked list {self.get_length}")
        
    def insert_after(self, index, value):
        index_node = self.get_node(index=index)
        new_node = Node(value)

        new_node.next = index_node.next
        index_node.next = new_node
    
    def delete_node(self, key):
        if not self.head:
            return
        
        # if key is in the head itself 
        if self.head.value == key:
            self.head = self.head.next
            return 

        # search key and delete
        prev_node = None 
        current_node = self.head 
        while current_node:
            if current_node.value == key:
                break
            prev_node = current_node
            current_node = current_node.next
        
        if not current_node:
            print(f"key {key} not found in the linked list")
            return 
        prev_node.next = current_node.next
    
    # mainly needed to do the swap 
    def search_nodes(self, key_1, key_2):
        prev_node_k1, prev_node_k2 = None, None
        node_k1, node_k2 = self.head, self.head

        # search for key 1 
        while node_k1 and node_k1.value != key_1:
            prev_node_k1 = node_k1
            node_k1 = node_k1.next
        
        # search for key 2
        while node_k2 and node_k2.value != key_2:
            prev_node_k2= node_k2
            node_k2 = node_k2.next
        
        return prev_node_k1, node_k1, prev_node_k2, node_k2
    
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return 
        prev_node_k1, node_k1, prev_node_k2, node_k2 = self.search_nodes(key_1=key_1, key_2=key_2)

        if node_k1 == None or node_k2 == None:
            return 
        
        # check if prev_node_k1 is not none and assign the next to prev node as node_k2
        if prev_node_k1 is not None:
            prev_node_k1.next = node_k2
        else:
            # make key 2 as the current head 
            self.head = node_k2

        # check if prev_node_k2 is not none and assign the next to prev node as node_k1
        if prev_node_k2 is not None:
            prev_node_k2.next = node_k1
        else:
            # make key 1 as the head 
            self.head = node_k1
        
        node_k1.next, node_k2.next = node_k2.next, node_k1.next

    # https://www.youtube.com/watch?v=X1yXhnks60E
    def reverse(self):
        prev_node = None
        curr_node = self.head 

        while curr_node != None:
            next_node = curr_node.next 
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node =  next_node
        
        self.head = prev_node

    def reverse_recursive(self):

        def rec(prev, curr):
            if not curr:
                return prev 
            tail = rec(curr, curr.next)
            curr.next = prev
            
            return tail 
        
        self.head = rec(None, self.head)

    def has_cycle(self):
        head = self.head 
        if head != None or head.next != None:
            return False
        
        slow = head 
        fast = head.next

        while slow != fast:
            if head != None or head.next !=None:
                return False 
            
            slow = slow.next 
            fast = fast.next.next 
        
        return True

   
    def detect_cycle(self):
        head = self.head 
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Find the intersection point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # If there's no cycle, return None
        if not fast or not fast.next:
            return None

        # Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    

    def display(self, return_elements=False):

        current = self.head
        elements = []
        if not current:
            print("linked list is empty")
            return 

        while current:
            current_value = current.value
            elements.append(current_value)
            current = current.next

        if return_elements:
            return elements 
        else:
            print(elements)
    

    def get_length(self, verbose=True):

        if not self.head:
            print('linked list is empty')
            return
        l = 1
        current_node = self.head
        while current_node.next:
            l += 1
            current_node = current_node.next
        
        if verbose:
            print(f"length of the linked list is: {l}\n")
        return l
        

ll = LinedList()
# print the empty linked list 
ll.display()


# append node 
ll.append('b')
ll.display()

# prepend 
ll.prepend('a')
ll.display()

# append node 
ll.append('d')
ll.display()
# print length of the linked list 
l = ll.get_length()

# get the second node in the linked list 
index = 2  # also test index out of bound of the linked list 
node = ll.get_node(index=index)
print(f"value of index {index} node in the linked-list is: {node.value}")

# insert after a index 
ll.insert_after(1,'c')
ll.display()


# delete a node that matches a key value 
ll.delete_node('e')
ll.display()

# search for two nodes, used mainly in swapping method 
prev_node_k1, node_k1, prev_node_k2, node_k2 = ll.search_nodes('b', 'c')

# swap two nodes 
ll.swap_nodes('b', 'b')
ll.display()

# reverse linked list 
ll.reverse()
ll.display()

# reverse recusively 
ll.reverse_recursive()
ll.display()

ll.append('b')
ll.display()
# check cycle in linked list 
if ll.has_cycle():
    print(f"linked list cycle detected")
else:
    print(f"linked list does not have cyclic pointer")

