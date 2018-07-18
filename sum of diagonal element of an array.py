##calculate the sum of diagonal elementsof an aray/matrix

def diagsum(arr):
    summ = 0
    return sum([summ + arr[i][i] for i in range(len(arr))])
arr = [[2,5,1],[2,3,6],[8,5,4]] 
diagsum(arr)