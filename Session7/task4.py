# A spam comment is defined by the following keywords:
#"make a lot of money" , "buy now" , " subscribe this" , "click this"
#Write a program to detect these spams

text =  input("Enter the text: ")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is a spam")
else:
    print("not spam")


