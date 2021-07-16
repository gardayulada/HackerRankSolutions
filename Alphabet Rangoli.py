def print_rangoli(n):
    height = (n*2)-1
    width = ((n-1)*2*2)+1
    half_width = (width+1)/2
    max_alpha_char = 96+n
    min_alpha_char = 97
    dash = '-'
    h = 1
    while h <= n-1:
        w = 1
        count_alpha = h - 1
        alpha_reduction = 0
        alpha_increment = 0
        string = ''
        while w <= half_width-1-(count_alpha*2):
            string += dash
            w += 1
        while (w > half_width-1-(count_alpha*2)) and (w < half_width):
            string = string + chr(max_alpha_char-alpha_reduction) + '-'
            alpha_reduction += 1
            w += 2
        while w == half_width:
            string += chr(max_alpha_char-alpha_reduction)
            w += 1
        while (w > half_width) and (w < half_width+1+(count_alpha*2)):
            alpha_increment += 1
            string = string + '-' + chr(max_alpha_char-alpha_reduction+alpha_increment)
            w += 2
        while (w >= half_width+1+(count_alpha*2)) and (w <= width):
            string += dash
            w += 1
        print(string)
        h += 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)