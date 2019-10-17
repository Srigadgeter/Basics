# >>>>> Files <<<<<

# Open a file
my_file = open('myFile.txt', 'w')
# We have to open our file whatever operations we do
# The second parameter 'w' represents the 'write' access of the file
# So, here I'm opening the file with write access given to it. I can write now.


# Info of the file
print('Name of the file:', my_file.name)
print('Close Status: Is it closed (True/False)?', my_file.closed)
print('Mode of the file:', my_file.mode)


# Write to the file
'''
Continuously we can make many write operations before the close operation. Once you closed the file will be saved.
The content will override the previous content if you do the write operation again.
Because write will override every thing. 
'''
my_file.write('Hi, This is tutorial of Files in Python. ')
my_file.write('Here you learn CRUD operation of files in python.')
my_file.close()  # After writing we have to close the document

print('Close Status: Is it closed (True/False)?', my_file.closed)
# Now we see it results in 'True' because we closed the file

my_file = open('myFile.txt', 'w')
my_file.write('Here the new content for the file')  # Override content
my_file.close()


# Append to the file
'''
Overridden is a drawback of the writing operation. So, we need non-overriding stuff.
Then we go with append operation
'''
my_file = open('myFile.txt', 'a')  # 'a' represents 'append' operation
my_file.write('--Appending content--')  # this content will append to the existing content in the file
my_file.close()


# Read a file
my_file = open('myFile.txt', 'r+')  # 'r+' represents 'read' operation
data = my_file.read(35)
# The parameter which we passing here is 35 which represents number of characters to read from starting of the file
print('data >>>', data)
