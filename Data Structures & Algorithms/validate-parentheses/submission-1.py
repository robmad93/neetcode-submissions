class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top_element = stack.pop()
                if pairs[top_element] != char:
                    return False
        return len(stack) == 0
                

        
        

        
        