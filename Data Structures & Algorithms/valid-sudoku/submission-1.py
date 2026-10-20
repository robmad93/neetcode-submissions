class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]: # Using (r // 3, c // 3) makes coordinates that fit 3 * 3 grids inside the board. The integer division is essential for creating 9 specific grid coordinates.
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
        return True

        