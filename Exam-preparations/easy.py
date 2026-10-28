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

# Print names that contain the letter "a". 

#result=find.names("A")
#print(result)
# names.find("a")

names=['pravin','avi','bhi','sahil']
for name in names:
        
        if "a" in name:
                print(name)
                
print("Frequecy of number")
                
names = ["Amit", "Rahul", "Amit", "Neha", "Rahul", "Amit"]

frequency = {}

for name in names:
    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1

print(frequency)

