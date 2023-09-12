'''
Day 2
1. If else elif statements
Leap year :
The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.

2. Scores grade.
if 
    score < 60 fail
    score >= 60 and score < 70 D
    score >= 70 and score < 80 C
    score >= 80 and score < 90 B
    score >= 90 and score < 100 A
'''

# year = int(input("Input year :"))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
#     print("Leap Year")
# else :
#     print("Not leap year")



# score = 0
# total_score = 0
# student_count = 0
# score_array = [0,0,0,0,0]

# while score  >= 0 :
#     score = int(input("Input scores :"))
#     if score > 100 or score < 0:
#         if score < 0 :
#             break
#         print("Please input score between 0 - 100")
#         continue
#     total_score += score
#     student_count += 1
#     if (score < 60) :
#         score_array[0] += 1
#     elif (score >= 60 and score < 70) :
#         score_array[1] += 1
#     elif (score >= 70 and score < 80) :
#         score_array[2] += 1
#     elif (score >= 80 and score < 90) :
#         score_array[3] += 1
#     else :
#         score_array[4] += 1

# print(f'The total score is : {total_score}')
# print(f'The total score is : {student_count}')
# print (f'''
#         Total student who got F : {score_array[0]}
#         Total student who got D : {score_array[1]}
#         Total student who got C : {score_array[2]}
#         Total student who got B : {score_array[3]}
#         Total student who got A : {score_array[4]}
#        ''')
# average_score = total_score/student_count
# print(f'The average score is : {average_score}\n')

'''
Automate scores using random
'''

import random

score = 0
total_score = 0
student_count = 0
score_array = [0,0,0,0,0]

for i in range(10):  # let's say we want to generate and process 10 scores
    score = random.randint(0, 100)
    total_score += score
    student_count += 1
    if (score < 60) :
        score_array[0] += 1
    elif (score >= 60 and score < 70) :
        score_array[1] += 1
    elif (score >= 70 and score < 80) :
        score_array[2] += 1
    elif (score >= 80 and score < 90) :
        score_array[3] += 1
    else :
        score_array[4] += 1

print(f'The total score is : {total_score}')
print(f'The total score is : {student_count}')
print (f'''
        Total student who got F : {score_array[0]}
        Total student who got D : {score_array[1]}
        Total student who got C : {score_array[2]}
        Total student who got B : {score_array[3]}
        Total student who got A : {score_array[4]}
       ''')
average_score = total_score/student_count
print(f'The average score is : {average_score}\n')