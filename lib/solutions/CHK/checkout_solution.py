

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    items = {}

    for char in 'ABCDEFGHIKLMNOPQRSTVXYZ':
        items[char] = 0

    for char in skus:

        if not char in items:
            return -1

        items[char] += 1
    
    specialA = 0
    while items['A'] >= 3:
        if items['A'] >= 5:
            specialA += 200
            items['A'] -= 5
        else:
            specialA += 130
            items['A'] -= 3


    specialE = 0
    while items['E'] >= 2 and items['B'] > 0:
        specialE += 80
        items['E'] -= 2
        items['B'] -= 1

    specialB = 0
    while items['B'] >= 2:
        specialB += 45
        items['B'] -= 2

    specialF = 0
    while items['F'] >= 3:
        specialF += 20
        items['F'] -= 3


    total_sum = specialF + specialA + specialB + specialE + items['A']*50 + items['B'] * 30 + items['C'] * 20 + items['D'] * 15 + items['E'] * 40 + items['F'] * 10

    return total_sum
