import re

N = int(input())
for i in range(N):
    some_input = input()
    float_num = re.findall(r'(^[.][0-9]+$)|(^([+]|-)[.][0-9]+$)|(^([+]|-)[0-9]+[.][0-9]+$)|'
                           r'(^[0-9]+[.][0-9]+$)', some_input)
    if len(float_num) > 0:
        print(True)
    else:
        print(False)
