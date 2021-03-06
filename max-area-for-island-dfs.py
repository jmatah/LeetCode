class Solution:
    def calculateIsland(self, grid:list[list[int]], i:int,j:int)-> int:
        curCount = 0
        if grid[i][j] == 1:
            curCount += 1
            grid[i][j] = 0
            if i - 1 >= 0:
                curCount += self.calculateIsland( grid, i-1, j)
            if j + 1 < len(grid[0]):
                curCount += self.calculateIsland( grid, i, j + 1 )
            if i + 1 < len(grid):
                curCount += self.calculateIsland( grid, i + 1, j )
            if j - 1 >= 0:
                curCount += self.calculateIsland( grid, i, j - 1 )
        return curCount 

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if len(grid) == 0: 
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0 
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max( res, self.calculateIsland(grid, i,j))

        return res

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[0,1],[1,1]]
sol = Solution()
max = sol.maxAreaOfIsland(grid)
print(max)