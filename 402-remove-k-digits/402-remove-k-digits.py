class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while True:
                if k == 0 or not stack:
                    break
                if stack[-1] > num[i]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[i])
        while k and stack:
            k -= 1
            stack.pop()
        if not stack:
            return '0'
        return str(int("".join(stack)))