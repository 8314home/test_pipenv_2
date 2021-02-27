class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def inorder_preorder_to_tree(inorder_array, preorder_array):
    root = helper(inorder_array, preorder_array)
    return root


def traverse(node):
    print(f"{node.data} -> ",end="")
    if node.left_child:
        traverse(node.left_child)
    if node.right_child:
        traverse(node.right_child)


def helper(inorder_array, preorder_array):

    if len(inorder_array) == 0 or len(preorder_array) == 0:
        return None

    node = Node(preorder_array[0])
    print(f"current_node - {node.data}")
    item = preorder_array[0]
    x = -1
    for i in range(len(inorder_array)):
        if inorder_array[i] == item:
            x = i
            break
    if x == -1:
        return None
    print(f"x index - {x}")
    # we need to ignore the item at index x
    inorder_left_subtree = inorder_array[:x]
    inorder_right_subtree = inorder_array[x+1:]
    preorder_left_subtree = preorder_array[1:x+1]
    preorder_right_subtree = preorder_array[x+1:]

    print(f"inorder_left_subtree - {inorder_left_subtree}")
    print(f"inorder_right_subtree - {inorder_right_subtree}")
    print(f"preorder_left_subtree - {preorder_left_subtree}")
    print(f"preorder_right_subtree - {preorder_right_subtree}")

    node.left_child = helper(inorder_left_subtree, preorder_left_subtree)
    node.right_child = helper(inorder_right_subtree, preorder_right_subtree)

    return node


if __name__ == "__main__":
    inorder_exp = [3,1,4,0,5,2,6]
    preorder_exp = [0,1,3,4,2,5,6]

    inorder_preorder_to_tree_root = inorder_preorder_to_tree(inorder_exp, preorder_exp)

    traverse(inorder_preorder_to_tree_root)




