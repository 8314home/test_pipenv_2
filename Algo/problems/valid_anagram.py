from collections import Counter


def valid_anagram(a: str, b: str):

    if len(a) != len(b):
        return False
    counter_a = Counter(a)
    print(counter_a)

    for i in b:
        if i in counter_a:
            counter_a[i] -= 1
            if counter_a[i] == 0:
                del counter_a[i]

    if counter_a:
        print(f"some values still present - {counter_a}")
        return False
    else:
        return True


if __name__=="__main__":
    string1='raganam'
    string2='agrnaam'

    print(valid_anagram(string1, string2))
