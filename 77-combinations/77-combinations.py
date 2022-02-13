class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combination(ind, sub):
            if len(sub) == k:
                res.append(sub)
                return
            if ind > n:
                return
            combination(ind + 1, sub)
            combination(ind + 1, sub + [ind])
        combination(1, [])
        return res