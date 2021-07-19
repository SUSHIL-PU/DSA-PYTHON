# Given weights and values of n items, put these items in a knapsack of capacity W to 
# get the maximum total value in the knapsack. In other words, given two integer arrays 
# val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items 
# respectively. Also given an integer W which represents knapsack capacity, find out the 
# maximum value subset of val[] such that sum of the weights of this subset is smaller than 
# or equal to W.
# ---------------------------------------------------------------------------------


def knapSack(ind, tillWeight, dp):
    if tillWeight > bagCapacity: # if bag capacity exceeded
        return -1e7
    if ind == n:
        return 0
    if dp[ind][tillWeight] != -1: 
        return dp[ind][tillWeight]

    pick = value[ind] + knapSack(ind+1, tillWeight+weight[ind], dp) #taking the item
    notPick = knapSack(ind+1, tillWeight, dp)    #not taking the item

    dp[ind][tillWeight] = max(pick, notPick)
    return dp[ind][tillWeight]

n = int(input("Enter the number of item : "))
bagCapacity = int(input("Enter the bag capacity : "))
print("Enter weight list : ")
weight = list(map(int, input().split()))
print("Enter value list : ")
value = list(map(int, input().split()))
dp = []
for i in range(n+1):
    elm = [-1 for j in range(bagCapacity+1)]
    dp.append(elm)
maxValue = knapSack(0, 0, dp)
print("So the maximum value is = ", maxValue)


#     ---------------------------------------------------------------------
#                                   sample IO
# 
# Enter the number of item : 3
# Enter the bag capacity : 50
# Enter weight list : 
# 10 20 30
# Enter value list :
# 60 100 120
# So the maximum value is =  220