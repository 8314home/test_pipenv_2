import logging
import sys
import os
from configparser import ConfigParser
from pathlib import Path

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add_node(self,data):

        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = Node(data)
        return self.head

    def traverse(self, input_log: logging.Logger):
        current_node = self.head
        while current_node:
            input_log.info(f"{current_node.data} ->", end="")
            current_node = current_node.next_node

    def rotate_list(self, input_no_of_rotations):

        list_size = 0
        current_node = self.head
        while current_node:
            list_size += 1
            current_node = current_node.next_node

        k = list_size - input_no_of_rotations
        k = k % list_size  # this is done in case list size is 5 and rotations are 8

        if k == 0 or list_size == 1 or list_size == k or self.head is None:
            return self.head

        current_node = self.head
        previous_node = None
        for i in range(k):
            previous_node = current_node
            current_node = current_node.next_node

        previous_node.next_node = None
        tmp = current_node

        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = self.head
        self.head = tmp

        return self.head


def create_logger():
    # create logger
    logger = logging.getLogger(__name__)

    # create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(filename='sample.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    # create formatter
    c_formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    f_formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    c_handler.setFormatter(c_formatter)
    f_handler.setFormatter(f_formatter)

    # add handlers to logger objects
    logger.addHandler(f_handler)
    logger.addHandler(c_handler)

    return logger


if __name__ == "__main__":



    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)

    log = create_logger()
    print(type(log))
    log.warning("Sample log generation")
    log.warning(f"{type(log)}")

    ll.traverse(log)

    ll.rotate_list(2)

    print("\n")
    ll.traverse(log)
    log.error("Sample log generation ERROR")

    sys.path.append(os.path.abspath(Path(__file__).resolve().parent.parent))

    print(f"{Path(__file__).resolve().parent.parent}")
    filename_config_ini = os.path.join(Path(__file__).resolve().parent.parent, 'problems/config.ini')
    print(f"filename_config_ini= {filename_config_ini}")

    props = ConfigParser()
    props.read(filenames=filename_config_ini)

    log.warning(f"{props.sections()}")
    log.warning(f"{props['dev']['config_name_1']}")

    print(f"")
