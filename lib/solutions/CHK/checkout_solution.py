

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    items = {}
    price = {'A': 50, 'B':30, 'C':20, 'D': 15, 'E':40, 'F':10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P': 50, 'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90, 'Y':10, 'Z':50}

    for char in 'ABCDEFGHIJKLMNOPQRSTVXYZ':
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

    special_sum = specialF + specialA + specialB + specialE

    usual_sum = 0
    for char in items:
        usual_sum += items[char] * price[char]

    return usual_sum + special_sum
