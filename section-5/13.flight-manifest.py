#showing example for operation by using flight_manifest this is example 13 call operation

manifest = 'Flight: JPILU99 | Destination: America | Passenger: 120'

#Strings are immutable   //not changable if changed variable, we get error 
#manifest[0] = 'D'   # this showing error in output because manifest(string) 
# having 0 index is already assigned ie with 'F'

print(manifest[0])   #showing F at index 0
#other indexing 
print(manifest[8])


#slicing : print the given string from given starting point to a given ending point 

print(manifest[6:15])  #starting point 6 and ending point 15 

#concatenation: we can add more to the string (joining one with other using +)

gate = '| Gate: 12 '
manifest += gate 
print(manifest)

#length function 
total_chars = len(manifest)
print(f'The total character in manifest is: {total_chars}')

#membership : allow us to check whether the sub-string(character in string ) are 
# present in string or not 

print('JPILU99' in manifest)

print('JPIHU' in manifest)

#Replication : we can replicate the string , following by the times (how many time to replicate)
print(manifest*3)












 





