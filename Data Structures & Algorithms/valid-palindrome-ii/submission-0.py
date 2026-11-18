class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                left_slice = s[l + 1:r + 1]
                right_slice = s[l:r]
                return left_slice == left_slice[::-1] or right_slice == right_slice[::-1]

        return True



        