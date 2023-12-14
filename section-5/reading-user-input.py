#calculate volume and surface of the spare

PI = 3.14

# input radius is the string
input_radius = input("Enter the radius of the spare: \n ~$ ")

#performing typeCasting
radius = float(input_radius)

#calculate the surface area
surface_area = 4*PI*radius**2

#calculate the volume 
volume = (4/3) * PI * radius **3        #4/3*pi*r3 garda yesari lekhni ho hai

#print the surface area of the spare  f= formatted strings (feature in python:allow us
# to pass  variable in strings ),so

print(f'The surface area of spare is: {surface_area} ')

print(f'The volume of the spare is {volume}')


 