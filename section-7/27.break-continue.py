#let's talk about break and continue uses in loops 
#using "break" makes one step jump or break while using loop
#using "continue" makes all continious from same step without jumping or breaking loop step


#break
#continue
# Used with loop 

#Example 1 
# lets take the example for infinity loop without break

# infinity = "Suman"
# while True:
#     print(infinity)


while True:
    print("infinity")
    break               #jumps ahead;print one line and then breaks
                        #the code(flow) will jump out of while loop

print("Out of the loop")



#continue: you don't have to go outside of the loop, 
# but you have to go to next interation in loop itself
#(tei loop ko next iteration ma jani, loop vanda bahira jump garni haina continue vaneko cahie)

counter = 0
while counter < 10:
    counter +=1        #yo increment
    if counter <=5:      #counter 5 jatti wa 5 vanda tala vayo vani print gara otherwise continue
        print(counter)
    continue

print("This one is out of loop ")

#you can make many scenerio as possible to relate your programming and understand easily
####Real scenerio (Example) Of ATM machine (user taking out cash)
#try to make as simple as possible

attempts = 0
MAX_ATTEMPTS = 4
correct_pin = '4321'

while attempts < MAX_ATTEMPTS:
    user_ko_pin = input("Enter your pin \n ~$")
    
    if not user_ko_pin:
        print("You did not enter the pin.Please enter your pin")
        continue
    if user_ko_pin == correct_pin:
        print("Please wait while we process request for you")
        break 
    
    else:
        attempts +=1
        print(f"Incorrect pin.{MAX_ATTEMPTS-attempts } attempts remaining:") #formatted string necesy {} ko lage

if attempts == MAX_ATTEMPTS:
    print("Too many attempts. Card Blocked!!!!")
    
print(f"Thanks for using Demo ATM ")
