from collections import deque


class Node(object):
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


def traverse(node):
    print(f"{node.data}->", end=" ")
    if node.left_child:
        traverse(node.left_child)
    if node.right_child:
        traverse(node.right_child)


def preorder_leaf_node_to_tree(pre_order_array, leaf_node_ind_array):
    # if N node , stack append 1st element is root
    stack = deque()
    _root = Node(pre_order_array[0])
    stack.append(_root)
    print("root is set")
    for i in range(1, len(pre_order_array)):
        x = Node(pre_order_array[i])
        parent = stack[-1]
        if parent.left_child is None:
            parent.left_child = x
        else:
            parent.right_child = x
            stack.pop()
        if leaf_node_ind_array[i] == 'N':
            stack.append(x)  # we should not push any Leaf node into stack
    return _root


if __name__ == "__main__":
    test_pre_order_array = [10,30,5,15,20]
    test_leaf_node_ind_array = ['N','N','L','L','L']

    preorder_leaf_node_to_tree_root = preorder_leaf_node_to_tree(test_pre_order_array, test_leaf_node_ind_array)
    traverse(preorder_leaf_node_to_tree_root)
