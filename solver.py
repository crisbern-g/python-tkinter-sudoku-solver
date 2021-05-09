def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def findEmpty(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)
    
    return None


def isValid(board, input, position):
    #check row
    for column in range(len(board[0])):
        if board[position[0]][column] == input and position[1] != column:
            return False

    #check column
    for row in range(len(board[0])):
        if board[row][position[1]] == input and position[0] != row:
            return False

    #check box
    box_row = position[0] // 3
    box_column = position[1] // 3

    for row in range(box_row * 3, (box_row * 3) + 3):
        for column in range(box_column * 3, (box_column *3) + 3):
            if board[row][column] == input and (row, column) != position:
                return False

    return True


def solve(board):
    vacantSquare = findEmpty(board)

    if vacantSquare == None:
        return True
    else:
        row, column = vacantSquare

    for input in range (1, 10):
        if isValid(board, input, (row, column)):
            board[row][column] = input
            
            if solve(board):
                return True

            board[row][column] = 0

    return False