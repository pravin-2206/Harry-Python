def rightTriangle(n):
        result=[]
        for i in range(1,n+1):
                result.append("*"*i)
        return result
print(rightTriangle(5))