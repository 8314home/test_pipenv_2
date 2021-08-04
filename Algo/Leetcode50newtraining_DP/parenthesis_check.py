def parenthesis_check(input_str: str):
    dict_p = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    stack = []
    all_parenthsis_values = [*dict_p.keys(), *dict_p.values()] # chaining keys and values together - all_parenthsis_values
    print(f"all_parenthsis_values - {all_parenthsis_values}")

    if len(input_str) == 0:
        return True

    for x in input_str:
        if x not in all_parenthsis_values:  # all_parenthsis_values - ['[', '{', '(', ']', '}', ')']
            continue
        if len(stack) == 0:
            stack.append(x)
            continue
        stack_top = stack[-1]
        if dict_p.get(stack_top) == x:
            print(f"stack_top-{stack_top} x={x}")
            del stack[-1]
        else:
            stack.append(x)
    print(f"final stack content - {stack}")
    return len(stack) == 0


if __name__ == "__main__":
    INPUT = '[{1+4}/6]){}('
    print("Parenthesis check of {0} is {1}".format(INPUT, parenthesis_check(INPUT)))
