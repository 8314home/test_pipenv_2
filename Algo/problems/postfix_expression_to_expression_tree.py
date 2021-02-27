class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class Stack(object):

    def __init__(self):
        self.stack = list()

    def push(self, data: Node):
        self.stack.append(data)
        return self.stack

    def pop(self):
        tmp = self.stack[-1]
        del self.stack[-1]
        return tmp

    def peek(self):
        return self.stack[-1]

    def show(self):
        print(f"current stack content:")
        for node in self.stack:
            print(node.data, end='->')
        print()


class Binary_tree(object):
    def __init__(self):
        self.root = None

    def postfix_expression_to_expression_tree(self, input_list):
        # create an empty stack that will contain items of type node
        stk = Stack()
        for item in input_list:
            # print(f"item - {item}")
            if item in ('*','-','+','/'):
                exp_node = Node(item)
                if stk.stack:
                    t1 = stk.pop()
                    exp_node.right_child = t1
                    # print(f"found - {t1.data}")
                if stk.stack:
                    t2 = stk.pop()
                    exp_node.left_child = t2
                    # print(f"found - {t2.data}")
                stk.push(exp_node)
            else:
                # then create a node with it and insert into stack
                stk.push(Node(item))
        self.root = stk.peek()  # final element as root
        print(f"root data: {self.root.data}")
        return self.root

    def inorder_traverse(self, node: Node):
        if node.left_child:
            self.inorder_traverse(node.left_child)
        print(f"{node.data} ", end='')
        if node.right_child:
            self.inorder_traverse(node.right_child)


if __name__ == "__main__":
    bt = Binary_tree()
    postfix_exp = 'ab+ef*g*-'

    bt_root: Node = bt.postfix_expression_to_expression_tree(postfix_exp)
    bt.inorder_traverse(bt_root)


