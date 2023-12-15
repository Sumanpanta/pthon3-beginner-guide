#looping in looping, there are scenarios where we have to run a piece of code until
# again and again until some conditions are fulfilled,true or for some specified range
# , in this case, looping is used 
## while talking about control structures in pythons, looping is most important in some cases


#while loop 

#while loop is a loop construct; which runs a piece of code repeatedly as long as 
#certain condition is True or False 

#let's look at the syntax 
'''
while<condition>:
    <block of code>'''




#Example 1 :
provided_number = 1

while provided_number <=25:
    print("All number less than 26 is:",provided_number)
    provided_number = provided_number + 1
    
    
#Example 2:
multiple_of = 5
provided_number = 1

while provided_number <=20:
    print(provided_number*multiple_of)
    provided_number = provided_number + 1
        

