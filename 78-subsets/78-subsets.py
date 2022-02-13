class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def subsets(pos, sub):
            if pos >= len(nums):
                return res.append(sub)
            subsets(pos + 1, sub), subsets(pos + 1, sub + [nums[pos]])
        subsets(0, [])
        return res