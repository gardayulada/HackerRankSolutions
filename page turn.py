n = 96993
p = 70030

if n % 2 == 0:
    mid_val = n/2
    if p > mid_val:
        turn_from = 'back'
    else:
        turn_from = 'front'
else:
    mid_val = (n+1)/2
    if p >= mid_val:
        turn_from = 'back'
    else:
        turn_from = 'front'
if turn_from == 'front':
    page_turn = 0
    i = 1
    while i < p:
        i += 2
        page_turn += 1
        if p <= i:
            break
        else:
            continue
else:
    page_turn = 0
    i = n
    if n % 2 == 0:
        while i > p:
            i -= 2
            page_turn += 1
            if i <= p:
                break
            else:
                continue
    else:
        if p == i-1:
            page_turn = 0
        else:
            while i > p:
                i -= 2
                page_turn += 1
                if i <= p:
                    break
                else:
                    continue
print(page_turn)