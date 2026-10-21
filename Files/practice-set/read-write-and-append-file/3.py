'''Read the file and print all lines as list using readlines()'''

with open('tasks.txt','r') as f:
        read=f.readline()
        print(read)
        read2=f.readline()
        print(read2)
        read3=f.readline()
        print(read3)
        read4=f.readline()
        print(read4)
        # for line in f.readline():
        #         print(line)