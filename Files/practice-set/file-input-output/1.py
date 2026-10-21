'''1.Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
2. Open notes.txt , read its content, and print it to the console.'''


with open('notes.txt','w') as file:
        string='Learning Python is fun!'
        file.write(string)

with open('notes.txt','r') as file:
        content=file.read()
        print(content)