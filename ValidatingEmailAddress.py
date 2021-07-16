import re

N = int(input())
for i in range(N):
    str_input = input()
    modified_str = re.sub('>', '', re.sub('<', '', str_input))
    tuple_str = tuple(modified_str.split())
    email_address = tuple_str[1]
    email_user = re.search(r'\A(?=[a-zA-Z])(\w|[.]|-)*(?=@[a-zA-Z])', email_address)
    email_domain = re.search(r'(?<=@)[a-zA-Z]+(?=[.]([a-zA-Z]|[a-zA-Z]{2}|[a-zA-Z]{3})\Z)', email_address)
    email_ext = re.search(r'(?<=[.])([a-zA-Z]|[a-zA-Z]{2}|[a-zA-Z]{3})\Z', email_address)
    if email_user and email_domain and email_ext:
        print(str_input)

