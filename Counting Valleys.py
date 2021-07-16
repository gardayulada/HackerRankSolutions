steps = 8
path = 'UDDDUDUU'

valleys_count = 0
incline_lvl = 0
for i in path:
    if incline_lvl == 0 and i == 'D':
        valleys_count += 1
    if i == 'D':
        incline_lvl -= 1
    else:
        incline_lvl += 1

print(valleys_count)