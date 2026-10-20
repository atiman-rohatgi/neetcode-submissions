class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        - in this basically all the edge cells cant be surrounded
        - so we create a list of starting points as 0's on the edges.
            - 4 way dfs friom these edge points, and mark all the connected 0's
            - then go over the cells, any 0's that are not marked can be sunk
            - marked ones will be returned back to 0
        Complexity
            - time = O(m*n)
            - space = O(m*n)
        """
        
        #setting things up
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        #dfs function
        def dfs(r, c):
            #base case
            if not (0<= r < rows) or not (0<= c < cols) or board[r][c] != "O":
                return

            #mark
            board[r][c] = "#"
            
            #recurse
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            #nothing to return

        #loop to dfs over the edge cells
        for r in range(rows):
            # Check left and right edges
            if board[r][0] == "O": dfs(r, 0)
            if board[r][cols - 1] == "O": dfs(r, cols - 1)
            
        for c in range(cols):
            # Check top and bottom edges
            if board[0][c] == "O": dfs(0, c)
            if board[rows - 1][c] == "O": dfs(rows - 1, c)

        #main loop - mark x all unmarked 0's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
