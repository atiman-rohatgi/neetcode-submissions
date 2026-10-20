from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - this is a grid bfs question, since we check each level
            - dfs is if exploring if one path leads to ans else backtrack
        - 0's are skipped, 1's are to be rot and 2's will be the start point
        - keep a minute counter, which will increment after each 4-way bfs
        - we will use deque, to implement the q for this
        - we wont use the visited set, just mark them as 2 in place
        - complexity
            - time = O(m*n)
            - space = O(m*n)
        """
        
        #defining things
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        #starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        minute = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        #bfs
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if (0<= nr < rows) and (0<= nc < cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            #every single fruit selected is +1 minute, then bfs to rot nearby
            minute += 1
        
        if fresh == 0:
            return minute
        else:
            return -1
            

