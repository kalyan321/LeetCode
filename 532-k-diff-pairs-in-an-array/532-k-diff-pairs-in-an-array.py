class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        nums.sort()
        i = 0
        j = 1
        count = 0
        while (i < j and j < n):
            if nums[j] - nums[i] == k:
                j += 1
                count += 1
                while j < n and nums[j] == nums[j-1]:
                    j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                j += 1
            if i == j:
                j += 1
        return count
                
                    