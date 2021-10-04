class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def has_cycle(self,head):
        t = head
        h = head
        while t and h and h.next:
            h = h.next.next
            t = t.next
            if t == h:  # we can not place this just after while as initally both will have head, t= h = head
                return True
        return False


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

#mark cycle
node6.next = node3

s = Solution()
print(s.has_cycle(node1))