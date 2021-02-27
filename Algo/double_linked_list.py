
class Node(object):

    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.total_size = 0
        self.tail = None

    def insert_at_start(self, data): # O(1) operation
        print("\nInsert data at start of DLIST")
        new_node = Node(data)
        if self.total_size == 0:
            self.head = self.tail = new_node
        else:
            current_node = self.head
            new_node.next_node = current_node
            current_node.prev_node = new_node
            self.head = new_node
        self.total_size += 1
        self.print_all()

    def insert_at_end(self, data): # O(1) operation
        print("\ninsert data at the end")
        new_node = Node(data)
        if self.total_size == 0:
            self.head = self.tail = new_node
        else:
            current_node = self.tail
            current_node.next_node = new_node
            new_node.prev_node = current_node
            self.tail = new_node
        self.total_size += 1
        self.print_all()

    def print_all(self):  # O(n) operation
        print(f"Total List size - {self.total_size}")
        current_node = self.head
        while current_node:
            print(f"{current_node.data} -->", end=" ")
            current_node = current_node.next_node
        print("\n")

    def remove_from_start(self): #O(1)
        print("\nremove_from_start")
        if self.head.next_node:
            new_head = self.head.next_node
            new_head.prev_node = None
            self.head = new_head
        else:
            self.head = self.tail = None
        self.total_size -= 1
        self.print_all()

    def remove_from_end(self): #O(1)
        print("\nremove_from_end")
        if self.tail.prev_node:
            new_tail = self.tail.prev_node
            new_tail.next_node = None
            self.tail = new_tail
        else:
            self.head = self.tail = None
        self.total_size -= 1
        self.print_all()

    def remove_node_if_data_present(self, data):
        print(f"\nSearching for node with {data} to remove from list")
        removing_node = None
        if self.total_size == 0:
            print("Empty List")
            return removing_node
        prev_node = None
        current_node = self.head
        while current_node:
            if data == current_node.data:
                print("data node found")
                removing_node = current_node
                prev_node.next_node = current_node.next_node
                current_node.next_node.prev_node = prev_node
                self.total_size -= 1
                break
            prev_node = current_node
            current_node = current_node.next_node
        else:
            print(f"No node with data {data} in list")
        self.print_all()
        return removing_node


if __name__ == "__main__":
    print("Double Linked List")

    dll = DoubleLinkedList()
    dll.print_all()

    dll.insert_at_start(5)
    dll.insert_at_start(10)
    dll.insert_at_start(15)
    dll.insert_at_start(20)
    dll.insert_at_end(21)
    dll.insert_at_end(23)
    dll.remove_from_start()
    dll.remove_from_end()

    dll.insert_at_start(101)
    dll.insert_at_end(151)
    dll.insert_at_start(201)

    dll.remove_node_if_data_present(5)

    dll.remove_node_if_data_present(8)
