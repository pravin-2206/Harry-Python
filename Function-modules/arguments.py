
def add(a,b): # a and b is parameters
        return a+b
print(add(10,20))  # passing values is arguments

# types of arguments

# 1 positional arguments

def add(a,b): # a and b is parameters
        return a+b
print(add(10,20))  # passing values is arguments 

# 2 default arguments

def add(a,b,pos=1): # pos is default arguments 
        return a+b+pos  
print(add(10,20))   

#  if i pass the default parameters in arguments this override the value of pos 
def add(a,b,pos=1): # pos is default arguments 
        return a+b+pos  
print(add(10,20,5)) # output will be 35 

# 3 key word arguments 
print("key word arguments:")
def add(a,b):
        print("value of a:",a)
        print("value of b:",b)
        return a+b

print(add(b=10,a=20))