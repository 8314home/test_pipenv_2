class Solution(object):

    def is_mountain_array(self, A):

        if len(A)<3:
            return False
        i=1

        while i<len(A) and A[i-1] < A[i]:
            i += 1
        # check if we are still at 1st or last position then means not a mountain array
        if i == 1 or i == len(A)-1:
            return False

        while i<len(A) and A[i-1] > A[i]:
            i += 1
        return i == len(A)


if __name__ == '__main__':

    input_list = [1,2,4,6,3,5,1]
    s=Solution()
    print(s.is_mountain_array(input_list))