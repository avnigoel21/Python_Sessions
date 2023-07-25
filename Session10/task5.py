# write a program using function to find greatest of three numbers

def maximum(num1 , num2 , num3):
    if(num1 > num2):
       if(num1 > num3):
            return num1
       else:
            return num3
    else:
        if(num2 > num3):
            return num2
        else:
            return num3
        
m = maximum(1200 , 55 , 122) 
# n = maximum(56 , 78 , 34)
# o = maximum(34  , 12 , 90)

# print(m)
# print(n)
# print(o)

print("The greatest of all three is: " + str(m))