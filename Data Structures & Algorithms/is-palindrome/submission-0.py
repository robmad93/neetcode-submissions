class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""

        for ch in s:
            if ch.isalnum():
                palin += ch.lower()
        
        return palin == palin[::-1]

        