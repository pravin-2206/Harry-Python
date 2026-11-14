class Marks:
        
        # def Subject_info(self,DSA,Networking,Database,Python):
        #         self.DSA=DSA
        #         self.Networking=Networking
        #         self.Database=Database
        #         self.Python=Python
        
        def Subject_info(self):
                self.DSA=int(input("Enter DSA Marks: "))
                self.Python=int(input("Enter Python Marks: "))
                self.Database=int(input("Enter Database Marks: "))
                self.Networking=int(input("Enter Networking Marks: "))
        def Each_Subject_Marks(self):
                print(f'Marks of Each Subject Python: {self.Python} DSA: {self.DSA} Database: {self.Database} Networking: {self.Networking}' )
        
        def Sum_of_marks(self):
                total=self.Database+self.DSA+self.Database+self.Networking
                print(f'Sum of marks:',total)
                
m=Marks()
# m.Subject_info(100,99,98,89)
m.Subject_info()

m.Each_Subject_Marks()

m.Sum_of_marks()
                