# Write a program to find out whether a student is pass or fail, if it requirs total 40% and
# at least 33% in each subject to pass.
#Assume 3 subjects and take marks as an input from the user

name = input("Enter your name: ")
sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("FAIL , YOU HAVE LESS THAN 33 IN ONE OF THE SUBECT")
elif((sub1+sub2+sub3)/3 < 40):
    print("FAIL, DUE TO TOTAL PERCENTAGE LESS THAN 40%")
else:
    print("Congratulations, you are pass")