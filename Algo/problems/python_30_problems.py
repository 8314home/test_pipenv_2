# 5.
#  Write a Python program to count the number of strings
#  where the string length is 2 or more
#  and the first and last character are same
#  from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

sample_list_pr5 = ['abc', 'xyz', 'aba', '1221']

print("program-5")
print(list(filter(lambda x: len(x) > 2 and x[0] == x[-1], sample_list_pr5)))



# 6.
# Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

print("\nprogram-6")
sample_list_pr6=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# sorted return a new list
print(sorted(sample_list_pr6, key=lambda t: t[1], reverse=True))


# 12.
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

print("\nprogram-12")
sample_list_pr12=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(list(enumerate(sample_list_pr12)))

print([x[1] for x in list(enumerate(sample_list_pr12)) if x[0] not in (0,4,5)])


#  13.
# Write a Python program to generate a 3*4*6 3D array whose each element is the index

print("\nprogram-13")
array_3d = [[[(i,j,k) for k in range(3)] for j in range(4)] for i in range(6)]
print(array_3d)

#  17. Write a Python program to generate and print a list except for the first 5 elements and lst 5 elements
#  , where the values are square of numbers between 1 and 30 (both included).

print("\nprogram-17")
sample_list_pr17 = [i**2 for i in range(1, 31)]
print(sample_list_pr17)

print(sample_list_pr17[5:-5])


# Python | Merge Python key values to list

# while working with Python, we might have a problem in which we need to get the values of dictionary
# from several dictionaries to be encapsulated into one dictionary

# Input
# test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
#              {'it' : 5, 'is' : 7, 'best' : 8},
#              {'CS' : 10}]

# Output
# {‘is’: [4, 7], ‘it’: [5], ‘gfg’: [2], ‘CS’: [10], ‘best’: [6, 8]}

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
             {'it' : 5, 'is' : 7, 'best' : 8},
             {'CS' : 10}]

result_set=dict()

for elem in test_list:
    for key, value in elem.items():
        result_set.setdefault(key, []).append(value)

print("\ndict problem -1")
print(f"test_list - {test_list}")
print(f"result_set - {result_set}")

# setdefault(key,default_value) - Insert key with a value of default_value if key is not in the dictionary.
# Return the value for key if key is in the dictionary,

# 1. Write a Python program to sort (ascending and descending) a dictionary by value.
print("program -1")
d = {1: 2, 10: 4, 4: 4, 3: 3}


#  sorted(d.items(), key=lambda x: x[1])) is returning a list that can be converted to dict()
print(dict(sorted(d.items(), key=lambda x: x[1])))

print(dict(sorted(d.items(), key=lambda x: x[0], reverse=True)))

# 3. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

result_dict=dict()

for d in [dic1, dic2, dic3]:
    result_dict.update(d)

print(f"\nresult_dict")
print(result_dict)

# 4. Write a Python script to check whether a given key already exists in a dictionary.
print("\n\n program -3,4")

check_key=2

if check_key in result_dict.keys():
    print(f"check_key- {check_key} exists in {result_dict}")

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys. Go to the editor
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

dict_prog_7=dict()

for i in range(1,16):
    dict_prog_7[i]=i**2

print(f"dict_prog_7 - {dict_prog_7}")


# 19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
print("\n\n program -19")

#Option-1 using collections module

# Counter - is a subclass of dict for counting items, elements are stored in Counter keys and counts in values.

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
result_dict_19=Counter(d1) + Counter(d2)
print(f"result_dict_19 - {dict(result_dict_19)}")

# Option 2 using zip

for comb in zip(d1.items(),d2.items()):
    print(comb)

d1_keys=d1.keys()
d2_keys=d2.keys()
result_dict_19_2=d1.copy()

for key in d2_keys:
    if key in d1_keys:
        result_dict_19_2[key] = result_dict_19_2[key] + d2[key]
    else:
        result_dict_19_2[key] = d2[key]

print(f"d1= {d1} d2={d2}")
print(f"result_dict_19_2 - {result_dict_19_2}")

# 20 Write a Python program to print all unique values in a list of dictionaries. Go to the editor
# Sample Data :
# [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
print("\n\n program -20")


Sample_Data_20 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

set_of_values=set()

for dicts in Sample_Data_20:
    for v in dicts.values():
        set_of_values.add(v)

print(f"set_of_values - {set_of_values}")

# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different
# key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

print("\n\n program -21")
import itertools

sample_data_21 = {'1':['a','b'], '2':['c','d']}

print(sample_data_21.values())
print(*sample_data_21.values())

for comb in itertools.product(*sample_data_21.values()):
    print(''.join(comb))


# 22. Write a Python program to find the highest 3 values in a dictionary. Go to the editor
# Click me to see the sample solution

print(f"program-22")
sample_dict_22 = {'a': 10, 'b': 8, 'c': 101, 'd': 30, 'e': 70}

print(sorted(sample_dict_22.values(), reverse=True)[:3])

# 25. Write a Python program to print a dictionary in table format. Go to the editor
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# expected o/p
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11
print(f"program-25")

my_dict_25 = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# defining a list with key, [key] & adding value
for key, value in sorted(my_dict_25.items()):
    print([key] + value)

print(([key] + value for key, value in my_dict_25.items()))

# The * in a function call "unpacks" a list(or other iterable), making each of its elements a separate argument.

l2 = list([key] + value for key, value in my_dict_25.items())
print(l2)

for row in zip(*([key] + value for key, value in my_dict_25.items())):
    print(row)
    print(*row)

# 26. Write a Python program to count the values associated with key in a dictionary. Go to the editor
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True