# find fibonacci number of a particular index
#    fibonacci numbers : 0  1   1   2   3   5   8   13  21 ...
#            Index     : 0  1   2   3   4   5   6   7   8  ...

# Input : 6
# Output: 8


def fibo(n):
    if n==0 or n==1:
        return n
    fib1 = fibo(n-1)
    fib2 = fibo(n-2)
    fib = fib1 + fib2
    return fib

n = int(input("enter the index : "))
print("fibonacci is ", fibo(n))