#!/bin/python3

import os
import sys

def gradingStudents(grades):
    finalgrades = []
    for studentmark in grades[0:]:
        if studentmark > 37 and studentmark % 5 > 2:
            finalgrades.append(studentmark+(studentmark%5)-1)
        else:
            finalgrades.append(studentmark)
    #print(finalgrades)
    return finalgrades
            
        

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
