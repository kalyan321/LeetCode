class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d=collections.defaultdict(int)
        d[0]=1
        c=0
        summ=0
        for i in nums:
            summ+=i
            c+=d[summ-k]
            d[summ]+=1
        return c 