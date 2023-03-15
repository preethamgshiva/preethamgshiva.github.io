import re

# Define a regular expression pattern to match the date in the URL
pattern = r'\d{4}/\d{2}/\d{2}'

# Example URL
url = 'https://example.com/2023/03/15/some-page.html'

# Find the date in the URL using the regular expression pattern
match = re.search(pattern, url)

# If a match is found, extract the year, month, and date
if match:
    date_str = match.group()
    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    print("Year: ", year)
    print("Month: ", month)
    print("Day: ", day)
else:
    print("No date found in URL.")
