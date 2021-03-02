
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def most_frequent_subtree_sum(_root_node: Node):
    most_frequent_sum = -99
    count_dict = dict()
    helper(count_dict, _root_node)

    print(f"count_dict - {count_dict}")

    longest_list = sorted(count_dict.values(), key=lambda l: len(l), reverse=True)
    print(f"longest_list - {longest_list}")
    return longest_list[0]


def helper(_count_dict: dict, node: Node):

    if node is None:
        return 0

    # below include recursive call for left subtree (child at node level) and right_subtree
    node_level_subtree_sum = node.data + helper(_count_dict, node.left_child) + helper(_count_dict, node.right_child)
    str_node_level_subtree_sum = str(node_level_subtree_sum)

    if str_node_level_subtree_sum in _count_dict.keys():
        _count_dict[str_node_level_subtree_sum].append(node.data)
    else:
        _count_dict.setdefault(str_node_level_subtree_sum, []).append(node.data)

    return node_level_subtree_sum


def traverse(node):
    print(f"{node.data} ->", end="")
    if node.left_child:
        traverse(node.left_child)
    if node.right_child:
        traverse(node.right_child)


if __name__ == "__main__":

    root = Node(5)
    root.left_child = Node(3)
    root.right_child = Node(4)
    root.left_child.left_child = Node(6)
    root.left_child.right_child = Node(-5)

    print(f"most_frequent_subtree_sum - {most_frequent_subtree_sum(root)}")
