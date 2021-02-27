class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.total_size = 0

    def list_size(self):
        return self.total_size

    # O(1) no looping
    def add_data_at_front(self, data):
        new_node = Node(data)
        if self.head:
            print("\nList has data - adding in front - set current head to next_node of new_node")
            new_node.next_node = self.head
        self.head = new_node
        self.total_size += 1
        self.print_all()

    def add_data_at_end(self, data):
        new_node = Node(data)
        current_node = self.head
        if self.head is None:  # O(1) no looping
            print("List was empty ")
            self.head = new_node
        else:
            print("\nList has data - adding in end")
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        self.total_size += 1
        self.print_all()

    def print_all(self):
        print(f"list length - {self.total_size}")
        if self.head:
            current_node = self.head
            while current_node.next_node:
                print(f"{current_node.data}", end=" -> ")
                current_node = current_node.next_node
            print(f"{current_node.data}", end=" ")
        print("\n")

    def middle_node(self):
        print("Middle Node")
        print(f"list length - {self.list_size()}")
        start_pointer = self.head
        end_pointer = self.head
        while end_pointer.next_node.next_node:
            start_pointer = start_pointer.next_node
            end_pointer = end_pointer.next_node.next_node
        # end_pointer reached last node, start_pointer reached middle
        print(f"Middle node data value- {start_pointer.data}")
        return start_pointer

    def add_at_nth_position(self, vposition, data): # O(n) operation
        try:
            print("\nadd_at_nth_position")
            assert (str(vposition).isdigit()), "Position not a number, enter number value"
            position = vposition - 1

            if 0 <= int(position) < self.list_size():
                print("position is valid")
            else:
                print("position not valid")
                raise
            # traverse till that position, keep current(nth) and previous node(n-1 th)
            previous_node = None
            current_node = self.head
            i = 0
            while i < position:
                previous_node = current_node
                current_node = current_node.next_node
                i += 1
            print(f"Traversed till node with data - {current_node.data}")
            print(f"Previous node data - {previous_node.data}")
            # create node with new data and assign new_node.node_next to existing nth position node
            new_node = Node(data)
            new_node.next_node = current_node
            # n-1 th node next_node to new_node
            previous_node.next_node = new_node
            self.total_size += 1
            self.print_all()
        except AssertionError as error:
            print("exception block - add_at_nth_position ")
            print(error)

    def remove_from_first(self):
        print("\nNode remove_from_first ")
        if self.total_size == 0:
            print("Empty list - no node to remove")
        elif self.total_size == 1:
            print("Only one node in list")
            self.head = None
        else:
            current_node = self.head
            self.head = current_node.next_node
        self.total_size -= 1
        self.print_all()

    def remove_from_end(self): # O(n) operation
        print("Node remove from end")
        if self.total_size == 0:
            print("Empty List")
        elif self.total_size == 1:
            self.head = None
        else: # self.total_size > 1
            # traverse till end and keep previous node
            current_node = self.head
            previous_node = None
            while current_node.next_node:
                previous_node = current_node
                current_node = current_node.next_node
            # set previous_node.next_node to None
            previous_node.next_node = None
        self.total_size -= 1
        self.print_all()

    def search_node_with_data(self, data):
        print(f"Searching for node with data - {data} in linked list")
        previous_node, current_node = None, None
        if self.total_size == 0:
            print("Empty List")
        else:
            current_node = self.head
            while current_node.next_node:
                if current_node.data == data:
                    print(f"Match found for data - {data}")
                    break
                else:
                    previous_node = current_node
                    current_node = current_node.next_node
            else:
                previous_node, current_node = None, None
                print("No match with data found")
        self.print_all()
        return previous_node, current_node

    def remove_node_with_data(self, data):
        print(f"remove_node_with_data {data} from linked list")
        print(f"Going to search for {data} from linked list")
        previous_node, current_node = self.search_node_with_data(data)

        if previous_node is None and current_node is None:
            print("No match with data  - Can NOT remove node")
        if previous_node is None and current_node:
            print("List with only one element")
            self.head = None
            self.total_size -= 1
        if previous_node and current_node:
            print("Middle or end node")
            previous_node.next_node = current_node.next_node
            self.total_size -= 1
        self.print_all()

    def reverse_linked_list(self): # O(n) operation
        print("Reversing linked list")
        prev_node = None
        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = prev_node
                break
            self.head = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = self.head
            #self.print_all()
        self.print_all()


if __name__ == "__main__":
    print("----Linked List----")
    ll = LinkedList()
    ll.print_all()
    ll.add_data_at_front(10)
    ll.add_data_at_end(5)
    ll.add_data_at_front(11)
    ll.add_data_at_end(6)
    ll.add_data_at_front(12)
    ll.add_data_at_end(7)
    ll.add_data_at_front(13)
    ll.add_data_at_end(8)

    ll.middle_node()

    ll.add_at_nth_position(4, 99)

    ll.add_at_nth_position(6, 101)

    ll.add_at_nth_position('$', 103)

    ll.remove_from_first()

    ll.remove_from_end()

    ll.search_node_with_data(99)

    ll.search_node_with_data(199)

    ll.remove_node_with_data(100)

    ll.remove_node_with_data(101)

    ll.reverse_linked_list()

