# #include<iostream>                                                                                                      
# using namespace std;
# int main()
# {
# long int i=1,s=0,fib=2,r,n; 
#     cin>>n;
#     while (i<n)
# {
#     r=s+fib; 
#   s=fib; 
#   fib=r;
#     i=i+1;
# }
#     cout<<fib;
#     return 0;
# }
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
    