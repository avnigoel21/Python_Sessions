
# Use open function to read the content of a file!
f = open('sample.txt' ,'r')

# f = open('sample.txt') # by default the mode is read (r)

data = f.read()
# data = f.read(5) # reads first 5 chararcters from the file
print(data)

f.close


# modes
# r => open for reading 
# w => open for writing
# a => open for appending
# + => open for updating


# files -> text files and binary files
# rb => will open for read in binary mode
# rt = > will open for read in text mode