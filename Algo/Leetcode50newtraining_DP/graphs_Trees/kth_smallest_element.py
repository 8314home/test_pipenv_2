class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def _inorder_ans(node, k, ans):
    if node.left_child:
        k, ans = _inorder_ans(node.left_child, k, ans)
    print(f'k={k}, ans={ans}, node={node.data}')
    k = k - 1
    print(f'k={k}, ans={ans}, node={node.data}')
    if k == 0:
        return k, node.data
    if node.right_child:
        k, ans = _inorder_ans(node.right_child, k, ans)
    return k, ans if ans else None


def _inorder_traverse(node, k, list_of_numbers):
    if node is None:
        return None
    _inorder_traverse(node.left_child, k, list_of_numbers)
    list_of_numbers.append(node.data)
    _inorder_traverse(node.right_child, k, list_of_numbers)


def kth_smallest_element(root_node, k_value):
    final_list = list()
    _inorder_traverse(root_node, k_value, final_list)

    result = _inorder_ans(root_node, k_value, ans = None)
    print(f'result={result}')
    print(f'final_list-{final_list}')
    return final_list[k_value-1]


if __name__ == '__main__':
    target = 3

    root = Node(10)
    root.left_child = Node(8)
    root.right_child = Node(15)
    root.right_child.left_child = Node(12)
    root.right_child.right_child = Node(25)
    root.right_child.right_child.left_child = Node(23)
    root.right_child.right_child.right_child = Node(28)
    print(f'BST - {target}th smallest element is {kth_smallest_element(root, target)}')

