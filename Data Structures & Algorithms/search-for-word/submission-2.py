from collections import deque
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def bfs(row, col):
            queue = deque()
            queue.append((row, col, 1, {(row, col)}))  
            # row, col, next index in word, visited cells for this path

            while queue:
                row, col, counter, visited = queue.pop()

                if counter == len(word):
                    return True

                # top
                if (
                    row - 1 >= 0
                    and (row - 1, col) not in visited
                    and board[row - 1][col] == word[counter]
                ):
                    queue.append(
                        (row - 1, col, counter + 1, visited | {(row - 1, col)})
                    )

                # bottom
                if (
                    row + 1 < len(board)
                    and (row + 1, col) not in visited
                    and board[row + 1][col] == word[counter]
                ):
                    queue.append(
                        (row + 1, col, counter + 1, visited | {(row + 1, col)})
                    )

                # left
                if (
                    col - 1 >= 0
                    and (row, col - 1) not in visited
                    and board[row][col - 1] == word[counter]
                ):
                    queue.append(
                        (row, col - 1, counter + 1, visited | {(row, col - 1)})
                    )

                # right
                if (
                    col + 1 < len(board[0])
                    and (row, col + 1) not in visited
                    and board[row][col + 1] == word[counter]
                ):
                    queue.append(
                        (row, col + 1, counter + 1, visited | {(row, col + 1)})
                    )

            return False

        len_row = len(board)
        len_col = len(board[0])

        for i in range(len_row):
            for j in range(len_col):
                if board[i][j] == word[0]:
                    if bfs(i, j):
                        return True

        return False