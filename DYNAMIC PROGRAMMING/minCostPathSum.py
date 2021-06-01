#  minimum path sum / Minimum cost path
# In a 2d matrix path, have to visit from (0,0) to (row-1, col-1) by minimum cost 
#  you can only visit right side or bottom side

#             MEMOIZATION/DYNAMIC APPROACH
#        TIME COMPLEXITY : O(N * M)     -> N = no of row,   M = no of col
# 
  
import sys

def minCostSum(matrix, row, col, dp):
    if  row == len(matrix) or col == len(matrix[0]):
        return sys.maxsize    # returning a maximum constant int, as we are taking min

    if row == len(matrix)-1 and col == len(matrix[0])-1:
        return matrix[row][col]

    if dp[row][col] != 0:
        return dp[row][col]

    dp[row][col] = matrix[row][col] + min(minCostSum(matrix, row, col+1, dp), minCostSum(matrix, row+1, col, dp))
    return dp[row][col]


# ----------------------------------------------------------------------------------------------
#               TABULATION APPROACH
#            TIME COMPLEXITY : O(N * M)
# 
# def minCostSum(matrix, dp):
#     row = len(matrix)-1
#     col = len(matrix[0])-1
#     dp[row][col] = matrix[row][col]

#     for i in range(col-1, -1, -1):
#         dp[row][i] = dp[row][i+1] + matrix[row][i]

#     for i in range(row-1, -1, -1):
#         dp[i][col] = dp[i+1][col] + matrix[i][col]
    
#     for i in range(row-1, -1, -1):
#         for j in range(col-1, -1, -1):
#             if dp[i][j] == 0:
#                 dp[i][j] = matrix[i][j] + min(dp[i+1][j],  dp[i][j+1])

#     print(dp)
#     return dp[0][0]

    



# ----------------------------------------------------------------------------------------------
#                       RECURSIVE APPROACH
#                    TIME COMPLEXITY : O(2^N)
# 
# 
# def minCostSum(matrix, row, col):
#     if  row == len(matrix) or col == len(matrix[0]):
#         return sys.maxsize    # returning a maximum constant int, as we are taking min

#     if row == len(matrix)-1 and col == len(matrix[0])-1:
#         return matrix[row][col]
    
#     minCost = matrix[row][col] + min(minCostSum(matrix, row, col+1), minCostSum(matrix, row+1, col))
#     return minCost

# ---------------------------------------------------------------------------------------------

row = int(input("Enter the number of row : "))
col = int(input("Enter the number of col : "))
matrix = list()
print("Enter elements ")
for i in range(row):
    elm = list(map(int, input().split()))
    matrix.append(elm)

#  for memoization
dp = []
for i in range(row):
    elm = [0 for i in range(col)]
    dp.append(elm)
print(dp)

minCost = minCostSum(matrix, 0, 0, dp)    # 0, 0 is the source 
# minCost = minCostSum(matrix, dp)  # for tabulation 
print("Minimum cost =", minCost)


#  ---------------------------------------------------------------------------------------------
#       
# 
#         OUTPUT
# Input :
#       Enter the number of row : 3
#       Enter the number of col : 3
#       Enter elements
#       1 3 5
#       2 1 2
#       4 3 1
# Output :
#       Minimum cost = 7