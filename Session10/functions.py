# function creation
def percent(marks): 
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400) * 100



marks1 = [56 , 23 , 78  , 12]
#percentage1 = (sum(marks1)/400)* 100
# percentage1 = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400) * 100
percentage1 = percent(marks1)  # function calling


marks2 = [54 , 12 , 34 , 14]
#percentage2 = (sum(marks2)/400)* 100
percentage2  = percent(marks2)

print(percentage1 , percentage2)




# Two types of functions
# 1) Built in functions - example - sum() , print() , range()
# 2) User defined functions