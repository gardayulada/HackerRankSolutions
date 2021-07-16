A = [9,13,12]

prev, diff = -1, 10 ** 9
A.sort()
for a in A:
    if prev != -1:
        diff = min(diff, abs(a - prev))
    prev = a
print(diff)