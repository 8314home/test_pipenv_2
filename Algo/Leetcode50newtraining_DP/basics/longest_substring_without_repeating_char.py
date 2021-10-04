class Solution(object):
    def longest_substring_without_repeating_char(self, S):

        # using approach, two pointer & Memorize
        m = dict()
        lp = 0
        rp = 0
        n = len(S)
        ans = 0 # will contain max substring size

        while lp < n and rp < n:
            el = S[rp]
            if el in m:  # if present, move lp past that duplicate index position
                lp = max(lp, m[el]+1)  #setting lp to position after last seen position of el
            m[el] = rp
            ans = max(ans, rp - lp+1)
            rp += 1
            print(f'substring - {S[lp:rp+1]}')
        print(m)
        return ans


if __name__ == '__main__':
    input_string = 'abcabcbb'
    s = Solution()
    print(s.longest_substring_without_repeating_char(input_string))