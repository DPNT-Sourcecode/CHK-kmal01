

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {'A': 0, 'B': 0, 'C': 0, 'D':0}
    for char in skus:
        items[char] += 1
    
    return items
