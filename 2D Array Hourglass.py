arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

def hourGlass(arr):
    li_sum = []
    i = 0
    sum_hourglass = 0
    while i < 4:
        k = i + 2
        j = 0
        while j < 4:
            l = j + 2
            sum_hourglass += arr[i][j]
            j += 1
        i += 1
    return result

result = hourGlass(arr)
print(result)