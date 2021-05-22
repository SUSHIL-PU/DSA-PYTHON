# you are given two number N and K.
# N -> total number of soldiers standing in a circle form from index 0 to N-1
# A cruel king wants to execute them but in a different way - 
# He wants to execute soldiers from 0'th position and proceed around the circle in clockwise direction - 
#        in each step k-1 soldiers are skipped and the k'th soldier is executed.
# 
#  The elimination process around the circle until only the last soldier remains, who is given freedom. Find the position of the lucky soldier..
#  will be followed 0 based index

# if N = 5, K = 3  
#                            #       0   1   2   3   4   
# output  = 3 
# Explaination :  
#              in every iteration the k'th soldier will be exeuted until only one left
# first iteation : 
#                   2 will be executed
#                   remaining = 3   4   0   1
# second iteration :
#                   0 will be executed
#                   remaining =  1 3 4
# third iteration : 
#                   4 will be executed
#                   remaining = 1 3
# fourth iteration :
#                   1 will be executed
#                   remaining = 3

# So, the soldier in index 3 will be given freedom


# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(1)



def josephus(n, k):
    if n == 1:
        return 0
    luckySolInd = josephus(n-1, k)  # will return the lucky index from n-1 soldiers
    lucky = (luckySolInd + k) % n   # As in every iteration index will be changed because of a soldier is being executed. So to maintain the index order k is added and % by n
    return lucky


N = int(input('Enter the number of soldires : '))
K = int(input('Enter the K value : '))
print('The lucky soldier is, who is in index ', str(josephus(N, K)))
