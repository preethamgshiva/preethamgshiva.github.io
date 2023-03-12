import re
from collections import Counter
def most_repeated_words(filename):
    # Open the file and read the text
    with open(filename, 'r') as file:
        text = file.read()

    # Find all words in the text and count their occurrences
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    # Return the 10 most common words
    return word_counts.most_common(10)

# Call the function and print the results
result = most_repeated_words('input.txt')
print('The 10 most repeated words are:')
for word, count in result:
    print(f'{word}: {count} times')