# Write a program to read the text from a given file 'poems.txt' and find out whether it
# contains the word twinkle


f = open('poems.txt')
t = f.read()

if 'twinkle' in t:
    print("twinkle is present")
else:
    print("not present")

f.close()



