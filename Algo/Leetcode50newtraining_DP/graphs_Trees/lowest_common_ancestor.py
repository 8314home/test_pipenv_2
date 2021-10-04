class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def lowest_common_ancestor(node, p, q):
    if node is None:
        return None
    if node.data == p or node.data == q:
        return node

    left = lowest_common_ancestor(node.left_child, p, q)
    right = lowest_common_ancestor(node.right_child, p, q)
    print(f'currently at node - {node.data}')

    if left is None and right is None:
        return None
    if left is None and right:
        return right
    if left and right is None:
        return left
    if left and right:
        return node


if __name__ == '__main__':
    root = Node(10)
    root.left_child = Node(8)
    root.right_child = Node(15)
    root.right_child.left_child = Node(12)
    root.right_child.right_child = Node(25)
    root.right_child.right_child.left_child = Node(23)
    root.right_child.right_child.right_child = Node(28)

    t1 = 12
    t2 = 28
    answer = lowest_common_ancestor(root, t1, t2)

    print(f'lowest_common_ancestor({t1}, {t2}) is Node - {answer.data}')
