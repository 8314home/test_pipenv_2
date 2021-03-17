import logging
from collections import Counter


def top_n_frequently_occuring_element(input_list, n):
    clist = dict(Counter(input_list))
    list_of_top_n_items = list(t[0] for t in sorted(clist.items(), key=lambda x: x[1], reverse=True)[:n])
    return list_of_top_n_items


if __name__ == "__main__":
    initial_list = [1,2,1,3,4,2,1,2,3,3,1,3,4,1]
    k = 3

    logger = logging.getLogger("top_n_frequently_occuring_element")
    logger.setLevel("WARN")

    logger.warning(f"top_n_frequently_occuring_element - {top_n_frequently_occuring_element(initial_list,k)}")


