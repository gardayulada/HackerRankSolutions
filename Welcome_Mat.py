input_int = input().split()
N = int(input_int[0])
M = int(input_int[1])
dash = '-'
tiang = '.|.'
welc = 'WELCOME'
mid_N = (N+1)/2
h = 1
series = [i*2+1 for i in range(int((N-1)/2))]
while h < mid_N:
    string = ''
    mid_M = (M+1)/2
    w = 1
    while w < mid_M - 1 - 3 * (h-1):
        string += dash
        w += 1
    while w < mid_M + 1 + 3 * (h-1):
        string += tiang
        w += 3
    while w <= M:
        string += dash
        w += 1
    print(string)
    h += 1
string = ''
mid_M = (M+1)/2
w = 1
while w < mid_M - 3:
    string += dash
    w += 1
while w < mid_M + 3:
    string += welc
    w += 7
while w <= M:
    string += dash
    w += 1
print(string)
h += 1
series.sort(reverse=True)
series_el = 0
while h <= N:
    string = ''
    mid_M = (M+1)/2
    count_tiang = series[series_el]
    w = 1
    while w < mid_M - 1 - 3 * ((count_tiang-1)/2):
        string += dash
        w += 1
    while w < mid_M + 1 + 3 * ((count_tiang-1)/2):
        string += tiang
        w += 3
    while w <= M:
        string += dash
        w += 1
    print(string)
    series_el += 1
    h += 1
