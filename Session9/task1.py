# Write a program to print multiplication table of a given number using for loops


num = int(input("Enter the number: "))

# num = 5
# 5 x 1 = 5
# 5 x 2 = 10
# .......
# 5 x 10 = 50

for i in range(1, 11):
    # print(str(num) + "x" + str(i) + "=" + str(num*i)) # String concatination
    print(f"{num} x {i} = {num*i}")  # f-strings






