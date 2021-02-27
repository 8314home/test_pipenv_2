class Queue(object):
    def __init__(self):
        self.queue = list()
        print(f"Queue - {self.queue}")

    def enqueue(self, data):
        self.queue.append(data)
        print(f"Queue - {self.queue}")

    def dequeue(self):
        tmp = self.queue[0]
        del self.queue[0]
        print(f"Removed element {tmp}")
        print(f"Queue - {self.queue}")


if __name__ == "__main__":

    qq = Queue()
    qq.enqueue(10)
    qq.enqueue(20)
    qq.enqueue(30)
    qq.enqueue(40)
    qq.dequeue()

