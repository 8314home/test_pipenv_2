from collections import Counter


def first_non_unique_char_in_string(input_value: str):
    first_value = ''
    chars_dict = Counter(input_value)
    for c in input_value:
        if chars_dict[c] == 1:
            first_value = c
            break
    return first_value


if __name__ == "__main__":
    input_string = "navneet"
    first_char = first_non_unique_char_in_string(input_string)
    print(f"input_string - {input_string} first_char - {first_char}")
