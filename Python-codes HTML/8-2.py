import re
#check that a string contains only a certain set of characters
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)
print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))


#matches a string that has an a followed by zero or more b's
def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
# find sequences of lowercase letters joined with a underscore.
def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))


# find the sequences of one upper case letter followed by lower case letters.
def text_match(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))


# to match a string that contains only upper and lowercase letters, numbers,and underscores.
def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))


#search for a literal string in a string and also find the location within the original string where the pattern occurs
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
if re.search(pattern, text):
    print('Matched!')
else:
    print('Not Matched!')