class Stack(object):

    def __init__(self):
        self.list = []

    def size_of_list(self):
        return len(self.list)

    def push(self, data):
        self.list.append(data)
        self.print_all()
        return self.list

    def pop(self):
        print(f"poped item - {self.list[-1]}")
        del self.list[-1]
        self.print_all()
        return self.list

    def peek(self):
        return self.list[-1]

    def print_all(self):
        i = 0
        list_size = self.size_of_list()
        while i < list_size:
            print(f"{self.list[i]} ->", end=" ")
            i += 1
        print("\n")


if __name__ == "__main__":
    print("Stack operations")

    st = Stack()
    print("\n Pushed Items")
    st.push(10)
    st.push(20)
    st.push(15)
    st.push(25)

    print("\n Poped Items")
    st.pop()
    st.print_all()
    print("\n Pushed Items")
    st.push(35)
    st.pop()
