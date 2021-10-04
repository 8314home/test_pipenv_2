# sort + left, right pointer
# when left + right <= limit fit them in 1 boat
# when NOT, 1 boat for heavy
# when last person left , 1 boat last person


class Solution:

    def save_people_boat(self, arr, limit):
        arr.sort()
        boat = 0
        lp = 0
        rp = len(arr)-1

        while lp <= rp:
            # last person remaining, lp==rp
            if lp == rp:
                boat += 1
                break
            # When light & heavy fit
            if arr[lp] + arr[rp] <= limit:
                boat += 1
                lp += 1
                rp -= 1
            else:
                # need a boat for heavy person
                boat += 1
                rp -= 1
        return boat


if __name__ == '__main__':

    input_list = [2,3,2,5,4]
    input_limit = 6
    # ans = 3

    s = Solution()
    print(s.save_people_boat(input_list, input_limit))
