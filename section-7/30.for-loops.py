#this is used in scenerio where we know how many time we iterate how many times to increament etc

#before going to for loop lets talk about "range" in interpreter range(1,10)
#range starts at 0 and ends at n-1
#then listing range through "list(range(1,15))" ;count from 0 provide n-1 as last

## starting and ending with passing how much steps  to jump in single iteration: list(range(1,30,3)) 
#Iterable is an object, that one can iterate over. It generates an Iterator when passed to iter() method. An iterator is an object, which is used to iterate over an iterable object using the __next__() method. Iterators have the __next__() method, which returns the next item of the object.

#Note: Every iterator is also an iterable, but not every iterable is an iterator in Python.
# For example, a list is iterable but a list is not an iterator. 
# An iterator can be created from an iterable by using the function iter(). 
# To make this possible, the class of an object needs either a method __iter__, 
# which returns an iterator, or a __getitem__ method with sequential indexes starting with 0.

'''
What is an Iterable?

An Iterable is basically an object that any user can iterate over. 
We can generate an iterator when we pass the object to the iter() method.
What is an Iterator?

An Iterator is also an object that helps a user in iterating over another object (that is iterable).
We use the __next__() method for iterating. 
This method helps iterators return the next item available from the object
'''

'''
for <iterator> in <iterable>:
    <block of code>
'''

#Example 1

# simple_number = [1,2,3,4,5,6,7,8,9]

# for iter in simple_number:
#     print(iter)
    

for iter in range(1,20,3):
    print(iter)
    
#Example 2
#time for nested for loop example

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:             #at first use one by one in  row and 
    for elem in row:           #pick up  element from row
        print(elem, end = '')        #end = custom separator in python only print upto this dont go other
    print()                            #have to write print() in same for loop alike 
                                    #  print one complete line: like matrix
                                    #move to next line then 
                                    #without print, all shown: 123456789
                                    #can always use break,continue: known as loop-control stment


#Example 3: showing break and continue

for number in range(10):
    if number ==4:
        break         # shows only upto 4 then break
    elif number ==2:
        continue      #don't show 2:continue means on the same iteration but don't jumps ahead or break
    print(number)     #elif kai tala rakhni: otherwise continue le garda print hudaina 
    

#Example 4: showing range fxn has one more params(step params):can be used in diff wys (last example)

num_list = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(num_list) -1,-1,-1):  #going towards negative direction form 10,9.. 
    print(num_list[i])                  #  (start from 0 so 0 vanda negative(talako)ligna paryo)
                                        
    
    

