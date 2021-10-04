class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


class Solution:

    def reverse_linked_list(self, head_node):
        prev = None
        head = head_node
        nextn = None

        while head:
            nextn = head.next
            head.next = prev
            prev = head
            head = nextn
        return prev

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
    reversed_head = s.reverse_linked_list(node1)
    s.print_ll(reversed_head)
