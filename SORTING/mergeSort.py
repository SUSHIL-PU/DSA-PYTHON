#      Implementation of Merge Sort
#   Time Comppxity : n log n




def merge(leftList, rightList):
    i = 0   # for iterate over leftList
    j = 0   # for iterate over rightList
    newList = []
    while i < len(leftList) and j < len(rightList):
        if leftList[i] < rightList[j]:
            newList.append(leftList[i])
            i += 1
        else:
            newList.append(rightList[j])
            j += 1
    if i >= len(leftList):    # check if leftList is exhausted
        while j < len(rightList):   # then fill the newList with rightList
            newList.append(rightList[j])
            j += 1
    else:       # when rightList is exhausted
        while i < len(leftList): # filling with leftList
            newList.append(leftList[i])
            i += 1
    return newList


def MergeSort(inputList):
    if len(inputList) == 1: 
        return inputList
    mid =  len(inputList)//2
    leftSubArray = MergeSort(inputList[: mid])
    rightSubArray = MergeSort(inputList[mid : ])
    mergeList = merge(leftSubArray, rightSubArray)
    return mergeList

n = int(input("Enter the size of the list : "))
print("Enter elements ")
arr = list(map(int, input().split()))
print("Before sorting : ", arr)
sortedList = MergeSort(arr)
print("After sorting : ", sortedList)





#                   OUTPUT 
# Test Case 1 :
#           Input :
#               Enter the size of the list : 6
#               Enter elements
#               7 9 5 8 3 6
#           Output :
#               Before sorting :  [7, 9, 5, 8, 3, 6]
#               After sorting :  [3, 5, 6, 7, 8, 9]            
