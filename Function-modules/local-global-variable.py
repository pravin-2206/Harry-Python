a=10 # global variable

def add(a,b):
        c= a+b
        print("a variable values:",a)
        return c
        z=10 # local variable 
print(add(20,20))

print(a) # output 10


# we can access local variable as global using global keyword

# def demo():
#         global z # modify global variable
#         z=100
#         print("global variable:",z)
# demo()
# z=200
# print(z)
