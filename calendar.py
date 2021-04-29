#it shows the complete days and months of a desired year

#first import a calendar module or package
import calendar 

#asking the user to give the input that should be a valid calendar year number 
year_number = int(input("enter the year number to show the complete calendar"))
display = calendar.calendar(year_number)

#displaying the complete desired year calendar
print(display)
