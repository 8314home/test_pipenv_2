from collections import Counter

string_a = 'bacbababcbbca'
string_b = 'abc'

# All anagrams from string
# Program should return starting index of all possible anagrams in the list format
# We can solve this using the help of two stacks
# stack -1 will contain histogram of string_b
# from string_a we will take string part of len(string_b) and calculate corresponding string_part histogram
# and look for histogram matching

result_list = []
hist_b = dict(Counter(string_b))
print(hist_b)

start_string_part = 0
end_string_part = len(string_b)
hist_a=dict()

while end_string_part < len(string_a):
    hist_a.update(dict(Counter(string_a[start_string_part: end_string_part])))
    print(f"hist_a - {hist_a}")
    if hist_b == hist_a:
        result_list.append(start_string_part)
        print("Match found")
    start_string_part += 1
    end_string_part += 1

print(f"final_list_result - {result_list}")
