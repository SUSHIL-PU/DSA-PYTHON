# Implementation of Insertion sort 

#       TIME COMPLEXITY 
#  BEST CASE : O(N)
#  AVERAGE/WORST CASE : O(N^2)
# --------------------------------------------------------------------------------------------

def insertionsort(arr):
    for i in range(1, len(arr)):
        currentElm = arr[i]
        j = i - 1
        while arr[j] > currentElm and j >= 0: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = currentElm
    
    print(arr)




# n = int(input("Enter thr number of element : "))
print("Enter elements ")
num = list(map(int, input().split()))
insertionsort(num)

# ----------------------------------------------------------------------------------------------
#           OUTPUT
#  Input :
#         Enter elements
#         6 8 2 4 1 0 1
# Output :
#        [0, 1, 1, 2, 4, 6, 8]