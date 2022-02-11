class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ''
        for i in range(len(s)):
            stack += s[i]
            while len(stack) >= len(part) and stack[len(stack) - len(part) : ] == part:
                print(stack)
                stack = stack[ : len(stack) - len(part)]
                print(stack)
        return "".join(stack)
        