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