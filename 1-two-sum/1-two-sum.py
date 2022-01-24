class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        d=defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]]=i
        print(d)
        for i in range(len(nums)):
            val=target-nums[i]
            print(d[val])
            if(d[val] and d[val]!=i):
                return [i,d[val]]