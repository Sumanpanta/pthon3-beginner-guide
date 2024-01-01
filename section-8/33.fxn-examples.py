 
#lets talk more about function with example
'''
    Params: define the value expected by the fxn
    Args: Represent the actual values which are passed
'''

def rectangle_area_perimeter(length, breadth):
    '''
    Calculate the area and perimeter of the rectangle
    '''
    area = length * breadth
    perimeter = 2 *(length * breadth)
    return area, perimeter

#Now calling the fxn
area, perimeter = rectangle_area_perimeter(40,30)  #yeta (area,perimeter = )j lekhyo print garda tei print garda pass garnu parxa
print(f"Area of rectangle:{area} and perimeter of rectangle:{perimeter}")


#Example 2 : show how the built-in fxn can be used inside fxn

def average(list_of_all_number):
    '''
    average from all the elements present in list
    '''
    return sum(list_of_all_number) // len(list_of_all_number)  #sum, len etc are built-in fxn(fxn return parameter)

print(float(average([1,2,3,4,5])))  