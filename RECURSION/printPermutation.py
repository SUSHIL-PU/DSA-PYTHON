#          To print the permutation of a string  using recursion 
#  if the string is abc then permutations of abc is -
#               abc acb bac bca cab cba 

# if the length of the string is n then permutation has n! strings.. 



def printPermutationn(str, answerTillNow):
    if len(str) == 0:
        print(answerTillNow)   

    for i in range(len(str)):
        first = str[i]      # i'th char of the string
        remaining = str[0 : i] + str[i+1 :]     #finding the remaining substring
        printPermutationn(remaining, answerTillNow + first)

str = input("Enter the string to find permutation : ")
printPermutationn(str, "")



#                   OUTPUT
# input :
#       Enter the string to find permutation : abc
# Output :
#         abc
#         acb
#         bac
#         bca
#         cab
#         cba