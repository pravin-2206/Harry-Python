'''1. Write a program that writes three lines of text to a file tasks.txt'''

with open('tasks.txt','w') as f:
        # string='''hey i am learning 
        # python programming
        # it iss easy and fun'''
        # f.write(string)
        
        f.write('line 1\n')
        f.write('line 2\n')
        f.write('line 3\n')