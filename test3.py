A = [7,-1,3,2,1,-2,-3,-5]

li_a = list(set(A))
li_a2 = [[x,y] for x in li_a if x > 0 for y in li_a if y <0 if x == -y]
print(max(li_a2))