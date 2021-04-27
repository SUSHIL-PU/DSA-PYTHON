#               TOWER OF HANOI PROBLEM 
#    There are 3 towers, tower1 has n number of disks. Tower2 and Tower3 is empty. The disks 
#    are incresingly placed in terms of such that smallest disk on top and largest disk on 
#   bottom. 
#        print the steps to move the disk from tower1 to tower2 using tower3.
#       
# 
# INPUT : N  - the number of disks to be to be shifted.
#               name of the 3 towers
# OUTPUT : steps to move from tower1 to tower2 using tower3


def towerOfHanoi(n, A, B, C):
    if n == 0:
        return

    towerOfHanoi(n-1, A, C, B)     # move n-1 disks from towerA to towerC using towerB 
    print(n, " | ", A, " --> ", B)  
    towerOfHanoi(n-1, C, B, A)  # will move n-1 disks from towerC to towerB using towerA



noOfDisk = int(input("Enter the number of disks : "))
tower1 = input("Enter name of tower1 : ")
tower2 = input("Enter name of tower2 : ")
tower3 = input("Enter name of tower3 : ")

towerOfHanoi(noOfDisk, tower1, tower2, tower3)


#       OUTPUT
# 
#    Input :
#            Enter the number of disks : 3
#            Enter name of tower1 : A
#            Enter name of tower2 : B
#            Enter name of tower3 : C
#     Output :
#             1  |  A  -->  B
#             2  |  A  -->  C
#             1  |  B  -->  C
#             3  |  A  -->  B
#             1  |  C  -->  A
#             2  |  C  -->  B
#             1  |  A  -->  B