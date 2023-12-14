#reserved keywords : special keyword having special meaning, 
# built-in keywords for special purpose

#to list all the keywords to avoid confusion: you have to do 

import keyword
print(keyword.kwlist)



#18. built-in functions in python are used as we import modules
#how do we know which fxn are built-in : by using some methods called

#fxn called as dir then, we  can name the module inside __
dir(__builtins__)

#to show in output use print(dir(__builtins__))

#built-in are all available to you by default and don't have to import it anywhere 
#you can use freely some builtin includes: vars,print,tuple, type, zip etc 

#type "python" in terminal and type dir(__builtins__) and "Enter" to see all of it 
print("This don't have to be imported ")
