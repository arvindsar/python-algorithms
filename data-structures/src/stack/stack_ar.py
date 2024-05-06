from collections import deque

    
class Stack:
    def __init__(self, stack_type='list'):
        self.stack_type = stack_type
        if stack_type == 'list':
            self.stack = []
        else:
            self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def get_values(self):
        return self.stack
# Example usage
if 0:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"stack values after push: {stack.get_values()}")
    print(f"pop which means removes the last element of the array: {stack.pop()}")  # Output: 3
    print(f"stack values after pop: {stack.get_values()}")
    print(f"peek just displays the last element in the stack: {stack.peek()}")  # Output: 2
    print(f"stack values after peek: {stack.get_values()}")
    print(f"is statck empty: {stack.is_empty()}")  # Output: False


## Reverse the string 
def reverse_string(input_str):
    stack = []
    # push charecters in the stack 
    for c in input_str:
        stack.append(c)
    
    # reverse the stack into a string 
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string


if 0:
    print(reverse_string("Hello, World!"))  # Output: "!dlroW ,olleH"


## check for balanced paranthesis  
def is_balanced(s):
    stack = []

    braces = ['(', ')', '[',']','{','}']
    s_ = ""
    for c in s:
        if c in braces:
            s_ += c

    for char in s_:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
            if current_char == '{':
                if char != "}":
                    return False

    return len(stack) == 0

if 0:
    print(is_balanced("(a{[]})"))  # Output: True
    print(is_balanced("({[}])"))  # Output: False



def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

if 1:
    print(is_valid_parentheses("()[]{}"))  # Expected output: True
    print(is_valid_parentheses("(]"))  # Expected output: False