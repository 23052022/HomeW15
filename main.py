

n = int(input("enter number:"))
fib= 0
fib1 = 1
for i in range(n):
    fib, fib1 = fib1, fib + fib1
    print(fib, end=' ')
