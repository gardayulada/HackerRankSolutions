b = 17
keyboards = [3,1,7,12,18]
drives = [5,2,8,9,12]

expense = 0
if len(keyboards) == 1 and len(drives) == 1:
    if keyboards[0] + drives[0] > b:
        expense = -1
    else:
        expense = keyboards[0] + drives[0]
else:
    for k in keyboards:
        for d in drives:
            if k + d >= expense:
                if k + d <= b:
                    expense = k + d
                else:
                    continue
            else:
                continue
if expense == 0:
    expense = -1
print(expense)
