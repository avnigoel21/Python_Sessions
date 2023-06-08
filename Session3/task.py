#WRITE A PROGRAM to fill in a letter template given below with name and date

letter = "Dear |<NAME>|\n\tYOU ARE SELECTED! \n|<DATE>|"

name = input("Enter your name: ")
date = input("Enter Date : ")

letter = letter.replace("|<NAME>|" , name)
letter = letter.replace("|<DATE>|" , date)

print(letter)