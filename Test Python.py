N = -5228

str_n = str(N)
len_digit = len(str_n)
if str_n[0] == '-':
    if int(str_n[1]) > 5:
        str_result = str_n[0] + '5' + str_n[1:]
    else:
        i = 2
        while i < len_digit:
            if int(str_n[i]) > 5:
                str_result = str_n[:i] + '5' + str_n[i:]
                break
            elif i == len_digit - 1:
                str_result = str_n + '5'
            else:
                pass
            i += 1
else:
    if int(str_n[0]) < 5:
        str_result = '5' + str_n
    else:
        i = 1
        while i < len_digit:
            if int(str_n[i]) < 5:
                str_result = str_n[:i] + '5' + str_n[i:]
                break
            elif i == len_digit -1:
                str_result = str_n + '5'
            else:
                pass
            i += 1
print(int(str_result))