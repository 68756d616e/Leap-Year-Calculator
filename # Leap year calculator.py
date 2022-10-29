# Leap year calculator
# Discover when there will be a leap year

# You input a integer year below
year = int(input("Please enter a year: "))
# the input year, if the remainder is greater than 0, then move onto the next if functions.
# Example : input 9 ; 4 + 4 + 1 = 9, there is a remainder 1, which will return, not a leap year. 0 would dictate a move onto the next if function
# The below dictates if any of the outcomes below are greater than 0, you move onto the next statement until you reach a conclusion where it is == 0
# There may be one issue, if the year % 4 is = 0, and the year % 100 is > that 0, it should return a "Leap Year"
if year % 4 > 0:
  print("This is not a leap year")
  if year % 4 == 0:
    if year % 100 > 0:
      print("This is not a leap year")
      if year % 100 > 0:
        if year % 400 == 0:
          print("This is not a leap year")
else:
  print("This is a leap year")

# Alternative method

# if year % 4 == 0:
#  if year % 100 == 0:
#   if year % 400 -- 0:
#     print("this is a leap year")
#   else:
#     print("This is not a leap year!") 
#  else:
#   print("This is a leap year!") 
# else:
#  print("Not a leap year") 