import math

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self._insert_data(self.root, data)
        else:
            self.root = Node(data)
        print(f"data inserted in BST - {data}")

    def _insert_data(self, node, data):
        if data < node.data:
            if node.left_child:
                self._insert_data(node.left_child, data)
            else:
                node.left_child = Node(data)
        if node.data < data:
            if node.right_child:
                self._insert_data(node.right_child, data)
            else:
                node.right_child = Node(data)

    def traverse(self, traverse_list):
        if self.root:
            print(f"Tree root - {self.root.data}")
            print(f"Tree min value - {self.min_value_of_tree()}")
            print(f"Tree max value - {self.max_value_of_tree()}")
            print("INORDER TRAVERSAL")
            self._inorder_traversal(self.root, traverse_list)
            print("\n")
            return traverse_list
        else:
            print("EMPTY BST")

    def traverse_pre_order(self):
        if self.root:
            print("\nPRE-ORDER TRAVERSAL")
            self._preorder_traversal(self.root)
        else:
            print("EMPTY BST")

    def traverse_post_order(self):
        if self.root:
            self._post_order_traversal(self.root)
        else:
            print("EMPTY BST")

    # left most child of subtree--> print data --> right most child of subtree
    def _inorder_traversal(self, node, traverse_list):
        if node.left_child:
            self._inorder_traversal(node.left_child, traverse_list)
        print(f"{node.data} -> ", end="")
        traverse_list.append(node.data)
        if node.right_child:
            self._inorder_traversal(node.right_child, traverse_list)

    def _preorder_traversal(self, node):
        print(f"{node.data} -> ", end="")
        if node.left_child:
            self._preorder_traversal(node.left_child)
        if node.right_child:
            self._preorder_traversal(node.right_child)

    def _post_order_traversal(self, node):
        if node.left_child:
            self._post_order_traversal(node.left_child)
        if node.right_child:
            self._post_order_traversal(node.right_child)
        print(f"{node.data} -> ", end="")

    def min_value_of_tree(self): # left most child - use return-recursion when we need final value to be returned
        if self.root:
            return self._min_value_node(self.root)
        else:
            print("EMPTY BST")

    def _min_value_node(self, node):
        if node.left_child:
            return self._min_value_node(node.left_child)
        else:
            return node.data

    def max_value_of_tree(self): # right most node value
        if self.root:
            return self._max_value_node(self.root)
        else:
            print("EMPTY BST")

    def _max_value_node(self, node):
        if node.right_child:
            return self._max_value_node(node.right_child)
        else:
            return node.data

    def remove(self, data):
        if self.root:
            self.root = self._remove_node(self.root, data) # Return new root after node delete
        else:
            print("EMPTY BST")

    def _remove_node(self, node, data):
        if node is None: # reached till best possible leaf of tree, no match found
            print(f"--------NO node with {data} found in tree--------")
            return node
        if data < node.data:
            print(f"{data} less than {node.data} , go to left child")
            node.left_child = self._remove_node(node.left_child, data) # give me my left child
            print(f"-- {data} comparison to {node.data} done")
        elif node.data < data:
            print(f"{data} greater than {node.data}  , go to right child")
            node.right_child = self._remove_node(node.right_child, data) # give me my right child
            print(f"-- {data} comparison to {node.data} done")
        else:
            print(f"node with {data} found")
            if not node.left_child and not node.right_child:
                print("leaf node - no left or right child")
                del node
                return None
            if not node.left_child and node.right_child:
                print("node with only right child")
                node_right_child = node.right_child
                del node
                return node_right_child
            if node.left_child and not node.right_child:
                print("node with only left child")
                node_left_child = node.left_child
                del node
                return node_left_child
            if node.left_child and node.right_child:
                print("node with both child, need to get max_value from left subtree to replace node")
                right_most_node_of_left_subtree = self._get_predecessor(node.left_child)
                node.data = right_most_node_of_left_subtree.data
                node.left_child = self._remove_node(node.left_child, right_most_node_of_left_subtree.data)
                return node
        return node  # Finally returns new root

    def _get_predecessor(self, node):
        if node.right_child:
            return self._get_predecessor(node.right_child)
        print(f"right_most_node_of_left_subtree - {node.data}")
        return node

    def bfs_of_tree(self):
        bfs_queue = list()

        bfs_queue.append(self.root)

        while bfs_queue:
            current_node = bfs_queue.pop(0)
            print(f"{current_node.data} => ", end="")

            if current_node.left_child:
                bfs_queue.append(current_node.left_child)
            if current_node.right_child:
                bfs_queue.append(current_node.right_child)

    def dfs_of_tree(self, node):  # same as pre-order

        print(f"{node.data} ", end="")
        if node.left_child:
            self.dfs_of_tree(node.left_child)
        if node.right_child:
            self.dfs_of_tree(node.right_child)

    # Greater tree

# Tree is identical or not - check roots level, check for left subtree, check for right subtree


def identical_tree_check(node1, node2):
    # node level checks
    if node1 is None and node2:
        return False
    if node1 and node2 is None:
        return False

    print(f"checking node1 and node2 - {node1.data} and {node2.data}")
    if node1 and node2:
        if node1.data != node2.data:
            return False
    # Above means node data values are same

    # child level checks
    left_flag = right_flag = True

    if node1.left_child and node2.left_child:
        left_flag = identical_tree_check(node1.left_child, node2.left_child)

    if node1.right_child and node2.right_child:
        right_flag = identical_tree_check(node1.right_child, node2.right_child)

    return left_flag and right_flag


if __name__ == "__main__":
    print("BST ")

    bst = BST()

    bst.insert(10)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(11)
    bst.insert(9)
    bst.insert(14)
    bst.insert(8)
    print("\n traverse list : ")
    print("\n IN ORDER traversal gives sorted outcome")
    print(bst.traverse(traverse_list=[]))
    # Above  list retuned can be used to check element of a tree with other tree, no of elements in tree etc

    print("\n post order traversal")
    bst.traverse_post_order()

    print(f"Minimum value of tree - {bst.min_value_of_tree()}")
    print(f"Maximum value of tree - {bst.max_value_of_tree()}")

    print("\n Remove node with data")
    bst.remove(8)
    print("\n traverse list : ")
    print(bst.traverse(traverse_list=[]))

    bst.insert(23)
    bst.insert(12)
    bst.insert(13)

    print("\n Remove node with data")
    bst.remove(18)
    print("\n traverse list : ")
    print(bst.traverse(traverse_list=[]))

    print("\n Remove node with data")
    bst.remove(9)
    print("\n traverse list : ")
    print(bst.traverse(traverse_list=[]))

    print("\n Remove node with data")
    bst.remove(10)
    print("\n traverse list : ")
    print(bst.traverse(traverse_list=[]))

    print("\n BFS walk of tree")
    bst.bfs_of_tree()

    print("\n DFS walk of tree")
    bst.dfs_of_tree(bst.root)

    print("\n pre order traversal")
    bst.traverse_pre_order()



    print(f"bst_2 ")

    bst_2 = BST()
    bst_2.insert(23)
    bst_2.insert(12)
    bst_2.insert(13)
    bst_2.insert(33)

    print(f"bst_3")

    bst_3 = BST()
    bst_3.insert(23)
    bst_3.insert(12)
    bst_3.insert(13)
    bst_3.insert(33)

    print("Checking whether two trees are identical or not")

    identical_tree_check_flag=identical_tree_check(bst_2.root, bst_3.root)
    print(f"identical_tree_check_flag - {identical_tree_check_flag}")



