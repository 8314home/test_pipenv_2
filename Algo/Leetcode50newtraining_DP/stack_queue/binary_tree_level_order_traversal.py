

# Whenever someone is sayong about level-by-level, layer-by-leyer, iteration-after-iteration
# Think about BFS-Queue,
# DFS - Stack(recursion) operation
from collections import deque


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def binary_tree_level_order_traversal(root: Node):
    final_list = []
    q = deque()
    q.append(root)
    temp = []

    while q:
        n = len(q)  # len is need to get all children in queue
        print(f"n- {n}")
        for i in range(0, n):
            poped_item = q.popleft()
            temp.append(poped_item.data)
            print(poped_item.data)
            print(temp)
            if poped_item.left_child:
                q.append(poped_item.left_child)
            if poped_item.right_child:
                q.append(poped_item.right_child)
        final_list.append(list(temp))
        print(f"final_list - {final_list}")
        temp.clear()
    return final_list


def binary_tree_level_order_traversal_recursion(root):
    height_dict = {}
    _helper(root, 0, height_dict)
    print(height_dict)
    return height_dict


def _helper(node, h, height_dict):
    if node is None:
        return
    height_dict.setdefault(h, []).append(node.data)
    _helper(node.left_child, h+1, height_dict)
    _helper(node.right_child, h+1, height_dict)


if __name__ == "__main__":
    ROOT = Node(10)
    ROOT.left_child = Node(5)
    ROOT.right_child = Node(15)
    ROOT.right_child.left_child = Node(13)
    ROOT.right_child.right_child = Node(17)

    print(f"Level order traversal result - {binary_tree_level_order_traversal(ROOT)}")
    binary_tree_level_order_traversal_recursion(ROOT)
