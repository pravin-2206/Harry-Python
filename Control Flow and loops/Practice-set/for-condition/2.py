#Print the multiplication table of a number (entered by user).

num=int(input("Enter the number to find that multiplication table:"))

for i in range(1,11):
        print(i,"X",num,"=",i*num)
