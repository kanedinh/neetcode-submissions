class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        island = 0

        def dfs(row, col):
            q = []
            visited.add((row,col))
            q.append((row,col))

            while q:
                row, col = q.pop()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    island += 1
        return island