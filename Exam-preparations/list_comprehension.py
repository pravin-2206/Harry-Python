square=[x * x for x in range(1,11)]
print(square)

even=[i for i in range(1,11) if i%2==0]
print(even)

numbers = [1, 2, 2, 3, 3, 4]
result = {i for i in numbers}
print(result)

squares = {i: i * i for i in range(1, 6)}
print(squares)