# Define the Node class which will be used to create new nodes.
class Node:
    def __init__(self, value=None):
        self.value = value  
        self.next = None 

def detect_cycle(head):
    slow = head 
    fast = head
    # check for cycle, once detected break the loop  
    while fast != None and fast.next != None:
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast:
            break 

    # base check to remove cases where there is only node or no cycle 
    if fast is None and fast.next is None:
        return None 
    
    # find the node where exactly the cycle starts, by setting slow to head and moving slow and fast by one step 
    slow = head 
    while slow != fast:
        slow = slow.next 
        fast = fast.next 

    return slow 




# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

# Setup links (last node points to node3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

# Detect cycle
cycle_start_node = detect_cycle(node1)
print(cycle_start_node.value)  # Output: 3


# applying this to array problem
# leet code problem 287: given an array of integers nums containing n+1 intergers, where each integer is in the range [1,n] inclusive,
# there is only one repeated number in this 
def findDuplicate(nums):
    slow = 0
    fast = 0

    # Find the meeting point of slow and fast pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find the entrance of the cycle
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

nums = [1,4,2,3,2]
print(f"duplicate number is: {findDuplicate(nums)}\n")