
def increasingTriplet(nums: list) -> bool:
    first = 1 << 32  # Big +ve value 4294967296
    second = 1 << 32
    third = 1 << 32
    for x in nums:
        if x <= third: #third highest value
            third = x
        elif x <= second: # second highest value
            second = x
        else:
            first = x # highest value
            print(f'third={third} second={second} first = {first}')
            return True
    return False

if __name__ == '__main__':
    input_list = [20,100,4,12,5,13]
    print(increasingTriplet(input_list))