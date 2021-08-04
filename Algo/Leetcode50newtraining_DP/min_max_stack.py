class MyStack:

    def __init__(self):
        self.stk = []

    def push(self, x):
        if len(self.stk) == 0:
            self.stk.append((x, x, x))
        else:
            get_min = self.min_value_of_stack()
            get_max = self.max_value_of_stack()

            if x < get_min:
                self.stk.append((x, x, get_max))
            elif get_max < x:
                self.stk.append((x, get_min, x))
            else:
                self.stk.append((x, get_min, get_max))
        print("push - {0}".format(self.stk))

    def pull(self):
        value = self.stk[-1][0]
        del self.stk[-1]
        return value

    def peek(self):
        return self.stk[-1][0] if self.stk else None

    def min_value_of_stack(self):
        return self.stk[-1][1] if self.stk else None

    def max_value_of_stack(self):
        return self.stk[-1][2] if self.stk else None

    def show(self):
        map(lambda x: print(x[0]), self.stk)


if __name__ == "__main__":
    print("Stack create")

    mystk = MyStack()
    mystk.push(3)
    mystk.push(6)
    mystk.push(1)
    mystk.push(4)
    mystk.push(5)

    print("All Values")
    mystk.show()

    print("Pull Values")
    mystk.pull()

    print("Max and Min Values")
    print("Min - {0} Max - {1}".format(mystk.min_value_of_stack(), mystk.max_value_of_stack()))
