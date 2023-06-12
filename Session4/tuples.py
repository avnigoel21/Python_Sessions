# t = (1 , 3, 5, 2 , 6 , 1 , 1, 1, 2)
# print(t)
# print(t[0])

# Cannot update the values of a tuple
# t[0] = 2 
# print(t)

# t1 = () # Empty tuple

# t2 = (3) # Wrong way to declare  a tuple with single element
# t2 = (3 , ) # Tuple with single element
# print(t2)


#tuple functions/methods
t = (1 , 3, 5, 2 , 6 , 1 , 1, 1, 2)
print(t.count(1)) # count the number of 1's in this tuple
print(t.index(2)) # finding the index of element 2 only for first occourence