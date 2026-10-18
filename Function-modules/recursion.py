'''
recursion in python 

fibbonaccies series
0,1,1,2,3,5,8,13,21,....n

start index with 0 

fib(0)=0
fib(1)=1
fib(2)=1
fib(3)=2
fib(4)=3
fib(n)=fib(n-2)+fib(n-1)

'''

def fib(n):
        # base case of recursion 
        if n==0 or n==1:
                return n
        return fib(n-2)+fib(n-1)
print(fib(5))

'''
output are 

fib(0)=0
fib(1)=1
fib(5)

fib(3)+fib(4)
fib(1)+fib(2)+fib(2)+fib(3)
1+fib(0)+fib(1)+fib(0)+fib(1)+fib(1)+fib(2)
1+0+1+0+1+1+fib(0)+fib(1)
1+0+1+0+1+1+0+1
5

'''

# def walk(steps):
#         for step in range(1,steps+1):
#                 print(f'walk steps are:{step}')
# walk(10)