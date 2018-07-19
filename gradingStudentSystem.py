#!/bin/python3

import os
import sys
finalgrade=[]
def gradingStudents(grades):
    for grade in grades[0:]:
        if grade >= 38:
            if grade % 5 > 2:
                grade += 5 - (grade % 5)
                finalgrade.append(grade)
            else: 
                finalgrade.append(grade)
        else:
            finalgrade.append(grade)
    return finalgrade

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
