# * can be considered as an empty string or ( or ) - based on the requirement
from collections import deque


def fn_valid_parethesis_string(input_string):

    stack_1 = deque()  # stack for left parenthesis (
    stack_2 = deque()  # stack for star *

    for i in range(len(input_string)):
        c = input_string[i]
        if c == '(':
            stack_1.append(i)  # stack for left parenthesis (
        elif c == '*':
            stack_2.append(i)   # stack for star *
        else:  # found a ')'
            if stack_1:
                stack_1.pop()
            elif stack_2:
                stack_2.pop()
            else:
                return False

    while stack_1 and stack_2:
        if stack_1[0] < stack_2[0]:     # for a string like (*
            stack_1.pop()
            stack_2.pop()
        else:                           # for a string like *(
            return False

    if stack_1:                         # Meaning still some ( are left
        return False
    else:
        return True


if __name__ == "__main__":

    parethesis_string = "(((*))))*("

    print(f"Validation of {parethesis_string} is {fn_valid_parethesis_string(parethesis_string)}")
