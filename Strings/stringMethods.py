#String are immutable if we are create sting do not change in existing string.
s=" Python Proramming"
print(s)

# methods are 

print(len(s)) # show the length of characters
u=s.upper()# convert into upper case
print(u) 

l=s.lower() # lowercase
print(l) 

c=s.capitalize() # First character of entire string a capital 
print(c)  

t=s.title() # First charactre of word a capital
print(t)

strips=" \n hello Guys!  "
print("Original string",strips)
print(strips.strip()) # remove left and write space

l=strips.lstrip()
print(l)  # remove left side space

r=strips.rstrip()
print(r) # remove right side space


print("Find and replace methods")

text="Python is fun"

print(text.find("is"))  # it return the index of word
print(text.replace("fun","easy")) # it is replace the words

# split and join

fruits="apple,banana,orange,pineapple,mango"
print(fruits)

change=fruits.split(',')   # a split method is used to convert the string into list
print(change)

# join method is used to convert list to string
print(',',fruits.join(['apple,banana,orange,pineapple,mango']))

# string properties

text="python2134"
print(text.isalnum()) # true
print(text.isalpha()) # false
print(text.isalnum()) # true
print(text.isspace()) # false



