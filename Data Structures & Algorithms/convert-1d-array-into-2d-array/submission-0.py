class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        pass
        # Check if total elements match m * n dimensions exactly
        if len(original) != m * n:
            return []

        # Build 2D matrix by slicing original array row by row
        result = []
        for i in range(m):
            # Slice the n elements for row i
            row = original[i * n : (i + 1) * n]
            result.append(row)

        return result
