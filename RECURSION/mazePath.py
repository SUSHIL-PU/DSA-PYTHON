#       Find all the possible paths of a Maze where some sort of obstackle is there..
# 
#  A maze is there with the values 0's and 1's . if 1's means obstackle and 0's means we can
#  go through the path. Have to find the total number of paths from source to destination. 
#  We can move to top(t), left(l), down(d), and right(r).

# example                           0  0   1
                #                   0  0   1
                #                   1  0   0
                #                   1  0   0
#    we havee to go from (0,0) to (3,3)..... varoius paths are drddr
                                                            #  drdrd
                                                            #  rdddr
                                                            #  rddrd


def printMazePath(maze, row, col, answerTillNow, visited):
    if row<0 or col<0 or row == len(maze) or col==len(maze[0]) or maze[row][col] == 1 or visited[row][col] == True:
        return      # Simply returning if control goes out of the maze, i.e. if row or col going beyond the maze or the node having obstackle(value is 1) or a node is already visited 
    elif row == len(maze)-1 and col == len(maze[0])-1:
        print(answerTillNow)
        return

    visited[row][col] = True    #making visited the node True before visiting a node
    printMazePath(maze, row-1, col, answerTillNow+"t", visited)     # visit top from existing node
    printMazePath(maze, row, col-1, answerTillNow+"l", visited)     # visit left  
    printMazePath(maze, row+1, col, answerTillNow+"d", visited)     # visit down
    printMazePath(maze, row, col+1, answerTillNow+"r", visited)     # visit right

    visited[row][col] = False   # need to make the path as unvisit for next path iteration
 


row = int(input("Enter the number of row :"))
col = int(input("Enter the number of column : "))
print("Enter the elements")
maze =[]
for r in range(row):
    colInput = list(map(int, input().split()))
    maze.append(colInput)

visited = []
#  making al visited node as False
for r in range(row):
    c = [False for i in range(col)]
    visited.append(c)


# 0,0 is  the source and destination is maze[row-1][col-1]
# initially visited is False
printMazePath(maze, 0, 0, "", visited)


#               OUTPUT
# Input :
#       Enter the number of row :4
#       Enter the number of column : 3
#       Enter the elements
#       0 0 1
#       0 0 0
#       1 0 0
#       1 1 0
# Output :
#       drdrd
#       drrdd
#       rddrd
#       rdrdd
