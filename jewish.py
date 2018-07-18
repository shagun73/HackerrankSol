import sys

total, num = map(int, input().strip().split(','))

resultArr = []
peopleArr = [0] * total

for i in range(total):
    peopleArr[i] = i

val = 0

while total != 0:
    val = (val + num - 1) % total
    resultArr.append(peopleArr[val])
    del peopleArr[val]
    total = len(peopleArr)
    
for i in resultArr:
    print(i, sep=' ', end=' ', flush=True)