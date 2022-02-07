class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.count = 0
        stack = []
        
        def bfs():
            while stack:
                self.count += 1
                for i in range(len(stack)):
                    ele = stack.pop(0)
                    r, c = ele[0], ele[1]
                    for nr,nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                            grid[nr][nc] = 3
                            stack.append([nr,nc])
            self.count -= 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = 3
                    stack.append([i,j])
        
        if len(stack) > 0:
            bfs()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return self.count