
class bst:
    def __init__(self, data=None):
        self.data = data 
        self.left = None
        self.right = None 
        self.max_depth = 0
    

    def insert(self, data):
        # return if the data is the root node 
        if self.data == data:
            return 
        
        # if empty bst set the initial data 
        if self.data == None:
            self.data =  data
            return
        
        # search the left branch if the data is less than root_node value 
        if data < self.data:
            if self.left == None:
                self.left = bst(data)
            else:
                self.left.insert(data)
        
        else:
            if self.right == None:
                self.right = bst(data)
            else:
                self.right.insert(data)
        
    def search(self, data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left != None:
                return self.left.search(data)
            else:
                return False
        
        else:
            if self.right != None:
                return self.right.search(data)
            else: 
                return False
    
    def in_order_traversal(self):
        """Left->Root->Right"""
        elements = []

        # go to left branch of the tree 
        if self.left != None:
            elements += self.left.in_order_traversal()
        
        # append the root node 
        elements.append(self.data)

        # go to the right branch of the tree 
        if self.right != None:
            elements += self.right.in_order_traversal()
        
        return elements

    
    def pre_order_traversal(self):
        """Root->Left->Right"""

        elements = []

        # append the root node 
        elements.append(self.data)

        # go to left branch of the tree 
        if self.left != None:
            elements += self.left.in_order_traversal()

        # go to the right branch of the tree 
        if self.right != None:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        """Left->Right->Root"""

        elements = []

        # go to left branch of the tree 
        if self.left != None:
            elements += self.left.in_order_traversal()

        # go to the right branch of the tree 
        if self.right != None:
            elements += self.right.in_order_traversal()
        

        # append the root node 
        elements.append(self.data)

        return elements

    def get_min(self):
        if self.left == None:
            return self.data 
        else:
            return self.right.get_min()
    
    def get_max(self):
        if self.right == None:
            return self.data 
        else:
            return self.right.get_max()
        
    def total_sum(self):
       
       # base case for recursive 
       if self == None:
           return 0

        # left tree sum 
       if self.left != None:
          left_sum = self.left.total_sum()
       else:
           left_sum = 0
           
        # right tree sum 
       if self.right != None:
           right_sum = self.right.total_sum()
       else:
           right_sum = 0

        # add root to left and right sums
       total = left_sum + self.data + right_sum

       return total
   
    def delete(self, value):
        # if data is less than root node, recursively go to left tree to delete 
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        # if the value in the right tree 
        if value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        
        else:
            if self.left is None and self.right is None: 
                return None
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            
            # find min in the right branch set as root node and delete the right node
            min_val = self.right.get_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
            
            # or alternatively find the max in the left nodes set as root node and delete the left node 

            # max_val = self.left.find_max()
            # self.data = max_val
            # self.left = self.left.delete(max_val)
            
        return self 
        
    def get_max_depth(self):
        """Recursively calculate the maximum depth of the node"""
        if self.left is None and self.right is None:
            self.max_depth = 1
            return self.max_depth
        elif self.left is None:
            self.max_depth = self.right.get_max_depth() + 1
            return self.max_depth
        elif self.right is None:
            self.max_depth = self.left.get_max_depth() + 1
            return self.max_depth
        else:
            left_depth = self.left.get_max_depth()
            right_depth = self.right.get_max_depth()
            self.max_depth = max(left_depth, right_depth) + 1
            return self.max_depth
        
        
    


bt = bst()

# inserts 
bt.insert(10)
bt.insert(5)
bt.insert(15)



# traversals 
print(f"in-order-traversal: {bt.in_order_traversal()}")
print(f"pre-order-traversal: {bt.pre_order_traversal()}")
print(f"post-order-traversal: {bt.post_order_traversal()}")


# total sum 
print(f"total sum in the binary tree: {bt.total_sum()}")


bt.insert(20)
print(f"in-order-traversal: {bt.in_order_traversal()}")
bt.delete(20)
print(f"in-order-traversal: {bt.in_order_traversal()}")

bt.insert(20)
print(f"max depth of the binary search tree: {bt.get_max_depth()}")