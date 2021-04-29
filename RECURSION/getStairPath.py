#               Get stair path
# given a number n representing the number of staircase. You are allowed to climb/down 
# 1 step , 2step or 3 step in one move.
# return all the possible paths in a list to reach the top/down of the stairs. 


def stairPaths(n):
    if n == 0:
        return ['']
    elif n < 0:  # 0'th is the last stair. so for negative stair returning [].
        return []

    paths1 = stairPaths(n-1) # taking 1 step
    paths2 = stairPaths(n-2) # taking 2 step
    paths3 = stairPaths(n-3)  # taking 3 step

    ans = []
    for path in paths1:
        ans.append('1' + path)   #appending 1 to the existing path of paths1
    for path in paths2:
        ans.append('2' + path)
    for path in paths3:
        ans.append('3' + path)
    return ans

noOfStairs = int(input("Enter the number of stairs : "))
ans = stairPaths(noOfStairs) 
print(ans)




#               OUTPUT
# Test case 1:
#   Input :  Enter the number of stairs : 3
#   Output:  ['111', '12', '21', '3']


# Test case  2:
#    Input :  Enter the number of stairs : 4
#   Output :  ['1111', '112', '121', '13', '211', '22', '31']