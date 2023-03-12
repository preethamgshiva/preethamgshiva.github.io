def count_this_these(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    # Count the occurrences of "this" and "these"
    count_this = text.count('this')
    count_these = text.count('these')
    
    # Return the results as a tuple
    return count_this, count_these
filename = 'my_text_file.txt'
count_this, count_these = count_this_these(filename)
print(f'The word "this" appears {count_this} times and "these" appears {count_these} times in {filename}.')
