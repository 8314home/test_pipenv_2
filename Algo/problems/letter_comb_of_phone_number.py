from collections import deque


def letter_comb_of_phone_number(input_number_string):

    # Hashmap of number and chars
    number_char_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # Two ques for performing ops

    q1 = deque()
    q2 = deque()

    # Add into queue for 1st number

    for x in number_char_dict[input_number_string[0]]:
        q1.append(x)

    for n in input_number_string[1:]:
        list_of_chars = number_char_dict[n]
        print(f"n - {n} \n list_of_chars- {list_of_chars} \n q1- {q1}")
        q2.clear()                                  # Cleared Q2 before operation
        while q1:
            top_item_from_queue = q1.popleft()      # pop 1 char at a time from q1 and combine it with all chars from list_of_chars
            for c in list_of_chars:
                q2.append(top_item_from_queue + c)  # Adding combined string to Q2
        print(f"q2 after char join- {q2}")
        q1 = q2.copy()                              # Copying back item to Q1
        print(f"q1 after copy- {q1}")

    return list(q1)


if __name__ == "__main__":
    number_string = '238'
    list_of_strings = letter_comb_of_phone_number(number_string)
    print(f"list_of_strings - {list_of_strings}")
    print(f"len of list_of_strings - {len(list_of_strings)}")


