'''
    You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
    Return true if the Sudoku board is valid, otherwise return false
    Note: A board does not need to be full or be solvable to be valid.
'''

def validSudoku(board):
    ''' Time complexity: O(n^2)
    Space complexity: O(n) '''

    l = len(board)

    #validate rows
    for i in range(0, l):
        tempSet = set()
        for j in range(0, l):
            if board[i][j] in tempSet and board[i][j] != ".": #duplicate encountered
                return False
            else:
                tempSet.add(board[i][j])
        
    #validate columns
    for i in range(0, l):
        tempSet = set()
        for j in range(0, l):
            if board[j][i] in tempSet and board[j][i] != ".": #duplicate encountered
                return False
            else:
                tempSet.add(board[j][i])
        
    #validate box
    tempDict = {}
    for i in range(0, l):            
        for j in range(0, l):
            if board[i][j] != ".":
                tempTuple = (i // 3, j // 3)
                tempSet = set()
                if tempTuple not in tempDict:
                    tempDict[tempTuple] = set(board[i][j])
                else:
                    existingSet = tempDict[tempTuple]
                    if board[i][j] in existingSet:
                        return False
                    else:
                        existingSet.add(board[i][j])
                        tempDict[tempTuple] = existingSet
    return True

print(validSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))

print(validSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
))