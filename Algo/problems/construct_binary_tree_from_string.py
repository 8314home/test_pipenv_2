class Node(object):

    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


# While loop is controlling when to exit
# recursion is controlling current_node position
# we are altering input string after every ops
# This approach is independent of global variable

def helper(input_string, node):

    while len(input_string):
        print(f"input_string - {input_string}")

        if len(input_string) and input_string[0] == ")":
            input_string = input_string[1:]
            print(f"received a ) , alter string string to {input_string}, returning")
            return node, input_string

        if len(input_string) and input_string[0] in '0123456789':
            node = Node(input_string[0])
            input_string = input_string[1:]
            print(f"call helper for input_string={input_string} node={node.data} ")
            node, input_string = helper(input_string, node)
            print(f" helper complete for input_string={input_string} node={node.data} returning")
            return node, input_string

        if len(input_string) and input_string[0] == "(":
            print(f"received a ( , current_node={node.data}")
            if node.left_child is None:
                node.left_child, input_string = helper(input_string[1:], node)
                print(f"for node= {node.data} left child set - {node.left_child.data} input_string = {input_string}")
            else:
                node.right_child, input_string = helper(input_string[1:], node)
                print(f"for node= {node.data} right_child set - {node.right_child.data}  input_string = {input_string}")


def construct_binary_tree_from_string(input_string):

    tmp = ""
    i = 0
    for i in range(len(input_string)):
        if input_string[i] == "(":
            break
        tmp += input_string[i]

    root = Node(int(tmp))

    input_string = input_string[i:]
    helper(input_string, root)

    return root


def traverse(node):
    if node.left_child:
        traverse(node.left_child)
    print(f"{node.data} ->", end='')
    if node.right_child:
        traverse(node.right_child)


if __name__ == "__main__":

    string_to_convert = "-4(2(3)(1))(6(5))"

    print(f"\nconstruct_binary_tree_from_string -\n")

    root_of_tree = construct_binary_tree_from_string(string_to_convert)
    traverse(root_of_tree)

