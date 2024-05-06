class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def get_height(self):
        if not self:
            return 0
        return self.height

    def update_height(self):
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

    def get_balance(self):
        if not self:
            return 0
        return self.get_height(self.left) - self.get_height(self.right)

    def rotate_right(self):
        new_root = self.left
        self.left = self.left.right
        new_root.right = self
        self.update_height()
        new_root.update_height()
        return new_root

    def rotate_left(self):
        new_root = self.right
        self.right = self.right.left
        new_root.left = self
        self.update_height()
        new_root.update_height()
        return new_root

    def balance(self):
        self.update_height()
        balance_factor = self.get_balance()

        if balance_factor > 1:
            if self.left.get_balance() < 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()

        if balance_factor < -1:
            if self.right.get_balance() > 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()

        return self

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left = self.left.add_child(data)
            else:
                self.left = AVLTreeNode(data)
        else:
            if self.right:
                self.right = self.right.add_child(data)
            else:
                self.right = AVLTreeNode(data)

        return self.balance()

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self.balance()


def build_avl_tree(elements):
    print(f"Building the AVL tree with the input elements: {elements}\n")
    root = AVLTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    avl_tree = build_avl_tree([15, 12, 7, 14, 27, 20, 23, 88])

    print(" In order traversal gives the sorted list")
    print(f"In order traversal (left nodes, root node, right nodes): [{avl_tree.in_order_traversal()}]")
    print(f"Pre order traversal (root node, left nodes, right nodes): [{avl_tree.pre_order_traversal()}]")
    print(f"Post order traversal (left nodes, right nodes, root node): [{avl_tree.post_order_traversal()}]\n")

    print(f"Find min function output: {avl_tree.find_min()}")
    print(f"Find max function output: {avl_tree.find_max()}\n")

    print(f"Sum of the AVL tree: {avl_tree.calculate_sum()}\n")

    avl_tree.delete(20)
    print("After deleting 20, the in-order traversal is: ", avl_tree.in_order_traversal())