class Student:
        # Assign values 
        # name='Pravin' 
        # age=21
        # address='Atpadi'
        
        
        name='' # this is a attribute 
        age=0
        address=''
        
        # create one methods that contains class values
        
        def set_info(self):
                self.name=input("Enter your name =")
                self.age=int(input("Enter Your Age="))
                self.address=input("Enter Your Address=")
        
        # create methods 
        def display(self):
                print("This is display methods")
                print(f"name={self.name} ,age={self.age}, Address={self.address}")
        

s=Student() # creating object
print(s) 

# set the values 
# s.name='Karan'
# s.age=15
# s.address='sangli'
# print(s.name)
# print(s.age)
# print(s.address)

s.set_info()
s.display()

print("\nSecond Object")
s2=Student()
# s2.name="Suja"
# s2.age=24
# s2.address='Pune'
# print(s2.name)
# print(s2.age,s2.address) 

# s2.set_info()
# s2.display()


