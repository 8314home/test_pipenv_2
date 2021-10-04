class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


class Solution:

    def add_two_numbers(self, h1, h2):
        pointer = Node(None)  # None->7
        ans = pointer
        carry = 0
        while h1 or h2:
            sm = carry
            if h1:
                sm += h1.data
                h1 = h1.next
            if h2:
                sm += h2.data
                h2 = h2.next
            carry = sm // 10
            pointer.next = Node(sm % 10)
            pointer = pointer.next
        if carry > 0:
            pointer.next = Node(carry)
        return ans.next


    @staticmethod
    def print_ll(head_node):
        while head_node:
            print(f'{head_node.data}->', end='')
            head_node = head_node.next


if __name__ == '__main__':
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(3)

    node4 = Node(5)
    node5 = Node(6)
    node6 = Node(9)

    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6

    s = Solution()
    finalsum = s.add_two_numbers(node1, node4)
    s.print_ll(finalsum)