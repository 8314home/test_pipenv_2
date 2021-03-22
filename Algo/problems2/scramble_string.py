from collections import Counter


def scramble_string(input_string_1, input_string_2):

    print(f"input_string_1={input_string_1} input_string_2={input_string_2}")

    if input_string_1 == input_string_2:
        return True

    if dict(Counter(input_string_1)) != dict(Counter(input_string_2)):
        print(f"{dict(Counter(input_string_1))} and {dict(Counter(input_string_2))}")
        return False

    for i in range(len(input_string_1)-1):  # we are taking till last but 1 position

        i += 1  # this being done to avoid infinite recursion, as list :i take element before ith place

        flag_1 = scramble_string(input_string_1[:i], input_string_2[:i])
        flag_2 = scramble_string(input_string_1[i:], input_string_2[i:])

        print(f"flag_1 = {flag_1}")
        print(f"flag_2 = {flag_2}")

        if flag_1 and flag_2:
            print("Red circle")
            return True

        flag_3 = scramble_string(input_string_1[:i], input_string_2[len(input_string_2) - i:])
        flag_4 = scramble_string(input_string_1[len(input_string_1) - i:], input_string_2[:i])

        print(f"flag_3 = {flag_3}")
        print(f"flag_4 = {flag_4}")

        if flag_3 and flag_4:
            print("Green box")
            return True

    return False


if __name__=="__main__":

    string_1 = 'great'
    string_2 = 'rgeat'

    print(f"{string_1} and {string_2} are scrambled ? {scramble_string(string_1, string_2)}")
