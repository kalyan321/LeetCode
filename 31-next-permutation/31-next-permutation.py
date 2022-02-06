class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        flag = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                flag = 1
                j = i + 1
                while j < len(nums):
                    if nums[i] >= nums[j]:
                        break
                    j += 1
                nums[i],nums[j-1] = nums[j-1], nums[i]
                nums[i+1:] = nums[i+1:len(nums)][::-1]
                break
        if flag == 0:
            nums[:] = nums[::-1]
        