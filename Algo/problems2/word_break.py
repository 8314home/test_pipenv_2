
def fn_word_break(dict_of_words, input_string):
    list_of_words = []
    tmp = ''
    for c in input_string:
        tmp += c
        if tmp in dict_of_words:
            list_of_words.append(tmp)
            tmp = ''
    return list_of_words


if __name__ == "__main__":

    set_of_words = {'I', 'like', 'ice', 'cream', 'sam', 'sung', 'samsung', 'mobile', 'icecream'}
    test_string = "Ilikeicecream"

    print(f"word break of {test_string} is {fn_word_break(set_of_words, test_string)}")




