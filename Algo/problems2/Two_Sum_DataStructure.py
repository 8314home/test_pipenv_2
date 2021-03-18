class TwoSum(object):

    def __init__(self):
        self.bag_of_numbers = dict()

    def add(self, data):
        if data in self.bag_of_numbers.keys():
            self.bag_of_numbers[data] += 1
        else:
            self.bag_of_numbers[data] = 1

    def find(self, sum_element):
        # Check if dict contains two elements whose sum is sum_element
        print(f"Searching two elements whose sum is - {sum_element}")
        for k in self.bag_of_numbers.keys():
            tmp = sum_element - k

            if tmp in self.bag_of_numbers.keys():
                if tmp == k and self.bag_of_numbers[tmp] < 2:
                    print("No such elements were found\n")
                    return None
                print(f"found Sum - {k}, {tmp}\n")
                return k, tmp
        print("No such elements were found\n")
        return None


if __name__ == "__main__":
    print("Two Sum Problem")

    twosum = TwoSum()
    twosum.add(5)
    twosum.add(1)
    twosum.add(2)
    twosum.add(4)
    twosum.add(5)

    twosum.find(7)
    twosum.find(2)
    twosum.find(10)



