class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def kadane(arr, curr = 0, res = 0):
            for num in arr:
                curr = max(num, num + curr)
                res = max(res, curr)
            return res
        if k > 1:
            return ((k - 2) * max(sum(arr), 0) + kadane(arr * 2)) % (10**9 + 7)
        return kadane(arr) % (10 ** 9 + 7)