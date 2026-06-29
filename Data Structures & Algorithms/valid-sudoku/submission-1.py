class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every line to see if there are any repetitive chars
        for line_no in range(9):
            line_set = set()
            for column_no in range(9):
                if board[line_no][column_no] != "." and board[line_no][column_no] in line_set:
                    return False
                line_set.add(board[line_no][column_no])
        
        # check every columns to see if there are any repetiive cahrs
        for column_no in range(9):
            columns_set = set()
            for line_no in range(9):
                if board[line_no][column_no] != "." and board[line_no][column_no] in columns_set:
                    return False
                columns_set.add(board[line_no][column_no])
        
        # check every 9 square to see if there are any repetitive chars
        for line_no in range(0,9,3):
            for columns_no in range(0,9,3):
                square_set = set()
                for i in range(line_no, line_no + 3):
                    for j in range(columns_no, columns_no + 3):
                        if board[i][j] != "." and board[i][j] in square_set:
                            return False
                        square_set.add(board[i][j])
        
        return True
