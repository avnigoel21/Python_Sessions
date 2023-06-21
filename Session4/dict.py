#dictionary =  key-value pair


#It is mutable
#It is indexed
# cannot contain duplicate values


myDict = {
    "Fast" : "In a quick manner" , 
    "Aditi" : "A coder",
    "Marks" : [1 , 3, 5] , 
    "anotherDict" : {"Aditi" : "Player"},
    "Aditi" : "A dancer", # override the previous value
}

# print(myDict['Fast'])
# print(myDict['Aditi'])
# # print(myDict['Marks'])
# print(myDict['anotherDict']["Aditi"])

# print(myDict)

# print(myDict.keys()) # print the keys of the dictionary
# print(type(myDict.keys())) # checking the type 

# print(list(myDict.keys())) # print the keys of the dictionary in list (typecasting from dict_keys to list)

# print(myDict.values()) # print the values of the dictionary 
# print(type(myDict.values())) # checking the type



#Dictionary methods/functions
# print(myDict.items()) # prints the (key, value) for all contents of the dictionary
# print(type(myDict.items()))
# print(myDict)
# print(type(myDict))

# updateDict = {
#     "Rohan" : "friend" ,
#     "Smriti" : "friend"
# }

# myDict.update(updateDict) # updates the mydict 
# print(myDict)

# print(myDict['Fasst']) # throws an error as Fasst is not present in the dict 
# print(myDict.get("Fasst")) # returns none as Fasst is not present in the dict 