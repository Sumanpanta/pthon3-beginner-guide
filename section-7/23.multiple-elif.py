#here we will understand multiple elif through example
#lets calculate the grade of the students based on the marks gain in a subject 

obtain_marks = int(input("Enter the marks obtained \n ~$"))

if obtain_marks >=90:
    grade = 'A'

elif obtain_marks >= 80:
    grade = 'B'

elif obtain_marks >= 70:
    grade = 'C'

elif obtain_marks >= 50:
    grade = 'D'


else:
    grade = 'E'
    
print("The obtained grade is: ",grade)  #you can use both double and single quotes: sane like other

