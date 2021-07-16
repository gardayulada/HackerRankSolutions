x = 1
y = 7
z = 4

if abs(x-z) < abs(y-z):
    result = 'Cat A'
elif abs(y-z) < abs(x-z):
    result = 'Cat B'
else:
    result = 'Mouse C'

print(result)