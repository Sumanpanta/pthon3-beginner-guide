#indentation.py 

#Blocks of code

#4 space for Indentation

#if Else
#while
# for 


'''
if <condition>:
    <block of code>

else:
    <block of code>
'''    #three single quotes 

## syntax

# the condition has to evaluate to boolean
# the below block can contain any python code

'''
if <condition>:
    <block of code>
'''

## Example1
# Check whether the number given by user is even or odd

user_input = input("Enter the number: \n ~$ ")
user_input = int(user_input)

if user_input %2 == 0:              #if<condition>:   <block of code>
    print("The number is even")

if user_input %2 !=0:
    print("The number is odd")
    
if user_input<0:
    print("The number is negative")
    
    '''
    This is just a line of code that read by python in bulk:::only executed if print
    or other statement takes place ;like other code,it
    is seen by python: otherwise, this is just for documentation generation or 
    documentation purpose
    '''
