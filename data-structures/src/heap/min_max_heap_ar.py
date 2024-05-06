
# min heap is like a tree structure, where the values in the tree goes from minimum to maximum from top to down and from left to right 
# heap can basically be in a array 
# where root node can be (index-1)//2, left node: 2*index +1 right node = 2*index+2

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def get_parent_index(self, index):
        return (index-1)//2
    
    def get_left_node_index(self, index):
        return 2*index+1
    
    def get_right_node_index(self, index):
        return 2*index+2
    
    # insert the value at the end of the array(heap) and move it up by comparing the elements in the heap
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    # check the parent and child and swap elements to move the min to top 
    def heapify_up(self, index):
        while index != 0 and self.heap[self.get_parent_index(index)] > self.heap[index]:
            self.heap[index], self.heap[self.get_parent_index(index)] = self.heap[self.get_parent_index(index)],  self.heap[index]
            # update the parent index
            index = self.get_parent_index(index)
            print(index)

    # to remove the root minimum value 
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]             # which is a minimum value 
        self.heap[0] = self.heap.pop()  # swap the root with the last element in the heap
        self.heapify_down(0)            # move the element down 
        
        return root 
    
    # compare parent and child and move them accordingly 
    def heapify_down(self, index):
        smallest_idx = index
        left_index = self.get_left_node_index(index)
        right_index = self.get_right_node_index(index)
        
        heap_size = len(self.heap)
        
        # check if left index is smaller than the heap size and if left value is smaller than current smallest value update it
        if left_index < heap_size and self.heap[left_index] < self.heap[smallest_idx]:
            smallest_idx = left_index 
            
        # same as above but for right 
        if right_index < heap_size and self.heap[right_index] < self.heap[smallest_idx]:
            smallest_idx = right_index
        
        # if smallest index has changed swap the index and smallest_index
        if smallest_idx != index:
            self.heap[index], self.heap[smallest_idx] = self.heap[smallest_idx], self.heap[index]
            self.heapify_down(0)
        


if 1:
    # Test vectors for min heap
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(12)
    min_heap.insert(1)
    min_heap.insert(7)
    print(min_heap.heap)  
    print(min_heap.extract_min())  # Output: 1
    print(min_heap.heap) 
    




class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def get_parent_index(self, index):
        return (index-1)//2
    
    def get_left_node_index(self, index):
        return 2*index+1
    
    def get_right_node_index(self, index):
        return 2*index+2
    
    # insert the value at the end of the array(heap) and move it up by comparing the elements in the heap
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    # check the parent and child and swap elements to move the min to top 
    def heapify_up(self, index):
        while index != 0 and self.heap[self.get_parent_index(index)] < self.heap[index]:
            self.heap[index], self.heap[self.get_parent_index(index)] = self.heap[self.get_parent_index(index)],  self.heap[index]
            # update the parent index
            index = self.get_parent_index(index)

    # to remove the root minimum value 
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]             # which is a minimum value 
        self.heap[0] = self.heap.pop()  # swap the root with the last element in the heap
        self.heapify_down(0)            # move the element down 
        
        return root 
    
    # compare parent and child and move them accordingly 
    def heapify_down(self, index):
        largest_idx = index
        left_index = self.get_left_node_index(index)
        right_index = self.get_right_node_index(index)
        
        heap_size = len(self.heap)
        
        # check if left index is smaller than the heap size and if left value is smaller than current smallest value update it
        if left_index < heap_size and self.heap[left_index] > self.heap[largest_idx]:
            largest_idx = left_index 
            
        # same as above but for right 
        if right_index < heap_size and self.heap[right_index] > self.heap[largest_idx]:
            largest_idx = right_index
        
        # if smallest index has changed swap the index and smallest_index
        if largest_idx != index:
            self.heap[index], self.heap[largest_idx] = self.heap[largest_idx], self.heap[index]
            self.heapify_down(0)





if 0:
    # Test vectors for max heap
    max_heap = MaxHeap()
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(17)
    max_heap.insert(10)
    max_heap.insert(12)
    max_heap.insert(1)
    max_heap.insert(7)
    print(max_heap.heap)  
    print(max_heap.extract_max())  # Output: 17
    print(max_heap.heap) 