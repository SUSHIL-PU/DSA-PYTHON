# There are n stairs, a person standing at the bottom wants to reach the top. The  person can climb 1 stairs or 2 stairs or 3 stairs at a time.  
# count the number of ways a person can reach the top.
#  
# 
#    SAMPLE I/O
#       N = 3
#  OUTPUT : 4
# EXPLANATION :  possible paths [ 1 1 1,
#                                 1 2,
#                                 2 1,
#                                 3     ]      ---------------------------------------------------------------------------------

            # RECURSIVE APPROACH 

        # TIME COMPLEXITY : O(3^N)
        # SPACE COMPLEXITY : O(1)

# def countStairePath(n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0

#     oneStep = countStairePath(n-1) 
#     twoStep = countStairePath(n-2)
#     threeStep = countStairePath(n-3)
#     return oneStep + twoStep + threeStep

# N = int(input("Enter the number of stairs : "))
# print(countStairePath(N))

# -------------------------------------------------------------------------------

        # MEMOIZATION TECHNIQUE  - DYNAMIC 

        # TIME COMPLEXITY : O(N)
        # SPACE COMPLEXITY : O(N)


def countStairePath(n, dp):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if dp[n] != 0:
        return dp[n]

    oneStep = countStairePath(n-1, dp)
    twoStep = countStairePath(n-2, dp)
    threeStep =  countStairePath(n-3, dp)
    dp[n] = oneStep + twoStep + threeStep
    return dp[n]


N = int(input("Enter the number of stairs : "))
dp = [0 for i in range(N+1)]
print("total number of paths = ", countStairePath(N, dp))
print(dp)



# ---------------------------------------------------------------------------

#                    TABULAR METHOD
# 
#               TIME COMPLEXITY : O(N)
#               SPACE COMPLEXITY : O(N)



# def countStairePath(n):
#     dp = [0 for i in range(n+1)]
#     dp[0] = 1
#     for i in range(1, n+1):
#         if i == 1:
#             dp[i] = dp[i-1]
#         elif i == 2:
#             dp[i] = dp[i-1] + dp[i-2]
#         else:
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#     print(dp)
#     return dp[n]

# N = int(input("Enter the number of stairs : "))
# countStairePath(N)
