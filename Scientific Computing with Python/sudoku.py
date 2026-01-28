class Board:
    def __init__(self, board):
        self.board = board
        
    def __str__(self):
        board_str = ''
        for row in self.board:    
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None
    
    def is_valid_row(self, row, num):
        return num not in self.board[row]
    
    def is_valid_col(self, col, num):
        return all([self.board[row][col] != num for row in range(9)])
    
    def is_valid_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False 
        return True  
    
    def is_valid(self, empty, num):
        row, col = empty
        is_valid_square = self.is_valid_square(row, col, num)
        is_valid_row = self.is_valid_row(row, num)
        is_valid_col = self.is_valid_col(col, num)
        return all([is_valid_row, is_valid_col, is_valid_square])
    
    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1,10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True 
                self.board[row][col] = 0
        return False
            
def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard
    
puzzle = [
  [0, 0, 3, 0, 0, 4, 0, 0, 0],
  [4, 0, 0, 0, 0, 0, 6, 9, 2],
  [9, 2, 0, 0, 6, 0, 7, 0, 0],
  [0, 0, 0, 0, 0, 0, 9, 4, 0],
  [0, 0, 0, 5, 0, 7, 0, 0, 8],
  [0, 8, 0, 0, 9, 0, 0, 0, 0],
  [0, 0, 0, 3, 0, 6, 2, 0, 0],
  [0, 0, 1, 0, 5, 2, 4, 0, 0],
  [6, 0, 2, 0, 0, 0, 3, 5, 0]
]

solve_sudoku(puzzle)