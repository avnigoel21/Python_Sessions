# Write a program to find greatest of four numbers entered by the user

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1 > num4):
    ans1 = num1
else:
    ans1 = num4

if(num2  > num3):
    ans2 = num2
else:
   ans2 = num3


if(ans1 > ans2):
    print(str(ans1) + " is greatest")
else:
    print(str(ans2) + " is greatest")