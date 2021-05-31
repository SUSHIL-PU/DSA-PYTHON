# Implematation of Selection Sort

#           TIME COMPLEXITY
#     BEST/AVERAGE/WORST CASE : O(N^2)   


def selectionsort(arr):
    for i in range(len(arr)-1):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]


    print(arr)


# n = int(input("Enter the number of elements : "))
print("Enter elements ")
arr = list(map(int, input().split()))
selectionsort(arr)


# -------------------------------------------------------------------------------------------------
#       OUTPUT 
# Input :
#        Enter elements
#        7 4 9 1 2 0
#Output :
#       [0, 1, 2, 4, 7, 9]