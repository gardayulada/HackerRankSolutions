s = [[4,5,8], [2,4,1], [1,9,7]]
s = [[4,9,2],[3,5,7],[8,1,5]]
s = [[1,3,8],[6,4,1],[2,6,5]]

if s[0][1] == 1:
    correct_s = [[6,1,8],[7,5,3],[2,9,4]]
    result = 0
    i = 0
    while i <= 2:
        j = 0
        while j <= 2:
            result += abs(s[i][j] - correct_s[i][j])
            j += 1
        i += 1
elif s[1][0] == 1:
    correct_s = [[8,3,4],[1,5,9],[6,7,2]]
    result = 0
    i = 0
    while i <= 2:
        j = 0
        while j <= 2:
            result += abs(s[i][j] - correct_s[i][j])
            j += 1
        i += 1
elif s[2][1] == 1:
    correct_s = [[4,9,2],[3,5,7],[8,1,6]]
    result = 0
    i = 0
    while i <= 2:
        j = 0
        while j <= 2:
            result += abs(s[i][j] - correct_s[i][j])
            j += 1
        i += 1
elif s[1][2] == 1:
    correct_s = [[2,7,6],[9,5,1],[4,3,8]]
    result = 0
    i = 0
    while i <= 2:
        j = 0
        while j <= 2:
            result += abs(s[i][j] - correct_s[i][j])
            j += 1
        i += 1

print(result)
