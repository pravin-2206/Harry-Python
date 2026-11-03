set=(10,20,80,77,97)
print(set)

for i in set:
        print(i)
        
A = {10, 20, 30}

A.add(40)
print(A)

A.update([50, 60])
print(A)

A = {10, 20, 30, 40}

A.remove(20)
A.discard(50)

print(A)


A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))