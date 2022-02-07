class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr = [0]*26
        for i in s:
            arr[ord(i) - 97] += 1
        for i in t:
            arr[ord(i) - 97] -= 1
        for i in range(len(arr)):
            if arr[i] != 0:
                return chr(97+i)