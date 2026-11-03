student={ 'firstname':'Pravin',
         'lastname':'Nangare',
         'age':21,
         'address':'Sangli-Atpadi',
}
print(student)
print(student['firstname'])

for i in student:
        print(i) # display the key only
        
student = {"name": "Pravin", "age": 21}

print(student.get("name"))

print(student.keys())
print(student.values())
 
 # update
student.update({"age": 22})
print(student) 

student.pop("age")
print(student)