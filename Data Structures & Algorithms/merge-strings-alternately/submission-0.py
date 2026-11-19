class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        l, r = 0, 0
        while l < len(word1) and r < len(word2):
            new_string += word1[l]
            new_string += word2[r]
            l += 1
            r += 1
        if word1[l:]:
            new_string += word1[l:]
        else:
            new_string += word2[r:]
        return new_string
