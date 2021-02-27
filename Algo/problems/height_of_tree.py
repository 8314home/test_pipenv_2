class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class binary_tree(object):

    def __init__(self):
        self.root = None

    def insert_data(self, data):
        tmp = Node(data)
        if self.root:
            self._insert_node(self.root, tmp)
        else:
            print("No root of tree")
            self.root = tmp

    def _insert_node(self, node, data_node):
        if node.data < data_node.data:
            if node.right_child:
                self._insert_node(node.right_child, data_node)
            else:
                node.right_child = data_node
        if data_node.data < node.data:
            if node.left_child:
                self._insert_node(node.left_child, data_node)
            else:
                node.left_child = data_node

        # left most child of subtree--> print data --> right most child of subtree
    def inorder_traversal(self, node, traverse_list):
        if node.left_child:
            self.inorder_traversal(node.left_child, traverse_list)
        print(f"{node.data} -> ", end="")
        traverse_list.append(node.data)
        if node.right_child:
            self.inorder_traversal(node.right_child, traverse_list)


def height_of_tree(node: Node):
    # Op on node, handle left & right subtree/node
    if node is None:
        return 0
    print(f"data node - {node.data}")
    return 1 + max(height_of_tree(node.left_child), height_of_tree(node.right_child))


if __name__ == "__main__":
    bt = binary_tree()
    bt.insert_data(10)
    bt.insert_data(7)
    bt.insert_data(3)
    bt.insert_data(5)
    bt.insert_data(15)
    bt.insert_data(14)
    bt.insert_data(13)
    print(bt.inorder_traversal(bt.root, traverse_list=[]))

    print(f"height of tree - {height_of_tree(bt.root)}")

