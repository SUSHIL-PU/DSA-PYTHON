#  Count the number of ways to construct sum by throwing a dice
# any number of times. Eace throwing produces an outcoome between 
# 1 to 6.
# Ex. if sum = 3 , then there are 4 ways --->
#  possible combinations        1 + 1 + 1
 #                              1 + 2
#                               2 + 1
#                               3
# ===========================================================================

def diceCombinations(n):
    if n == 0:
        return 1
    count = 0
    for i in range(1, 6):
        if n >= i:
            count = count + diceCombinations(n-i)
        else:  
            break
    return count

n = int(input("Enter the sum "))
print("no of ways", diceCombinations(n))



#                       OUTPUT 
# Test case 1 :
#           Enter the sum 4
#           no of ways 8
# 
# Test case 2:
#           Enter the sum 5
#           no of ways 16