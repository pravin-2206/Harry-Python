class Marks:
        def Subject_info(self,DSA,Networking,Database,Python):
                self.DSA=DSA
                self.Networking=Networking
                self.Database=Database
                self.Python=Python
        def Total_Marks(self):
                print(f'Marks of Each Subject Python: {self.Python} DSA: {self.DSA} Database: {self.Database} Networking: {self.Networking}' )
m=Marks()
m.Subject_info(100,99,98,89)
m.Total_Marks()
                