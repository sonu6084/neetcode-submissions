class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## rows
        for row in range(0,9):
            row_dict = {}
            for col in range(0,9):
                row_dict[board[row][col]] = 1+row_dict.get(board[row][col],0)
                if row_dict[board[row][col]] > 1 and board[row][col] != ".":
                    return False
        
        for col in range(0,9):
            col_dict = {}
            for row in range(0,9):
                col_dict[board[row][col]] = 1+col_dict.get(board[row][col],0)
                if col_dict[board[row][col]] > 1 and board[row][col] != ".":
                    return False

        
        row_col_pairs = [[0,2,0,2],[0,2,3,5],[0,2,6,8],[3,5,0,2],[3,5,3,5],[3,5,6,8],[6,8,0,2],[6,8,3,5],[6,8,6,8]]

        for size in row_col_pairs:
            box_dict = {}
            for row in range(size[0],size[1]+1):
                for col in range(size[2],size[3]+1):
                    box_dict[board[row][col]] = 1 + box_dict.get(board[row][col],0)
                    if box_dict[board[row][col]] > 1 and board[row][col] != ".":
                        return False

        return True