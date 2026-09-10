age=int(input("Enter the age: "))
person=input("Enter the person role: ")

eligible = age<=21 and person=='student'
print(f'Eligible : {eligible}')