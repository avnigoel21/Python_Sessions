#Sets store non - repetitive elements

#sets are unordered
#sets are unindexed
#sets are immutable


# a = {1 , 5 , 8 , 6 }

# print(a)
# print(type(a))


#Imp : this syntax will create an empty dictionary and not an empty set
# b = {}
# print(type(b))


# An  empty set can be created using the below syntax
c = set()
# print(c)
# print(type(c))


# Adding values to an empty set
c.add(5)
c.add(4)
c.add(5) # Adding a value repeatedly does not change a set
c.add(5)
c.add(5)

c.add((2, 5, 7)) # can add a tuple to a set

# c.add({4:5}) # cannot add list or dictionary to sets


print(c)

# SETS METHODS/FUNCTIONS

# print(len(c)) # prints length of this set

# c.remove(5) # removes 5 from set c
# print(c)
# c.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
# print(c)

# c.pop() # removes an arbitary element from the set and returns the element removed
# print(c)

# c.clear() # empties the set
# print(c)




