class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def comb(pos, l, summ):
            if summ == target:
                res.append(l)
                return
            if pos >= len(candidates) or summ > target:
                return
            comb(pos, l + [candidates[pos]], summ + candidates[pos])
            comb(pos + 1, l, summ)
        comb(0, [], 0)
        return res