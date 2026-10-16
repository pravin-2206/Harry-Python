# string declare 3 types 

name1="Pravin" 
name2='Pravin' 
name3='''Pravin'''

print(name1,name2,name3)

# indexing

# in python indexing starting with 0

print(name1[0])
print(name1[1])
print(name1[2])
print(name1[3])
print(name1[4])
print(name1[5])

# as well as negative indexing 

# negative indexing start with -1.
print("Negative indexing")
print(name2[-1])
print(name2[-2])
print(name2[-3])
print(name2[-4])
print(name2[-5])
print(name2[-6])

# convert negative indexing into positive indexing
print("Negative index to positive index")
print(name3[-1+1]) # print 0 index in name variable
print(name3[-6+8]) # print 2 index
# print(name3[-3+10]) # index out of range error