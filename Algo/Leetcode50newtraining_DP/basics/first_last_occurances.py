class Solution(object):

    def first_occurance(self, A, t):
        # sorted array , find something , think of binary search as best result

        n = len(A)
        lp = 0
        rp = n - 1

        while lp <= rp:
            mid = (lp + rp) // 2
            if A[mid] == t:  # found target match
                if mid == 0 or A[mid - 1] != t:  # means mid pos is the 1st pos of target
                    return mid
                rp = mid - 1
            elif t < A[mid]:
                rp = mid - 1
            else:
                lp = mid + 1

    def last_occurance(self, B, t):
        n = len(B)
        lp = 0
        rp = n - 1

        while lp <= rp:
            mid = (lp + rp) // 2
            if B[mid] == t:  # found target match
                if mid == (n-1) or B[mid + 1] != t:  # means mid pos is the last pos of target
                    return mid
                lp = mid + 1
            elif t < B[mid]:  # means target must be before current mid
                rp = mid - 1
            else:
                lp = mid - 1


if __name__ == '__main__':

    input_list = [9,10,11,11,11,12,14]
    target = 11
    s = Solution()

    print(f'First occurance position(0 based) - {s.first_occurance(input_list, target)}')
    print(f'Last occurance position(0 based)- {s.last_occurance(input_list,target) }')