#     Target Sum Problem 
#  an array of integer elements and a target of sum is given. Have to find out
#  the elements whose sum is equal to the target.

# Input : n - number of element.
#         an array of integer of n element
#         target sum
# Output : set of elements whose sum is equal to target sum



def printTargetSum(arr, index, answerSet, total, target):
    if index == len(arr):
        if total == target:
            print(answerSet + ".")
        return

           # adding the element into answerSet
    printTargetSum(arr, index+1, answerSet+str(arr[index])+", ", total+arr[index], target)
    printTargetSum(arr, index+1, answerSet, total, target)  # not adding the element into answerSet

    # These was the two choice for every element, either add or not add.



num = int(input("Enter the number of element : "))
print("Enter elements ")
arr = []
arr = list(map(int, input().split()))
# for i in range(num):
#     arr.append(int(input()))

target = int(input("Enter the target sum : "))

#  arr, first index, answerSet, totalSum, targetSum is passed
printTargetSum(arr, 0, "", 0, target)




#               OUTPUT
# Test case 1:
#  Input :  Enter the number of element : 5
#           Enter elements
#           10 20 30 40 50
#           Enter the target sum : 60
#  Output:
#           10, 20, 30, .
#           10, 50, .
#           20, 40, .

# Test case 2:
#  Input :  Enter the number of element : 6
#           Enter elements 
#           2 4 6 7 3 1
#           Enter the target sum : 10
#  Output :
#           2, 4, 3, 1, .
#           2, 7, 1, .
#           4, 6, .
#           6, 3, 1, .
#           7, 3, .