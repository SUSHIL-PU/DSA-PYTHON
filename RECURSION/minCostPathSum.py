#  minimum path sum / Minimum cost path
# In a 2d matrix path, have to visit from (0,0) to (row-1, col-1) by minimum cost

#           RECURSIVE APPROACH
#        TIME COMPLEXITY : O(2^N)
# 
  
import sys
def minCostSum(matrix, row, col):
    if  row == len(matrix) or col == len(matrix[0]):
        return sys.maxsize    # returning a maximum constant int, as we are taking min

    if row == len(matrix)-1 and col == len(matrix[0])-1:
        return matrix[row][col]
    
    minCost = matrix[row][col] + min(minCostSum(matrix, row, col+1), minCostSum(matrix, row+1, col))
    return minCost



row = int(input("Enter the number of row : "))
col = int(input("Enter the number of col : "))
matrix = list()
print("Enter elements ")
for i in range(row):
    elm = list(map(int, input().split()))
    matrix.append(elm)

minCost = minCostSum(matrix, 0, 0) # 0, 0 is the source 
print("Minimum cost =", minCost)


# --------------------------------------------------------------------------------------
#               OUTPUT
# Input :
#       Enter the number of row : 3
#       Enter the number of col : 3
#       Enter elements
#       1 3 5
#       2 1 2
#       4 3 1
# Output :
#       Minimum cost = 7