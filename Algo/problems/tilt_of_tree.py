# tilt of tree is to sum(tilt of node)
# tilt of node = MOD(left_subtree value - right subtree value)
import math


class Node(object):

    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


def helper(node: Node, tilt):

    if node is None:
        return 0, 0
    print(f"current_node = {node.data}, incoming tilt = {tilt}")
    left_subtree_val, tilt_left = helper(node.left_child, tilt)
    right_subtree_val, tilt_right = helper(node.right_child, tilt)

    tilt = tilt + tilt_left + tilt_right + math.fabs(left_subtree_val - right_subtree_val)
    print(f"Tilt of node = {node.data} is {tilt}")

    return node.data + left_subtree_val + right_subtree_val, tilt


def tilt_of_tree(node: Node, tilt=0):
    node_sum, tilt = helper(node, tilt)
    return tilt


def traverse(node: Node):
    print(f"{node.data} -> ", end='')
    if node.left_child:
        traverse(node.left_child)
    if node.right_child:
        traverse(node.right_child)


if __name__ == "__main__":
    print("Tilt of tree")

    root = Node(4)
    root.left_child = Node(2)
    root.right_child = Node(9)
    root.left_child.left_child = Node(3)
    root.left_child.right_child = Node(5)
    root.right_child.right_child = Node(7)

    print("Tree")
    traverse(root)

    print(f"Tilt of tree = {tilt_of_tree(root)}")




