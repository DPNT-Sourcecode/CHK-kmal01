

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    items = {}
    special = {}
    price = {'A': 50, 'B':30, 'C':20, 'D': 15, 'E':40, 'F':10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':70, 'L':90, 'M':15, 'N':40, 'O':10, 'P': 50, 'Q':30, 'R':50, 'S':20, 'T':20, 'U':40, 'V':50, 'W':20, 'X':17, 'Y':20, 'Z':21}

    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        items[char] = 0
        special[char] = 0

    for char in skus:

        if not char in items:
            return -1

        items[char] += 1
    
    while items['A'] >= 3:
        if items['A'] >= 5:
            special['A'] += 200
            items['A'] -= 5
        else:
            special['A'] += 130
            items['A'] -= 3

    while items['E'] >= 2 and items['B'] > 0:
        special['E'] += 80
        items['E'] -= 2
        items['B'] -= 1

    while items['B'] >= 2:
        special['B'] += 45
        items['B'] -= 2

    while items['F'] >= 3:
        special['F'] += 20
        items['F'] -= 3

    while items['H'] >= 5:
        if items['H'] >= 10:
            items['H'] -= 10
            special['H'] += 80
        else:
            items['H'] -= 5
            special['H'] += 45

    while items['K'] >= 2:
        special['K'] += 120
        items['K'] -= 2
    
    while items['N'] >= 3 and items['M'] >= 1:
        special['N'] += 120
        items['N'] -= 3
        items['M'] -= 1

    while items['P'] >= 5:
        special['P'] += 200
        items['P'] -= 5

    while items['R'] >= 3 and items['Q'] >= 1:
        special['R'] += 150
        items['R'] -= 3
        items['Q'] -= 1

    while items['Q'] >= 3:
        special['Q'] += 80
        items['Q'] -= 3

    while items['V'] >= 2:
        if items['V'] >= 3:
            items['V'] -= 3
            special['V'] += 130
        else:
            items['V'] -= 2
            special['V'] += 90 

    while items['U'] >= 4:
        special['U'] += 120
        items['U'] -= 4  
    
    group_sum = 0
    while items['S'] + items['T'] + items['X'] + items['Y'] + items['Z'] >= 3:
        group_sum += 45
        remove_items_num = 3
        for char in 'ZSTYX':
            while items[char] > 0 and remove_items_num > 0:
                items[char] -= 1
                remove_items_num -= 1

    special_sum = 0
    for char in special:
        special_sum += special[char]

    usual_sum = 0
    for char in items:
        usual_sum += items[char] * price[char]

    return group_sum + usual_sum + special_sum
