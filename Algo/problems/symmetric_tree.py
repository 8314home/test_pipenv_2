class Node(object):

    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


class binary_tree(object):

    def _init_(self):
        self.root = None

    def traverse(self):
        if self.root:
            self._traverse(self.root)

    def _traverse(self, node):
        print(f"{node.data} - > ", end='')
        if node.left_child:
            self._traverse(node.left_child)
        if node.right_child:
            self._traverse(node.right_child)

    def symmetric_tree_check(self, root_node):
        if root_node is None:
            return True
        return self.mirror_node_check(root_node.left_child, root_node.right_child)

    def mirror_node_check(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None and node2:
            return False
        if node1 and node2 is None:
            return False
        return node1.data == node2.data \
               and self.mirror_node_check(node1.left_child, node2.right_child) \
               and self.mirror_node_check(node1.right_child, node2.left_child)


if __name__ == "__main__":
    bt = binary_tree()
    bt.root = Node(10)
    bt.root.left_child = Node(2)
    bt.root.right_child = Node(2)

    n1 = bt.root.left_child
    n2 = bt.root.right_child

    n1.left_child = Node(3)
    n1.right_child = Node(4)

    n2.left_child = Node(4)
    n2.right_child = Node(3)

    bt.traverse()

    print(f"\n\nsymmetric_tree_check -> {bt.symmetric_tree_check(bt.root)}")

