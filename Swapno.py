n1=int(input("Enter the first number: "))
n2=int(input("Enter the Second number: "))

print(f'before swap a = {n1}, b= {n2}')

n1=n1+n2
n2=n1-n2
n1=n1-n2

print(f'after swap a = {n1}, b= {n2}')