#Can we have a set with 18(int) and "18"(str) as a value in it.

# s = {18 , "18" , 18.1}
# print(s)

#------------------------------------------------------------------------------------------------

# What will be the length of following set s. 
# s = set()

# s.add(20)
# s.add(20.0)
# s.add("20")

# print(s)
# print(len(s))

#----------------------------------------------------------------------------------------------------

#can you change the values inside a list which is contained in set s

# s = {8 , 7 , 12 , "aditi"  , [2 , 4 , 5]}

# no as list is stored in sets and sets are hashable i.e non updateable

#---------------------------------------------------------------------------------------------------------


# Create an empty dictionary
# Allow 4 friends to enter their favourte language as values and use keys as their names.
# Assume that the names are unique 


fav_lang = {}

a = input("Enter your favourite language Shubham :")
b = input("Enter your favourite language Ankit :")
c = input("Enter your favourite language Sonali :")
d = input("Enter your favourite language Harshita :")

fav_lang['Shubham'] = a
fav_lang['Ankit'] = b
fav_lang['Sonali'] = c
fav_lang['Ankit'] = d

print(fav_lang)



