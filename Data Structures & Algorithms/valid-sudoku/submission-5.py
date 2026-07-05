class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row wise check - 1X9
        is_valid = True
        for i in range(9):
            row = [x for x in board[i][:] if x != "."]
            col = [board[j][i] for j in range(9) if board[j][i] != "."]

            # print(board[i][:], board[:][i])

            if len(row) != len(set(row)) or len(col) != len(set(col)):
                is_valid = False
                return is_valid

        # box check - 3X3

        def check_3_by_3_board(board_3_by_3: List[str]):
            clean_board = [x for x in board_3_by_3 if x != "."]
            # print("clean_board", clean_board)
            return len(set(clean_board)) == len(clean_board)


        for i in range(3):
            for j in range(3):
                board_3_by_3 = board[i*3][j*3:j*3 + 3] + board[i*3+1][j*3:j*3+3] + board[i*3+2][j*3:j*3+3]
                print(i, j, board_3_by_3, check_3_by_3_board(board_3_by_3))
                if not check_3_by_3_board(board_3_by_3):
                    return False
        return is_valid

        # [
        #     [".",".","4",".",".",".","6","3","."],
        #     [".",".",".",".",".",".",".",".","."],
        #     ["5",".",".",".",".",".",".","9","."],
        #     [".",".",".","5","6",".",".",".","."],
        #     ["4",".","3",".",".",".",".",".","1"],
        #     [".",".",".","7",".",".",".",".","."],
        #     [".",".",".","5",".",".",".",".","."],
        #     [".",".",".",".",".",".",".",".","."],
        #     [".",".",".",".",".",".",".",".","."]
        # ]

        
        