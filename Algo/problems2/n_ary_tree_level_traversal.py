from collections import deque
import logging


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def n_ary_tree_level_traversal(node: Node):
    final_list = list()
    queue = deque()
    queue.append(node)
    size = 1

    while len(queue):
        new_size = 0
        final_list.append([])

        for i in range(size):  # using this loop we are fetching all child nodes at same level
            tmp = queue.popleft()
            final_list[-1].append(tmp.data)
            if tmp.left_child:
                queue.append(tmp.left_child)
                new_size += 1
            if tmp.right_child:
                queue.append(tmp.right_child)
                new_size += 1
        size = new_size # here no of children will keep increasing
    return final_list


def n_ary_tree_level_traversal_2(root_node: Node):
    final_dict = dict()
    root_level = 1
    helper_function(root_node, root_level, final_dict)
    print(f"final_dict= {final_dict}")


def helper_function(node, level, input_dict):
    input_dict.setdefault(level, []).append(node.data)
    if node.left_child:
        helper_function(node.left_child, level + 1, input_dict)
    if node.right_child:
        helper_function(node.right_child, level + 1, input_dict)


if __name__ == "__main__":
    root = Node(5)
    root.left_child = Node(3)
    root.right_child = Node(4)
    root.right_child.right_child = Node(18)
    root.left_child.left_child = Node(6)
    root.left_child.right_child = Node(-5)

    print(f"n_ary_tree_level_traversal - {n_ary_tree_level_traversal(root)}")

    n_ary_tree_level_traversal_2(root)
