
def findTarget(i, s, path,final_set):
    if s == 0:
        print(path)
        return
    if i == len(nums):
        return
    findTarget(i+1, s-nums[i], path + [nums[i]],final_set)
    findTarget(i+1, s, path, final_set)



nums = [1,4,3,2,6,5,8,7]
target = 9
count = 0
final_set = set()
for i in range(len(nums)):
    path = []
    findTarget(i, target, path)


