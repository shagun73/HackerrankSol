
# Write your code here
import sys
testcases = int(input())
numbers = [int(x) for x in input().split()]
#for i in range(1,testcases):
for num in numbers:
    for j in range(1,num+1):
        if j%3 == 0:
            if j%5 ==0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif j%5 == 0:
            print("Buzz")
        else: print(j)
#print(testcases,type(numbers))
