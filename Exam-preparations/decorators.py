def decorator(func):
        def wrapper():
                print("First Step:")
                
                func()
                print("second step")
        return wrapper
@decorator
def hello():
        print("Thired step")
hello()

print()

def deco(fun):
        def add(a=10,b=20):
                c=a+b
                print(c)
                
                fun()
                print("Executed code")
        return add
@deco
def mess():
        print("Addition of two numbers")
mess()
        
        