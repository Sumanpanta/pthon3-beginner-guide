#dates and times in python 
#for various functions, we can import various modules there 
# are various libraries for importing 

from datetime import datetime    #standard library, we can use certain fxn by importing 
#it: to avoid confusion or anyother things, we use from datetime: import "datetime"
from datetime import timedelta    #for line 33
from datetime import date

#Current date and time 
current_datetime = datetime.now()

print(f'The current datetime is {current_datetime}')   # then pass current_datetime to show oput in {}


#Dispaly date and time in different format
print(f'Current date: {current_datetime.date()}')   #showing todays date

print(f'Current time according to local machine:{current_datetime.time()}')



#Format the date and time //strf stands for formatted date and time///inside ofit, 
#we have to pass certain arguments 

print(f'formatted DateTime:{current_datetime.strftime("%m-%Y-%d %H:%M:%S")}') 
#single quotation,so double should be inside: same quotn shows errors 

#Get weekday of the week 
week_day = current_datetime.strftime('%A')   #you can find about all symbl in documetation
print(f'Weekday:{week_day}')

#Adding and Subtracting Time durations      //delta means differences
delta = timedelta(days=1)       #can use directly: instead datetime.timedelta(day = 1)after importing
# days ko tham ma days lekheni error so should pass right arguments 
one_day_ahead_in_future = current_datetime + delta
print(f'One day in future:{one_day_ahead_in_future}')  #for this we've to use import fxn, from..imp. timedelta



#One day in Past 
one_day_in_past = current_datetime - delta 
print(f'one day in past is: {one_day_in_past}')

#Specific date creation 
#for this we have to import date, in first line, 
specific_date = date(2023, 12, 26)      #only importing remove warning in code 
print(f'the specific date: {specific_date}')   


#there are so many fxns you can experiment all of them
#for using fxn about dateTime,we have to use (from datetime) module(always remember)






