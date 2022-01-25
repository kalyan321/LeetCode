class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i,j,count):
            if grid[i][j] == 2:
                if count == 0:
                    self.ans += 1 
                return
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] != -1:
                    grid[i][j] = -1
                    dfs(x,y,count-1)
                    grid[i][j] = 0
        
        
        self.ans = 0
        count = 0
        for i in grid:
            for j in i:
                if j!=-1:
                    count+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    dfs(i,j,count-1)
        return self.ans