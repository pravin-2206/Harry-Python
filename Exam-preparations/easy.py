# print name longer than five character

list=['pravin','om','viraj','ravi','swaraj','ishan']

for i in list:
        if len(i)>5:                
                print(i)
                
print("count how many names start with a vowel")
count=0
for i in list:        
        if i.startswith('a') or i.startswith('e') or i.startswith('i'):
                print(i)
                count+=1
print(count)

# Sort the list of names alphabetically and print them in ascending order. 

print("sort name as alphabetically order")
# print(list.sort())

names = ["Pravin", "Amit", "Rahul", "Neha", "Sanket"]

names.sort()

print(names)

