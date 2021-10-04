

# loop- i- from 2 upto SQRT(number)
#     if i is prime then,
#        loop -j - mark all multiples of i to no prime
# End return count(is_prime_list)

import math
target = 35


is_prime_array = [True] * target

for i in range(2,math.ceil(math.sqrt(target))):
    if is_prime_array[i]:
        for j in range(i*i, target, i):
            is_prime_array[j] = False
print(f'count - {sum(is_prime_array)}')

for x in range(target):
    if is_prime_array[x]:
        print(x)
