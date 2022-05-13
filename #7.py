N = int(input())
i=1
s=0
fib=2
while N>i:
    r=s+fib
    s=fib
    fib=r
    i+=1
print(fib)
    