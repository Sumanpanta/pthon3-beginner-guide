
#lets talk about while loop along with else

'''
    while<condition>:
        <statements(block of code)>
    else:
        <statements(block of code)>
        
Else condition executes only when:
1. When the while conditon becomes flase
2. And when the loop didn't encounter any break     

    '''
    
    
#simple example 

counter = 1

while(counter<10):
    print(counter)
    counter+=1
    if counter == 6:
        break
else:
    print("All desired numbers have been shown")



    
