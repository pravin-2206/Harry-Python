# Write a program using 
# 1. match case that simulates a simple calculator.Ask the user for two numbers and an operation (+, -, *, /).
# 2. Perform the operation using match case 

n1=int(input("Enter the first number: "))
n2=int(input("Enter the Second number: "))

operations=input("Enter which operations u perform like (+,-,*,/): ")

match operations:
        case '+':
                print("Addition of two numbers:",n1+n2)
        case '-':
                print("Substraction of two numbers:",n1-n2)
        case '*':
                print("Multiplications of two numbers:",n1*n2)
        case '/':
                print("Division of two numbers:",n1/n2)
        case _:
                print("Wrong Operations perform:")
                
        