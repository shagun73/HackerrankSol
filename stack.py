import sys

input = list(map(int, input().strip().split(' ')))
result = []
flag = True

while(flag == True):
    if(len(input)):
        result.append(input.pop())
        # print(input.pop())
        input.pop()
    else:
        flag = False

    
for i in result:
    print(i, sep=' ', end=' ', flush=True)