#       Implementing Quick Sort
#   Time Complexity : n log n   -> Best case/ Average Case
#                   :  n^2      -> Worst case

def swap(arrList, index1, index2):
    temp = arrList[index1]
    arrList[index1] =  arrList[index2]
    arrList[index2] = temp

def partition(arrList, start, end):
    pivot = arrList[end]       # taking the last element as  pivot
    i = start - 1        # index of smaller element, whenever will get a smaller element then pivot, will swap with element of index i
    for j in range(start, end):
        if arrList[j] <= pivot:   # check if element is <= pivot, then increment i and swap 
            i += 1
            swap(arrList, i, j)
    swap(arrList, i+1, end)    # at the end swap the pivot element with the element of index i+1,
    return i+1  # return the index of pivot element 
    

def quickSort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot-1)
        quickSort(arr, pivot+1, end)

n = int(input("Enter the number of element in the list : "))
print("Enter elements ")
arr = list(map(int, input().split()))
print("Before sorting ", arr)
quickSort(arr, 0, n-1)
print("After sorting", arr)



#               OUTPUT 
# input :
#       Enter the number of element in the list : 5
#       Enter elements
#       6 2 8 9 1
# output :
#       Before sorting  [6, 2, 8, 9, 1]
#       After sorting [1, 2, 6, 8, 9]