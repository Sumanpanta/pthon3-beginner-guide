
'''
    1.Unit of reusable code
    2. They enhance readibility
    3. More maintainable code 
    
'''

"""
     Syntax of Functions in python
     
def<function name>( <parameters> 1,2,3 ....)
    '''
    Doc String: Describes why this function exists
    '''
    <block of code>
    
    return <expression>    #if a fxn is not returning anything explicitly 
                            #like in line 18, then we assume that fxn will by default return a none value  
    
"""


#Example 1: you can see def(which is keyword):and fxn name(greet()) 
        # and we don't pass any parameter inside it. we have call the fxn:
        # calling fxn is done simply by name of fxn along with opening and closing parenthesis. 
def greet():
   '''
       This functions greets the user.
   ''' 
   print("Hello, Welcome to the world of Python Programming:Have Fun!!")
   
#calling the fxn
greet() 




#Example 2:     fxn greet_user having parameter user; greeting is there so have to return greeting

def greet_user(user):
    '''
    This fxn accepts the name of the user, because we are passing parameter named "user"
         Return the greetings for the user.
    
    '''
    greeting = f'Hello, {user}!, Are you having fun in coding!!!?'
    return greeting
#the value we are returning is then assigned to this user_greeting

##now calling the function : j mn lagxa tei nam u_g = then print(u_g) or something else
user_greeting = greet_user("Madhav")
print(user_greeting)
    
   