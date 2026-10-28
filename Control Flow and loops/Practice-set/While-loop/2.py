# Write a program that keeps asking the user to enter a password until they enter the correct one.
pas=input("Enter the password:")
while True:
        gues=input("Enter the gues password:")
        if(pas==gues):
                print("Access granted!")
                break
        else:
                print("Wrong try again")
