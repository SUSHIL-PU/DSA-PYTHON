#  To find the fibonacci of an index using dynamic approach.
#     fibonacci numbers : 0  1   1   2   3   5   8   13  21 ...
#             Index     : 0  1   2   3   4   5   6   7   8  ...
# 
# Input : 6
# Output: 8
# 
# ------------------------------------------------


def fibo(n, dp):
    if n == 0 or n == 1:
        return n
    if(dp[n] != 0):     # if fibo(n) is stored in the dp list, then simply returning the value
        return dp[n]
    
    fib1 = fibo(n-1, dp)
    fib2 = fibo(n-2, dp)
    fib = fib1 + fib2
    dp[n] = fib     # storing the result fib in dp list
    return fib

n = int(input("enter a number : "))

dp = [0 for i in range(n+1)]    # Filling the dp list with all 0's
print("fibonacci is  = ", fibo(n, dp))
print("dp list = " ,dp)


#                       OUTPUT
# Test case 1 :
#         Input : 
#                   enter a number : 5
#        Output :   
#                    fibonacci is  =  5
#                    dp list =  [0, 0, 1, 2, 3, 5]
#        
# Test case 2 :
#        Input :
#               enter a number : 10
#       Output : 
#               fibonacci is  =  55
#               dp list =  [0, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55]