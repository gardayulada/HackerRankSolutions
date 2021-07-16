import re

N = int(input())
for i in range(N):
    line = input()
    if re.search(r'\s[{]', line):
        continue
    else:
        line_list = re.findall(r'(?<=#)([0-9a-fA-F]{3}|[0-9a-fA-F]{6})[^0-9a-fA-F]', line)
        j = 0
        while j < len(line_list):
            print('#'+line_list[j])
            j += 1
