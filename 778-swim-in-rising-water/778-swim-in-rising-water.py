class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0],0,0)]
        ans = 0
        visited = set([(0,0)])
        while True:
            d, r, c = heapq.heappop(heap)
            ans = max(ans,d)
            if r == c == (len(grid) -1):
                return ans
            for i, j in [(r + 1, c), (r - 1, c),(r, c + 1), (r, c - 1)]:
                if (i,j) not in visited and 0<=i<len(grid) and 0<=j<len(grid):
                    visited.add((i,j))
                    heapq.heappush(heap, (grid[i][j], i, j))
