class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        def get_neighbors(row, col):
            neighbors = []
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n:
                    neighbors.append([r, c])
            return neighbors

        def bfs(seeds):
            reached = [[False] * n for _ in range(m)]
            queue = []
            for r, c in seeds:
                reached[r][c] = True
                queue.append([r, c])
            while queue:
                new_queue = []
                for row, col in queue:
                    for x, y in get_neighbors(row, col):
                        if not reached[x][y] and heights[x][y] >= heights[row][col]:
                            reached[x][y] = True
                            new_queue.append([x, y])
                queue = new_queue
            return reached

        pacific = bfs([[0, c] for c in range(n)] + [[r, 0] for r in range(m)])
        atlantic = bfs([[m - 1, c] for c in range(n)] + [[r, n - 1] for r in range(m)])

        return [[r, c] for r in range(m) for c in range(n)
                if pacific[r][c] and atlantic[r][c]]
        