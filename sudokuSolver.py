board = [
    [0,2,6  ,0,0,0  ,8,1,0],
    [3,0,0  ,7,0,8  ,0,0,6],
    [4,0,0  ,0,5,0  ,0,0,7],
    [0,5,0  ,1,0,7  ,0,9,0],
    [0,0,3  ,9,0,5  ,1,0,0],
    [0,4,0  ,3,0,2  ,0,5,0],
    [1,0,0  ,0,3,0  ,0,0,2],
    [5,0,0  ,2,0,4  ,0,0,9],
    [0,3,8  ,0,0,0  ,4,6,0]]

#outputs the final board to the user
def showBoard(board):

    for k in range(12):
         print('-', end=" ")
    print()
    
    for i in range(len(board)):
        #borders
        if i % 3 == 0 and i > 0:
            for k in range(12):
                print('-', end=" ")
            print()
        for j in range(len(board[i])):
            #borders
            if j%3 == 0:
                print('|', end=' ')

            if j == len(board[i]) - 1:
                print(f'{board[i][j]}|')

            else:
                print(board[i][j], end =' ')

    for k in range(12):
         print('-', end=" ")
    print()
            
def isValid(board, num, row, col):
    #checking to see if the number chosen is already in the row
    for i in range(len(board)):
        if board[row][i] == num and i!=col:
            return False

    #checking to see if the number chosen is already in the col
    for i in range(len(board)):
        if board[i][col] == num and i!=row:
            return False
    #checking to see if teh number chosen is not already in the same block
    
    blockRow = row//3
    blockCol = col//3

    for i in range(blockRow * 3, blockRow * 3 + 3):
        for j in range(blockCol * 3, blockCol * 3 + 3):
            if board[i][j] == num and (i != row and j != col):
                return False

    return True

def solve(board):
    #base case where the board no longer has empty spaces
    solved = True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                solved = False
                
    if(solved):
        return True
    
    #looks for first free space
    for i in range(len(board)):
        for j in range(len(board)):
            #free space is found
            if (board[i][j] == 0):
                #tries to enter a number 
                for num in range(1,10):
                    if isValid(board, num, i, j):
                        board[i][j] = num
                        if solve (board):
                             return True
                        board[i][j] = 0
                return False       
                    


def main():
    showBoard(board)
    solve(board)
    print("this is the answer")
    showBoard(board)

main()