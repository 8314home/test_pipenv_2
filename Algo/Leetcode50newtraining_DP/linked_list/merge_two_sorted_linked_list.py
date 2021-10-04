class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, data):
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
        else:
            tmp.next = self.head
            self.head =tmp


def merge_two_linked_list(L1,L2):

    l1 = L1.head
    l2 = L2.head
    ans_head = current = Node(None)  # dummy node to start with need to return ans_head.next for new list head

    while l1 or l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    while l1:
        current.next = l1
        l1 = l1.next
        current = current.next

    while l2:
        current.next = l2
        l2 = l2.next
        current = current.next

    return ans_head.next

if __name__ == '__main__':
    pass





# sorted linked list
# L1 : 1->2->3
# L2 : 1->3->4
# start , ans = current = None

# if __name__ == '__main__':
#
#     input_list_1.add