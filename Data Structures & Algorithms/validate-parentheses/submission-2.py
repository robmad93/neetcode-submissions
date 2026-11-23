class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop() # removes closing parentheses
                else:
                    return False
            else:
                stack.append(char) # append opening parentheses
            
        return True if not stack else False
        