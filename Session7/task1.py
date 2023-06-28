#Write a program to print yes when the age entered by the user is greater than 18 or equal to 18


age = int(input("Enter your age : "))

if(age >= 18):
    print("Yes, you are eligible for voting")
else:
    print(("No , you are not eligible for voting"))


if(age > 18 or age == 18):
    print("Yes, you are eligible for voting")
else:
    print(("No , you are not eligible for voting"))
