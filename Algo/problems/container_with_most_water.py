def container_with_most_water(input_array):
    # index 0 to n on x axis represents base
    # list values at every index represent the height
    # need to take min between heights
    # Every iteration,
    # Two pointers start and end
    # find min between two heights * difference between  start and end index
    # area = min(h1,h2) * (index[h2]-index[h1])
    # if new area is greater than old area set it and keep x=index[h2], y=index[h1]
    # finally return index positions

    start = 0
    end = len(input_array)-1
    area = 0
    x,y = 0,0
    while start < end:
        base = end - start
        height = min(input_array[start], input_array[end])
        if area < base * height:
            area = base * height
            x = start
            y = end
        if input_array[start] < input_array[end]:
            start += 1 # means there is possibility that next start value will make area more
        else:
            end -= 1 # means there is possibility that next end value will make area more

    # x,y are co-ordinates
    return x,y,area

if __name__ == "__main__":

    a,b,area_value = container_with_most_water([1,8,6,2,5,4,8,3,7])
    print(a,b,area_value)
