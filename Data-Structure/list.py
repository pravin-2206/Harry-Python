# list are ordered , mutable (changeable) collection of iteam.

marks=[90,78,89,67,95,60] # create list

print(marks)

#indexing

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

# sclicing 
print(marks[0:5])
print(marks[0:3])
print(marks[0:])
#print(marks[7]) # error indexout of bound

# list methods
print()
print()
print()

marks=[90,78,89,67,95,60]
print(marks)
marks.append(10) # add new number in list at last
print(marks)

marks.pop() # remove last element in list 
print(marks)

extra_list=[12,25,46,40]
marks.extend(extra_list) # add extra_list in marks list
print(marks)

extra_list.insert(1,100) # insert at index 1 value 100
print(extra_list)

extra_list.remove(12)  # remove the 12 element in list 
print(extra_list)

extra_list.sort() # sort list
print(extra_list)

extra_list.reverse()  # reverse list
print(extra_list)