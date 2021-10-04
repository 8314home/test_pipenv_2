from collections import deque


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def zigzag_level_order_traversal(root):
    if root is None:
        return None
    q = deque()
    q.append(root)
    tmp = []
    final_list = []
    zigzag = False

    while q:
        n = len(q)
        for _ in range(n):
            if zigzag:
                item = q.pop()  # pop() ousts from right side
                tmp.append(item.data)
                if item.right_child:
                    q.appendleft(item.right_child)
                if item.left_child:
                    q.appendleft(item.left_child)
            else:
                item = q.popleft()
                tmp.append(item.data)
                if item.left_child:
                    q.append(item.left_child)
                if item.right_child:
                    q.append(item.right_child)
        final_list.append(list(tmp))
        tmp.clear()
        zigzag = not zigzag  # flip the flag
        print(final_list)
    return final_list


if __name__ == '__main__':
    print("zigzag_level_order_traversal")

    ROOT = Node(10)
    ROOT.left_child = Node(5)
    ROOT.right_child = Node(15)
    ROOT.right_child.left_child = Node(13)
    ROOT.right_child.right_child = Node(17)

    print(f"zigzag_level_order_traversal - {zigzag_level_order_traversal(ROOT)}")
