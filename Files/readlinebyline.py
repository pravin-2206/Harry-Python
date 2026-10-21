# f=open('details.txt','r')

# for file in f:
#         content=f.read()
#         print(content)
# f.close()

with open('details.txt','r') as f:
        cont=f.read()
        print(cont)