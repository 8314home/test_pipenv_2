# Next right node pointer problem
# Aim of this problem is to show a list of nodes which will have next pointer from a node pointer it's parent node
# Or for a parent node to it's right child node
# This can be done using in order traversal of tree and a Queue
# During Inorder traversal , instead of printing we will append item to the queue
# This will keep right side node for a node ,next in line inside the queue

from collections import deque


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.next_right_pointer = None


def next_right_pointer(root_node):
    # define a queue

    q = deque()

    # get filled queue from inorder traversal
    _inorder_traversal(root_node, q)

    # loop over queue, each node poped from queue, right pointer pointing to 1st node from queue
    start = q[0]

    while len(q):
        item = q.popleft()
        if len(q):
            item.next_right_pointer = q[0]
        else:
            item.next_right_pointer = None

    while start:
        print(f"{start.data} ->",end="")
        start = start.next_right_pointer


def _inorder_traversal(node: Node, input_queue):
    if node.left_child:
        _inorder_traversal(node.left_child, input_queue)
    input_queue.append(node)
    if node.right_child:
        _inorder_traversal(node.right_child, input_queue)


if __name__ == "__main__":

    root = Node(10)
    root.left_child = Node(8)
    root.right_child = Node(12)
    root.left_child.left_child = Node(3)

    print(f"\nNext right node pointer problem - ")
    next_right_pointer(root)
