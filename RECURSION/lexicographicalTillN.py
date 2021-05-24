#  Given an integer N, you have to print all the numbers upto n in laxicographical order
#  Laxicographical order :  Laxicographical order is the generalization of alphabetical order in dictionaries to sequence. It is also known as Dictionary order.




def lexicographicalOrder(i, n):
    if i > n:
        return
    
    print(i, end = "  ")
    for j in range(0, 10):          # finding every possible lexicographical combination of i, until i becomes grater than n
        lexicographicalOrder(i * 10 + j, n)

N = int(input("Enter a number N whose Lexicographical to be found : "))
for i in range(1, 10):
    lexicographicalOrder(i, N)
    print()  # for new line after every itertion



#                                         OUTPUT
#  TEST CASE 1:
# 
# Input :
#        Enter a number N whose Lexicographical to be found : 19
# output :
#       1  10  11  12  13  14  15  16  17  18  19  
#       2
#       3
#       4
#       5
#       6
#       7
#       8
#       9  
#
# 
#
#  TEST CASE 2 :
# 
#  Input :   
#        Enter a number N whose Lexicographical to be found : 101
# Output :
#        1  10  100  101  11  12  13  14  15  16  17  18  19  
#        2  20  21  22  23  24  25  26  27  28  29
#        3  30  31  32  33  34  35  36  37  38  39
#        4  40  41  42  43  44  45  46  47  48  49
#        5  50  51  52  53  54  55  56  57  58  59
#        6  60  61  62  63  64  65  66  67  68  69
#        7  70  71  72  73  74  75  76  77  78  79
#        8  80  81  82  83  84  85  86  87  88  89
#        9  90  91  92  93  94  95  96  97  98  99
