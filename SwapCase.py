def swap_case(s):
    count_str = len(s)
    modified_str = ''
    for i in range(count_str):
        if s[i].isupper():
            a = s[i].lower()
        elif s[i].islower():
            a = s[i].upper()
        else:
            a = s[i]
        modified_str = modified_str + a
    return modified_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

