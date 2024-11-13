

# Write a function called fibonacci(n) that takes a non-negative integer in as input The function should calculate the nth number in the Fibonacci sequence using recursion.
# The Fibonacci sequence is defined as follows:
# F(0) = 0
# F(1) = 1
# F(n)=F(n-1)+F(n-2) for n > 1



# 0 1 1 2 3 5 8 13 


def fibonacci(n):

    first,second=0,1

    for i in range(2,n):

        first,second=second,first+second

    print(second)    


fibonacci(5)