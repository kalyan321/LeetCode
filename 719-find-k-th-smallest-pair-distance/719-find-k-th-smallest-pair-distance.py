import math
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countpairs(d):
            count = 0
            left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > d:
                    left += 1
                count += right - left
            return count
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (low + high)//2
            if countpairs(mid) >= k:
                high = mid
            else:
                low =  mid + 1
        return low