def check_element_in_tuple(element, tup):
    if element in tup:
        return True
    else:
        return False
tup = (1, 2, 3, 4, 5)
element1 = 3
element2 = 6
print(check_element_in_tuple(element1, tup)) # Output: True
print(check_element_in_tuple(element2, tup)) # Output: False
