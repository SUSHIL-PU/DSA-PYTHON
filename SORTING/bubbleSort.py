#  Implementation of bubble sort
# 
#             TIME COMPLEXITY
#     AVERAGE/WORST CASE : O(N^2),       BEST CASE : O(N)


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swapping the values of arr[j] and arr[j+1]
    print(arr)


# n = int(input("Enter the number of elements : "))
print("Enter elements ")
arr = list(map(int, input().split()))
bubblesort(arr)