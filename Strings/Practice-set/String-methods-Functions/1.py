'''
1. Take the string " i love python programming " and:
        1. Remove extra spaces from both ends
        2. Convert it to title case
        3. Count how many times "o" appears

2 Check if the string  "123abc" is alphanumeric.

'''

message=" i love python programming "

print(message)
#print(message.strip)
remo=message.strip()
print(remo)

t=message.title()
print(t)

count=message.find('o')
print(count)

alpha='123abc'
# print(alpha.isalpha)
a=alpha.isalpha()
print(a)