def find_repeated_items(tup):
    repeated_items = []
    for item in tup:
        if tup.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return tuple(repeated_items)

tup = (1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 4, 9)
repeated = find_repeated_items(tup)
print(repeated) # Output: (1, 2, 4)
