class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def XORSum(pos, val):
            if pos >= len(nums):
                self.ans += val
                return
            XORSum(pos + 1, val ^ nums[pos])
            XORSum(pos + 1, val)
        XORSum(0, 0)
        return self.ans