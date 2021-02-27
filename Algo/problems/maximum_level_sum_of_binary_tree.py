# This problems is solved by using "level tracking solution approach of binary tree"
# Here we use two queus , at a time we fill one queue with all nodes of that level
# continue till both queues are empty

from collections import deque


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def max_level_sum_of_binary_tree(root_node: Node):
    q1 = deque()
    q2 = deque()

    sum = 0
    level = -1
    max_sum_label = -99
    max_sum = -99

    # root_node added to 1st queue to start the process
    q1.append(root_node)
    print(f"\nq1 - {len(q1)} q2- {len(q2)}")

    while q1 or q2:  # keep continuing loop untill both queues are empty

        if len(q1):
            level += 1

        sum = 0

        while q1:
            tmp = q1.popleft()
            sum += tmp.data
            if tmp.left_child:
                q2.append(tmp.left_child)
            if tmp.right_child:
                q2.append(tmp.right_child)

        if sum > max_sum:
            max_sum = sum
            max_sum_label = level
        print(f"sum ={sum} level={level} max_sum-{max_sum} max_sum_label-{max_sum_label}")

        if len(q2):
            level += 1

        sum = 0

        while q2:
            tmp = q2.popleft()
            sum += tmp.data
            if tmp.left_child:
                q1.append(tmp.left_child)
            if tmp.right_child:
                q1.append(tmp.right_child)

        if sum > max_sum:
            max_sum = sum
            max_sum_label = level
        print(f"sum ={sum} level={level} max_sum-{max_sum} max_sum_label-{max_sum_label}")
    return max_sum_label, max_sum


def travserse(node):
    print(f"{node.data} ->", end="")
    if node.left_child:
        travserse(node.left_child)
    if node.right_child:
        travserse(node.right_child)


if __name__ == "__main__":

    root = Node(1)
    root.left_child=Node(7)
    root.right_child= Node(0)
    root.left_child.left_child = Node(7)
    root.left_child.right_child = Node(-8)

    print(f"binary tree")
    travserse(root)

    print(f"\nmax_level_sum_of_binary_tree - {max_level_sum_of_binary_tree(root)}")
