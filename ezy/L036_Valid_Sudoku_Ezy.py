'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''


class L036_Valid_Sudoku_Ezy:
    # @param {character[][]} board
    # @return {boolean}
    
    # idea:use bitvector or hashmap to check
    def isValidSudoku(self, board):
            if board == None:
                return False

            # bitvectors
            _row = [0 for _ in range(9)]
            _col = [0 for _ in range(9)]
            _blo = [0 for _ in range(9)]

            for i in range(len(board)):
                for j in range(len(board[0])):

                    if board[i][j] != ".":
                        _tem = 1 << (int)(board[i][j])
                        _ind = (i / 3) * 3 + j / 3
                        if _tem & _row[j] or _tem & _col[i] or _tem & _blo[_ind]:
                            return False
                        else:
                            _col[i] = _col[i] | _tem
                            _row[j] = _row[j] | _tem
                            _blo[_ind] = _blo[_ind] | _tem
            return True
