class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or max(grid) == 0:
            return 0
        maxArea = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea