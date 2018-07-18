# Given an array of n integers and a number, d , perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.


def array_left_rotation(a, n, k):
    if k%n == 0:
        a = a
    else:        
        x = 0
        while x < k:
            temp = a[0]
            for i in range(0,n-1):            
                a[i] = a[i+1]
            a[n-1] = temp   
            x += 1 
    return a  

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

            