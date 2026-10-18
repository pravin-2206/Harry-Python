'''
. 
1. Write a function a rectangle. calculate_area(length, width=10) that returns the area of Test it by calling the function with:

1. Both length and width
2. Only length (use default width)
'''

def rectangle(length,width=10):
        area=length*width
        return area
print(rectangle(10,20))
print(rectangle(12))