class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        - we make a count, count number of 1's in each row and col
        - whenever we encounter a 1, we check if row or col > 1, if yes then count += 1
        - return the count
        - complexity
            - Time = O(m*n)
            - Space = O(m+n)
        """
        
        rows = len(grid)
        cols = len(grid[0])
        
        #make a count list
        row_c = [0]*rows
        col_c = [0]*cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_c[r] += 1
                    col_c[c] += 1

        #counting the actual servers
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_c[r]>1 or col_c[c]>1):
                    res += 1

        return res


