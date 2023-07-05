# Write a program to find whether a given number is prime or not

# 2 , 3, 5 , 7 , 11......


# num = 5
# 5  divided by 1 = 5
# 5  divided by 2 = 
# 5  divided by 3 = 
# 5  divided by 4 = 
# 5  divided by 5 = 1

# num = 6
# 6  divided by 1 = 6
# 6  divided by 2 = 3
# 6  divided by 3 = 2
# 6  divided by 4 = 
# 6  divided by 5 = 
# 6  divided by 6 = 1




num = int(input("Enter the number: "))
prime = True
for i in range(2 , num):
    if(num % i == 0 ):
        prime = False
        break

if prime:
    print("This number is prime")
else:
    print("not prime")



