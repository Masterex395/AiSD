from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child == None and self.right_child == None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None: self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None: self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child != None: self.left_child.traverse_post_order(visit)
        if self.right_child != None: self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None: self.left_child.traverse_pre_order(visit)
        if self.right_child != None: self.right_child.traverse_pre_order(visit)


class BinaryTree:
    root: BinaryNode
    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)


def bottom_line(tree: 'BinaryTree'):
    x = []
    root = tree.root
    def bottom_view(node: 'BinaryNode'):
        if node.left_child:
            temp = node.left_child
            if temp.right_child == None:
                x.append(node.value)
        elif node.right_child:
            temp = node.right_child
            if temp.left_child == None:
                x.append(node.value)
        else:
            x.append(node.value)
    root.traverse_in_order(bottom_view)
    return x


tree = BinaryTree(8)

tree.root.add_left_child(1)
tree.root.left_child.add_left_child(2)
tree.root.left_child.left_child.add_right_child(5)
tree.root.left_child.left_child.add_left_child(4)
tree.root.left_child.left_child.left_child.add_right_child(9)
tree.root.left_child.left_child.left_child.add_left_child(8)

tree.root.left_child.add_right_child(3)
tree.root.left_child.right_child.add_right_child(7)

print(bottom_line(tree))