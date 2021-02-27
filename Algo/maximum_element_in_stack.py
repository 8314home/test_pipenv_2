class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.total_size = 0

# Max Stack - Max element - during every insertion into stack, compare it against top most element of max stack
# and insert corresponding maximum element inside max_stack.

    def push(self, data):
        self.stack.append(data)
        self.total_size += 1

        if self.total_size == 1:
            self.max_stack.append(data)
        else:
            max_stack_topmost_element = self.max_stack[-1]
            if data > self.max_stack[-1]:
                self.max_stack.append(data) # for this round insert the incoming data
            else:
                self.max_stack.append(max_stack_topmost_element) # for this round insert the top most element again
        print(f"Stack Value - {self.stack}")
        print(f"Max Stack Value - {self.max_stack}")
        print("\n")

    def pop(self):
        self.max_stack.pop()
        tmp = self.stack.pop()
        print(f"popped element - {tmp}")
        print(f"Stack Value - {self.stack}")
        print(f"Max Stack Value - {self.max_stack}")
        print("\n")
        return tmp

    def max_element(self):
        tmp = self.max_stack[-1]
        print(f"Max element is - {tmp}")
        print(f"Stack Value - {self.stack}")
        print(f"Max Stack Value - {self.max_stack}")
        print("\n")
        return tmp


if __name__ == "__main__":
    maxstack = MaxStack()
    maxstack.push(10)
    maxstack.push(47)
    maxstack.push(13)
    maxstack.push(50)
    maxstack.push(15)
    maxstack.pop()
    maxstack.max_element()



