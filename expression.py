import sys

input = list(map(str, input().strip().split(' ')))

symbolStack = []
digitStack = []


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    
    return False

for i in range(len(input)):
    if(is_number(input[i])):
        digitStack.append(int(input[i]))
    else:
        symbolStack.append(input[i])

digitStack.reverse()

while(len(digitStack) != 1):
    op = symbolStack.pop()
    input1 = digitStack.pop()
    input2 = digitStack.pop()
    
    if op == "+":
        digitStack.append(input1 + input2)
    elif op == "*":
        digitStack.append(input1 * input2)
    elif op == "/":
        digitStack.append(input1 / input2)
    else:
        print("Wrong input")
        exit()

print(digitStack[0])