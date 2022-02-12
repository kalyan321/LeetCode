class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in arr:
            res.append([abs(i - x), i])
        res.sort(key=lambda x:(x[0],x[1]))
        print(res)
        ans = []
        for i in range(k):
            ans.append(res[i][1])
        ans.sort()
        return ans