#In other programming language, its if elseif and else:
# but in this programming language: its if elif and else: (also pronouns as elseif)

'''
if condition:
    <block of code>
elif condition:
    <block of code>
else:
    <block of code>
    '''
    
#its just a simple example to find positive, negative and zero

user_input = input("Enter the number \n ~$")
user_input = int(user_input)

if user_input == 0:
    print("The number is zero")
elif user_input > 0:
    print("The entered numbered is positive")
    
else:
    print("The entered number is negative")
    
    