 #typecasting : converting any datatype into another (eg: int to str, str to int etc.)
 #string -> integer 
 
 #not all the strings can be converted into integer, only some valid decimal can be the converted
 
score_of_english = "90"
score_of_programming = "100"
score_of_mathematics = "95"
 
# lets convert strings into integer
#int :: built-in-function (datatype)

score_of_english = int(score_of_english)
scortypee_of_mathematics = int(score_of_mathematics)
score_of_programming = int(score_of_programming)

#calculate total score
total_score = (score_of_english + score_of_english + score_of_programming)

print(total_score)

#calculate average score
average_score = (total_score/3)
print(average_score)


 