from collections import deque

pol_list = ['2','4','+','6','*']

# define a stack
# loop through list
# if a number push into stack
# if a operator pop- 2 items and perform operation and push result into stack
# return final result

stack = deque()

for x in pol_list:
    if x == '*' or x == '-' or x == '+' or x == '/':
        b = stack.pop()
        a = stack.pop()
        result = 0
        if x == '*':
            result = a * b
        elif x == '-':
            result = a - b
        elif x == '+':
            result = a + b
        else:
            result = a / b
        stack.append(result)
    else:
        stack.append(int(x))
final_result = stack.pop()
print(f"final result - {final_result}")

