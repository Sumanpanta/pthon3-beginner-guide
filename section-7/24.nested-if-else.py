
#Creating scenerio for ecommerce site 

##Domain: Ecomm.

##Calculate discount

##electronic clothing/other

prompt_category = '''                        #As I said earlier the code is first seen by python intrepeter

Please choose the product: \n
1. Electronics | Press-1 \n
2. Furniture | Press-2 \n
3. Clothing | Press-3 \n
4. Other | Press-4 \n
>>>>
'''

product = int(input(prompt_category))

prompt_location = '''
Please choose the location for product to deliver:
1. Nepal | Press-1 \n
2. India | Press-2 \n
3. America | Press-3 \n 
>>>>
 '''
 
location = int(input(prompt_location))
#print(location)    this is just for testing purpose
#print(product)     "                 "


if product ==1:
    if location ==1:                 #For Nepal's location
        discount = 30
    elif location ==2:               #For India's location
        discount = 20
    else:
        discount = 10
        
elif product ==2:
    if location == 1:
        discount = 25
    elif location == 2:
        discount = 15
    else: 
        discount = 5
        
elif product == 3:
    if location == 1:
        discount = 22
    elif location == 2:
        discount = 12 
    else:
        discount = 7

else: 
    discount = 2
    

print("Applicable Discount for product is :",discount)

#learn it carefully to know all about other simple-if, if-else,if-elif-else etc.
        