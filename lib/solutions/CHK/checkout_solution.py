

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    items = {'A': 0, 'B': 0, 'C': 0, 'D':0, 'E': 0}
    for char in skus:

        if char != 'A' and char != 'B' and char != 'C' and char != 'D' and char != 'E':
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
    while items['E'] >= 2:
        specialE += 40
        items['E'] -= 2
        items['B'] -= 1

    specialB = 0
    while items['B'] >= 2:
        specialB += 45
        items['B'] -= 2


    total_sum = specialA + specialB + specialE + items['A']*50 + items['B'] * 30 + items['C'] * 20 + items['D'] * 15 + items['E'] * 40

    return total_sum
