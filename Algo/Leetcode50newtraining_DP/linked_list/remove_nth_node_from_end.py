

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


class Solution:

    def remove_nth_node_from_end(self, head, k):
        # two pointers
        h = head
        t = Node(None)
        t.next = head

        # move h to (k+1)th node from START  # make sure difference between position of h and k is n no of nodes
        while k > 0:
            h = h.next
            k -= 1

        # traverse untill h is None

        while h:
            h = h.next
            t = t.next

        # currently t at position, whose next nede need to be deleted,
        tmp = t.next
        t.next = tmp.next
        del tmp
        return head

    @staticmethod
    def print_ll(head_node):
        while head_node:
            print(f'{head_node.data}->', end='')
            head_node = head_node.next


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    n = 2
    s.print_ll(node1)
    print('\n')
    head_after_remove = s.remove_nth_node_from_end(node1, n)
    s.print_ll(head_after_remove)
