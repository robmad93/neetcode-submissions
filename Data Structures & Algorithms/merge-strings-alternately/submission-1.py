class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # It makes for better space complexity to use an array over a string.
        merged = []
        l, r = 0, 0
        while l < len(word1) and r < len(word2):
            merged.append(word1[l])
            merged.append(word2[r])
            l += 1
            r += 1
        if word1[l:]:
            merged.append(word1[l:])
        else:
            merged.append(word2[r:])
        return "".join(merged)