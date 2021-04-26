#                        N QUEEN PROBLEM 
#  A n x n chessboard is there and in the board we have to place n queen in suCh a way that no queen can kill each other.
#           A queen will kill another queen if two queen either placed in same row, or same column or in the diagonal, otherwise queens are safe .
#   So have to find the way where all queen will be placed safely. there can be a multiple way to placed the queen in the chessboard, print all the possible ways...

# Input : queen = 4
# Output : 0-1, 1-3, 2-0, 3-2,
#          0-2, 1-0, 2-3, 3-1,      these two possible combinations are possible where queens will be safe.



def queenSafe(chessBoard, row, col):
    # checking top if there any queen is present then return False
    i = row - 1
    while(i >= 0):
        if chessBoard[i][col] == 1:
            return False
        i = i - 1

    # checking top left diagonal of the cell
    i = row-1
    j = col - 1
    while(i >= 0 and j >= 0):
        if chessBoard[i][j] == 1:
            return False
        i = i-1
        j = j-1

    # checking top right diagonal of the cell
    i = row-1
    j = col + 1
    while(i >= 0 and j < len(chessBoard)):
        if chessBoard[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    # if there is no queen in top, top left and top right diagonal then we can placed a queen in that particular cell, means queen is safe so return true
    return True
    
  
def printNqueen(chessBoard, answerSet, row):
    if row == len(chessBoard):
            print(answerSet)
            return
    
    for col in range(len(chessBoard)):
        if queenSafe(chessBoard, row, col) == True:
            # if queen is safe then place at that position and then check for the next row 
            chessBoard[row][col] = 1
            printNqueen(chessBoard, answerSet + str(row) + "-" + str(col) + ", ", row+1)
            chessBoard[row][col] = 0    #while returning back from stack making it 0 as we trying with every posible position.



num = int(input("Enter the number of queen to be placed : "))
chessBoard = []

# Initially filling the chessBoard with all 0's
for row in range(num):
    col = [0 for i in range(num)]
    chessBoard.append(col)

# chessBoard, initially ans ="", and row = 0
printNqueen(chessBoard, "", 0)
