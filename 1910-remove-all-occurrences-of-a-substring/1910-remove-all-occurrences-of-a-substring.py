class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = s[:len(part)]
        for i in range(len(part), len(s)):
            while len(stack) >= len(part) and stack[len(stack) - len(part) : ] == part:
                print(stack)
                stack = stack[ : len(stack) - len(part)]
                print(stack)
            stack += s[i]
        while len(stack) >= len(part) and stack[len(stack) - len(part) : ] == part:
                print(stack)
                stack = stack[ : len(stack) - len(part)]
                print(stack)
        return "".join(stack)
        