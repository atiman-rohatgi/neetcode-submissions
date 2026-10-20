class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        - this is backtrack + dfs + visited set
        - we move in all 4 directions while within range using (r, c)
        - stop when len(curr) > len(word) or the current word dont match index word
        - compre with the index wise word
        - complexity
            - time = 
            - space = 
        """

        rows = len(board) 
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):
            #base, exit
            if i == len(word): #word found
                return True
            if not (0 <= r < rows) or not (0 <= c < cols) or (r,c) in visited or board[r][c] != word[i]: #early exit
                return False
            
            #explore
            visited.add((r, c))
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in dirs:
                if dfs(r+dr, c+dc, i+1) == True:
                    return True

            #undo
            visited.remove((r,c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0) == True:
                    return True
                
        return False