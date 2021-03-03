

class Node(object):

    def __init__(self,data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add_node(self,data):

        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = Node(data)
        return self.head

    def traverse(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data} ->", end="")
            current_node = current_node.next_node

    def rotate_list(self, input_no_of_rotations):

        list_size = 0
        current_node = self.head
        while current_node:
            list_size += 1
            current_node = current_node.next_node

        k = list_size - input_no_of_rotations
        k = k % list_size  # this is done in case list size is 5 and rotations are 8

        if k == 0 or list_size == 1 or list_size == k or self.head is None:
            return self.head

        current_node = self.head
        previous_node = None
        for i in range(k):
            previous_node = current_node
            current_node = current_node.next_node

        previous_node.next_node = None
        tmp = current_node

        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = self.head
        self.head = tmp

        return self.head


if __name__ == "__main__":

    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)

    ll.traverse()

    ll.rotate_list(2)

    print("\n")
    ll.traverse()
