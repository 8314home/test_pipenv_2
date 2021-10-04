
class Solution:

    def __init__(self):
        self.final_list = []
        self.tmplist = []

    def is_palindrome(self, input_string):
        i = 0
        j = len(input_string) - 1
        while i < j:
            if input_string[i] != input_string[j]:
                return False
            i += 1
            j -= 1
        return True

    def dfs(self, s):
        '''
        Every time we take (Taking a Slice )a range of char from incoming string (c = s[:i]),
         check for palindrome and pass remaining to dfs again for other checking.
         if s is empty and tmplist is filled, we put a copy of tmplist into final list
        :param s:
        :return:

        '''
        print(f's-{s}, fl-{self.final_list}, tmpl-{self.tmplist}')
        if len(s) == 0 and len(self.tmplist) > 0:
            self.final_list.append(self.tmplist[:])
            print(self.final_list)
            return
        n = len(s) + 1  # is done to make sure c=s[:i] can get full string at final position s[:2] at 0 and at 1.
        for i in range(1, n):
            c = s[:i]
            print(f'sliced segment - {c} i={i}')
            if self.is_palindrome(c):
                self.tmplist.append(c)
                print(f'tmpl-{self.tmplist}')
                self.dfs(s[i:])
                self.tmplist.pop()
            else:
                print(f'{c} not palindrome')

    def palindrome_partitions(self, input_string):
        self.dfs(input_string)
        print('-------')
        return self.final_list


if __name__ == '__main__':
    sln = Solution()
    print(sln.is_palindrome('aab'))
    print(sln.palindrome_partitions('aab'))
