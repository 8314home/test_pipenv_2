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

    def binary_tree_path_sum(self, node, current_sum, look_for_path_sum):
        print(f"At node - {node.data}")
        left_flag = right_flag = False
        current_sum += node.data
        if node.left_child is None and node.right_child is None:
            print(f"At a leaf node - {node.data}")
            print(f"current_sum - {current_sum}")
            if current_sum == look_for_path_sum:
                return True
            else:
                return False
        if node.left_child:
            left_flag = self.binary_tree_path_sum(node.left_child, current_sum, look_for_path_sum)
        if node.right_child:
            right_flag = self.binary_tree_path_sum(node.right_child, current_sum, look_for_path_sum)
        return left_flag or right_flag


if __name__ == "__main__":
    bt = binary_tree()
    bt.insert_data(7)
    bt.insert_data(10)
    bt.insert_data(3)
    bt.insert_data(5)
    bt.insert_data(9)
    bt.inorder_traversal(bt.root, [])
    look_for_path_sum = 26
    print(f"root of tree - {bt.root.data}")
    print(bt.binary_tree_path_sum(bt.root, 0, look_for_path_sum))


