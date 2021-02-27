from BST import Node, BST


def string_to_tree(s, root=None):
    """
    Input string , Output is a Tree, For Trees we always return the root of tree
    :param s:
    :param root:
    :return:
    """
    print("+++++++++++")
    print(f"string = {s} len(s) - {len(s)}")
    if root:
        print(f"root- {root.data}")

    # Determine root
    neg_value = False  # decides 1st number being root of tree
    nums = 0

    if s[0] == '-':
        neg_value = True
        start = 1
        while s[start] != '(':
            nums = nums*10 + int(s[start])
            start += 1
        s = s[start:]
        print(f"After root is set edited string to check for nodes - {s}")

    if neg_value:
        root = Node(-1*nums)

    # root has been decided
    # When root is decided and ( is encounter
    # then check if left child is there for node
    # If not set the node

    if not neg_value and (s[0] != '(') and (s[0] != '('):
        root = Node(s[0])
        print(f"new node created - {s[0]}")
        s = s[1:]
        print(f"remaining string after node creation - {s}")

    if len(s) and s[0] == '(' and (not root.left_child):
        print("found and skipped a (")
        s, root.left_child = string_to_tree(s[1:], root)
        print(f"root-{root.data} root.left_child-{root.left_child.data} string - {s}")

    if len(s) and s[0] == ')':
        print("found and skipped a )")
        return s[1:], root

    if len(s) and s[0] == '(' and (not root.right_child):
        print("found and skipped a (")
        s, root.right_child = string_to_tree(s[1:], root)
        print(f"root-{root.data} root.right_child-{root.right_child.data} string - {s}")

    if len(s) and s[0] == ')':
        print("found and skipped a )")
        return s[1:], root

    return s, root


def traverse_root(node: Node):
    print(f"{node.data} ->", end=" ")
    if node.left_child:
        traverse_root(node.left_child)
        # print(f"{node.data} has left child - {node.left_child.data}")
    if node.right_child:
        traverse_root(node.right_child)
        # print(f"{node.data} has left child - {node.right_child.data}")


def traverse_root_relation(node: Node):
    if node.left_child:
        traverse_root_relation(node.left_child)
        print(f"{node.data} has left child - {node.left_child.data}")
    if node.right_child:
        traverse_root_relation(node.right_child)
        print(f"{node.data} has right_child - {node.right_child.data}")


if __name__ == "__main__":
    print("Hello")
    input_string = '-423(2(3)(1))(6(5))'
    final_string,root_of_tree = string_to_tree(input_string)
    print("------------------")
    print(f"root_of_tree: {root_of_tree.data}")
    traverse_root(root_of_tree)
    print("\n------------------\n")
    traverse_root_relation(root_of_tree)


