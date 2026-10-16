# use a while loop to reverse a given number (e.g., 123 → 321).
n=123
org=n
rev=0
while n>0:
        dig=n%10
        rev=rev*10+dig
        n//=10
print("Original Number:",org,"\nReverse Number:",rev)
# print("Original number:",org)
# print("Reverse Number:",rev)