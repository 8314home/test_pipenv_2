# serialize - data structure/object to sequence of bits
# de-serialize - sequence of bits to object/data structure

from collections import deque


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class solution(object):

    def __init__(self):
        self.final_string = ''
        self.deser_queue = deque()
        self.serilzed_iter = None

    def serialze(self, node):
        if node is None:
            self.final_string = self.final_string + 'X#'
            return
        self.final_string = self.final_string + str(node.data) + '#'
        self.serialze(node.left_child)
        self.serialze(node.right_child)
        #print(f'str_val={self.final_string}')

    def _helper_deserialize(self):
        s = next(self.serilzed_iter)
        if s == 'X':
            return None
        node = Node(int(s))
        node.left_child = self._helper_deserialize()
        node.right_child = self._helper_deserialize()
        return node

    def deserialize(self, serilzed_str):
        self.serilzed_iter = iter(serilzed_str.split('#'))
        root_node = self._helper_deserialize()
        return root_node

    def show_nodes(self, root_node):
        if root_node.left_child:
            self.show_nodes(root_node.left_child)
        print(f'{root_node.data} -> ', end=' ')
        if root_node.right_child:
            self.show_nodes(root_node.right_child)


if __name__ == '__main__':
    root = Node(10)
    root.left_child = Node(8)
    root.right_child = Node(15)
    root.right_child.left_child = Node(12)
    root.right_child.right_child = Node(25)
    root.right_child.right_child.left_child = Node(23)
    root.right_child.right_child.right_child = Node(28)

    sln = solution()
    sln.serialze(root)

    print(f'BST - serialzed is {sln.final_string} ')
    input_str = sln.final_string
    returned_root_node = sln.deserialize(input_str)

    print(f'BSt - deserialized is -')
    sln.show_nodes(returned_root_node)
