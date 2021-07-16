import re

user_input = input()
split_input = re.split(r'([.]|[,])+', user_input)
split_list = [x for x in split_input if x != ',' and x != '.']
for i in split_list:
    print(i)

