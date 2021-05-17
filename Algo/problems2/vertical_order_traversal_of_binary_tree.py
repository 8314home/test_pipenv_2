
# To solve this problem , starting from root (height=0)and downstream ,
# if we encounter a right child then we do +1 and for a left child we do -1


class Node(object):

    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


def print_binary_tree_in_vertical_order(root_node: Node):
    height_dict = dict()
    helper(root_node, 0, height_dict)
    print(f"height_dict - {height_dict}")
    return sorted(height_dict.items(), key=lambda x: x[0])


def helper(node: Node, height, input_height_dict):
    input_height_dict.setdefault(height, []).append(str(node.data))
    if node.left_child:
        helper(node.left_child, height-1, input_height_dict)
    if node.right_child:
        helper(node.right_child, height+1, input_height_dict)


if __name__ == "__main__":
    print(f"print_binary_tree_in_vertical_order")

    root = Node(10)
    root.left_child = Node(5)
    root.right_child = Node(15)
    root.left_child.left_child = Node(3)
    root.left_child.right_child = Node(8)
    root.right_child.left_child = Node(12)
    root.right_child.right_child = Node(17)

    print(f"{print_binary_tree_in_vertical_order(root)}")
