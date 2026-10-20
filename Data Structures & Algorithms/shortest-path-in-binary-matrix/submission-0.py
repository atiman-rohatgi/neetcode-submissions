from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        - basically it is 8-way we can move
        - find shortest path to n-1, n-1, track the number of 0's
        - grid bfs
        - 0's is open path while 1's are the wall
        - edge cases, if start or end is 1, then return -1
        - complexity
            - time = O(m*n)
            - space = O(m*n)
        """

        #setting things up
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        steps = 1 #first cell is pre counted
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

        #edge cases
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        #starting case
        q.append((0, 0))
        visited.add((0, 0))

        #bfs
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                #target check
                if (r == rows-1) and (c == cols-1):
                    return steps
                
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if (0<= nr < rows) and (0<= nc < cols) and (nr, nc) not in visited and grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            steps += 1
        return -1
